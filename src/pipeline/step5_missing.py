"""
Step 5 - Missing value indicators and imputation.

Indicators are created FIRST so the imputed value does not destroy the signal
that a value was originally absent.

Strategy by column (EDA Section 3):
  FLAG_NO_CAR              -> OWN_CAR_AGE missing = applicant has no car
  FLAG_NO_HOUSING_DATA     -> all BUILDING_MODE_COLS missing = no recorded building detail
  FLAG_EXT_SOURCE_*_MISSING -> score availability is uncertainty, not adverse evidence
  FLAG_SENTINEL_EMPLOYED   -> already created in step4

Imputation:
  Zero   : OWN_CAR_AGE, BUILDING_MODE_COLS (structural absence == zero)
  Median : numeric columns with MCAR/random missingness
  Mode   : NAME_TYPE_SUITE (categorical)
  "Unknown" fill : FONDKAPREMONT_MODE, HOUSETYPE_MODE, WALLSMATERIAL_MODE, EMERGENCYSTATE_MODE
  OCCUPATION_TYPE : mode within NAME_INCOME_TYPE group (group-mode imputation)
  EXT_SOURCE_1/2/3 : median model value after source copy and missing flag
  Aggregated table NaNs : applicants with no records -> 0 (absence = no activity)
"""
import numpy as np
import pandas as pd
from .config import (
    BUILDING_MODE_COLS,
    MEDIAN_IMPUTE_COLS,
    ZERO_IMPUTE_COLS,
    MODE_IMPUTE_COLS,
    CATEGORICAL_FILL_UNKNOWN,
)
from .utils import log, log_missing, log_shape

# Columns introduced by the five aggregated tables (step2).
# Absent rows = applicant had no records in that table -> fill with 0.
AGG_TABLE_COLS_PREFIX = [
    "BUREAU_", "BB_", "PREV_", "POS_", "INST_", "CC_",
]


def _is_agg_col(col: str) -> bool:
    return any(col.startswith(p) for p in AGG_TABLE_COLS_PREFIX)


def run(df: pd.DataFrame) -> pd.DataFrame:
    log("Step 5 - Missing value handling ...")
    df = df.copy()

    log_missing(df, "before imputation")

    # Missingness indicators
    df["FLAG_NO_CAR"] = df["OWN_CAR_AGE"].isna().astype(np.int8)

    housing_missing = df[BUILDING_MODE_COLS].isna().all(axis=1)
    df["FLAG_NO_HOUSING_DATA"] = housing_missing.astype(np.int8)
    log(f"  FLAG_NO_HOUSING_DATA=1: {housing_missing.sum():,}")

    # Preserve source score availability for record-level explanations.  The
    # model-facing values can be imputed, but a missing score must never be
    # described as if it were an observed weak score.
    for col in ["EXT_SOURCE_1", "EXT_SOURCE_2", "EXT_SOURCE_3"]:
        if col in df.columns:
            source_col = f"SOURCE_{col}"
            flag_col = f"FLAG_{col}_MISSING"
            df[source_col] = df[col]
            df[flag_col] = df[col].isna().astype(np.int8)
            log(f"  {flag_col}=1: {df[flag_col].sum():,}")

    # Zero imputation
    for col in ZERO_IMPUTE_COLS:
        if col in df.columns:
            n = df[col].isna().sum()
            df[col] = df[col].fillna(0)
            if n:
                log(f"  Zero-imputed {col}: {n:,} NaNs")

    # Median imputation
    for col in MEDIAN_IMPUTE_COLS + (["EXT_SOURCE_1"] if "EXT_SOURCE_1" in df.columns else []):
        if col in df.columns and df[col].isna().any():
            med = df[col].median()
            n = df[col].isna().sum()
            df[col] = df[col].fillna(med)
            log(f"  Median-imputed {col}: {n:,} NaNs -> {med:.4f}")

    # Mode imputation
    for col in MODE_IMPUTE_COLS:
        if col in df.columns and df[col].isna().any():
            mode_val = df[col].mode(dropna=True).iloc[0]
            n = df[col].isna().sum()
            df[col] = df[col].fillna(mode_val)
            log(f"  Mode-imputed {col}: {n:,} NaNs -> '{mode_val}'")

    # Categorical "Unknown" fill
    for col in CATEGORICAL_FILL_UNKNOWN:
        if col in df.columns and df[col].isna().any():
            n = df[col].isna().sum()
            df[col] = df[col].fillna("Unknown")
            log(f"  Unknown-filled {col}: {n:,} NaNs")

    # OCCUPATION_TYPE: group-mode imputation
    if "OCCUPATION_TYPE" in df.columns and df["OCCUPATION_TYPE"].isna().any():
        occ_mode = (
            df.dropna(subset=["OCCUPATION_TYPE"])
            .groupby("NAME_INCOME_TYPE")["OCCUPATION_TYPE"]
            .agg(lambda x: x.mode().iloc[0] if len(x) > 0 else np.nan)
        )
        mask = df["OCCUPATION_TYPE"].isna()
        df.loc[mask, "OCCUPATION_TYPE"] = df.loc[mask, "NAME_INCOME_TYPE"].map(occ_mode)
        # Any remaining (income type also had no occupation data)
        remaining_mode = df["OCCUPATION_TYPE"].mode(dropna=True).iloc[0]
        df["OCCUPATION_TYPE"] = df["OCCUPATION_TYPE"].fillna(remaining_mode)
        log(f"  OCCUPATION_TYPE group-mode imputed: {mask.sum():,} NaNs")

    # Aggregated table NaNs -> 0
    agg_cols = [c for c in df.columns if _is_agg_col(c)]
    agg_null_before = df[agg_cols].isna().sum().sum()
    df[agg_cols] = df[agg_cols].fillna(0)
    log(f"  Agg-table NaNs -> 0: {agg_null_before:,} cells")

    log_missing(df, "after imputation")
    log_shape("step5_out", df)
    return df

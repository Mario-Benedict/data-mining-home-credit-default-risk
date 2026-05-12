"""
Step 7 — Feature engineering, log transforms, and column pruning.

Derived features (EDA Section 7, 10):
  AGE_YEARS            = |DAYS_BIRTH| / 365
  YEARS_EMPLOYED_CLEAN = |DAYS_EMPLOYED| / 365   (NaN for sentinel rows)
  CREDIT_TO_INCOME     = AMT_CREDIT / AMT_INCOME_TOTAL
  ANNUITY_TO_INCOME    = AMT_ANNUITY / AMT_INCOME_TOTAL   (debt-service ratio)
  CREDIT_TERM_MONTHS   = AMT_CREDIT / AMT_ANNUITY         (implied loan term)
  GOODS_TO_CREDIT      = AMT_GOODS_PRICE / AMT_CREDIT     (LTV proxy)

DAYS_* conversion: stored as negative days before application date.
  Convert to positive years. Original columns then dropped.

Log transforms (after winsorizing in step6, before scaling in step9):
  AMT_INCOME_TOTAL, AMT_CREDIT, AMT_ANNUITY, AMT_GOODS_PRICE
  Use log1p to handle any residual zeros safely.

Column drops:
  _AVG / _MEDI building variants  (r > 0.99 with _MODE, EDA Section 7)
  OBS_60_CNT_SOCIAL_CIRCLE        (r = 0.998 with OBS_30)
  FLAG_EMP_PHONE                  (r = -1.0 with DAYS_EMPLOYED post-sentinel)
  FLAG_MOBIL                      (near-constant, all 1s)
  REGION_RATING_CLIENT            (r > 0.85 with REGION_RATING_CLIENT_W_CITY)
  SK_ID_CURR                      (identifier, not a feature)
  Original DAYS_* columns         (replaced by positive-year versions)
"""
import numpy as np
import pandas as pd
from .config import (
    COLS_DROP_AVG, COLS_DROP_MEDI, COLS_DROP_REDUNDANT,
    DAYS_COLS, LOG_TRANSFORM_COLS,
)
from .utils import log, log_shape

_DAYS_BUREAU_COLS = [
    "BUREAU_DAYS_CREDIT_MEAN", "BUREAU_DAYS_CREDIT_MAX", "BUREAU_DAYS_ENDDATE_MEAN",
]


def run(df: pd.DataFrame) -> pd.DataFrame:
    log("Step 7 — Feature engineering ...")
    df = df.copy()

    # ── DAYS_* → positive years ────────────────────────────────────────────
    for col in DAYS_COLS:
        if col not in df.columns:
            continue
        year_col = col.replace("DAYS_", "YEARS_")
        df[year_col] = np.abs(df[col]) / 365.0
        log(f"  {col} → {year_col}")

    # DAYS_EMPLOYED was NaN for sentinel rows after step4 — preserve NaN
    # The YEARS_EMPLOYED column will also be NaN for those rows (correct).

    # ── Derived ratio features ─────────────────────────────────────────────
    # Use post-winsorize AMT_INCOME_TOTAL (log not yet applied)
    df["CREDIT_TO_INCOME"] = df["AMT_CREDIT"] / df["AMT_INCOME_TOTAL"].replace(0, np.nan)
    df["ANNUITY_TO_INCOME"] = df["AMT_ANNUITY"] / df["AMT_INCOME_TOTAL"].replace(0, np.nan)
    df["CREDIT_TERM_MONTHS"] = df["AMT_CREDIT"] / df["AMT_ANNUITY"].replace(0, np.nan)
    df["GOODS_TO_CREDIT"] = df["AMT_GOODS_PRICE"] / df["AMT_CREDIT"].replace(0, np.nan)
    log("  Derived: CREDIT_TO_INCOME, ANNUITY_TO_INCOME, CREDIT_TERM_MONTHS, GOODS_TO_CREDIT")

    # ── Log transforms ─────────────────────────────────────────────────────
    for col in LOG_TRANSFORM_COLS:
        if col in df.columns:
            df[col] = np.log1p(df[col].clip(lower=0))
            log(f"  log1p({col})")

    # ── Drop redundant / near-constant / collinear columns ────────────────
    drop_cols = (
        COLS_DROP_AVG
        + COLS_DROP_MEDI
        + COLS_DROP_REDUNDANT
        + DAYS_COLS            # replaced by YEARS_* above
        + ["SK_ID_CURR"]
    )
    drop_cols = [c for c in drop_cols if c in df.columns]
    df = df.drop(columns=drop_cols)
    log(f"  Dropped {len(drop_cols)} redundant/ID columns")

    log_shape("step7_out", df)
    return df

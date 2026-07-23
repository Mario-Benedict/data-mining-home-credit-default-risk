"""
Structural cleaning: sentinel values, rare categories, column drops.

Order matters:
  1. DAYS_EMPLOYED sentinel -> FLAG_SENTINEL_EMPLOYED + replace with NaN
     (EDA Section 4: 365243 = ~1000 years, encodes pensioners/unemployed)
  2. CODE_GENDER / ORGANIZATION_TYPE XNA -> NaN (true unknown, not a category)
  3. Rare NAME_INCOME_TYPE groups -> "Other_Rare"
     (EDA Section 5: Unemployed/Student/Businessman/Maternity leave total n=55)
  4. ORGANIZATION_TYPE macro-sector mapping (58 -> 12 sectors)
  5. DAYS_* columns -> positive years (applied in engineer_ratios after flags are set here)
"""
import numpy as np
import pandas as pd
from .config import (
    DAYS_EMPLOYED_SENTINEL,
    RARE_INCOME_TYPES, RARE_INCOME_LABEL,
    ORG_TYPE_MAP,
)
from .utils import log, log_shape


def run(df: pd.DataFrame) -> pd.DataFrame:
    log("Step 4 - Structural cleaning ...")
    df = df.copy()

    # 1. DAYS_EMPLOYED sentinel
    sentinel_mask = df["DAYS_EMPLOYED"] == DAYS_EMPLOYED_SENTINEL
    df["FLAG_SENTINEL_EMPLOYED"] = sentinel_mask.astype(np.int8)
    df.loc[sentinel_mask, "DAYS_EMPLOYED"] = np.nan
    log(f"  DAYS_EMPLOYED sentinel replaced: {sentinel_mask.sum():,} rows flagged")

    # 2. CODE_GENDER XNA -> NaN
    if "CODE_GENDER" in df.columns:
        xna_gender = (df["CODE_GENDER"] == "XNA").sum()
        df["CODE_GENDER"] = df["CODE_GENDER"].replace("XNA", np.nan)
        log(f"  CODE_GENDER XNA -> NaN: {xna_gender:,} rows")

    # 3. ORGANIZATION_TYPE XNA -> NaN
    if "ORGANIZATION_TYPE" in df.columns:
        xna_org = (df["ORGANIZATION_TYPE"] == "XNA").sum()
        df["ORGANIZATION_TYPE"] = df["ORGANIZATION_TYPE"].replace("XNA", np.nan)
        log(f"  ORGANIZATION_TYPE XNA -> NaN: {xna_org:,} rows")

    # 4. Rare NAME_INCOME_TYPE groups
    if "NAME_INCOME_TYPE" in df.columns:
        rare_mask = df["NAME_INCOME_TYPE"].isin(RARE_INCOME_TYPES)
        df.loc[rare_mask, "NAME_INCOME_TYPE"] = RARE_INCOME_LABEL
        log(f"  Rare income types grouped: {rare_mask.sum():,} rows -> '{RARE_INCOME_LABEL}'")

    # 5. ORGANIZATION_TYPE macro-sector mapping
    if "ORGANIZATION_TYPE" in df.columns:
        # Unmapped values (NaN already handled above) keep their original value
        df["ORGANIZATION_TYPE"] = df["ORGANIZATION_TYPE"].map(ORG_TYPE_MAP).fillna(
            df["ORGANIZATION_TYPE"]
        )
        n_unique = df["ORGANIZATION_TYPE"].nunique()
        log(f"  ORGANIZATION_TYPE mapped: {n_unique} unique sectors remaining")

    log_shape("clean_structure", df)
    return df

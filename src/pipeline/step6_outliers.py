"""
Step 6 - Outlier treatment.

EDA Section 6 findings drive every decision here:

AMT_INCOME_TOTAL
  p99 = 472,500; max = 117,000,000 (247x median). Extreme right skew.
  Action: winsorize at p99 -> then log-transform in step7.

AMT_REQ_CREDIT_BUREAU_* (QRT, MON, YEAR)
  Extreme spikes (max=261 for QRT vs p99~5). Cap at p99.

CNT_CHILDREN / CNT_FAM_MEMBERS
  Max values (19 / 20) are biologically implausible data entry errors.
  Hard-cap at defensible upper limits (10 / 15).

DEF_30_CNT_SOCIAL_CIRCLE / DEF_60_CNT_SOCIAL_CIRCLE
  EDA Section 8: 11.4% "outlier" rate is a REAL behavioral sub-population
  (applicants embedded in high-default social circles). Do NOT winsorize.
  Bin into 0 / 1 / 2+ ordered categories instead.

OBS_30 / OBS_60 already handled in step7 (OBS_60 dropped as redundant with OBS_30).
"""
import numpy as np
import pandas as pd
from .config import WINSORIZE_CONFIG, CAP_CONFIG
from .utils import log, log_shape


def run(df: pd.DataFrame) -> pd.DataFrame:
    log("Step 6 - Outlier treatment ...")
    df = df.copy()

    # Winsorize at configured percentile
    for col, pct in WINSORIZE_CONFIG.items():
        if col not in df.columns:
            continue
        cap_val = df[col].quantile(pct)
        n_capped = (df[col] > cap_val).sum()
        df[col] = df[col].clip(upper=cap_val)
        log(f"  Winsorized {col} at p{int(pct*100)}={cap_val:.2f}: {n_capped:,} values capped")

    # Hard cap
    for col, cap_val in CAP_CONFIG.items():
        if col not in df.columns:
            continue
        n_capped = (df[col] > cap_val).sum()
        df[col] = df[col].clip(upper=cap_val)
        log(f"  Hard-capped {col} at {cap_val}: {n_capped:,} values capped")

    # DEF_30 / DEF_60 -> ordinal bins
    for col in ["DEF_30_CNT_SOCIAL_CIRCLE", "DEF_60_CNT_SOCIAL_CIRCLE"]:
        if col not in df.columns:
            continue
        bin_col = col + "_BIN"
        df[bin_col] = pd.cut(
            df[col],
            bins=[-np.inf, 0, 1, np.inf],
            labels=["0", "1", "2+"],
            right=True,
        ).astype(str)
        log(f"  Binned {col} -> {bin_col}: {df[bin_col].value_counts().to_dict()}")
        # Drop the original to avoid leaking raw count into encoded features
        df = df.drop(columns=[col])

    log_shape("step6_out", df)
    return df

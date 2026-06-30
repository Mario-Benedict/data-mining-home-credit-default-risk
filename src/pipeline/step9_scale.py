"""
Step 9 - Feature selection, NaN fill, StandardScaler -> features_clustering.csv.

1. Select  - keep SK_ID_CURR (identifier) + the CLUSTERING_FEATURES that exist
             + the ordinal DEF_30 social-circle bin.
2. Fill    - residual NaN -> 0  (YEARS_EMPLOYED is NaN for sentinel rows;
             FLAG_SENTINEL_EMPLOYED already encodes that, so 0 is correct).
3. Scale   - StandardScaler on everything EXCEPT true {0,1} binary flags.
             Ordinal columns (education 0-4, DEF_30 bin 0-2) and the
             frequency-encoded columns ARE scaled: without scaling their raw
             range would silently out-weight the standardized features. Binary
             flags stay in {0,1} so cluster profiles remain readable as
             "share of the cluster that has this trait".

Output: datasets/final/features_clustering.csv
  First column SK_ID_CURR is an identifier (not scaled, not a feature) so
  Phase 2-5 outputs are traceable to real applicants.
"""
import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from .config import OUTPUT_DIR, CLUSTERING_FEATURES
from .utils import log, log_shape


def run(df: pd.DataFrame) -> pd.DataFrame:
    log("Step 9 - Feature selection + scaling ...")
    df = df.copy().reset_index(drop=True)

    # 1. Select features
    base_cols = [c for c in CLUSTERING_FEATURES if c in df.columns]
    missing_base = [c for c in CLUSTERING_FEATURES if c not in df.columns]
    if missing_base:
        log(f"  WARNING - expected features not found (skipped): {missing_base}", "WARN")

    # DEF_30_CNT_SOCIAL_CIRCLE_BIN is ordinal-encoded (int), kept alongside.
    extra_encoded = [c for c in ["DEF_30_CNT_SOCIAL_CIRCLE_BIN"] if c in df.columns]

    select_cols = base_cols + extra_encoded
    feature_df = df[select_cols].copy()
    log(f"  Selected {len(select_cols)} features "
        f"({len(base_cols)} base + {len(extra_encoded)} ordinal bin)")

    # 2. Fill residual NaN
    nan_count = feature_df.isna().sum().sum()
    if nan_count > 0:
        feature_df = feature_df.fillna(0)
        log(f"  Filled {nan_count:,} residual NaN -> 0")

    # 3. Scale everything except true {0,1} binary flags
    # Detection is by VALUE SET, not dtype: an int8 ordinal (0-4) is NOT
    # binary and must be scaled, otherwise its range silently dominates.
    binary_cols = [
        c for c in feature_df.columns
        if set(pd.unique(feature_df[c].dropna())).issubset({0, 1, 0.0, 1.0})
    ]
    scale_cols = [
        c for c in feature_df.select_dtypes(include=[np.number]).columns
        if c not in binary_cols
    ]
    log(f"  Scaling {len(scale_cols)} continuous/ordinal cols; "
        f"{len(binary_cols)} binary flags left as 0/1")

    scaler = StandardScaler()
    scaled_values = pd.DataFrame(
        scaler.fit_transform(feature_df[scale_cols]),
        columns=scale_cols,
        index=feature_df.index,
    )
    feature_df = pd.concat(
        [feature_df.drop(columns=scale_cols), scaled_values],
        axis=1,
    )[select_cols]   # restore original column order

    # 4. Re-attach identifier and save
    if "SK_ID_CURR" in df.columns:
        feature_df.insert(0, "SK_ID_CURR", df["SK_ID_CURR"].astype(np.int64))

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(OUTPUT_DIR, "features_clustering.csv")
    feature_df.to_csv(out_path, index=False)
    log(f"  Saved -> {out_path}")
    log_shape("features_clustering", feature_df)
    return feature_df

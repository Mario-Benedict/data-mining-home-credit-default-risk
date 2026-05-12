"""
Step 9 — Feature selection, NaN fill, StandardScaler → features_clustering.csv.

1. Select  — keep only CLUSTERING_FEATURES + OHE-expanded columns
2. Fill    — residual NaN → 0  (YEARS_EMPLOYED is NaN for sentinel rows;
             FLAG_SENTINEL_EMPLOYED already encodes that, so 0 is correct)
3. Scale   — StandardScaler on continuous features only
             (binary / flag columns already in [0,1]; scaling them distorts
             cluster-profile interpretability)

Output: datasets/final/features_clustering.csv
  Single fully-numeric file, no train/test split indicator.
  Ready to feed directly into K-Means, DBSCAN, or Hierarchical clustering.
"""
import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from .config import OUTPUT_DIR, CLUSTERING_FEATURES, CLUSTER_OHE_COLS
from .utils import log, log_shape


def run(df: pd.DataFrame) -> pd.DataFrame:
    log("Step 9 — Feature selection + scaling ...")
    df = df.copy().reset_index(drop=True)

    # ── 1. Select features ────────────────────────────────────────────────
    base_cols = [c for c in CLUSTERING_FEATURES if c in df.columns]
    missing_base = [c for c in CLUSTERING_FEATURES if c not in df.columns]
    if missing_base:
        log(f"  WARNING — expected features not found (skipped): {missing_base}", "WARN")

    ohe_cols = [
        c for c in df.columns
        if any(c.startswith(p + "_") for p in CLUSTER_OHE_COLS)
    ]

    # DEF_30_CNT_SOCIAL_CIRCLE_BIN is ordinal-encoded (int), not OHE'd
    extra_encoded = [
        c for c in ["DEF_30_CNT_SOCIAL_CIRCLE_BIN"]
        if c in df.columns
    ]

    select_cols = base_cols + extra_encoded + ohe_cols
    feature_df = df[select_cols].copy()
    log(f"  Selected {len(select_cols)} features "
        f"({len(base_cols)} base + {len(extra_encoded)} ordinal + {len(ohe_cols)} OHE)")

    # ── 2. Fill residual NaN ───────────────────────────────────────────────
    nan_count = feature_df.isna().sum().sum()
    if nan_count > 0:
        feature_df = feature_df.fillna(0)
        log(f"  Filled {nan_count:,} residual NaN → 0")

    # ── 3. StandardScale continuous features ──────────────────────────────
    binary_cols = [
        c for c in feature_df.columns
        if feature_df[c].dtype == np.int8
        or set(feature_df[c].dropna().unique()).issubset({0, 1, 0.0, 1.0})
    ]
    scale_cols = [
        c for c in feature_df.select_dtypes(include=[np.number]).columns
        if c not in binary_cols
    ]
    log(f"  Scaling {len(scale_cols)} continuous cols; {len(binary_cols)} binary cols left as-is")

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

    # ── 4. Save ───────────────────────────────────────────────────────────
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(OUTPUT_DIR, "features_clustering.csv")
    feature_df.to_csv(out_path, index=False)
    log(f"  Saved → {out_path}")
    log_shape("features_clustering", feature_df)
    return feature_df

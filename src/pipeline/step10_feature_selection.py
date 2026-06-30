"""
Step 10 - Feature selection check (correlation plus entropy / mutual information).

This step validates the feature set from steps 1 to 9 with two formal measures:
    1. Pearson correlation between features, to catch any leftover multicollinearity.
    2. Mutual information against TARGET (entropy-based), to gauge discriminative power.

It does not rewrite features_clustering.csv. It only writes two small CSVs that
back up why each feature is kept. The written discussion lives in the project-root
REPORT.md, not here.

Output:
  results/phase1_preprocessing/feature_importance.csv
  results/phase1_preprocessing/high_corr_pairs.csv
"""
import os
import numpy as np
import pandas as pd
from sklearn.feature_selection import mutual_info_classif

from .config import BASE_DIR, OUTPUT_DIR, PATHS
from .utils import log


REPORT_DIR = os.path.join(BASE_DIR, "results", "phase1_preprocessing")
FEATURES_PATH = os.path.join(OUTPUT_DIR, "features_clustering.csv")


def compute_mutual_info(features: pd.DataFrame, target: pd.Series) -> pd.DataFrame:
    """
    Mutual information of each feature against TARGET.
    MI = 0 means the feature carries no information about default vs non-default.
    MI > 0 means there is a detectable relationship, including non-linear ones.
    A fixed random_state keeps the result reproducible.
    """
    log(f"  Computing mutual_info_classif on {features.shape[1]} features ...")
    mi_scores = mutual_info_classif(
        features.values,
        target.values,
        discrete_features=False,
        random_state=42,
        n_neighbors=3,
    )
    df = pd.DataFrame({
        "feature": features.columns,
        "mutual_info": mi_scores,
    }).sort_values("mutual_info", ascending=False).reset_index(drop=True)
    df["rank"] = df.index + 1
    return df


def compute_correlation_pairs(features: pd.DataFrame, threshold: float = 0.85) -> pd.DataFrame:
    """Pearson correlation pairs with |r| above the threshold, self-pairs excluded."""
    log(f"  Computing correlation matrix ({features.shape[1]} x {features.shape[1]}) ...")
    corr = features.corr().abs()
    upper = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool))
    pairs = (
        upper.stack()
        .reset_index()
        .rename(columns={"level_0": "feature_1", "level_1": "feature_2", 0: "abs_corr"})
    )
    high = pairs[pairs["abs_corr"] > threshold].sort_values("abs_corr", ascending=False).reset_index(drop=True)
    return high


def run() -> None:
    log("Step 10 - Feature selection check (correlation plus entropy) ...")

    os.makedirs(REPORT_DIR, exist_ok=True)

    log(f"  Loading {FEATURES_PATH} ...")
    features_df = pd.read_csv(FEATURES_PATH)
    log(f"  features_clustering: {features_df.shape[0]:,} x {features_df.shape[1]}")

    log("  Loading TARGET from application_train.csv ...")
    target_df = pd.read_csv(PATHS["application_train"], usecols=["SK_ID_CURR", "TARGET"])
    n_train = len(target_df)
    log(f"  application_train: {n_train:,} rows (TARGET available)")

    if "SK_ID_CURR" in features_df.columns:
        # Robust ID-based alignment, no reliance on row order.
        aligned = features_df.merge(target_df, on="SK_ID_CURR", how="inner")
        train_target = aligned["TARGET"].reset_index(drop=True)
        train_features = aligned.drop(columns=["SK_ID_CURR", "TARGET"]).reset_index(drop=True)
    else:
        # Fallback: positional alignment (train rows are stacked first in step3).
        train_features = features_df.iloc[:n_train].reset_index(drop=True)
        train_target = target_df["TARGET"].reset_index(drop=True)
    log(f"  Aligned for MI: {train_features.shape[0]:,} train rows, {train_features.shape[1]} features")

    mi_df = compute_mutual_info(train_features, train_target)
    mi_path = os.path.join(REPORT_DIR, "feature_importance.csv")
    mi_df.to_csv(mi_path, index=False)
    log(f"  Saved {mi_path}")

    high_corr = compute_correlation_pairs(train_features, threshold=0.85)
    corr_path = os.path.join(REPORT_DIR, "high_corr_pairs.csv")
    high_corr.to_csv(corr_path, index=False)
    log(f"  Saved {corr_path} ({len(high_corr)} pairs with |r| > 0.85)")

    log("  Feature selection check complete (correlation plus entropy).")

"""
KDD Pipeline — Phase 1 Preprocessing
=====================================
Single entry-point. Run from the project root:

    python src/run_pipeline.py

Output: datasets/final/features_clustering.csv
  Fully numeric, StandardScaler-normalized, one row per applicant.
  Ready for Phase 2 (K-Means, DBSCAN, Hierarchical clustering).

Pipeline steps:
    1  load       — read all CSV files
    2  aggregate  — roll up 5 relational tables to SK_ID_CURR grain
    3  merge      — stack train+test, left-join aggregated features
    4  clean      — sentinel values, rare categories, XNA → NaN
    5  missing    — missingness indicators + imputation
    6  outliers   — winsorize / cap / bin social-circle delinquency
    7  engineer   — derived ratios, log transforms, drop redundant cols
    8  encode     — binary / ordinal / OHE all remaining categoricals
    9  scale      — feature selection + StandardScaler → features_clustering.csv
"""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pipeline import (
    step1_load,
    step2_aggregate,
    step3_merge,
    step4_clean,
    step5_missing,
    step6_outliers,
    step7_engineer,
    step8_encode,
    step9_scale,
)
from pipeline.utils import log


def main() -> None:
    t0 = time.time()
    log("=" * 60)
    log("KDD Phase 1 — Preprocessing pipeline starting")
    log("=" * 60)

    dfs      = step1_load.run()
    agg_dfs  = step2_aggregate.run(dfs)
    merged   = step3_merge.run(dfs, agg_dfs)
    cleaned  = step4_clean.run(merged)
    imputed  = step5_missing.run(cleaned)
    outlier_treated = step6_outliers.run(imputed)
    engineered = step7_engineer.run(outlier_treated)
    encoded    = step8_encode.run(engineered)
    step9_scale.run(encoded)

    elapsed = time.time() - t0
    log("=" * 60)
    log(f"Pipeline complete in {elapsed:.1f}s")
    log("Output: datasets/final/features_clustering.csv")
    log("=" * 60)


if __name__ == "__main__":
    main()

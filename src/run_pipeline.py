"""
KDD Pipeline - Phase 1 Preprocessing
=====================================
Single entry-point. Run from the project root:

    python src/run_pipeline.py

Output: datasets/final/features_clustering.csv
  Fully numeric, StandardScaler-normalized, one row per applicant.
  Ready for Phase 2 (K-Means, DBSCAN, Hierarchical clustering).

Pipeline steps:
    1  load              - read all CSV files
    2  aggregate         - roll up 5 relational tables to SK_ID_CURR grain
    3  merge             - stack train+test, left-join aggregated features
    4  clean             - sentinel values, rare categories, XNA -> NaN
    5  missing           - missingness indicators + imputation
    6  outliers          - winsorize / cap / bin social-circle delinquency
    7  engineer          - derived ratios, log transforms, drop redundant cols
    8  encode            - binary / ordinal / frequency encode remaining categoricals (no OHE)
    9  scale             - feature selection + StandardScaler -> features_clustering.csv
   10  feature_selection - correlation + entropy (MI) check -> feature_importance.csv, high_corr_pairs.csv
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
    step10_feature_selection,
)
from pipeline.utils import log

# Orchestration: Prefect (per tech-stack doc) with plain-Python fallback
# The project tech stack prescribes Mage/Prefect/Airflow for the pipeline.
# Prefect is used when installed (task-level retries, run tracking, UI);
# without it the pipeline still runs as a plain script.
try:
    from prefect import flow, task
    _PREFECT = True
except ImportError:
    _PREFECT = False

    def task(*args, **kwargs):
        def _wrap(fn):
            return fn
        if args and callable(args[0]):
            return args[0]
        return _wrap

    flow = task


@task(name="step1_load")
def t1_load():
    return step1_load.run()


@task(name="step2_aggregate")
def t2_aggregate(dfs):
    return step2_aggregate.run(dfs)


@task(name="step3_merge")
def t3_merge(dfs, agg_dfs):
    return step3_merge.run(dfs, agg_dfs)


@task(name="step4_clean")
def t4_clean(df):
    return step4_clean.run(df)


@task(name="step5_missing")
def t5_missing(df):
    return step5_missing.run(df)


@task(name="step6_outliers")
def t6_outliers(df):
    return step6_outliers.run(df)


@task(name="step7_engineer")
def t7_engineer(df):
    return step7_engineer.run(df)


@task(name="step8_encode")
def t8_encode(df):
    return step8_encode.run(df)


@task(name="step9_scale")
def t9_scale(df):
    return step9_scale.run(df)


@task(name="step10_feature_selection")
def t10_feature_selection():
    return step10_feature_selection.run()


@flow(name="kdd-phase1-preprocessing")
def main() -> None:
    t0 = time.time()
    log("=" * 60)
    log(f"KDD Phase 1 - Preprocessing pipeline starting "
        f"(orchestrator: {'Prefect' if _PREFECT else 'plain Python'})")
    log("=" * 60)

    dfs      = t1_load()
    agg_dfs  = t2_aggregate(dfs)
    merged   = t3_merge(dfs, agg_dfs)
    cleaned  = t4_clean(merged)
    imputed  = t5_missing(cleaned)
    outlier_treated = t6_outliers(imputed)
    engineered = t7_engineer(outlier_treated)
    encoded    = t8_encode(engineered)
    t9_scale(encoded)
    t10_feature_selection()

    elapsed = time.time() - t0
    log("=" * 60)
    log(f"Pipeline complete in {elapsed:.1f}s")
    log("Output: datasets/final/features_clustering.csv")
    log("        results/phase1_preprocessing/feature_importance.csv, high_corr_pairs.csv")
    log("=" * 60)


if __name__ == "__main__":
    main()

"""
KDD Pipeline - Phase 1 Preprocessing
=====================================
Single entry-point. Run from the project root:

    python src/run_pipeline.py

Outputs:
  datasets/final/features_business.csv
    Unscaled values for business interpretation, rules, and record-level review.
  datasets/final/features_clustering.csv
    Fully numeric, StandardScaler-normalized values for K-Means, DBSCAN, and
    hierarchical clustering. Continuous axes are clipped at p0.5/p99.5 so a few
    extreme files cannot capture the centroids.
  datasets/final/features_anomaly.csv
    The same columns standardized WITHOUT clipping, for Phase 4. An outlier
    detector cannot find an extreme on an axis whose extremes were truncated.

The steps run in the order listed below and that order is strict: each one
consumes the frame the previous one returned. The sequence lives here, in the
orchestrator, rather than in the filenames, which is why the modules are named
for what they do instead of for where they sit in the queue.

    load_raw_tables          read the eight source CSV files
    aggregate_histories      roll up 5 relational credit histories to SK_ID_CURR grain
    join_to_applicant        stack train+test, left-join the aggregated histories
    clean_structure          sentinel values, rare categories, XNA -> NaN, redundant columns
    flag_and_impute_missing  missingness indicators FIRST, then imputation
    treat_outliers           winsorize / cap / bin social-circle delinquency
    engineer_ratios          leverage and burden ratios, log transforms, drop redundant cols
    encode_categoricals      binary / ordinal / frequency encoding (no one-hot)
    build_matrices           the three output views: business, clustering, anomaly
    check_features           publishes the keep/drop audit plus correlation diagnostics
"""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pipeline import (
    load_raw_tables,
    aggregate_histories,
    join_to_applicant,
    clean_structure,
    flag_and_impute_missing,
    treat_outliers,
    engineer_ratios,
    encode_categoricals,
    build_matrices,
    check_features,
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


# The task wrappers carry a leading underscore so they do not shadow the module
# of the same name imported above.
@task(name="load_raw_tables")
def _load_raw_tables():
    return load_raw_tables.run()


@task(name="aggregate_histories")
def _aggregate_histories(dfs):
    return aggregate_histories.run(dfs)


@task(name="join_to_applicant")
def _join_to_applicant(dfs, agg_dfs):
    return join_to_applicant.run(dfs, agg_dfs)


@task(name="clean_structure")
def _clean_structure(df):
    return clean_structure.run(df)


@task(name="flag_and_impute_missing")
def _flag_and_impute_missing(df):
    return flag_and_impute_missing.run(df)


@task(name="treat_outliers")
def _treat_outliers(df):
    return treat_outliers.run(df)


@task(name="engineer_ratios")
def _engineer_ratios(df):
    return engineer_ratios.run(df)


@task(name="encode_categoricals")
def _encode_categoricals(df):
    return encode_categoricals.run(df)


@task(name="build_matrices")
def _build_matrices(df):
    return build_matrices.run(df)


@task(name="check_features")
def _check_features():
    return check_features.run()


@flow(name="kdd-phase1-preprocessing")
def main() -> None:
    """Run the pipeline through Prefect when orchestration is explicitly requested."""
    _run_steps(orchestrator="Prefect")


def _local_callable(fn):
    """Return the undecorated function for a Prefect task, or the function itself."""
    return getattr(fn, "fn", fn)


def _run_steps(orchestrator: str = "plain Python") -> None:
    t0 = time.time()
    log("=" * 60)
    log(f"KDD Phase 1 - Preprocessing pipeline starting "
        f"(orchestrator: {orchestrator})")
    log("=" * 60)

    # Calling the task's ``fn`` attribute bypasses Prefect's temporary API.  This
    # keeps local reruns deterministic even when the installed Prefect/FastAPI
    # versions are incompatible, while preserving the optional Prefect flow.
    load = _local_callable(_load_raw_tables)
    aggregate = _local_callable(_aggregate_histories)
    join = _local_callable(_join_to_applicant)
    clean = _local_callable(_clean_structure)
    impute = _local_callable(_flag_and_impute_missing)
    outliers = _local_callable(_treat_outliers)
    ratios = _local_callable(_engineer_ratios)
    encode = _local_callable(_encode_categoricals)
    matrices = _local_callable(_build_matrices)
    check = _local_callable(_check_features)

    raw_tables = load()
    histories = aggregate(raw_tables)
    applicants = join(raw_tables, histories)
    cleaned = clean(applicants)
    imputed = impute(cleaned)
    outlier_treated = outliers(imputed)
    engineered = ratios(outlier_treated)
    encoded = encode(engineered)
    matrices(encoded)
    check()

    elapsed = time.time() - t0
    log("=" * 60)
    log(f"Pipeline complete in {elapsed:.1f}s")
    log("Output: datasets/final/features_business.csv   (readable, for case review)")
    log("        datasets/final/features_clustering.csv (clipped, for K-Means)")
    log("        datasets/final/features_anomaly.csv    (unclipped, for Phase 4)")
    log("        results/phase1_preprocessing/feature_selection_decisions.csv, high_corr_pairs.csv")
    log("=" * 60)


if __name__ == "__main__":
    # Prefect is opt-in for local execution.  The plain runner performs the
    # exact same steps without starting a temporary API server.
    if os.environ.get("HOME_CREDIT_USE_PREFECT", "0") == "1" and _PREFECT:
        main()
    else:
        _run_steps()

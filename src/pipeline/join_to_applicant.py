"""
Combine application tables and join all aggregated features.

Design decisions:
  - train + test are stacked after dropping TARGET (unsupervised pipeline).
  - FLAG_NO_BUREAU is set BEFORE the left-join so genuine bureau absence
    is distinguishable from imputed 0s.
  - All five aggregated tables are left-joined on SK_ID_CURR.
"""
import numpy as np
import pandas as pd
from .utils import log, log_shape


def run(dfs: dict, agg_dfs: dict) -> pd.DataFrame:
    log("Step 3 - Merging application tables ...")

    train = dfs["application_train"].copy()
    test  = dfs["application_test"].copy()

    if "TARGET" in train.columns:
        train = train.drop(columns=["TARGET"])

    app = pd.concat([train, test], axis=0, ignore_index=True)
    log_shape("app_combined", app)

    # Duplicate check. The two application files are disjoint by construction,
    # but this is the point where a stray duplicated applicant would silently
    # double-count into every downstream count, so it is verified explicitly
    # rather than assumed. Exact row duplicates are dropped; a duplicated
    # identifier with differing rows is a data fault and stops the pipeline.
    exact_dups = int(app.duplicated().sum())
    if exact_dups:
        app = app.drop_duplicates(ignore_index=True)
        log(f"  Dropped {exact_dups:,} exact duplicate application rows")
    id_dups = int(app["SK_ID_CURR"].duplicated().sum())
    if id_dups:
        raise ValueError(
            f"{id_dups:,} applications share an SK_ID_CURR with conflicting rows; "
            "resolve the source conflict before joining histories."
        )
    log(f"  Applicant identifier is unique across all {len(app):,} rows "
        f"({exact_dups} exact duplicates removed)")

    bureau_ids = set(agg_dfs["bureau_agg"]["SK_ID_CURR"])
    app["FLAG_NO_BUREAU"] = (~app["SK_ID_CURR"].isin(bureau_ids)).astype(np.int8)
    log(f"  FLAG_NO_BUREAU=1 count: {app['FLAG_NO_BUREAU'].sum():,}")

    for key, df in [
        ("bureau_agg", agg_dfs["bureau_agg"]),
        ("prev_agg",  agg_dfs["prev_agg"]),
        ("pos_agg",   agg_dfs["pos_agg"]),
        ("inst_agg",  agg_dfs["inst_agg"]),
        ("cc_agg",    agg_dfs["cc_agg"]),
    ]:
        app = app.merge(df, on="SK_ID_CURR", how="left")
        log(f"  Joined {key}: {app.shape[1]} cols after merge")

    log_shape("merged", app)
    return app

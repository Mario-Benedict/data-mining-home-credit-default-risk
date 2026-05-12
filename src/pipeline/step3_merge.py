"""
Step 3 — Combine application tables and join all aggregated features.

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
    log("Step 3 — Merging application tables ...")

    train = dfs["application_train"].copy()
    test  = dfs["application_test"].copy()

    if "TARGET" in train.columns:
        train = train.drop(columns=["TARGET"])

    app = pd.concat([train, test], axis=0, ignore_index=True)
    log_shape("app_combined", app)

    bureau_ids = set(agg_dfs["bureau_agg"]["SK_ID_CURR"])
    app["FLAG_NO_BUREAU"] = (~app["SK_ID_CURR"].isin(bureau_ids)).astype(np.int8)
    log(f"  FLAG_NO_BUREAU=1 count: {app['FLAG_NO_BUREAU'].sum():,}")

    for key, df in [
        ("bureau_agg", agg_dfs["bureau_agg"]),
        ("prev_agg",   agg_dfs["prev_agg"]),
        ("pos_agg",    agg_dfs["pos_agg"]),
        ("inst_agg",   agg_dfs["inst_agg"]),
        ("cc_agg",     agg_dfs["cc_agg"]),
    ]:
        app = app.merge(df, on="SK_ID_CURR", how="left")
        log(f"  Joined {key}: {app.shape[1]} cols after merge")

    log_shape("merged", app)
    return app

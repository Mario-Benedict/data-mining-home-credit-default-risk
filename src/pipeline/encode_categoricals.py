"""
Encode categoricals into a fully numeric, clustering-ready frame.

The guiding question for every column here is NOT "how do we make it numeric"
but "how do we make it numeric WITHOUT distorting Euclidean distance", because
the output feeds K-Means / DBSCAN / hierarchical clustering.

  Binary (2 levels - encoding is unambiguous):
    CODE_GENDER         F -> 1, M -> 0
    NAME_CONTRACT_TYPE  Cash loans -> 1, Revolving loans -> 0

  Ordinal (the order is real, so we keep it as one ordered integer):
    NAME_EDUCATION_TYPE           Lower secondary(0) ... Academic degree(4)
    DEF_30_CNT_SOCIAL_CIRCLE_BIN  "0"(0) "1"(1) "2+"(2)

  Frequency (nominal, no order - collapse to one "common  to  rare" axis):
    NAME_INCOME_TYPE  -> NAME_INCOME_TYPE_FREQ
    ORGANIZATION_TYPE -> ORGANIZATION_TYPE_FREQ

We deliberately do NOT one-hot encode. OHE would add ~21 sparse binary axes
that dominate Euclidean distance and force every category to be equidistant
from every other - both wrong for segmentation. See config.py for the full
rationale.

Any leftover object columns are dropped: they are not in CLUSTERING_FEATURES
and would only add noise dimensions.
"""
import numpy as np
import pandas as pd
from .config import (
    ORDINAL_ENCODE_COLS,
    EDUCATION_DEFAULT_LEVEL,
    FREQUENCY_ENCODE_COLS,
    DEF30_BIN_ORDINAL,
)
from .utils import log, log_shape


def run(df: pd.DataFrame) -> pd.DataFrame:
    log("Step 8 - Encoding categoricals (ordinal + frequency, no OHE) ...")
    df = df.copy()

    # Binary: CODE_GENDER
    if "CODE_GENDER" in df.columns:
        df["CODE_GENDER"] = (df["CODE_GENDER"] == "F").astype(np.int8)
        log("  CODE_GENDER: F=1, M=0")

    # Binary: NAME_CONTRACT_TYPE
    if "NAME_CONTRACT_TYPE" in df.columns:
        df["NAME_CONTRACT_TYPE"] = (df["NAME_CONTRACT_TYPE"] == "Cash loans").astype(np.int8)
        log("  NAME_CONTRACT_TYPE: Cash loans=1, Revolving loans=0")

    # Ordinal: DEF_30_CNT_SOCIAL_CIRCLE_BIN
    bin_col = "DEF_30_CNT_SOCIAL_CIRCLE_BIN"
    if bin_col in df.columns:
        df[bin_col] = df[bin_col].map(DEF30_BIN_ORDINAL).fillna(0).astype(np.int8)
        log(f"  {bin_col}: '0'->0, '1'->1, '2+'->2")

    # Ordinal: NAME_EDUCATION_TYPE (education ladder)
    for col, mapping in ORDINAL_ENCODE_COLS.items():
        if col not in df.columns:
            continue
        unseen = set(df[col].dropna().unique()) - set(mapping)
        if unseen:
            log(f"  WARNING - {col} has unmapped levels {unseen}; "
                f"sent to default {EDUCATION_DEFAULT_LEVEL}", "WARN")
        df[col] = df[col].map(mapping).fillna(EDUCATION_DEFAULT_LEVEL).astype(np.int8)
        log(f"  {col}: ordinal 0-{max(mapping.values())} "
            f"(value counts: {df[col].value_counts().sort_index().to_dict()})")

    # Frequency: NAME_INCOME_TYPE, ORGANIZATION_TYPE
    # "Unknown" (e.g. pensioners' XNA organisation) is a legitimate category
    # and gets its own frequency - pensioners stay separately flagged via
    # FLAG_SENTINEL_EMPLOYED, so this does not recreate the r~1.0 collinearity.
    for col, new_col in FREQUENCY_ENCODE_COLS.items():
        if col not in df.columns:
            continue
        n_na = df[col].isna().sum()
        if n_na:
            df[col] = df[col].fillna("Unknown")
            log(f"  {col}: filled {n_na:,} NaN -> 'Unknown' before frequency encoding")
        freq = df[col].value_counts(normalize=True)
        df[new_col] = df[col].map(freq).astype(np.float32)
        top = freq.head(3).round(3).to_dict()
        log(f"  {col} -> {new_col}: {df[col].nunique()} categories -> 1 axis "
            f"(top shares: {top})")
        df = df.drop(columns=[col])

    # Drop any remaining object columns
    drop_obj = [c for c in df.columns if df[c].dtype == object]
    if drop_obj:
        df = df.drop(columns=drop_obj)
        log(f"  Dropped {len(drop_obj)} unused categoricals: {drop_obj}")

    log_shape("encode_categoricals", df)
    return df

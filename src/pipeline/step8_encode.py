"""
Step 8 — Encode all remaining categoricals so the output is fully numeric.

Binary encodings:
  CODE_GENDER         : F→1, M→0
  NAME_CONTRACT_TYPE  : Cash loans→1, Revolving loans→0

Ordinal encoding:
  DEF_30_CNT_SOCIAL_CIRCLE_BIN : "0"→0, "1"→1, "2+"→2
  (ordering is meaningful; OHE would discard it)

OHE (drop_first=True):
  NAME_INCOME_TYPE    — 5 cats after rare grouping → 4 dummies
  NAME_EDUCATION_TYPE — 5 cats → 4 dummies
  ORGANIZATION_TYPE   — 12 macro-sectors → 11 dummies

All remaining object columns are dropped — they are not in CLUSTERING_FEATURES
and would only add noise dimensions to Euclidean-distance clustering.
"""
import numpy as np
import pandas as pd
from .config import CLUSTER_OHE_COLS, DEF30_BIN_ORDINAL
from .utils import log, log_shape


def run(df: pd.DataFrame) -> pd.DataFrame:
    log("Step 8 — Encoding categoricals ...")
    df = df.copy()

    # ── Binary: CODE_GENDER ───────────────────────────────────────────────
    if "CODE_GENDER" in df.columns:
        df["CODE_GENDER"] = (df["CODE_GENDER"] == "F").astype(np.int8)
        log("  CODE_GENDER: F=1, M=0")

    # ── Binary: NAME_CONTRACT_TYPE ────────────────────────────────────────
    if "NAME_CONTRACT_TYPE" in df.columns:
        df["NAME_CONTRACT_TYPE"] = (df["NAME_CONTRACT_TYPE"] == "Cash loans").astype(np.int8)
        log("  NAME_CONTRACT_TYPE: Cash loans=1, Revolving loans=0")

    # ── Ordinal: DEF_30_CNT_SOCIAL_CIRCLE_BIN ────────────────────────────
    bin_col = "DEF_30_CNT_SOCIAL_CIRCLE_BIN"
    if bin_col in df.columns:
        df[bin_col] = df[bin_col].map(DEF30_BIN_ORDINAL).fillna(0).astype(np.int8)
        log(f"  {bin_col}: '0'→0, '1'→1, '2+'→2")

    # ── Fill NaN in OHE candidates before encoding ────────────────────────
    for col in CLUSTER_OHE_COLS:
        if col in df.columns and df[col].isna().any():
            n = df[col].isna().sum()
            df[col] = df[col].fillna("Unknown")
            log(f"  {col}: filled {n:,} NaN → 'Unknown'")

    # ── OHE: NAME_INCOME_TYPE, NAME_EDUCATION_TYPE, ORGANIZATION_TYPE ─────
    ohe_present = [c for c in CLUSTER_OHE_COLS if c in df.columns]
    if ohe_present:
        before = df.shape[1]
        df = pd.get_dummies(df, columns=ohe_present, drop_first=True, dtype=np.int8)
        added = df.shape[1] - before + len(ohe_present)
        log(f"  OHE {ohe_present} → {added} dummy columns")

    # ── Drop all remaining object columns ─────────────────────────────────
    drop_obj = [c for c in df.columns if df[c].dtype == object]
    if drop_obj:
        df = df.drop(columns=drop_obj)
        log(f"  Dropped {len(drop_obj)} unused categoricals: {drop_obj}")

    log_shape("step8_out", df)
    return df

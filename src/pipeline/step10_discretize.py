"""
Step 10 — Discretize features → features_discretized.csv  (Phase 3 Apriori).

Uses the same CLUSTERING_FEATURES base + CLUSTER_OHE_COLS as the scaled path,
so Phase 3 association rules are directly interpretable alongside Phase 2
cluster profiles.  Every feature is EDA §10-justified (see config.py comments).

CLUSTER_OHE_COLS are kept here as raw string categories (not OHE'd) because
Apriori benefits from the full label rather than binary dummies.

Binning strategy:
  Domain bins  : YEARS_BIRTH, YEARS_EMPLOYED, CREDIT_TERM_MONTHS, EXT_SOURCE_*,
                 CC_UTILIZATION_MEAN, ANNUITY_TO_INCOME
  Equal-freq q=4: all other continuous features → Low / Medium-Low / Medium-High / High
  Binary flags  : mapped to readable labels  (e.g. HasBureau / NoBureau)
  String cats   : kept as-is (already meaningful after step4 macro-sector mapping)

All values prefixed "ColName=" for unambiguous Apriori transaction items.

Output: datasets/final/features_discretized.csv
"""
import os
import numpy as np
import pandas as pd
from .config import OUTPUT_DIR, CLUSTERING_FEATURES, CLUSTER_OHE_COLS
from .utils import log, log_shape

_Q4_LABELS = ["Low", "Medium-Low", "Medium-High", "High"]

_CUSTOM_BINS = {
    # Demographics (EDA §4, §10)
    "YEARS_BIRTH": {
        "bins": [0, 30, 45, 60, np.inf],
        "labels": ["Age_18-30", "Age_30-45", "Age_45-60", "Age_60+"],
    },
    "YEARS_EMPLOYED": {
        "bins": [-np.inf, 0, 3, 10, np.inf],
        "labels": ["Unemployed/Pensioner", "Junior(<3yr)", "Mid(3-10yr)", "Senior(10yr+)"],
    },
    "CREDIT_TERM_MONTHS": {
        "bins": [0, 24, 48, 84, np.inf],
        "labels": ["Short(<2yr)", "Medium(2-4yr)", "Long(4-7yr)", "VeryLong(7yr+)"],
    },
    # EXT_SOURCE scores (EDA §11-12)
    "EXT_SOURCE_1": {
        "bins": [-np.inf, 0.4, 0.6, 0.8, np.inf],
        "labels": ["Low", "Medium-Low", "Medium-High", "High"],
    },
    "EXT_SOURCE_2": {
        "bins": [-np.inf, 0.4, 0.6, 0.8, np.inf],
        "labels": ["Low", "Medium-Low", "Medium-High", "High"],
    },
    "EXT_SOURCE_3": {
        "bins": [-np.inf, 0.4, 0.6, 0.8, np.inf],
        "labels": ["Low", "Medium-Low", "Medium-High", "High"],
    },
    # Credit card stress tiers (EDA §10: >80% = stress indicator)
    "CC_UTILIZATION_MEAN": {
        "bins": [-np.inf, 0.3, 0.6, 0.8, np.inf],
        "labels": ["Low(<30%)", "Moderate(30-60%)", "High(60-80%)", "Stressed(80%+)"],
    },
    "CC_UTILIZATION_MAX": {
        "bins": [-np.inf, 0.3, 0.6, 0.8, np.inf],
        "labels": ["Low(<30%)", "Moderate(30-60%)", "High(60-80%)", "Stressed(80%+)"],
    },
    # Debt-service burden tiers
    "ANNUITY_TO_INCOME": {
        "bins": [-np.inf, 0.1, 0.2, 0.35, np.inf],
        "labels": ["Low(<10%)", "Manageable(10-20%)", "Stretched(20-35%)", "Overextended(35%+)"],
    },
}

# Flag columns: 0/1 → domain-readable labels (EDA §10 flags)
_FLAG_LABELS = {
    "FLAG_SENTINEL_EMPLOYED":    {0: "Employed",    1: "NotEmployed"},
    "FLAG_NO_BUREAU":            {0: "HasBureau",   1: "NoBureau"},
    "FLAG_NO_CAR":               {0: "HasCar",      1: "NoCar"},
    "FLAG_NO_HOUSING_DATA":      {0: "HasHousing",  1: "NoHousingData"},
    "FLAG_EXT_SOURCE_1_MISSING": {0: "EXT1Present", 1: "EXT1Missing"},
}

# These columns are still raw strings in the pre-step8 engineered DataFrame.
# Map them to readable labels before the numeric flag branch runs.
_STRING_REMAP = {
    "CODE_GENDER":      {"F": "Female", "M": "Male"},
    "NAME_CONTRACT_TYPE": {"Cash loans": "CashLoan", "Revolving loans": "Revolving"},
}


def _qcut_safe(series: pd.Series, q: int = 4, labels=None) -> pd.Series:
    if labels is None:
        labels = _Q4_LABELS
    if not pd.api.types.is_numeric_dtype(series):
        return series.astype(str)
    # Replace inf values that would break quantile calculation
    series = series.replace([np.inf, -np.inf], np.nan)
    try:
        return pd.qcut(series, q=q, labels=labels, duplicates="drop").astype(str)
    except (ValueError, TypeError):
        return series.astype(str)


def run(df: pd.DataFrame) -> pd.DataFrame:
    log("Step 10 — Discretizing features for Apriori ...")
    df = df.copy()

    is_train = df["IS_TRAIN"].copy() if "IS_TRAIN" in df.columns else None

    # ── Select EDA-justified feature columns ──────────────────────────────
    select_cols = [
        c for c in CLUSTERING_FEATURES + CLUSTER_OHE_COLS
        if c in df.columns
    ]
    work = df[select_cols].copy()

    # Fill residual NaN before binning (YEARS_EMPLOYED NaN → 0 for sentinel rows)
    num_cols = work.select_dtypes(include=[np.number]).columns
    work[num_cols] = work[num_cols].fillna(0)
    for col in CLUSTER_OHE_COLS:
        if col in work.columns:
            work[col] = work[col].fillna("Unknown")

    # ── Pre-convert raw-string columns to readable labels ─────────────────
    # CODE_GENDER and NAME_CONTRACT_TYPE are still strings here (step8 hasn't run).
    for col, mapping in _STRING_REMAP.items():
        if col in work.columns:
            work[col] = work[col].map(mapping).fillna("Unknown")

    n_cont = n_flag = n_cat = 0

    for col in work.columns:
        series = work[col]

        # ── String categoricals first — never let object dtype reach numeric ops ─
        if series.dtype == object:
            n_cat += 1
            continue

        # ── Named flag columns → readable labels ─────────────────────────
        if col in _FLAG_LABELS:
            work[col] = series.astype(int).map(_FLAG_LABELS[col])
            n_flag += 1
            continue

        # ── Generic binary 0/1 ───────────────────────────────────────────
        uniq = set(series.dropna().unique())
        if series.dtype in [np.int8, bool] or uniq.issubset({0, 1, 0.0, 1.0}):
            work[col] = series.astype(int).map({0: "No", 1: "Yes"})
            n_flag += 1
            continue

        # ── Domain bins ──────────────────────────────────────────────────
        if col in _CUSTOM_BINS:
            cfg = _CUSTOM_BINS[col]
            work[col] = pd.cut(
                series,
                bins=cfg["bins"],
                labels=cfg["labels"],
                right=False,
                include_lowest=True,
            ).astype(str)
            n_cont += 1
            continue

        # ── Default: equal-frequency quartile bins ────────────────────────
        work[col] = _qcut_safe(series)
        n_cont += 1

    log(f"  Discretized: {n_cont} continuous, {n_flag} flags, {n_cat} categoricals kept")

    # ── Prefix col=value for unambiguous Apriori items ────────────────────
    for col in work.columns:
        work[col] = col + "=" + work[col].astype(str)

    if is_train is not None:
        work = pd.concat(
            [is_train.reset_index(drop=True), work.reset_index(drop=True)],
            axis=1,
        )

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(OUTPUT_DIR, "features_discretized.csv")
    work.to_csv(out_path, index=False)
    log(f"  Saved → {out_path}")
    log_shape("features_discretized", work)
    return work

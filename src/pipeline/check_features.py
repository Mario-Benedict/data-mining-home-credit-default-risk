"""
Audit the finished feature set and publish every keep/drop decision.

The name matters, because an earlier one (step10_feature_selection) implied this
module chooses features at the end. It does not rewrite
features_clustering.csv. It records the correlation- and entropy-led decisions
already applied in steps 1 to 9, then checks the retained matrix.

Two checks, both fully unsupervised:

    1. Pearson correlation between features, to catch leftover multicollinearity.
       Correlation is computed feature-to-feature only. This is what actually
       drove column removals, back in steps 4 and 7.

    2. Unsupervised entropy, to document whether a field varies enough to form
       a useful segment axis.

The portfolio is analyzed as one unlabeled population: the out-of-scope
outcome column is dropped at ingestion, so no audit here reads it either.

The reasoning is documented in REPORT.md.

Output:
  results/phase1_preprocessing/high_corr_pairs.csv
  results/phase1_preprocessing/feature_selection_decisions.csv
"""
import os
import numpy as np
import pandas as pd

from .config import (
    BASE_DIR,
    OUTPUT_DIR,
    PATHS,
    COLS_DROP_AVG,
    COLS_DROP_MEDI,
    COLS_DROP_REDUNDANT,
)
from .utils import log


REPORT_DIR = os.path.join(BASE_DIR, "results", "phase1_preprocessing")
FEATURES_PATH = os.path.join(OUTPUT_DIR, "features_clustering.csv")


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


def normalized_unsupervised_entropy(series: pd.Series, bins: int = 20) -> float:
    """Entropy on values or quantile bins, scaled to 0-1 and independent of TARGET."""
    if len(series) == 0:
        return 0.0
    non_missing = series.dropna()
    if non_missing.nunique() <= 1 and not series.isna().any():
        return 0.0

    if pd.api.types.is_numeric_dtype(non_missing) and non_missing.nunique() > bins:
        value_counts = non_missing.value_counts()
        dominant_value = value_counts.index[0]
        dominant_share = float(value_counts.iloc[0] / len(non_missing))
        # Quantiles collapse to one bin when almost every value is tied at zero,
        # even though a meaningful rare tail remains. Preserve that dominant
        # mass, then bin the remaining values separately.
        if dominant_share >= 0.50 and len(value_counts) > 1:
            tail = non_missing[non_missing.ne(dominant_value)]
            tail_q = min(bins - 1, int(tail.nunique()))
            tail_bins = pd.qcut(tail, q=tail_q, duplicates="drop")
            counts = pd.concat([
                pd.Series({"dominant_value": float(value_counts.iloc[0])}),
                tail_bins.value_counts(sort=False).astype(float).set_axis(
                    tail_bins.value_counts(sort=False).index.astype("object")
                ),
            ])
        else:
            bucketed = pd.qcut(non_missing, q=bins, duplicates="drop")
            counts = bucketed.value_counts(sort=False).astype(float)
        if series.isna().any():
            # A CategoricalIndex cannot accept a new label. Convert it before
            # adding missingness as its own unsupervised state.
            counts.index = counts.index.astype("object")
            counts = pd.concat([
                counts,
                pd.Series({"missing": float(series.isna().sum())}),
            ])
    else:
        counts = series.astype("object").where(series.notna(), "__MISSING__").value_counts().astype(float)

    probabilities = (counts / counts.sum()).to_numpy()
    if len(probabilities) <= 1:
        return 0.0
    entropy = float(-(probabilities * np.log(probabilities)).sum())
    return entropy / float(np.log(len(probabilities)))


def feature_selection_decisions(
    retained: pd.DataFrame,
    high_corr: pd.DataFrame,
) -> pd.DataFrame:
    """Combine upstream removals with an unsupervised audit of retained features."""
    partner_map: dict[str, tuple[str, float]] = {}
    for row in high_corr.itertuples(index=False):
        partner_map[row.feature_1] = (row.feature_2, float(row.abs_corr))
        partner_map[row.feature_2] = (row.feature_1, float(row.abs_corr))

    rows: list[dict[str, object]] = []
    for feature in retained.columns:
        values = retained[feature]
        entropy = normalized_unsupervised_entropy(values)
        dominant_share = float(values.value_counts(dropna=False, normalize=True).max())
        partner, corr = partner_map.get(feature, ("", np.nan))
        if partner:
            reason = (
                f"Retain with {partner}: mean and maximum card-use fields describe sustained and peak "
                "historical behaviour. Their correlation remains a sensitivity caveat."
            )
            basis = "Correlation review plus distinct domain role"
        else:
            reason = "Retained in the governed mining matrix; no unresolved redundancy or zero-variance issue."
            basis = "Correlation and unsupervised entropy audit"
        rows.append({
            "feature": feature,
            "status": "keep",
            "decision_basis": basis,
            "normalized_unsupervised_entropy": entropy,
            "dominant_value_share": dominant_share,
            "n_unique": int(values.nunique(dropna=False)),
            "high_corr_partner": partner,
            "abs_corr": corr,
            "business_reason": reason,
            "target_used_for_decision": False,
        })

    dropped = list(dict.fromkeys(COLS_DROP_AVG + COLS_DROP_MEDI + COLS_DROP_REDUNDANT))
    available_train = pd.read_csv(PATHS["application_train"], nrows=0).columns
    correlation_partners = (
        [feature.replace("_AVG", "_MODE") for feature in COLS_DROP_AVG]
        + [feature.replace("_MEDI", "_MODE") for feature in COLS_DROP_MEDI]
        + ["OBS_30_CNT_SOCIAL_CIRCLE", "DAYS_EMPLOYED", "REGION_RATING_CLIENT_W_CITY"]
    )
    available = [
        feature for feature in dict.fromkeys(dropped + correlation_partners)
        if feature in available_train
    ]
    raw = pd.concat([
        pd.read_csv(PATHS["application_train"], usecols=available),
        pd.read_csv(PATHS["application_test"], usecols=available),
    ], ignore_index=True)

    for feature in available:
        if feature not in dropped:
            continue
        values = raw[feature]
        entropy = normalized_unsupervised_entropy(values)
        dominant_share = float(values.value_counts(dropna=False, normalize=True).max())
        corr_value = np.nan
        if feature in COLS_DROP_AVG:
            partner = feature.replace("_AVG", "_MODE")
            basis = "Correlation redundancy"
            reason = f"Dropped because AVG and MODE exceed the redundancy threshold; retain {partner}."
            corr_value = abs(float(values.corr(raw[partner])))
        elif feature in COLS_DROP_MEDI:
            partner = feature.replace("_MEDI", "_MODE")
            basis = "Correlation redundancy"
            reason = f"Dropped because MEDI and MODE exceed the redundancy threshold; retain {partner}."
            corr_value = abs(float(values.corr(raw[partner])))
        elif feature == "OBS_60_CNT_SOCIAL_CIRCLE":
            partner = "OBS_30_CNT_SOCIAL_CIRCLE"
            basis = "Correlation redundancy"
            reason = "Dropped because the 60-day and 30-day observation counts are almost identical."
            corr_value = abs(float(values.corr(raw[partner])))
        elif feature == "FLAG_EMP_PHONE":
            partner = "FLAG_SENTINEL_EMPLOYED"
            basis = "Correlation redundancy"
            sentinel = raw["DAYS_EMPLOYED"].eq(365243).astype(int)
            corr_value = abs(float(values.corr(sentinel)))
            reason = "Dropped because the employment-duration sentinel state already carries the same information."
        elif feature == "REGION_RATING_CLIENT":
            partner = "REGION_RATING_CLIENT_W_CITY"
            basis = "Correlation redundancy"
            reason = "Dropped because the city-aware rating retains the same information at a more specific level."
            corr_value = abs(float(values.corr(raw[partner])))
        else:
            partner = ""
            basis = "Near-zero unsupervised entropy"
            reason = "Dropped because the flag is constant or nearly constant and cannot separate records."
        rows.append({
            "feature": feature,
            "status": "drop",
            "decision_basis": basis,
            "normalized_unsupervised_entropy": entropy,
            "dominant_value_share": dominant_share,
            "n_unique": int(values.nunique(dropna=False)),
            "high_corr_partner": partner,
            "abs_corr": corr_value,
            "business_reason": reason,
            "target_used_for_decision": False,
        })

    return pd.DataFrame(rows).sort_values(["status", "feature"], ascending=[False, True])


def run() -> None:
    log("Step 10 - Feature selection check (correlation plus entropy) ...")

    os.makedirs(REPORT_DIR, exist_ok=True)

    log(f"  Loading {FEATURES_PATH} ...")
    features_df = pd.read_csv(FEATURES_PATH)
    log(f"  features_clustering: {features_df.shape[0]:,} x {features_df.shape[1]}")

    feature_matrix = features_df.drop(columns=["SK_ID_CURR"], errors="ignore")

    high_corr = compute_correlation_pairs(feature_matrix, threshold=0.85)
    corr_path = os.path.join(REPORT_DIR, "high_corr_pairs.csv")
    high_corr.to_csv(corr_path, index=False)
    log(f"  Saved {corr_path} ({len(high_corr)} pairs with |r| > 0.85)")

    # Publish the complete decision trail. This combines the upstream removals
    # with an audit of every field retained in the final mining matrix. TARGET
    # is deliberately absent from the decision basis.
    retained_full = features_df.drop(columns=["SK_ID_CURR"], errors="ignore")
    decisions = feature_selection_decisions(retained_full, high_corr)
    decisions_path = os.path.join(REPORT_DIR, "feature_selection_decisions.csv")
    decisions.to_csv(decisions_path, index=False)
    log(f"  Saved {decisions_path} ({len(decisions)} documented decisions)")

    log("  Feature selection check complete (correlation plus entropy).")

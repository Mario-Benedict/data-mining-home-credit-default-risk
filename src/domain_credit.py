"""Domain-led interpretation helpers for the Home Credit mining project.

The statistical phases identify unusual geometry and portfolio segments. This
module translates those outputs into review evidence without turning an
unsupervised pattern into an approval/decline decision.

Design rules
------------
* Use unscaled business values for every threshold and explanation.
* Separate inconsistent data from repayment evidence and from a rare but
  plausible application profile.
* Treat missing or thin credit history as uncertainty, not bad behaviour.
* Include the applicant's actual values in every exported recommendation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np
import pandas as pd


METHOD_COLUMNS = {
    "is_iqr_outlier": "Adjusted IQR",
    "is_zscore_outlier": "Calibrated Z-score",
    "is_mahalanobis_outlier": "Shrinkage Mahalanobis",
    "is_isolation_outlier": "Isolation Forest",
    "is_lof_outlier": "Local Outlier Factor",
}

SAMPLED_DENSITY_STATES = (
    "Not assessed",
    "Assessed (not isolated)",
    "Assessed (isolated)",
)

EVIDENCE_FEATURE_LABELS = {
    "AMT_INCOME_TOTAL": "reported income",
    "AMT_CREDIT": "current-loan credit amount",
    "AMT_ANNUITY": "annuity amount",
    "CREDIT_TO_INCOME": "credit-to-income ratio",
    "ANNUITY_TO_INCOME": "annuity-to-income ratio",
    "CREDIT_TO_ANNUITY": "credit-to-annuity payment-size proxy",
    "BUREAU_COUNT": "bureau record count",
    "BUREAU_DEBT_TO_CREDIT_RATIO": "bureau debt-to-credit ratio",
    "BUREAU_BB_DPD_RATIO_MEAN": "average late-payment share in bureau monthly history",
    "BUREAU_BB_SEVERE_DPD_MEAN": "average severe-late share in bureau monthly history",
    "PREV_COUNT": "previous application count",
    "PREV_REFUSED_COUNT": "previous refusal count",
    "INST_DPD_MEAN": "average instalment delay",
    "INST_DPD_MAX": "longest instalment delay",
    "INST_LATE_RATIO": "late-instalment share",
    "INST_SEVERE_LATE_RATIO": "severely late instalment share",
    "INST_PAYMENT_RATIO_MEAN": "average payment-to-due ratio",
    "INST_COUNT": "instalment record count",
    "POS_SK_DPD_MEAN": "average previous-account POS or cash-loan delay",
    "POS_MONTHS_COUNT": "previous-account POS or cash-loan monthly record count",
    "CC_UTILIZATION_MEAN": "average previous-account card utilisation",
    "CC_UTILIZATION_MAX": "maximum previous-account card utilisation",
    "CC_SK_DPD_MEAN": "average previous-account card delay",
    "CC_AMT_BALANCE_MEAN": "average previous-account card balance",
}


@dataclass(frozen=True)
class Evidence:
    driver: str
    severity: int
    evidence: str
    action: str
    owner: str


def _number(row: pd.Series, column: str) -> float:
    value = row.get(column, np.nan)
    try:
        return float(value)
    except (TypeError, ValueError):
        return np.nan


def _source_number(row: pd.Series, column: str) -> float:
    """Return the preserved source value when the pipeline exported one.

    A present-but-missing SOURCE_* value deliberately stays missing; falling
    back to an imputed model value would make an explanation claim that an
    unobserved value was actually supplied by the applicant or score provider.
    """
    source = f"SOURCE_{column}"
    if source in row.index:
        return _number(row, source)
    return _number(row, column)


def _present(value: float) -> bool:
    return bool(np.isfinite(value))


def _pct(value: float, digits: int = 1) -> str:
    return "missing" if not _present(value) else f"{value * 100:.{digits}f}%"


def _num(value: float, digits: int = 2) -> str:
    return "missing" if not _present(value) else f"{value:,.{digits}f}"


def _feature_value_text(column: str, value: float) -> str:
    """Format an unscaled feature value without inventing a currency or unit."""
    if not _present(value):
        return "missing in the business-value file"
    if column in {
        "ANNUITY_TO_INCOME", "BUREAU_BB_DPD_RATIO_MEAN",
        "BUREAU_BB_SEVERE_DPD_MEAN", "INST_LATE_RATIO",
        "INST_SEVERE_LATE_RATIO", "CC_UTILIZATION_MEAN",
        "CC_UTILIZATION_MAX",
    }:
        return _pct(value, 2)
    if column in {"CREDIT_TO_INCOME", "BUREAU_DEBT_TO_CREDIT_RATIO", "INST_PAYMENT_RATIO_MEAN"}:
        return f"{value:,.2f}x"
    if "DPD" in column:
        return f"{value:,.2f} days"
    if column.endswith("COUNT"):
        return f"{value:,.0f}"
    return _num(value)


def _extreme_axis_evidence(row: pd.Series) -> Evidence | None:
    feature = str(row.get("_EXTREME_FEATURE", "")).strip()
    standardized_value = _number(row, "_EXTREME_STANDARDIZED_VALUE")
    if not feature or not _present(standardized_value) or abs(standardized_value) < 10:
        return None
    label = EVIDENCE_FEATURE_LABELS.get(feature, feature.replace("_", " ").lower())
    business_value = _source_number(row, feature)
    return Evidence(
        f"Extreme {label}",
        3,
        f"{label} is {_feature_value_text(feature, business_value)}; its prepared detection value is "
        f"{standardized_value:+.1f} standard deviations from the portfolio mean, so this is the exact field "
        "that needs the single-axis source check",
        f"reconcile {label} and its contributing source fields for sign, units, joins, and aggregation. "
        "If confirmed, keep the value as verified evidence and continue the appropriate affordability or repayment review",
        "Data Operations / Credit Review",
    )


def _as_sentence(value: str) -> str:
    text = str(value).strip()
    if not text:
        return ""
    text = text[0].upper() + text[1:]
    return text if text.endswith((".", "!", "?")) else f"{text}."


def _join_sentences(values: Iterable[str]) -> str:
    return " ".join(_as_sentence(value) for value in values if str(value).strip())


def _natural_join(values: Iterable[str]) -> str:
    items = list(dict.fromkeys(str(value).strip() for value in values if str(value).strip()))
    if len(items) < 2:
        return items[0] if items else ""
    if len(items) == 2:
        return " and ".join(items)
    return f"{', '.join(items[:-1])}, and {items[-1]}"


def _methods_fired(row: pd.Series) -> list[str]:
    fired = []
    for column, label in METHOD_COLUMNS.items():
        value = row.get(column, 0)
        if pd.notna(value) and int(value) == 1:
            fired.append(label)
    return fired


def _nullable_boolean(value: object, field: str) -> bool | None:
    """Read a CSV-safe nullable Boolean without treating missing as false."""
    if pd.isna(value):
        return None
    if isinstance(value, (bool, np.bool_)):
        return bool(value)
    if isinstance(value, (int, np.integer)) and int(value) in {0, 1}:
        return bool(value)
    if isinstance(value, (float, np.floating)) and float(value) in {0.0, 1.0}:
        return bool(value)
    if isinstance(value, str):
        normalized = value.strip().lower()
        if normalized in {"true", "1"}:
            return True
        if normalized in {"false", "0"}:
            return False
    raise ValueError(f"{field} contains an invalid Boolean value: {value!r}")


def _sampled_density_state(row: pd.Series) -> str:
    """Describe DBSCAN sample coverage separately from its isolation result."""
    covered = _nullable_boolean(
        row.get("dbscan_sample_covered", pd.NA), "dbscan_sample_covered"
    )
    noise = _nullable_boolean(
        row.get("dbscan_sample_noise", pd.NA), "dbscan_sample_noise"
    )
    if covered is not True:
        if noise is not None:
            raise ValueError(
                "dbscan_sample_noise must be missing when dbscan_sample_covered is false."
            )
        return "Not assessed"
    if noise is None:
        raise ValueError(
            "dbscan_sample_noise must be present when dbscan_sample_covered is true."
        )
    return "Assessed (isolated)" if noise else "Assessed (not isolated)"


OUTLIER_TYPES = (
    "Point (globally extreme single value)",
    "Collective (sampled sparse-density group)",
    "Contextual (unusual multivariate combination)",
)


def _outlier_type(row: pd.Series) -> str:
    """Classify the record in the point / contextual / collective typology.

    Precedence: a value >=10 SD on one prepared axis is anomalous with no
    context at all, so it outranks the sampled density view; DBSCAN noise
    corroboration marks records isolated together in the sampled embedding;
    everything else entered on multivariate detector agreement alone, i.e.
    each individual value is plausible and only the combination is unusual.
    """
    extreme = _nullable_boolean(
        row.get("extreme_single_axis", pd.NA), "extreme_single_axis"
    )
    if extreme is True:
        return OUTLIER_TYPES[0]
    noise = _nullable_boolean(
        row.get("dbscan_sample_noise", pd.NA), "dbscan_sample_noise"
    )
    if noise is True:
        return OUTLIER_TYPES[1]
    return OUTLIER_TYPES[2]


def _segment_reference(
    business: pd.DataFrame,
    labels: pd.DataFrame,
    candidates: Iterable[str],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    joined = business.merge(
        labels[["ROW_ID", "CLUSTER_KMEANS"]], on="ROW_ID", how="inner"
    )
    cols = [c for c in candidates if c in joined.columns]
    med = joined.groupby("CLUSTER_KMEANS")[cols].median(numeric_only=True)
    mad_rows = []
    for cid, group in joined.groupby("CLUSTER_KMEANS"):
        row = {"CLUSTER_KMEANS": cid}
        for col in cols:
            values = pd.to_numeric(group[col], errors="coerce")
            median = med.loc[cid, col]
            mad = np.nanmedian(np.abs(values - median)) * 1.4826
            if not np.isfinite(mad) or mad <= 1e-12:
                q1, q3 = np.nanpercentile(values, [25, 75])
                mad = (q3 - q1) / 1.349
            row[col] = mad if np.isfinite(mad) and mad > 1e-12 else np.nan
        mad_rows.append(row)
    mad = pd.DataFrame(mad_rows).set_index("CLUSTER_KMEANS")
    return med, mad


def _logical_data_checks(row: pd.Series) -> list[Evidence]:
    issues: list[Evidence] = []
    income = _source_number(row, "AMT_INCOME_TOTAL")
    credit = _source_number(row, "AMT_CREDIT")
    annuity = _source_number(row, "AMT_ANNUITY")
    age = _number(row, "YEARS_BIRTH")
    employed = _number(row, "YEARS_EMPLOYED")
    payment_ratio = _number(row, "INST_PAYMENT_RATIO_MEAN")

    for label, value in [
        ("income", income), ("credit amount", credit), ("annuity", annuity)
    ]:
        if _present(value) and value <= 0:
            issues.append(Evidence(
                "Non-positive financial amount", 3,
                f"{label} is {_num(value)}, although this field should be positive",
                f"check the {label} against the original application before using it",
                "Data Operations",
            ))

    if _present(age) and not 18 <= age <= 100:
        issues.append(Evidence(
            "Age outside the review range", 3, f"recorded age is {_num(age, 1)} years",
            "check the birth date in the original application and confirm that the age was calculated correctly",
            "Data Operations",
        ))
    if _present(age) and _present(employed) and employed > max(age - 14, 0) + 0.5:
        issues.append(Evidence(
            "Employment history exceeds feasible working life", 3,
            f"employment tenure is {_num(employed, 1)} years for age {_num(age, 1)}",
            "check the employment start date and any placeholder value against the source record",
            "Data Operations",
        ))
    if _present(payment_ratio) and (payment_ratio < 0 or payment_ratio > 3):
        issues.append(Evidence(
            "Payment ratio needs checking", 2,
            f"mean paid-to-due ratio is {_num(payment_ratio, 2)}x",
            "check for reversals, early payments, duplicate instalments, and inconsistent currency units",
            "Data Operations",
        ))

    for col in ["EXT_SOURCE_1", "EXT_SOURCE_2", "EXT_SOURCE_3"]:
        value = _number(row, col)
        if _present(value) and not 0 <= value <= 1:
            issues.append(Evidence(
                "External score outside expected range", 3,
                f"{col} is {_num(value, 3)} rather than a value from 0 to 1",
                f"check {col} against the score provider or preprocessing record",
                "Data Operations",
            ))
    return issues


def _repayment_risk_evidence(row: pd.Series) -> list[Evidence]:
    signals: list[Evidence] = []
    source_income = _source_number(row, "AMT_INCOME_TOTAL")
    source_credit = _source_number(row, "AMT_CREDIT")
    source_annuity = _source_number(row, "AMT_ANNUITY")
    ati = (
        source_annuity / source_income
        if _present(source_annuity) and _present(source_income) and source_income > 0
        else np.nan
    )
    cti = (
        source_credit / source_income
        if _present(source_credit) and _present(source_income) and source_income > 0
        else np.nan
    )
    inst_max = _number(row, "INST_DPD_MAX")
    late = _number(row, "INST_LATE_RATIO")
    severe_late = _number(row, "INST_SEVERE_LATE_RATIO")
    pay_ratio = _number(row, "INST_PAYMENT_RATIO_MEAN")
    util_mean = _number(row, "CC_UTILIZATION_MEAN")
    util_max = _number(row, "CC_UTILIZATION_MAX")
    cc_dpd = _number(row, "CC_SK_DPD_MEAN")
    pos_dpd = _number(row, "POS_SK_DPD_MEAN")
    bureau_debt = _number(row, "BUREAU_DEBT_TO_CREDIT_RATIO")
    bureau_dpd = _number(row, "BUREAU_BB_DPD_RATIO_MEAN")
    bureau_severe = _number(row, "BUREAU_BB_SEVERE_DPD_MEAN")
    prev_refused = _number(row, "PREV_REFUSED_COUNT")
    approval = _number(row, "PREV_APPROVAL_RATE")

    if _present(ati) and ati >= 0.35:
        severity = 3 if ati >= 0.50 else 2
        signals.append(Evidence(
            "High payment burden", severity,
            f"scheduled annuity equals {_pct(ati)} of reported income",
            "confirm sustainable income and check whether the payments still work if income falls",
            "Senior Underwriter",
        ))
    if _present(cti) and cti >= 6:
        severity = 3 if cti >= 8 else 2
        signals.append(Evidence(
            "High credit compared with income", severity,
            f"current-loan credit amount equals {_num(cti, 1)} times reported income",
            "confirm all current obligations and check whether the applicant could still pay if income falls",
            "Senior Underwriter",
        ))
    if _present(inst_max) and inst_max > 30:
        severity = 3 if inst_max >= 90 else 2
        signals.append(Evidence(
            "Long instalment delay", severity,
            f"the longest observed instalment delay is {_num(inst_max, 0)} days",
            "review the payment timeline. If the customer is already in hardship, follow the contact or restructuring policy",
            "Credit Review / Customer Assistance",
        ))
    if _present(severe_late) and severe_late >= 0.05:
        signals.append(Evidence(
            "Repeated severe instalment delays", 3,
            f"{_pct(severe_late)} of observed instalments were more than 30 days late",
            "check how often the delays happened, how recent they were, and whether the account was brought up to date",
            "Credit Review / Customer Assistance",
        ))
    elif _present(late) and late >= 0.20:
        signals.append(Evidence(
            "Frequent instalment delays", 2,
            f"{_pct(late)} of observed instalments were late",
            "check when and why the late payments happened, then confirm that the proposed schedule is affordable",
            "Credit Review",
        ))
    if _present(pay_ratio) and 0 <= pay_ratio < 0.90:
        signals.append(Evidence(
            "Repeated underpayment", 2,
            f"the average payment is {_pct(pay_ratio)} of the amount due",
            "check the previous-loan payment timeline for partial payments, reversals, and cure, then verify whether any related obligation is still open",
            "Credit Review",
        ))
    if (_present(util_mean) and util_mean >= 0.80) or (_present(util_max) and util_max >= 1.0):
        evidence = (
            f"average utilisation in previous Home Credit card accounts is {_pct(util_mean)} and the historical maximum is {_pct(util_max)}"
        )
        signals.append(Evidence(
            "High card utilisation", 2, evidence,
            "verify whether a revolving facility is still open. Only then obtain its current balance and payment status, assess capacity, and consider limit suitability. Historical utilisation alone does not prove financial distress",
            "Revolving Credit Review",
        ))
    max_dpd = np.nanmax([cc_dpd, pos_dpd]) if any(_present(v) for v in [cc_dpd, pos_dpd]) else np.nan
    if _present(max_dpd) and max_dpd > 0:
        signals.append(Evidence(
            "Card or POS arrears", 2,
            f"average days past due reaches {_num(max_dpd, 1)} days in previous Home Credit card or POS history",
            "check the source timeline, recency, severity, and cure status, then verify whether any related facility or obligation remains open",
            "Credit Review",
        ))
    if _present(bureau_debt) and bureau_debt >= 0.80:
        signals.append(Evidence(
            "High bureau debt utilisation", 2,
            f"bureau debt is {_pct(bureau_debt)} of recorded bureau credit",
            "confirm outstanding external debts and include them in the affordability calculation",
            "Senior Underwriter",
        ))
    if (_present(bureau_severe) and bureau_severe >= 0.02) or (_present(bureau_dpd) and bureau_dpd >= 0.10):
        signals.append(Evidence(
            "Late payments in bureau history", 3,
            f"bureau history shows {_pct(bureau_dpd)} of months with a late payment and {_pct(bureau_severe)} with a severe late payment",
            "check how recent the bureau arrears are, whether they are disputed, and whether they were cured",
            "Credit Review",
        ))

    ext_values = []
    for col in ["EXT_SOURCE_1", "EXT_SOURCE_2", "EXT_SOURCE_3"]:
        missing_flag = row.get(f"FLAG_{col}_MISSING", 0)
        if pd.notna(missing_flag) and int(missing_flag) == 1:
            continue
        value = _source_number(row, col)
        if _present(value):
            ext_values.append(value)
    if ext_values and np.mean(ext_values) < 0.30:
        signals.append(Evidence(
            "Low combined external score", 2,
            f"the average available external score is {_num(float(np.mean(ext_values)), 3)}",
            "verify which external scores were observed and their source validity, then reconcile them with directly observed bureau, income, and repayment evidence. Do not use the combined mean as a reason code",
            "Senior Underwriter",
        ))
    if _present(prev_refused) and prev_refused >= 3 and _present(approval) and approval < 0.50:
        signals.append(Evidence(
            "Repeated previous application refusals", 1,
            f"{_num(prev_refused, 0)} prior applications were refused and historical approval rate is {_pct(approval)}",
            "check why earlier applications were refused and whether those reasons still apply",
            "Credit Review",
        ))
    return signals


def _rare_profile_evidence(
    row: pd.Series,
    medians: pd.DataFrame,
    scales: pd.DataFrame,
    top_n: int = 2,
) -> list[Evidence]:
    cid = int(row["CLUSTER_KMEANS"])
    if cid not in medians.index:
        return []
    candidates = []
    for col in medians.columns:
        value = _number(row, col)
        median = medians.loc[cid, col]
        scale = scales.loc[cid, col]
        if _present(value) and _present(median) and _present(scale) and scale > 0:
            score = abs(value - median) / scale
            candidates.append((score, col, value, median))
    candidates.sort(reverse=True)

    evidence = []
    for score, col, value, median in candidates[:top_n]:
        label = EVIDENCE_FEATURE_LABELS.get(col, col.replace("_", " ").lower())
        evidence.append(Evidence(
            f"Unusual {label}", 1,
            f"{label} is {_num(value)} compared with the cluster median of {_num(median)} ({score:.1f} robust deviations)",
            f"check {label} against its usual source. If it is correct, continue with standard underwriting",
            "Standard Underwriting",
        ))
    return evidence


def build_anomaly_investigation(
    business: pd.DataFrame,
    combined: pd.DataFrame,
    labels: pd.DataFrame,
    cluster_names: pd.DataFrame,
    anomaly_features: pd.DataFrame | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Build one evidence-backed recommendation per targeted-review record."""
    names = dict(zip(cluster_names["cluster_id"].astype(int), cluster_names["nama"]))
    required_density_fields = {"dbscan_sample_covered", "dbscan_sample_noise"}
    missing_density_fields = required_density_fields.difference(combined.columns)
    if missing_density_fields:
        raise ValueError(
            "anomaly_combined is missing sampled-density context fields: "
            f"{sorted(missing_density_fields)}"
        )
    label_cols = ["ROW_ID", "CLUSTER_KMEANS"]
    label_view = labels[label_cols].drop_duplicates("ROW_ID")
    targeted_labels = {"TARGETED_REVIEW", "HIGH_CONFIDENCE_ANOMALY"}
    focus_ids = combined.loc[
        combined["anomaly_category"].isin(targeted_labels), "ROW_ID"
    ]

    merged = business[business["ROW_ID"].isin(focus_ids)].merge(
        combined, on="ROW_ID", how="inner", suffixes=("", "_det")
    )
    if "CLUSTER_KMEANS" not in merged.columns:
        merged = merged.merge(label_view, on="ROW_ID", how="left")
    if anomaly_features is not None:
        if "SK_ID_CURR" not in anomaly_features:
            raise ValueError("anomaly_features must contain SK_ID_CURR")
        feature_view = anomaly_features.loc[
            anomaly_features["SK_ID_CURR"].isin(merged["SK_ID_CURR"])
        ].drop_duplicates("SK_ID_CURR")
        feature_columns = [
            column for column in feature_view.columns
            if column not in {"ROW_ID", "SK_ID_CURR"}
            and pd.api.types.is_numeric_dtype(feature_view[column])
        ]
        if not feature_columns:
            raise ValueError("anomaly_features has no numeric detection columns")
        prepared = feature_view[feature_columns].apply(pd.to_numeric, errors="coerce")
        prepared_abs = prepared.abs().fillna(-np.inf).to_numpy()
        peak_positions = prepared_abs.argmax(axis=1)
        prepared_values = prepared.to_numpy()
        extreme_lookup = pd.DataFrame({
            "SK_ID_CURR": feature_view["SK_ID_CURR"].astype(int).to_numpy(),
            "_EXTREME_FEATURE": np.asarray(feature_columns, dtype=object)[peak_positions],
            "_EXTREME_STANDARDIZED_VALUE": prepared_values[
                np.arange(len(feature_view)), peak_positions
            ],
        })
        merged = merged.merge(
            extreme_lookup,
            on="SK_ID_CURR",
            how="left",
            validate="one_to_one",
        )
    else:
        merged["_EXTREME_FEATURE"] = ""
        merged["_EXTREME_STANDARDIZED_VALUE"] = np.nan

    reference_cols = [
        "AMT_INCOME_TOTAL", "AMT_CREDIT", "AMT_ANNUITY",
        "CREDIT_TO_INCOME", "ANNUITY_TO_INCOME", "CREDIT_TO_ANNUITY",
        "BUREAU_COUNT", "BUREAU_DEBT_TO_CREDIT_RATIO", "PREV_COUNT",
        "INST_DPD_MAX", "INST_LATE_RATIO", "INST_PAYMENT_RATIO_MEAN",
        "INST_COUNT",
        "CC_UTILIZATION_MEAN", "CC_UTILIZATION_MAX", "CC_AMT_BALANCE_MEAN",
    ]
    medians, scales = _segment_reference(business, labels, reference_cols)

    rows = []
    driver_rows = []
    for _, row in merged.iterrows():
        cid = int(row["CLUSTER_KMEANS"])
        segment = names.get(cid, f"Cluster {cid}")
        queue_route = str(row.get("queue_route", "Detector consensus")).replace(
            "Implausible single value", "Extreme single-axis value"
        )
        data_issues = _logical_data_checks(row)
        risk_signals = _repayment_risk_evidence(row)
        rare_signals = _rare_profile_evidence(row, medians, scales)
        extreme_signal = _extreme_axis_evidence(row)

        if data_issues:
            review_type = "Data consistency check"
            evidence = sorted(data_issues, key=lambda x: x.severity, reverse=True)
            interpretation = (
                "One or more values conflict with their expected range or units. Confirm the source data before using this record. "
                "The anomaly is a data-quality issue, not evidence of payment difficulty."
            )
        elif risk_signals:
            review_type = "Affordability / repayment review"
            evidence = sorted(risk_signals, key=lambda x: x.severity, reverse=True)
            interpretation = (
                "The record contains a specific affordability or repayment concern. A reviewer should check the underlying history "
                "and the applicant's current circumstances before any credit action."
            )
        else:
            review_type = "Rare but plausible profile"
            evidence = rare_signals or [Evidence(
                "Unusual combination", 1,
                "the combination is unusual, although no affordability, repayment, or data-quality threshold was triggered",
                "check the unusual values. If they are correct, continue with standard underwriting",
                "Standard Underwriting",
            )]
            interpretation = (
                "The record is unusual for its cluster, but no affordability, repayment, or data-quality threshold was triggered. "
                "Check the unusual values, then continue with standard review if they are correct."
            )

        if extreme_signal is not None:
            evidence = [extreme_signal, *[item for item in evidence if item.driver != extreme_signal.driver]]

        top = evidence[:3]
        primary = top[0]
        primary_fact = _as_sentence(primary.evidence)
        if review_type == "Data consistency check":
            interpretation = (
                f"Start with {primary.driver.lower()}: {primary_fact} Until the source is reconciled, this value "
                "could distort the application assessment. The check does not establish payment difficulty."
            )
        elif review_type == "Affordability / repayment review":
            interpretation = (
                f"The first review point is {primary.driver.lower()}: {primary_fact} This can affect the view of "
                "affordability or repayment history, but recency, cure status, and the applicant's current position "
                "still need to be verified."
            )
        else:
            interpretation = (
                f"The main unusual point is {primary.driver.lower()}: {primary_fact} Rarity is a prompt to verify "
                "the source, not evidence for an adverse credit conclusion."
            )
        if extreme_signal is not None and queue_route == "Extreme single-axis value":
            interpretation += (
                " This is the exact field behind the single-axis queue entry; its standardized distance does not "
                "prove an error or payment difficulty."
            )
        elif extreme_signal is not None:
            interpretation += (
                " The record also contains a field at least 10 standard deviations from the portfolio mean, "
                "although agreement among portfolio-wide detectors remains its queue-entry route."
            )
        methods = _methods_fired(row)
        scope = (
            "Portfolio single-axis extreme"
            if queue_route == "Extreme single-axis value"
            else "Detector-consensus pattern"
        )
        sampled_density_corroboration = _sampled_density_state(row)
        outlier_type = _outlier_type(row)

        max_severity = max(e.severity for e in evidence)
        priority = (
            "Urgent data reconciliation" if review_type == "Data consistency check" and max_severity >= 3
            else "High-priority human review" if max_severity >= 3
            else "Targeted human review" if max_severity == 2
            else "Standard review"
        )
        actual_evidence = _join_sentences(e.evidence for e in top)
        actions = []
        for e in top:
            if e.action not in actions:
                actions.append(e.action)
        recommendation = (
            f"Applicant {int(row['SK_ID_CURR'])}: start with {primary.driver.lower()}: {primary.evidence}. "
            f"{_join_sentences(actions)} "
            "Document the facts confirmed during review. Base any credit action on those facts, "
            "not the anomaly or cluster label."
        )
        owner_parts = [
            owner.strip()
            for evidence in top
            for owner in evidence.owner.split(" / ")
            if owner.strip()
        ]
        owners = _natural_join(owner_parts)

        output = {
            "ROW_ID": int(row["ROW_ID"]),
            "SK_ID_CURR": int(row["SK_ID_CURR"]),
            "Cluster": f"cluster_{cid}",
            "Segment": segment,
            "Detected By": ", ".join(methods),
            "Detector Count": len(methods),
            "Queue Route": queue_route,
            "Anomaly Scope": scope,
            "Outlier Type": outlier_type,
            "Sampled Density Corroboration": sampled_density_corroboration,
            "Review Type": review_type,
            "Priority": priority,
            "Primary Driver": primary.driver,
            "Record Evidence": actual_evidence,
            "Business Interpretation": interpretation,
            "Recommended Action": recommendation,
            "Review Owner": owners,
            "Automatic Decision Allowed": "No",
            "Extreme Trigger Field": str(row.get("_EXTREME_FEATURE", "")),
            "Extreme Trigger Standardized Value": _number(row, "_EXTREME_STANDARDIZED_VALUE"),
            "Extreme Trigger Business Value": _feature_value_text(
                str(row.get("_EXTREME_FEATURE", "")),
                _source_number(row, str(row.get("_EXTREME_FEATURE", ""))),
            ) if extreme_signal is not None else "",
            "Evidence Value Basis": "Uses original source values where available and observed history summaries otherwise",
        }
        rows.append(output)
        for item in evidence:
            driver_rows.append({
                "SK_ID_CURR": int(row["SK_ID_CURR"]),
                "Segment": segment,
                "Review Type": review_type,
                "Driver": item.driver,
                "Severity": item.severity,
            })

    investigation = pd.DataFrame(rows)
    priority_order = {
        "Urgent data reconciliation": 0,
        "High-priority human review": 1,
        "Targeted human review": 2,
        "Standard review": 3,
    }
    investigation["_priority_order"] = investigation["Priority"].map(priority_order).fillna(9)
    investigation = investigation.sort_values(
        ["_priority_order", "Detector Count"], ascending=[True, False]
    ).drop(columns="_priority_order")
    drivers = pd.DataFrame(driver_rows)
    driver_summary = (
        drivers.groupby(["Review Type", "Driver"], as_index=False)
        .agg(records=("SK_ID_CURR", "nunique"), mean_severity=("Severity", "mean"))
        .sort_values(["records", "mean_severity"], ascending=False)
    )
    return investigation, driver_summary

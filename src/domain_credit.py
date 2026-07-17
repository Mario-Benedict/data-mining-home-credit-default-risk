"""Domain-led interpretation helpers for the Home Credit mining project.

The statistical phases identify unusual geometry and portfolio segments. This
module translates those outputs into review evidence without turning an
unsupervised pattern into an approval/decline decision.

Design rules
------------
* Use unscaled business values for every threshold and explanation.
* Separate impossible/inconsistent data from repayment-risk evidence and from
  a rare-but-plausible customer profile.
* Treat missing or thin credit history as uncertainty, not bad behaviour.
* Include the applicant's actual values in every exported recommendation.
* Keep cluster-based TARGET analysis as a train-only, out-of-fold backtest.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np
import pandas as pd
from sklearn.metrics import (
    average_precision_score,
    brier_score_loss,
    confusion_matrix,
    f1_score,
    precision_recall_curve,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold


METHOD_COLUMNS = {
    "is_iqr_outlier": "Adjusted IQR",
    "is_zscore_outlier": "Calibrated Z-score",
    "is_mahalanobis_outlier": "Robust Mahalanobis",
    "is_isolation_outlier": "Isolation Forest",
    "is_lof_outlier": "Local Outlier Factor",
    "IS_OUTLIER": "DBSCAN noise",
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


def _methods_fired(row: pd.Series) -> list[str]:
    fired = []
    for column, label in METHOD_COLUMNS.items():
        value = row.get(column, 0)
        if pd.notna(value) and int(value) == 1:
            fired.append(label)
    return fired


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
    term = credit / annuity if _present(credit) and _present(annuity) and annuity > 0 else np.nan
    payment_ratio = _number(row, "INST_PAYMENT_RATIO_MEAN")

    for label, value in [
        ("income", income), ("credit amount", credit), ("annuity", annuity)
    ]:
        if _present(value) and value <= 0:
            issues.append(Evidence(
                "Non-positive financial amount", 3,
                f"{label} is {_num(value)}, although this field should be positive",
                f"reconcile the {label} with the source application before any underwriting use",
                "Data Operations",
            ))

    if _present(age) and not 18 <= age <= 100:
        issues.append(Evidence(
            "Implausible age", 3, f"recorded age is {_num(age, 1)} years",
            "verify the birth-date transformation and original application document",
            "Data Operations",
        ))
    if _present(age) and _present(employed) and employed > max(age - 14, 0) + 0.5:
        issues.append(Evidence(
            "Employment history exceeds feasible working life", 3,
            f"employment tenure is {_num(employed, 1)} years for age {_num(age, 1)}",
            "reconcile employment start date and sentinel handling with the source record",
            "Data Operations",
        ))
    if _present(term) and (term <= 0 or term > 600):
        issues.append(Evidence(
            "Implausible implied term", 3,
            f"credit divided by annuity implies {_num(term, 1)} payment periods",
            "verify credit and annuity units and the contracted repayment schedule",
            "Data Operations",
        ))
    if _present(payment_ratio) and (payment_ratio < 0 or payment_ratio > 3):
        issues.append(Evidence(
            "Installment ratio needs reconciliation", 2,
            f"mean paid-to-due ratio is {_num(payment_ratio, 2)}x",
            "check reversals, prepayments, duplicated installments, and currency units",
            "Data Operations",
        ))

    for col in ["EXT_SOURCE_1", "EXT_SOURCE_2", "EXT_SOURCE_3"]:
        value = _number(row, col)
        if _present(value) and not 0 <= value <= 1:
            issues.append(Evidence(
                "External score outside expected range", 3,
                f"{col} is {_num(value, 3)} rather than a value from 0 to 1",
                f"reconcile {col} with the score provider or preprocessing record",
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
            "High repayment burden", severity,
            f"annuity is {_pct(ati)} of reported income",
            "verify sustainable income and run an affordability stress scenario before changing exposure",
            "Senior Underwriter",
        ))
    if _present(cti) and cti >= 6:
        severity = 3 if cti >= 8 else 2
        signals.append(Evidence(
            "High credit-to-income leverage", severity,
            f"requested credit is {_num(cti, 1)}x reported income",
            "reconcile all current obligations and test repayment capacity under lower income",
            "Senior Underwriter",
        ))
    if _present(inst_max) and inst_max > 30:
        severity = 3 if inst_max >= 90 else 2
        signals.append(Evidence(
            "Material installment delinquency", severity,
            f"maximum observed installment delay is {_num(inst_max, 0)} days",
            "review the payment timeline and, for an existing customer in hardship, assess contact or restructuring under policy",
            "Credit Review / Customer Assistance",
        ))
    if _present(severe_late) and severe_late >= 0.05:
        signals.append(Evidence(
            "Repeated severe installment lateness", 3,
            f"{_pct(severe_late)} of observed installments were more than 30 days late",
            "review recurrence, recency, and any cure before taking a credit action",
            "Credit Review / Customer Assistance",
        ))
    elif _present(late) and late >= 0.20:
        signals.append(Evidence(
            "Frequent installment lateness", 2,
            f"{_pct(late)} of observed installments were late",
            "review lateness recency and causes and confirm the proposed payment schedule is affordable",
            "Credit Review",
        ))
    if _present(pay_ratio) and 0 <= pay_ratio < 0.90:
        signals.append(Evidence(
            "Persistent underpayment", 2,
            f"mean paid amount is {_pct(pay_ratio)} of the amount due",
            "reconcile partial payments and unresolved balances before increasing exposure",
            "Credit Review",
        ))
    if (_present(util_mean) and util_mean >= 0.80) or (_present(util_max) and util_max >= 1.0):
        evidence = (
            f"mean card utilisation is {_pct(util_mean)} and maximum is {_pct(util_max)}"
        )
        signals.append(Evidence(
            "High revolving-credit utilisation", 2, evidence,
            "review current card balances, payment capacity, and limit suitability; do not infer distress from utilisation alone",
            "Revolving Credit Review",
        ))
    max_dpd = np.nanmax([cc_dpd, pos_dpd]) if any(_present(v) for v in [cc_dpd, pos_dpd]) else np.nan
    if _present(max_dpd) and max_dpd > 0:
        signals.append(Evidence(
            "Current product delinquency signal", 2,
            f"mean days-past-due signal reaches {_num(max_dpd, 1)} days across card/POS history",
            "inspect recency and product-level arrears before changing exposure",
            "Credit Review",
        ))
    if _present(bureau_debt) and bureau_debt >= 0.80:
        signals.append(Evidence(
            "High external debt utilisation", 2,
            f"bureau debt is {_pct(bureau_debt)} of recorded bureau credit",
            "reconcile outstanding external obligations and include them in the affordability calculation",
            "Senior Underwriter",
        ))
    if (_present(bureau_severe) and bureau_severe >= 0.02) or (_present(bureau_dpd) and bureau_dpd >= 0.10):
        signals.append(Evidence(
            "External delinquency history", 3,
            f"bureau months show {_pct(bureau_dpd)} any-DPD and {_pct(bureau_severe)} severe-DPD",
            "verify bureau recency, dispute status, and cure information before relying on the signal",
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
            "Weak combined external score", 2,
            f"mean available external score is {_num(float(np.mean(ext_values)), 3)}",
            "review the underlying bureau information and use specific verified reasons rather than the score alone",
            "Senior Underwriter",
        ))
    if _present(prev_refused) and prev_refused >= 3 and _present(approval) and approval < 0.50:
        signals.append(Evidence(
            "Repeated prior refusals", 1,
            f"{_num(prev_refused, 0)} prior applications were refused and historical approval rate is {_pct(approval)}",
            "reconcile the earlier refusal reasons and confirm whether they remain current",
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
        evidence.append(Evidence(
            f"Unusual {col}", 1,
            f"{col} is {_num(value)} versus segment median {_num(median)} ({score:.1f} robust deviations)",
            f"confirm {col} from the normal source document and otherwise keep the case in the standard underwriting path",
            "Standard Underwriting",
        ))
    return evidence


def build_anomaly_investigation(
    business: pd.DataFrame,
    combined: pd.DataFrame,
    labels: pd.DataFrame,
    cluster_names: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Build one evidence-backed review recommendation per high-confidence row."""
    names = dict(zip(cluster_names["cluster_id"].astype(int), cluster_names["nama"]))
    label_cols = ["ROW_ID", "CLUSTER_KMEANS", "IS_OUTLIER"]
    label_view = labels[label_cols].drop_duplicates("ROW_ID")
    focus_ids = combined.loc[
        combined["anomaly_category"].eq("HIGH_CONFIDENCE_ANOMALY"), "ROW_ID"
    ]

    merged = business[business["ROW_ID"].isin(focus_ids)].merge(
        combined, on="ROW_ID", how="inner", suffixes=("", "_det")
    )
    if "CLUSTER_KMEANS" not in merged.columns:
        merged = merged.merge(label_view, on="ROW_ID", how="left")
    if "IS_OUTLIER" not in merged.columns:
        merged = merged.merge(label_view[["ROW_ID", "IS_OUTLIER"]], on="ROW_ID", how="left")

    reference_cols = [
        "AMT_INCOME_TOTAL", "AMT_CREDIT", "AMT_ANNUITY",
        "CREDIT_TO_INCOME", "ANNUITY_TO_INCOME", "CREDIT_TERM_MONTHS",
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
        data_issues = _logical_data_checks(row)
        risk_signals = _repayment_risk_evidence(row)
        rare_signals = _rare_profile_evidence(row, medians, scales)

        if data_issues:
            review_type = "Data consistency check"
            evidence = sorted(data_issues, key=lambda x: x.severity, reverse=True)
            interpretation = (
                "The record contains a logical or unit inconsistency. This is a data-governance issue, "
                "not evidence that the applicant will default."
            )
        elif risk_signals:
            review_type = "Affordability / repayment review"
            evidence = sorted(risk_signals, key=lambda x: x.severity, reverse=True)
            interpretation = (
                "The unusual pattern is supported by repayment-capacity or delinquency evidence. "
                "It warrants a specific manual review, not an automatic adverse action."
            )
        else:
            review_type = "Rare but plausible profile"
            evidence = rare_signals or [Evidence(
                "Multivariate rarity", 1,
                "the combination is unusual although no single policy-relevant risk threshold is breached",
                "confirm the unusual fields and otherwise continue through the standard underwriting path",
                "Standard Underwriting",
            )]
            interpretation = (
                "The applicant is statistically unusual but has no identified affordability, delinquency, "
                "or logical-data breach. Rarity alone is not a credit-risk conclusion."
            )

        top = evidence[:3]
        primary = top[0]
        methods = _methods_fired(row)
        robust_peak = 0.0
        for item in rare_signals:
            try:
                robust_peak = max(robust_peak, float(item.evidence.split("(")[-1].split()[0]))
            except (ValueError, IndexError):
                pass
        if int(row.get("IS_OUTLIER", 0) or 0) == 1:
            scope = "Collective / density"
        elif robust_peak >= 8:
            scope = "Global / extreme value"
        else:
            scope = "Contextual / unusual combination"

        max_severity = max(e.severity for e in evidence)
        priority = (
            "Urgent data reconciliation" if review_type == "Data consistency check" and max_severity >= 3
            else "High-priority human review" if max_severity >= 3
            else "Targeted human review" if max_severity == 2
            else "Standard review"
        )
        actual_evidence = "; ".join(e.evidence for e in top)
        actions = []
        for e in top:
            if e.action not in actions:
                actions.append(e.action)
        recommendation = (
            f"For applicant {int(row['SK_ID_CURR'])}: because {actual_evidence}, "
            f"{'; then '.join(actions)}. Record the verified, specific reason; do not use cluster membership alone."
        )
        owner_parts = [
            owner.strip()
            for evidence in top
            for owner in evidence.owner.split(" / ")
            if owner.strip()
        ]
        owners = " / ".join(dict.fromkeys(owner_parts))

        output = {
            "ROW_ID": int(row["ROW_ID"]),
            "SK_ID_CURR": int(row["SK_ID_CURR"]),
            "Cluster": f"cluster_{cid}",
            "Segment": segment,
            "Detected By": ", ".join(methods),
            "Detector Count": len(methods),
            "Anomaly Scope": scope,
            "Review Type": review_type,
            "Priority": priority,
            "Primary Driver": primary.driver,
            "Record Evidence": actual_evidence,
            "Business Interpretation": interpretation,
            "Recommended Action": recommendation,
            "Review Owner": owners,
            "Automatic Decision Allowed": "No",
            "Evidence Value Basis": "Preserved source values where available; observed history aggregates otherwise",
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


def cluster_risk_backtest(
    labels: pd.DataFrame,
    cluster_names: pd.DataFrame,
    target: pd.DataFrame,
    n_splits: int = 5,
    threshold_uplift: float = 1.10,
    smoothing: float = 200.0,
) -> dict[str, pd.DataFrame]:
    """Train-only out-of-fold backtest of a cluster-level risk flag.

    Each validation row receives a smoothed default rate estimated only from
    the other folds. Test applications never enter the metric denominator.
    """
    data = target[["SK_ID_CURR", "TARGET"]].merge(
        labels[["SK_ID_CURR", "CLUSTER_KMEANS"]], on="SK_ID_CURR", how="inner",
        validate="one_to_one",
    )
    if len(data) != len(target):
        raise ValueError(
            f"Train ID alignment failed: expected {len(target):,}, matched {len(data):,}."
        )
    data = data.reset_index(drop=True)
    data["OOF_CLUSTER_DEFAULT_RATE"] = np.nan
    data["FOLD_BASELINE"] = np.nan
    data["FOLD_THRESHOLD"] = np.nan
    data["FOLD"] = -1

    splitter = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
    for fold, (fit_idx, valid_idx) in enumerate(splitter.split(data, data["TARGET"])):
        fit = data.iloc[fit_idx]
        baseline = float(fit["TARGET"].mean())
        grouped = fit.groupby("CLUSTER_KMEANS")["TARGET"].agg(["sum", "count"])
        rates = (grouped["sum"] + smoothing * baseline) / (grouped["count"] + smoothing)
        data.loc[valid_idx, "OOF_CLUSTER_DEFAULT_RATE"] = data.loc[
            valid_idx, "CLUSTER_KMEANS"
        ].map(rates)
        data.loc[valid_idx, "FOLD_THRESHOLD"] = baseline * threshold_uplift
        data.loc[valid_idx, "FOLD_BASELINE"] = baseline
        data.loc[valid_idx, "FOLD"] = fold

    if data["OOF_CLUSTER_DEFAULT_RATE"].isna().any():
        raise ValueError("At least one out-of-fold cluster score is missing.")

    data["CLUSTER_RISK_FLAG"] = (
        data["OOF_CLUSTER_DEFAULT_RATE"] >= data["FOLD_THRESHOLD"]
    ).astype(int)
    y = data["TARGET"].astype(int).to_numpy()
    pred = data["CLUSTER_RISK_FLAG"].to_numpy()
    score = data["OOF_CLUSTER_DEFAULT_RATE"].to_numpy()
    tn, fp, fn, tp = confusion_matrix(y, pred, labels=[0, 1]).ravel()
    baseline = float(np.mean(y))
    precision = float(precision_score(y, pred, zero_division=0))
    recall = float(recall_score(y, pred, zero_division=0))
    specificity = float(tn / (tn + fp)) if tn + fp else 0.0
    metrics = pd.DataFrame([
        ("evaluation_rows", len(data), "Train IDs only; test rows excluded"),
        ("test_rows_scored", 0, "No unlabeled test row enters scoring"),
        ("observed_default_rate", baseline, "TARGET=1 share in matched train rows"),
        ("flagged_share", float(np.mean(pred)), "Share receiving the cluster risk flag"),
        ("precision", precision, "Default share among cluster-risk flags"),
        ("recall", recall, "Share of observed defaults captured by the flag"),
        ("specificity", specificity, "Share of observed non-defaults not flagged"),
        ("f1", float(f1_score(y, pred, zero_division=0)), "Harmonic mean of precision and recall"),
        ("lift_vs_baseline", precision / baseline if baseline else np.nan, "Precision divided by portfolio default rate"),
        ("average_precision", float(average_precision_score(y, score)), "PR-area summary for the five-level cluster score"),
        ("roc_auc", float(roc_auc_score(y, score)), "Ranking metric; secondary under class imbalance"),
        ("score_levels", int(pd.Series(score).nunique()), "Distinct cluster-rate scores available"),
        ("true_negative", tn, "Confusion-matrix count"),
        ("false_positive", fp, "Confusion-matrix count"),
        ("false_negative", fn, "Confusion-matrix count"),
        ("true_positive", tp, "Confusion-matrix count"),
        ("threshold_uplift", threshold_uplift, "Flag if fold-trained cluster rate is at least this multiple of fold baseline"),
    ], columns=["metric", "value", "business_definition"])

    name_map = dict(zip(cluster_names["cluster_id"].astype(int), cluster_names["nama"]))
    rates = data.groupby("CLUSTER_KMEANS")["TARGET"].agg(
        train_applicants="size", defaults="sum", default_rate="mean"
    ).reset_index()
    rates["Segment"] = rates["CLUSTER_KMEANS"].map(name_map)
    rates["portfolio_default_rate"] = baseline
    rates["lift_vs_portfolio"] = rates["default_rate"] / baseline
    rates["descriptive_risk_flag"] = rates["default_rate"] >= baseline * threshold_uplift

    # This is the empirical precision ceiling of any rule that can only choose
    # whole clusters.  It makes the coarse-granularity limitation explicit.
    metrics = pd.concat([metrics, pd.DataFrame([{
        "metric": "cluster_precision_ceiling",
        "value": float(rates["default_rate"].max()),
        "business_definition": "Highest observed default share in any complete segment",
    }])], ignore_index=True)

    cm = pd.DataFrame(
        [[tn, fp], [fn, tp]],
        index=["Actual non-default", "Actual default"],
        columns=["Flag non-default", "Flag default"],
    ).rename_axis("actual").reset_index()

    p, r, thresholds = precision_recall_curve(y, score)
    pr = pd.DataFrame({"precision": p, "recall": r})
    pr["threshold"] = np.r_[thresholds, np.nan]

    sweep_rows = []
    for uplift in np.arange(1.00, 1.51, 0.05):
        sweep_pred = score >= data["FOLD_BASELINE"].to_numpy() * uplift
        sweep_precision = precision_score(y, sweep_pred, zero_division=0)
        sweep_rows.append({
            "threshold_uplift": round(float(uplift), 2),
            "flagged_share": float(np.mean(sweep_pred)),
            "precision": float(sweep_precision),
            "recall": float(recall_score(y, sweep_pred, zero_division=0)),
            "lift_vs_baseline": float(sweep_precision / baseline) if baseline else np.nan,
        })
    sweep = pd.DataFrame(sweep_rows)

    data["Segment"] = data["CLUSTER_KMEANS"].map(name_map)
    data["EVALUATION_SCOPE"] = "TRAIN_ONLY_CROSSFIT_OUTCOME_ALIGNMENT"
    return {
        "predictions": data,
        "metrics": metrics,
        "cluster_rates": rates,
        "confusion_matrix": cm,
        "pr_curve": pr,
        "policy_sweep": sweep,
    }


def supervised_reference_benchmark(
    features: pd.DataFrame,
    target: pd.DataFrame,
    flagged_share: float,
    n_splits: int = 5,
) -> dict[str, pd.DataFrame]:
    """Interpretable train-only supervised reference for objective diagnosis.

    This is intentionally separate from the five KDD phases.  It answers
    whether applicant-level TARGET signal exists when a method is actually
    optimized for TARGET.  It is not a deployment model: preprocessing remains
    the project's transductive discovery preprocessing and there is no temporal
    or market holdout, calibration approval, fairness validation, or policy
    threshold.
    """
    data = target[["SK_ID_CURR", "TARGET"]].merge(
        features, on="SK_ID_CURR", how="inner", validate="one_to_one"
    )
    if len(data) != len(target):
        raise ValueError(
            f"Supervised reference ID alignment failed: expected {len(target):,}, matched {len(data):,}."
        )

    # Remove life-stage and socioeconomic proxy axes from this diagnostic.  The
    # resulting benchmark is still not fairness-cleared, but avoids presenting
    # those fields as a route to higher model performance.
    excluded = {
        "YEARS_BIRTH", "NAME_EDUCATION_TYPE", "NAME_INCOME_TYPE_FREQ",
        "ORGANIZATION_TYPE_FREQ", "REGION_RATING_CLIENT_W_CITY",
    }
    feature_cols = [
        c for c in features.columns
        if c != "SK_ID_CURR" and c not in excluded
    ]
    X = data[feature_cols].to_numpy(dtype=np.float64)
    y = data["TARGET"].astype(int).to_numpy()
    oof = np.full(len(data), np.nan, dtype=float)
    coef_rows = []

    splitter = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
    for fold, (fit_idx, valid_idx) in enumerate(splitter.split(X, y)):
        model = LogisticRegression(
            solver="lbfgs", max_iter=500, C=1.0, class_weight=None,
            random_state=42,
        )
        model.fit(X[fit_idx], y[fit_idx])
        oof[valid_idx] = model.predict_proba(X[valid_idx])[:, 1]
        coef_rows.extend({
            "fold": fold, "feature": col, "coefficient": float(value)
        } for col, value in zip(feature_cols, model.coef_[0]))

    if np.isnan(oof).any():
        raise ValueError("At least one supervised out-of-fold score is missing.")
    flagged_share = float(np.clip(flagged_share, 1 / len(oof), 1.0))
    threshold = float(np.quantile(oof, 1 - flagged_share))
    pred = (oof >= threshold).astype(int)
    tn, fp, fn, tp = confusion_matrix(y, pred, labels=[0, 1]).ravel()
    baseline = float(y.mean())
    precision = float(precision_score(y, pred, zero_division=0))
    recall = float(recall_score(y, pred, zero_division=0))

    metrics = pd.DataFrame([
        ("evaluation_rows", len(data), "Train IDs only; test rows excluded"),
        ("test_rows_scored", 0, "No unlabeled test row enters scoring"),
        ("observed_default_rate", baseline, "TARGET=1 share"),
        ("flagged_share", float(pred.mean()), "Matched to the cluster review capacity"),
        ("precision", precision, "Default share among reference-model flags"),
        ("recall", recall, "Observed defaults captured at matched capacity"),
        ("specificity", float(tn / (tn + fp)), "Observed non-defaults not flagged"),
        ("f1", float(f1_score(y, pred, zero_division=0)), "Precision/recall harmonic mean"),
        ("lift_vs_baseline", precision / baseline, "Precision divided by base rate"),
        ("average_precision", float(average_precision_score(y, oof)), "Area under precision-recall curve"),
        ("roc_auc", float(roc_auc_score(y, oof)), "Out-of-fold ranking discrimination"),
        ("brier_score", float(brier_score_loss(y, oof)), "Mean squared probability error; lower is better"),
        ("score_threshold", threshold, "OOF score cut at matched review capacity"),
        ("true_negative", tn, "Confusion-matrix count"),
        ("false_positive", fp, "Confusion-matrix count"),
        ("false_negative", fn, "Confusion-matrix count"),
        ("true_positive", tp, "Confusion-matrix count"),
    ], columns=["metric", "value", "business_definition"])

    predictions = data[["SK_ID_CURR", "TARGET"]].copy()
    predictions["OOF_PD_REFERENCE_SCORE"] = oof
    predictions["REFERENCE_FLAG"] = pred
    predictions["EVALUATION_SCOPE"] = "TRAIN_ONLY_OOF_DIAGNOSTIC_REFERENCE"

    coefficients = pd.DataFrame(coef_rows)
    coefficient_summary = coefficients.groupby("feature", as_index=False).agg(
        mean_coefficient=("coefficient", "mean"),
        coefficient_sd=("coefficient", "std"),
    )
    coefficient_summary["abs_mean_coefficient"] = coefficient_summary["mean_coefficient"].abs()
    coefficient_summary = coefficient_summary.sort_values("abs_mean_coefficient", ascending=False)
    return {
        "metrics": metrics,
        "predictions": predictions,
        "coefficients": coefficient_summary,
    }

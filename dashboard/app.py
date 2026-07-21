"""Responsive, artifact-driven dashboard for Home Credit portfolio discovery."""

from __future__ import annotations

import math
import os
import textwrap
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, Input, Output, State, dash_table, dcc, html
from dash.dash_table.Format import Format, Scheme


ROOT = Path(__file__).resolve().parents[1]
P1 = ROOT / "results/phase1_preprocessing"
P2 = ROOT / "results/phase2_clustering"
P3 = ROOT / "results/phase3_association"
P4 = ROOT / "results/phase4_anomaly"


def read_csv(path: Path, **kwargs) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Could not find {path}. Run the notebooks in order to rebuild this dashboard file.")
    return pd.read_csv(path, **kwargs)


def read_optional(path: Path, columns: list[str] | None = None) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame(columns=columns or [])
    return pd.read_csv(path)


quality = read_csv(P1 / "data_quality_summary.csv")
feature_importance = read_csv(P1 / "feature_importance.csv")
portfolio = read_csv(P1 / "portfolio_context.csv")
cluster_names = read_csv(P2 / "cluster_names.csv").sort_values("cluster_id")
cluster_business = read_csv(P2 / "cluster_business_summary.csv")
cluster_feature_summary = read_csv(P2 / "cluster_summary.csv")
cluster_comparison = read_csv(P2 / "cluster_comparison_long.csv")
cluster_viz = read_csv(P2 / "cluster_viz_sample.csv")
dbscan_viz = read_csv(P2 / "dbscan_umap_sample.csv")
k_selection = read_csv(P2 / "k_selection.csv")
pca_sensitivity = read_optional(P2 / "pca_cluster_sensitivity.csv")
method_agreement = read_optional(P2 / "method_agreement.csv")
rule_view = read_csv(P3 / "rule_visual_summary.csv")
rule_segment = read_csv(P3 / "rule_segment_summary.csv")
algo_comparison = read_csv(P3 / "algo_comparison.csv")
anomaly_summary = read_csv(P4 / "anomaly_summary.csv").iloc[0]
anomaly_investigation = read_csv(P4 / "anomaly_investigation.csv")
anomaly_drivers = read_csv(P4 / "anomaly_driver_summary.csv")
anomaly_by_segment = read_csv(P4 / "anomaly_review_by_segment.csv", index_col=0)
detector_overlap = read_csv(P4 / "detector_jaccard_overlap.csv", index_col=0)
anomaly_pca = read_csv(P4 / "pca_anomaly_sample.csv")
backtest_metrics = read_csv(P4 / "cluster_default_backtest_metrics.csv")
cluster_rates = read_csv(P4 / "cluster_default_rates.csv")
backtest_cm = read_csv(P4 / "cluster_default_confusion_matrix.csv")
policy_sweep = read_csv(P4 / "cluster_default_policy_sweep.csv")
reference_metrics = read_optional(P4 / "supervised_reference_metrics.csv")
outcome_comparison = read_optional(P4 / "outcome_method_comparison.csv")

# Transitional fallbacks keep the app importable while a user is rerunning the
# phase notebooks; the verified run replaces these with denominator-labelled
# fields from the corrected Phase 3 artefact.
if "support_count" not in rule_view:
    rule_view["support_count"] = (rule_view["support"] * 356_255).round().astype(int)
if "metric_scope" not in rule_view:
    rule_view["metric_scope"] = "Run Phase 3 again to show which applications were used"
if "Context" not in rule_view:
    rule_view["Context"] = rule_view["Segment"]


CLUSTER_COPY = {
    "Intensive Card User": {
        "profil_risiko": "Card balance review",
        "profile_summary": "This group has the heaviest card use and the most recorded card history.",
        "watch_items": "Check current utilisation, balances, arrears, and whether the limit still fits the customer.",
        "recommended_action": "Check card balances and payment capacity before changing a limit. If policy allows, consider whether consolidation would help.",
    },
    "Repayment-Stress History": {
        "profil_risiko": "Repayment review",
        "profile_summary": "Late repayments are what most clearly set this group apart.",
        "watch_items": "Check when the delays happened, how serious they were, whether they were cured, and what the customer can afford now.",
        "recommended_action": "Review the repayment history and current affordability. If the customer is already in hardship, follow the contact or restructuring policy.",
    },
    "Thin-File / Low-Intensity": {
        "profil_risiko": "Standard thin-file review",
        "profile_summary": "This group uses fewer credit products and has less recorded credit history.",
        "watch_items": "Check whether the record is genuinely clean or simply too thin to judge.",
        "recommended_action": "Use the standard underwriting process. If the file is thin, ask for permitted supporting evidence instead of treating missing history as risk.",
    },
    "High-Exposure Applicant": {
        "profil_risiko": "Affordability review",
        "profile_summary": "This group asks for larger loans and carries the highest payment burden.",
        "watch_items": "Confirm income, total obligations, and whether the payments still work if income falls.",
        "recommended_action": "Confirm sustainable income and stress-test the proposed payment before increasing exposure.",
    },
    "History-Rich Credit User": {
        "profil_risiko": "Credit-history review",
        "profile_summary": "This group has the longest and most active internal and external credit history.",
        "watch_items": "Check whether older refusals or arrears still matter today.",
        "recommended_action": "Compare earlier decisions with current obligations. Use the extra history to verify today's position, not to assume it.",
    },
}

QUALITY_COPY = {
    "Extreme income above p99": (
        "Income above the 99th percentile",
        "These values are rare and can pull distance-based clusters. They are not necessarily errors.",
        "Cap only the clustering value at the 99th percentile and keep the original value in the audit trail.",
    ),
    "Employment sentinel": (
        "Employment-status placeholder",
        "This value usually marks a pensioner or someone who is not employed. It does not mean 1,000 years of work.",
        "Treat the duration as missing and keep a separate flag for the placeholder.",
    ),
    "Housing detail unavailable": (
        "No housing details recorded",
        "The property record is unavailable. That does not show poor credit quality.",
        "Use zero for the structural fields and keep a separate no-housing-data flag.",
    ),
    "EXT_SOURCE_1 unavailable": (
        "External score 1 is missing",
        "The score is unavailable or the credit file is thin. Missing information is not adverse behaviour.",
        "Use the median for modelling and keep a separate missing-score flag.",
    ),
    "No car-age value": (
        "No car age recorded",
        "This usually means that the applicant does not own a car.",
        "Set car age to zero and keep a separate no-car flag.",
    ),
}

RULE_TERM_LABELS = {
    "card_utilisation_high": "high card utilisation",
    "card_utilisation_moderate": "moderate card utilisation",
    "cluster_0_card_intensive": "card-intensive cluster",
    "cluster_4_history_rich": "history-rich cluster",
    "credit_small": "smaller requested loan",
    "credit_large": "larger requested loan",
    "repayment_some_late": "some late repayments",
    "repayment_serious_late": "serious late repayments",
    "repayment_not_observed": "no recorded instalment history",
    "leverage_under_3x": "credit below 3x income",
    "burden_under_20pct": "annuity below 20% of income",
    "previous_refusals_repeated": "repeated previous refusals",
    "previous_deep": "extensive previous-application history",
    "previous_none": "no previous applications recorded",
    "previous_outcome_not_observed": "no previous-application outcome recorded",
    "card_history_not_observed": "no recorded card history",
}

ANOMALY_DRIVER_LABELS = {
    "Current product delinquency signal": "Card or POS arrears",
    "Material installment delinquency": "Long instalment delay",
    "Persistent underpayment": "Repeated underpayment",
    "Repeated severe installment lateness": "Repeated severe instalment delays",
    "High revolving-credit utilisation": "High card utilisation",
    "High credit-to-income leverage": "High credit compared with income",
    "Frequent installment lateness": "Frequent instalment delays",
    "Weak combined external score": "Low combined external score",
    "High repayment burden": "High payment burden",
    "Installment ratio needs reconciliation": "Payment ratio needs checking",
    "Unusual BUREAU_COUNT": "Unusual bureau-history depth",
    "Unusual INST_COUNT": "Unusual instalment-history depth",
    "Unusual AMT_ANNUITY": "Unusual annuity amount",
    "Unusual ANNUITY_TO_INCOME": "Unusual annuity-to-income ratio",
    "Unusual INST_PAYMENT_RATIO_MEAN": "Unusual payment-to-due ratio",
    "Unusual AMT_CREDIT": "Unusual requested credit",
    "Unusual BUREAU_DEBT_TO_CREDIT_RATIO": "Unusual bureau debt-to-credit ratio",
    "Unusual CC_UTILIZATION_MAX": "Unusual maximum card utilisation",
    "Unusual CREDIT_TERM_MONTHS": "Unusual estimated credit term",
    "Unusual CREDIT_TO_INCOME": "Unusual credit-to-income ratio",
}

ANOMALY_INTERPRETATION_COPY = {
    "The unusual pattern is supported by repayment-capacity or delinquency evidence. It warrants a specific manual review, not an automatic adverse action.": (
        "Repayment or affordability evidence supports this flag. A reviewer should check it before anyone takes action."
    ),
    "The record contains a logical or unit inconsistency. This is a data-governance issue, not evidence that the applicant will default.": (
        "The values do not agree or may use different units. Confirm or fix the data before using it. This is not evidence of default."
    ),
    "The applicant is statistically unusual but has no identified affordability, delinquency, or logical-data breach. Rarity alone is not a credit-risk conclusion.": (
        "This application is unusual, but we found no clear affordability, repayment, or data-quality problem. Unusual does not mean risky."
    ),
}

REVIEW_TYPE_LABELS = {
    "Affordability / repayment review": "Affordability and repayment review",
    "Data consistency check": "Data quality check",
    "Rare but plausible profile": "Unusual but plausible",
}

PRIORITY_LABELS = {
    "Urgent data reconciliation": "Urgent data check",
    "High-priority human review": "High priority review",
    "Targeted human review": "Focused review",
}

ACTION_COPY = {
    "verify sustainable income and run an affordability stress scenario before changing exposure": "Confirm sustainable income and check whether the payments still work if income falls.",
    "reconcile all current obligations and test repayment capacity under lower income": "Confirm all current obligations and check whether the applicant could still pay if income falls.",
    "review the payment timeline and, for an existing customer in hardship, assess contact or restructuring under policy": "Review the payment timeline. If the customer is already in hardship, follow the contact or restructuring policy.",
    "review recurrence, recency, and any cure before taking a credit action": "Check how often the delays happened, how recent they were, and whether the account was brought up to date.",
    "review lateness recency and causes and confirm the proposed payment schedule is affordable": "Check when and why the late payments happened, then confirm that the proposed schedule is affordable.",
    "reconcile partial payments and unresolved balances before increasing exposure": "Check partial payments and unresolved balances before increasing exposure.",
    "review current card balances, payment capacity, and limit suitability; do not infer distress from utilisation alone": "Check card balances, payment capacity, and whether the limit still fits. High utilisation alone does not prove financial distress.",
    "inspect recency and product-level arrears before changing exposure": "Check how recent the card or POS arrears are before changing exposure.",
    "reconcile outstanding external obligations and include them in the affordability calculation": "Confirm outstanding external debts and include them in the affordability calculation.",
    "verify bureau recency, dispute status, and cure information before relying on the signal": "Check how recent the bureau arrears are, whether they are disputed, and whether they were cured.",
    "review the underlying bureau information and use specific verified reasons rather than the score alone": "Check the underlying bureau information. Do not rely on the combined score by itself.",
    "reconcile the earlier refusal reasons and confirm whether they remain current": "Check why earlier applications were refused and whether those reasons still apply.",
    "check reversals, prepayments, duplicated installments, and currency units": "Check for reversals, early payments, duplicate instalments, and inconsistent currency units.",
    "confirm the unusual fields and otherwise continue through the standard underwriting path": "Confirm the unusual values. If they are correct, continue with standard underwriting.",
}

FEATURE_TEXT_LABELS = {
    "BUREAU_DEBT_TO_CREDIT_RATIO": "bureau debt-to-credit ratio",
    "INST_PAYMENT_RATIO_MEAN": "average payment-to-due ratio",
    "CC_UTILIZATION_MEAN": "average card utilisation",
    "CC_UTILIZATION_MAX": "maximum card utilisation",
    "CREDIT_TERM_MONTHS": "estimated credit term",
    "ANNUITY_TO_INCOME": "annuity-to-income ratio",
    "CREDIT_TO_INCOME": "credit-to-income ratio",
    "AMT_INCOME_TOTAL": "reported income",
    "CC_AMT_BALANCE_MEAN": "average card balance",
    "AMT_ANNUITY": "annuity amount",
    "AMT_CREDIT": "requested credit",
    "BUREAU_COUNT": "bureau-history depth",
    "INST_COUNT": "instalment-history depth",
    "PREV_COUNT": "previous-application history",
    "EXT_SOURCE_1": "external score 1",
    "EXT_SOURCE_2": "external score 2",
    "EXT_SOURCE_3": "external score 3",
}


def as_sentence(value: str) -> str:
    text = str(value).strip()
    if not text:
        return ""
    text = text[0].upper() + text[1:]
    return text if text.endswith((".", "!", "?")) else f"{text}."


def humanize_rule(value: str) -> str:
    def readable_side(side: str) -> str:
        terms = [RULE_TERM_LABELS.get(part.strip(), part.strip().replace("_", " ")) for part in side.split(",")]
        return " + ".join(terms)

    raw = str(value)
    if "→" not in raw:
        return raw.replace("_", " ")
    left, right = raw.split("→", 1)
    readable = f"{readable_side(left)} → {readable_side(right)}"
    return readable[0].upper() + readable[1:]


def humanize_fragment(value: str) -> str:
    text = str(value).strip().rstrip(".")
    if text.startswith("bureau months show ") and " any-DPD and " in text and text.endswith(" severe-DPD"):
        any_share, severe_share = text[len("bureau months show "):].split(" any-DPD and ", 1)
        severe_share = severe_share[:-len(" severe-DPD")]
        return as_sentence(
            f"In bureau history, {any_share} of months had a late payment and {severe_share} had a severe late payment"
        )
    for technical, label in sorted(FEATURE_TEXT_LABELS.items(), key=lambda item: len(item[0]), reverse=True):
        text = text.replace(technical, label)
    replacements = {
        "annuity is": "scheduled annuity equals",
        "requested credit is": "requested credit equals",
        "x reported income": " times reported income",
        "maximum observed installment delay is": "the longest observed instalment delay is",
        "mean paid amount is": "the average payment is",
        "mean card utilisation is": "average card utilisation is",
        " and maximum is": " and the maximum is",
        "mean days-past-due signal reaches": "average days past due reaches",
        "across card/POS history": "across card or POS history",
        "bureau months show": "bureau history shows",
        "any-DPD": "any late payment",
        "severe-DPD": "a severe late payment",
        "mean available external score is": "the average available external score is",
        "versus segment median": "compared with the cluster median",
        "mean paid-to-due ratio": "average payment-to-due ratio",
        "robust deviations": "robust scale units",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return as_sentence(text)


def humanize_evidence(value: str) -> str:
    return " ".join(humanize_fragment(part) for part in str(value).split(";") if part.strip())


def humanize_owner(value: str) -> str:
    owners = list(dict.fromkeys(part.strip() for part in str(value).split(" / ") if part.strip()))
    if len(owners) < 2:
        return owners[0] if owners else ""
    if len(owners) == 2:
        return " and ".join(owners)
    return f"{', '.join(owners[:-1])}, and {owners[-1]}"


def humanize_recommendation(row: pd.Series) -> str:
    action = str(row["Recommended Action"]).strip()
    evidence = str(row["Record Evidence"]).strip()
    legacy_prefix = f"For applicant {int(row['SK_ID_CURR'])}: because {evidence}, "
    if action.startswith(legacy_prefix):
        action = action[len(legacy_prefix):]
    current_prefix = f"Applicant {int(row['SK_ID_CURR'])}: "
    if action.startswith(current_prefix):
        action = action[len(current_prefix):]

    for ending in [
        ". Record the verified, specific reason; do not use cluster membership alone.",
        " Document the facts confirmed during review. Base any credit action on those facts, not the anomaly or cluster label.",
        " Document what you checked in the case file. The cluster label alone is not a reason for a decision.",
    ]:
        if action.endswith(ending):
            action = action[:-len(ending)]

    parts = []
    for part in action.replace("; then ", "\n").split("\n"):
        clean = part.strip().rstrip(".")
        if not clean:
            continue
        if clean in ACTION_COPY:
            parts.append(ACTION_COPY[clean])
        elif clean.startswith("confirm ") and " from the normal source document" in clean:
            field = clean[len("confirm "):clean.index(" from the normal source document")]
            field = FEATURE_TEXT_LABELS.get(field, field.replace("_", " ").lower())
            parts.append(f"Check {field} against the source document. If it is correct, continue with standard underwriting.")
        elif clean.startswith("reconcile the ") and " with the source application" in clean:
            field = clean[len("reconcile the "):clean.index(" with the source application")]
            parts.append(f"Check the {field} against the original application before using it.")
        elif clean.startswith("reconcile external score "):
            parts.append(as_sentence(clean.replace("reconcile", "check", 1)))
        else:
            parts.append(humanize_fragment(clean))

    driver = ANOMALY_DRIVER_LABELS.get(row["Primary Driver"], row["Primary Driver"])
    introduction = f"For applicant {int(row['SK_ID_CURR']):,}, start with the {str(driver).lower()} shown in the evidence."
    guardrail = "Document what you checked in the case file. The cluster label alone is not a reason for a decision."
    return " ".join([introduction, *parts, guardrail])


for segment, copy in CLUSTER_COPY.items():
    mask = cluster_names["nama"].eq(segment)
    for column, value in copy.items():
        cluster_names.loc[mask, column] = value

for old_issue, (issue, meaning, treatment) in QUALITY_COPY.items():
    mask = quality["issue"].eq(old_issue)
    quality.loc[mask, ["issue", "business_meaning", "treatment"]] = [issue, meaning, treatment]

rule_view["short_rule"] = rule_view["short_rule"].map(humanize_rule)
rule_view["metric_scope"] = rule_view["metric_scope"].replace({
    "Full portfolio; Apriori/FP-Growth/ECLAT exact agreement": "Full portfolio. Apriori, FP-Growth, and ECLAT found the same rule.",
    "Within-segment FP-Growth; metrics use the segment denominator": "This cluster only. Support and confidence use this cluster as the denominator.",
})

raw_anomaly_evidence = anomaly_investigation["Record Evidence"].copy()
anomaly_investigation["Recommended Action"] = anomaly_investigation.apply(humanize_recommendation, axis=1)
anomaly_investigation["Record Evidence"] = raw_anomaly_evidence.map(humanize_evidence)
anomaly_investigation["Business Interpretation"] = anomaly_investigation["Business Interpretation"].replace(ANOMALY_INTERPRETATION_COPY)
anomaly_investigation["Primary Driver"] = anomaly_investigation["Primary Driver"].replace(ANOMALY_DRIVER_LABELS)
anomaly_investigation["Review Type"] = anomaly_investigation["Review Type"].replace(REVIEW_TYPE_LABELS)
anomaly_investigation["Priority"] = anomaly_investigation["Priority"].replace(PRIORITY_LABELS)
anomaly_investigation["Review Owner"] = anomaly_investigation["Review Owner"].map(humanize_owner)
anomaly_drivers["Driver"] = anomaly_drivers["Driver"].replace(ANOMALY_DRIVER_LABELS)
anomaly_drivers["Review Type"] = anomaly_drivers["Review Type"].replace(REVIEW_TYPE_LABELS)
anomaly_by_segment = anomaly_by_segment.rename(columns=REVIEW_TYPE_LABELS)


NAME_BY_ID = dict(zip(cluster_names["cluster_id"].astype(int), cluster_names["nama"]))
SEGMENT_ORDER = cluster_names["nama"].tolist()
SEGMENT_COLORS = {
    "Intensive Card User": "#64748B",
    "History-Rich Credit User": "#356A8A",
    "Thin-File / Low-Intensity": "#4F7D65",
    "Repayment-Stress History": "#B5534C",
    "High-Exposure Applicant": "#B98535",
}
REVIEW_COLORS = {
    "Affordability and repayment review": "#B5534C",
    "Data quality check": "#B98535",
    "Unusual but plausible": "#356A8A",
}
SEVERITY_COLORS = {
    "Typical record": "#CBD5E1",
    "One detector flag": "#D5AE5D",
    "Multiple detector flags": "#C97543",
    "Flagged by 3+ methods": "#A93F3A",
}
FEATURE_LABELS = {
    "EXT_SOURCE_1": "External score 1",
    "EXT_SOURCE_2": "External score 2",
    "EXT_SOURCE_3": "External score 3",
    "AMT_INCOME_TOTAL": "Income",
    "AMT_CREDIT": "Requested credit",
    "AMT_ANNUITY": "Annuity",
    "CREDIT_TO_INCOME": "Credit / income",
    "ANNUITY_TO_INCOME": "Annuity / income",
    "INST_DPD_MAX": "Longest instalment delay (days)",
    "INST_DPD_MEAN": "Average instalment delay (days)",
    "INST_LATE_RATIO": "Instalment late share",
    "INST_SEVERE_LATE_RATIO": "Severely late instalment share",
    "INST_PAYMENT_RATIO_MEAN": "Instalment payment ratio",
    "BUREAU_COUNT": "Bureau record count",
    "BUREAU_ACTIVE_RATIO": "Active bureau account share",
    "BUREAU_BB_DPD_RATIO_MEAN": "Bureau months with a late payment",
    "BUREAU_BB_SEVERE_DPD_MEAN": "Bureau months with a severe late payment",
    "PREV_COUNT": "Previous application count",
    "PREV_REFUSED_COUNT": "Prior refusals",
    "PREV_APPROVAL_RATE": "Prior approval rate",
    "INST_COUNT": "Instalment record count",
    "POS_MONTHS_COUNT": "POS / cash monthly records",
    "POS_SK_DPD_MEAN": "Average POS / cash delay (days)",
    "CC_UTILIZATION_MEAN": "Average card utilisation",
    "CC_UTILIZATION_MAX": "Maximum card utilisation",
    "CC_AMT_BALANCE_MEAN": "Average card balance",
    "CC_MONTHS_COUNT": "Card monthly records",
    "CC_SK_DPD_MEAN": "Average card delay (days)",
    "AMT_REQ_CREDIT_BUREAU_YEAR": "Recent bureau enquiries",
    "CREDIT_TERM_MONTHS": "Estimated credit term",
}

def metric(name: str, frame: pd.DataFrame = backtest_metrics, default: float = np.nan) -> float:
    if frame.empty or "metric" not in frame:
        return float(default)
    values = frame.loc[frame["metric"].eq(name), "value"]
    return float(values.iloc[0]) if len(values) else float(default)


def fmt_int(value: float) -> str:
    return f"{int(round(value)):,}"


def fmt_pct(value: float, digits: int = 1) -> str:
    return "—" if not np.isfinite(value) else f"{value * 100:.{digits}f}%"


def wilson_interval(successes: int, total: int, z: float = 1.959964) -> tuple[float, float]:
    if total <= 0:
        return np.nan, np.nan
    rate = successes / total
    denominator = 1 + (z ** 2 / total)
    center = (rate + z ** 2 / (2 * total)) / denominator
    margin = z * math.sqrt(rate * (1 - rate) / total + z ** 2 / (4 * total ** 2)) / denominator
    return center - margin, center + margin


def validate_cluster_identity() -> None:
    expected = (
        cluster_names[["cluster_id", "nama", "n_applicants"]]
        .rename(columns={"cluster_id": "CLUSTER_KMEANS", "nama": "Segment", "n_applicants": "applicants"})
        .sort_values("CLUSTER_KMEANS")
        .reset_index(drop=True)
    )
    business_identity = (
        cluster_business[["CLUSTER_KMEANS", "Segment", "applicants"]]
        .sort_values("CLUSTER_KMEANS")
        .reset_index(drop=True)
    )
    rate_identity = (
        cluster_rates[["CLUSTER_KMEANS", "Segment"]]
        .sort_values("CLUSTER_KMEANS")
        .reset_index(drop=True)
    )
    if not expected.equals(business_identity):
        raise ValueError("Phase 2 files disagree on cluster names, IDs, or applicant counts. Run Phase 2 again.")
    if not expected[["CLUSTER_KMEANS", "Segment"]].equals(rate_identity):
        raise ValueError("Phase 4 cluster names do not match Phase 2. Run Phases 2 through 4 again in order.")


validate_cluster_identity()


cluster_detail = (
    cluster_names.rename(columns={"cluster_id": "CLUSTER_KMEANS"})
    .merge(
        cluster_business.drop(columns=["Segment", "applicants"]),
        on="CLUSTER_KMEANS",
        how="left",
        validate="one_to_one",
    )
    .merge(
        cluster_rates[[
            "CLUSTER_KMEANS", "train_applicants", "defaults", "default_rate",
            "portfolio_default_rate", "lift_vs_portfolio",
        ]],
        on="CLUSTER_KMEANS",
        how="left",
        validate="one_to_one",
    )
)
COMBINED_APPLICATIONS = int(cluster_detail["n_applicants"].sum())
cluster_detail["portfolio_share"] = cluster_detail["n_applicants"] / COMBINED_APPLICATIONS

PROFILE_METRICS = [
    ("median_income", "Median income", "amount", "Median across applicants"),
    ("median_credit", "Median requested credit", "amount", "Median across applicants"),
    ("median_credit_to_income", "Credit / income", "multiple", "Median across applicants"),
    ("median_annuity_to_income", "Annuity / income", "pct", "Median across applicants"),
    ("median_installment_late_share", "Instalment late share", "pct", "Median across all applications. A zero can mean no recorded history"),
    ("median_external_score_2", "External score 2", "decimal", "Observed or imputed value used for clustering"),
    ("median_card_utilisation", "Card utilisation", "pct", "Median across all applications. A zero can mean no recorded history"),
    ("default_rate", "Observed default rate", "pct", "Training records with TARGET only"),
]

PROFILE_AXIS_LABELS = {
    "median_income": "Median income",
    "median_credit": "Requested credit",
    "median_credit_to_income": "Credit / income",
    "median_annuity_to_income": "Annuity / income",
    "median_installment_late_share": "Late instalments",
    "median_external_score_2": "External score 2",
    "median_card_utilisation": "Card utilisation",
    "default_rate": "Observed default rate",
}

SEGMENT_HEADER_LABELS = {
    "Intensive Card User": "Intensive Card<br>User",
    "Repayment-Stress History": "Repayment-Stress<br>History",
    "Thin-File / Low-Intensity": "Thin-File /<br>Low-Intensity",
    "High-Exposure Applicant": "High-Exposure<br>Applicant",
    "History-Rich Credit User": "History-Rich<br>Credit User",
}
SEGMENT_TICK_LABELS = {
    row["nama"]: (
        f"<b>{SEGMENT_HEADER_LABELS[row['nama']]}</b><br>"
        f"{int(row['n_applicants']):,} applicants<br>{row['portfolio_share']:.1%} of portfolio"
    )
    for _, row in cluster_detail.iterrows()
}


def format_profile_value(value: float, kind: str) -> str:
    if not np.isfinite(value):
        return "—"
    if kind == "count":
        return fmt_int(value)
    if kind == "amount":
        return f"{value:,.0f}"
    if kind == "pct":
        return fmt_pct(value, 1)
    if kind == "multiple":
        return f"{value:.2f}×"
    if kind == "decimal":
        return f"{value:.3f}"
    return f"{value:,.2f}"


def format_profile_cell(value: float, kind: str) -> str:
    if not np.isfinite(value):
        return "—"
    if kind == "amount":
        return f"{value / 1000:.0f}k"
    return format_profile_value(value, kind)


def wrap_hover(value: str, width: int = 42) -> str:
    return "<br>".join(textwrap.wrap(str(value), width=width))


def cluster_top_features(cluster_id: int, limit: int = 3) -> str:
    features = (
        cluster_feature_summary.loc[cluster_feature_summary["cluster_id"].eq(cluster_id)]
        .assign(magnitude=lambda frame: frame["rel_diff_pct"].abs())
        .sort_values("magnitude", ascending=False)
        .head(limit)
    )
    labels = []
    for item in features.itertuples():
        feature = FEATURE_LABELS.get(item.fitur, item.fitur.replace("_", " ").title())
        direction = "above" if item.rel_diff_pct >= 0 else "below"
        labels.append(f"{feature}: {abs(item.rel_diff_pct) / 100:.2f} SD {direction} the portfolio average")
    return "<br>• " + "<br>• ".join(labels)


def cluster_profile_matrix_figure() -> go.Figure:
    details = cluster_detail.set_index("nama").loc[SEGMENT_ORDER]
    score_rows, text_rows, hover_rows, y_labels = [], [], [], []

    for key, label, kind, scope in PROFILE_METRICS:
        values = details[key].astype(float)
        scale = float(values.std(ddof=0))
        scores = np.zeros(len(values)) if scale == 0 else ((values - values.mean()) / scale).to_numpy()
        ranks = values.rank(method="min", ascending=False)
        score_rows.append(scores)
        text_rows.append([format_profile_cell(float(value), kind) for value in values])
        y_labels.append(PROFILE_AXIS_LABELS[key])

        metric_hover = []
        for segment, value in values.items():
            row = details.loc[segment]
            if key == "default_rate":
                ci_low, ci_high = wilson_interval(int(row["defaults"]), int(row["train_applicants"]))
                comparison_note = (
                    f"{int(row['defaults']):,} defaults among {int(row['train_applicants']):,} training applications<br>"
                    f"95% CI {ci_low:.2%}–{ci_high:.2%}<br>{row['lift_vs_portfolio']:.2f}x the training-set average"
                )
            else:
                comparison_note = f"Number {int(ranks.loc[segment])} of 5, from highest to lowest"
            metric_hover.append([
                segment,
                format_profile_value(float(value), kind),
                scope,
                comparison_note,
                row["profil_risiko"],
                wrap_hover(row["profile_summary"]),
                cluster_top_features(int(row["CLUSTER_KMEANS"])),
                wrap_hover(row["watch_items"]),
                wrap_hover(row["recommended_action"]),
            ])
        hover_rows.append(metric_hover)

    fig = go.Figure(go.Heatmap(
        z=np.asarray(score_rows),
        x=SEGMENT_ORDER,
        y=y_labels,
        zmin=-1.8,
        zmax=1.8,
        zmid=0,
        colorscale=[[0, "#E8C4AB"], [.5, "#F7F7F2"], [1, "#AFCBD7"]],
        text=np.asarray(text_rows, dtype=object),
        texttemplate="%{text}",
        textfont=dict(size=11, color="#173647"),
        customdata=np.asarray(hover_rows, dtype=object),
        showscale=False,
        hovertemplate=(
            "<b>%{customdata[0]}</b><br>"
            "%{y}: <b>%{customdata[1]}</b><br>"
            "%{customdata[2]}<br>%{customdata[3]}<br><br>"
            "<b>Profile</b><br>%{customdata[4]}<br>%{customdata[5]}<br><br>"
            "<b>Features that stand out</b>%{customdata[6]}<br><br>"
            "<b>Check:</b> %{customdata[7]}<br>"
            "<b>Suggested review:</b> %{customdata[8]}"
            "<extra></extra>"
        ),
    ))
    chart_layout(fig, legend=False, left=96, bottom=22)
    fig.update_layout(margin=dict(l=96, r=8, t=18, b=22))
    fig.update_xaxes(
        title="",
        side="top",
        tickmode="array",
        tickvals=SEGMENT_ORDER,
        ticktext=[SEGMENT_TICK_LABELS[name] for name in SEGMENT_ORDER],
        tickangle=0,
        tickfont=dict(size=11),
        automargin=True,
        showgrid=False,
    )
    fig.update_yaxes(
        title="",
        autorange="reversed",
        tickfont=dict(size=11),
        showgrid=False,
    )
    return fig


def stratified_sample(frame: pd.DataFrame, group: str, limit: int, seed: int = 42) -> pd.DataFrame:
    if len(frame) <= limit:
        return frame.copy()
    rng = np.random.default_rng(seed)
    pieces = []
    for _, part in frame.groupby(group, dropna=False):
        take = max(1, int(round(limit * len(part) / len(frame))))
        indices = rng.choice(part.index.to_numpy(), size=min(take, len(part)), replace=False)
        pieces.append(frame.loc[indices])
    sampled = pd.concat(pieces)
    if len(sampled) > limit:
        sampled = sampled.sample(limit, random_state=seed)
    return sampled


def chart_layout(fig: go.Figure, *, legend: bool = True, left: int = 48, bottom: int = 48) -> go.Figure:
    fig.update_layout(
        template="plotly_white",
        autosize=True,
        margin=dict(l=left, r=22, t=18, b=bottom),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="#FFFFFF",
        font=dict(family="Inter, Segoe UI, sans-serif", size=12, color="#203746"),
        legend=dict(title_text="", orientation="h", yanchor="bottom", y=1.01, x=0),
        showlegend=legend,
        hoverlabel=dict(bgcolor="#173647", font_color="white"),
    )
    fig.update_xaxes(gridcolor="#E6EDF1", zeroline=False, automargin=True)
    fig.update_yaxes(gridcolor="#E6EDF1", zeroline=False, automargin=True)
    return fig


def graph(
    fig: go.Figure,
    size: str = "standard",
    min_width: int | None = None,
):
    component = dcc.Graph(
        figure=fig,
        responsive=True,
        className=f"plot plot-{size}",
        style={"height": "var(--plot-height)", "minHeight": "var(--plot-height)",
               **({"minWidth": f"{min_width}px"} if min_width else {})},
        config={"displaylogo": False, "responsive": True, "modeBarButtonsToRemove": ["lasso2d", "select2d"]},
    )
    return html.Div(component, className="plot-scroll" if min_width else "plot-wrap")


def card(label: str, value: str, note: str, tone: str = "blue") -> html.Div:
    return html.Div([
        html.Div(label, className="metric-label"),
        html.Div(value, className="metric-value"),
        html.Div(note, className="metric-note"),
    ], className=f"metric-card tone-{tone}")


def panel(title: str, content, caption: str | None = None, wide: bool = False) -> html.Div:
    children = [html.Div(title, className="panel-title")]
    if caption:
        children.append(html.Div(caption, className="panel-caption"))
    children.append(content)
    return html.Div(children, className=f"panel{' panel-wide' if wide else ''}")


def heading(kicker: str, title: str, subtitle: str) -> html.Div:
    return html.Div([
        html.Div(kicker, className="section-kicker"),
        html.H2(title),
        html.P(subtitle),
    ], className="section-heading")


# Overview figures
quality_plot = quality.sort_values("affected_share")
fig_quality = px.bar(
    quality_plot, x=quality_plot["affected_share"] * 100, y="issue", orientation="h",
    color_discrete_sequence=["#356A8A"], custom_data=["business_meaning", "treatment"],
)
fig_quality.update_traces(
    texttemplate="%{x:.1f}%", textposition="outside",
    hovertemplate="<b>%{y}</b><br>%{x:.1f}% of applications<br><br><b>Why it matters:</b> %{customdata[0]}<br><b>How we handled it:</b> %{customdata[1]}<extra></extra>",
)
fig_quality.update_xaxes(title="Share of all applications (%)", range=[0, quality_plot.affected_share.max() * 118])
fig_quality.update_yaxes(title="")
chart_layout(fig_quality, legend=False, left=150)

fi = feature_importance.head(10).sort_values("mutual_info").copy()
fi["label"] = fi["feature"].map(FEATURE_LABELS).fillna(fi["feature"].str.replace("_", " ").str.title())
fig_importance = px.bar(fi, x="mutual_info", y="label", orientation="h", color_discrete_sequence=["#4F7D65"])
fig_importance.update_traces(hovertemplate="<b>%{y}</b><br>Mutual information: %{x:.4f}<extra></extra>")
fig_importance.update_xaxes(title="Mutual information with TARGET (training data)")
fig_importance.update_yaxes(title="")
chart_layout(fig_importance, legend=False, left=155)


# Segmentation figures
comparison_matrix = cluster_comparison.pivot(
    index="business_dimension", columns="Segment", values="portfolio_sd"
).reindex(columns=SEGMENT_ORDER)
fig_segment_heatmap = go.Figure(go.Heatmap(
    z=comparison_matrix.values,
    x=comparison_matrix.columns,
    y=comparison_matrix.index,
    colorscale=[[0, "#C97543"], [.5, "#F7F7F2"], [1, "#356A8A"]],
    zmid=0,
    text=np.round(comparison_matrix.values, 2),
    texttemplate="%{text:.2f}",
    colorbar=dict(title="From portfolio<br>average (SD)", thickness=14),
    hovertemplate="<b>%{x}</b><br>%{y}: %{z:.2f} SD from the portfolio average<extra></extra>",
))
chart_layout(fig_segment_heatmap, left=135, bottom=75)

fig_cluster_profiles = cluster_profile_matrix_figure()

fig_sizes = px.bar(
    cluster_names, x="n_applicants", y="nama", orientation="h", color="nama",
    color_discrete_map=SEGMENT_COLORS, category_orders={"nama": SEGMENT_ORDER},
    custom_data=["profile_summary", "watch_items"],
)
fig_sizes.update_traces(
    texttemplate="%{x:,}", textposition="outside",
    hovertemplate="<b>%{y}</b><br>%{x:,} applications<br>%{customdata[0]}<br><b>Check:</b> %{customdata[1]}<extra></extra>",
)
fig_sizes.update_xaxes(title="Applications", range=[0, cluster_names.n_applicants.max() * 1.20])
fig_sizes.update_yaxes(title="", categoryorder="array", categoryarray=SEGMENT_ORDER[::-1])
chart_layout(fig_sizes, legend=False, left=120)

kmeans_plot = cluster_viz.copy()
kmeans_plot["Segment"] = kmeans_plot["CLUSTER_KMEANS"].map(NAME_BY_ID)
kmeans_plot = stratified_sample(kmeans_plot, "Segment", 8_000)
fig_kmeans = px.scatter(
    kmeans_plot, x="PC1", y="PC2", color="Segment", color_discrete_map=SEGMENT_COLORS,
    opacity=.48, render_mode="webgl",
)
fig_kmeans.update_traces(marker=dict(size=4), hovertemplate="%{fullData.name}<br>PC1 %{x:.2f} · PC2 %{y:.2f}<extra></extra>")
chart_layout(fig_kmeans, bottom=60)

dense_db = dbscan_viz[dbscan_viz["IS_NOISE"].eq(0)]
noise_db = dbscan_viz[dbscan_viz["IS_NOISE"].eq(1)]
dense_db = dense_db.sample(min(11_000, len(dense_db)), random_state=42)
dbscan_plot = pd.concat([dense_db, noise_db], ignore_index=True)
dbscan_plot["Density status"] = np.where(dbscan_plot["IS_NOISE"].eq(1), "Noise point", "Dense area")
fig_dbscan = px.scatter(
    dbscan_plot.sort_values("IS_NOISE"), x="UMAP1", y="UMAP2", color="Density status",
    color_discrete_map={"Dense area": "#356A8A", "Noise point": "#B5534C"},
    opacity=.48, render_mode="webgl", custom_data=["SK_ID_CURR", "Segment", "DBSCAN_LABEL"],
)
fig_dbscan.update_traces(
    marker=dict(size=4),
    hovertemplate="Applicant %{customdata[0]}<br>%{customdata[1]}<br>DBSCAN label %{customdata[2]}<extra></extra>",
)
chart_layout(fig_dbscan, bottom=55)

fig_k_selection = go.Figure()
fig_k_selection.add_trace(go.Scatter(
    x=k_selection["k"], y=k_selection["silhouette"], mode="lines+markers",
    name="Silhouette", line=dict(color="#356A8A", width=3),
    hovertemplate="K=%{x}<br>Silhouette %{y:.3f}<extra></extra>",
))
fig_k_selection.add_vline(x=5, line_dash="dash", line_color="#B98535", annotation_text="Kept: K=5")
fig_k_selection.update_xaxes(title="Number of clusters (K)", dtick=1)
fig_k_selection.update_yaxes(title="Silhouette", rangemode="tozero")
chart_layout(fig_k_selection, legend=False)

if not pca_sensitivity.empty:
    fig_pca_sensitivity = px.scatter(
        pca_sensitivity, x="retained_variance", y="ari_vs_10pc", size="n_components",
        color="silhouette", color_continuous_scale="Blues",
        custom_data=["n_components", "silhouette", "min_cluster_share"],
    )
    fig_pca_sensitivity.update_traces(
        marker=dict(line=dict(width=1, color="white")),
        hovertemplate="%{customdata[0]} components<br>Variance kept %{x:.1%}<br>Agreement with 10 components (ARI) %{y:.3f}<br>Silhouette score %{customdata[1]:.3f}<extra></extra>",
    )
    fig_pca_sensitivity.update_xaxes(title="Retained variance", tickformat=".0%")
    fig_pca_sensitivity.update_yaxes(title="Agreement with 10-component result (ARI)", range=[0, 1.02])
    chart_layout(fig_pca_sensitivity, legend=False)
else:
    fig_pca_sensitivity = go.Figure().add_annotation(text="Run Phase 2 again to build this PCA check", showarrow=False)
    chart_layout(fig_pca_sensitivity, legend=False)


# Rule figures
fig_rules = px.scatter(
    rule_view.sort_values("rank"), x="lift", y="rank", color="Segment", size="confidence",
    color_discrete_map=SEGMENT_COLORS,
    custom_data=["short_rule", "support", "confidence", "support_count", "metric_scope"],
)
fig_rules.update_traces(
    hovertemplate="<b>Rule %{y}</b><br>%{customdata[0]}<br>Lift %{x:.2f} · support %{customdata[1]:.1%} (%{customdata[3]:,} applications)<br>Confidence %{customdata[2]:.1%}<br>%{customdata[4]}<extra></extra>"
)
fig_rules.update_xaxes(title="Lift (1.0 means no association)")
fig_rules.update_yaxes(title="Rule number", autorange="reversed", dtick=1)
chart_layout(fig_rules, bottom=60)

algo_plot = algo_comparison.copy()
algo_plot["label"] = algo_plot["Algoritma"].replace({
    "apriori": "Apriori", "fpgrowth": "FP-Growth", "eclat": "ECLAT",
    "fpgrowth_per_cluster": "Segment FP-Growth",
})
fig_algorithms = px.bar(algo_plot, x="label", y="Rules", color_discrete_sequence=["#64748B"])
fig_algorithms.update_traces(texttemplate="%{y:,}", textposition="outside")
fig_algorithms.update_xaxes(title=""); fig_algorithms.update_yaxes(title="Rules found")
chart_layout(fig_algorithms, legend=False, bottom=70)

if "support_records" in rule_segment.columns:
    fig_rule_segments = px.bar(
        rule_segment, x="mean_lift", y="Segment", orientation="h", color="Segment",
        color_discrete_map=SEGMENT_COLORS, custom_data=["mean_confidence", "support_records"],
    )
    fig_rule_segments.update_traces(
        texttemplate="%{x:.2f}×", textposition="outside",
        hovertemplate="%{y}<br>Average lift %{x:.2f}x<br>Average confidence %{customdata[0]:.1%}<br>Total rule matches %{customdata[1]:,} (may overlap)<extra></extra>",
    )
    fig_rule_segments.update_xaxes(title="Average lift of selected rules")
    fig_rule_segments.update_yaxes(title="")
    chart_layout(fig_rule_segments, legend=False, left=120)
else:
    fig_rule_segments = go.Figure().add_annotation(text="Run Phase 3 again to build this chart", showarrow=False)
    chart_layout(fig_rule_segments, legend=False)


# Anomaly figures
detector_counts = pd.DataFrame({
    "Detector": ["Adjusted IQR", "Z-score", "Mahalanobis", "Isolation Forest", "LOF", "DBSCAN noise", "Flagged by 3+ methods"],
    "Records": [anomaly_summary.N_IQR, anomaly_summary.N_ZSCORE, anomaly_summary.N_MAHALANOBIS,
                anomaly_summary.N_ISOFOREST, anomaly_summary.N_LOF, anomaly_summary.N_DBSCAN,
                anomaly_summary.HIGH_CONFIDENCE],
}).sort_values("Records")
fig_detectors = px.bar(detector_counts, x="Records", y="Detector", orientation="h", color_discrete_sequence=["#64748B"])
fig_detectors.update_traces(texttemplate="%{x:,}", textposition="outside")
fig_detectors.update_xaxes(title="Applications", range=[0, detector_counts.Records.max() * 1.35])
fig_detectors.update_yaxes(title="")
chart_layout(fig_detectors, legend=False, left=120)

fig_overlap = go.Figure(go.Heatmap(
    z=detector_overlap.values.astype(float), x=detector_overlap.columns, y=detector_overlap.index,
    colorscale="Blues", zmin=0, zmax=1, text=np.round(detector_overlap.values.astype(float), 2),
    texttemplate="%{text:.2f}", colorbar=dict(title="Jaccard", thickness=14),
    hovertemplate="%{y} × %{x}<br>Jaccard overlap %{z:.2f}<extra></extra>",
))
chart_layout(fig_overlap, left=105, bottom=85)

driver_plot = anomaly_drivers.head(12).sort_values("records")
fig_drivers = px.bar(
    driver_plot, x="records", y="Driver", orientation="h", color="Review Type",
    color_discrete_map=REVIEW_COLORS,
)
fig_drivers.update_traces(texttemplate="%{x:,}", textposition="outside")
fig_drivers.update_xaxes(title="Records flagged by 3+ methods"); fig_drivers.update_yaxes(title="")
chart_layout(fig_drivers, left=170)

review_long = anomaly_by_segment.reset_index(names="Segment").melt(
    id_vars="Segment", var_name="Review Type", value_name="Records"
)
fig_review_segment = px.bar(
    review_long, x="Records", y="Segment", color="Review Type", orientation="h",
    color_discrete_map=REVIEW_COLORS,
)
fig_review_segment.update_yaxes(title="", categoryorder="array", categoryarray=SEGMENT_ORDER[::-1])
fig_review_segment.update_xaxes(title="Records flagged by 3+ methods")
chart_layout(fig_review_segment, left=120)

anomaly_plot = anomaly_pca.copy()
high = anomaly_plot[anomaly_plot["anomaly_category"].eq("HIGH_CONFIDENCE_ANOMALY")]
other = anomaly_plot[~anomaly_plot.index.isin(high.index)]
other = stratified_sample(other, "anomaly_category", max(1, 12_000 - len(high)))
anomaly_plot = pd.concat([other, high], ignore_index=True)
anomaly_plot["Review status"] = anomaly_plot["anomaly_category"].map({
    "NORMAL": "Typical record",
    "WEAK_SIGNAL": "One detector flag",
    "MODERATE_ANOMALY": "Multiple detector flags",
    "HIGH_CONFIDENCE_ANOMALY": "Flagged by 3+ methods",
})
fig_anomaly_pca = px.scatter(
    anomaly_plot, x="PC1", y="PC2", color="Review status",
    color_discrete_map=SEVERITY_COLORS, opacity=.50, render_mode="webgl",
    category_orders={"Review status": list(SEVERITY_COLORS)},
)
fig_anomaly_pca.update_traces(marker=dict(size=4), hovertemplate="%{fullData.name}<br>PC1 %{x:.2f} · PC2 %{y:.2f}<extra></extra>")
chart_layout(fig_anomaly_pca, bottom=60)


# Outcome figures
rates = cluster_rates.set_index("Segment").reindex(SEGMENT_ORDER).reset_index()
fig_rates = px.bar(
    rates, x="default_rate", y="Segment", orientation="h", color="descriptive_risk_flag",
    color_discrete_map={True: "#B5534C", False: "#356A8A"},
    custom_data=["train_applicants", "defaults", "lift_vs_portfolio"],
)
fig_rates.add_vline(
    x=metric("observed_default_rate"), line_dash="dash", line_color="#203746",
    annotation_text=f"Training average: {fmt_pct(metric('observed_default_rate'))}",
)
fig_rates.update_traces(
    texttemplate="%{x:.1%}", textposition="outside",
    hovertemplate="<b>%{y}</b><br>Default rate %{x:.2%}<br>%{customdata[1]:,} defaults among %{customdata[0]:,} labeled training records<br>%{customdata[2]:.2f}x the training-set average<extra></extra>",
)
fig_rates.update_xaxes(title="Observed default rate (training data)", tickformat=".0%", range=[0, rates.default_rate.max() * 1.28])
fig_rates.update_yaxes(title="")
chart_layout(fig_rates, legend=False, left=120)

cm = backtest_cm.set_index("actual")[["Flag non-default", "Flag default"]]
fig_cm = go.Figure(go.Heatmap(
    z=cm.values, x=["Not flagged by cluster", "Flagged by cluster"], y=["TARGET = 0", "TARGET = 1"],
    colorscale="Blues", text=cm.values, texttemplate="%{text:,}", showscale=False,
    hovertemplate="%{y} / %{x}<br>%{z:,} labeled training applications<extra></extra>",
))
chart_layout(fig_cm, left=120, bottom=65)

fig_policy = go.Figure()
for col, label, color in [
    ("precision", "Precision", "#B5534C"),
    ("recall", "Recall", "#356A8A"),
    ("flagged_share", "Share sent to review", "#B98535"),
]:
    fig_policy.add_trace(go.Scatter(
        x=policy_sweep["threshold_uplift"], y=policy_sweep[col], mode="lines+markers",
        name=label, line=dict(color=color, width=3),
        hovertemplate=f"{label}: %{{y:.1%}}<br>Cutoff: %{{x:.2f}}x the training baseline<extra></extra>",
    ))
fig_policy.add_vline(x=1.10, line_dash="dash", line_color="#203746", annotation_text="Dashboard setting: 1.10x")
fig_policy.update_xaxes(title="Required cluster rate vs. training baseline")
fig_policy.update_yaxes(title="Share of labeled training records", tickformat=".0%", range=[0, 1])
chart_layout(fig_policy)

if not outcome_comparison.empty:
    metric_labels = {
        "precision": "Precision", "recall": "Recall", "average_precision": "Average precision",
        "roc_auc": "ROC AUC", "lift_vs_baseline": "Lift over training average",
    }
    comparison_plot = outcome_comparison.copy()
    comparison_plot["Metric"] = comparison_plot["metric"].map(metric_labels)
    comparison_plot["method"] = comparison_plot["method"].replace({
        "Cluster outcome alignment": "Cluster-based flag",
        "Supervised logistic diagnostic": "Logistic model check",
    })
    fig_objective = px.bar(
        comparison_plot, x="Metric", y="value", color="method", barmode="group",
        color_discrete_map={
            "Cluster-based flag": "#64748B",
            "Logistic model check": "#4F7D65",
        },
    )
    fig_objective.update_traces(texttemplate="%{y:.2f}", textposition="outside")
    fig_objective.update_yaxes(title="Metric value", rangemode="tozero")
    fig_objective.update_xaxes(title="")
    chart_layout(fig_objective, bottom=80)
else:
    fig_objective = go.Figure().add_annotation(text="Run Phase 4 again to build the logistic comparison", showarrow=False)
    chart_layout(fig_objective, legend=False)


TABLE_BASE = {
    "style_header": {
        "backgroundColor": "#E8EFF2", "fontWeight": "700", "color": "#173647",
        "border": "0", "padding": "10px",
    },
    "style_cell": {
        "fontFamily": "Inter, Segoe UI, sans-serif", "fontSize": 12, "padding": "9px",
        "textAlign": "left", "border": "1px solid #E4EBEF", "whiteSpace": "nowrap",
        "overflow": "hidden", "textOverflow": "ellipsis", "maxWidth": "280px",
    },
    "style_table": {"overflowX": "auto", "minWidth": "100%"},
}


rules_table = dash_table.DataTable(
    data=rule_view[["rank", "Segment", "short_rule", "support", "confidence", "lift", "metric_scope"]].to_dict("records"),
    columns=[
        {"name": "#", "id": "rank"}, {"name": "Segment", "id": "Segment"},
        {"name": "Condition pair", "id": "short_rule"},
        {"name": "Support", "id": "support", "type": "numeric", "format": Format(precision=1, scheme=Scheme.percentage)},
        {"name": "Confidence", "id": "confidence", "type": "numeric", "format": Format(precision=1, scheme=Scheme.percentage)},
        {"name": "Lift", "id": "lift", "type": "numeric", "format": Format(precision=2, scheme=Scheme.fixed)},
        {"name": "Scope", "id": "metric_scope"},
    ],
    page_size=8,
    sort_action="native",
    filter_action="native",
    tooltip_data=[
        {column: {"value": str(value), "type": "markdown"} for column, value in row.items()}
        for row in rule_view[["rank", "Segment", "short_rule", "support", "confidence", "lift", "metric_scope"]].to_dict("records")
    ],
    tooltip_duration=None,
    **TABLE_BASE,
)


ANOMALY_TABLE_COLUMNS = ["SK_ID_CURR", "Segment", "Review Type", "Priority", "Primary Driver", "Detected By"]
ANOMALY_TABLE_LABELS = {
    "SK_ID_CURR": "Applicant ID",
    "Segment": "Cluster",
    "Review Type": "Review type",
    "Priority": "Priority",
    "Primary Driver": "Main reason",
    "Detected By": "Methods",
}


def anomaly_page(frame: pd.DataFrame, page_current: int = 0, page_size: int = 10) -> list[dict]:
    start = page_current * page_size
    return frame.iloc[start:start + page_size][ANOMALY_TABLE_COLUMNS].to_dict("records")


def anomaly_table_component() -> dash_table.DataTable:
    return dash_table.DataTable(
        id="anomaly-table",
        data=anomaly_page(anomaly_investigation),
        columns=[{"name": ANOMALY_TABLE_LABELS[c], "id": c} for c in ANOMALY_TABLE_COLUMNS],
        page_current=0,
        page_size=10,
        page_count=max(1, math.ceil(len(anomaly_investigation) / 10)),
        page_action="custom",
        sort_action="custom",
        sort_mode="multi",
        sort_by=[],
        filter_action="custom",
        filter_query="",
        cell_selectable=True,
        style_data_conditional=[
            {"if": {"filter_query": '{Review Type} = "Data quality check"', "column_id": "Review Type"},
             "backgroundColor": "#FFF3DA", "fontWeight": "700"},
            {"if": {"filter_query": '{Review Type} = "Affordability and repayment review"', "column_id": "Review Type"},
             "backgroundColor": "#FBE9E7", "fontWeight": "700"},
            {"if": {"state": "active"}, "backgroundColor": "#DCEBF2", "border": "1px solid #356A8A"},
        ],
        **TABLE_BASE,
    )


def overview_layout() -> html.Section:
    return html.Section([
        heading("01 · DATA", "Start with the data we actually have",
                "We use train and test records to find patterns. Any check against TARGET uses the labeled training set only."),
        html.Div([
            card("Applications analysed", "356,255", "307,511 train + 48,744 test", "blue"),
            card("Training default rate", fmt_pct(metric("observed_default_rate"), 2), "TARGET=1 in the training data", "amber"),
            card("Customer groups", "5", "K-Means clusters, checked against Ward", "green"),
            card("Flagged by 3+ methods", fmt_int(anomaly_summary.HIGH_CONFIDENCE), "Sent to the review queue", "red"),
        ], className="metric-grid"),
        html.Div([
            panel("Data issues and how we handled them", graph(fig_quality, "standard"),
                  "A missing value can mean something different from a suspicious value, so we handle them separately."),
            panel("Which features relate to TARGET?", graph(fig_importance, "standard"),
                  "This training-only check happens after preprocessing. TARGET was not used to form the clusters."),
        ], className="two-col"),
        html.Div([
            html.Strong("What this report can do"),
            html.Span("This report describes patterns in the portfolio. It is not a probability-of-default model and cannot approve, reject, price, or explain a loan decision."),
        ], className="guardrail"),
    ], className="tab-section")


def segments_layout() -> html.Section:
    ward_text = "Result unavailable"
    if not method_agreement.empty:
        ward_text = f"ARI {method_agreement.adjusted_rand_index.iloc[0]:.3f}"
    return html.Section([
        heading("02 · CUSTOMER GROUPS", "How the five clusters differ",
                "The first chart shows broad patterns. The next one puts the actual values side by side, including the observed default rate for training records."),
        panel("Broad differences between clusters", graph(fig_segment_heatmap, "tall", min_width=720),
              "Each cell is the cluster average after the features in that row were standardized. Compare clusters across a row. A positive value means higher than the portfolio average, not better.", wide=True),
        html.H3("Cluster profiles", className="subsection-title"),
        panel(
            "Five clusters, side by side",
            graph(fig_cluster_profiles, "profile"),
            "Each column is one cluster, with its size and portfolio share in the header. Hover over a cell for the exact value, profile, checks, and suggested review. "
            "Colors reset on each row, so compare across a row only. Blue means a higher number and amber a lower one. Neither color means safer or riskier. "
            "All rows use train and test records except the observed default rate. That row uses labeled training records and did not affect clustering. "
            "A zero for repayment or card history can mean that no history was recorded.",
            wide=True,
        ),
        html.Div([
            panel("Cluster size", graph(fig_sizes, "standard")),
            panel("Choosing the number of clusters", graph(fig_k_selection, "standard"),
                  "K=3 gave the strongest sampled silhouette score. We kept K=5 because the five-group result was stable and gave the business more useful profiles."),
        ], className="two-col"),
        html.Div([
            panel("Does PCA change the groups?", graph(fig_pca_sensitivity, "standard"),
                  "This checks whether using 10 principal components materially changes who belongs to each cluster."),
            panel("Ward comparison", html.Div([
                html.Div(ward_text, className="method-value"),
                html.P("We compared the K-Means labels with a sampled Ward solution."),
                html.P("DBSCAN is shown separately because it finds dense areas and isolated points, not the same type of groups as K-Means."),
            ], className="method-box")),
        ], className="two-col"),
        html.Div([
            panel("K-Means on the first two principal components", graph(fig_kmeans, "map", min_width=620),
                  "A stratified sample of 8,000 applications. These two axes are for display. The clustering model used 10 components."),
            panel("DBSCAN density view", graph(fig_dbscan, "map"),
                  f"All {int(anomaly_summary.N_DBSCAN):,} noise points are shown. Dense points are sampled to keep the chart responsive."),
        ], className="two-col"),
    ], className="tab-section")


def rules_layout() -> html.Section:
    return html.Section([
        heading("03 · ASSOCIATION RULES", "Conditions that often appear together",
                "We removed rules that simply restate a formula. Each cluster rule uses only the applications in that cluster."),
        html.Div([
            panel("Rule strength and coverage", graph(fig_rules, "tall")),
            panel("Average rule lift by cluster", graph(fig_rule_segments, "tall")),
        ], className="two-col"),
        panel("Do the methods agree?", graph(fig_algorithms, "compact"),
              "Apriori, FP-Growth, and ECLAT found the same global rules. Cluster-level FP-Growth uses only the applications in each cluster, so its metrics have a different denominator.", wide=True),
        panel("Rules kept for review", html.Div(rules_table, className="table-shell"),
              "Filter by cluster or condition. The scope column tells you which applications were used to calculate support and confidence.", wide=True),
    ], className="tab-section")


def anomalies_layout() -> html.Section:
    counts = anomaly_investigation["Review Type"].value_counts()
    return html.Section([
        heading("04 · RECORDS TO REVIEW", "Why these unusual applications need a closer look",
                "A record enters the queue when at least three methods agree. The evidence tells the reviewer what to check. The flag itself is never a credit decision."),
        html.Div([
            card("Flagged by 3+ methods", fmt_int(anomaly_summary.HIGH_CONFIDENCE), "Stronger agreement between methods", "red"),
            card("Payment or affordability", fmt_int(counts.get("Affordability and repayment review", 0)), "Needs a focused review", "red"),
            card("Data problems", fmt_int(counts.get("Data quality check", 0)), "Confirm or fix the values first", "amber"),
            card("Unusual but plausible", fmt_int(counts.get("Unusual but plausible", 0)), "Unusual does not mean risky", "blue"),
        ], className="metric-grid"),
        html.Div([
            panel("Flags by method", graph(fig_detectors, "standard")),
            panel("Where methods agree", graph(fig_overlap, "standard", min_width=600),
                  "Jaccard compares the records shared by two methods, even when they flag different numbers of applications."),
        ], className="two-col"),
        html.Div([
            panel("Why records were flagged", graph(fig_drivers, "tall")),
            panel("Review queue by cluster", graph(fig_review_segment, "tall")),
        ], className="two-col"),
        panel("Where flagged records sit", graph(fig_anomaly_pca, "map"),
              "Every record flagged by three or more methods is shown. Other records are sampled so the chart stays responsive.", wide=True),
        panel("Applications to review", html.Div([
            html.P("Filter or sort the queue, then select an application to see the evidence and next step.", className="table-instruction"),
            html.Div(anomaly_table_component(), className="table-shell"),
            html.Div("Select an application to see its evidence.", id="anomaly-detail", className="record-detail"),
        ]), "The dashboard loads ten rows at a time. All 3,758 records remain available.", wide=True),
    ], className="tab-section")


def outcome_layout() -> html.Section:
    ref_precision = metric("precision", reference_metrics)
    ref_recall = metric("recall", reference_metrics)
    return html.Section([
        heading("05 · DEFAULT OUTCOME CHECK", "Clusters do not predict individual defaults well",
                "We compare each cluster's observed default rate with TARGET in the training data. A separate logistic model shows what changes when prediction is the goal."),
        html.Div([
            card("Cluster flag precision", fmt_pct(metric("precision"), 2), "Among applicants in flagged clusters", "red"),
            card("Cluster flag recall", fmt_pct(metric("recall"), 2), "Share of observed defaults captured", "blue"),
            card("Highest cluster rate", fmt_pct(metric("cluster_precision_ceiling"), 2), "Best rate available when selecting a whole cluster", "amber"),
            card("Logistic model check", f"{fmt_pct(ref_precision, 1)} / {fmt_pct(ref_recall, 1)}", "Precision / recall at the same review volume", "green"),
        ], className="metric-grid"),
        panel("Cluster flag vs. logistic check", graph(fig_objective, "standard"),
              "The logistic model shows what a prediction-focused method can do. It still needs full validation before deployment.", wide=True),
        html.Div([
            panel("Default rate by cluster", graph(fig_rates, "standard")),
            panel("Where the cluster flag is wrong", graph(fig_cm, "standard")),
        ], className="two-col"),
        panel("What changes when the cutoff moves", graph(fig_policy, "standard"),
              "The dashed line shows the project's 1.10x sensitivity setting: a cluster is flagged when its training default rate is at least 10% above that fold's training average. "
              "It is a transparent comparison point, not an optimized production cutoff. Moving it changes review volume and recall, but it cannot rank applicants within a cluster.", wide=True),
        html.Div([
            html.Strong("Before anyone uses these results"),
            html.Span("These results describe the dataset. They cannot approve, reject, price, or explain an individual loan decision. Production use would require time-based validation, calibration, fairness and proxy checks, policy approval, and ongoing monitoring."),
        ], className="guardrail"),
    ], className="tab-section")


TAB_BUILDERS = {
    "overview": overview_layout,
    "segments": segments_layout,
    "rules": rules_layout,
    "anomalies": anomalies_layout,
    "outcome": outcome_layout,
}


app = Dash(
    __name__,
    title="Home Credit Portfolio Analysis",
    assets_folder=str(ROOT / "dashboard/assets"),
    suppress_callback_exceptions=True,
)
server = app.server

app.layout = html.Div([
    html.Header([
        html.Div([
            html.Div("HOME CREDIT · PORTFOLIO ANALYSIS", className="eyebrow"),
            html.H1("What the Home Credit portfolio data tells us"),
            html.P("Five customer groups, recurring application patterns, unusual records, and a check against observed defaults."),
        ]),
        html.Div([
            html.Span("356,255 applications analysed"),
            html.Span("307,511 have TARGET labels"),
            html.Span("48,744 test rows have no TARGET label"),
        ], className="scope-badges"),
    ], className="hero"),
    dcc.Tabs(
        id="phase-tabs",
        value="overview",
        className="phase-tabs",
        parent_className="tabs-shell",
        children=[
            dcc.Tab(label="Overview", value="overview", className="phase-tab", selected_className="phase-tab selected"),
            dcc.Tab(label="Segments", value="segments", className="phase-tab", selected_className="phase-tab selected"),
            dcc.Tab(label="Rules", value="rules", className="phase-tab", selected_className="phase-tab selected"),
            dcc.Tab(label="Anomalies", value="anomalies", className="phase-tab", selected_className="phase-tab selected"),
            dcc.Tab(label="Outcome", value="outcome", className="phase-tab", selected_className="phase-tab selected"),
        ],
    ),
    dcc.Store(id="tab-scroll-signal"),
    html.Main(id="tab-content", className="phase-content"),
    html.Footer([
        html.Span("Methods and reasoning: REPORT.md and reports/reasoning_validation.md"),
        html.Span("Charts use files produced by the project notebooks"),
    ]),
], className="app-shell")


@app.callback(Output("tab-content", "children"), Input("phase-tabs", "value"))
def render_tab(value: str):
    return TAB_BUILDERS.get(value, overview_layout)()


app.clientside_callback(
    """
    function(value) {
        window.requestAnimationFrame(function() {
            const content = document.getElementById('tab-content');
            const tabs = document.querySelector('.tabs-shell');
            if (content) {
                const offset = tabs ? tabs.offsetHeight : 0;
                const top = content.getBoundingClientRect().top + window.scrollY - offset;
                window.scrollTo({top: Math.max(0, top), behavior: 'auto'});
            }
        });
        return Date.now();
    }
    """,
    Output("tab-scroll-signal", "data"),
    Input("phase-tabs", "value"),
    prevent_initial_call=True,
)


FILTER_OPERATORS = [
    (" ge ", ">="), (" le ", "<="), (" lt ", "<"), (" gt ", ">"),
    (" ne ", "!="), (" eq ", "="),
    (" scontains ", "contains"), (" contains ", "contains"),
]


def split_filter_part(filter_part: str):
    for token, operator in FILTER_OPERATORS:
        if token not in filter_part:
            continue
        name_part, value_part = filter_part.split(token, 1)
        column = name_part[name_part.find("{") + 1:name_part.rfind("}")]
        value_part = value_part.strip()
        if value_part and value_part[0] in {'"', "'", "`"}:
            value = value_part[1:-1].replace("\\" + value_part[0], value_part[0])
        else:
            try:
                value = float(value_part)
            except ValueError:
                value = value_part
        return column, operator, value
    return None, None, None


@app.callback(
    Output("anomaly-table", "data"),
    Output("anomaly-table", "page_count"),
    Input("anomaly-table", "page_current"),
    Input("anomaly-table", "page_size"),
    Input("anomaly-table", "sort_by"),
    Input("anomaly-table", "filter_query"),
    prevent_initial_call=False,
)
def update_anomaly_table(page_current, page_size, sort_by, filter_query):
    frame = anomaly_investigation.copy()
    for filter_part in (filter_query or "").split(" && "):
        column, operator, value = split_filter_part(filter_part)
        if not column or column not in frame.columns:
            continue
        series = frame[column]
        if operator == "contains":
            frame = frame[series.astype(str).str.contains(str(value), case=False, na=False)]
        elif operator == "=":
            frame = frame[series == value]
        elif operator == "!=":
            frame = frame[series != value]
        elif operator == ">=":
            frame = frame[series >= value]
        elif operator == "<=":
            frame = frame[series <= value]
        elif operator == "<":
            frame = frame[series < value]
        elif operator == ">":
            frame = frame[series > value]
    if sort_by:
        frame = frame.sort_values(
            [item["column_id"] for item in sort_by],
            ascending=[item["direction"] == "asc" for item in sort_by],
            kind="mergesort",
        )
    page_size = int(page_size or 10)
    page_current = min(int(page_current or 0), max(0, math.ceil(len(frame) / page_size) - 1))
    return anomaly_page(frame, page_current, page_size), max(1, math.ceil(len(frame) / page_size))


@app.callback(
    Output("anomaly-detail", "children"),
    Input("anomaly-table", "active_cell"),
    State("anomaly-table", "data"),
    prevent_initial_call=True,
)
def show_anomaly_detail(active_cell, page_data):
    if not active_cell or not page_data:
        return "Select an application to see its evidence."
    record_id = page_data[active_cell["row"]]["SK_ID_CURR"]
    row = anomaly_investigation.loc[anomaly_investigation.SK_ID_CURR.eq(record_id)].iloc[0]
    return html.Div([
        html.Div([
            html.Span(f"Applicant {int(row.SK_ID_CURR):,}", className="record-id"),
            html.Span(row["Priority"], className="record-priority"),
        ], className="record-head"),
        html.Div([html.Strong("Evidence"), html.P(row["Record Evidence"])]),
        html.Div([html.Strong("Why it matters"), html.P(row["Business Interpretation"])]),
        html.Div([html.Strong("What to do next"), html.P(row["Recommended Action"])]),
        html.Div([html.Strong("Review owner"), html.P(row["Review Owner"])]),
        html.Div("This flag cannot make an automatic decision.", className="no-auto"),
    ])


if __name__ == "__main__":
    app.run(
        host=os.getenv("DASH_HOST", "127.0.0.1"),
        port=int(os.getenv("DASH_PORT", "8050")),
        debug=False,
    )

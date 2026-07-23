"""Responsive, artifact-driven dashboard for Home Credit portfolio discovery."""

from __future__ import annotations

import base64
import math
import os
import textwrap
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash import ALL, Dash, Input, Output, State, ctx, dash_table, dcc, html


ROOT = Path(__file__).resolve().parents[1]
P1 = ROOT / "results/phase1_preprocessing"
P2 = ROOT / "results/phase2_clustering"
P3 = ROOT / "results/phase3_association"
P4 = ROOT / "results/phase4_anomaly"


def image_data_uri(path: Path) -> str:
    return "data:image/png;base64," + base64.b64encode(path.read_bytes()).decode("ascii")


LINKAGE_COMPARISON_SRC = image_data_uri(P2 / "linkage_comparison.png")


def read_csv(path: Path, **kwargs) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Could not find {path}. Run the notebooks in order to rebuild this dashboard file.")
    return pd.read_csv(path, **kwargs)


def read_optional(path: Path, columns: list[str] | None = None) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame(columns=columns or [])
    return pd.read_csv(path)


quality = read_csv(P1 / "data_quality_summary.csv")
portfolio = read_csv(P1 / "portfolio_context.csv")
cluster_names = read_csv(P2 / "cluster_names.csv").sort_values("cluster_id")
cluster_business = read_csv(P2 / "cluster_business_summary.csv")
cluster_feature_summary = read_csv(P2 / "cluster_summary.csv")
if "std_diff" not in cluster_feature_summary:
    if "rel_diff_pct" not in cluster_feature_summary:
        raise ValueError("cluster_summary.csv needs std_diff. Run Phase 2 again.")
    # Legacy Phase 2 stored standardized differences multiplied by 100 under
    # a misleading percent-style name. Convert that artifact back to SD units.
    cluster_feature_summary["std_diff"] = cluster_feature_summary["rel_diff_pct"] / 100
cluster_comparison = read_csv(P2 / "cluster_comparison_long.csv")
cluster_viz = read_csv(P2 / "cluster_viz_sample.csv")
dbscan_viz = read_csv(P2 / "dbscan_umap_sample.csv")
k_selection = read_csv(P2 / "k_selection.csv")
k_stability = read_csv(P2 / "k_stability.csv")
pca_sensitivity = read_optional(P2 / "pca_cluster_sensitivity.csv")
method_agreement = read_optional(P2 / "method_agreement.csv")
business_rules = read_csv(P3 / "business_rules_final.csv").sort_values("rank").reset_index(drop=True)
algo_comparison = read_csv(P3 / "algo_comparison.csv")
rule_screening = read_csv(P3 / "rule_screening_summary.csv")
anomaly_summary = read_csv(P4 / "anomaly_summary.csv").iloc[0]
anomaly_investigation = read_csv(P4 / "anomaly_investigation.csv")
segment_credit_concentration = read_csv(P4 / "segment_credit_concentration.csv")
anomaly_drivers = read_csv(P4 / "anomaly_driver_summary.csv")
anomaly_by_segment = read_csv(P4 / "anomaly_review_by_segment.csv", index_col=0)
detector_overlap = read_csv(P4 / "detector_jaccard_overlap.csv", index_col=0)
queue_sensitivity = read_csv(P4 / "ensemble_single_axis_sensitivity.csv")
anomaly_pca = read_csv(P4 / "pca_anomaly_sample.csv")

PORTFOLIO_VALUES = portfolio.set_index("measure")["value"].to_dict()
COMBINED_APPLICATIONS = int(
    PORTFOLIO_VALUES.get("Applications", PORTFOLIO_VALUES.get("Combined applications"))
)

if int(segment_credit_concentration["applications"].sum()) != COMBINED_APPLICATIONS:
    raise ValueError("Segment credit concentration does not reconcile to the application count.")

if "Queue Route" not in anomaly_investigation:
    anomaly_investigation["Queue Route"] = np.where(
        anomaly_investigation["Detector Count"].ge(3),
        "Detector consensus",
        "Extreme single-axis value",
    )

REQUIRED_BUSINESS_RULE_COLUMNS = {
    "rank", "business_rule", "Segment", "Context", "context_n", "condition_count",
    "support_count", "support", "consequent_baseline", "confidence", "uplift_pp", "lift",
    "business_theme", "source_families", "why_it_matters", "review_action", "caveat",
    "metric_scope",
}
missing_rule_columns = REQUIRED_BUSINESS_RULE_COLUMNS.difference(business_rules.columns)
if missing_rule_columns:
    raise ValueError(
        "business_rules_final.csv is missing fields needed by the dashboard: "
        + ", ".join(sorted(missing_rule_columns))
        + ". Run Phase 3 again."
    )


CLUSTER_COPY = {
    "Historical Card-Use Intensity": {
        "profil_risiko": "Revolving-credit history review",
        "profile_summary": "This group has the heaviest recorded revolving-credit use in previous Home Credit accounts.",
        "watch_items": "Verify current balances, utilisation, arrears, affordability, and whether any existing limit still fits.",
        "recommended_action": "Use the historical pattern to focus the review, then verify the current position before changing a limit or exposure.",
    },
    "Repayment-Stress History": {
        "profil_risiko": "Repayment review",
        "profile_summary": "Late repayments are what most clearly set this group apart.",
        "watch_items": "Check when the delays happened, how serious they were, whether they were cured, and what the applicant can afford now.",
        "recommended_action": "Review the repayment history and current affordability. If the applicant is already in hardship, follow the contact or restructuring policy.",
    },
    "Lower-Intensity Credit Footprint": {
        "profil_risiko": "Standard evidence review",
        "profile_summary": "This group has lower product activity and smaller loan amounts than the other segments.",
        "watch_items": "Check coverage source by source. Lower activity does not mean that useful history is absent or that payment risk is lower.",
        "recommended_action": "Use the standard underwriting process. Ask for permitted supporting evidence only when a relevant source is genuinely unavailable.",
    },
    "Larger-Loan Affordability": {
        "profil_risiko": "Affordability review",
        "profile_summary": "This group has larger current-loan credit amounts and the highest scheduled payment burden.",
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
        "This source did not return or record a score. The dataset does not say why, and missing information is not adverse behaviour.",
        "Use the median for modelling and keep a separate missing-score flag.",
    ),
    "No car-age value": (
        "No car age recorded",
        "This usually means that the applicant does not own a car.",
        "Set car age to zero and keep a separate no-car flag.",
    ),
}

ANOMALY_DRIVER_LABELS = {
    "Current product delinquency signal": "Recorded card or POS arrears",
    "Material installment delinquency": "Long instalment delay",
    "Persistent underpayment": "Repeated underpayment",
    "Repeated severe installment lateness": "Repeated severe instalment delays",
    "High revolving-credit utilisation": "High previous-account card utilisation",
    "High card utilisation": "High historical card utilisation",
    "Card or POS arrears": "Historical card or POS arrears",
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
    "Unusual AMT_CREDIT": "Unusual current-loan credit amount",
    "Unusual BUREAU_DEBT_TO_CREDIT_RATIO": "Unusual bureau debt-to-credit ratio",
    "Unusual CC_UTILIZATION_MAX": "Unusual maximum previous-account card utilisation",
    "Unusual CREDIT_TO_ANNUITY": "Unusual credit-to-annuity proxy",
    "Unusual CREDIT_TO_INCOME": "Unusual credit-to-income ratio",
}

ANOMALY_INTERPRETATION_COPY = {
    "The unusual pattern is supported by repayment-capacity or delinquency evidence. It warrants a specific manual review, not an automatic adverse action.": (
        "Repayment or affordability evidence supports this flag. A reviewer should check it before anyone takes action."
    ),
    "The record contains a logical or unit inconsistency. This is a data-governance issue, not evidence that the applicant will default.": (
        "The values do not agree or may use different units. Confirm or fix the data before using it. This is not evidence of payment difficulty."
    ),
    "The applicant is statistically unusual but has no identified affordability, delinquency, or logical-data breach. Rarity alone is not a credit-risk conclusion.": (
        "This application is unusual, but we found no clear affordability, repayment, or data-quality problem. Unusual does not mean risky."
    ),
}

REVIEW_TYPE_LABELS = {
    "Affordability / repayment review": "Affordability and repayment review",
    "Data consistency check": "Source reconciliation",
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
    "review current card balances, payment capacity, and limit suitability; do not infer distress from utilisation alone": "The recorded utilisation comes from previous Home Credit accounts. Verify whether a revolving facility is still open, obtain its current balance and payment status, and assess limit suitability only if a current limit exists. Historical high utilisation alone does not prove financial distress.",
    "inspect recency and product-level arrears before changing exposure": "The recorded card or POS arrears are historical aggregates. Check the source timeline, cure status, and whether any related facility is still open before changing current exposure.",
    "reconcile outstanding external obligations and include them in the affordability calculation": "Confirm outstanding external debts and include them in the affordability calculation.",
    "verify bureau recency, dispute status, and cure information before relying on the signal": "Check how recent the bureau arrears are, whether they are disputed, and whether they were cured.",
    "review the underlying bureau information and use specific verified reasons rather than the score alone": "Confirm which external scores were observed and whether their sources are valid. Reconcile them with directly observed income, repayment, and bureau evidence; do not use the combined score as a reason code.",
    "reconcile the earlier refusal reasons and confirm whether they remain current": "Check why earlier applications were refused and whether those reasons still apply.",
    "check reversals, prepayments, duplicated installments, and currency units": "Check for reversals, early payments, duplicate instalments, and inconsistent currency units.",
    "confirm the unusual fields and otherwise continue through the standard underwriting path": "Confirm the unusual values. If they are correct, continue with standard underwriting.",
}

FEATURE_TEXT_LABELS = {
    "BUREAU_DEBT_TO_CREDIT_RATIO": "bureau debt-to-credit ratio",
    "INST_PAYMENT_RATIO_MEAN": "average payment-to-due ratio",
    "CC_UTILIZATION_MEAN": "average previous-account card utilisation",
    "CC_UTILIZATION_MAX": "maximum previous-account card utilisation",
    "CREDIT_TO_ANNUITY": "credit-to-annuity payment-size proxy",
    "ANNUITY_TO_INCOME": "annuity-to-income ratio",
    "CREDIT_TO_INCOME": "credit-to-income ratio",
    "AMT_INCOME_TOTAL": "reported income",
    "CC_AMT_BALANCE_MEAN": "average previous-account card balance",
    "AMT_ANNUITY": "annuity amount",
    "AMT_CREDIT": "current-loan credit amount",
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


def humanize_business_pattern(value: str) -> str:
    """Turn the exported condition/evidence pair into a presentation label."""
    raw = str(value).replace("→", "->")
    if "->" not in raw:
        return as_sentence(raw.replace("_", " ")).rstrip(".")
    condition, evidence = [part.strip() for part in raw.split("->", 1)]
    condition = condition[0].upper() + condition[1:] if condition else "Condition"
    evidence = evidence[0].lower() + evidence[1:] if evidence else "associated evidence"
    return f"{condition}; also observed more often: {evidence}"


def clean_rule_prose(value: str) -> str:
    """Apply small terminology fixes without changing the exported evidence."""
    text = str(value).strip()
    replacements = {
        "requested credit": "current-loan credit amount",
        "low default risk": "a lower chance of payment difficulty",
        ".Then ": ". Then ",
        ";Then ": "; then ",
        "; then ": ". Then ",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


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
        "requested credit is": "current-loan credit amount equals",
        "x reported income": " times reported income",
        "maximum observed installment delay is": "the longest observed instalment delay is",
        "mean paid amount is": "the average payment is",
        "mean card utilisation is": "average previous-account card utilisation is",
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
    introduction = f"For application {int(row['SK_ID_CURR']):,}, start with the {str(driver).lower()} shown in the evidence."
    guardrail = "Document what you checked in the case file. The cluster label alone is not a reason for a decision."
    return " ".join([introduction, *parts, guardrail])


for segment, copy in CLUSTER_COPY.items():
    mask = cluster_names["nama"].eq(segment)
    for column, value in copy.items():
        cluster_names.loc[mask, column] = value

for old_issue, (issue, meaning, treatment) in QUALITY_COPY.items():
    mask = quality["issue"].eq(old_issue)
    quality.loc[mask, ["issue", "business_meaning", "treatment"]] = [issue, meaning, treatment]

business_rules["Business pattern"] = business_rules["business_rule"].map(humanize_business_pattern)
for column in ["why_it_matters", "review_action", "caveat", "metric_scope"]:
    business_rules[column] = business_rules[column].map(clean_rule_prose)
for column in ["rank", "context_n", "condition_count", "support_count"]:
    business_rules[column] = pd.to_numeric(business_rules[column], errors="raise").round().astype(int)
for column in ["support", "consequent_baseline", "confidence", "uplift_pp", "lift"]:
    business_rules[column] = pd.to_numeric(business_rules[column], errors="raise")
business_rules["condition_share"] = business_rules["condition_count"] / business_rules["context_n"]
business_rules["baseline_count"] = np.rint(
    business_rules["consequent_baseline"] * business_rules["context_n"]
).astype(int)

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
# Assigned by position, not by name. Phase 2 renames segments whenever the
# feature set changes, and a name-keyed palette silently fell back to Plotly
# defaults the moment that happened.
SEGMENT_PALETTE = ["#64748B", "#356A8A", "#4F7D65", "#B5534C", "#B98535",
                   "#7A5C8E", "#4A7C87", "#996B4F"]
SEGMENT_COLORS = {
    name: SEGMENT_PALETTE[i % len(SEGMENT_PALETTE)]
    for i, name in enumerate(SEGMENT_ORDER)
}
# Short forms for axis ticks. Full segment names ("Historical Card-Use
# Intensity") are 20-30 characters; on a narrow chart axis five of them
# collide with each other or with adjacent cell text. The full name is
# always still available in the hover tooltip.
CONTEXT_SHORT = {
    "Portfolio-wide": "Portfolio-wide",
    "Lower-Intensity Credit Footprint": "Lower-Intensity",
    "Historical Card-Use Intensity": "Card-Use Intensity",
    "History-Rich Credit User": "History-Rich",
    "Larger-Loan Affordability": "Larger-Loan",
    "Repayment-Stress History": "Repayment-Stress",
}
REVIEW_COLORS = {
    "Affordability and repayment review": "#B5534C",
    "Source reconciliation": "#B98535",
    "Unusual but plausible": "#356A8A",
}
SEVERITY_COLORS = {
    "No detector flag": "#CBD5E1",
    "One detector flag": "#D5AE5D",
    "Two detector signals": "#C97543",
    "Targeted review queue": "#A93F3A",
}
FEATURE_LABELS = {
    "EXT_SOURCE_1": "External score 1",
    "EXT_SOURCE_2": "External score 2",
    "EXT_SOURCE_3": "External score 3",
    "AMT_INCOME_TOTAL": "Income",
    "AMT_CREDIT": "Current-loan credit amount",
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
    "CC_UTILIZATION_MEAN": "Average previous-account card utilisation",
    "CC_UTILIZATION_MAX": "Maximum previous-account card utilisation",
    "CC_AMT_BALANCE_MEAN": "Average previous-account card balance",
    "CC_MONTHS_COUNT": "Previous-account card monthly records",
    "CC_SK_DPD_MEAN": "Average previous-account card delay (days)",
    "AMT_REQ_CREDIT_BUREAU_YEAR": "Recent bureau enquiries",
    "CREDIT_TO_ANNUITY": "Credit / annuity proxy",
}

def fmt_int(value: float) -> str:
    return "N/A" if not np.isfinite(value) else f"{int(round(value)):,}"


def fmt_pct(value: float, digits: int = 1) -> str:
    return "N/A" if not np.isfinite(value) else f"{value * 100:.{digits}f}%"


def require_one(frame: pd.DataFrame, mask: pd.Series, description: str) -> pd.Series:
    """Return one required business-evidence row with an actionable error."""
    matches = frame.loc[mask]
    if len(matches) != 1:
        raise ValueError(
            f"Expected exactly one {description} row, found {len(matches)}. "
            "Rebuild the phase artifacts before starting the dashboard."
        )
    return matches.iloc[0]


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
    concentration_identity = (
        segment_credit_concentration[["CLUSTER_KMEANS", "Segment"]]
        .sort_values("CLUSTER_KMEANS")
        .reset_index(drop=True)
    )
    if not expected.equals(business_identity):
        raise ValueError("Phase 2 files disagree on cluster names, IDs, or applicant counts. Run Phase 2 again.")
    if not expected[["CLUSTER_KMEANS", "Segment"]].equals(concentration_identity):
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
        segment_credit_concentration[[
            "CLUSTER_KMEANS", "credit_amount_share", "annuity_amount_share",
        ]],
        on="CLUSTER_KMEANS",
        how="left",
        validate="one_to_one",
    )
)
COMBINED_APPLICATIONS = int(cluster_detail["n_applicants"].sum())
cluster_detail["portfolio_share"] = cluster_detail["n_applicants"] / COMBINED_APPLICATIONS

PROFILE_METRICS = [
    ("median_income", "Median income", "amount", "Median across applications"),
    ("median_credit", "Median current-loan credit amount", "amount", "Median across applications"),
    ("median_credit_to_income", "Credit / income", "multiple", "Median across applications"),
    ("median_annuity_to_income", "Annuity / income", "pct", "Median across applications"),
    ("median_installment_late_share", "Instalment late share", "pct", "Median across all applications. A zero can mean no recorded history"),
    ("median_external_score_2", "External score 2", "decimal", "Observed or imputed value used for clustering"),
    ("median_card_utilisation", "Historical card utilisation", "pct", "Previous-credit history. A zero can mean no recorded history"),
    ("credit_amount_share", "Share of portfolio loan amount", "pct", "Segment total of recorded loan amounts over the portfolio total"),
]

PROFILE_AXIS_LABELS = {
    "median_income": "Median income",
    "median_credit": "Current-loan credit",
    "median_credit_to_income": "Credit / income",
    "median_annuity_to_income": "Annuity / income",
    "median_installment_late_share": "Late instalments",
    "median_external_score_2": "External score 2",
    "median_card_utilisation": "Historical card utilisation",
    "credit_amount_share": "Loan amount share",
}

def wrap_segment_name(name: str, width: int = 16) -> str:
    """Two-line axis label for a segment name.

    Derived rather than hard-coded: Phase 2 renames segments whenever the
    feature set changes, and a missing key here used to raise KeyError and take
    the whole Segments page down with it.
    """
    words = str(name).split()
    if not words:
        return str(name)
    lines, current = [], words[0]
    for word in words[1:]:
        if len(current) + 1 + len(word) <= width:
            current = f"{current} {word}"
        else:
            lines.append(current)
            current = word
    lines.append(current)
    return "<br>".join(lines[:2]) if len(lines) <= 2 else "<br>".join(
        [lines[0], " ".join(lines[1:])]
    )


SEGMENT_HEADER_LABELS = {name: wrap_segment_name(name) for name in cluster_names["nama"]}
SEGMENT_TICK_LABELS = {
    row["nama"]: (
        f"<b>{SEGMENT_HEADER_LABELS[row['nama']]}</b><br>"
        f"{int(row['n_applicants']):,} applications<br>{row['portfolio_share']:.1%} of the portfolio"
    )
    for _, row in cluster_detail.iterrows()
}


def format_profile_value(value: float, kind: str) -> str:
    if not np.isfinite(value):
        return "N/A"
    if kind == "count":
        return fmt_int(value)
    if kind == "amount":
        return f"{value:,.0f}"
    if kind == "pct":
        return fmt_pct(value, 1)
    if kind == "multiple":
        return f"{value:.2f}x"
    if kind == "decimal":
        return f"{value:.3f}"
    return f"{value:,.2f}"


def format_profile_cell(value: float, kind: str) -> str:
    if not np.isfinite(value):
        return "N/A"
    if kind == "amount":
        return f"{value / 1000:.0f}k"
    return format_profile_value(value, kind)


def wrap_hover(value: str, width: int = 42) -> str:
    return "<br>".join(textwrap.wrap(str(value), width=width))


def cluster_top_features(cluster_id: int, limit: int = 3) -> str:
    features = (
        cluster_feature_summary.loc[cluster_feature_summary["cluster_id"].eq(cluster_id)]
        .assign(magnitude=lambda frame: frame["std_diff"].abs())
        .sort_values("magnitude", ascending=False)
        .head(limit)
    )
    labels = []
    for item in features.itertuples():
        feature = FEATURE_LABELS.get(item.fitur, item.fitur.replace("_", " ").title())
        direction = "above" if item.std_diff >= 0 else "below"
        labels.append(f"{feature}: {abs(item.std_diff):.2f} SD {direction} the portfolio mean")
    return "<br> " + "<br> ".join(labels)


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
            if key == "credit_amount_share":
                comparison_note = (
                    f"This segment holds {value:.1%} of all recorded loan amounts "
                    f"while holding {row['portfolio_share']:.1%} of applications<br>"
                    "Amounts are recorded loan values, not balances or losses"
                )
            else:
                tied = np.isclose(values.to_numpy(), float(value), rtol=1e-9, atol=1e-12)
                tie_count = int(tied.sum())
                higher_count = int((values > float(value) + 1e-12).sum())
                lower_count = int((values < float(value) - 1e-12).sum())
                if tie_count == len(values):
                    rank_word = "Tied across all five segments"
                elif tie_count > 1 and higher_count == 0:
                    rank_word = "Tied highest"
                elif tie_count > 1 and lower_count == 0:
                    rank_word = "Tied lowest"
                elif tie_count > 1:
                    rank_word = "Tied in the middle"
                else:
                    rank = int(ranks.loc[segment])
                    rank_word = {
                        1: "Highest", 2: "Second-highest", 3: "Middle",
                        4: "Second-lowest", 5: "Lowest",
                    }[rank]
                comparison_note = (
                    f"{rank_word} for this measure; "
                    "this rank is descriptive, not a risk grade"
                )
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
    mobile_min_width: int | None = None,
):
    style = {
        "height": "var(--plot-height)",
        "minHeight": "var(--plot-height)",
        **({"minWidth": f"{min_width}px"} if min_width else {}),
        **({"--mobile-min-width": f"{mobile_min_width}px"} if mobile_min_width else {}),
    }
    component = dcc.Graph(
        figure=fig,
        responsive=True,
        className=f"plot plot-{size}",
        style=style,
        config={"displaylogo": False, "responsive": True, "modeBarButtonsToRemove": ["lasso2d", "select2d"]},
    )
    classes = ["plot-scroll" if min_width else "plot-wrap"]
    if mobile_min_width:
        classes.append("plot-scroll-mobile")
    return html.Div(component, className=" ".join(classes))


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

# Evidence coverage per segment: which review sources actually exist for the
# applications in each group. This replaces the earlier label-association
# chart; the portfolio is presented without any outcome label.
#
# Short axis labels plus FIXED (non-automargin) margins, sized by hand for
# the longest short label on each axis. automargin measures rendered tick
# text and can settle on a bad value the first time this chart mounts inside
# a Dash tab-switch callback; a fixed margin has no such measurement step,
# so it cannot mis-fire.
EVIDENCE_SOURCE_SHORT = {
    "Previous Home Credit card history": "Prior card history",
    "At least one external score": "Any external score",
}
evidence_coverage = read_csv(P2 / "segment_evidence_coverage.csv")
coverage_matrix = evidence_coverage.pivot(
    index="Evidence source", columns="Segment", values="coverage"
).reindex(columns=SEGMENT_ORDER)
fig_evidence_coverage = go.Figure(go.Heatmap(
    z=coverage_matrix.values,
    x=[CONTEXT_SHORT.get(c, c) for c in coverage_matrix.columns],
    y=[EVIDENCE_SOURCE_SHORT.get(r, r) for r in coverage_matrix.index],
    colorscale=[[0, "#F7F7F2"], [1, "#356A8A"]],
    zmin=0,
    zmax=1,
    text=np.vectorize(lambda v: f"{v:.0%}")(coverage_matrix.values),
    texttemplate="%{text}",
    textfont=dict(size=12, color="#173647"),
    showscale=False,
    hovertemplate=(
        "<b>%{x}</b><br>%{y}: %{z:.0%} of applications<extra></extra>"
    ),
))
fig_evidence_coverage.update_layout(
    template="plotly_white",
    autosize=True,
    margin=dict(l=150, r=20, t=10, b=40),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="#FFFFFF",
    font=dict(family="Inter, Segoe UI, sans-serif", size=12, color="#203746"),
    showlegend=False,
    hoverlabel=dict(bgcolor="#173647", font_color="white"),
)
fig_evidence_coverage.update_xaxes(gridcolor="#E6EDF1", zeroline=False, automargin=False, tickangle=0)
fig_evidence_coverage.update_yaxes(gridcolor="#E6EDF1", zeroline=False, automargin=False)


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
fig_kmeans.update_traces(marker=dict(size=4), hovertemplate="%{fullData.name}<br>PC1 %{x:.2f} - PC2 %{y:.2f}<extra></extra>")
chart_layout(fig_kmeans, bottom=60)
# Five long segment names wrap onto several legend rows once the chart fits
# its column instead of forcing a horizontal scrollbar; reserve headroom.
fig_kmeans.update_layout(margin=dict(t=70), legend=dict(font=dict(size=11)))

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
    hovertemplate="Application %{customdata[0]}<br>%{customdata[1]}<br>DBSCAN label %{customdata[2]}<extra></extra>",
)
chart_layout(fig_dbscan, bottom=55)

stability_view = (
    k_stability.groupby("k", as_index=False)["adjusted_rand_index"]
    .mean()
    .rename(columns={"adjusted_rand_index": "mean_ari"})
)
stability_by_k = stability_view.set_index("k")["mean_ari"]
fig_k_selection = make_subplots(
    rows=2, cols=1, shared_xaxes=True, vertical_spacing=.16,
    subplot_titles=("Separation on one fixed evaluation sample", "Seed stability for the detailed alternatives"),
)
fig_k_selection.add_trace(go.Scatter(
    x=k_selection["k"], y=k_selection["silhouette"], mode="lines+markers",
    name="Silhouette", line=dict(color="#356A8A", width=3),
    hovertemplate="K=%{x}<br>Silhouette %{y:.3f}<extra></extra>",
), row=1, col=1)
fig_k_selection.add_trace(go.Bar(
    x=stability_view["k"], y=stability_view["mean_ari"], name="Mean seed ARI",
    marker_color=["#4F7D65" if int(k) == 5 else "#CBD5E1" for k in stability_view["k"]],
    text=stability_view["mean_ari"], texttemplate="%{text:.3f}", textposition="outside",
    hovertemplate="K=%{x}<br>Mean seed ARI %{y:.3f}<extra></extra>",
), row=2, col=1)
fig_k_selection.add_vline(
    x=5, line_dash="dash", line_color="#B98535",
    annotation_text="K=5 selected", annotation_position="top left",
    annotation_font=dict(size=11, color="#8A6A2E"),
    row=1, col=1,
)
# Row 2 repeats the same line without a second text label: the green bar
# already marks K=5, and a duplicate annotation collided with its value text.
fig_k_selection.add_vline(x=5, line_dash="dash", line_color="#B98535", row=2, col=1)
fig_k_selection.update_xaxes(title="Number of segments (K)", dtick=1, row=2, col=1)
fig_k_selection.update_yaxes(title="Silhouette", rangemode="tozero", row=1, col=1)
fig_k_selection.update_yaxes(title="Mean ARI", range=[0, 1.15], row=2, col=1)
chart_layout(fig_k_selection, legend=False)
fig_k_selection.update_layout(height=500)

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


# Rule figures. The business view compares each rule with its own stated
# population. That matters because portfolio-wide and segment rules do not use
# the same denominator.
#
# Axis labels stay compact on purpose: the full business sentence made every
# tick three to four lines tall, which overlapped the neighbouring rows. The
# tick now carries the rule number, a short context, and a shorthand pattern;
# the complete sentence lives in the hover.
RULE_TOKEN_SHORT = {
    "bureau_debt_high": "bureau debt ≥80%",
    "bureau_debt_moderate": "bureau debt 30-80%",
    "bureau_debt_low": "bureau debt <30%",
    "external_score_weak": "weak external scores",
    "external_score_strong": "strong external scores",
    "card_utilisation_high": "card use ≥80%",
    "card_utilisation_moderate": "card use <80%",
    "previous_refusals_repeated": "3+ prior refusals",
    "previous_approval_high": "75%+ prior approvals",
    "previous_outcome_mixed": "mixed prior outcomes",
    "repayment_some_late": "some late instalments",
    "repayment_serious_late": "serious late instalments",
    "repayment_clean_observed": "clean instalments",
    "credit_large": "larger loan",
    "credit_medium": "mid-size loan",
    "credit_small": "smaller loan",
    "leverage_over_6x": "loan >6x income",
    "leverage_3_to_6x": "loan 3-6x income",
    "leverage_under_3x": "loan <3x income",
    "burden_under_20pct": "payment <20% income",
    "burden_20_to_35pct": "payment 20-35% income",
    "burden_over_35pct": "payment >35% income",
}


def compact_rule_pattern(rule_str: str) -> str:
    left, right = str(rule_str).split(" -> ", 1)
    tokens = lambda side: [t.strip() for t in side.strip("{}").split(",") if t.strip()]
    describe = lambda side: " + ".join(
        RULE_TOKEN_SHORT.get(t, t.replace("_", " ")) for t in tokens(side)
    )
    return f"{describe(left)} → {describe(right)}"


def rule_tick_label(row) -> str:
    pattern_lines = textwrap.wrap(compact_rule_pattern(row["rule_str"]), width=42)[:2]
    context = CONTEXT_SHORT.get(str(row["Context"]), str(row["Context"]))
    return (
        f"<b>R{int(row['rank']):02d} | {context}</b><br>"
        + "<br>".join(pattern_lines)
    )


rule_plot = business_rules.sort_values(["uplift_pp", "rank"]).copy()
rule_plot["plot_label"] = rule_plot.apply(rule_tick_label, axis=1)

fig_signal_agreement = go.Figure()
for row in rule_plot.itertuples(index=False):
    fig_signal_agreement.add_trace(go.Scatter(
        x=[row.consequent_baseline, row.confidence],
        y=[row.plot_label, row.plot_label],
        mode="lines",
        line=dict(color="#AFCBD7", width=3),
        hoverinfo="skip",
        showlegend=False,
    ))

fig_signal_agreement.add_trace(go.Scatter(
    x=rule_plot["consequent_baseline"],
    y=rule_plot["plot_label"],
    mode="markers",
    name="Context baseline",
    marker=dict(color="#CBD5E1", size=10, symbol="circle", line=dict(color="#64748B", width=1)),
    customdata=rule_plot[[
        "Context", "context_n", "consequent_baseline", "business_theme", "source_families",
        "Business pattern",
    ]].to_numpy(),
    hovertemplate=(
        "<b>%{customdata[5]}</b><br>Context: %{customdata[0]}<br>"
        "Evidence baseline: %{customdata[2]:.2%} of %{customdata[1]:,} applications<br>"
        "Business meaning: %{customdata[3]}<br>Sources: %{customdata[4]}<extra></extra>"
    ),
))
fig_signal_agreement.add_trace(go.Scatter(
    x=rule_plot["confidence"],
    y=rule_plot["plot_label"],
    mode="markers+text",
    name="When the condition is present",
    marker=dict(color="#356A8A", size=12, symbol="diamond", line=dict(color="#FFFFFF", width=1)),
    text=[f"{value:+.1f} pp" for value in rule_plot["uplift_pp"]],
    textposition="middle right",
    cliponaxis=False,
    customdata=rule_plot[[
        "Context", "context_n", "condition_count", "support_count", "support",
        "consequent_baseline", "confidence", "uplift_pp", "lift", "business_theme",
        "Business pattern",
    ]].to_numpy(),
    hovertemplate=(
        "<b>%{customdata[10]}</b><br>Context: %{customdata[0]} (%{customdata[1]:,} applications)<br>"
        "Condition and evidence: %{customdata[3]:,} of %{customdata[2]:,} condition-matching applications "
        "(%{customdata[6]:.2%})<br>Support in the full context: %{customdata[4]:.2%}<br>"
        "Context baseline: %{customdata[5]:.2%}<br>Difference: %{customdata[7]:+.2f} percentage points<br>"
        "Association lift: %{customdata[8]:.3f}x<br>Business meaning: %{customdata[9]}<extra></extra>"
    ),
))
fig_signal_agreement.update_xaxes(
    title="Observed evidence rate",
    tickformat=".0%",
    range=[
        max(0, float(rule_plot["consequent_baseline"].min()) - .05),
        min(1, float(rule_plot["confidence"].max()) + .16),
    ],
)
fig_signal_agreement.update_yaxes(
    title="",
    categoryorder="array",
    categoryarray=rule_plot["plot_label"].tolist(),
    tickfont=dict(size=11),
)
chart_layout(fig_signal_agreement, left=265, bottom=58)


# One highest-uplift example from each business interpretation theme keeps the
# executive view focused. The Rules tab retains all shortlisted patterns.
# Operational reach: how much of each rule's context contains the condition,
# and how much contains both the condition and its associated evidence.
rule_workload = business_rules.sort_values(["support", "rank"]).copy()
rule_workload["context_label"] = rule_workload.apply(rule_tick_label, axis=1)
fig_rule_workload = go.Figure()
fig_rule_workload.add_trace(go.Bar(
    x=rule_workload["condition_share"],
    y=rule_workload["context_label"],
    orientation="h",
    name="Condition present",
    marker_color="#AFCBD7",
    text=[
        f"{count:,} / {context:,}"
        for count, context in zip(rule_workload["condition_count"], rule_workload["context_n"])
    ],
    textposition="outside",
    customdata=rule_workload[["condition_count", "context_n", "Business pattern"]].to_numpy(),
    hovertemplate=(
        "<b>%{customdata[2]}</b><br>Condition present in %{customdata[0]:,} of "
        "%{customdata[1]:,} applications (%{x:.2%})<extra></extra>"
    ),
))
fig_rule_workload.add_trace(go.Bar(
    x=rule_workload["support"],
    y=rule_workload["context_label"],
    orientation="h",
    name="Condition and evidence",
    marker_color="#356A8A",
    text=[
        f"{support:,} / {context:,}"
        for support, context in zip(rule_workload["support_count"], rule_workload["context_n"])
    ],
    textposition="outside",
    customdata=rule_workload[[
        "support_count", "condition_count", "context_n", "confidence", "Business pattern",
    ]].to_numpy(),
    hovertemplate=(
        "<b>%{customdata[4]}</b><br>Condition and evidence occur together in %{customdata[0]:,} applications.<br>"
        "That is %{customdata[3]:.2%} of the %{customdata[1]:,} condition-matching applications and "
        "%{x:.2%} of the %{customdata[2]:,}-application context.<extra></extra>"
    ),
))
fig_rule_workload.update_layout(barmode="group")
fig_rule_workload.update_xaxes(
    title="Share of the rule's stated context",
    tickformat=".0%",
    range=[0, min(1, float(rule_workload["condition_share"].max()) * 1.34)],
)
fig_rule_workload.update_yaxes(
    title="",
    categoryorder="array",
    categoryarray=rule_workload["context_label"].tolist(),
    tickfont=dict(size=11),
)
chart_layout(fig_rule_workload, left=265, bottom=58)

algo_plot = algo_comparison.copy()
algo_plot["label"] = algo_plot["Algoritma"].replace({
    "apriori": "Apriori", "fpgrowth": "FP-Growth", "eclat": "ECLAT",
    "fpgrowth_per_cluster": "Segment FP-Growth",
})
fig_algorithms = px.bar(algo_plot, x="label", y="Rules", color_discrete_sequence=["#64748B"])
fig_algorithms.update_traces(texttemplate="%{y:,}", textposition="outside")
fig_algorithms.update_xaxes(title=""); fig_algorithms.update_yaxes(title="Rules found")
chart_layout(fig_algorithms, legend=False, bottom=70)

# Anomaly figures
_total_eval = int(anomaly_summary.Total_Evaluated)
_targeted_queue = len(anomaly_investigation)
_route_counts = anomaly_investigation["Queue Route"].value_counts()
_consensus_route = int(_route_counts.get("Detector consensus", 0))
_single_axis_route = int(_route_counts.get("Extreme single-axis value", 0))
_dbscan_queue_corroboration = int(
    anomaly_investigation["Sampled Density Corroboration"].eq("Assessed (isolated)").sum()
)

detector_counts = pd.DataFrame({
    "Detector": [
        "Adjusted IQR", "Z-score", "Shrinkage Mahalanobis", "Isolation Forest", "LOF",
        "DBSCAN noise points (30k sample)", "Consensus route", "Single-value route",
    ],
    "Records": [anomaly_summary.N_IQR, anomaly_summary.N_ZSCORE, anomaly_summary.N_MAHALANOBIS,
                anomaly_summary.N_ISOFOREST, anomaly_summary.N_LOF, anomaly_summary.N_DBSCAN_SAMPLE_NOISE,
                _consensus_route, _single_axis_route],
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
    hovertemplate="%{y} x %{x}<br>Jaccard overlap %{z:.2f}<extra></extra>",
))
chart_layout(fig_overlap, left=105, bottom=85)

driver_plot = anomaly_drivers.head(12).sort_values("records")
fig_drivers = px.bar(
    driver_plot, x="records", y="Driver", orientation="h", color="Review Type",
    color_discrete_map=REVIEW_COLORS,
)
fig_drivers.update_traces(texttemplate="%{x:,}", textposition="outside")
fig_drivers.update_xaxes(title="Applications in the targeted review queue"); fig_drivers.update_yaxes(title="")
chart_layout(fig_drivers, left=170)

review_long = anomaly_by_segment.reset_index(names="Segment").melt(
    id_vars="Segment", var_name="Review Type", value_name="Records"
)
fig_review_segment = px.bar(
    review_long, x="Records", y="Segment", color="Review Type", orientation="h",
    color_discrete_map=REVIEW_COLORS,
)
fig_review_segment.update_yaxes(title="", categoryorder="array", categoryarray=SEGMENT_ORDER[::-1])
fig_review_segment.update_xaxes(title="Applications in the targeted review queue")
chart_layout(fig_review_segment, left=120)

# The two scopes follow the mutually exclusive queue-entry routes. Sampled
# DBSCAN is reported separately as corroboration and never changes admission.
SCOPE_LABELS = {
    "Portfolio single-axis extreme": "Single-axis source check",
    "Detector-consensus pattern": "Multi-method pattern review",
}
SCOPE_ORDER = ["Single-axis source check", "Multi-method pattern review"]
SCOPE_COLORS = {
    "Single-axis source check": "#B5534C",
    "Multi-method pattern review": "#356A8A",
}

# Why each kind of unusual is a different credit problem. These are the review
# consequences, not restatements of the detector maths.
SCOPE_MEANING = {
    "Single-axis source check": (
        "One field is at least 10 standard deviations from the portfolio mean.",
        "Check its source, sign, units, and joins before relying on it.",
    ),
    "Multi-method pattern review": (
        "At least three of five portfolio-wide methods agree the record is unusual.",
        "Use the exported values to decide the review type: data check, affordability, or standard.",
    ),
}

scope_series = anomaly_investigation["Anomaly Scope"].map(SCOPE_LABELS)
scope_counts = scope_series.value_counts().reindex(SCOPE_ORDER).fillna(0).astype(int)
scope_share = scope_counts / scope_counts.sum()
scope_frame = pd.DataFrame({
    "Scope": SCOPE_ORDER,
    "Records": scope_counts.to_numpy(),
    "Share": scope_share.to_numpy(),
    "Meaning": [SCOPE_MEANING[s][0] for s in SCOPE_ORDER],
})
fig_scope = px.bar(
    scope_frame.iloc[::-1], x="Records", y="Scope", orientation="h",
    color="Scope", color_discrete_map=SCOPE_COLORS,
    custom_data=["Share", "Meaning"],
)
fig_scope.update_traces(
    texttemplate="%{x:,}", textposition="outside",
    hovertemplate="<b>%{y}</b><br>%{x:,} records (%{customdata[0]:.1%} of the queue)<br><br>%{customdata[1]}<extra></extra>",
)
fig_scope.update_xaxes(title="Applications in the targeted review queue", range=[0, scope_counts.max() * 1.25])
fig_scope.update_yaxes(title="")
chart_layout(fig_scope, legend=False, left=90)

scope_by_segment = (
    pd.crosstab(anomaly_investigation["Segment"], scope_series)
    .reindex(index=SEGMENT_ORDER, columns=SCOPE_ORDER)
    .fillna(0).astype(int)
)
scope_segment_long = scope_by_segment.reset_index().melt(
    id_vars="Segment", var_name="Scope", value_name="Records"
)
scope_segment_long["Segment total"] = scope_segment_long["Segment"].map(scope_by_segment.sum(axis=1))
scope_segment_long["Share of segment queue"] = (
    scope_segment_long["Records"] / scope_segment_long["Segment total"].replace(0, np.nan)
)
fig_scope_segment = px.bar(
    scope_segment_long, x="Records", y="Segment", color="Scope", orientation="h",
    color_discrete_map=SCOPE_COLORS, category_orders={"Scope": SCOPE_ORDER},
    custom_data=["Share of segment queue", "Segment total"],
)
fig_scope_segment.update_traces(
    hovertemplate="<b>%{y}</b><br>%{fullData.name}: %{x:,} records<br>"
                  "%{customdata[0]:.0%} of that segment's queue (%{customdata[1]:,} flagged)<extra></extra>",
)
fig_scope_segment.update_yaxes(title="", categoryorder="array", categoryarray=SEGMENT_ORDER[::-1])
fig_scope_segment.update_xaxes(title="Applications in the targeted review queue")
chart_layout(fig_scope_segment, left=120)

scope_by_review = (
    pd.crosstab(scope_series, anomaly_investigation["Review Type"])
    .reindex(index=SCOPE_ORDER).fillna(0).astype(int)
)
scope_review_long = scope_by_review.reset_index(names="Scope").melt(
    id_vars="Scope", var_name="Review Type", value_name="Records"
)
fig_scope_review = px.bar(
    scope_review_long, x="Records", y="Scope", color="Review Type", orientation="h",
    color_discrete_map=REVIEW_COLORS,
)
fig_scope_review.update_traces(
    hovertemplate="<b>%{y} review pattern</b><br>%{fullData.name}: %{x:,} records<extra></extra>",
)
fig_scope_review.update_yaxes(title="", categoryorder="array", categoryarray=SCOPE_ORDER[::-1])
fig_scope_review.update_xaxes(title="Applications in the targeted review queue")
chart_layout(fig_scope_review, left=90)

# The standard outlier typology. Point outranks the sampled density label
# because a >=10 SD single value needs no context to be anomalous.
TYPOLOGY_LABELS = {
    "Point (globally extreme single value)": "Point",
    "Contextual (unusual multivariate combination)": "Contextual",
    "Collective (sampled sparse-density group)": "Collective",
}
TYPOLOGY_ORDER = ["Point", "Contextual", "Collective"]
TYPOLOGY_COLORS = {"Point": "#B5534C", "Contextual": "#356A8A", "Collective": "#4F7D65"}
TYPOLOGY_MEANING = {
    "Point": "One prepared value is at least 10 standard deviations from the portfolio mean; no context is needed to see it. Check the field's source first.",
    "Contextual": "Every individual value is plausible; only the combination is unusual under multi-method agreement. Read the record evidence to find the conflicting sources.",
    "Collective": "No globally extreme value, but the record sits in a sparse micro-group isolated by the sampled density view. Verify the shared pattern before reviewing members.",
}
typology_series = anomaly_investigation["Outlier Type"].map(TYPOLOGY_LABELS)
anomaly_investigation["Outlier Type Short"] = typology_series
typology_counts = typology_series.value_counts().reindex(TYPOLOGY_ORDER).fillna(0).astype(int)
typology_frame = pd.DataFrame({
    "Outlier type": TYPOLOGY_ORDER,
    "Records": typology_counts.to_numpy(),
    "Share": (typology_counts / typology_counts.sum()).to_numpy(),
    "Meaning": [TYPOLOGY_MEANING[t] for t in TYPOLOGY_ORDER],
})
fig_typology = px.bar(
    typology_frame.iloc[::-1], x="Records", y="Outlier type", orientation="h",
    color="Outlier type", color_discrete_map=TYPOLOGY_COLORS,
    custom_data=["Share", "Meaning"],
)
fig_typology.update_traces(
    texttemplate="%{x:,}", textposition="outside",
    hovertemplate="<b>%{y} outlier</b><br>%{x:,} records (%{customdata[0]:.1%} of the queue)<br><br>%{customdata[1]}<extra></extra>",
)
fig_typology.update_xaxes(
    title="Applications in the targeted review queue",
    range=[0, typology_counts.max() * 1.25],
)
fig_typology.update_yaxes(title="")
chart_layout(fig_typology, legend=False, left=90)


queue_routes = pd.DataFrame({
    "Queue route": ["Detector consensus", "Extreme single-axis value"],
    "Applications": [_consensus_route, _single_axis_route],
})
fig_queue_routes = px.bar(
    queue_routes.sort_values("Applications"),
    x="Applications",
    y="Queue route",
    orientation="h",
    color="Queue route",
    color_discrete_map={
        "Detector consensus": "#356A8A",
        "Extreme single-axis value": "#B98535",
    },
)
fig_queue_routes.update_traces(
    texttemplate="%{x:,}",
    textposition="outside",
    hovertemplate="<b>%{y}</b><br>%{x:,} applications<extra></extra>",
)
fig_queue_routes.update_xaxes(
    title=f"Applications in the {_targeted_queue:,}-file queue",
    range=[0, queue_routes["Applications"].max() * 1.22],
)
fig_queue_routes.update_yaxes(title="")
chart_layout(fig_queue_routes, legend=False, left=165)

consensus_levels = [2, 3, 4]
single_axis_levels = [8.0, 10.0, 12.0]
sensitivity_share = queue_sensitivity.pivot(
    index="consensus_at_least", columns="single_axis_z_cutoff", values="queue_share"
).reindex(index=consensus_levels, columns=single_axis_levels)
sensitivity_total = queue_sensitivity.pivot(
    index="consensus_at_least", columns="single_axis_z_cutoff", values="total_queue"
).reindex(index=consensus_levels, columns=single_axis_levels)
sensitivity_text = np.empty(sensitivity_total.shape, dtype=object)
for row_index, consensus_level in enumerate(consensus_levels):
    for column_index, z_cutoff in enumerate(single_axis_levels):
        selected = consensus_level == 3 and z_cutoff == 10
        sensitivity_text[row_index, column_index] = (
            f"{int(sensitivity_total.iloc[row_index, column_index]):,}<br>"
            f"{sensitivity_share.iloc[row_index, column_index]:.2%}"
            + ("<br><b>Selected</b>" if selected else "")
        )
fig_queue_sensitivity = go.Figure(go.Heatmap(
    z=sensitivity_share.values,
    x=single_axis_levels,
    y=consensus_levels,
    text=sensitivity_text,
    texttemplate="%{text}",
    colorscale=[[0, "#EEF3F5"], [1, "#356A8A"]],
    colorbar=dict(title="Queue share", tickformat=".1%", thickness=14),
    customdata=sensitivity_total.values,
    hovertemplate=(
        "Consensus at least %{y} of 5<br>Single-axis cutoff %{x:.0f} SD<br>"
        "%{customdata:,} applications (%{z:.2%})<extra></extra>"
    ),
))
fig_queue_sensitivity.add_shape(
    type="rect", x0=9, x1=11, y0=2.5, y1=3.5,
    line=dict(color="#B98535", width=3), fillcolor="rgba(0,0,0,0)",
)
fig_queue_sensitivity.update_xaxes(
    title="Single-axis source-check cutoff (standard deviations)",
    tickmode="array", tickvals=single_axis_levels,
)
fig_queue_sensitivity.update_yaxes(
    title="Minimum detector agreement", tickmode="array", tickvals=consensus_levels,
    ticktext=["At least 2 of 5", "At least 3 of 5", "At least 4 of 5"],
)
chart_layout(fig_queue_sensitivity, legend=False, left=105, bottom=62)


def scope_explainer() -> html.Div:
    """One card per scope type: what it is, and why it is a credit problem."""
    return html.Div([
        html.Div([
            html.Div([
                html.Span(scope, className="scope-name"),
                html.Span(f"{scope_counts[scope]:,}", className="scope-count"),
            ], className="scope-card-head"),
            html.P(SCOPE_MEANING[scope][0], className="scope-what"),
            html.P(SCOPE_MEANING[scope][1], className="scope-why"),
        ], className="scope-card", style={"--scope-color": SCOPE_COLORS[scope]})
        for scope in SCOPE_ORDER
    ], className="scope-grid")

anomaly_plot = anomaly_pca.copy()
high = anomaly_plot[anomaly_plot["anomaly_category"].eq("TARGETED_REVIEW")]
other = anomaly_plot[~anomaly_plot.index.isin(high.index)]
other = stratified_sample(other, "anomaly_category", max(1, 12_000 - len(high)))
anomaly_plot = pd.concat([other, high], ignore_index=True)
anomaly_plot["Review status"] = anomaly_plot["anomaly_category"].map({
    "NO_DETECTOR_FLAG": "No detector flag",
    "ONE_DETECTOR_SIGNAL": "One detector flag",
    "TWO_DETECTOR_SIGNAL": "Two detector signals",
    "TARGETED_REVIEW": "Targeted review queue",
})
fig_anomaly_pca = px.scatter(
    anomaly_plot, x="PC1", y="PC2", color="Review status",
    color_discrete_map=SEVERITY_COLORS, opacity=.50, render_mode="webgl",
    category_orders={"Review status": list(SEVERITY_COLORS)},
)
fig_anomaly_pca.update_traces(marker=dict(size=4), hovertemplate="%{fullData.name}<br>PC1 %{x:.2f} - PC2 %{y:.2f}<extra></extra>")
chart_layout(fig_anomaly_pca, bottom=60)


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


rule_table_view = business_rules.copy()
rule_table_view["Context and denominator"] = rule_table_view.apply(
    lambda row: f"{row['Context']}\n{int(row['context_n']):,} applications",
    axis=1,
)
rule_table_view["Observed together"] = rule_table_view.apply(
    lambda row: (
        f"{int(row['support_count']):,} of {int(row['condition_count']):,} condition-matching applications "
        f"({row['confidence']:.1%})"
    ),
    axis=1,
)
rule_table_view["Association compared with context"] = rule_table_view.apply(
    lambda row: (
        f"{row['consequent_baseline']:.1%} baseline to {row['confidence']:.1%} with the condition "
        f"({row['uplift_pp']:+.1f} pp; {row['lift']:.2f}x lift)"
    ),
    axis=1,
)
RULE_TABLE_COLUMNS = [
    "rank", "Business pattern", "Context and denominator", "source_families", "Observed together",
    "Association compared with context", "why_it_matters", "review_action", "caveat",
]
RULE_TABLE_LABELS = {
    "rank": "#",
    "Business pattern": "Business pattern",
    "Context and denominator": "Context and denominator",
    "source_families": "Sources to check together",
    "Observed together": "Observed together",
    "Association compared with context": "Association vs. context",
    "why_it_matters": "Why it matters",
    "review_action": "Reviewer action",
    "caveat": "Use boundary",
}
RULE_TABLE_STYLE = {
    **TABLE_BASE,
    "style_cell": {
        **TABLE_BASE["style_cell"],
        "whiteSpace": "normal",
        "height": "auto",
        "minWidth": "150px",
        "maxWidth": "320px",
        "lineHeight": "1.45",
        "verticalAlign": "top",
    },
}
rules_table = dash_table.DataTable(
    data=rule_table_view[RULE_TABLE_COLUMNS].to_dict("records"),
    columns=[{"name": RULE_TABLE_LABELS[column], "id": column} for column in RULE_TABLE_COLUMNS],
    page_size=6,
    sort_action="native",
    filter_action="native",
    tooltip_data=[
        {column: {"value": str(value), "type": "markdown"} for column, value in row.items()}
        for row in rule_table_view[RULE_TABLE_COLUMNS].to_dict("records")
    ],
    tooltip_duration=None,
    style_cell_conditional=[
        {"if": {"column_id": "rank"}, "minWidth": "44px", "width": "44px", "maxWidth": "44px"},
        {"if": {"column_id": "Business pattern"}, "minWidth": "260px"},
        {"if": {"column_id": "review_action"}, "minWidth": "300px"},
        {"if": {"column_id": "caveat"}, "minWidth": "300px"},
    ],
    **RULE_TABLE_STYLE,
)


ANOMALY_TABLE_COLUMNS = [
    "SK_ID_CURR", "Segment", "Outlier Type Short", "Review Type", "Priority", "Primary Driver",
]
ANOMALY_TABLE_LABELS = {
    "SK_ID_CURR": "Application ID",
    "Segment": "Business segment",
    "Outlier Type Short": "Outlier type",
    "Review Type": "Review type",
    "Priority": "Priority",
    "Primary Driver": "Main reason",
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
            {"if": {"filter_query": '{Review Type} = "Source reconciliation"', "column_id": "Review Type"},
             "backgroundColor": "#FFF3DA", "fontWeight": "700"},
            {"if": {"filter_query": '{Review Type} = "Affordability and repayment review"', "column_id": "Review Type"},
             "backgroundColor": "#FBE9E7", "fontWeight": "700"},
            {"if": {"filter_query": '{Outlier Type Short} = "Point"', "column_id": "Outlier Type Short"},
             "color": "#B5534C", "fontWeight": "700"},
            {"if": {"filter_query": '{Outlier Type Short} = "Contextual"', "column_id": "Outlier Type Short"},
             "color": "#356A8A", "fontWeight": "700"},
            {"if": {"filter_query": '{Outlier Type Short} = "Collective"', "column_id": "Outlier Type Short"},
             "color": "#4F7D65", "fontWeight": "700"},
            {"if": {"state": "active"}, "backgroundColor": "#DCEBF2", "border": "1px solid #356A8A"},
        ],
        **TABLE_BASE,
    )


# The landing page is a synthesis layer. Every chart answers a business
# question by combining compact outputs across phases; none is a raw notebook
# diagnostic.
business_view = cluster_business.merge(
    segment_credit_concentration,
    on=["CLUSTER_KMEANS", "Segment"],
    how="inner",
    validate="one_to_one",
)
business_view["review_count"] = (
    business_view["Segment"].map(anomaly_by_segment.sum(axis=1)).fillna(0).astype(int)
)
business_view["portfolio_share"] = business_view["applicants"] / business_view["applicants"].sum()
business_view["review_share"] = business_view["review_count"] / business_view["review_count"].sum()


# Finding 1: two history-heavy profiles create most of the specialist queue.
FOCUS_SEGMENTS = ["Repayment-Stress History", "Historical Card-Use Intensity"]
focus_view = business_view.loc[business_view["Segment"].isin(FOCUS_SEGMENTS)]
focus_portfolio_share = float(focus_view["portfolio_share"].sum())
focus_review_share = float(focus_view["review_share"].sum())
focus_queue_count = int(focus_view["review_count"].sum())

attention_summary = pd.DataFrame({
    "Denominator": ["All applications", "Targeted review queue"],
    "Focus profiles": [focus_portfolio_share, focus_review_share],
})
attention_summary["Other three profiles"] = 1 - attention_summary["Focus profiles"]
attention_long = attention_summary.melt(
    id_vars="Denominator", var_name="Profile group", value_name="Share"
)
attention_long["Profile group"] = attention_long["Profile group"].replace({
    "Focus profiles": "Repayment-Stress History + Historical Card-Use Intensity",
})
fig_attention_concentration = px.bar(
    attention_long,
    x="Share",
    y="Denominator",
    color="Profile group",
    orientation="h",
    barmode="stack",
    text="Share",
    color_discrete_map={
        "Repayment-Stress History + Historical Card-Use Intensity": "#B98535",
        "Other three profiles": "#CBD5E1",
    },
    category_orders={"Denominator": ["Targeted review queue", "All applications"]},
)
fig_attention_concentration.update_traces(
    texttemplate="%{x:.1%}",
    textposition="inside",
    insidetextanchor="middle",
    hovertemplate="<b>%{y}</b><br>%{fullData.name}: %{x:.2%}<extra></extra>",
)
fig_attention_concentration.update_xaxes(
    title="Share within each denominator", tickformat=".0%", range=[0, 1]
)
fig_attention_concentration.update_yaxes(title="")
chart_layout(fig_attention_concentration, left=165)


# Finding 2: show nominal amount concentration directly instead of asking the
# reader to infer it from a bubble chart.
larger_loan_row = require_one(
    business_view,
    business_view["Segment"].eq("Larger-Loan Affordability"),
    "Larger-Loan Affordability segment",
)
amount_concentration = pd.DataFrame({
    "Measure": [
        "Share of applications",
        "Share of recorded loan amounts",
        "Share of scheduled payment amounts",
    ],
    "Share": [
        larger_loan_row["portfolio_share"],
        larger_loan_row["credit_amount_share"],
        larger_loan_row["annuity_amount_share"],
    ],
    "Scope": [
        f"{int(larger_loan_row['applicants']):,} of {COMBINED_APPLICATIONS:,} applications",
        "This segment's recorded loan amounts over the portfolio total",
        "This segment's scheduled payment amounts over the portfolio total",
    ],
})
amount_concentration["Plot label"] = amount_concentration["Measure"].map({
    "Share of applications": "Applications",
    "Share of recorded loan amounts": "Recorded<br>loan amounts",
    "Share of scheduled payment amounts": "Scheduled<br>payments",
})
fig_amount_concentration = px.bar(
    amount_concentration,
    x="Share",
    y="Plot label",
    orientation="h",
    text="Share",
    custom_data=["Measure", "Scope"],
    color="Measure",
    color_discrete_map={
        "Share of applications": "#CBD5E1",
        "Share of recorded loan amounts": "#356A8A",
        "Share of scheduled payment amounts": "#82A9BB",
    },
)
fig_amount_concentration.update_traces(
    texttemplate="%{x:.1%}",
    textposition="outside",
    cliponaxis=False,
    hovertemplate="<b>%{customdata[0]}</b><br>%{x:.2%}<br>%{customdata[1]}<extra></extra>",
)
fig_amount_concentration.update_xaxes(
    title="Share of the whole portfolio", tickformat=".0%", range=[0, .65]
)
fig_amount_concentration.update_yaxes(title="", categoryorder="array", categoryarray=[
    "Scheduled<br>payments", "Recorded<br>loan amounts", "Applications",
])
chart_layout(fig_amount_concentration, legend=False, left=120)


# 04. Rule-method audit. The business association view is built above directly
# from business_rules_final.csv; this funnel stays in the Rules tab.
fig_rule_screening = go.Figure(go.Funnel(
    y=[wrap_segment_name(stage, width=24) for stage in rule_screening["stage"]],
    x=rule_screening["remaining_rules"],
    textposition="inside",
    texttemplate="%{x:,}",
    marker=dict(color=["#CBD5E1", "#AFCBD7", "#82A9BB", "#5C87A0", "#356A8A"]),
    customdata=rule_screening[["removed_at_stage", "business_reason"]].to_numpy(),
    hovertemplate=(
        "<b>%{y}</b><br>%{x:,} rules remain<br>Removed at this step: %{customdata[0]:,}<br>"
        "%{customdata[1]}<extra></extra>"
    ),
    connector=dict(line=dict(color="#E4E9EC")),
))
chart_layout(fig_rule_screening, legend=False, left=180)


# Finding 3: two corroborating cross-source associations. These are review
# prompts from the portfolio itself; no outcome information exists in them.
prior_lateness_rule = require_one(
    business_rules,
    business_rules["pattern_key"].eq("previous_refusals_repeated | repayment_some_late"),
    "prior-refusal and late-instalment association",
)
bureau_score_rule = require_one(
    business_rules,
    business_rules["pattern_key"].eq("bureau_debt_high | external_score_weak"),
    "bureau-debt and external-score association",
)
# Finding 2 corroboration: high leverage with a clean observed repayment record
# still goes together with a history of earlier approvals, so earlier outcomes
# do not settle whether the present amount is affordable.
leverage_approval_rule = require_one(
    business_rules,
    business_rules["pattern_key"].eq(
        "leverage_over_6x | previous_approval_high | repayment_clean_observed"
    ),
    "leverage, clean-repayment and prior-approval association",
)

# Finding 1 corroboration: the source-profile geometry that separates the two
# specialist segments, read from the standardized business-dimension view.
def dimension_sd(segment: str, dimension: str) -> float:
    match = cluster_comparison.loc[
        cluster_comparison["Segment"].eq(segment)
        & cluster_comparison["business_dimension"].eq(dimension),
        "portfolio_sd",
    ]
    if len(match) != 1:
        raise ValueError(f"Expected one comparison value for {segment} / {dimension}.")
    return float(match.iloc[0])
association_examples = pd.DataFrame([
    {
        "Pattern": "≥3 prior refusals<br>+ late instalments",
        **prior_lateness_rule.to_dict(),
    },
    {
        "Pattern": "Lower-Intensity<br>Credit Footprint:<br>high debt + weak score",
        **bureau_score_rule.to_dict(),
    },
])
fig_converging_evidence = go.Figure()
fig_converging_evidence.add_trace(go.Bar(
    x=association_examples["consequent_baseline"],
    y=association_examples["Pattern"],
    orientation="h",
    name="Context baseline",
    marker_color="#CBD5E1",
    text=[f"{value:.1%}" for value in association_examples["consequent_baseline"]],
    textposition="inside",
    insidetextanchor="middle",
    textfont=dict(color="#203746"),
    customdata=association_examples[["Context", "context_n"]].to_numpy(),
    hovertemplate=(
        "<b>%{y}</b><br>Context baseline: %{x:.2%}<br>"
        "Context: %{customdata[0]} (%{customdata[1]:,} applications)<extra></extra>"
    ),
))
fig_converging_evidence.add_trace(go.Bar(
    x=association_examples["confidence"],
    y=association_examples["Pattern"],
    orientation="h",
    name="Condition present",
    marker_color="#356A8A",
    text=[
        f"{rate:.1%}<br>+{uplift:.1f} pp"
        for rate, uplift in zip(association_examples["confidence"], association_examples["uplift_pp"])
    ],
    textposition="inside",
    insidetextanchor="middle",
    textfont=dict(color="#FFFFFF"),
    customdata=association_examples[[
        "condition_count", "support_count", "source_families", "review_action",
    ]].to_numpy(),
    hovertemplate=(
        "<b>%{y}</b><br>Condition present: %{x:.2%}<br>"
        "%{customdata[1]:,} of %{customdata[0]:,} condition-matching applications<br>"
        "Sources: %{customdata[2]}<br>Review: %{customdata[3]}<extra></extra>"
    ),
))
fig_converging_evidence.update_layout(barmode="group")
fig_converging_evidence.update_xaxes(
    title="Associated-evidence rate", tickformat=".0%", range=[0, .72]
)
fig_converging_evidence.update_yaxes(
    title="",
    categoryorder="array",
    categoryarray=association_examples["Pattern"].tolist()[::-1],
)
chart_layout(fig_converging_evidence, left=112, bottom=58)

rule_count = len(business_rules)


def finding(
    number: str,
    headline: str,
    evidence: str,
    corroboration: str,
    implication: str,
    action: str,
    boundary: str | None = None,
) -> html.Div:
    """Show one decision-ready finding with its evidence chain and response."""

    def fact(label: str, text: str, class_name: str = "") -> html.Div:
        return html.Div([
            html.Span(label, className="finding-fact-label"),
            html.Span(text, className="finding-fact-text"),
        ], className=f"finding-fact {class_name}".strip())

    body = [
        html.Div(headline, className="finding-headline"),
        html.Div([
            fact("Evidence", evidence),
            fact("Corroboration", corroboration),
            fact("Business implication", implication),
            fact("Recommended action", action, "finding-fact-action"),
        ], className="finding-facts"),
    ]
    if boundary:
        body.append(html.Div([
            html.Span("Evidence boundary", className="evidence-label"),
            html.Span(boundary, className="evidence-text"),
        ], className="finding-evidence"))
    return html.Div([
        html.Div(number, className="finding-num"),
        html.Div(body),
    ], className="finding")


def keyfindings_layout() -> html.Section:
    exposure_row = require_one(
        business_view, business_view["Segment"].eq("Larger-Loan Affordability"),
        "Larger-Loan Affordability segment"
    )
    focus_applications = int(focus_view["applicants"].sum())
    stress_delinquency_sd = dimension_sd("Repayment-Stress History", "Observed delinquency")
    card_revolving_sd = dimension_sd("Historical Card-Use Intensity", "Revolving intensity")

    return html.Section([
        heading(
            "KEY FINDINGS",
            "What changes for the credit business",
            "The three findings below have the clearest operational consequence. Each one links the evidence to a specific business response.",
        ),
        finding(
            "01",
            "Two history-heavy profiles account for most of the specialist queue.",
            f"Repayment-Stress History and Historical Card-Use Intensity contain {focus_applications:,} of "
            f"{COMBINED_APPLICATIONS:,} applications ({focus_portfolio_share:.2%}), but contribute {focus_queue_count:,} "
            f"of the {_targeted_queue:,} targeted reviews ({focus_review_share:.2%}).",
            "The source records explain why the work concentrates there. Recorded instalment delays sit "
            f"{stress_delinquency_sd:.2f} standard deviations above the portfolio average in Repayment-Stress History, "
            f"and historical card activity sits {card_revolving_sd:.2f} standard deviations above average in "
            "Historical Card-Use Intensity. The queue concentration follows from the evidence in each profile, not from any outside score.",
            "A small part of the portfolio is likely to absorb most specialist time. It is not one job, however. "
            "Repayment history calls for a timeline review, while historical card use calls for a current facility and balance check.",
            "Create two review paths. For Repayment-Stress History, check recency, severity, cure, disputes, hardship and "
            "current affordability. For Historical Card-Use Intensity, confirm whether the facility is still open, then "
            "verify current balance, limit, arrears and affordability. Start staffing from the observed queue mix and adjust it using handling time and review yield.",
            "Shows where review effort will land, not how any application will perform.",
        ),
        panel(
            f"{focus_portfolio_share:.1%} of applications account for {focus_review_share:.1%} of the targeted review queue",
            graph(fig_attention_concentration, "standard"),
            f"The application denominator is all {COMBINED_APPLICATIONS:,} applications. The queue denominator is the {_targeted_queue:,} exported reviews.",
            wide=True,
        ),

        finding(
            "02",
            "One third of applications carry more than half of the recorded loan amounts.",
            f"Larger-Loan Affordability contains {int(exposure_row['applicants']):,} applications, or "
            f"{exposure_row['portfolio_share']:.2%} of the portfolio, yet it carries "
            f"{exposure_row['credit_amount_share']:.2%} of all recorded loan amounts and "
            f"{exposure_row['annuity_amount_share']:.2%} of all scheduled payment amounts.",
            f"A cross-source pattern sharpens the concern: among applications with a loan above six times income and a "
            f"clean observed repayment record, {leverage_approval_rule['confidence']:.1%} also had at least three quarters "
            f"of their earlier applications approved, against a {leverage_approval_rule['consequent_baseline']:.1%} baseline. "
            "Earlier approvals and clean history therefore accompany exactly the loans where affordability matters most, and neither settles it.",
            "Application volume and amount concentration are different control questions. Where the recorded amounts "
            "concentrate, a weakness in affordability verification touches a disproportionate share of the money the "
            "portfolio has committed, whatever the eventual outcomes turn out to be.",
            "Confirm sustainable income and current obligations, then stress the scheduled payment under the institution's approved lower-income scenario. "
            "Track application volume and amount concentration as separate measures, and keep affordability standards independent of how routine the segment's history looks.",
            "Recorded loan amounts are anonymized contract values, not outstanding balance or loss.",
        ),
        panel(
            f"{exposure_row['portfolio_share']:.1%} of applications carry {exposure_row['credit_amount_share']:.1%} of recorded loan amounts",
            graph(fig_amount_concentration, "standard"),
            f"All three bars share one denominator: the whole {COMBINED_APPLICATIONS:,}-application portfolio.",
            wide=True,
        ),

        finding(
            "03",
            "Prior refusals and late repayment often appear in the same application history.",
            f"Across the portfolio, {int(prior_lateness_rule['support_count']):,} of "
            f"{int(prior_lateness_rule['condition_count']):,} applications with at least three prior refusals also have "
            f"some recorded instalment lateness ({prior_lateness_rule['confidence']:.2%}). The portfolio baseline is "
            f"{prior_lateness_rule['consequent_baseline']:.2%}, a difference of {prior_lateness_rule['uplift_pp']:.2f} percentage points.",
            f"The pattern is supported by a second cross-source check inside Lower-Intensity Credit Footprint: "
            f"{int(bureau_score_rule['support_count']):,} of {int(bureau_score_rule['condition_count']):,} applications "
            f"with bureau debt at least 80% of bureau credit also have weak available external scores "
            f"({bureau_score_rule['confidence']:.2%} versus a {bureau_score_rule['consequent_baseline']:.2%} segment baseline).",
            "Agreement across application history, repayment history, bureau data and external scores makes the review question more precise. "
            "The broad Lower-Intensity profile can still contain a subgroup whose evidence deserves closer reconciliation.",
            "For the first pattern, check refusal reason and date alongside lateness severity, recency, cure and disputes. "
            "For the second, reconcile bureau balance, credit limit and reporting date, then verify which external scores are available and how current they are. "
            "Finish with current affordability; neither pattern should trigger an automatic decline.",
            "Exploratory co-occurrence, not causality.",
        ),
        panel(
            "Two cross-source checks show the same need for evidence reconciliation",
            graph(fig_converging_evidence, "standard"),
            "Grey is the context baseline; blue is the rate when the condition is present.",
            wide=True,
        ),

        html.Div([
            html.Strong("Decision boundary"),
            html.Span(
                "The dashboard supports portfolio strategy, staffing, review design, data-quality controls and monitoring. "
                "It does not approve, decline, price, rank or change a limit for any application. Every finding remains a prompt for a documented human review."),
        ], className="guardrail"),
    ], className="tab-section")


def overview_layout() -> html.Section:
    return html.Section([
        heading("01 - DATA", "Start with the data we actually have",
                "One application portfolio, built from the current application plus five history sources. No outcome label exists anywhere in the analysis."),
        html.Div([
            card(
                "Applications analysed",
                fmt_int(COMBINED_APPLICATIONS),
                "One portfolio; eight source files",
                "blue",
            ),
            card("History sources per applicant", "5", "Bureau, prior applications, instalments, POS or cash loans, card records", "amber"),
            card("Application segments", str(len(SEGMENT_ORDER)), "K-Means clusters, checked against Ward", "green"),
            card("Targeted review queue", fmt_int(_targeted_queue), "Two transparent entry routes", "red"),
        ], className="metric-grid"),
        html.Div([
            panel("Data issues and how we handled them", graph(fig_quality, "standard"),
                  "A missing value can mean something different from a suspicious value, so we handle them separately."),
            panel("Which evidence exists for each segment", graph(fig_evidence_coverage, "standard"),
                  "Share of a segment's applications with that source on file. Coverage decides what a reviewer can check; it is not a risk measure."),
        ], className="two-col"),
        html.Div([
            html.Strong("What this report can do"),
            html.Span("This report describes portfolio patterns. It is not an individual payment-difficulty prediction or credit-decision model."),
        ], className="guardrail"),
    ], className="tab-section")


def segments_layout() -> html.Section:
    ward_text = "Result unavailable"
    if not method_agreement.empty:
        ward_text = f"ARI {method_agreement.adjusted_rand_index.iloc[0]:.3f}"
    return html.Section([
        heading("02 - APPLICATION SEGMENTS", "How the five business segments differ",
                "Broad patterns first, then the actual values behind them."),
        panel("Broad differences between segments", graph(fig_segment_heatmap, "tall", mobile_min_width=650),
              "Each cell is a standardized segment average. Compare across a row; a positive value means above the portfolio average, not better.", wide=True),
        html.H3("Business segment profiles", className="subsection-title"),
        panel(
            "Five business segments, side by side",
            graph(fig_cluster_profiles, "profile", mobile_min_width=760),
            "Each column is one segment. Hover a cell for its value, profile, and suggested review. Colors compare within a row only; blue is higher, amber is lower, neither means safer or riskier.",
            wide=True,
        ),
        html.Div([
            panel("Segment size", graph(fig_sizes, "standard", mobile_min_width=520)),
            panel("Choosing the number of clusters", graph(fig_k_selection, "standard"),
                  f"K=5 is the elbow and the most seed-stable choice (mean ARI {stability_by_k.loc[5]:.3f}); higher K reaches similar or better silhouette but is far less stable. Full comparison in REPORT.md."),
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
        panel(
            "Ward, complete and average linkage on the same sample",
            html.Div(
                html.Img(
                    src=LINKAGE_COMPARISON_SRC,
                    className="evidence-image",
                    alt="Three sampled hierarchical dendrograms comparing Ward, complete and average linkage.",
                ),
                className="evidence-image-scroll",
            ),
            "A 2,000-application sample. Different merge shapes show that hierarchical structure depends on linkage choice; Ward is a sensitivity check, not the one true hierarchy.",
            wide=True,
        ),
        html.Div([
            panel("K-Means on the first two principal components", graph(fig_kmeans, "map"),
                  "A stratified sample of 8,000 applications. These two axes are for display. The clustering model used 10 components."),
            panel("DBSCAN density view", graph(fig_dbscan, "map"),
                  f"A {int(anomaly_summary.N_DBSCAN_SAMPLE_COVERED):,}-application sample. Noise points are a density signal, not a fraud or anomaly label."),
        ], className="two-col"),
    ], className="tab-section")


def rules_layout() -> html.Section:
    return html.Section([
        heading(
            "03 - ASSOCIATION RULES",
            "Which evidence should be checked together",
            f"The {rule_count} shortlisted patterns compare applications that match a condition with the same "
            "portfolio or segment context. They are review prompts, not predictions or lending rules.",
        ),
        panel(
            "How the associated evidence changes when a condition is present",
            graph(fig_signal_agreement, "rules", mobile_min_width=900),
            "Grey is the context baseline; blue is the rate when the condition is present. Hover for full detail.",
            wide=True,
        ),
        panel(
            "How much review work each pattern can generate",
            graph(fig_rule_workload, "rules", mobile_min_width=700),
            "Pale: applications matching the condition. Blue: applications matching condition and evidence. Patterns overlap, so bars must not be added.",
            wide=True,
        ),
        panel(
            "What each pattern means for a reviewer",
            html.Div(rules_table, className="table-shell"),
            "Filter by source, context, or phrase. No pattern is an automatic reason to change a credit decision.",
            wide=True,
        ),
        html.Div([
            panel(
                "How candidate rules were screened",
                graph(fig_rule_screening, "standard", mobile_min_width=560),
                "Removes arithmetic identities and schema-induced relationships. Shortlisting sets presentation volume; it does not make a pattern causal.",
            ),
            panel(
                "Method check",
                graph(fig_algorithms, "standard", mobile_min_width=520),
                "Apriori, FP-Growth, and ECLAT check the same portfolio-wide search. Segment FP-Growth uses a different denominator.",
            ),
        ], className="two-col"),
    ], className="tab-section")


def anomalies_layout() -> html.Section:
    counts = anomaly_investigation["Review Type"].value_counts()
    stress_consensus = int((
        anomaly_investigation["Segment"].eq("Repayment-Stress History")
        & anomaly_investigation["Anomaly Scope"].eq("Detector-consensus pattern")
    ).sum())
    consensus_total = int(
        anomaly_investigation["Anomaly Scope"].eq("Detector-consensus pattern").sum()
    )
    data_checks = int(counts.get("Source reconciliation", 0))
    return html.Section([
        heading("04 - RECORDS TO REVIEW", "One queue, two entry routes, different work",
                "Detector agreement finds unusual combinations; a separate route catches one extreme value. Neither is a credit decision."),
        html.Div([
            card("Targeted review queue", fmt_int(_targeted_queue), f"{_targeted_queue / _total_eval:.2%} of the portfolio", "red"),
            card("Detector consensus", fmt_int(_consensus_route), "Three or more methods agree", "blue"),
            card("Extreme single-axis value", fmt_int(_single_axis_route), "At least 10 SD; verify the source", "amber"),
            card("Source reconciliation", fmt_int(data_checks), "Potential inconsistency; verify first", "green"),
        ], className="metric-grid"),
        html.Div([
            panel("How records enter the queue", graph(fig_queue_routes, "standard", mobile_min_width=520),
                  f"Consensus and the extreme single-axis check are separate controls; their counts sum to {_targeted_queue:,}."),
            panel("Method flags and queue routes", graph(fig_detectors, "standard"),
                  f"Five detectors cover all {COMBINED_APPLICATIONS:,} applications; DBSCAN corroborates {_dbscan_queue_corroboration:,} queued records but never votes. Counts overlap, do not add them."),
        ], className="two-col"),
        panel(
            "Review workload changes materially when the two operating cutoffs move",
            graph(fig_queue_sensitivity, "standard", mobile_min_width=560),
            "The selected 3-of-5 and 10-SD cell is a project operating point, not an industry standard.",
            wide=True,
        ),
        panel("Where methods agree", graph(fig_overlap, "standard", mobile_min_width=560),
              "Jaccard overlap between two methods' flagged records. DBSCAN uses only its "
              f"{int(anomaly_summary.N_DBSCAN_SAMPLE_COVERED):,}-application sample, so its overlaps are not directly comparable.", wide=True),
        html.Div("Why each file entered the queue", className="subsection-title"),
        scope_explainer(),
        html.Div([
            panel("How the queue splits by kind", graph(fig_scope, "standard", mobile_min_width=500),
                  "Sampled DBSCAN appears only as separate corroboration, never as a queue route."),
            panel("Kind of unusual by cluster", graph(fig_scope_segment, "standard", mobile_min_width=540),
                  f"Repayment-Stress History holds {stress_consensus:,} of {consensus_total:,} multi-method reviews, a workload result, not a prediction."),
        ], className="two-col"),
        panel("Kind of unusual against the type of review it triggers", graph(fig_scope_review, "compact", mobile_min_width=540),
              f"The {data_checks:,} source-reconciliation cases are none confirmed until the source is checked.", wide=True),
        panel("Point, contextual, and collective records need different first steps", graph(fig_typology, "compact", mobile_min_width=520),
              "Point: one extreme value, check its source first. Contextual: plausible alone, unusual in combination. Collective: isolated in the sampled density view (a lower bound, not a total).", wide=True),
        html.Div([
            panel("What reviewers should examine", graph(fig_drivers, "tall", mobile_min_width=580),
                  "A record can carry several triggers; bars overlap and must not be added."),
            panel("Review queue by cluster", graph(fig_review_segment, "tall", mobile_min_width=540)),
        ], className="two-col"),
        panel("Where flagged records sit", graph(fig_anomaly_pca, "map"),
              "The full targeted queue is shown; other records are sampled for responsiveness.", wide=True),
        panel("Applications to review", html.Div([
            html.P("Select a row to see its evidence and next step.", className="table-instruction"),
            html.Div(anomaly_table_component(), className="table-shell"),
            html.Div("Select an application to see its evidence.", id="anomaly-detail", className="record-detail"),
        ]), f"All {_targeted_queue:,} targeted reviews are available, ten rows at a time.", wide=True),
    ], className="tab-section")


SECTION_BUILDERS = {
    "keyfindings": keyfindings_layout,
    "overview": overview_layout,
    "segments": segments_layout,
    "rules": rules_layout,
    "anomalies": anomalies_layout,
}

# Rail order. Key findings leads because it carries the conclusions; the phase
# sections behind it are the evidence. The number is a quiet step marker.
SECTIONS = [
    ("keyfindings", "Key findings", ""),
    ("overview", "Data", "01"),
    ("segments", "Segments", "02"),
    ("rules", "Rules", "03"),
    ("anomalies", "Anomalies", "04"),
]


app = Dash(
    __name__,
    title="Home Credit Portfolio Analysis",
    assets_folder=str(ROOT / "dashboard/assets"),
    suppress_callback_exceptions=True,
)
server = app.server

app.layout = html.Div([
    html.Aside([
        html.Div([
            html.Div("Home Credit", className="rail-brand-name"),
            html.Div("Portfolio discovery", className="rail-brand-sub"),
        ], className="rail-brand"),
        html.Nav([
            html.Button(
                [html.Span(num, className="rail-num"), html.Span(label, className="rail-label")],
                id={"type": "rail-link", "section": key},
                className="rail-link",
                n_clicks=0,
            )
            for key, label, num in SECTIONS
        ], className="rail-nav"),
        html.Div([
            html.Div([html.Span(f"{COMBINED_APPLICATIONS:,}"), html.Span("applications")], className="rail-stat"),
            html.Div([html.Span(str(len(SEGMENT_ORDER))), html.Span("business segments")], className="rail-stat"),
            html.Div([html.Span(f"{_targeted_queue:,}"), html.Span("targeted reviews")], className="rail-stat"),
        ], className="rail-meta"),
    ], className="rail"),
    html.Div([
        html.Main(id="section-content", className="section-content"),
        html.Footer([
            html.Span("Methods and reasoning: REPORT.md"),
            html.Span("Charts read the artefacts written by the project notebooks"),
        ]),
    ], className="canvas"),
    dcc.Store(id="section-scroll-signal"),
], className="app-shell")


@app.callback(
    Output("section-content", "children"),
    Output({"type": "rail-link", "section": ALL}, "className"),
    Input({"type": "rail-link", "section": ALL}, "n_clicks"),
)
def render_section(_clicks):
    triggered = ctx.triggered_id
    active = triggered["section"] if isinstance(triggered, dict) else "keyfindings"
    # Derive order from the resolved output ids; ALL sorts by id, not by SECTIONS.
    order = [item["id"]["section"] for item in ctx.outputs_list[1]]
    classes = ["rail-link active" if key == active else "rail-link" for key in order]
    return SECTION_BUILDERS.get(active, keyfindings_layout)(), classes


app.clientside_callback(
    """
    function(_clicks) {
        window.requestAnimationFrame(function() {
            const canvas = document.querySelector('.canvas');
            if (canvas) { canvas.scrollTop = 0; }
            window.scrollTo({top: 0, behavior: 'auto'});
        });
        return Date.now();
    }
    """,
    Output("section-scroll-signal", "data"),
    Input({"type": "rail-link", "section": ALL}, "n_clicks"),
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
    Input("anomaly-table", "data"),
    prevent_initial_call=True,
)
def show_anomaly_detail(active_cell, page_data):
    if not active_cell or not page_data:
        return "Select an application to see its evidence."
    row_index = int(active_cell.get("row", -1))
    if row_index < 0 or row_index >= len(page_data):
        return "Select an application to see its evidence."
    record_id = page_data[row_index]["SK_ID_CURR"]
    matches = anomaly_investigation.loc[anomaly_investigation.SK_ID_CURR.eq(record_id)]
    if len(matches) != 1:
        return "This application is no longer available in the current review data."
    row = matches.iloc[0]
    density_status = str(row["Sampled Density Corroboration"])
    density_short = {
        "Not assessed": "outside the DBSCAN sample",
        "Assessed (not isolated)": "in the DBSCAN sample, not isolated",
        "Assessed (isolated)": "in the DBSCAN sample, isolated (corroboration only)",
    }.get(density_status, "sample status unavailable")
    return html.Div([
        html.Div([
            html.Span(f"Application {int(row.SK_ID_CURR):,}", className="record-id"),
            html.Span(row["Priority"], className="record-priority"),
        ], className="record-head"),
        html.Div([
            html.Strong("Outlier type: "), html.Span(row["Outlier Type Short"]),
            html.Span("  |  "),
            html.Strong("Entered via: "), html.Span(row["Queue Route"]),
            html.Span("  |  "),
            html.Strong("DBSCAN: "), html.Span(density_short),
        ], className="record-meta"),
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

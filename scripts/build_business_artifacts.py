"""Build compact, auditable summaries used by the business dashboard.

Run this after Phases 1-4.  The script does not fit a model.  It joins the
phase outputs by ``SK_ID_CURR`` and turns them into small tables whose
denominators and meanings are explicit.
"""

from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.domain_credit import DENSITY_STATES, build_anomaly_investigation

DATA = ROOT / "datasets"
P2 = ROOT / "results" / "phase2_clustering"
P3 = ROOT / "results" / "phase3_association"
P4 = ROOT / "results" / "phase4_anomaly"

BUSINESS_RULE_THEMES = {
    "adverse_convergence",
    "supportive_convergence",
    "mixed_evidence_reconcile",
}
BUSINESS_RULE_THEME_LABELS = {
    "Concern signals converge",
    "Lower-concern evidence agrees",
    "Evidence conflict to reconcile",
}
REQUIRED_RULE_SCREEN_REASONS = {
    "algebraic_financial_identity",
    "nested_previous_count_definition",
    "same_bureau_derived_family",
    "same_source_missingness_identity",
    "schema_induced_missingness_identity",
    "accepted_cross_source",
}
CANONICAL_SEGMENTS = {
    "Lower-Intensity Credit Footprint",
    "Repayment-Stress History",
    "History-Rich Credit User",
    "Larger-Loan Affordability",
    "Historical Card-Use Intensity",
    "Portfolio-wide",
}
STALE_SEGMENT_LABELS = {
    "thin-file / low-intensity",
    "high-exposure / established",
    "high-exposure applicant",
    "card-active revolvers",
    "intensive card user",
}
STRUCTURAL_RULE_TOKENS = {
    "previous_none",
    "previous_one",
    "previous_two_to_four",
    "previous_deep",
    "previous_outcome_not_observed",
    "repayment_not_observed",
    "card_history_not_observed",
    "credit_file_none",
    "bureau_debt_not_observed",
    "external_score_unavailable",
}


def require_columns(frame: pd.DataFrame, required: set[str], artifact: str) -> None:
    """Raise a readable error when a Phase 3 export has drifted."""
    missing = required.difference(frame.columns)
    if missing:
        raise ValueError(f"{artifact} is missing columns: {sorted(missing)}")


def integer_values(series: pd.Series, field: str) -> pd.Series:
    """Return integer-valued CSV data without silently rounding it."""
    numeric = pd.to_numeric(series, errors="coerce")
    if numeric.isna().any() or not numeric.eq(numeric.round()).all():
        raise ValueError(f"{field} must contain whole numbers without missing values.")
    return numeric.astype("int64")


def boolean_value(value: object, field: str) -> bool:
    """Parse one Boolean-like CSV value without treating a string as truthy."""
    if isinstance(value, bool):
        return value
    normalized = str(value).strip().lower()
    if normalized in {"true", "1"}:
        return True
    if normalized in {"false", "0"}:
        return False
    raise ValueError(f"{field} must be true or false, not {value!r}.")


def validate_phase3_business_rules(
    rules: pd.DataFrame,
    status: pd.DataFrame,
    rejection: pd.DataFrame,
    business_screen: pd.DataFrame,
) -> dict[str, int]:
    """Check that the Phase 3 shortlist contains defensible business signals."""
    require_columns(rejection, {"reason", "rules"}, "rule_rejection_audit.csv")
    require_columns(business_screen, {"reason", "rules"}, "rule_business_screen_audit.csv")
    require_columns(
        status,
        {
            "business_signal_candidates",
            "unique_business_patterns",
            "selected_unique_patterns",
            "assignment_minimum",
            "meets_assignment_minimum",
            "selection_note",
        },
        "rule_shortlist_status.csv",
    )
    require_columns(
        rules,
        {
            "rank",
            "pattern_key",
            "rule_str",
            "short_rule",
            "business_rule",
            "Segment",
            "Context",
            "context_n",
            "condition_count",
            "support_count",
            "support",
            "consequent_baseline",
            "confidence",
            "uplift_pp",
            "lift",
            "business_theme",
            "source_families",
            "why_it_matters",
            "review_action",
            "caveat",
            "metric_scope",
        },
        "business_rules_final.csv",
    )

    if rejection["reason"].duplicated().any() or business_screen["reason"].duplicated().any():
        raise ValueError("Phase 3 audit reasons must be unique.")
    rejection = rejection.copy()
    business_screen = business_screen.copy()
    rejection["rules"] = integer_values(rejection["rules"], "rule_rejection_audit.rules")
    business_screen["rules"] = integer_values(
        business_screen["rules"], "rule_business_screen_audit.rules"
    )
    if rejection["rules"].lt(0).any() or business_screen["rules"].lt(0).any():
        raise ValueError("Phase 3 audit counts cannot be negative.")
    if rejection["reason"].eq("accepted_nontrivial").any():
        raise ValueError("The legacy accepted_nontrivial screen must not be reused.")
    missing_reasons = REQUIRED_RULE_SCREEN_REASONS.difference(rejection["reason"])
    if missing_reasons:
        raise ValueError(f"The first rule screen is missing audit reasons: {sorted(missing_reasons)}")

    rejection_counts = rejection.set_index("reason")["rules"]
    candidate_rules = int(rejection_counts.sum())
    accepted_cross_source = int(rejection_counts.get("accepted_cross_source", 0))
    if not 0 < accepted_cross_source < candidate_rules:
        raise ValueError("The first rule screen must retain a non-empty cross-source subset.")
    if int(business_screen["rules"].sum()) != accepted_cross_source:
        raise ValueError(
            "The business-screen audit must account for every cross-source rule from the first screen."
        )

    if len(status) != 1:
        raise ValueError("rule_shortlist_status.csv must contain exactly one status row.")
    status_row = status.iloc[0]
    status_counts = {
        field: int(integer_values(pd.Series([status_row[field]]), f"status.{field}").iloc[0])
        for field in [
            "business_signal_candidates",
            "unique_business_patterns",
            "selected_unique_patterns",
            "assignment_minimum",
        ]
    }
    business_signal_candidates = int(
        business_screen.loc[business_screen["reason"].isin(BUSINESS_RULE_THEMES), "rules"].sum()
    )
    if status_counts["business_signal_candidates"] != business_signal_candidates:
        raise ValueError("The shortlist status does not match the accepted business-screen themes.")
    if not (
        business_signal_candidates
        >= status_counts["unique_business_patterns"]
        >= status_counts["selected_unique_patterns"]
    ):
        raise ValueError("Phase 3 shortlist counts must narrow at each selection step.")
    if status_counts["assignment_minimum"] != 10:
        raise ValueError("The documented assignment minimum must remain 10 defensible rules.")
    if not boolean_value(status_row["meets_assignment_minimum"], "meets_assignment_minimum"):
        raise ValueError("The Phase 3 shortlist does not meet the documented assignment minimum.")
    if not str(status_row["selection_note"]).strip():
        raise ValueError("The Phase 3 shortlist needs a selection note.")

    selected_rules = status_counts["selected_unique_patterns"]
    if not 10 <= selected_rules <= 12 or len(rules) != selected_rules:
        raise ValueError("Phase 3 must export 10 to 12 selected business rules.")
    if rules["pattern_key"].duplicated().any() or rules["rule_str"].duplicated().any():
        raise ValueError("Selected business rules must be unique patterns.")

    ranks = integer_values(rules["rank"], "business_rules_final.rank")
    if ranks.tolist() != list(range(1, len(rules) + 1)):
        raise ValueError("Business-rule ranks must be consecutive and start at 1.")
    numeric_counts = {
        field: integer_values(rules[field], f"business_rules_final.{field}")
        for field in ["context_n", "condition_count", "support_count"]
    }
    context_n = numeric_counts["context_n"]
    condition_count = numeric_counts["condition_count"]
    support_count = numeric_counts["support_count"]
    if (
        support_count.le(0).any()
        or condition_count.lt(support_count).any()
        or context_n.lt(condition_count).any()
    ):
        raise ValueError("Rule counts must satisfy 0 < support <= condition <= context.")

    numeric = {
        field: pd.to_numeric(rules[field], errors="coerce")
        for field in ["support", "consequent_baseline", "confidence", "uplift_pp", "lift"]
    }
    if any(values.isna().any() for values in numeric.values()):
        raise ValueError("Business-rule metrics cannot be missing or non-numeric.")
    if (
        not numeric["support"].between(0, 1, inclusive="both").all()
        or not numeric["confidence"].between(0, 1, inclusive="both").all()
        or not numeric["consequent_baseline"].between(0, 1, inclusive="both").all()
        or not numeric["lift"].ge(1.20).all()
    ):
        raise ValueError("Business-rule support, confidence, baseline, or lift is outside its valid range.")

    expected_metrics = {
        "support": support_count / context_n,
        "confidence": support_count / condition_count,
        "consequent_baseline": numeric["confidence"] / numeric["lift"],
        "uplift_pp": 100 * (numeric["confidence"] - numeric["consequent_baseline"]),
    }
    for field, expected in expected_metrics.items():
        if numeric[field].sub(expected).abs().max() > 1e-9:
            raise ValueError(f"Business-rule {field} does not match its counts or related metrics.")

    required_text = [
        "pattern_key",
        "rule_str",
        "short_rule",
        "business_rule",
        "Segment",
        "Context",
        "business_theme",
        "source_families",
        "why_it_matters",
        "review_action",
        "caveat",
        "metric_scope",
    ]
    for field in required_text:
        if rules[field].fillna("").astype(str).str.strip().eq("").any():
            raise ValueError(f"Every selected rule needs a non-empty {field}.")
    if not set(rules["business_theme"]).issubset(BUSINESS_RULE_THEME_LABELS):
        raise ValueError("Selected rules contain an unknown business interpretation theme.")
    if not set(rules["Segment"]).issubset(CANONICAL_SEGMENTS) or not set(
        rules["Context"]
    ).issubset(CANONICAL_SEGMENTS):
        raise ValueError("Business rules contain an unknown or stale segment name.")

    text_columns = [
        column for column in rules.columns
        if pd.api.types.is_object_dtype(rules[column].dtype)
        or pd.api.types.is_string_dtype(rules[column].dtype)
    ]
    all_rule_text = "\n".join(
        rules[text_columns].fillna("").astype(str).to_numpy().ravel()
    ).lower()
    stale_labels = sorted(label for label in STALE_SEGMENT_LABELS if label in all_rule_text)
    stale_tokens = sorted(token for token in STRUCTURAL_RULE_TOKENS if token in all_rule_text)
    if stale_labels:
        raise ValueError(f"Business rules contain stale segment labels: {stale_labels}")
    if "cluster_" in all_rule_text or stale_tokens or "not_observed" in all_rule_text:
        raise ValueError(
            "Selected business rules must not restate cluster membership, history depth, or missingness."
        )

    source_counts = rules["source_families"].map(
        lambda value: len({part.strip() for part in str(value).split(";") if part.strip()})
    )
    if source_counts.lt(2).any() or rules["source_families"].str.contains(
        "unknown", case=False, na=False
    ).any():
        raise ValueError("Every selected rule must connect at least two known evidence sources.")

    return {
        "candidate_rules": candidate_rules,
        "accepted_cross_source": accepted_cross_source,
        "business_signal_candidates": business_signal_candidates,
        "unique_business_patterns": status_counts["unique_business_patterns"],
        "selected_rules": selected_rules,
    }


def nullable_boolean_series(series: pd.Series, field: str) -> pd.Series:
    """Normalize a nullable Boolean column read from CSV without filling gaps."""
    def parse(value: object) -> object:
        if pd.isna(value):
            return pd.NA
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            normalized = value.strip().lower()
            if normalized in {"true", "1"}:
                return True
            if normalized in {"false", "0"}:
                return False
        else:
            try:
                numeric = float(value)
            except (TypeError, ValueError):
                numeric = float("nan")
            if numeric in {0.0, 1.0}:
                return bool(numeric)
        raise ValueError(f"{field} contains an invalid Boolean value: {value!r}")

    return series.map(parse).astype("boolean")


def density_states(frame: pd.DataFrame) -> pd.Series:
    """Map DBSCAN coverage and noise without treating unsampled rows as negative."""
    required = {"dbscan_sample_covered", "dbscan_sample_noise"}
    missing = required.difference(frame.columns)
    if missing:
        raise ValueError(f"Missing sampled-density fields: {sorted(missing)}")
    covered = nullable_boolean_series(frame["dbscan_sample_covered"], "dbscan_sample_covered")
    noise = nullable_boolean_series(frame["dbscan_sample_noise"], "dbscan_sample_noise")
    if covered.isna().any():
        raise ValueError("dbscan_sample_covered must be present for every portfolio row.")
    if noise.loc[covered].isna().any():
        raise ValueError("Covered DBSCAN sample rows must have an isolation result.")
    if noise.loc[~covered].notna().any():
        raise ValueError("Rows outside the DBSCAN sample must not have an isolation result.")

    states = pd.Series("Not assessed", index=frame.index, dtype="object")
    isolated = covered & noise.fillna(False)
    assessed_not_isolated = covered & ~noise.fillna(False)
    states.loc[isolated] = "Assessed (isolated)"
    states.loc[assessed_not_isolated] = "Assessed (not isolated)"
    return states




def named_labels() -> pd.DataFrame:
    labels = pd.read_csv(
        DATA / "final" / "cluster_labels.csv",
        usecols=["SK_ID_CURR", "CLUSTER_KMEANS"],
    )
    names = pd.read_csv(P2 / "cluster_names.csv", usecols=["cluster_id", "segment_name"])
    labels = labels.merge(
        names,
        left_on="CLUSTER_KMEANS",
        right_on="cluster_id",
        how="left",
        validate="many_to_one",
    ).rename(columns={"segment_name": "Segment"})
    if labels["Segment"].isna().any():
        raise ValueError("At least one cluster label has no business segment name.")
    return labels[["SK_ID_CURR", "CLUSTER_KMEANS", "Segment"]]


def build_evidence_coverage(labels: pd.DataFrame) -> pd.DataFrame:
    columns = [
        "SK_ID_CURR",
        "FLAG_NO_BUREAU",
        "PREV_COUNT",
        "INST_COUNT",
        "CC_MONTHS_COUNT",
        "SOURCE_EXT_SOURCE_1",
        "SOURCE_EXT_SOURCE_2",
        "SOURCE_EXT_SOURCE_3",
    ]
    features = pd.read_csv(DATA / "final" / "features_business.csv", usecols=columns)
    data = features.merge(labels, on="SK_ID_CURR", how="inner", validate="one_to_one")
    if len(data) != len(labels):
        raise ValueError("Evidence coverage did not match every combined application ID.")

    observed = pd.DataFrame({
        "Bureau history": data["FLAG_NO_BUREAU"].fillna(1).eq(0),
        "Previous applications": data["PREV_COUNT"].fillna(0).gt(0),
        "Instalment history": data["INST_COUNT"].fillna(0).gt(0),
        "Previous Home Credit card history": data["CC_MONTHS_COUNT"].fillna(0).gt(0),
        "At least one external score": data[[
            "SOURCE_EXT_SOURCE_1", "SOURCE_EXT_SOURCE_2", "SOURCE_EXT_SOURCE_3"
        ]].notna().any(axis=1),
    })
    observed.insert(0, "Segment", data["Segment"])
    long = observed.melt(
        id_vars="Segment", var_name="Evidence source", value_name="Observed"
    )
    summary = (
        long.groupby(["Segment", "Evidence source"], as_index=False)
        .agg(observed_applications=("Observed", "sum"), applications=("Observed", "size"))
    )
    summary["coverage"] = summary["observed_applications"] / summary["applications"]
    summary["population"] = "All applications in the portfolio"
    summary.to_csv(P2 / "segment_evidence_coverage.csv", index=False)
    return summary


def build_segment_full_profiles(labels: pd.DataFrame) -> pd.DataFrame:
    """Write the full per-segment profile used by report Appendix A.

    One row per population and business field: mean and standard deviation on
    the readable business scale, plus the modal value for low-cardinality
    fields. The DBSCAN noise population is profiled as its own group against
    the whole portfolio, because Phase 2 now runs DBSCAN on all 356,255
    applications in the distance-preserving space. An earlier version read the
    30,000-row UMAP sample here, which profiled 519 records and described them
    as if they were the portfolio's isolated applications.
    """
    features = pd.read_csv(DATA / "final" / "features_business.csv")
    data = features.merge(labels, on="SK_ID_CURR", how="inner", validate="one_to_one")
    if len(data) != len(labels):
        raise ValueError("Full profiles did not match every combined application ID.")

    # anomaly_combined.csv is keyed by ROW_ID, so the applicant identifier comes
    # back through the label file rather than being assumed to align by position.
    density = pd.read_csv(
        P4 / "anomaly_combined.csv",
        usecols=["ROW_ID", "dbscan_sample_covered", "dbscan_sample_noise"],
    ).merge(
        pd.read_csv(
            DATA / "final" / "cluster_labels.csv", usecols=["ROW_ID", "SK_ID_CURR"]
        ),
        on="ROW_ID",
        how="inner",
        validate="one_to_one",
    )
    covered = nullable_boolean_series(
        density["dbscan_sample_covered"], "dbscan_sample_covered"
    )
    if not covered.fillna(False).all():
        raise ValueError(
            "The density view must cover every application before Appendix A profiles "
            "its noise population; a sampled denominator has come back."
        )
    noise_flags = nullable_boolean_series(
        density["dbscan_sample_noise"], "dbscan_sample_noise"
    ).fillna(False)
    noise_ids = set(density.loc[noise_flags, "SK_ID_CURR"].astype(int))

    mining_columns = set(
        pd.read_csv(DATA / "final" / "features_clustering.csv", nrows=0).columns
    )
    feature_columns = [
        column for column in features.columns if column not in {"ROW_ID", "SK_ID_CURR"}
    ]

    populations: list[tuple[str, pd.DataFrame, int, str]] = [
        (segment, data.loc[data["Segment"].eq(segment)], len(data),
         "All applications in the portfolio")
        for segment in sorted(data["Segment"].unique())
    ]
    populations.append((
        "DBSCAN density noise",
        data.loc[data["SK_ID_CURR"].isin(noise_ids)],
        len(density),
        "All 356,255 applications, 10-component distance-preserving space; noise is "
        "a density state, not an anomaly label, and never votes in the review queue",
    ))

    rows = []
    for name, group, base, base_note in populations:
        for column in feature_columns:
            values = pd.to_numeric(group[column], errors="coerce")
            distinct = values.nunique(dropna=True)
            mode_value = mode_share = None
            if 0 < distinct <= 20:
                counts = values.value_counts()
                mode_value = float(counts.index[0])
                mode_share = float(counts.iloc[0] / values.notna().sum())
            rows.append({
                "population": name,
                "applications": len(group),
                "population_base": base,
                "share_of_base": len(group) / base,
                "feature": column,
                "mean": float(values.mean()),
                "std": float(values.std()),
                "mode": mode_value,
                "mode_share": mode_share,
                "in_mining_matrix": column in mining_columns,
                "base_note": base_note,
            })

    profiles = pd.DataFrame(rows)
    profiles.to_csv(P2 / "segment_full_profiles.csv", index=False)
    return profiles


def build_credit_concentration_summary(labels: pd.DataFrame) -> pd.DataFrame:
    """Summarize where the recorded loan amounts sit, segment by segment.

    Every figure uses the whole application portfolio as its denominator.
    No outcome label exists anywhere in this summary: the point is that the
    amount a segment carries and the number of applications it contains are
    two different control questions, and both are visible without any label.
    """
    features = pd.read_csv(
        DATA / "final" / "features_business.csv",
        usecols=[
            "SK_ID_CURR", "AMT_CREDIT", "AMT_ANNUITY",
            "CREDIT_TO_INCOME", "ANNUITY_TO_INCOME",
        ],
    )
    data = features.merge(labels, on="SK_ID_CURR", how="inner", validate="one_to_one")
    if len(data) != len(labels):
        raise ValueError("Credit concentration summary did not match every application ID.")
    summary = (
        data.groupby(["CLUSTER_KMEANS", "Segment"], as_index=False)
        .agg(
            applications=("SK_ID_CURR", "size"),
            credit_amount_total=("AMT_CREDIT", "sum"),
            annuity_amount_total=("AMT_ANNUITY", "sum"),
            median_credit_to_income=("CREDIT_TO_INCOME", "median"),
            median_annuity_to_income=("ANNUITY_TO_INCOME", "median"),
        )
    )
    summary["application_share"] = summary["applications"] / summary["applications"].sum()
    summary["credit_amount_share"] = (
        summary["credit_amount_total"] / summary["credit_amount_total"].sum()
    )
    summary["annuity_amount_share"] = (
        summary["annuity_amount_total"] / summary["annuity_amount_total"].sum()
    )
    summary["population"] = "All applications; no outcome label exists in this summary"
    summary["amount_caveat"] = (
        "Amounts are recorded loan and scheduled-payment values in anonymized units, "
        "not outstanding balance, exposure, or loss"
    )
    summary.to_csv(P4 / "segment_credit_concentration.csv", index=False)
    return summary


def build_rule_summaries() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Build the screening funnel and validate the selected Phase 3 rules."""
    rejection = pd.read_csv(P3 / "rule_rejection_audit.csv")
    business_screen = pd.read_csv(P3 / "rule_business_screen_audit.csv")
    status = pd.read_csv(P3 / "rule_shortlist_status.csv")
    rules = pd.read_csv(P3 / "business_rules_final.csv")
    counts = validate_phase3_business_rules(rules, status, rejection, business_screen)

    stages = [
        (
            "Candidate rules tested",
            counts["candidate_rules"],
            "All mined rules before identity and evidence-source screening",
        ),
        (
            "Cross-source patterns",
            counts["accepted_cross_source"],
            "Retained compact patterns that connect separate evidence sources and include behaviour or history",
        ),
        (
            "Business signals",
            counts["business_signal_candidates"],
            "Retained concern, supportive, or conflicting evidence that gives a reviewer a concrete question",
        ),
        (
            "Unique business patterns",
            counts["unique_business_patterns"],
            "Collapsed duplicate item combinations before presentation selection",
        ),
        (
            "Displayed for review",
            counts["selected_rules"],
            "Selected a varied set for explanation; these are not lending policy rules",
        ),
    ]
    previous = stages[0][1]
    screening_rows = []
    for stage, remaining, reason in stages:
        screening_rows.append((stage, remaining, previous - remaining, reason))
        previous = remaining
    screening = pd.DataFrame(
        screening_rows,
        columns=["stage", "remaining_rules", "removed_at_stage", "business_reason"],
    )
    screening.to_csv(P3 / "rule_screening_summary.csv", index=False)
    return screening, rules


def build_association_threshold_register() -> pd.DataFrame:
    """Show how stricter rule thresholds change the candidate workload.

    Phase 3 mines at 3% support, 35% confidence, and 1.20 lift.  The saved
    candidate pool can therefore test stricter settings, but it cannot estimate
    what a looser mining run would have found.  The register makes that boundary
    explicit and keeps the full-portfolio and within-segment denominators apart.
    """
    portfolio = pd.read_csv(P3 / "rules_combined.csv")
    within_segment = pd.read_csv(P3 / "rules_per_cluster.csv")
    smallest_segment = int(within_segment["context_n"].min())
    full_portfolio = int(portfolio["context_n"].max())
    scenarios = [
        ("Selected discovery setting", .03, .35, 1.20),
        ("Higher support", .04, .35, 1.20),
        ("Higher confidence", .03, .45, 1.20),
        ("Higher lift", .03, .35, 1.30),
        ("All three stricter", .04, .45, 1.30),
    ]

    rows = []
    for name, support, confidence, lift in scenarios:
        def count(frame: pd.DataFrame) -> int:
            return int((
                frame["support"].ge(support)
                & frame["confidence"].ge(confidence)
                & frame["lift"].ge(lift)
            ).sum())

        rows.append({
            "scenario": name,
            "minimum_support": support,
            "minimum_confidence": confidence,
            "minimum_lift": lift,
            "portfolio_candidate_rules": count(portfolio),
            "within_segment_candidate_rules": count(within_segment),
            "minimum_matches_full_portfolio": int(round(support * full_portfolio)),
            "minimum_matches_smallest_segment": int(round(support * smallest_segment)),
            "denominator_note": (
                f"Support means applications within its own context: {full_portfolio:,} portfolio-wide, "
                f"or as few as {smallest_segment:,} in the smallest segment."
            ),
            "interpretation": (
                "Counts describe the mined candidate workload before business identity screening; "
                "they are not applicant risk counts or underwriting rules."
            ),
            "sensitivity_boundary": (
                "Only equal or stricter settings can be evaluated from the saved 3%/35%/1.20 candidate pool; "
                "a looser setting requires a new mining run."
            ),
        })
    register = pd.DataFrame(rows)
    register.to_csv(P3 / "association_threshold_register.csv", index=False)
    return register


def rebuild_anomaly_investigation() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Rebuild the row-level queue with the exact field behind any >=10-SD trigger."""
    business = pd.read_csv(DATA / "final" / "features_business.csv")
    combined = pd.read_csv(P4 / "anomaly_combined.csv")
    labels = pd.read_csv(
        DATA / "final" / "cluster_labels.csv",
        usecols=["ROW_ID", "SK_ID_CURR", "CLUSTER_KMEANS"],
    )
    cluster_names = pd.read_csv(P2 / "cluster_names.csv")
    anomaly_features = pd.read_csv(DATA / "final" / "features_anomaly.csv")
    investigation, drivers = build_anomaly_investigation(
        business=business,
        combined=combined,
        labels=labels,
        cluster_names=cluster_names,
        anomaly_features=anomaly_features,
    )
    investigation.to_csv(P4 / "anomaly_investigation.csv", index=False)
    drivers.to_csv(P4 / "anomaly_driver_summary.csv", index=False)
    return investigation, drivers


def build_review_trigger_register() -> pd.DataFrame:
    """Publish the heuristic thresholds used only to compose human-review text."""
    columns = [
        "SK_ID_CURR", "SOURCE_AMT_INCOME_TOTAL", "SOURCE_AMT_CREDIT", "SOURCE_AMT_ANNUITY",
        "INST_DPD_MAX", "INST_LATE_RATIO", "INST_SEVERE_LATE_RATIO",
        "INST_PAYMENT_RATIO_MEAN", "CC_UTILIZATION_MEAN", "CC_UTILIZATION_MAX",
        "CC_SK_DPD_MEAN", "POS_SK_DPD_MEAN", "BUREAU_DEBT_TO_CREDIT_RATIO",
        "BUREAU_BB_DPD_RATIO_MEAN", "BUREAU_BB_SEVERE_DPD_MEAN",
        "SOURCE_EXT_SOURCE_1", "SOURCE_EXT_SOURCE_2", "SOURCE_EXT_SOURCE_3",
        "PREV_REFUSED_COUNT", "PREV_APPROVAL_RATE",
    ]
    data = pd.read_csv(DATA / "final" / "features_business.csv", usecols=columns)
    income = data["SOURCE_AMT_INCOME_TOTAL"]
    valid_income = income.gt(0)
    annuity_to_income = data["SOURCE_AMT_ANNUITY"].div(income).where(valid_income)
    credit_to_income = data["SOURCE_AMT_CREDIT"].div(income).where(valid_income)
    card_or_pos_dpd = data[["CC_SK_DPD_MEAN", "POS_SK_DPD_MEAN"]].max(axis=1)
    external_mean = data[[
        "SOURCE_EXT_SOURCE_1", "SOURCE_EXT_SOURCE_2", "SOURCE_EXT_SOURCE_3"
    ]].mean(axis=1, skipna=True)

    rows: list[dict[str, object]] = []

    def add(
        trigger: str,
        field: str,
        looser_label: str,
        selected_label: str,
        stricter_label: str,
        looser_mask: pd.Series,
        selected_mask: pd.Series,
        stricter_mask: pd.Series,
        basis: str,
        rationale: str,
    ) -> None:
        looser_count = int(looser_mask.fillna(False).sum())
        selected_count = int(selected_mask.fillna(False).sum())
        stricter_count = int(stricter_mask.fillna(False).sum())
        if not looser_count >= selected_count >= stricter_count:
            raise ValueError(f"Sensitivity counts are not monotonic for {trigger}")
        rows.append({
            "trigger": trigger,
            "field_or_expression": field,
            "looser_sensitivity": looser_label,
            "selected_review_trigger": selected_label,
            "stricter_sensitivity": stricter_label,
            "looser_application_count": looser_count,
            "selected_application_count": selected_count,
            "stricter_application_count": stricter_count,
            "basis": basis,
            "business_rationale": rationale,
            "population": "All 356,255 applications",
            "usage_boundary": (
                "Composes review evidence only after a record enters the anomaly queue; "
                "not a queue-entry rule, approval rule, decline rule, or Home Credit policy"
            ),
            "automatic_decision_allowed": "No",
        })

    add(
        "Scheduled payment burden", "SOURCE_AMT_ANNUITY / SOURCE_AMT_INCOME_TOTAL",
        ">=30%", ">=35%", ">=50%", annuity_to_income.ge(.30), annuity_to_income.ge(.35),
        annuity_to_income.ge(.50), "Project review heuristic; 50% escalates priority",
        "Directs a queued record to verified-income, obligation, and lower-income affordability review.",
    )
    add(
        "Current-loan amount relative to income", "SOURCE_AMT_CREDIT / SOURCE_AMT_INCOME_TOTAL",
        ">=5x", ">=6x", ">=8x", credit_to_income.ge(5), credit_to_income.ge(6),
        credit_to_income.ge(8), "Project review heuristic; product term and existing obligations are unavailable",
        "Highlights scale relative to reported income without treating the ratio as a policy cutoff.",
    )
    add(
        "Longest recorded instalment delay", "INST_DPD_MAX", ">15 days", ">30 days", ">=90 days",
        data["INST_DPD_MAX"].gt(15), data["INST_DPD_MAX"].gt(30), data["INST_DPD_MAX"].ge(90),
        "Operational 30+/90+ DPD severity bands; not a legal-default definition",
        "Routes attention to recency, cure, dispute, and whether an obligation remains open.",
    )
    add(
        "Severely late instalment share", "INST_SEVERE_LATE_RATIO", ">=2%", ">=5%", ">=10%",
        data["INST_SEVERE_LATE_RATIO"].ge(.02), data["INST_SEVERE_LATE_RATIO"].ge(.05),
        data["INST_SEVERE_LATE_RATIO"].ge(.10), "Project recurrence heuristic over aggregated previous-loan history",
        "Separates an isolated delay from a repeated severe-lateness pattern for manual timeline review.",
    )
    add(
        "Any late instalment share", "INST_LATE_RATIO", ">=10%", ">=20%", ">=30%",
        data["INST_LATE_RATIO"].ge(.10), data["INST_LATE_RATIO"].ge(.20),
        data["INST_LATE_RATIO"].ge(.30), "Project recurrence heuristic over aggregated previous-loan history",
        "Prompts a reviewer to examine timing and causes; it does not establish current distress.",
    )
    add(
        "Average paid-to-due ratio", "INST_PAYMENT_RATIO_MEAN", "<95%", "<90%", "<85%",
        data["INST_PAYMENT_RATIO_MEAN"].between(0, .95, inclusive="left"),
        data["INST_PAYMENT_RATIO_MEAN"].between(0, .90, inclusive="left"),
        data["INST_PAYMENT_RATIO_MEAN"].between(0, .85, inclusive="left"),
        "Project underpayment heuristic; reversals and early payments can affect the aggregate",
        "Prompts reconciliation of partial payments, reversals, duplicates, and cure status.",
    )
    add(
        "Historical card utilisation", "CC_UTILIZATION_MEAN or CC_UTILIZATION_MAX",
        "mean >=70% or max >=90%", "mean >=80% or max >=100%", "mean >=90% or max >=110%",
        data["CC_UTILIZATION_MEAN"].ge(.70) | data["CC_UTILIZATION_MAX"].ge(.90),
        data["CC_UTILIZATION_MEAN"].ge(.80) | data["CC_UTILIZATION_MAX"].ge(1.00),
        data["CC_UTILIZATION_MEAN"].ge(.90) | data["CC_UTILIZATION_MAX"].ge(1.10),
        "Project historical-utilisation heuristic; fields summarize previous Home Credit accounts",
        "Requires checking whether a revolving facility is still open before any current-limit review.",
    )
    add(
        "Historical card or POS delay", "max(CC_SK_DPD_MEAN, POS_SK_DPD_MEAN)",
        ">0 days", ">0 days", ">30 days", card_or_pos_dpd.gt(0), card_or_pos_dpd.gt(0),
        card_or_pos_dpd.gt(30), "Any recorded average delay is surfaced; 30 days is the stricter sensitivity",
        "Directs the reviewer to the previous-account timeline, cure status, and current facility status.",
    )
    add(
        "Recorded bureau debt share", "BUREAU_DEBT_TO_CREDIT_RATIO", ">=60%", ">=80%", ">=100%",
        data["BUREAU_DEBT_TO_CREDIT_RATIO"].ge(.60), data["BUREAU_DEBT_TO_CREDIT_RATIO"].ge(.80),
        data["BUREAU_DEBT_TO_CREDIT_RATIO"].ge(1.00), "Project external-obligation review heuristic",
        "Prompts direct confirmation of outstanding obligations and ratio construction.",
    )
    add(
        "Bureau late-payment history", "BUREAU_BB_DPD_RATIO_MEAN or BUREAU_BB_SEVERE_DPD_MEAN",
        "late >=5% or severe >=1%", "late >=10% or severe >=2%", "late >=20% or severe >=5%",
        data["BUREAU_BB_DPD_RATIO_MEAN"].ge(.05) | data["BUREAU_BB_SEVERE_DPD_MEAN"].ge(.01),
        data["BUREAU_BB_DPD_RATIO_MEAN"].ge(.10) | data["BUREAU_BB_SEVERE_DPD_MEAN"].ge(.02),
        data["BUREAU_BB_DPD_RATIO_MEAN"].ge(.20) | data["BUREAU_BB_SEVERE_DPD_MEAN"].ge(.05),
        "Project recurrence heuristic on aggregated bureau monthly history",
        "Prompts a source-timeline, dispute, recency, and cure check rather than a causal conclusion.",
    )
    add(
        "Available external-score mean", "mean(observed SOURCE_EXT_SOURCE_1..3)",
        "<0.40", "<0.30", "<0.20", external_mean.lt(.40), external_mean.lt(.30),
        external_mean.lt(.20), "Project heuristic; external-score construction and calibration are opaque",
        "Only prompts source-validity and evidence reconciliation; the mean is never a reason code.",
    )
    add(
        "Repeated previous refusals", "PREV_REFUSED_COUNT and PREV_APPROVAL_RATE",
        ">=2 refusals and approval <50%", ">=3 refusals and approval <50%", ">=4 refusals and approval <50%",
        data["PREV_REFUSED_COUNT"].ge(2) & data["PREV_APPROVAL_RATE"].lt(.50),
        data["PREV_REFUSED_COUNT"].ge(3) & data["PREV_APPROVAL_RATE"].lt(.50),
        data["PREV_REFUSED_COUNT"].ge(4) & data["PREV_APPROVAL_RATE"].lt(.50),
        "Project history-reconciliation heuristic; earlier policy and evidence are unknown",
        "Prompts review of the historical reason and whether it remains relevant now.",
    )

    register = pd.DataFrame(rows)
    register.to_csv(P4 / "review_trigger_register.csv", index=False)
    return register


def build_queue_route_summary() -> pd.DataFrame:
    investigation_path = P4 / "anomaly_investigation.csv"
    investigation = pd.read_csv(investigation_path)
    if "Queue Route" not in investigation:
        combined = pd.read_csv(
            P4 / "anomaly_combined.csv",
            usecols=["ROW_ID", "queue_route"],
        )
        investigation = investigation.merge(
            combined,
            on="ROW_ID",
            how="left",
            validate="one_to_one",
        ).rename(columns={"queue_route": "Queue Route"})
    investigation["Queue Route"] = investigation["Queue Route"].replace(
        "Implausible single value", "Extreme single-axis value"
    )
    investigation["Record Evidence"] = (
        investigation["Record Evidence"].astype(str)
        .str.replace("Requested credit equals", "Current-loan credit amount equals", regex=False)
        .str.replace("Requested credit is", "Current-loan credit amount is", regex=False)
    )
    investigation["Business Interpretation"] = (
        investigation["Business Interpretation"].astype(str)
        .str.replace("not evidence of default", "not evidence of payment difficulty", regex=False)
    )
    investigation.to_csv(investigation_path, index=False)
    summary = (
        investigation.groupby(
            ["Queue Route", "Review Type", "Anomaly Scope", "Outlier Type"],
            as_index=False,
        )
        .size()
        .rename(columns={"size": "applications"})
    )
    summary["population"] = "Targeted review queue"
    summary["automatic_decision_allowed"] = "No"
    summary.to_csv(P4 / "anomaly_queue_route_summary.csv", index=False)
    return summary


def main() -> None:
    labels = named_labels()
    coverage = build_evidence_coverage(labels)
    profiles = build_segment_full_profiles(labels)
    assert profiles["population"].nunique() == 6
    assert not profiles[["mean", "std"]].isna().all(axis=1).any()
    concentration = build_credit_concentration_summary(labels)
    screening, selected_rules = build_rule_summaries()
    association_register = build_association_threshold_register()
    investigation, _ = rebuild_anomaly_investigation()
    trigger_register = build_review_trigger_register()
    queue = build_queue_route_summary()

    assert len(labels) == 356_255
    assert int(concentration["applications"].sum()) == 356_255
    assert abs(float(concentration["credit_amount_share"].sum()) - 1.0) < 1e-9
    combined = pd.read_csv(
        P4 / "anomaly_combined.csv",
        usecols=[
            "ROW_ID", "anomaly_category", "dbscan_sample_covered",
            "dbscan_sample_noise",
        ],
    )
    targeted_count = int(combined["anomaly_category"].isin(
        ["TARGETED_REVIEW", "HIGH_CONFIDENCE_ANOMALY"]
    ).sum())
    assert int(queue["applications"].sum()) == targeted_count == len(investigation)
    extreme_route = investigation["Queue Route"].eq("Extreme single-axis value")
    assert set(investigation["Queue Route"]) == {
        "Detector consensus", "Extreme single-axis value"
    }
    assert investigation.loc[extreme_route, "Extreme Trigger Field"].ne("").all()
    assert investigation.loc[extreme_route, "Extreme Trigger Standardized Value"].abs().ge(10).all()
    assert investigation.loc[extreme_route, "Anomaly Scope"].eq("Portfolio single-axis extreme").all()
    assert investigation.loc[~extreme_route, "Anomaly Scope"].eq("Detector-consensus pattern").all()
    assert investigation["Density Corroboration"].isin(DENSITY_STATES).all()
    combined_density_states = density_states(combined)
    targeted_density = combined.loc[
        combined["anomaly_category"].isin(["TARGETED_REVIEW", "HIGH_CONFIDENCE_ANOMALY"]),
        ["ROW_ID"],
    ].copy()
    targeted_density["Expected Density Corroboration"] = combined_density_states.loc[
        targeted_density.index
    ]
    density_audit = investigation[["ROW_ID", "Density Corroboration"]].merge(
        targeted_density,
        on="ROW_ID",
        how="outer",
        validate="one_to_one",
        indicator=True,
    )
    assert density_audit["_merge"].eq("both").all()
    assert density_audit["Density Corroboration"].eq(
        density_audit["Expected Density Corroboration"]
    ).all()
    actual_density_counts = investigation["Density Corroboration"].value_counts()
    expected_density_counts = targeted_density[
        "Expected Density Corroboration"
    ].value_counts()
    assert actual_density_counts.reindex(DENSITY_STATES, fill_value=0).to_dict() == (
        expected_density_counts.reindex(DENSITY_STATES, fill_value=0).to_dict()
    )
    assert int(screening.iloc[-1]["remaining_rules"]) == len(selected_rules)
    assert 10 <= len(selected_rules) <= 12
    assert len(coverage) == 25
    assert len(trigger_register) == 12
    assert len(association_register) == 5
    assert trigger_register["automatic_decision_allowed"].eq("No").all()
    print("Business summaries rebuilt and denominator checks passed.")


if __name__ == "__main__":
    main()

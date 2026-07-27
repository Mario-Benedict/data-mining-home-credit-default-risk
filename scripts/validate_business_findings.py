"""Fail fast when dashboard claims drift away from the exported evidence.

This is deliberately a business-output test rather than another model test. It
checks denominators, route totals, feature governance, the exact dashboard
figures used in the presentation, and that no outcome-label vocabulary leaks
into any business-facing surface: the portfolio is presented as one unlabeled
population, so labels, label rates, and raw source column names must not
appear in the story told to reviewers.
"""
from __future__ import annotations

import ast
import itertools
import json
import math
import re
import sys
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
P1 = ROOT / "results" / "phase1_preprocessing"
P2 = ROOT / "results" / "phase2_clustering"
P3 = ROOT / "results" / "phase3_association"
P4 = ROOT / "results" / "phase4_anomaly"

DENSITY_STATES = (
    # Retained for schema stability. Since the density view became
    # portfolio-wide this state is empty by construction, and the validator
    # asserts that it matches the count of uncovered rows, which is now zero.
    "Not assessed",
    "Assessed (not isolated)",
    "Assessed (isolated)",
)
# Deliberately re-declared here rather than imported. This module exists to
# catch drift, so it states the labels it expects and fails if the pipeline
# ever quietly renames one.
OUTLIER_TYPES = (
    "Point (globally extreme single value)",
    "Collective (mutually linked separated group)",
    "Contextual (unusual against its own segment)",
)
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
CANONICAL_RULE_CONTEXTS = {
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


def assert_columns(frame: pd.DataFrame, required: set[str], artifact: str) -> None:
    missing = required.difference(frame.columns)
    assert not missing, (artifact, sorted(missing))


def integer_values(series: pd.Series, field: str) -> pd.Series:
    """Check that an exported count is genuinely integer-valued."""
    numeric = pd.to_numeric(series, errors="coerce")
    assert numeric.notna().all(), field
    assert numeric.eq(numeric.round()).all(), field
    return numeric.astype("int64")


def csv_boolean(value: object, field: str) -> bool:
    """Parse a Boolean-like CSV value without bool('False') mistakes."""
    if isinstance(value, bool):
        return value
    normalized = str(value).strip().lower()
    assert normalized in {"true", "false", "1", "0"}, (field, value)
    return normalized in {"true", "1"}


def nullable_boolean_series(series: pd.Series, field: str) -> pd.Series:
    """Normalize Boolean-like CSV values while preserving a missing result."""
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
        raise AssertionError(f"{field} contains an invalid Boolean value: {value!r}")

    return series.map(parse).astype("boolean")


def expected_density_states(frame: pd.DataFrame) -> pd.Series:
    """Map DBSCAN sample coverage and isolation to the expected three-state label."""
    required = {"dbscan_sample_covered", "dbscan_sample_noise"}
    assert required.issubset(frame.columns), required.difference(frame.columns)
    covered = nullable_boolean_series(frame["dbscan_sample_covered"], "dbscan_sample_covered")
    noise = nullable_boolean_series(frame["dbscan_sample_noise"], "dbscan_sample_noise")
    assert covered.notna().all()
    assert noise.loc[covered].notna().all()
    assert noise.loc[~covered].isna().all()

    states = pd.Series("Not assessed", index=frame.index, dtype="object")
    states.loc[covered & noise.fillna(False)] = "Assessed (isolated)"
    states.loc[covered & ~noise.fillna(False)] = "Assessed (not isolated)"
    return states


def close(actual: float, expected: float, *, tolerance: float = 1e-12) -> None:
    assert math.isclose(float(actual), float(expected), rel_tol=tolerance, abs_tol=tolerance), (
        actual,
        expected,
    )


def component_count(node: object, class_name: str) -> int:
    """Count Dash components carrying one exact class name."""
    if node is None or isinstance(node, (str, int, float, bool)):
        return 0
    if isinstance(node, (list, tuple)):
        return sum(component_count(item, class_name) for item in node)
    current = int(getattr(node, "className", None) == class_name)
    return current + component_count(getattr(node, "children", None), class_name)


def validate_feature_governance() -> None:
    decisions = pd.read_csv(P1 / "feature_selection_decisions.csv")
    assert len(decisions) == 74
    assert decisions["status"].value_counts().to_dict() == {"keep": 41, "drop": 33}
    assert not decisions["target_used_for_decision"].astype(bool).any()

    # EXT_SOURCE_1 must stay an explicit, reasoned drop rather than quietly
    # disappearing from the mining matrix. Its removal is the one case neither
    # correlation nor entropy can express, so the audit has to name it.
    ext1 = decisions.loc[decisions["feature"].eq("EXT_SOURCE_1")]
    assert len(ext1) == 1, "EXT_SOURCE_1 must appear exactly once in the decision trail"
    ext1 = ext1.iloc[0]
    assert ext1["status"] == "drop"
    assert ext1["decision_basis"] == "Imputation-induced duplication of its own missingness flag"
    assert ext1["high_corr_partner"] == "FLAG_EXT_SOURCE_1_MISSING"
    for matrix in ("features_clustering.csv", "features_anomaly.csv"):
        columns = pd.read_csv(ROOT / "datasets" / "final" / matrix, nrows=0).columns
        assert "EXT_SOURCE_1" not in columns, (matrix, "still carries the imputed score")
        assert "FLAG_EXT_SOURCE_1_MISSING" in columns, (matrix, "lost the availability flag")

    correlation_drops = decisions.loc[decisions["decision_basis"].eq("Correlation redundancy")]
    assert len(correlation_drops) == 31
    assert correlation_drops["abs_corr"].notna().all()
    assert correlation_drops["abs_corr"].min() > 0.85

    mobile = decisions.loc[decisions["feature"].eq("FLAG_MOBIL")].iloc[0]
    assert mobile["status"] == "drop"
    assert float(mobile["dominant_value_share"]) > 0.9999

    severe = decisions.loc[decisions["feature"].eq("BUREAU_BB_SEVERE_DPD_MEAN")].iloc[0]
    assert int(severe["n_unique"]) > 1
    assert float(severe["normalized_unsupervised_entropy"]) > 0


def validate_populations_and_queue() -> None:
    concentration = pd.read_csv(P4 / "segment_credit_concentration.csv")
    assert concentration["Segment"].nunique() == 5
    assert int(concentration["applications"].sum()) == 356_255
    close(concentration["application_share"].sum(), 1.0)
    close(concentration["credit_amount_share"].sum(), 1.0)
    close(concentration["annuity_amount_share"].sum(), 1.0)
    assert concentration["amount_caveat"].str.contains(
        "not outstanding balance", regex=False
    ).all()
    assert not (P4 / "segment_outcome_credit_summary.csv").exists(), (
        "The label-based outcome summary must not be regenerated; the portfolio "
        "is presented as one unlabeled population."
    )

    evidence = pd.read_csv(P2 / "segment_evidence_coverage.csv")
    assert len(evidence) == 25
    assert evidence["Segment"].nunique() == 5
    assert evidence["Evidence source"].nunique() == 5
    lower_intensity = evidence.loc[
        evidence["Segment"].eq("Lower-Intensity Credit Footprint")
    ]
    # Segment sizes are re-derived rather than pinned to a literal, because a
    # deliberate feature change re-partitions the portfolio and a stale literal
    # would then fail for the wrong reason. What must hold is that the coverage
    # table agrees with the label file it was built from.
    labels_by_segment = pd.read_csv(
        ROOT / "datasets" / "final" / "cluster_labels.csv", usecols=["CLUSTER_KMEANS"]
    )["CLUSTER_KMEANS"].value_counts()
    names = pd.read_csv(ROOT / "datasets" / "final" / "cluster_names.csv")
    expected_sizes = {
        row.segment_name: int(labels_by_segment.loc[int(row.cluster_id)])
        for row in names.itertuples()
    }
    for segment, expected in expected_sizes.items():
        recorded = evidence.loc[evidence["Segment"].eq(segment), "applications"].unique()
        assert len(recorded) == 1, (segment, recorded)
        assert int(recorded.item()) == expected, (segment, int(recorded.item()), expected)
    assert sum(expected_sizes.values()) == 356_255
    # Coverage is a share, so it must stay inside [0, 1] and the bureau source
    # must remain the best-covered one for this segment.
    assert evidence["coverage"].between(0, 1).all()
    assert float(lower_intensity.loc[
        lower_intensity["Evidence source"].eq("Bureau history"), "coverage"
    ].iloc[0]) > float(lower_intensity.loc[
        lower_intensity["Evidence source"].eq("Previous Home Credit card history"), "coverage"
    ].iloc[0])

    investigation = pd.read_csv(P4 / "anomaly_investigation.csv")
    assert set(investigation["Queue Route"]) == {
        "Extreme single-axis value", "Detector consensus"
    }
    assert set(investigation["Review Type"]).issubset({
        "Affordability / repayment review",
        "Data consistency check",
        "Rare but plausible profile",
    })
    assert set(investigation["Anomaly Scope"]) == {
        "Portfolio single-axis extreme",
        "Detector-consensus pattern",
    }
    assert investigation["Density Corroboration"].isin(DENSITY_STATES).all()
    assert investigation["Automatic Decision Allowed"].eq("No").all()
    assert investigation["Recommended Action"].nunique() > 100
    assert investigation["Record Evidence"].nunique() > 1_000
    assert investigation["Business Interpretation"].nunique() > 1_000

    combined = pd.read_csv(
        P4 / "anomaly_combined.csv",
        usecols=[
            "ROW_ID", "max_abs_z", "anomaly_category", "queue_route",
            "detection_count", "available_detector_count", "agreement_share",
            "is_iqr_outlier", "is_zscore_outlier", "is_mahalanobis_outlier",
            "is_isolation_outlier", "is_lof_outlier", "dbscan_sample_covered",
            "dbscan_sample_noise", "extreme_single_axis", "collective_group",
        ],
    )
    method_columns = [
        "is_iqr_outlier", "is_zscore_outlier", "is_mahalanobis_outlier",
        "is_isolation_outlier", "is_lof_outlier",
    ]
    assert combined["available_detector_count"].eq(5).all()
    assert combined["detection_count"].eq(combined[method_columns].sum(axis=1)).all()
    close(float((combined["detection_count"] / 5).sub(combined["agreement_share"]).abs().max()), 0.0)
    targeted = combined["anomaly_category"].eq("TARGETED_REVIEW")
    assert len(investigation) == int(targeted.sum())
    assert combined.loc[targeted & combined["detection_count"].ge(3), "queue_route"].eq(
        "Detector consensus"
    ).all()
    assert combined.loc[targeted & combined["detection_count"].lt(3), "queue_route"].eq(
        "Extreme single-axis value"
    ).all()
    assert combined.loc[targeted & combined["detection_count"].lt(3), "max_abs_z"].ge(10).all()

    combined["Expected Density Corroboration"] = expected_density_states(combined)
    audited = investigation.merge(combined, on="ROW_ID", how="left", validate="one_to_one")
    expected_scope = audited["Queue Route"].map({
        "Detector consensus": "Detector-consensus pattern",
        "Extreme single-axis value": "Portfolio single-axis extreme",
    })
    assert audited["Anomaly Scope"].eq(expected_scope).all()
    audited_extreme = nullable_boolean_series(
        audited["extreme_single_axis"], "extreme_single_axis"
    ).fillna(False)
    audited_collective = nullable_boolean_series(
        audited["collective_group"], "collective_group"
    ).fillna(False)
    expected_type = pd.Series(OUTLIER_TYPES[2], index=audited.index)
    expected_type[audited_collective] = OUTLIER_TYPES[1]
    expected_type[audited_extreme] = OUTLIER_TYPES[0]
    assert audited["Outlier Type"].eq(expected_type).all()
    # Every record beyond 10 SD on a prepared axis is a point outlier, whichever
    # queue route admitted it, so the point count must cover the extreme route.
    assert audited.loc[
        audited["Queue Route"].eq("Extreme single-axis value"), "Outlier Type"
    ].eq(OUTLIER_TYPES[0]).all()
    assert audited["Density Corroboration"].eq(
        audited["Expected Density Corroboration"]
    ).all()
    actual_density_counts = investigation["Density Corroboration"].value_counts()
    expected_density_counts = combined.loc[
        targeted, "Expected Density Corroboration"
    ].value_counts()
    assert actual_density_counts.reindex(DENSITY_STATES, fill_value=0).to_dict() == (
        expected_density_counts.reindex(DENSITY_STATES, fill_value=0).to_dict()
    )
    covered = nullable_boolean_series(
        combined["dbscan_sample_covered"], "dbscan_sample_covered"
    )
    noise = nullable_boolean_series(combined["dbscan_sample_noise"], "dbscan_sample_noise")
    full_density_counts = combined["Expected Density Corroboration"].value_counts()
    assert int(full_density_counts.get("Not assessed", 0)) == int((~covered).sum())
    assert int(full_density_counts.get("Assessed (isolated)", 0)) == int(
        (covered & noise.fillna(False)).sum()
    )
    assert int(full_density_counts.get("Assessed (not isolated)", 0)) == int(
        (covered & ~noise.fillna(False)).sum()
    )
    assert ~audited["Detected By"].fillna("").str.contains("DBSCAN", case=False).any()
    assert audited["Detector Count"].between(0, 5).all()

    anomaly_summary = pd.read_csv(P4 / "anomaly_summary.csv").iloc[0]
    assert int(anomaly_summary["Total_Evaluated"]) == len(combined) == 356_255
    assert int(anomaly_summary["TARGETED_REVIEW"]) == int(targeted.sum()) == len(investigation)
    assert int(anomaly_summary["N_CONSENSUS_ROUTE"]) == int(
        combined["queue_route"].eq("Detector consensus").sum()
    )
    assert int(anomaly_summary["N_SINGLE_AXIS_ROUTE"]) == int(
        combined["queue_route"].eq("Extreme single-axis value").sum()
    )
    # The density view is portfolio-wide: DBSCAN runs on all 356,255 rows in the
    # 10-component space, so every application carries a density result and the
    # "Not assessed" state must be empty. A regression back to the sampled view
    # would show up here as a coverage count below the portfolio size.
    assert int(anomaly_summary["N_DBSCAN_SAMPLE_COVERED"]) == int(covered.sum()) == 356_255, (
        "the density view must cover every application; a sampled denominator has come back"
    )
    assert int(full_density_counts.get("Not assessed", 0)) == 0
    assert int(anomaly_summary["N_DBSCAN_SAMPLE_NOISE"]) == int(
        (covered & noise.fillna(False)).sum()
    )
    # The noise flag is corroboration, never a queue route, so it must stay far
    # more permissive than the queue itself. If it ever became selective enough
    # to look like a detector, the report's "reported but never votes" framing
    # would be wrong.
    density_space = pd.read_csv(P2 / "dbscan_space_comparison.csv")
    operating = density_space.loc[
        density_space["decides_downstream_flags"].map(
            lambda value: csv_boolean(value, "decides_downstream_flags")
        )
    ]
    assert len(operating) == 1, "exactly one density space may decide downstream flags"
    assert int(operating.iloc[0]["rows_assessed"]) == 356_255
    assert int(operating.iloc[0]["noise_points"]) == int(anomaly_summary["N_DBSCAN_SAMPLE_NOISE"])
    queued_noise = int((targeted & noise.fillna(False)).sum())
    assert int(anomaly_summary["Phase2_Corroborated_DBSCAN"]) == queued_noise
    assert queued_noise / int(targeted.sum()) > float(operating.iloc[0]["noise_share"]), (
        "density noise must be enriched inside the queue, otherwise it corroborates nothing"
    )

    sensitivity = pd.read_csv(P4 / "ensemble_single_axis_sensitivity.csv")
    assert len(sensitivity) == 9
    assert set(zip(
        sensitivity["consensus_at_least"].astype(int),
        sensitivity["single_axis_z_cutoff"].astype(float),
    )) == {(votes, cutoff) for votes in (2, 3, 4) for cutoff in (8.0, 10.0, 12.0)}
    for scenario in sensitivity.itertuples(index=False):
        consensus_mask = combined["detection_count"].ge(int(scenario.consensus_at_least))
        single_axis_mask = (~consensus_mask) & combined["max_abs_z"].ge(
            float(scenario.single_axis_z_cutoff)
        )
        assert int(scenario.consensus_records) == int(consensus_mask.sum())
        assert int(scenario.single_axis_additions) == int(single_axis_mask.sum())
        assert int(scenario.total_queue) == int((consensus_mask | single_axis_mask).sum())
        close(float(scenario.queue_share), float((consensus_mask | single_axis_mask).mean()))
    selected_sensitivity = sensitivity.loc[
        sensitivity["consensus_at_least"].eq(3)
        & sensitivity["single_axis_z_cutoff"].eq(10.0)
    ].iloc[0]
    assert int(selected_sensitivity["total_queue"]) == len(investigation)

    lof_diagnostic = pd.read_csv(P4 / "lof_crossfit_diagnostic.csv")
    assert int(lof_diagnostic["rows_scored"].sum()) == len(combined)
    assert lof_diagnostic["rows_seen_during_scoring_model_fit"].eq(0).all()
    assert lof_diagnostic["unseen_share"].eq(1.0).all()

    mahalanobis = pd.read_csv(P4 / "mahalanobis_diagnostics.csv").iloc[0]
    assert int(mahalanobis["fit_rows"]) == len(combined)
    assert int(mahalanobis["covariance_rank"]) == int(mahalanobis["feature_count"])
    assert csv_boolean(mahalanobis["all_scores_finite"], "mahalanobis.all_scores_finite")
    assert float(mahalanobis["min_eigenvalue"]) > 0
    assert math.isfinite(float(mahalanobis["condition_number"]))

    extreme_route = audited["Queue Route"].eq("Extreme single-axis value")
    assert audited.loc[extreme_route, "Extreme Trigger Field"].fillna("").ne("").all()
    assert audited.loc[extreme_route, "Extreme Trigger Standardized Value"].abs().ge(10).all()
    assert audited.loc[extreme_route, "Primary Driver"].str.startswith("Extreme ").all()
    assert audited.loc[extreme_route, "Record Evidence"].str.contains(
        "exact field that needs the single-axis source check", case=False, regex=False
    ).all()
    assert audited.loc[extreme_route, "Recommended Action"].str.contains(
        "sign, units, joins, and aggregation", case=False, regex=False
    ).all()

    routes = pd.read_csv(P4 / "anomaly_queue_route_summary.csv")
    assert int(routes["applications"].sum()) == len(investigation)
    assert routes.groupby("Queue Route")["applications"].sum().to_dict() == (
        investigation["Queue Route"].value_counts().to_dict()
    )


def validate_rules_and_review_controls() -> None:
    rejection = pd.read_csv(P3 / "rule_rejection_audit.csv")
    business_screen = pd.read_csv(P3 / "rule_business_screen_audit.csv")
    status = pd.read_csv(P3 / "rule_shortlist_status.csv")
    rules = pd.read_csv(P3 / "business_rules_final.csv")
    screening = pd.read_csv(P3 / "rule_screening_summary.csv")

    assert_columns(rejection, {"reason", "rules"}, "rule_rejection_audit.csv")
    assert_columns(business_screen, {"reason", "rules"}, "rule_business_screen_audit.csv")
    assert_columns(
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
    assert_columns(
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
    assert not rejection["reason"].duplicated().any()
    assert not business_screen["reason"].duplicated().any()
    rejection_counts = integer_values(rejection["rules"], "rule_rejection_audit.rules")
    business_screen_counts = integer_values(
        business_screen["rules"], "rule_business_screen_audit.rules"
    )
    assert rejection_counts.ge(0).all()
    assert business_screen_counts.ge(0).all()
    assert not rejection["reason"].eq("accepted_nontrivial").any()
    assert REQUIRED_RULE_SCREEN_REASONS.issubset(set(rejection["reason"]))
    rejection_by_reason = pd.Series(
        rejection_counts.to_numpy(), index=rejection["reason"]
    )
    candidate_rules = int(rejection_by_reason.sum())
    accepted_cross_source = int(rejection_by_reason.get("accepted_cross_source", 0))
    assert 0 < accepted_cross_source < candidate_rules
    assert int(business_screen_counts.sum()) == accepted_cross_source

    assert len(status) == 1
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
        business_screen_counts.loc[business_screen["reason"].isin(BUSINESS_RULE_THEMES)].sum()
    )
    assert status_counts["business_signal_candidates"] == business_signal_candidates
    assert (
        business_signal_candidates
        >= status_counts["unique_business_patterns"]
        >= status_counts["selected_unique_patterns"]
    )
    assert status_counts["assignment_minimum"] == 10
    assert csv_boolean(status_row["meets_assignment_minimum"], "meets_assignment_minimum")
    assert str(status_row["selection_note"]).strip()

    selected_rules = status_counts["selected_unique_patterns"]
    assert 10 <= selected_rules <= 12
    assert len(rules) == selected_rules
    assert rules["pattern_key"].is_unique
    assert rules["rule_str"].is_unique
    assert integer_values(rules["rank"], "business_rules_final.rank").tolist() == list(
        range(1, selected_rules + 1)
    )

    context_n = integer_values(rules["context_n"], "business_rules_final.context_n")
    condition_count = integer_values(
        rules["condition_count"], "business_rules_final.condition_count"
    )
    support_count = integer_values(rules["support_count"], "business_rules_final.support_count")
    assert support_count.gt(0).all()
    assert condition_count.ge(support_count).all()
    assert context_n.ge(condition_count).all()
    numeric = {
        field: pd.to_numeric(rules[field], errors="coerce")
        for field in ["support", "consequent_baseline", "confidence", "uplift_pp", "lift"]
    }
    assert all(series.notna().all() for series in numeric.values())
    assert numeric["support"].between(0, 1, inclusive="both").all()
    assert numeric["confidence"].between(0, 1, inclusive="both").all()
    assert numeric["consequent_baseline"].between(0, 1, inclusive="both").all()
    assert numeric["lift"].ge(1.20).all()
    expected_metrics = {
        "support": support_count / context_n,
        "confidence": support_count / condition_count,
        "consequent_baseline": numeric["confidence"] / numeric["lift"],
        "uplift_pp": 100 * (numeric["confidence"] - numeric["consequent_baseline"]),
    }
    for field, expected in expected_metrics.items():
        assert numeric[field].sub(expected).abs().max() <= 1e-9, field

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
        assert rules[field].fillna("").astype(str).str.strip().ne("").all(), field
    assert set(rules["business_theme"]).issubset(BUSINESS_RULE_THEME_LABELS)
    assert set(rules["Segment"]).issubset(CANONICAL_RULE_CONTEXTS)
    assert set(rules["Context"]).issubset(CANONICAL_RULE_CONTEXTS)
    text_columns = [
        column for column in rules.columns
        if pd.api.types.is_object_dtype(rules[column].dtype)
        or pd.api.types.is_string_dtype(rules[column].dtype)
    ]
    all_rule_text = "\n".join(
        rules[text_columns].fillna("").astype(str).to_numpy().ravel()
    ).lower()
    assert not any(label in all_rule_text for label in STALE_SEGMENT_LABELS)
    assert "cluster_" not in all_rule_text
    assert "not_observed" not in all_rule_text
    assert not any(token in all_rule_text for token in STRUCTURAL_RULE_TOKENS)
    source_counts = rules["source_families"].map(
        lambda value: len({part.strip() for part in str(value).split(";") if part.strip()})
    )
    assert source_counts.ge(2).all()
    assert not rules["source_families"].str.contains("unknown", case=False, na=False).any()

    assert screening["stage"].tolist() == [
        "Candidate rules tested",
        "Cross-source patterns",
        "Business signals",
        "Unique business patterns",
        "Displayed for review",
    ]
    expected_remaining = [
        candidate_rules,
        accepted_cross_source,
        business_signal_candidates,
        status_counts["unique_business_patterns"],
        selected_rules,
    ]
    assert integer_values(screening["remaining_rules"], "screening.remaining_rules").tolist() == (
        expected_remaining
    )
    assert integer_values(screening["removed_at_stage"], "screening.removed_at_stage").tolist() == [
        0,
        *(left - right for left, right in zip(expected_remaining, expected_remaining[1:])),
    ]
    assert screening["business_reason"].fillna("").str.strip().ne("").all()

    association_register = pd.read_csv(P3 / "association_threshold_register.csv")
    assert len(association_register) == 5
    assert association_register.iloc[0]["scenario"] == "Selected discovery setting"
    assert association_register["sensitivity_boundary"].str.contains(
        "requires a new mining run", regex=False
    ).all()

    trigger_register = pd.read_csv(P4 / "review_trigger_register.csv")
    assert len(trigger_register) == 12
    assert trigger_register["automatic_decision_allowed"].eq("No").all()
    assert trigger_register["looser_application_count"].ge(
        trigger_register["selected_application_count"]
    ).all()
    assert trigger_register["selected_application_count"].ge(
        trigger_register["stricter_application_count"]
    ).all()


def validate_presentation_surface() -> None:
    for notebook in (ROOT / "notebooks").glob("*.ipynb"):
        payload = json.loads(notebook.read_text(encoding="utf-8"))
        for cell in payload["cells"]:
            if cell.get("cell_type") != "code" or not "".join(cell.get("source", [])).strip():
                continue
            assert cell.get("execution_count") is not None, (
                notebook.name, "contains an unexecuted non-empty code cell"
            )
            assert not any(output.get("output_type") == "error" for output in cell.get("outputs", [])), (
                notebook.name, "contains a saved execution error"
            )
        assert "determinant has increased" not in notebook.read_text(encoding="utf-8").lower()

    report_text = (ROOT / "REPORT.md").read_text(encoding="utf-8")
    readme_text = (ROOT / "README.md").read_text(encoding="utf-8")
    dashboard_text = (ROOT / "dashboard" / "app.py").read_text(encoding="utf-8")

    report_findings = re.findall(r"^### Finding ", report_text, flags=re.MULTILINE)
    assert len(report_findings) == 3, "REPORT.md must contain exactly three Finding headings"

    dashboard_tree = ast.parse(dashboard_text, filename="dashboard/app.py")
    dashboard_finding_calls = sum(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "finding"
        for node in ast.walk(dashboard_tree)
    )
    assert dashboard_finding_calls == 3, "dashboard/app.py must call finding() exactly three times"

    combined_text = "\n".join([
        report_text,
        dashboard_text,
        *(path.read_text(encoding="utf-8") for path in (ROOT / "notebooks").glob("*.ipynb")),
    ]).lower()
    for stale in [
        "money at risk",
        "bottom line",
        "safest customers",
        "investigated 3+ detector-consensus records: 5,914",
        "single implausible value",
        "credit_term_months",
        "high_confidence_anomaly",
        "thin documentation",
    ]:
        assert stale not in combined_text, stale

    presentation_text = "\n".join([readme_text, report_text, dashboard_text]).lower()
    for stale in [
        "cluster_default_",
        "supervised_reference",
        "outcome_method_comparison",
        "plot_objective_comparison",
        "supervised logistic diagnostic",
        "outcome-trained diagnostic",
        "train-only outcome diagnostic",
        "segmentation precision",
        "segmentation recall",
        "threshold_uplift",
        "lift_vs_baseline",
        "confusion matrix",
        "1.10x",
        # The portfolio is presented as one unlabeled population. No business
        # surface may lean on the outcome label, split the data into labeled
        # and unlabeled parts, or describe a label rate.
        "labeled train",
        "labelled train",
        "labelled (train)",
        "unlabelled (test)",
        "unlabeled test",
        "target=1",
        "train-only",
        "train average",
        "payment-difficulty rate",
        "payment difficulty rate",
        "segment_outcome_credit_summary",
        "observed_payment_difficulty",
    ]:
        assert stale not in presentation_text, stale
    assert re.search(r"\b(?:precision|recall|specificity)\b", presentation_text) is None
    raw_presentation_text = "\n".join([readme_text, report_text, dashboard_text])
    assert re.search(r"\bTARGET\b", raw_presentation_text) is None, (
        "The outcome-label column name must not appear on a business surface."
    )
    assert "—" not in raw_presentation_text, (
        "Em dashes are not allowed in presentation text."
    )

    sys.path.insert(0, str(ROOT))
    import dashboard.app as dashboard  # noqa: PLC0415

    assert component_count(dashboard.keyfindings_layout(), "finding") == 3
    # Every layout must build. A stale lookup keyed on an exported label used to
    # fail silently here rather than raising: the dashboard mapped 2,057 of the
    # 6,391 queued records to a blank outlier type because Phase 4 had renamed
    # two of the three labels. Rendering each section and then reconciling the
    # rendered typology against the export is what turns that into a build failure.
    for layout in (
        dashboard.segments_layout,
        dashboard.anomalies_layout,
        dashboard.rules_layout,
        dashboard.overview_layout,
    ):
        assert layout() is not None, layout.__name__
    investigation = pd.read_csv(P4 / "anomaly_investigation.csv")
    short_labels = dashboard.anomaly_investigation["Outlier Type Short"]
    assert short_labels.notna().all(), (
        "the dashboard could not label every queued record's outlier type"
    )
    assert set(short_labels) == set(dashboard.TYPOLOGY_ORDER)
    expected_typology = (
        investigation["Outlier Type"].str.split("(", n=1).str[0].str.strip().value_counts()
    )
    assert short_labels.value_counts().to_dict() == expected_typology.to_dict(), (
        "the dashboard's outlier typology counts disagree with anomaly_investigation.csv"
    )
    assert set(dashboard.TYPOLOGY_MEANING) == set(dashboard.TYPOLOGY_ORDER)
    for figure in [
        dashboard.fig_attention_concentration,
        dashboard.fig_amount_concentration,
        dashboard.fig_converging_evidence,
        dashboard.fig_rule_screening,
        dashboard.fig_signal_agreement,
        dashboard.fig_rule_workload,
        dashboard.fig_cluster_profiles,
        dashboard.fig_queue_sensitivity,
        dashboard.fig_dbscan,
    ]:
        assert len(figure.data) > 0
    for figure_path in ("linkage_comparison.png", "plot_cluster_tendency.png"):
        assert (P2 / figure_path).stat().st_size > 10_000, figure_path



DETECTOR_LABELS = {
    "IQR": "Adjusted IQR",
    "Z-score": "Calibrated Z-score",
    "Mahalanobis": "Shrinkage Mahalanobis",
    "IsoForest": "Isolation Forest",
    "LOF": "Local Outlier Factor",
}


def _validate_record_appendix(report: str) -> None:
    """Reconcile every record row in Appendix C against the exported queue."""
    header = (
        "| Record ID | Methods flagged by | Key scores | Outlier type | "
        "Typology basis | Business interpretation |"
    )
    assert report.count(header) == 1, "Appendix C's record table header has changed"
    body = report.split(header, 1)[1].split("\n")[2:]
    lines = list(itertools.takewhile(lambda line: line.startswith("| "), body))
    assert lines, "Appendix C lists no records"

    investigation = pd.read_csv(P4 / "anomaly_investigation.csv")
    scores = pd.read_csv(
        P4 / "anomaly_combined.csv",
        usecols=[
            "ROW_ID", "mahalanobis_d2", "isolation_score", "lof_score",
            "iqr_outlier_count", "zscore_outlier_count",
        ],
    )
    queue = investigation.merge(scores, on="ROW_ID", how="left", validate="one_to_one")
    queue = queue.set_index("SK_ID_CURR")

    covered_types: set[str] = set()
    for line in lines:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        record_id = int(cells[0])
        assert record_id in queue.index, (record_id, "is not in the review queue")
        record = queue.loc[record_id]
        detected = str(record["Detected By"])

        # Every detector named in the report must have fired, and every detector
        # that fired must be named. An omission reads as weaker evidence than
        # the record actually carries.
        for short, full in DETECTOR_LABELS.items():
            written = bool(re.search(rf"\b{re.escape(short)}\b", cells[1]))
            fired = full in detected
            assert written == fired, (record_id, short, "written" if written else "omitted", fired)

        for pattern, column in [
            (r"IQR \((\d+)\)", "iqr_outlier_count"),
            (r"Z-score \((\d+)\)", "zscore_outlier_count"),
        ]:
            match = re.search(pattern, cells[1])
            if match:
                assert int(match.group(1)) == int(record[column]), (record_id, column)

        for pattern, column, tolerance in [
            (r"D-sq ([\d,]+)", "mahalanobis_d2", 1.5),
            (r"ISO (-?[\d.]+)", "isolation_score", 0.002),
            (r"LOF ([\d.]+)", "lof_score", 0.02),
        ]:
            match = re.search(pattern, cells[2])
            if match:
                written = float(match.group(1).replace(",", ""))
                assert abs(written - float(record[column])) <= tolerance, (record_id, column)

        expected_type = str(record["Outlier Type"]).split(" (")[0]
        assert cells[3] == expected_type, (record_id, cells[3], expected_type)
        covered_types.add(expected_type)

    # The appendix is meant to be representative, so all three types must appear.
    assert covered_types == {label.split(" (")[0] for label in OUTLIER_TYPES}, covered_types


def validate_headline_numbers_in_prose() -> None:
    """Re-derive every headline figure and require it to appear in the prose.

    The other checks in this module compare artefacts with artefacts. That let a
    whole class of defect through: a phase is re-run, its CSV changes, and
    REPORT.md keeps quoting the number the previous run produced. Nine such
    figures survived one re-run of Phase 2. This check closes that gap from the
    other side, by computing each figure from the artefact and asserting that the
    written text contains it. It deliberately does not check that a stale number
    is absent, because the same digits legitimately appear elsewhere: what it
    guarantees is that the current number is on the page.
    """
    report = (ROOT / "REPORT.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    agreement = pd.read_csv(P2 / "method_agreement.csv")
    primary = agreement.iloc[0]
    contrast = agreement.iloc[1]
    space = pd.read_csv(P2 / "dbscan_space_comparison.csv")
    deciding = space["decides_downstream_flags"].map(
        lambda value: csv_boolean(value, "decides_downstream_flags")
    )
    operating = space.loc[deciding].iloc[0]
    picture = space.loc[~deciding].iloc[0]
    tendency = pd.read_csv(P2 / "cluster_tendency.csv")
    at_five = tendency.loc[tendency["k"].eq(5)].iloc[0]
    degenerate = tendency.loc[
        tendency["shuffled_silhouette"].gt(tendency["real_silhouette"])
    ].sort_values("shuffled_silhouette").iloc[-1]
    families = pd.read_csv(P2 / "silhouette_by_feature_family.csv")
    alone = families.loc[~families["feature_family"].str.contains("together", case=False)]
    best_family = alone.sort_values("silhouette_alone").iloc[-1]
    split_half = pd.read_csv(P2 / "k_split_half_stability.csv")
    split_five = split_half.loc[split_half["k"].eq(5)].iloc[0]

    summary = pd.read_csv(P4 / "anomaly_summary.csv").iloc[0]
    queue = int(summary["TARGETED_REVIEW"])
    queued_noise = int(summary["Phase2_Corroborated_DBSCAN"])
    criteria = pd.read_csv(P4 / "collective_outlier_criteria.csv")
    group_test = criteria.iloc[0]
    density_row = criteria.iloc[1]

    # The overlap range is quoted three times in the report and is easy to get
    # wrong, because the exported matrix carries a sixth row for the density view
    # that is not one of the five detectors. Re-derive it from the five.
    overlap = pd.read_csv(P4 / "detector_jaccard_overlap.csv", index_col=0)
    detectors = [name for name in overlap.columns if "DBSCAN" not in name]
    assert len(detectors) == 5, detectors
    pairs = [
        float(overlap.loc[left, right])
        for index, left in enumerate(detectors)
        for right in detectors[index + 1:]
    ]
    mahalanobis = pd.read_csv(P4 / "mahalanobis_diagnostics.csv").iloc[0]
    thresholds = pd.read_csv(P4 / "anomaly_threshold_sensitivity.csv").set_index("detector")
    conventional_iqr = float(thresholds.loc["IQR conventional 1.5x; 3+ columns", "share"])

    # (surface, description, required text)
    required: list[tuple[str, str, str]] = [
        (report, "hierarchical validation ARI", f"{primary['adjusted_rand_index']:.4f}"),
        (report, "hierarchical validation NMI", f"{primary['normalized_mutual_information']:.4f}"),
        (report, "hierarchical largest group", f"{primary['largest_group_share']:.2%}".rstrip("%")),
        (report, "sampled Ward contrast ARI", f"{contrast['adjusted_rand_index']:.4f}"),
        (report, "portfolio DBSCAN eps", f"{float(operating['eps']):g}"),
        (report, "portfolio DBSCAN noise", f"{int(operating['noise_points']):,}"),
        (report, "portfolio DBSCAN pockets", f"{int(operating['density_pockets'])} density pockets"),
        (report, "UMAP DBSCAN noise", f"{int(picture['noise_points']):,}"),
        (report, "two-space Jaccard",
         f"{float(operating['agreement_jaccard_on_shared_rows']):.3f}"),
        (report, "null-model real silhouette", f"{at_five['real_silhouette']:.4f}"),
        (report, "null-model shuffled silhouette", f"{at_five['shuffled_silhouette']:.4f}"),
        (report, "null-model uniform silhouette", f"{at_five['uniform_silhouette']:.4f}"),
        (report, "degenerate null silhouette", f"{degenerate['shuffled_silhouette']:.4f}"),
        (report, "best feature family alone", f"{best_family['silhouette_alone']:.4f}"),
        (report, "split-half ARI at K=5", f"{split_five['split_half_ari_mean']:.3f}"),
        (report, "queue size", f"{queue:,}"),
        (report, "density corroboration of the queue", f"{queued_noise:,}"),
        (report, "collective eligible base", f"{int(group_test['eligible_applications']):,}"),
        (report, "density flags among eligible", f"{int(density_row['flagged']):,}"),
        (report, "detector overlap range", f"{min(pairs) * 100:.1f} to {max(pairs) * 100:.1f} percent"),
        (report, "detector overlap range, appendix", f"{min(pairs) * 100:.1f}%"),
        (report, "Mahalanobis review threshold", f"{float(mahalanobis['review_threshold']):.2f}"),
        (report, "chi-square 99.9th percentile", f"{float(mahalanobis['chi2_999_threshold']):.2f}"),
        (report, "chi-square diagnostic flag rate",
         f"{float(mahalanobis['chi2_999_diagnostic_flag_rate']) * 100:.2f}"),
        (report, "conventional IQR flag rate", f"{conventional_iqr * 100:.2f} percent"),
        (readme, "hierarchical validation ARI", f"{primary['adjusted_rand_index']:.3f}"),
        (readme, "portfolio DBSCAN noise", f"{int(operating['noise_points']):,}"),
        (readme, "two-space Jaccard",
         f"{float(operating['agreement_jaccard_on_shared_rows']):.3f}"),
        (readme, "best feature family alone", f"{best_family['silhouette_alone']:.3f}"),
    ]
    # Appendix C names individual records and the detectors that flagged them.
    # Four of its eight rows understated the detector list, each omitting a
    # detector that had in fact fired, which no artefact-to-artefact check could
    # see because the record itself was real. Reconcile each row against the
    # exported queue.
    _validate_record_appendix(report)

    missing = [
        (description, text) for surface, description, text in required if text not in surface
    ]
    assert not missing, (
        "these current figures are not written anywhere in the prose, so the text is "
        f"quoting a previous run: {missing}"
    )

    # Appendix B is a 12 by 5 grid of numbers transcribed by hand, which is where
    # per-cell drift hides: two cells had been stale by 0.04 of a percentage
    # point and 0.1 of one. Rather than spot-check, reconcile the whole grid.
    # Rows are matched by Lift descending, which is the order the appendix states.
    measures = pd.read_csv(P3 / "rule_interestingness_measures.csv").sort_values(
        "lift", ascending=False
    )
    header = "| Antecedent | Consequent | Context | Support | Confidence | Lift | Adjusted Lift | Kulczynski |"
    assert report.count(header) == 1, "Appendix B's rule table header has changed"
    body = report.split(header, 1)[1].split("\n")[2:]
    appendix_b = list(itertools.takewhile(lambda line: line.startswith("| "), body))
    assert len(appendix_b) == len(measures), (
        "Appendix B does not carry exactly one row per retained rule",
        len(appendix_b), len(measures),
    )
    for line, rule in zip(appendix_b, measures.itertuples(index=False)):
        cells = [cell.strip().strip("*") for cell in line.strip().strip("|").split("|")]
        support, confidence, lift, adjusted, kulczynski = cells[3:8]
        expected = {
            "support": (support, f"{rule.support * 100:.2f}%"),
            "confidence": (confidence, f"{rule.confidence * 100:.1f}%"),
            "lift": (lift, f"{rule.lift:.3f}"),
            "kulczynski": (kulczynski, f"{rule.kulczynski:.3f}"),
        }
        for field, (written, computed) in expected.items():
            assert written == computed, (cells[0], field, written, computed)
        # A rule whose consequent cannot accumulate must be marked, not silently
        # given a number equal to its raw Lift, because the marking is what makes
        # the unchanged rules readable as the control on the correction.
        if math.isclose(rule.exposure_adjusted_lift, rule.lift, rel_tol=1e-9):
            assert adjusted == "not applicable", (cells[0], adjusted)
        else:
            assert adjusted == f"{rule.exposure_adjusted_lift:.3f}", (cells[0], adjusted)


def validate_reasoning_controls() -> None:
    """Guard the four controls that stop a finding from restating its own construction.

    Each of these was added because an earlier version of a headline finding was
    arithmetically true and analytically empty. The assertions here make that
    class of defect fail the build instead of surviving review.
    """
    # 1. Exposure standardisation. An accumulation consequent (something that
    #    was "ever observed") must carry a confidence re-measured with history
    #    depth held constant, otherwise the rule can be reporting length of
    #    relationship rather than behaviour.
    rules = pd.read_csv(P3 / "business_rules_final.csv")
    exposure_columns = {
        "exposure_variable", "exposure_ratio", "exposure_adjusted_confidence",
        "exposure_adjusted_lift", "exposure_bias_share", "headline_lift",
        "exposure_sensitive", "exposure_note",
    }
    assert_columns(rules, exposure_columns, "business_rules_final.csv")
    sensitive = rules["exposure_sensitive"].map(
        lambda v: csv_boolean(v, "exposure_sensitive")
    )
    assert sensitive.any(), "no rule was tested for exposure bias"
    assert rules.loc[~sensitive, "exposure_adjusted_lift"].round(9).equals(
        rules.loc[~sensitive, "lift"].round(9)
    ), "application-time consequents must not be adjusted"
    assert rules.loc[sensitive, "exposure_ratio"].notna().all()
    assert rules["headline_lift"].notna().all()
    # The refusals-to-lateness pattern is the known exposure trap in this
    # dataset. If its adjusted lift ever stops being materially lower than its
    # raw lift, the correction has silently stopped working.
    trap = rules[rules["rule_str"].str.contains("previous_refusals_repeated")
                 & rules["rule_str"].str.contains("repayment_some_late")]
    assert len(trap) == 1, "the refusals-to-lateness pattern must remain in the shortlist"
    trap_row = trap.iloc[0]
    assert float(trap_row["exposure_adjusted_lift"]) < float(trap_row["lift"]) - 0.15, (
        "exposure standardisation is no longer reducing the known exposure-driven rule"
    )
    assert float(trap_row["exposure_bias_share"]) > 0.5

    # 1b. Cluster tendency. A silhouette of 0.148 is only interpretable beside
    #     the value chance produces on the same data. Two nulls are required: a
    #     column-wise shuffle that keeps every marginal and destroys only the
    #     joint structure, and a uniform draw over the same box. The operating K
    #     must beat both, and the degenerate low-K rows must stay on the record,
    #     because that is what stops a reader comparing 0.148 with a textbook
    #     threshold that assumes well-separated spheres.
    tendency = pd.read_csv(P2 / "cluster_tendency.csv")
    assert_columns(
        tendency,
        {"k", "real_silhouette", "real_smallest_group", "shuffled_silhouette",
         "shuffled_smallest_group", "uniform_silhouette", "gap_vs_shuffled",
         "degenerate_null"},
        "cluster_tendency.csv",
    )
    operating = tendency.loc[tendency["k"].eq(5)]
    assert len(operating) == 1, "the operating resolution K=5 must be scored against both nulls"
    operating = operating.iloc[0]
    assert float(operating["real_silhouette"]) > float(operating["shuffled_silhouette"])
    assert float(operating["real_silhouette"]) > float(operating["uniform_silhouette"])
    close(
        float(operating["gap_vs_shuffled"]),
        float(operating["real_silhouette"]) - float(operating["shuffled_silhouette"]),
        tolerance=1e-9,
    )
    # The trap this table exists to expose: at least one low-K row must show a
    # null scoring HIGHER than the real data by isolating a tiny group. Losing
    # that row would leave the low silhouette looking like a plain failure.
    degenerate = tendency.loc[
        tendency["degenerate_null"].map(lambda v: csv_boolean(v, "degenerate_null"))
        & tendency["shuffled_silhouette"].gt(tendency["real_silhouette"])
    ]
    assert len(degenerate) >= 1, (
        "no null model out-scores the real data by isolating a tiny group, so the "
        "warning against reading this silhouette against a textbook threshold has lost its evidence"
    )
    assert degenerate["shuffled_smallest_group"].max() < 0.02

    # 1c. Silhouette by feature family. The low combined value is claimed to be
    #     several overlapping segmentations rather than an absence of structure.
    #     That claim needs at least one family separating materially better on
    #     its own than all features together.
    families = pd.read_csv(P2 / "silhouette_by_feature_family.csv")
    assert_columns(
        families, {"feature_family", "features", "silhouette_alone"},
        "silhouette_by_feature_family.csv",
    )
    combined_row = families.loc[families["feature_family"].str.contains("together", case=False)]
    assert len(combined_row) == 1
    combined_silhouette = float(combined_row.iloc[0]["silhouette_alone"])
    single_families = families.drop(combined_row.index)
    assert len(single_families) >= 3
    assert float(single_families["silhouette_alone"].max()) > combined_silhouette + 0.30, (
        "no feature family separates materially better alone than all features together, "
        "so the overlapping-segmentation reading is no longer supported"
    )

    # 1d. Split-half stability. Seed stability answers whether the optimiser
    #     lands in the same place twice; only disjoint fits answer whether the
    #     segments belong to the portfolio. K=5 must win on the sample measure,
    #     which is the reason it is preferred over the K that scores higher on
    #     silhouette alone.
    split_half = pd.read_csv(P2 / "k_split_half_stability.csv")
    assert_columns(
        split_half,
        {"k", "split_half_ari_mean", "split_half_ari_min", "split_half_ari_max",
         "seed_ari_mean", "stability_gap"},
        "k_split_half_stability.csv",
    )
    assert {5, 6, 7}.issubset(set(split_half["k"].astype(int)))
    assert split_half["split_half_ari_min"].le(split_half["split_half_ari_mean"]).all()
    assert split_half["split_half_ari_mean"].le(split_half["split_half_ari_max"]).all()
    close(
        float(
            (split_half["seed_ari_mean"] - split_half["split_half_ari_mean"])
            .sub(split_half["stability_gap"]).abs().max()
        ),
        0.0,
        tolerance=1e-9,
    )
    chosen = split_half.loc[split_half["k"].eq(5)].iloc[0]
    assert float(chosen["split_half_ari_mean"]) > 0.90
    assert float(chosen["split_half_ari_mean"]) > float(
        split_half.loc[split_half["k"].ne(5), "split_half_ari_mean"].max()
    ), "K=5 no longer leads on sample stability, which is the ground it was chosen on"

    # 2. Concentration calibration. A segment share of recorded amount is only
    #    interpretable between its null and its ceiling.
    concentration = pd.read_csv(P2 / "segment_amount_concentration_calibrated.csv")
    assert_columns(
        concentration,
        {"Segment", "application_share", "amount_share", "null_share",
         "ceiling_share", "capture_ratio", "portfolio_gini"},
        "segment_amount_concentration_calibrated.csv",
    )
    assert concentration["Segment"].nunique() == 5
    close(float(concentration["amount_share"].sum()), 1.0, tolerance=1e-9)
    assert (concentration["ceiling_share"] >= concentration["amount_share"] - 1e-9).all(), (
        "no segment can carry more amount than the same number of largest loans"
    )
    assert (concentration["null_share"] - concentration["application_share"]).abs().max() < 1e-9

    # 3. Circularity control on the anomaly queue. Removing the features that
    #    named a segment must not be allowed to go unmeasured.
    circularity = pd.read_csv(P4 / "anomaly_circularity_check.csv")
    assert_columns(
        circularity,
        {"Segment", "applications", "queue_full", "queue_reduced",
         "share_of_queue_full", "share_of_queue_reduced", "retained_ratio"},
        "anomaly_circularity_check.csv",
    )
    assert circularity["Segment"].nunique() == 5
    assert int(circularity["applications"].sum()) == 356_255
    close(float(circularity["share_of_queue_full"].sum()), 1.0, tolerance=1e-9)
    close(float(circularity["share_of_queue_reduced"].sum()), 1.0, tolerance=1e-9)

    # 4. Typology basis. Every queued record must state the evidence that earned
    #    its label, and the contextual class must not be a pure residual.
    investigation = pd.read_csv(P4 / "anomaly_investigation.csv")
    assert_columns(
        investigation,
        {"Outlier Type", "Typology Basis", "Peer Deviation", "Peer Deviation Field"},
        "anomaly_investigation.csv",
    )
    assert investigation["Typology Basis"].notna().all()
    assert investigation["Typology Basis"].str.strip().ne("").all()
    point = investigation["Outlier Type"].eq(OUTLIER_TYPES[0])
    collective = investigation["Outlier Type"].eq(OUTLIER_TYPES[1])
    contextual = investigation["Outlier Type"].eq(OUTLIER_TYPES[2])
    assert investigation.loc[point, "Typology Basis"].str.startswith(
        "Portfolio reference").all()
    assert investigation.loc[collective, "Typology Basis"].str.startswith(
        "Group reference").all()
    # The collective class must be derived in the detection space, not borrowed
    # from the sampled projection that an earlier version relied on.
    criteria = pd.read_csv(P4 / "collective_outlier_criteria.csv")
    assert_columns(
        criteria,
        {"criterion", "eligible_applications", "flagged", "depends_on_projection"},
        "collective_outlier_criteria.csv",
    )
    primary = criteria.iloc[0]
    assert not csv_boolean(primary["depends_on_projection"], "depends_on_projection")
    # The three outlier types must stay disjoint, so the collective test runs on
    # the queued records that are not already point outliers. Its eligible base
    # is therefore the queue minus the point class, and every one of those
    # records is eligible: no sampling, no projection, no coverage gap.
    point_count = int(investigation["Outlier Type"].eq(OUTLIER_TYPES[0]).sum())
    assert int(primary["eligible_applications"]) == len(investigation) - point_count, (
        "the collective test must cover every queued record that is not a point outlier"
    )
    assert int(primary["flagged"]) == int(
        investigation["Outlier Type"].eq(OUTLIER_TYPES[1]).sum()
    ), "the collective criterion and the exported typology must agree"
    assert investigation.loc[contextual, "Typology Basis"].str.startswith(
        ("Segment reference", "Combination reference")).all()
    peer_backed = investigation.loc[contextual, "Typology Basis"].str.startswith(
        "Segment reference")
    assert peer_backed.any(), (
        "no contextual record is backed by a segment-relative deviation, so the "
        "class has degenerated into a residual bucket again"
    )

    # 5. The density view is embedding-dependent, so its disagreement has to stay
    #    on the record. A silently high agreement would mean the check stopped running.
    space = pd.read_csv(P2 / "dbscan_space_comparison.csv")
    assert_columns(
        space,
        {"space", "rows_assessed", "eps", "noise_points", "noise_share",
         "density_pockets", "decides_downstream_flags",
         "agreement_jaccard_on_shared_rows"},
        "dbscan_space_comparison.csv",
    )
    assert len(space) == 2
    # One Jaccard is computed on the rows both spaces judged, so it must be the
    # same value on both rows, and it must stay low: a high agreement would mean
    # the projection check had silently stopped comparing two different spaces.
    assert space["agreement_jaccard_on_shared_rows"].nunique() == 1
    assert float(space["agreement_jaccard_on_shared_rows"].iloc[0]) < 0.30, (
        "the two density spaces now agree closely; re-check that the comparison "
        "is still running on two genuinely different embeddings"
    )
    deciding = space["decides_downstream_flags"].map(
        lambda value: csv_boolean(value, "decides_downstream_flags")
    )
    assert int(deciding.sum()) == 1
    assert space.loc[~deciding, "space"].str.contains("UMAP").all(), (
        "the UMAP view must stay a picture and must not decide any downstream flag"
    )

    # 5b. Hierarchical validation. The primary comparison must be the one every
    #     application participates in, and it must sit first in the file, because
    #     the report and the dashboard both quote row zero. The sampled Ward
    #     contrast is retained only to show how much of the older, friendlier
    #     figure came from assigning the portfolio to nearest sample centres.
    agreement = pd.read_csv(P2 / "method_agreement.csv")
    assert_columns(
        agreement,
        {"comparison", "rows_clustered", "adjusted_rand_index",
         "normalized_mutual_information", "largest_group_share",
         "smallest_group_share", "role"},
        "method_agreement.csv",
    )
    assert len(agreement) == 2
    primary_agreement = agreement.iloc[0]
    assert int(primary_agreement["rows_clustered"]) == 356_255, (
        "row zero of method_agreement.csv must be the full-portfolio comparison, "
        "because that is the row the report and the dashboard quote"
    )
    assert "BIRCH" in str(primary_agreement["comparison"])
    assert "Primary" in str(primary_agreement["role"])
    contrast = agreement.iloc[1]
    assert int(contrast["rows_clustered"]) < 356_255
    assert "Contrast" in str(contrast["role"])
    assert float(contrast["adjusted_rand_index"]) > float(
        primary_agreement["adjusted_rand_index"]
    ), "the sampled contrast is expected to overstate agreement; if it no longer does, re-read both"

    # 6. Method alternatives must stay documented for every defended decision.
    alternatives = pd.read_csv(P2 / "method_alternatives_register.csv")
    assert_columns(
        alternatives,
        {"decision", "chosen", "alternatives_tested", "evidence",
         "why_rejected", "cost_accepted"},
        "method_alternatives_register.csv",
    )
    assert len(alternatives) >= 6
    assert alternatives.notna().all().all()


def main() -> None:
    validate_feature_governance()
    validate_populations_and_queue()
    validate_rules_and_review_controls()
    validate_reasoning_controls()
    validate_headline_numbers_in_prose()
    validate_presentation_surface()
    print("Business findings validation passed: denominators, routes, claims, and dashboard evidence agree.")


if __name__ == "__main__":
    main()

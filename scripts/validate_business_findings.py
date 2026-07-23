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

SAMPLED_DENSITY_STATES = (
    "Not assessed",
    "Assessed (not isolated)",
    "Assessed (isolated)",
)
OUTLIER_TYPES = (
    "Point (globally extreme single value)",
    "Collective (sampled sparse-density group)",
    "Contextual (unusual multivariate combination)",
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


def expected_sampled_density_states(frame: pd.DataFrame) -> pd.Series:
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
    assert decisions["status"].value_counts().to_dict() == {"keep": 42, "drop": 32}
    assert not decisions["target_used_for_decision"].astype(bool).any()

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
    assert int(lower_intensity["applications"].unique().item()) == 120_294
    close(float(lower_intensity.loc[
        lower_intensity["Evidence source"].eq("Bureau history"), "coverage"
    ].iloc[0]), 0.8139308693700434)
    close(float(lower_intensity.loc[
        lower_intensity["Evidence source"].eq("Previous Home Credit card history"), "coverage"
    ].iloc[0]), 0.12123630438758375)

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
    assert investigation["Sampled Density Corroboration"].isin(SAMPLED_DENSITY_STATES).all()
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
            "dbscan_sample_noise", "extreme_single_axis",
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

    combined["Expected Sampled Density Corroboration"] = expected_sampled_density_states(combined)
    audited = investigation.merge(combined, on="ROW_ID", how="left", validate="one_to_one")
    expected_scope = audited["Queue Route"].map({
        "Detector consensus": "Detector-consensus pattern",
        "Extreme single-axis value": "Portfolio single-axis extreme",
    })
    assert audited["Anomaly Scope"].eq(expected_scope).all()
    audited_extreme = nullable_boolean_series(
        audited["extreme_single_axis"], "extreme_single_axis"
    ).fillna(False)
    audited_noise = nullable_boolean_series(
        audited["dbscan_sample_noise"], "dbscan_sample_noise"
    ).fillna(False)
    expected_type = pd.Series(OUTLIER_TYPES[2], index=audited.index)
    expected_type[audited_noise] = OUTLIER_TYPES[1]
    expected_type[audited_extreme] = OUTLIER_TYPES[0]
    assert audited["Outlier Type"].eq(expected_type).all()
    # Every record beyond 10 SD on a prepared axis is a point outlier, whichever
    # queue route admitted it, so the point count must cover the extreme route.
    assert audited.loc[
        audited["Queue Route"].eq("Extreme single-axis value"), "Outlier Type"
    ].eq(OUTLIER_TYPES[0]).all()
    assert audited["Sampled Density Corroboration"].eq(
        audited["Expected Sampled Density Corroboration"]
    ).all()
    actual_density_counts = investigation["Sampled Density Corroboration"].value_counts()
    expected_density_counts = combined.loc[
        targeted, "Expected Sampled Density Corroboration"
    ].value_counts()
    assert actual_density_counts.reindex(SAMPLED_DENSITY_STATES, fill_value=0).to_dict() == (
        expected_density_counts.reindex(SAMPLED_DENSITY_STATES, fill_value=0).to_dict()
    )
    covered = nullable_boolean_series(
        combined["dbscan_sample_covered"], "dbscan_sample_covered"
    )
    noise = nullable_boolean_series(combined["dbscan_sample_noise"], "dbscan_sample_noise")
    full_density_counts = combined["Expected Sampled Density Corroboration"].value_counts()
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
    assert int(anomaly_summary["N_DBSCAN_SAMPLE_COVERED"]) == int(covered.sum()) == 30_000
    assert int(anomaly_summary["N_DBSCAN_SAMPLE_NOISE"]) == int(
        (covered & noise.fillna(False)).sum()
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
    assert (P2 / "linkage_comparison.png").stat().st_size > 10_000


def main() -> None:
    validate_feature_governance()
    validate_populations_and_queue()
    validate_rules_and_review_controls()
    validate_presentation_surface()
    print("Business findings validation passed: denominators, routes, claims, and dashboard evidence agree.")


if __name__ == "__main__":
    main()

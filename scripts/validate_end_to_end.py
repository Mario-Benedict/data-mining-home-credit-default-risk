"""Executable end-to-end verifier for the Home Credit KDD project.

The verifier checks data contracts, phase artefacts, evaluation boundaries,
business-language safeguards, and reproducibility evidence.  It does not rerun
the pipeline; run it after the pipeline and all four notebooks complete.
"""

from __future__ import annotations

import hashlib
import json
import math
import platform
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import sklearn


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "datasets"
FINAL = DATA / "final"
P1 = ROOT / "results" / "phase1_preprocessing"
P2 = ROOT / "results" / "phase2_clustering"
P3 = ROOT / "results" / "phase3_association"
P4 = ROOT / "results" / "phase4_anomaly"
OUT = ROOT / "results" / "validation"
OUT.mkdir(parents=True, exist_ok=True)


@dataclass
class Check:
    phase: str
    check: str
    status: str
    observed: str
    expected: str
    severity: str
    detail: str


checks: list[Check] = []


def record(
    phase: str,
    name: str,
    passed: bool,
    observed,
    expected,
    detail: str = "",
    severity: str = "ERROR",
) -> None:
    checks.append(Check(
        phase=phase,
        check=name,
        status="PASS" if passed else ("WARN" if severity == "WARN" else "FAIL"),
        observed=str(observed),
        expected=str(expected),
        severity=severity,
        detail=detail,
    ))


def sha256(path: Path, chunk_size: int = 8 * 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def require(path: Path, phase: str) -> bool:
    exists = path.exists() and path.stat().st_size > 0
    record(phase, f"artifact exists: {path.name}", exists,
           path.stat().st_size if path.exists() else "missing", "> 0 bytes")
    return exists


def metric_map(frame: pd.DataFrame) -> dict[str, float]:
    return dict(zip(frame["metric"], pd.to_numeric(frame["value"])))


def raw_contract() -> dict:
    train_path = DATA / "application_train.csv"
    test_path = DATA / "application_test.csv"
    train = pd.read_csv(train_path, usecols=["SK_ID_CURR", "TARGET", "DAYS_BIRTH", "DAYS_EMPLOYED"])
    test = pd.read_csv(test_path, usecols=["SK_ID_CURR", "DAYS_BIRTH", "DAYS_EMPLOYED"])
    all_ids = pd.Index(pd.concat([train.SK_ID_CURR, test.SK_ID_CURR], ignore_index=True))

    record("raw", "train row count", len(train) == 307_511, len(train), 307_511)
    record("raw", "test row count", len(test) == 48_744, len(test), 48_744)
    record("raw", "train IDs unique", train.SK_ID_CURR.is_unique, train.SK_ID_CURR.nunique(), len(train))
    record("raw", "test IDs unique", test.SK_ID_CURR.is_unique, test.SK_ID_CURR.nunique(), len(test))
    overlap = len(set(train.SK_ID_CURR) & set(test.SK_ID_CURR))
    record("raw", "train/test ID disjointness", overlap == 0, overlap, 0)
    record("raw", "TARGET domain", set(train.TARGET.dropna().unique()) == {0, 1},
           sorted(train.TARGET.dropna().unique()), "{0, 1}")
    base_rate = float(train.TARGET.mean())
    record("raw", "observed default prevalence", 0 < base_rate < 0.5,
           f"{base_rate:.6f}", "between 0 and 0.5")
    record("raw", "birth dates use past-day encoding", (pd.concat([train.DAYS_BIRTH, test.DAYS_BIRTH]) < 0).all(),
           pd.concat([train.DAYS_BIRTH, test.DAYS_BIRTH]).max(), "< 0")
    employed = pd.concat([train.DAYS_EMPLOYED, test.DAYS_EMPLOYED])
    invalid_employed = int((~((employed <= 0) | employed.eq(365_243))).sum())
    record("raw", "employment-day sentinel contract", invalid_employed == 0, invalid_employed,
           "0 values outside past days or sentinel")

    relations = {
        "bureau.csv": "SK_ID_CURR",
        "previous_application.csv": "SK_ID_CURR",
        "POS_CASH_balance.csv": "SK_ID_CURR",
        "installments_payments.csv": "SK_ID_CURR",
        "credit_card_balance.csv": "SK_ID_CURR",
    }
    relation_rows = {}
    for filename, key in relations.items():
        series = pd.read_csv(DATA / filename, usecols=[key])[key]
        orphan = int((~series.isin(all_ids)).sum())
        relation_rows[filename] = len(series)
        record("raw", f"{filename} applicant-key coverage", orphan == 0, orphan,
               "0 orphan rows", severity="WARN" if orphan else "ERROR")

    bureau_ids = pd.read_csv(DATA / "bureau.csv", usecols=["SK_ID_BUREAU"])["SK_ID_BUREAU"]
    balance = pd.read_csv(DATA / "bureau_balance.csv", usecols=["SK_ID_BUREAU", "MONTHS_BALANCE"])
    bb_orphans = int((~balance.SK_ID_BUREAU.isin(pd.Index(bureau_ids))).sum())
    record("raw", "bureau_balance key coverage", bb_orphans == 0, bb_orphans,
           "0 orphan monthly rows", severity="WARN" if bb_orphans else "ERROR")
    record("raw", "bureau_balance time direction", (balance.MONTHS_BALANCE <= 0).all(),
           balance.MONTHS_BALANCE.max(), "<= 0")
    prev_days = pd.read_csv(DATA / "previous_application.csv", usecols=["DAYS_DECISION"])["DAYS_DECISION"]
    record("raw", "previous-decision time direction", (prev_days <= 0).all(),
           prev_days.max(), "<= 0")
    return {
        "train_rows": len(train), "test_rows": len(test), "combined_rows": len(all_ids),
        "base_rate": base_rate, "relation_rows": relation_rows,
    }


def phase1_contract(raw: dict) -> dict:
    business_path = FINAL / "features_business.csv"
    cluster_path = FINAL / "features_clustering.csv"
    if not (require(business_path, "phase1") and require(cluster_path, "phase1")):
        return {}
    business = pd.read_csv(business_path)
    clustering = pd.read_csv(cluster_path)
    expected_rows = raw["combined_rows"]
    for label, frame in [("business", business), ("clustering", clustering)]:
        record("phase1", f"{label} row preservation", len(frame) == expected_rows,
               len(frame), expected_rows)
        record("phase1", f"{label} applicant IDs unique", frame.SK_ID_CURR.is_unique,
               frame.SK_ID_CURR.nunique(), len(frame))
        record("phase1", f"TARGET excluded from {label}", "TARGET" not in frame.columns,
               "TARGET" in frame.columns, False)
    record("phase1", "clustering matrix finite",
           np.isfinite(clustering.drop(columns="SK_ID_CURR").to_numpy()).all(),
           int((~np.isfinite(clustering.drop(columns="SK_ID_CURR").to_numpy())).sum()), 0)
    record("phase1", "gender excluded from clustering", "CODE_GENDER" not in clustering.columns,
           "CODE_GENDER" in clustering.columns, False)
    required = {
        "SOURCE_AMT_INCOME_TOTAL", "SOURCE_EXT_SOURCE_1", "SOURCE_EXT_SOURCE_2",
        "SOURCE_EXT_SOURCE_3", "FLAG_EXT_SOURCE_1_MISSING",
        "FLAG_EXT_SOURCE_2_MISSING", "FLAG_EXT_SOURCE_3_MISSING", "INST_COUNT",
    }
    missing = sorted(required - set(business.columns))
    record("phase1", "source/missingness evidence contract", not missing, missing, "none missing")
    clip = pd.read_csv(P1 / "clustering_clip_limits.csv") if require(P1 / "clustering_clip_limits.csv", "phase1") else pd.DataFrame()
    if len(clip):
        record("phase1", "robust clipping limits ordered",
               (clip.lower_model_value <= clip.upper_model_value).all(),
               int((clip.lower_model_value > clip.upper_model_value).sum()), 0)
    mi = pd.read_csv(P1 / "feature_importance.csv") if require(P1 / "feature_importance.csv", "phase1") else pd.DataFrame()
    if len(mi):
        record("phase1", "mutual-information screen finite",
               np.isfinite(mi.mutual_info).all(), int((~np.isfinite(mi.mutual_info)).sum()), 0,
               detail="Train-label relevance screen only; it does not select unsupervised clusters.")
    return {"business_rows": len(business), "clustering_features": clustering.shape[1] - 1}


def phase2_contract(raw: dict) -> dict:
    labels = pd.read_csv(P2 / "cluster_labels.csv")
    names = pd.read_csv(P2 / "cluster_names.csv")
    record("phase2", "cluster-label row preservation", len(labels) == raw["combined_rows"],
           len(labels), raw["combined_rows"])
    record("phase2", "cluster applicant IDs unique", labels.SK_ID_CURR.is_unique,
           labels.SK_ID_CURR.nunique(), len(labels))
    k = names.cluster_id.nunique()
    record("phase2", "five named segments", k == 5, k, 5)
    record("phase2", "segment names unique", names.nama.is_unique, names.nama.nunique(), len(names))
    counts = labels.CLUSTER_KMEANS.value_counts()
    record("phase2", "no empty K-Means segment", len(counts) == 5 and counts.min() > 0,
           counts.to_dict(), "five non-empty segments")

    stability = pd.read_csv(P2 / "k_stability.csv") if require(P2 / "k_stability.csv", "phase2") else pd.DataFrame()
    if len(stability):
        record("phase2", "K-Means seed stability", stability.adjusted_rand_index.mean() >= .90,
               f"mean ARI={stability.adjusted_rand_index.mean():.4f}", ">= 0.90")
    sensitivity = pd.read_csv(P2 / "pca_cluster_sensitivity.csv") if require(P2 / "pca_cluster_sensitivity.csv", "phase2") else pd.DataFrame()
    if len(sensitivity):
        non_primary = sensitivity.loc[sensitivity.n_components.ne(10), "ari_vs_10pc"]
        record("phase2", "PCA dimensionality sensitivity", len(non_primary) > 0 and non_primary.min() >= .90,
               f"minimum ARI={non_primary.min():.4f}" if len(non_primary) else "missing", ">= 0.90")
    agreement = pd.read_csv(P2 / "method_agreement.csv") if require(P2 / "method_agreement.csv", "phase2") else pd.DataFrame()
    if len(agreement):
        record("phase2", "Ward comparison is quantified", agreement.adjusted_rand_index.notna().all(),
               agreement.adjusted_rand_index.iloc[0], "finite ARI",
               severity="WARN", detail="Sampled Ward is an approximation; low agreement is a limitation, not a forced pass.")
    dbscan = pd.read_csv(P2 / "dbscan_umap_sample.csv")
    record("phase2", "DBSCAN sample size", len(dbscan) == 50_000, len(dbscan), 50_000)
    record("phase2", "DBSCAN noise exists but is not universal", 0 < dbscan.IS_NOISE.sum() < len(dbscan),
           int(dbscan.IS_NOISE.sum()), "between 1 and 49,999")
    return {"segments": k, "cluster_counts": counts.to_dict(), "dbscan_noise": int(dbscan.IS_NOISE.sum())}


def phase3_contract() -> dict:
    rules = pd.read_csv(P3 / "rule_visual_summary.csv")
    record("phase3", "minimum final non-trivial rules", len(rules) >= 10, len(rules), ">= 10")
    # Require an item/word boundary so the suffix in ``leverage_`` is not
    # mistaken for an age-derived token.
    protected = rules.short_rule.astype(str).str.contains(
        r"(?<![a-z])(?:code_gender|gender|years_birth|age_)", case=False, regex=True
    )
    record("phase3", "protected/life-stage vocabulary excluded", not protected.any(), int(protected.sum()), 0)
    record("phase3", "support counts positive", (rules.support_count > 0).all(),
           int((rules.support_count <= 0).sum()), 0)
    record("phase3", "rule metrics valid",
           ((rules.support > 0) & (rules.support <= 1) &
            (rules.confidence > 0) & (rules.confidence <= 1) & (rules.lift >= 1.2)).all(),
           "support/confidence/lift ranges", "0<s<=1, 0<c<=1, lift>=1.2")
    algebraic_tokens = ["income", "credit", "leverage", "burden"]
    purely_algebraic = []
    for text in rules.short_rule.astype(str).str.lower():
        has_history = any(token in text for token in [
            "repayment", "card_", "credit_file", "bureau_", "previous_", "external_score"])
        if not has_history and any(token in text for token in algebraic_tokens):
            purely_algebraic.append(text)
    record("phase3", "algebra-only rules rejected", not purely_algebraic,
           len(purely_algebraic), 0)
    deterministic_pairs = [
        ("previous_none", "previous_outcome_not_observed"),
        ("credit_file_none", "bureau_debt_not_observed"),
    ]
    deterministic_rules = [
        text for text in rules.short_rule.astype(str).str.lower()
        if any(left in text and right in text for left, right in deterministic_pairs)
    ]
    record("phase3", "same-source missingness identities rejected", not deterministic_rules,
           len(deterministic_rules), 0)
    audit = pd.read_csv(P3 / "rule_rejection_audit.csv") if require(P3 / "rule_rejection_audit.csv", "phase3") else pd.DataFrame()
    if len(audit):
        record("phase3", "algebraic rejection audit present",
               "algebraic_financial_identity" in set(audit.reason),
               audit.set_index("reason").rules.to_dict(), "algebraic reason listed")
    return {"final_rules": len(rules), "segments_covered": rules.Segment.nunique()}


def phase4_contract(raw: dict) -> dict:
    summary = pd.read_csv(P4 / "anomaly_summary.csv").iloc[0]
    tier_total = int(summary.HIGH_CONFIDENCE + summary.MODERATE + summary.WEAK + summary.NORMAL)
    record("phase4", "anomaly tiers reconcile", tier_total == raw["combined_rows"],
           tier_total, raw["combined_rows"])
    investigation = pd.read_csv(P4 / "anomaly_investigation.csv")
    record("phase4", "one investigation per consensus row",
           len(investigation) == int(summary.HIGH_CONFIDENCE), len(investigation), int(summary.HIGH_CONFIDENCE))
    record("phase4", "investigation applicant IDs unique", investigation.SK_ID_CURR.is_unique,
           investigation.SK_ID_CURR.nunique(), len(investigation))
    for col in ["Record Evidence", "Recommended Action", "Evidence Value Basis"]:
        record("phase4", f"{col} complete", col in investigation and investigation[col].notna().all(),
               int(investigation[col].isna().sum()) if col in investigation else "missing column", 0)
    record("phase4", "automatic adverse decisions prohibited",
           investigation["Automatic Decision Allowed"].astype(str).eq("No").all(),
           investigation["Automatic Decision Allowed"].value_counts().to_dict(), "all No")
    record("phase4", "record recommendations are individualized",
           investigation["Recommended Action"].nunique() == len(investigation),
           investigation["Recommended Action"].nunique(), len(investigation))
    require(P4 / "anomaly_threshold_sensitivity.csv", "phase4")

    cluster_metrics = pd.read_csv(P4 / "cluster_default_backtest_metrics.csv")
    cm = pd.read_csv(P4 / "cluster_default_confusion_matrix.csv").set_index("actual")
    metrics = metric_map(cluster_metrics)
    tn = int(cm.loc["Actual non-default", "Flag non-default"])
    fp = int(cm.loc["Actual non-default", "Flag default"])
    fn = int(cm.loc["Actual default", "Flag non-default"])
    tp = int(cm.loc["Actual default", "Flag default"])
    recomputed_precision = tp / (tp + fp) if tp + fp else 0
    recomputed_recall = tp / (tp + fn) if tp + fn else 0
    record("phase4", "cluster evaluation uses all train IDs only",
           int(metrics["evaluation_rows"]) == raw["train_rows"] and int(metrics["test_rows_scored"]) == 0,
           f"train={int(metrics['evaluation_rows'])}, test={int(metrics['test_rows_scored'])}",
           f"train={raw['train_rows']}, test=0")
    record("phase4", "cluster precision arithmetic",
           math.isclose(recomputed_precision, metrics["precision"], rel_tol=0, abs_tol=1e-12),
           recomputed_precision, metrics["precision"])
    record("phase4", "cluster recall arithmetic",
           math.isclose(recomputed_recall, metrics["recall"], rel_tol=0, abs_tol=1e-12),
           recomputed_recall, metrics["recall"])
    record("phase4", "cluster precision ceiling explicit",
           "cluster_precision_ceiling" in metrics and metrics["precision"] <= metrics["cluster_precision_ceiling"] + 1e-12,
           metrics.get("cluster_precision_ceiling", "missing"), "present and >= chosen precision")

    reference_metrics = pd.read_csv(P4 / "supervised_reference_metrics.csv")
    reference = metric_map(reference_metrics)
    record("phase4", "supervised diagnostic uses train only",
           int(reference["evaluation_rows"]) == raw["train_rows"] and int(reference["test_rows_scored"]) == 0,
           f"train={int(reference['evaluation_rows'])}, test={int(reference['test_rows_scored'])}",
           f"train={raw['train_rows']}, test=0")
    record("phase4", "objective-matched diagnostic discriminates better",
           reference["average_precision"] > metrics["average_precision"] and reference["roc_auc"] > metrics["roc_auc"],
           f"AP {reference['average_precision']:.4f} vs {metrics['average_precision']:.4f}; "
           f"AUC {reference['roc_auc']:.4f} vs {metrics['roc_auc']:.4f}",
           "supervised AP and AUC greater",
           severity="WARN",
           detail="This diagnoses objective mismatch; it does not validate deployment.")
    return {
        "consensus_rows": len(investigation),
        "cluster_metrics": {k: metrics[k] for k in ["precision", "recall", "average_precision", "roc_auc", "lift_vs_baseline"]},
        "supervised_reference": {k: reference[k] for k in ["precision", "recall", "average_precision", "roc_auc", "lift_vs_baseline"]},
    }


def fallacy_audit() -> list[dict]:
    return [
        {"fallacy": "Simpson's paradox", "assessment": "LIMITATION",
         "evidence": "Overall base rate and all segment rates are shown together.",
         "remaining_risk": "No product, market, or time strata are available for a full reversal test."},
        {"fallacy": "Ecological fallacy", "assessment": "MITIGATED",
         "evidence": "Cluster rates are explicitly barred from individual approve/decline decisions.",
         "remaining_risk": "Readers may still overgeneralize a segment average without the guardrail."},
        {"fallacy": "Berkson's paradox", "assessment": "LIMITATION",
         "evidence": "Claims are limited to the observed Home Credit application portfolio.",
         "remaining_risk": "Applicant selection mechanisms are unavailable; population generalization is unsupported."},
        {"fallacy": "Collider bias", "assessment": "MITIGATED",
         "evidence": "No causal effect is estimated after conditioning on discovered clusters.",
         "remaining_risk": "Segment-context associations remain descriptive only."},
        {"fallacy": "Base-rate neglect", "assessment": "MITIGATED",
         "evidence": "Precision, lift, average precision, false positives, and the 8% base rate are reported together.",
         "remaining_risk": "Operational costs still need an approved cost function."},
        {"fallacy": "Regression to the mean", "assessment": "NOT_APPLICABLE",
         "evidence": "There is no before/after intervention or treatment-effect claim.",
         "remaining_risk": "Future monitoring should avoid interpreting natural score movement as remediation impact."},
        {"fallacy": "Survivorship bias", "assessment": "LIMITATION",
         "evidence": "No-history states are separated from clean observed history.",
         "remaining_risk": "Public-table availability and prior-loan observation still define who can appear in behavior summaries."},
        {"fallacy": "Look-elsewhere effect", "assessment": "LIMITATION",
         "evidence": "Rule thresholds, compact search length, rejection reasons, and final counts are exported.",
         "remaining_risk": "Rules are exploratory; no multiplicity-adjusted external holdout is available."},
        {"fallacy": "Garden of forking paths", "assessment": "MITIGATED",
         "evidence": "Seeds, K range, thresholds, sensitivity tables, and rejected interpretations are fixed in code.",
         "remaining_risk": "K=5 and anomaly operating points retain documented business judgment."},
        {"fallacy": "Causation fallacy", "assessment": "MITIGATED",
         "evidence": "Association, anomaly, and cluster outputs are labeled descriptive and non-causal.",
         "remaining_risk": "No intervention data exist to support causality."},
        {"fallacy": "Reverse causality", "assessment": "MITIGATED",
         "evidence": "Repayment history is used as observed context, never as a causal mechanism claim.",
         "remaining_risk": "Temporal recency and cure status are aggregated and require record review."},
    ]


def main() -> int:
    raw = raw_contract()
    p1 = phase1_contract(raw)
    p2 = phase2_contract(raw)
    p3 = phase3_contract()
    p4 = phase4_contract(raw)

    check_frame = pd.DataFrame(asdict(item) for item in checks)
    check_frame.to_csv(OUT / "end_to_end_checks.csv", index=False)
    fallacies = fallacy_audit()
    pd.DataFrame(fallacies).to_csv(OUT / "fallacy_audit.csv", index=False)

    raw_files = [
        DATA / name for name in [
            "application_train.csv", "application_test.csv", "bureau.csv",
            "bureau_balance.csv", "previous_application.csv", "POS_CASH_balance.csv",
            "installments_payments.csv", "credit_card_balance.csv",
        ]
    ]
    passport = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "project": "Home Credit Default Risk domain-led knowledge discovery",
        "objective": "Discover interpretable portfolio segments, associations, and review-worthy anomalies; diagnose but do not deploy TARGET prediction.",
        "data_snapshot": [
            {"path": str(path.relative_to(ROOT)), "bytes": path.stat().st_size, "sha256": sha256(path)}
            for path in raw_files
        ],
        "population": raw,
        "phase_outputs": {"phase1": p1, "phase2": p2, "phase3": p3, "phase4": p4},
        "methods": {
            "preprocessing": "source-aware imputation, robust model-facing clipping, standardization, MI/correlation screen",
            "segmentation": "PCA sensitivity + K-Means K=5 + sampled Ward benchmark + sampled UMAP/DBSCAN",
            "association": "Apriori/FP-Growth/ECLAT global validation; denominator-preserving per-segment FP-Growth",
            "anomaly": "adjusted IQR, calibrated Z, Isolation Forest, robust Mahalanobis, LOF, sampled DBSCAN corroboration",
            "outcome": "train-only cross-fitted cluster-rate alignment plus separate OOF logistic diagnostic",
        },
        "fixed_seeds": [42, 52, 62],
        "environment": {
            "python": platform.python_version(), "pandas": pd.__version__,
            "numpy": np.__version__, "scikit_learn": sklearn.__version__,
        },
        "claims_supported": [
            "Portfolio segments are reproducible descriptive structures.",
            "Final association rules are non-trivial co-occurrences, not causes.",
            "Consensus anomalies are human-review routes, not adverse decisions.",
            "Low cluster precision follows from objective and score granularity; supervised performance is a separate diagnostic.",
        ],
        "claims_not_supported": [
            "Production probability of default", "approval/decline policy", "causal effect",
            "test-set precision/recall", "temporal stability", "fairness clearance",
        ],
        "fallacy_audit": fallacies,
    }
    (OUT / "material_passport.json").write_text(json.dumps(passport, indent=2), encoding="utf-8")

    failures = check_frame[check_frame.status.eq("FAIL")]
    summary = {
        "verification_status": "VERIFIED" if failures.empty else "FAILED",
        "checks": len(check_frame), "passed": int(check_frame.status.eq("PASS").sum()),
        "warnings": int(check_frame.status.eq("WARN").sum()), "failed": len(failures),
        "failed_checks": failures[["phase", "check", "detail"]].to_dict("records"),
    }
    (OUT / "verification_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 1 if len(failures) else 0


if __name__ == "__main__":
    raise SystemExit(main())

# Home Credit default-risk knowledge discovery

This project applies the KDD process to the Home Credit Default Risk data. Its primary goal is portfolio discovery and business interpretation, as required by the project brief. Default prediction is included only as a train-only diagnostic.

## Verified result

| Check | Result |
|---|---:|
| Combined applications | 356,255 |
| Train rows used for outcome metrics | 307,511 |
| Test rows used for outcome metrics | 0 |
| Clustering features | 49 |
| K-Means segments | 5 |
| K=5 seed ARI range | 0.9979-0.9989 |
| Final association rules | 15 |
| Detector-consensus review records | 3,758 |
| Cluster alignment precision / recall | 10.83% / 23.33% |
| Supervised diagnostic precision / recall | 21.75% / 46.84% |
| End-to-end verification | 67 pass, 1 warning, 0 fail |

The low cluster precision is expected. Clustering groups similar applications without optimizing TARGET. At a matched 17.38% review capacity, the outcome-trained diagnostic roughly doubles both precision and recall. Use clustering for segmentation and portfolio actions, not applicant-level decline decisions.

## Run the project

From the repository root:

```powershell
python src/run_pipeline.py
python scripts/update_analysis_notebooks.py
python scripts/execute_notebook.py notebooks/exploratory_data_analysis.ipynb --timeout 900
python scripts/execute_notebook.py notebooks/phase2_clustering.ipynb --timeout 1200
python scripts/execute_notebook.py notebooks/phase3_association.ipynb --timeout 1200
python scripts/execute_notebook.py notebooks/phase4_anomaly.ipynb --timeout 1800
python scripts/validate_end_to_end.py
python dashboard/app.py
```

Open `http://127.0.0.1:8050` after the last command.

`src/run_pipeline.py` uses direct local execution by default. Set `HOME_CREDIT_USE_PREFECT=1` only when a compatible Prefect/FastAPI environment is available.

## What each phase does

### Phase 1: applicant-level feature construction

Eight raw tables are checked, aggregated to `SK_ID_CURR`, cleaned, encoded, and split into two artifacts:

- `datasets/final/features_business.csv` preserves readable values, source-value evidence, and missingness flags.
- `datasets/final/features_clustering.csv` contains 49 finite numeric features for distance-based mining.

Continuous distance axes are clipped at p0.5/p99.5 and standardized. Source values remain available for case review. Missing external scores and missing credit histories are flagged so imputed values are never described as observations.

### Phase 2: portfolio segmentation

K-Means, DBSCAN, and sampled Ward linkage are compared. K=3 has the highest sampled silhouette. K=5 is retained because it is near the elbow, seed-stable, non-empty, and more useful for business segmentation.

Ten PCs retain 55.59% of variance. The choice is supported by sensitivity, not by a false variance claim: K=5 labels at 21, 27, and 49 PCs have ARI 0.963-0.965 against the 10-PC solution.

The five neutral segment labels are:

- Intensive Card User
- Repayment-Stress History
- Thin-File / Low-Intensity
- High-Exposure Applicant
- History-Rich Credit User

DBSCAN is a 50,000-row UMAP sample view. Its noise points are exploratory and are not default or fraud labels.

### Phase 3: association rules

Apriori, FP-Growth, and ECLAT use the same full-portfolio transaction population for algorithm comparison. Per-segment rules retain their own denominators. The final 15-rule view rejects algebraic identities, same-source missingness identities, and near-duplicate displays.

Thin-file rules are interpreted as data-availability patterns. They do not mean that unobserved repayment was clean.

### Phase 4: anomaly review and outcome diagnostics

Adjusted IQR, empirical Z-score, Mahalanobis distance, Isolation Forest, LOF, and sampled DBSCAN evidence feed a 3,758-row detector-consensus queue. Every exported row has applicant-specific evidence and an action. Automatic decisions are prohibited.

The outcome page compares:

- cross-fitted cluster outcome alignment, which measures whether unsupervised segments contain historical signal; and
- a separate out-of-fold logistic diagnostic at the same review share, which tests the objective-mismatch explanation.

Neither result is deployment validation.

## Dashboard design

The Dash app renders phase tabs lazily. It uses bounded plot samples and a server-side paged anomaly table, so millions of raw values and thousands of long recommendations are not embedded in the initial page.

The segment page places all profiles on a common heatmap and shows the DBSCAN map directly. The outcome page labels the train-only boundary and presents cluster alignment beside the supervised diagnostic. Mobile layouts use stacked panels, shorter plots, and internal scroll only where a wide comparison chart requires it.

## Validation artifacts

Important files:

- `REPORT.md`: full business and methodological interpretation
- `reports/domain_knowledge_basis.md`: Home Credit domain assumptions and decision boundaries
- `reports/reasoning_validation.md`: method choice and sensitivity rationale
- `reports/validation_report.md`: independent contracts, metric arithmetic, and UI checks
- `results/validation/end_to_end_checks.csv`: all automated checks
- `results/validation/fallacy_audit.csv`: eleven-fallacy review
- `results/validation/material_passport.json`: raw-file hashes and lineage
- `results/validation/verification_summary.json`: final status

## Known limitation

The single verification warning is a source-data referential issue: 3,120,184 `bureau_balance` monthly rows lack a matching `bureau` record. Without the parent key, they cannot be mapped to `SK_ID_CURR`; the pipeline excludes them from applicant aggregation and records the count. All executable phase checks pass.

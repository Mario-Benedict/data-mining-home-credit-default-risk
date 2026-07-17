# Home Credit default-risk knowledge discovery report

## Decision summary

The workflow is suitable for the assignment's stated purpose: discovering and interpreting portfolio structure. It is not a production default-prediction system.

The earlier low precision did not show that the entire process was wrong. It showed that an unsupervised cluster label is too coarse for applicant-level default prediction. In the verified run, cluster outcome alignment reaches 10.83% precision and 23.33% recall at a 17.38% review share. A separate train-only, out-of-fold logistic diagnostic reaches 21.75% precision and 46.84% recall at the same capacity. The difference comes from the objective: clustering optimizes similarity; logistic regression optimizes outcome separation.

The discovery pipeline now passes 67 of 68 independent checks. One raw-data warning remains: 3,120,184 of 27,299,925 `bureau_balance` rows have no matching `bureau` parent and cannot be mapped to an applicant. They are excluded from applicant aggregation and recorded in the validation material rather than silently imputed.

## Scope and evaluation boundary

| Population | Rows | Permitted use |
|---|---:|---|
| Combined train and test | 356,255 | Unlabeled, transductive discovery and portfolio profiling |
| Labeled train | 307,511 | Train-only outcome diagnostics |
| Unlabeled test | 48,744 | Discovery only; never enters precision, recall, lift, AUC, or calibration metrics |

The observed train default rate is 8.07%. This base rate must accompany every precision or lift statement. A precision of 10.83% is only 1.34 times the base rate, even though it is above random selection.

## Phase 1: data construction and preprocessing

### Why combine the tables

The application row alone does not describe credit behavior. Bureau, previous-application, POS, installment, and credit-card histories are aggregated to `SK_ID_CURR`. Counts, recency, delinquency, utilization, approval history, and payment ratios give each application a portfolio context.

Train and test are combined only after a source flag is preserved. This is acceptable for the assignment's unlabeled discovery setting. It would not be a valid way to estimate deployment performance for a supervised model.

### Missingness

Missing values have different business meanings:

- No matched history is retained through flags such as `FLAG_NO_BUREAU` and `INST_COUNT`, because no history is not the same as clean history.
- Missing external scores have their own flags. Median-filled values support computation but are never presented as observed scores in a case explanation.
- Housing fields use an explicit no-record indicator. Zero-filled model values mean no recorded detail, not a literal zero-sized property.
- The `DAYS_EMPLOYED=365243` sentinel is separated from genuine employment duration.

### Outliers and scaling

Financial amounts and behavior ratios are skewed. Log transforms reduce scale compression for positive amounts. Continuous distance axes are clipped at the 0.5th and 99.5th percentiles before standardization so a handful of extreme files cannot consume K-Means centroids.

The original values are preserved in `SOURCE_*` columns. Clustering sees the robust model values; anomaly reviewers see the source values and whether a value was observed, capped, or imputed.

The final artifacts contain 64 readable business/audit columns and 49 clustering features. Binary flags remain 0/1. Continuous and ordinal axes are standardized. Mutual information is computed against train TARGET only as a feature relevance check, not as a clustering input. One pair exceeds absolute correlation 0.85: mean and maximum card utilization, at 0.892.

## Phase 2: segmentation

### PCA and K-Means

Ten principal components retain 55.59% of variance. Component 11 adds 2.72 percentage points, so the old "0.08 percentage point" justification was wrong and has been removed.

Ten components remain the compact primary view because the K=5 labels are stable when more dimensions are retained:

| Components | Variance retained | Silhouette | ARI versus 10 PCs |
|---:|---:|---:|---:|
| 10 | 55.59% | 0.144 | 1.000 |
| 21 | 81.25% | 0.087 | 0.965 |
| 27 | 90.77% | 0.073 | 0.963 |
| 49 | 100.00% | 0.063 | 0.963 |

K=3 has the highest sampled silhouette, 0.250. K=5 is retained as a business-resolution choice near the elbow, not as the universal statistical optimum. It produces five non-empty, interpretable segments; the smallest is 2.18% and the largest is 34.42% in the evaluation sample. Across seeds 42, 52, and 62, pairwise adjusted Rand indices range from 0.9979 to 0.9989.

### Segment profiles

| Segment | Applications | Median income | Median credit | Credit/income | Annuity/income | Median installment late share |
|---|---:|---:|---:|---:|---:|---:|
| Intensive Card User | 54,535 | 157,500 | 544,491 | 3.26x | 15.66% | 3.98% |
| Repayment-Stress History | 7,637 | 135,000 | 497,520 | 3.36x | 17.32% | 28.57% |
| Thin-File / Low-Intensity | 121,820 | 135,000 | 269,550 | 2.11x | 13.17% | 0.00% observed median |
| High-Exposure Applicant | 119,937 | 157,500 | 814,041 | 5.27x | 21.97% | 0.00% observed median |
| History-Rich Credit User | 52,326 | 166,500 | 454,500 | 2.67x | 14.52% | 5.08% |

These names describe dominant portfolio geometry. They are not character judgments or decision labels.

- Intensive Card User: review utilization, balances, arrears, and limit suitability before changing exposure.
- Repayment-Stress History: review lateness recency, severity, cure status, and current affordability. Existing hardship actions must follow policy.
- Thin-File / Low-Intensity: distinguish absent information from good behavior and request permitted alternative evidence when needed.
- High-Exposure Applicant: verify sustainable income, total obligations, and stressed affordability.
- History-Rich Credit User: use the larger history to reconcile current obligations; do not assume current capacity from depth alone.

### DBSCAN and hierarchical sensitivity

DBSCAN is run on a reproducible, distribution-checked 50,000-row UMAP sample. It marks 914 points as density noise. UMAP can distort global distance and density, so this result is an exploratory view, not a full-population default, fraud, or anomaly label.

Ward linkage is fit on a sample, then extended by nearest-center assignment. Its agreement with K-Means is ARI 0.719 and NMI 0.726. This is useful corroboration, but not proof that the methods found the same partition.

## Phase 3: association rules

The transaction vocabulary uses domain bins for income, requested credit, leverage, repayment burden, external-score availability, installment behavior, card utilization, bureau depth/debt, previous-application depth/outcome, and cluster membership.

Rules use a maximum itemset length of three and a single consequent. Every exported rule includes support count, support, confidence, lift, and the correct population denominator. Global Apriori, FP-Growth, and ECLAT agreement is compared only on the same full-portfolio transactions. Per-segment FP-Growth is labeled separately.

The final table contains 15 rules, three per segment. The selection rejects:

- purely algebraic income/credit/leverage/burden identities;
- same-source missingness identities such as `previous_none -> previous_outcome_not_observed`;
- compactness violations and rules without behavior or history context; and
- near-duplicate displays with the same antecedent.

High-lift thin-file rules are data-availability findings. They show that missing histories co-occur across independent tables; they do not show clean repayment. Behavioral rules cover card utilization, serious lateness, prior refusals, leverage, and burden. The dashboard links each displayed rule to a review action rather than treating lift as a decline rule.

## Phase 4: anomaly review

Six signals are available across the workflow: adjusted IQR, empirical Z-score, Mahalanobis distance, Isolation Forest, Local Outlier Factor, and sampled DBSCAN noise. Only the 50,000 DBSCAN sample has all six; other rows have five. The agreement denominator is therefore record-specific.

| Category | Records | Share of portfolio |
|---|---:|---:|
| Detector consensus, at least 3 signals and at least 50% agreement | 3,758 | 1.05% |
| Moderate, 2 signals | 5,431 | 1.52% |
| Weak, 1 signal | 20,532 | 5.76% |
| No detector flag | 326,534 | 91.66% |

DBSCAN corroborates 22 consensus records. "Consensus" refers to unusualness agreement, not a calibrated probability of default.

Each of the 3,758 review rows contains the applicant ID, actual evidence values, value basis, primary and supporting drivers, business interpretation, review priority, and a specific next action. All rows state `Automatic Decision Allowed = No`.

Threshold sensitivity is material. Conventional 1.5x IQR flags 67,522 rows, while the adjusted multicolumn IQR rule flags 1,158. Isolation Forest ranges from 3,563 to 35,626 flags as contamination moves from 1% to 10%. These differences are why detector agreement and human evidence review are required.

## Outcome alignment and the low precision question

### Cluster outcome alignment

The cluster diagnostic uses five out-of-fold splits. For each fold, train-only segment rates are learned from the other four folds and compared with that fold's baseline. Test IDs are excluded.

| Metric | Verified result |
|---|---:|
| Evaluation rows | 307,511 |
| Flagged share | 17.38% |
| Precision | 10.83% |
| Recall | 23.33% |
| Lift over 8.07% base rate | 1.34x |
| Average precision | 9.53% |
| ROC AUC | 0.557 |
| True positive / false positive | 5,791 / 47,657 |
| False negative / true negative | 19,034 / 235,029 |

The full-segment precision ceiling is 11.91%, the highest observed default rate among complete segments. This is the central reason cluster precision stays low: every member of a selected segment receives the same broad risk treatment even though most members did not default.

### Objective-matched supervised diagnostic

A separate logistic regression uses five-fold out-of-fold train predictions and the same 17.38% review share. Direct age, education, income-type frequency, organization-type frequency, and region-rating proxies are excluded from this diagnostic. This is a methodological reference, not a deployment model.

| Metric | Logistic diagnostic |
|---|---:|
| Precision | 21.75% |
| Recall | 46.84% |
| Lift | 2.69x |
| Average precision | 23.33% |
| ROC AUC | 0.751 |
| Brier score | 0.0683 |

The improvement confirms an objective mismatch. Clustering still has value for portfolio strategy, communication, and review design. It should not be used as the applicant-level default model.

## Governance and statistical interpretation

The verifier checks Simpson's paradox, ecological fallacy, Berkson's paradox, collider bias, base-rate neglect, regression to the mean, survivorship bias, the look-elsewhere effect, the garden of forking paths, causation, and reverse causality.

The main unresolved limits are straightforward:

- The public extract does not contain product, market, or calendar strata for a full Simpson reversal test.
- Home Credit's applicant-selection mechanism is unknown, so results cannot be generalized to all consumers.
- Association rules are exploratory and do not have a multiplicity-adjusted external holdout.
- No intervention data support causal claims.
- A deployable predictive model would still need temporal validation, calibration, cost-sensitive thresholding, fairness analysis, governance approval, and drift monitoring.

## Reproducibility

Run from the project root:

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

The verification outputs are in `results/validation/`. `material_passport.json` records the eight raw-file hashes, software environment, row contracts, and artifact lineage. `verification_summary.json` reports `VERIFIED`, 68 checks, 67 passes, one warning, and zero failures.

## Final interpretation

The corrected process is sound for knowledge discovery. It finds stable and usable portfolio segments, denominator-safe association patterns, and a conservative record-level anomaly queue. It also gives a clear negative result: cluster membership is not accurate enough for individual default decisions. That boundary is part of the analysis, not a defect to hide.

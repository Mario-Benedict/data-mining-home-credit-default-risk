# End-to-end validation report

Validation date: 2026-07-16

## Final status

`VERIFIED`

| Measure | Result |
|---|---:|
| Independent checks | 68 |
| Passed | 67 |
| Warnings | 1 |
| Failed | 0 |
| Notebooks executed without cell errors | 4 of 4 |
| Raw files hashed in material passport | 8 |

The machine-readable results are in:

- `results/validation/end_to_end_checks.csv`
- `results/validation/fallacy_audit.csv`
- `results/validation/material_passport.json`
- `results/validation/verification_summary.json`

## Reproduction performed

The verification run executed these steps from the project root:

1. Full applicant-level preprocessing and feature selection.
2. Notebook regeneration followed by code-cell parsing.
3. Phase 1 exploratory analysis.
4. Phase 2 clustering.
5. Phase 3 association mining.
6. Phase 4 anomaly and outcome diagnostics.
7. Independent contract and fallacy checks.
8. Live dashboard HTTP, callback, desktop, and mobile tests.

The local runner bypasses Prefect's temporary API by default. The installed Prefect/FastAPI pair could not start a compatible temporary server, so relying on Prefect would have blocked reproducibility before any data step ran. The direct path calls the same deterministic step functions.

## Raw material passport

The passport records SHA-256 hashes, byte sizes, and row/column contracts for:

- `application_train.csv`
- `application_test.csv`
- `bureau.csv`
- `bureau_balance.csv`
- `previous_application.csv`
- `POS_CASH_balance.csv`
- `installments_payments.csv`
- `credit_card_balance.csv`

Train and test contain 307,511 and 48,744 unique application IDs. Their union is 356,255, with no overlap. All applicant-level outputs retain 356,255 unique IDs.

### The one warning

`bureau_balance.csv` contains 3,120,184 monthly rows whose `SK_ID_BUREAU` has no parent record in `bureau.csv`. This is 11.43% of the monthly table. Without the parent record, those rows cannot be mapped to `SK_ID_CURR`.

The pipeline excludes these orphan months from applicant aggregation and records the count. It does not guess an applicant ID or impute a bureau relationship. This warning limits completeness but does not break applicant-key integrity.

## Phase 1 contracts

| Check | Result |
|---|---|
| Business artifact | 356,255 rows, 64 columns |
| Clustering artifact | 356,255 rows, ID plus 49 features |
| Duplicate applicant IDs | 0 |
| Non-finite clustering values | 0 |
| TARGET in clustering matrix | No |
| Gender in clustering matrix | No |
| Source-value audit columns in distance matrix | No |
| Source-value audit columns in business artifact | Yes |
| External-score missingness flags | Present |
| Continuous robust clipping | 37 axes, p0.5/p99.5 |
| Correlation pairs above 0.85 | 1 |

The single high-correlation pair is mean versus maximum card utilization, absolute correlation 0.892. It remains documented because the two measures have different business meanings.

The mutual-information check uses 307,511 train IDs aligned by `SK_ID_CURR`. Standardized ordinal values are factorized in a temporary estimator copy so discrete entropy estimation is methodologically valid.

## Phase 2 contracts

### K selection and stability

K=3 has the highest sampled silhouette, 0.250. K=5 has silhouette 0.140 and is retained for business resolution. Its smallest sampled segment share is 2.18%; its largest is 34.42%.

Pairwise adjusted Rand indices across seeds are:

| Seeds | ARI |
|---|---:|
| 42 vs 52 | 0.997876 |
| 42 vs 62 | 0.998086 |
| 52 vs 62 | 0.998911 |

### PCA sensitivity

| Components | Retained variance | ARI versus 10 PCs |
|---:|---:|---:|
| 10 | 55.59% | 1.000 |
| 21 | 81.25% | 0.965 |
| 27 | 90.77% | 0.963 |
| 49 | 100.00% | 0.963 |

The old statement that PC11 added 0.08 percentage points was rejected. PC11 adds 2.72 points.

### Method sensitivity

Sampled Ward nearest-center assignment versus K-Means has ARI 0.719 and NMI 0.726. The report labels this an approximation and a moderate agreement result.

DBSCAN has exactly 50,000 sampled rows and 914 noise points. The exported sample validation compares every clustering feature mean with the full portfolio. DBSCAN remains labeled a sampled UMAP density diagnostic.

### Segment lineage

| Cluster | Neutral label | Applications |
|---:|---|---:|
| 0 | Intensive Card User | 54,535 |
| 1 | Repayment-Stress History | 7,637 |
| 2 | Thin-File / Low-Intensity | 121,820 |
| 3 | High-Exposure Applicant | 119,937 |
| 4 | History-Rich Credit User | 52,326 |

Names are written to both the result and final-dataset locations. The dashboard reads the shared result artifact.

## Phase 3 contracts

| Check | Result |
|---|---:|
| Final rules | 15 |
| Rules per segment | 3 |
| Minimum lift | At least 1.2 |
| Non-positive support counts | 0 |
| Protected/life-stage vocabulary | 0 |
| Pure algebraic rules | 0 |
| Same-source missingness identities | 0 |

The verified rejection audit contains 565 algebraic financial identities and 279 same-source missingness identities. The selector also prevents two displayed rules from using an identical antecedent within the same segment.

Global algorithm agreement uses the same full-portfolio transactions for Apriori, FP-Growth, and ECLAT. Per-segment FP-Growth retains its segment denominator and is not counted as independent global confirmation.

## Phase 4 anomaly contracts

| Category | Records |
|---|---:|
| At least 3 detectors and at least 50% available-detector agreement | 3,758 |
| Two detectors | 5,431 |
| One detector | 20,532 |
| No detector flag | 326,534 |

The review CSV contains 3,758 rows and 3,758 unique applicants. Required fields are complete:

- source-based record evidence;
- evidence-value basis;
- detector names and available-detector scope;
- business interpretation;
- review priority and owner;
- applicant-specific recommended action; and
- `Automatic Decision Allowed = No`.

Review-owner components are deduplicated. For the tested applicant 100221, the live dashboard shows observed installment, bureau, and card evidence; a multi-step human action; owners `Credit Review / Customer Assistance / Revolving Credit Review`; and no automatic decision permission.

## Outcome metric reconstruction

### Cluster outcome alignment

Only train IDs enter the confusion matrix:

| Actual / flag | Not flagged | Flagged | Total |
|---|---:|---:|---:|
| Actual non-default | 235,029 | 47,657 | 282,686 |
| Actual default | 19,034 | 5,791 | 24,825 |
| Total | 254,063 | 53,448 | 307,511 |

Recomputed metrics:

- flagged share = 53,448 / 307,511 = 17.38%;
- precision = 5,791 / 53,448 = 10.83%;
- recall = 5,791 / 24,825 = 23.33%;
- specificity = 235,029 / 282,686 = 83.14%; and
- lift = 10.83% / 8.07% = 1.34x.

Average precision is 9.53% and ROC AUC is 0.557. The highest complete-segment default rate is 11.91%, recorded as the cluster precision ceiling.

### Supervised diagnostic

The five-fold logistic reference uses 307,511 train rows and zero test rows. Its flagged share is matched to 17.38%.

| Metric | Cluster alignment | Logistic diagnostic |
|---|---:|---:|
| Precision | 10.83% | 21.75% |
| Recall | 23.33% | 46.84% |
| Lift | 1.34x | 2.69x |
| Average precision | 9.53% | 23.33% |
| ROC AUC | 0.557 | 0.751 |

The comparison passes the objective-mismatch check. It is not marked as deployment validation.

## Statistical-fallacy audit

All eleven required items are present in `fallacy_audit.csv`:

| Fallacy | Assessment |
|---|---|
| Simpson's paradox | Limitation |
| Ecological fallacy | Mitigated |
| Berkson's paradox | Limitation |
| Collider bias | Mitigated |
| Base-rate neglect | Mitigated |
| Regression to the mean | Not applicable |
| Survivorship bias | Limitation |
| Look-elsewhere effect | Limitation |
| Garden of forking paths | Mitigated |
| Causation fallacy | Mitigated |
| Reverse causality | Mitigated |

Limitations remain visible rather than being forced into a pass state.

## Dashboard verification

### Payload and lazy rendering

| Measurement | Old dashboard | Final dashboard |
|---|---:|---:|
| Initial `/_dash-layout` payload | 6,724,465 bytes | 2,686 bytes |
| Anomaly records embedded at initial load | Thousands of long-form rows | 0 |
| Phase plots embedded at initial load | All | Active tab only |

The final dependencies endpoint returns HTTP 200 and 1,472 bytes. The root and layout endpoints return HTTP 200.

### Desktop, 1440x900

- Document width: 1,425px inside a 1,440px viewport; no horizontal page overflow.
- Outcome metric-card widths: 318px each.
- Wide outcome plots: 1,274x380px.
- Two-column plots: 611x380px.
- Segment comparison plot: 1,274x455px.
- The content begins directly after the navigation. A Dash internal `.tab-content` name collision that previously inserted a 620px blank block was removed.
- Browser console: no messages, warnings, or errors in the final clean tab.

### Mobile, 390x844

- Document width: 375px inside a 390px viewport; no horizontal page overflow.
- Navigation client and scroll widths: both 351px; all five tabs fit.
- Metric cards: 169px in the two-column grid.
- Standard plots: 319x325px; tall plots: 319x365px.
- Segment cards: 347px and stacked.
- Wide heatmaps use local scroll containers at 600-720px; the document itself does not overflow.
- Anomaly DataTable: 486px high, 10 data rows per page, and local 1,092px horizontal sheet width.
- Tab changes set the new content top to 47px, exactly below the 47px sticky navigation.
- The detector count label `17,813` is fully visible after x-axis headroom was added.

### Callback checks

- Anomaly row selection loads record-specific detail.
- Segment text filter `Intensive Card User` reduces pagination from 376 to 51 pages; all ten visible rows match.
- Applicant ID custom sort returns ascending IDs beginning 101048, 101405, 102551, and 102934.
- The parser accepts the `scontains` token emitted by the installed Dash DataTable version.

## Final validation judgment

The executable workflow, regenerated notebooks, CSV lineage, metric arithmetic, and responsive dashboard agree. The project is verified for the assignment's discovery and interpretation scope. Cluster outcome alignment is explicitly too weak for applicant decisions, and the supervised comparison is explicitly not production validation.

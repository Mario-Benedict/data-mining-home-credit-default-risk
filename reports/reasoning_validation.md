# Method reasoning and sensitivity review

## Overall judgment

The corrected workflow is coherent for unsupervised knowledge discovery. Its predictive result is weak because prediction was not the optimization target. The separate supervised reference confirms that distinction at matched review capacity.

## Decision log

| Decision | Method used | Why it fits | Main limitation |
|---|---|---|---|
| Applicant grain | Aggregate histories to `SK_ID_CURR` | Aligns all evidence with the application decision unit | Event sequence and account-level detail are compressed |
| Discovery population | Combine train and test with a source flag | Uses the full unlabeled portfolio requested by the assignment | Transductive result; not a future deployment estimate |
| Missing histories | Flags plus count features | Preserves the difference between absent and clean evidence | Source linkage can still be incomplete |
| Extreme values | p0.5/p99.5 clipping on continuous distance axes | Prevents a few files from capturing centroids | Tail geometry is compressed in the model view |
| Business evidence | Preserve `SOURCE_*` values | Keeps record explanations factual | Larger business artifact |
| Scaling | Standardize continuous/ordinal axes; keep flags binary | Euclidean methods need comparable scales | Standardization does not make every axis equally meaningful |
| Dimensionality | 10-PC primary view with 21/27/49-PC sensitivity | Compact and highly label-consistent | Retains 55.59%, so details are lost |
| Segment count | K=5 | Near elbow, stable, non-empty, interpretable | K=3 has the best silhouette |
| Alternative clustering | Sampled Ward and DBSCAN/UMAP | Tests structural sensitivity and density shape | Neither is an exact full-data alternative |
| Rule mining | Apriori, FP-Growth, ECLAT; segment FP-Growth | Meets assignment and checks algorithm agreement | Search is exploratory and multiplicity remains |
| Anomaly review | Multiple detectors plus evidence logic | Reduces dependence on one assumption | Agreement is not calibrated risk |
| Outcome check | Five-fold cluster-rate cross-fitting | Avoids using each fold's TARGET to score itself | Only broad segment-rate scores are available |
| Objective comparison | Five-fold logistic OOF at matched capacity | Tests whether low score is an objective mismatch | Still lacks time-based external validation |

## PCA validation

The previous PCA explanation was incorrect. The verified cumulative variance is 55.59% at 10 components, 81.25% at 21, 90.77% at 27, and 100% at 49. PC11 contributes 2.72 percentage points.

Ten components are kept because the segmentation changes little when more components are used. ARI versus the 10-PC solution is 0.965 at 21 PCs, 0.963 at 27, and 0.963 at 49. The compact solution also has the best silhouette among these dimensionality choices.

This is a sensitivity argument. It is not a claim that 55.59% captures all credit-risk information.

## K selection validation

| K | Silhouette | Davies-Bouldin | Smallest share | Largest share |
|---:|---:|---:|---:|---:|
| 2 | 0.236 | 1.809 | 17.30% | 82.70% |
| 3 | 0.250 | 1.478 | 2.28% | 80.75% |
| 4 | 0.139 | 1.848 | 2.22% | 42.73% |
| 5 | 0.140 | 1.787 | 2.18% | 34.42% |
| 6 | 0.144 | 1.644 | 1.29% | 34.21% |

K=3 is the strongest compact geometric split. K=5 provides two additional, interpretable operational profiles without creating an empty or vanishing segment. Pairwise seed ARI is 0.9979-0.9989. The report therefore calls K=5 a business-resolution choice. Claiming that it is the statistical winner would be wrong.

## Robust clipping validation

Unclipped sampling showed that a handful of extreme files could consume centroids and reduce seed agreement to about ARI 0.73. The p0.5/p99.5 model-facing clip raised sampled seed agreement to roughly 0.99-1.00. The source values remain intact for review.

This change improves the stability of Euclidean segmentation. It does not license deleting or rewriting the underlying applicant evidence.

## Alternative clustering validation

Sampled Ward nearest-center assignment has ARI 0.719 and NMI 0.726 against K-Means. The agreement is meaningful but incomplete. Ward is therefore a sensitivity check, not confirmation of a single true segmentation.

DBSCAN uses a representative 50,000-row sample and UMAP coordinates. Sample-to-portfolio standardized mean gaps are all small in the exported audit. DBSCAN finds 914 noise points. Because UMAP changes geometry and density, the notebook and dashboard label the result exploratory.

## Association-rule validation

Global algorithm comparison uses the same 356,255 transactions. Segment rules use their actual segment counts. The project no longer averages metrics across different populations or counts per-segment FP-Growth as a fourth confirming algorithm.

The final selector rejects 565 algebraic identities and 279 same-source missingness identities in the verified run. Fifteen rules remain. Rules with unobserved histories are presented as information-availability patterns. Behavioral rules include utilization, lateness, refusals, leverage, and burden.

The remaining statistical limitation is multiple search. Support, confidence, lift, itemset length, rejection counts, and selected rules are all exported, but there is no external holdout for rule discovery.

## Anomaly validation

Detector thresholds behave very differently:

| Setting | Records | Portfolio share |
|---|---:|---:|
| Conventional IQR 1.5x, at least 3 columns | 67,522 | 18.95% |
| Adjusted IQR, at least 3 columns | 1,158 | 0.33% |
| Conventional absolute Z > 3, at least 3 columns | 13,395 | 3.76% |
| Empirical 99th percentile Z, at least 3 columns | 5,940 | 1.67% |
| Isolation Forest 1% contamination | 3,563 | 1.00% |
| Isolation Forest 5% contamination | 17,813 | 5.00% |
| Isolation Forest 10% contamination | 35,626 | 10.00% |

The detector-consensus queue contains 3,758 rows. That number is not called "high probability". It means at least three available detectors agree and the agreement share is at least 50%.

## Outcome validation

The cluster diagnostic is recomputed from the confusion matrix:

- precision = 5,791 / (5,791 + 47,657) = 10.83%;
- recall = 5,791 / (5,791 + 19,034) = 23.33%;
- specificity = 235,029 / (235,029 + 47,657) = 83.14%; and
- lift = 10.83% / 8.07% = 1.34x.

The full-segment precision ceiling is 11.91%. A policy that flags only the smallest highest-rate segment reaches 11.91% precision but only 3.30% recall. Higher recall requires selecting broader segments and accepting more false positives.

At the same 17.38% review share, the supervised reference reaches 21.75% precision, 46.84% recall, AP 23.33%, and AUC 0.751. Cluster alignment reaches AP 9.53% and AUC 0.557. This is strong evidence of objective mismatch.

## Statistical-fallacy review

| Risk | Status | Control |
|---|---|---|
| Simpson's paradox | Limitation | Show portfolio and all segment rates; no product/time strata are available for a complete reversal test |
| Ecological fallacy | Mitigated | Prohibit applicant decisions from segment averages |
| Berkson's paradox | Limitation | Restrict claims to observed applicants; selection mechanism is unknown |
| Collider bias | Mitigated | Do not estimate causal effects after conditioning on cluster |
| Base-rate neglect | Mitigated | Report base rate, precision, lift, AP, and false positives together |
| Regression to the mean | Not applicable | No before/after treatment-effect claim |
| Survivorship bias | Limitation | Separate no history from clean history; public observation still defines availability |
| Look-elsewhere effect | Limitation | Export thresholds, search length, rejections, and final counts |
| Garden of forking paths | Mitigated | Fix seeds, K range, thresholds, and sensitivity tables in code |
| Causation fallacy | Mitigated | Label every mined relationship descriptive |
| Reverse causality | Mitigated | Use repayment history as context, not a causal mechanism |

## What would be required for a prediction project

If the business objective changes to applicant-level default prediction, the next workflow should use an out-of-time train/validation/test design, calibrated probabilities, cost-sensitive thresholds, stability and drift checks, proxy/fairness testing, reason-code governance, and documented human override. The cluster label may be one candidate feature, but it should not be the prediction itself.

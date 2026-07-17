# Dashboard presentation outline

Target length: 11 to 13 minutes.

## Run of show

| Time | Dashboard view | Main point |
|---|---|---|
| 0:00-1:00 | Overview | The assignment is knowledge discovery. Train and test are combined for unlabeled discovery; only 307,511 train IDs enter outcome metrics. |
| 1:00-2:15 | Overview, data-quality panels | Missing history is separated from clean history. Source values are preserved even when model values are clipped or imputed. |
| 2:15-4:30 | Segments | K=5 is stable and useful, but K=3 has the best silhouette. Compare all five profiles on one scale. |
| 4:30-5:20 | Segments, DBSCAN plot | DBSCAN is a 50,000-row UMAP sample. Its 914 noise points are exploratory, not fraud/default labels. |
| 5:20-7:00 | Rules | Show one utilization rule, one repayment rule, and one thin-file availability rule. Read support count and denominator before lift. |
| 7:00-9:00 | Anomalies | The 3,758-row queue requires detector consensus and record-specific evidence. Open one row and show the human action plus `Automatic Decision Allowed = No`. |
| 9:00-11:15 | Outcome | Explain 10.83% precision and 23.33% recall as a cluster-objective limitation. Compare with the matched-capacity logistic diagnostic at 21.75% and 46.84%. |
| 11:15-12:30 | Outcome / close | Clustering supports portfolio strategy; a separate governed supervised process is needed for applicant prediction. |

## Suggested narration

### Opening

"This project asks what structure and actionable patterns exist in the Home Credit portfolio. It does not ask us to maximize Kaggle prediction accuracy. I still test historical outcome alignment at the end, but I keep that separate from the unsupervised discovery work."

### Data boundary

"The full discovery population has 356,255 applications. TARGET exists only for 307,511 train rows. The test set contributes to unlabeled pattern discovery, but it contributes zero rows to precision and recall."

"The preprocessing also keeps two versions of sensitive numeric evidence. Robust model values support stable distances; preserved source values support honest record explanations."

### Segments

"K=3 has the strongest silhouette. I retain K=5 because it is near the elbow, stable across seeds, and gives five distinct operational profiles. I am not calling K=5 statistically optimal on every metric."

"The heatmap colors mean above or below the portfolio reference for the named feature. They do not mean approve or decline."

Short profile prompts:

- Intensive Card User: "Review current utilization, balances, payment capacity, and limit suitability."
- Repayment-Stress History: "Review recency, severity, cure status, and current affordability."
- Thin-File / Low-Intensity: "Treat limited history as uncertainty, not clean behavior."
- High-Exposure Applicant: "Verify income and stress the requested exposure."
- History-Rich Credit User: "Use the deeper history to reconcile current obligations."

### Rules

"Global algorithm agreement is only counted when Apriori, FP-Growth, and ECLAT use the same full-portfolio transactions. Segment rules keep their own denominator."

"Very high lift on thin-file rules mostly describes information availability across tables. That is useful for evidence collection, but it is not a repayment-quality signal."

### Anomalies

"A record enters the consensus queue only when at least three available detectors agree and the agreement share is at least half. Because DBSCAN only covers its sample, each record also shows how many detectors were available."

"The queue is for reconciliation, affordability review, or documenting a rare but plausible profile. It cannot issue an automatic decision."

### Outcome page

"The cluster flag is precise on 10.83% of flagged rows and captures 23.33% of observed defaults. That is above the 8.07% base rate, but it is too weak for applicant decisions. The highest complete segment rate is only 11.91%, so broad cluster scores have a hard precision ceiling."

"At the same 17.38% review capacity, a train-only out-of-fold logistic diagnostic reaches 21.75% precision and 46.84% recall. This is what we expect when the method is trained for the outcome. It diagnoses the objective mismatch; it does not create a production model."

### Close

"The project succeeds as a discovery system: stable segments, denominator-safe patterns, and a conservative review queue. Its negative finding is equally useful: cluster membership should not be used as the applicant default prediction."

## Likely questions

### Why not choose K=3?

K=3 is the compact geometric winner. K=5 is retained for business resolution because it remains near the elbow, seed-stable, non-empty, and interpretable. Both facts are shown.

### Is the Repayment-Stress segment a decline list?

No. Its train default rate is 11.91%, so most members did not default. It is a prompt to review repayment evidence, not a decision label.

### Why is High-Exposure lower-default historically?

That is a cohort association, not a causal or individual guarantee. It may reflect selection, product mix, unobserved underwriting, or other confounding. Verify each applicant.

### Can test precision be reported?

No. The public test data has no TARGET. The project reports zero test rows scored.

### Why does DBSCAN cover only 50,000 rows?

UMAP and density clustering are expensive at full scale. The sample is reproducible and its standardized feature means are checked against the portfolio. The result is still labeled sampled.

### Are anomalies defaults?

No. An anomaly is unusual. It may be a data issue, rare legitimate case, or a file needing affordability/repayment review.

### Is the logistic diagnostic production ready?

No. Production requires out-of-time validation, calibration, cost and capacity analysis, fairness testing, governance approval, and monitoring.

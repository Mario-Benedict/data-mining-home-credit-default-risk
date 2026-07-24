# Knowledge Discovery Report: Home Credit Application Portfolio

**Domain focus:** Consumer loan application risk assessment for borrowers with limited conventional credit history

**Dataset:** Home Credit Default Risk (Kaggle competition data). Source and full field dictionary: https://www.kaggle.com/competitions/home-credit-default-risk/data

**Decision boundary:** This report discovers portfolio structure, recurring evidence patterns, and unusual records that deserve human review. It is not an underwriting model and it does not approve, decline, price, rank, or change a limit for any application. The portfolio is analyzed as one unlabeled population of 356,255 applications. One raw source file carries a loan-outcome column from its original competition packaging; the pipeline removes that column at ingestion, and no later phase, finding, chart, or recommendation reads it. Every pattern here comes from the applications themselves: amounts, ratios, histories, and their combinations. Amounts are anonymized, so the report assumes no currency and treats a recorded loan amount as a contract value at application, not an outstanding balance, an exposure figure, or a loss.

## Executive Summary

A single behavioural segment that holds about one third of applications concentrates more than half of the portfolio's recorded loan value, and a separate multi-method anomaly review isolates 6,404 applications, or 1.80 percent of the portfolio, that warrant a human check, 121 of them carrying outright data-quality faults that no single field test would catch. The bank does not currently aim its affordability scrutiny or its data-quality controls at where the committed money and the recording risk actually concentrate, and headline application counts hide both. The most important action is to route affordability verification toward the concentrated segment and run the flagged queue as a controlled review workload, while treating every segment label and every flag as a prompt for a documented human check rather than an automatic decision.

## Dataset and Methodology

### Dataset

The analysis uses the Home Credit Default Risk dataset published for the Kaggle competition of the same name. It covers consumer lending to applicants who often have thin conventional credit files, which is the domain this report addresses. Eight source files are used: two application files and six behavioural history files (external bureau records, bureau monthly balances, previous Home Credit applications, point-of-sale and cash-loan monthly snapshots, instalment payments, and revolving card balances). The two application files are stacked into one working population of 356,255 applications. No sampling is applied to the population itself: every one of the 356,255 applications enters the analysis. Fixed random samples are used only inside individual evaluation steps (for example a 5,000-application silhouette sample and a 30,000-application density view), and each such sample is stated where it appears. After feature governance, 42 features enter the mining matrices, selected from 61 prepared business fields.

### Phase 1: Data Preprocessing

Cleaning follows the meaning of each field rather than a single generic rule. The employment-duration sentinel of 365,243 days, which encodes a pensioner or non-employed status for 64,648 applications (18.15 percent), is replaced with a missing value and a retained flag so it is never read as roughly a thousand years of tenure. Four gender values coded as unknown are treated as missing. Missingness indicators are created before imputation so an absent value is never silently overwritten: the unavailable first external score (54.43 percent of applications) keeps a missingness flag and is then median-imputed for the model-facing field, and the housing block (48.01 percent absent) keeps one no-housing-data indicator. Structural absences are set to zero with an explaining flag, for example a missing car age when the applicant owns no car. Duplicate handling is explicit rather than assumed: the two application files are checked for exact duplicate rows and for repeated applicant identifiers at the join step. The supplied files contain none, so no rows are removed, and the pipeline stops if a repeated identifier with conflicting values ever appears.

Transformation covers normalization, encoding, and binning. Skewed monetary fields are winsorized at the 99th percentile and log-transformed before scaling. Continuous mining axes are standardized. High-cardinality organization type is binned from 58 source values into 16 macro-sectors before frequency encoding, and rare income categories that together cover 55 applications are grouped into one bucket so they cannot form unstable fragments. Categorical fields use compact encodings rather than one-hot expansion, because sparse binary columns would dominate Euclidean distance and force every category to sit equidistant from every other. Binary flags stay as zero or one so a cluster profile can be read as the share of a group that carries a trait.

Feature selection uses correlation and unsupervised entropy, the two methods the course requires, and never reads any outcome label. Redundant building-measurement variants are removed in favour of one statistical form per measurement, and near-constant or almost duplicate columns are dropped. The final mining matrix retains 42 features and has one residual correlation above 0.85, between mean and maximum historical card utilization at 0.892; both are kept because one describes sustained use and the other peak use, and the overlap is recorded as a sensitivity caveat. Gender and fields carrying a high risk of socioeconomic, family, age, location, education, employment, or social-circle proxying are held out of the mining matrix and kept only in the readable business view for description and fairness testing.

### Phase 2: Clustering

Three clustering algorithms are applied. K-Means is the primary operating method, hierarchical (agglomerative) clustering is the validation method, and DBSCAN provides a density and noise view. PCA compresses the 42 features to 10 components, retaining 63.28 percent of total variance, and the choice is checked against 16, 22, and all 42 dimensions, which reproduce the 10-component labels at Adjusted Rand Index 0.977, 0.970, and 0.966. The number of segments is chosen from a fixed evaluation sample using both the Elbow method and the Silhouette score. K equal to 5 sits at the elbow with a silhouette of 0.147 and is highly reproducible across random seeds at a mean Adjusted Rand Index of 0.995; K equal to 2 scores a higher silhouette of 0.262 but places 83.4 percent of applications in one group, which is too coarse for differentiated review, so the trade-off is made explicit rather than resolved by one metric.

Hierarchical clustering uses Ward linkage. The linkage is defended with the cophenetic correlation on a common 2,000-application sample: Ward scores 0.447, complete 0.674, and average 0.809; average preserves pairwise distances best but chains almost every application into one group with a few tiny satellites, so Ward is retained for its balanced, usable merge structure and its lower distance fidelity is reported as the cost of that choice. The Adjusted Rand Index between K-Means and the sampled Ward solution is 0.584, with normalized mutual information 0.593, meaning the two methods see related but not identical structure. DBSCAN is run on a 30,000-application sample after a two-dimensional UMAP embedding, with min_samples of 15 and an eps of 0.104 taken from the knee of the normalized 15-neighbour distance curve; it isolates 493 sampled noise points and contributes a density view only, never a portfolio-wide anomaly rate.

### Phase 3: Association Rule Mining

Continuous variables are discretized into domain-meaningful bands before mining: income and loan-amount quantiles, leverage bands at three and six times income, payment-burden bands at 20 and 35 percent of income, external-score tertiles limited to observed and available scores, bureau-debt bands at 30 and 80 percent of bureau credit, and categorical states for previous-application outcomes, instalment behaviour, and historical card use. Apriori is applied with a minimum support of 3 percent, a minimum confidence of 35 percent, a minimum lift of 1.20, and a maximum itemset length of three (up to two antecedents and one consequent), and Support, Confidence, and Lift are computed for every rule and used to filter. FP-Growth and ECLAT are run at the same thresholds as an implementation cross-check, and all three enumerate the same 1,077 portfolio-wide rules with matching metrics.

The mining produces 4,516 candidate rules before filtering. A first screen removes arithmetic identities, nested count definitions, same-source missingness identities, same-family restatements, and relationships created by the parent-child table schema, leaving 689 genuine cross-source candidates. A business screen then removes decorative extra conditions and low-information bands, and equivalent forms are combined, leaving 80 unique patterns from which a diversity screen selects 12. The 12 retained rules span a Lift range of 1.202 to 1.463. The modest ceiling is itself a result: every candidate with a Lift above 2 restated an arithmetic identity or a table-join artifact rather than a genuine cross-source relationship.

### Phase 4: Anomaly Detection

The three outlier types are all searched for, each with methods suited to it. Point outliers, which are extreme on a single field, are caught by a skew-adjusted IQR fence and a calibrated Z-score, each run on 33 continuous fields and each calibrated so a field flags about 1 percent of its own values, with a record signalled only when at least three fields trigger; a separate route admits any record at least 10 standard deviations from the mean on one prepared axis. Contextual outliers, which are plausible field by field but unusual in combination, are caught by shrinkage Mahalanobis distance and Isolation Forest, which read the whole feature vector at once. Collective outliers, which sit in an unusual local group, are caught by Local Outlier Factor and corroborated by the Phase 2 DBSCAN density sample.

Thresholds are stated and justified. The IQR and Z-score fences use the calibrated 1 percent per-field operating point rather than the textbook 1.5 multiplier or the z above 3 rule. Shrinkage Mahalanobis and Local Outlier Factor use the empirical top 2.5 percent as a review-volume cut-off. The Mahalanobis review threshold at the 97.5 percent quantile is 92.3; for comparison, the textbook chi-square 99.9 percent threshold at 33 degrees of freedom is 63.9 and would flag 5.10 percent of applications rather than the 0.1 percent that normality predicts, which confirms the distances are heavy-tailed and justifies the empirical cut-off. Isolation Forest uses a 0.05 contamination value after a sensitivity sweep at 0.01, 0.05, and 0.10. The five portfolio-wide detectors flag between 1,295 and 17,813 records each, and their pairwise Jaccard overlap ranges from about 4.3 to 25.8 percent, so agreement is informative rather than mechanical. In total, 27,385 applications are flagged by at least one detector as candidates before the corroboration review that forms the final queue.

## Findings

The three findings below each come from a different phase: segmentation, association rule mining, and anomaly detection. Each states a business claim carrying a number from the analysis, is confirmed by a second method, and avoids causal language. Full technical backing is in the Appendix.

### Finding 1

One clustering segment holds 34.4 percent of applications yet carries 52.98 percent of the portfolio's recorded loan value, so application volume and committed amount are not the same control question.

**Evidence.** K-Means clustering at K equal to 5 (Silhouette Score 0.147 on a fixed 5,000-application sample) identifies the Larger-Loan Affordability segment: 122,395 applications, or 34.36 percent of the portfolio, with a median loan-to-income ratio of 5.24 against 3.16 portfolio-wide and a median payment-to-income ratio of 22.0 percent against 16.3 percent. This segment carries 52.98 percent of all recorded loan amounts and 46.63 percent of all scheduled payment amounts, so a third of applications account for more than half of the money the portfolio has committed on paper.

**Corroboration.** Ward-linkage hierarchical clustering recovers related structure at an Adjusted Rand Index of 0.584 with the K-Means partition, and the amount concentration does not depend on the exact partition: it is a direct sum of recorded loan amounts within the segment. A Phase 3 association rule adds independent support from a different method: among applications with a loan above six times income and a clean observed instalment record, 64.4 percent also had at least three quarters of their earlier applications approved, against a 52.4 percent baseline (Lift 1.228), so routine-looking history clusters exactly where the large amounts sit.

**Business Implication.** Where recorded amounts concentrate, a weakness in affordability verification touches a disproportionate share of committed value, so this segment is where affordability scrutiny earns the most control per case reviewed. A clean-looking history in this segment is not a substitute for income verification, since the pattern shows clean histories and prior approvals are common here. This speaks to the affordability-assessment policy for the higher-value application stream, not to a decision on any single applicant.

**Recommended Action.** The credit-policy and affordability-review teams should verify sustainable income and current obligations for this segment and test the recorded payment under an approved lower-income scenario before any credit action, and should track application volume and committed amount as two separate portfolio measures rather than reading one from the other.

### Finding 2

Applications with a history of at least three prior refusals show recorded instalment lateness 60.1 percent of the time, against a 44.5 percent portfolio baseline, a co-occurrence 15.6 percentage points above chance.

**Evidence.** Association rule mining with Apriori, cross-checked by FP-Growth and ECLAT (minimum support 3 percent, minimum confidence 35 percent, minimum lift 1.20), retains the portfolio-wide rule that at least three prior refused applications co-occur with some recorded instalment lateness at Support 6.22 percent, Confidence 60.1 percent, and Lift 1.351. In counts, 22,151 of 36,868 applications with three or more prior refusals also carry recorded instalment lateness.

**Corroboration.** All three algorithms enumerate this identical rule with matching Support, Confidence, and Lift, which confirms it is not an artifact of one search strategy. A second, independent cross-source pattern points the same way inside the Lower-Intensity Credit Footprint segment: among applications with bureau debt of at least 80 percent of bureau credit, 56.9 percent also have available external scores in the lower band, against a 38.9 percent segment baseline (Lift 1.463), so a second source again sharpens the review question.

**Business Implication.** Repeated refusals become more useful as a review prompt when repayment evidence points the same way, but the pattern is co-occurrence, not cause: it does not explain why an earlier application was refused, or whether lateness was severe, recent, or already cured. This speaks to how a manual reviewer sequences evidence for repeat applicants, not to an automatic decline rule.

**Recommended Action.** The manual underwriting team should, for applicants with repeated prior refusals, review the earlier refusal reasons and dates alongside the severity, recency, and cure status of any recorded lateness before assessing current affordability, and should record the verified facts rather than treat the pattern itself as a decline reason.

### Finding 3

Multi-method anomaly review isolates 6,404 applications (1.80 percent of the portfolio) for a human check, including 121 with data-quality faults that no single-field test would surface on its own.

**Evidence.** Five portfolio-wide detectors (skew-adjusted IQR, calibrated Z-score, shrinkage Mahalanobis, Isolation Forest, and Local Outlier Factor) run on every application. The review queue is formed by two transparent routes: 3,980 records on which at least three of the five detectors agree, and 2,424 further records with at least one prepared value 10 standard deviations from the mean, for a total of 6,404. Within the queue, 6,247 records raise an affordability or repayment question, 121 raise a data or source-reconciliation question, and 36 are rare but plausible profiles. The clearest data-quality case, applicant 161584, records an average paid-to-due ratio of 1,272.58 times (45.8 standard deviations from the mean), which is physically implausible and would distort any affordability read taken at face value.

**Corroboration.** The queue is built on method agreement itself: 3,980 records are admitted only where three or more of five independent detectors concur, and the Phase 2 DBSCAN density sample independently corroborates 28 queued records as isolated points. The typology splits into 4,334 point, 2,056 contextual, and 14 collective outliers, so different detector families confirm different kinds of unusualness rather than re-flagging one pattern.

**Business Implication.** The queue concentrates review effort: the Repayment-Stress History and Historical Card-Use Intensity segments, 17.4 percent of the portfolio, supply 69.3 percent of the queue, so a small part of the portfolio absorbs most specialist time. The 121 data-quality records matter out of proportion to their count: an unreconciled recording fault silently distorts every downstream affordability judgment on that application. This speaks to review-workload planning and to data-operations ownership, not to a risk score.

**Recommended Action.** The data-operations team should own the 121 source-reconciliation records and verify sign, units, joins, reversals, and duplicate rows before any of those applications is judged, while the review team runs the remaining queue as a controlled workload with two lanes, one for repayment-timeline review and one for confirming whether a historical facility is still open, recording outcomes so the 3-of-5 and 10-standard-deviation cut-offs can be tuned on real review yield.

## Limitations

This section states the boundaries of what the analysis can and cannot claim. It is an honest account of what the methodology does not cover, not a defence of the work.

### Scope of Outlier Detection

All three outlier types were searched for, but not to equal depth. Point and contextual outliers were assessed across the full portfolio by five detectors. Collective outliers were only partially addressed: the DBSCAN density view that identifies them ran on a 30,000-application sample, not the full portfolio, so the collective count of 14 is a sampled lower bound rather than a portfolio total, and no aggregate time-window feature was built to detect collective anomalies across the raw transaction-level histories. Contextual outliers were detected against one global covariance shape rather than separately within each segment, so a record that is unusual only relative to its own segment may be missed. The queue has no verified anomaly ground truth, so its thresholds set review volume rather than measure a true anomaly rate, and the detectors see only the 42 prepared applicant-level fields: anything unusual in a way those fields do not encode, such as collusion across applicants or document forgery, is invisible here.

### Correlation versus Causation

The association rules in Phase 3, and every finding drawn from them, establish co-occurrence and not causation. Finding 2 is the one most open to a tempting causal reading: it would be easy to treat prior refusals as a cause of later lateness, or to read both as symptoms of a single underlying risk. The evidence does not support either reading. The rule shows only that the two patterns appear together more often than chance in the supplied files, and a plausible non-causal explanation remains open, since applicants with more recorded history simply have more opportunity to show any pattern, and product mix and past approval policy shape which combinations can be observed at all. The same caution applies to Finding 1: the amount concentration describes the segment collectively and says nothing about whether any individual applicant in it is less affordable, and treating a group average as an individual property would be an ecological fallacy.

### Dataset Representativeness

The portfolio is the supplied set of 356,255 applications: people who applied to Home Credit, passed whatever intake occurred, and reached the recorded files, so it says nothing about applicants who never applied, applied elsewhere, or were filtered before recording. The competition data is a historical extract of unspecified collection dates, so no age-of-data or recency claim can be made, and the timing of any pattern relative to today is unknown. The geographic scope is a single lender's market and is not stated at country or region level in the supplied files, so the findings should not be generalized to other markets or products. Amounts are anonymized without currency or payment-frequency metadata, so no absolute monetary claim survives outside this dataset, and the segment sizes and shares would shift under a different intake policy, product mix, or time window. The course reference document also does not list Home Credit among its assigned datasets, so dataset approval remains an administrative dependency the analysis cannot settle.

### What Additional Data Would Improve These Findings

Several additions would allow stronger conclusions. Current account status for historical facilities, meaning open or closed flags and closure dates on card and bureau records, would resolve the central uncertainty in the Historical Card-Use Intensity segment, whether an intense historical facility is still live. Refusal reason codes on previous applications would let Finding 2 move from a review prompt to an operational rule. Verified income and current obligations, rather than declared income, would turn the amount concentration in Finding 1 into a measurable affordability control. Reporting timestamps and lineage on bureau records and external scores would let reviewers weight agreeing or conflicting sources instead of only reconciling them by hand. Recorded outcomes of the review queue itself, meaning confirmed errors, verified rare cases, and no-issue results per route, would let the anomaly thresholds be tuned on real review yield. Explicit currency, unit, and schema metadata would convert several data-quality checks from statistical inference into deterministic validation.

### Other boundaries

Historical sources do not always reveal current account status, reporting recency, dispute status, or whether arrears were cured, and source-table exposure is uneven, so an applicant with more prior Home Credit activity has more opportunities to show a historical pattern. Structural zeros and missingness flags preserve useful context but can still act as socioeconomic or life-stage proxies. K equal to 5 is a stable operating resolution, but Ward only partially agrees and DBSCAN is a sampled view. Dashboard responsiveness against the rubric's sub-100-millisecond expectation and the team's presentation delivery both require live demonstration that repository artifacts cannot certify.

## Appendix

The Appendix holds the full technical outputs. The Findings section references these but does not reproduce them.

### Appendix A: Full Cluster Profiles

The five K-Means segments and the sampled DBSCAN noise population are profiled below. Sizes: Lower-Intensity Credit Footprint 120,294 applications (33.77 percent); Repayment-Stress History 7,622 (2.14 percent); History-Rich Credit User 51,426 (14.44 percent); Larger-Loan Affordability 122,395 (34.36 percent); Historical Card-Use Intensity 54,518 (15.30 percent). The DBSCAN sampled-noise population is 493 records, profiled against its own 30,000-application sample base because the density view never assessed the rest of the portfolio. The recommended action per segment appears in Appendix E. The complete field-by-field profile is also exported to [`segment_full_profiles.csv`](results/phase2_clustering/segment_full_profiles.csv). Numeric features are shown as mean with standard deviation in parentheses; categorical and flag features are shown as the modal value with the share of the population that holds it. Amounts are in anonymized currency units.

**Table A1. Numeric features: mean (standard deviation)**

| Feature | Lower-Int | Repay-Stress | Hist-Rich | Larger-Loan | Card-Use | DBSCAN noise |
|---|---:|---:|---:|---:|---:|---:|
| AMT_INCOME_TOTAL | 141,167 (68,820) | 155,317 (77,144) | 188,750 (86,922) | 179,747 (89,686) | 179,964 (84,386) | 152,556 (79,866) |
| AMT_CREDIT | 279,348 (123,638) | 567,928 (368,643) | 524,917 (310,350) | 906,337 (376,103) | 615,154 (367,361) | 629,035 (385,382) |
| AMT_ANNUITY | 17,462 (7,799) | 26,627 (13,318) | 27,155 (13,250) | 37,226 (14,709) | 27,772 (13,152) | 28,449 (14,374) |
| CREDIT_TO_INCOME | 2.229 (1.075) | 4.052 (2.716) | 3.029 (1.754) | 5.810 (2.813) | 3.805 (2.441) | 4.942 (3.865) |
| ANNUITY_TO_INCOME | 0.139 (0.066) | 0.191 (0.096) | 0.158 (0.074) | 0.237 (0.103) | 0.172 (0.086) | 0.215 (0.119) |
| CREDIT_TO_ANNUITY | 16.8 (5.5) | 21.0 (7.9) | 19.5 (7.1) | 25.4 (7.6) | 21.9 (7.7) | 22.0 (8.5) |
| YEARS_EMPLOYED | 5.504 (5.710) | 7.011 (6.704) | 6.992 (6.440) | 7.196 (6.839) | 6.974 (6.388) | 5.833 (5.522) |
| OWN_CAR_AGE | 3.896 (9.205) | 4.202 (9.064) | 3.938 (8.707) | 4.400 (9.053) | 3.913 (8.422) | 3.097 (7.317) |
| EXT_SOURCE_1 | 0.481 (0.144) | 0.503 (0.133) | 0.509 (0.141) | 0.523 (0.138) | 0.509 (0.142) | 0.483 (0.147) |
| EXT_SOURCE_2 | 0.489 (0.195) | 0.500 (0.193) | 0.513 (0.188) | 0.541 (0.180) | 0.518 (0.190) | 0.441 (0.214) |
| EXT_SOURCE_3 | 0.520 (0.170) | 0.502 (0.179) | 0.459 (0.188) | 0.542 (0.165) | 0.491 (0.176) | 0.503 (0.170) |
| BUREAU_COUNT | 3.896 (3.896) | 4.776 (4.400) | 6.958 (5.554) | 4.539 (4.138) | 5.465 (4.958) | 4.097 (5.036) |
| BUREAU_ACTIVE_RATIO | 0.348 (0.338) | 0.342 (0.313) | 0.381 (0.284) | 0.332 (0.313) | 0.382 (0.314) | 0.324 (0.360) |
| BUREAU_DEBT_TO_CREDIT_RATIO | 0.234 (0.296) | 0.233 (0.285) | 0.283 (0.279) | 0.215 (0.573) | 0.277 (0.296) | 0.248 (0.326) |
| BUREAU_DAYS_CREDIT_MEAN | -814.2 (647.1) | -988.3 (661.4) | -1,035 (561) | -979.2 (653.7) | -970.2 (626.9) | -826.6 (631.2) |
| BUREAU_BB_DPD_RATIO_MEAN | 0.005 (0.028) | 0.017 (0.067) | 0.010 (0.040) | 0.005 (0.026) | 0.007 (0.031) | 0.019 (0.060) |
| BUREAU_BB_SEVERE_DPD_MEAN | 0.000 (0.011) | 0.005 (0.038) | 0.001 (0.020) | 0.001 (0.013) | 0.001 (0.015) | 0.005 (0.037) |
| PREV_COUNT | 2.991 (2.153) | 4.287 (3.348) | 10.8 (5.1) | 2.961 (2.221) | 6.630 (4.327) | 6.290 (5.311) |
| PREV_APPROVAL_RATE | 0.762 (0.300) | 0.734 (0.277) | 0.512 (0.225) | 0.752 (0.319) | 0.673 (0.254) | 0.716 (0.271) |
| PREV_REFUSED_COUNT | 0.309 (0.695) | 0.850 (1.618) | 2.936 (3.106) | 0.256 (0.646) | 1.185 (1.985) | 1.237 (2.126) |
| INST_DPD_MEAN | 0.437 (1.082) | 25.2 (53.1) | 0.617 (1.098) | 0.386 (1.007) | 0.467 (0.784) | 2.758 (10.199) |
| INST_DPD_MAX | 4.543 (12.465) | 474.5 (540.0) | 11.1 (26.3) | 4.346 (12.710) | 14.6 (31.5) | 80.4 (251.7) |
| INST_COUNT | 20.0 (16.8) | 42.7 (36.1) | 55.5 (35.1) | 21.2 (18.6) | 99.6 (52.7) | 57.8 (52.9) |
| INST_LATE_RATIO | 0.064 (0.113) | 0.298 (0.194) | 0.091 (0.108) | 0.057 (0.105) | 0.066 (0.076) | 0.092 (0.117) |
| INST_SEVERE_LATE_RATIO | 0.001 (0.006) | 0.075 (0.066) | 0.002 (0.007) | 0.001 (0.006) | 0.001 (0.006) | 0.007 (0.019) |
| INST_PAYMENT_RATIO_MEAN | 1.179 (18.710) | 1.984 (97.156) | 1.771 (40.680) | 1.251 (24.429) | 1.114 (6.455) | 1.184 (1.823) |
| POS_SK_DPD_MEAN | 1.066 (32.534) | 94.1 (220.1) | 4.699 (72.578) | 1.988 (46.553) | 2.169 (44.222) | 14.4 (87.5) |
| POS_MONTHS_COUNT | 20.0 (15.9) | 41.9 (28.7) | 53.3 (32.4) | 21.1 (17.2) | 35.8 (27.3) | 38.6 (29.6) |
| CC_UTILIZATION_MEAN | 0.007 (0.049) | 0.059 (0.161) | 0.018 (0.079) | 0.005 (0.038) | 0.550 (0.262) | 0.159 (0.279) |
| CC_UTILIZATION_MAX | 0.019 (0.118) | 0.170 (0.376) | 0.059 (0.209) | 0.018 (0.112) | 1.008 (0.128) | 0.324 (0.477) |
| CC_SK_DPD_MEAN | 0.023 (1.686) | 20.0 (84.6) | 0.011 (1.008) | 0.025 (3.210) | 4.895 (51.537) | 0.048 (0.223) |
| CC_AMT_BALANCE_MEAN | 1,041 (7,972) | 9,306 (36,876) | 3,570 (16,322) | 1,073 (8,128) | 123,541 (123,474) | 30,956 (69,541) |
| CC_MONTHS_COUNT | 2.162 (8.940) | 14.6 (30.7) | 7.393 (16.992) | 3.155 (12.255) | 49.6 (35.4) | 17.4 (27.7) |
| GOODS_TO_CREDIT | 0.913 (0.121) | 0.894 (0.098) | 0.900 (0.104) | 0.897 (0.085) | 0.883 (0.095) | 0.888 (0.088) |
| YEARS_BIRTH | 42.3 (13.1) | 45.0 (11.3) | 45.8 (12.1) | 44.6 (11.1) | 44.2 (10.5) | 44.2 (12.3) |
| NAME_INCOME_TYPE_FREQ | 0.365 (0.166) | 0.358 (0.168) | 0.347 (0.166) | 0.351 (0.168) | 0.361 (0.165) | 0.357 (0.168) |
| ORGANIZATION_TYPE_FREQ | 0.142 (0.097) | 0.138 (0.095) | 0.144 (0.095) | 0.140 (0.098) | 0.141 (0.099) | 0.147 (0.093) |
| SOURCE_EXT_SOURCE_1 | 0.450 (0.211) | 0.498 (0.205) | 0.512 (0.210) | 0.542 (0.201) | 0.513 (0.205) | 0.453 (0.221) |
| SOURCE_EXT_SOURCE_2 | 0.489 (0.196) | 0.500 (0.193) | 0.513 (0.188) | 0.541 (0.180) | 0.518 (0.190) | 0.441 (0.214) |
| SOURCE_EXT_SOURCE_3 | 0.515 (0.196) | 0.494 (0.200) | 0.452 (0.196) | 0.545 (0.184) | 0.482 (0.193) | 0.495 (0.189) |
| SOURCE_AMT_INCOME_TOTAL | 142,802 (345,077) | 156,199 (82,174) | 191,258 (105,575) | 183,707 (133,014) | 181,875 (99,340) | 153,633 (85,254) |
| SOURCE_AMT_REQ_CREDIT_BUREAU_MON | 0.141 (0.596) | 0.196 (0.793) | 0.260 (0.914) | 0.210 (0.840) | 0.255 (0.966) | 0.174 (0.623) |
| SOURCE_AMT_REQ_CREDIT_BUREAU_YEAR | 1.243 (1.213) | 1.483 (1.524) | 3.663 (2.159) | 1.199 (1.235) | 2.598 (1.876) | 2.166 (1.864) |
| SOURCE_AMT_GOODS_PRICE | 253,046 (112,782) | 507,178 (337,303) | 472,127 (286,289) | 815,586 (356,457) | 544,394 (335,726) | 556,785 (343,649) |

**Table A2. Categorical and flag features: modal value (share of population)**

Flag fields are coded 0 or 1. Ordinal fields (education, region rating, social-circle bin) keep their integer levels; frequency-encoded category fields appear in Table A1 as numeric axes. The two source amount fields that duplicate a model field exactly (recorded loan and annuity) are omitted here to avoid repetition and appear in Table A1.

| Feature | Lower-Int | Repay-Stress | Hist-Rich | Larger-Loan | Card-Use | DBSCAN noise |
|---|---:|---:|---:|---:|---:|---:|
| FLAG_SENTINEL_EMPLOYED | 0 (81%) | 0 (80%) | 0 (78%) | 0 (83%) | 0 (86%) | 0 (76%) |
| NAME_CONTRACT_TYPE | 1 (82%) | 1 (95%) | 1 (93%) | 1 (98%) | 1 (99%) | 1 (96%) |
| FLAG_NO_CAR | 1 (70%) | 1 (67%) | 1 (65%) | 1 (62%) | 1 (67%) | 1 (75%) |
| FLAG_NO_HOUSING_DATA | 0 (50%) | 1 (54%) | 0 (54%) | 0 (53%) | 0 (53%) | 1 (54%) |
| FLAG_EXT_SOURCE_1_MISSING | 1 (55%) | 1 (58%) | 1 (55%) | 1 (54%) | 1 (52%) | 1 (57%) |
| FLAG_EXT_SOURCE_2_MISSING | 0 (100%) | 0 (100%) | 0 (100%) | 0 (100%) | 0 (100%) | 0 (100%) |
| FLAG_EXT_SOURCE_3_MISSING | 0 (75%) | 0 (79%) | 0 (91%) | 0 (80%) | 0 (83%) | 0 (81%) |
| AMT_REQ_CREDIT_BUREAU_YEAR | 1 (41%) | 1 (37%) | 3 (19%) | 1 (38%) | 1 (28%) | 1 (30%) |
| FLAG_NO_BUREAU | 0 (81%) | 0 (85%) | 0 (95%) | 0 (86%) | 0 (88%) | 0 (86%) |
| CNT_CHILDREN | 0 (69%) | 0 (69%) | 0 (74%) | 0 (70%) | 0 (71%) | 0 (73%) |
| REGION_RATING_CLIENT_W_CITY | 2 (76%) | 2 (77%) | 2 (76%) | 2 (72%) | 2 (74%) | 2 (76%) |
| NAME_EDUCATION_TYPE | 1 (72%) | 1 (76%) | 1 (73%) | 1 (67%) | 1 (73%) | 1 (76%) |
| DEF_30_CNT_SOCIAL_CIRCLE_BIN | 0 (89%) | 0 (87%) | 0 (87%) | 0 (90%) | 0 (87%) | 0 (87%) |
| CODE_GENDER | 1 (64%) | 1 (67%) | 1 (68%) | 1 (66%) | 1 (67%) | 1 (67%) |
| SOURCE_AMT_REQ_CREDIT_BUREAU_QRT | 0 (83%) | 0 (83%) | 0 (73%) | 0 (82%) | 0 (79%) | 0 (80%) |

The noise profile explains why the DBSCAN corroboration is worth keeping despite its sampled coverage: noise records combine above-average borrowing scale, payment burden, card activity, and refusals without matching any single segment's signature. They are mixed, not extreme on one axis.

### Appendix B: Full Association Rule Table

All 12 retained rules, ranked by Lift descending. Support, Confidence, and Lift use the rule's own context as denominator (portfolio-wide or the named segment), as registered in [`business_rules_final.csv`](results/phase3_association/business_rules_final.csv). Band definitions are analytical categories from Phase 3, not policy thresholds.

| Antecedent | Consequent | Support | Confidence | Lift |
|---|---|---:|---:|---:|
| Bureau debt at least 80% of bureau credit (Lower-Intensity) | External scores in the lower band | 3.76% | 56.9% | 1.463 |
| Observed average card utilization at least 80% (Card-Use) | External scores in the lower band | 10.30% | 47.1% | 1.363 |
| At least three prior refused applications (portfolio-wide) | Some recorded instalment lateness | 6.22% | 60.1% | 1.351 |
| Loan in upper third plus at least 75% prior approvals (Card-Use) | External scores in the upper band | 6.83% | 41.0% | 1.319 |
| Loan in upper third plus no recorded lateness (portfolio-wide) | External scores in the upper band | 6.14% | 42.9% | 1.289 |
| Card utilization below 80% plus at least 75% prior approvals (Lower-Intensity) | Some recorded instalment lateness | 3.46% | 46.6% | 1.270 |
| Loan in lower third plus external scores in the lower band (History-Rich) | At least three prior refusals | 7.17% | 55.9% | 1.263 |
| Bureau debt 30% to 80% plus external scores in the upper band (Larger-Loan) | Scheduled payment below 20% of income | 4.52% | 51.8% | 1.253 |
| Observed instalments with no recorded lateness (Card-Use) | Mixed prior-application outcomes | 10.13% | 49.2% | 1.239 |
| Loan above six times income plus no recorded lateness (portfolio-wide) | At least 75% prior approvals | 4.94% | 64.4% | 1.228 |
| External scores in the upper band (History-Rich) | Bureau debt below 30% of bureau credit | 17.19% | 64.3% | 1.210 |
| Bureau debt 30% to 80% of bureau credit (History-Rich) | External scores in the lower band | 16.75% | 46.4% | 1.202 |

### Appendix C: Anomaly Detection Results

Representative queue records covering every outlier type and review type. Each row shows the value or flag from every method: IQR and Z-score report the number of continuous fields that triggered (a record signals at three or more), Mahalanobis reports the squared distance D-squared, Isolation Forest reports its score (more negative is easier to isolate), Local Outlier Factor reports its score (above roughly 1.5 is materially sparse), and the DBSCAN sample reports its density status. The full record-level table of all 6,404 queue records is [`anomaly_investigation.csv`](results/phase4_anomaly/anomaly_investigation.csv).

| Record ID | IQR | Z-score | Mahalanobis D-sq | Isolation Forest | LOF | DBSCAN sample | Outlier type | Business interpretation |
|---:|---|---|---:|---:|---:|---|---|---|
| 161584 | flag (3 fields) | flag (3 fields) | 2,301 | -0.454 (no) | 12.08 | not isolated | Point | Average paid-to-due ratio of 1,272.58 times is physically implausible; reconcile instalment rows, reversals, duplicates, and units. Data consistency check. |
| 100784 | flag (5 fields) | flag (4 fields) | 630 | -0.568 | 2.73 | not in sample | Point | Scheduled payment equals 137.4% of declared income; verify income and obligations. Affordability review. |
| 265042 | flag (4 fields) | flag (4 fields) | 240 | -0.486 (no) | 1.78 | not in sample | Point | 295 monthly POS or cash-loan records is an extreme but possible depth of history; confirm the source, then continue standard review. Rare but plausible. |
| 190549 | flag (3 fields) | flag (3 fields) | 164 | -0.514 | 1.57 | not in sample | Contextual | No single field is impossible, but the combined payment-burden pattern is unusual under every multivariate view. Affordability review. |
| 177061 | flag (3 fields) | flag (3 fields) | 114 | -0.558 | 1.49 | not in sample | Contextual | Payment-ratio evidence conflicts with the rest of the record; reconcile the instalment source. Data consistency check. |
| 197583 | flag (3 fields) | flag (4 fields) | 147 | -0.518 | 1.55 | not in sample | Contextual | Unusual previous-application count combined with its history depth; verify and document. Rare but plausible. |
| 303289 | flag (3 fields) | flag (3 fields) | 129 | -0.602 | 1.70 | isolated | Collective | Sits in a sparse micro-group in the sampled density view while carrying a high payment burden; verify the shared pattern, then review affordability. |

### Appendix D: Evaluation Metrics Summary

One reference table of the quantitative evaluation metrics produced across all phases. Each value is written by the phase that produced it and re-checked by the validation script.

| Phase | Metric | Value |
|---|---|---|
| Phase 1 | Portfolio size | 356,255 applications |
| Phase 1 | Exact duplicate rows removed | 0 |
| Phase 1 | Mining features after governance screen | 42 (from 61 business fields) |
| Phase 1 | Residual feature pairs with absolute correlation above 0.85 | 1 (card utilization mean vs max, 0.892) |
| Phase 2 | PCA components retained / cumulative variance | 10 / 63.28% |
| Phase 2 | Silhouette Score (primary K-Means, K=5) | 0.147 |
| Phase 2 | Silhouette Score (K=2 comparison point) | 0.262 |
| Phase 2 | Davies-Bouldin index (K=5) | 1.731 |
| Phase 2 | Mean seed-to-seed Adjusted Rand Index (K=5) | 0.995 |
| Phase 2 | Cophenetic Correlation (chosen Ward linkage) | 0.447 (complete 0.674, average 0.809) |
| Phase 2 | Adjusted Rand Index (K-Means vs Hierarchical) | 0.584 |
| Phase 2 | Normalized mutual information (K-Means vs Hierarchical) | 0.593 |
| Phase 2 | DBSCAN sampled noise | 493 of 30,000 (1.64%) |
| Phase 3 | Number of rules generated | 4,516 |
| Phase 3 | Identical portfolio rules across Apriori, FP-Growth, ECLAT | 1,077 |
| Phase 3 | Number of rules retained after filtering | 12 |
| Phase 3 | Support range of retained rules (own context) | 3.46% to 17.19% |
| Phase 3 | Confidence range of retained rules | 41.0% to 64.4% |
| Phase 3 | Highest Lift value in retained rules | 1.463 |
| Phase 4 | Mahalanobis review threshold (empirical 97.5%) | 92.3 |
| Phase 4 | Chi-square 99.9% threshold (df=33) / diagnostic flag rate | 63.9 / 5.10% |
| Phase 4 | Total anomaly candidates before corroboration | 27,385 (7.69%) |
| Phase 4 | Candidates corroborated by two or more detectors | 9,685 (2.72%) |
| Phase 4 | Detector-consensus route (3 of 5) | 3,980 |
| Phase 4 | Extreme single-axis additions (10+ SD) | 2,424 |
| Phase 4 | Targeted review queue | 6,404 (1.80%) |
| Phase 4 | Outlier typology: point / contextual / collective | 4,334 / 2,056 / 14 |
| Phase 4 | Queue records corroborated by the sampled density view | 28 |

This project uses no outcome label, so no label-based accuracy score is reported. The evaluation rests on internal validity, seed stability, dimensional and threshold sensitivity, and multi-method agreement rather than on any label comparison.

### Appendix E: Segment recommended actions and governance

Recommended review response per segment:

- **Lower-Intensity Credit Footprint (120,294).** Use standard underwriting and request permitted supporting evidence only when a relevant source is genuinely unavailable. This is not a thin-file group: 81.4 percent have bureau history, 94.5 percent have instalment history, and 99.9 percent have at least one external score; its defining feature is lower activity and smaller amounts.
- **Repayment-Stress History (7,622).** Review timing, severity, recency, cure status, disputes, and current affordability; follow hardship policy where verified. Recorded instalment delays sit 3.30 portfolio standard deviations above average.
- **History-Rich Credit User (51,426).** Use the additional evidence to reconcile earlier refusals, arrears, and current obligations rather than assuming that more history is favourable or adverse.
- **Larger-Loan Affordability (122,395).** Verify sustainable income and current obligations and test affordability under a lower-income scenario. This is the amount-concentrated segment of Finding 1.
- **Historical Card-Use Intensity (54,518).** Confirm whether a revolving facility is still open before treating any historical balance or limit as current, then verify current balance, utilization, and arrears.

Before any operational use, add a time-based stability check, segment drift monitoring, rule and queue-yield monitoring, a fairness assessment across permitted groups, lineage and recency controls on external-score inputs, and a clear prohibition on using any cluster, rule, or anomaly label as an adverse-action reason.

### Appendix F: Dashboard and presentation structure

The interactive dashboard (Python Dash) presents the work in the business order: Key findings first, then Data, Segments, Rules, and Anomalies. Key findings carries the three findings above with their evidence, corroboration, implication, and action. Data explains the single portfolio, its source files, evidence availability per segment, and the preprocessing decisions. Segments compares the five profiles including each segment's share of recorded loan amounts. Rules shows the 12 patterns against their own context baselines. Anomalies explains the two queue routes, the point, contextual, and collective typology, workload sensitivity, and record-level evidence. Full algorithm outputs stay in the notebooks and CSV artifacts.

### Appendix G: Reproducibility and evidence map

Run from the repository root in this order: `python src/run_pipeline.py`; then the four notebooks via `python scripts/execute_notebook.py` (exploratory_data_analysis, phase2_clustering, phase3_association, phase4_anomaly); then `python scripts/build_linkage_comparison.py` after Phase 2; then `python scripts/build_business_artifacts.py`; then `python scripts/validate_business_findings.py`; then `python dashboard/app.py`. The order matters because each phase reads the previous phase's outputs, and the validation script fails on stale identifiers, names, counts, rule metrics, queue logic, population denominators, or any reappearance of outcome-label vocabulary on a business surface. Random states and analytical samples are fixed, so with identical inputs, code, and library versions the outputs are reproducible. Cluster integers permute between runs, so downstream interpretation joins through the stable names in `cluster_names.csv`.

| Question | Source of truth |
|---|---|
| Population and scope | [`portfolio_context.csv`](results/phase1_preprocessing/portfolio_context.csv) |
| Cleaning and feature decisions | [`data_quality_summary.csv`](results/phase1_preprocessing/data_quality_summary.csv), [`feature_selection_decisions.csv`](results/phase1_preprocessing/feature_selection_decisions.csv) |
| K and dimensional sensitivity | [`k_selection.csv`](results/phase2_clustering/k_selection.csv), [`k_stability.csv`](results/phase2_clustering/k_stability.csv), [`pca_cluster_sensitivity.csv`](results/phase2_clustering/pca_cluster_sensitivity.csv) |
| Linkage cophenetic evidence | [`linkage_cophenetic.csv`](results/phase2_clustering/linkage_cophenetic.csv) |
| Segment names, sizes, actions | [`cluster_names.csv`](results/phase2_clustering/cluster_names.csv), [`cluster_business_summary.csv`](results/phase2_clustering/cluster_business_summary.csv) |
| Segment amount concentration | [`segment_credit_concentration.csv`](results/phase4_anomaly/segment_credit_concentration.csv) |
| Final association patterns | [`business_rules_final.csv`](results/phase3_association/business_rules_final.csv) |
| Rule screening and thresholds | [`rule_rejection_audit.csv`](results/phase3_association/rule_rejection_audit.csv), [`association_threshold_register.csv`](results/phase3_association/association_threshold_register.csv) |
| Queue size and sensitivity | [`anomaly_summary.csv`](results/phase4_anomaly/anomaly_summary.csv), [`ensemble_single_axis_sensitivity.csv`](results/phase4_anomaly/ensemble_single_axis_sensitivity.csv) |
| Record-level review actions | [`anomaly_investigation.csv`](results/phase4_anomaly/anomaly_investigation.csv) |

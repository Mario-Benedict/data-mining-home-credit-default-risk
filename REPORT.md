# Knowledge Discovery Report

**Dataset:** Home Credit Default Risk (Kaggle competition data). Source and full field dictionary: https://www.kaggle.com/competitions/home-credit-default-risk/data

**Domain Focus:** Consumer loan application risk assessment for borrowers with limited conventional credit history

## Executive Summary

One third of Home Credit's applications carry more than half of everything the portfolio has committed on paper, sit on the thinnest credit files in the book, and receive one tenth of the automated review queue, so a single review in that group stands behind roughly 116 times more committed money than a review in the most heavily checked group. The bank does not currently measure where its checking effort sits relative to the money at stake, and it does not know that its strongest history-based review prompt loses 81 percent of its apparent strength once length of customer relationship is held constant. Credit Policy should set a minimum income-verification standard for large loans that does not depend on how much history an applicant happens to have, and should rewrite every history-based prompt as a rate over the records actually observed.

## Dataset and Methodology

### Dataset

The analysis uses the Home Credit Default Risk dataset, assigned by the course instructor in place of the options in the reference document; the substitution changes neither the methodology nor the assessment criteria. It covers consumer lending to applicants who often have thin conventional credit files. Eight source files are used: two application files and six behavioural history files covering external bureau records, bureau monthly balances, previous Home Credit applications, point-of-sale and cash-loan snapshots, instalment payments, and card balances. The two application files are stacked into one population of **356,255 applications**; no sampling is applied to the population itself. Every method that produces a label runs on all 356,255 rows: K-Means, BIRCH, DBSCAN, and all five anomaly detectors. Fixed samples appear only where a measurement, not a label, is being taken, and each is stated where it appears: a 5,000-application silhouette evaluation sample, a 20,000-application cluster-tendency sample, a 2,000-application cophenetic sample, a 5,000-application sampled-Ward contrast, a 30,000-application UMAP picture, and a 60,000-application ordinary-portfolio reference in the collective-outlier test. After feature selection **41 features** enter the mining matrices, drawn from 60 prepared business fields.

The portfolio is analysed as one unlabeled population: one source file carries a loan-outcome column from its competition packaging, the pipeline removes it at ingestion, and nothing downstream reads it. Amounts are anonymized, so a recorded loan amount is a contract value at application, not a balance, exposure, or loss. Nothing here approves, declines, prices, ranks, or changes a limit.

One structural fact drives two later decisions: the instalment, credit-card, and point-of-sale tables are children of the previous-application table, joined on `SK_ID_PREV`, so a longer Home Credit relationship contributes more rows to all three. That is responsible for the schema-induced rules rejected in Phase 3 and for the exposure correction applied to those that survived.

### Phase 1: Data Preprocessing

Cleaning follows the meaning of each field. The employment-duration sentinel of 365,243 days, encoding pensioner or non-employed status for 64,648 applications (18.15 percent), is replaced with a missing value and a retained flag. Four gender values coded as unknown are treated as missing. Missingness indicators are created before imputation, so the unavailable first external score (54.43 percent) and the housing block (48.01 percent absent) each keep an availability flag, and structural absences such as a missing car age are set to zero with an explaining flag. Duplicate handling is explicit: both application files are checked for exact duplicate rows and repeated applicant identifiers, none are found, and the pipeline halts if a repeated identifier with conflicting values ever appears.

Transformation covers normalization, encoding, and binning. Skewed monetary fields are winsorized at the 99th percentile (486,000 anonymized units for declared income), log-transformed, then standardized. Organization type is binned from 58 source values into 16 macro-sectors before frequency encoding, and four rare income categories covering 59 applications are grouped into one bucket. Categorical fields use ordinal and frequency encoding rather than one-hot, since 15 sparse binary columns from a 16-sector field would outweigh a single standardized continuous feature in Euclidean distance and force every pair of sectors equidistant.

Feature selection uses correlation and unsupervised entropy, and the two do different work. **Correlation removed 31 columns**, each duplicating a column that was kept: the `_AVG` and `_MEDI` building variants against `_MODE` at r above 0.99, `OBS_60` against `OBS_30` at 0.999, `FLAG_EMP_PHONE` against the employment sentinel at -1.0, and the non-city region rating against the city-aware one. Entropy cannot find these, since a perfect duplicate has the same entropy as what it duplicates. **Entropy found the opposite defect:** `FLAG_MOBIL` correlates with nothing yet 99.999 percent of applicants share one value, giving normalized entropy 0.0001 and no capacity to separate any two records; 18 of 120 scored fields fall below a 0.10 screening line.

A third removal fits neither measure. `EXT_SOURCE_1` is unavailable for 54.43 percent of applications, so median imputation would place the majority of the portfolio on one coordinate, exactly the rows the flag already marks, duplicating one fact and handing density and covariance detectors a large artificial mode. The flag is kept, the observed value is kept in the business view where Phase 3 masks by the flag rather than imputing, and the imputed column leaves both mining matrices. The final matrix retains **41 features** with one residual correlation above 0.85 (card utilization mean versus max, 0.891), kept because one describes sustained and the other peak use. Gender and fields carrying socioeconomic, family, age, location, education, employment, or social-circle proxy risk are held out and kept only for description and fairness testing. All 74 decisions are exported with their basis.

Phase 1 produces three applicant-level views: readable source-scale values, values bounded at the 0.5th and 99.5th percentiles then standardized for clustering, and the same fields standardized **without** clipping for anomaly detection, since a truncated axis cannot contain an extreme.

### Phase 2: Clustering

**K-Means** is the primary method, **hierarchical agglomerative clustering** the validation method, and **DBSCAN** the density and noise view. PCA compresses 41 features to 10 components retaining 64.79 percent of variance, accepted because the five-segment labels reproduce at Adjusted Rand Index 0.970, 0.971, and 0.969 against the 16, 21, and full 41-dimensional solutions while silhouette falls as dimensions are added.

Both required selection methods are used. **The Elbow method points to K = 5**, located by maximum distance from the chord joining the endpoints of the normalized inertia curve. **The Silhouette Score at K = 5 is 0.1478**, with Davies-Bouldin 1.7241. Silhouette alone would prefer K = 3 (0.2681) or K = 2 (0.2639), but both place over 81 percent of applications in one group; K = 6 edges K = 5 on both geometric measures and is rejected on reproducibility.

A silhouette of 0.148 invites the conclusion that the clustering failed, so three diagnostics were run to distinguish an empty result from an informative one. **The Hopkins statistic is 0.8814** in the clustering space and 0.8338 across all 41 dimensions, against 0.4982 for a uniform reference scored by the same code, so the portfolio does concentrate rather than spreading like a uniform cloud. **Against two null models the observed value holds**: on the tendency sample K = 5 scores 0.1542 real against 0.1103 for a column-wise shuffle that preserves every marginal and 0.1029 for a uniform draw. That comparison also exposes why no textbook threshold applies here. **At K = 2 the shuffled null scores 0.6740, far above the real data, by isolating 0.91 percent of rows against the remaining 99.09 percent**: silhouette rewards a degenerate split on a skewed axis, so a high value on this data would be evidence of nothing. **The third diagnostic locates the separation.** Clustered on its own, card history scores 0.8452, instalment delinquency 0.6849, relationship depth 0.3469, and affordability 0.2643, against 0.1542 for all 41 features together. Families that separate well alone and poorly together is the signature of a portfolio carrying several overlapping segmentations rather than one, so each segment is described as a recurring evidence profile rather than a customer type.

Reproducibility is tested twice, since seed stability and sample stability differ. Across seeds K = 5 reproduces at **0.997**; across five disjoint split-half fits, where two models trained on non-overlapping halves label the same unseen applications, at **0.955**, against 0.670 for K = 6 and 0.815 for K = 7. Per-segment silhouette ranges from 0.084 for History-Rich Credit User, where 25.6 percent of members sit closer to another segment's centre, to 0.222 for Repayment-Stress History.

Hierarchical validation runs at two scales because exact agglomerative clustering is impossible here: it needs 63.46 billion pairwise distances, 236 GB as float32, and an attempt fails with a 242 GiB allocation error. **BIRCH over all 356,255 applications is the primary hierarchical validation**, summarising the portfolio into 9,381 CF-tree subclusters at threshold 2.0 and then agglomerating those, so every application participates. **The Adjusted Rand Index between K-Means and BIRCH is 0.2572**, with normalized mutual information 0.3667. That is weak agreement, and the reason is visible in the group sizes: BIRCH places 74.59 percent of applications in a single group. A sampled Ward solution with nearest-centre assignment reports 0.4355 and is retained only as a contrast, because assigning the portfolio to the nearest of five sample centroids produces a convex partition of exactly the shape K-Means produces, biasing the comparison upward by 0.178.

Linkage is chosen on the sample where it can be measured, and defended with a number. On a common 2,000-application sample, **cophenetic correlation is 0.4627 for Ward, 0.6337 for complete, and 0.8022 for average**. Average reproduces pairwise distances best and is still rejected: at K = 5 it places 98.80 percent of the sample in one group and complete 94.05 percent, against 33.65 percent for Ward. The chaining that disqualifies those two linkages on the sample is the same pathology BIRCH shows on the full portfolio, so it is a property of this data at every scale rather than an artifact of sampling.

**DBSCAN runs on all 356,255 applications** in the distance-preserving 10-component space, with min_samples 15 and eps 2.075 from the knee of the normalized 15-neighbour distance curve, isolating **12,402 noise points (3.48 percent) across 9 density pockets**, the largest holding 96.3 percent of the portfolio. Nothing is sampled, so the noise flag is a portfolio fact. The two-dimensional UMAP embedding is retained as a picture and as a cross-check: DBSCAN there, on 30,000 applications at eps 0.102, isolates 519 noise points across 29 pockets. **On the applications both spaces judged, the two noise sets agree at a Jaccard of 0.043** (67 shared of 1,547 flagged in either), so the embedded view is substantially a property of the projection. That is why the picture decides nothing and the density flag never votes in the Phase 4 queue.

### Phase 3: Association Rule Mining

Continuous variables are discretized into domain-meaningful bands: income and loan-amount quantiles, leverage at three and six times income, payment burden at 20 and 35 percent of income, external-score tertiles limited to observed scores, bureau debt at 30 and 80 percent of bureau credit, and categorical states for previous-application outcomes, instalment behaviour, and card use. Where a domain threshold exists it is used (30-day delinquency, 80 percent utilization); where anonymized units make an absolute threshold meaningless, quantiles are used and labelled as portfolio-relative.

**Apriori is applied with minimum Support 3 percent, minimum Confidence 35 percent, minimum Lift 1.20, and maximum itemset length three.** FP-Growth and a vertical-tidset ECLAT implementation run at identical thresholds and enumerate the same portfolio-wide rules with matching metrics. Rules are also mined within each segment against that segment's own denominator.

**Mining produces 4,492 candidate rules before filtering and retains 12 after filtering**, spanning a **Lift range of 1.213 to 1.475**, Support 3.48 to 17.03 percent, and Confidence 41.1 to 64.4 percent. The screen removes arithmetic identities (2,444), nested count definitions (537), two views of the same bureau fields (468), same-source missingness identities (274), and parent-child schema artifacts (86), leaving 683 cross-source candidates, 156 carrying a concrete reviewer question, 76 unique patterns, and 12 displayed. The modest ceiling is itself a result, and it is worth being exact about why. Of the 4,492 candidates, 789 reach a Lift above 2 and 778 of those are removed by the identity screens as arithmetic restatements, nested count definitions, or missingness that propagates along a foreign key. The 11 that survive into the cross-source pool are all one pattern in eleven dresses: **an observable card-utilization band implies a deep previous-application history, at Lift 2.27 to 2.67**. That is not borrower behaviour. A card record exists only where a previous application exists, so being measurable on card use already forces the consequent. It is the same history-depth confound that Finding 2 quantifies, arriving independently and at the top of the Lift ranking, which is why the strongest surviving cross-source signals sit at 1.658 before presentation selection and 1.475 after it. In this schema a high Lift is a warning that a join is being restated, not a discovery.

Two further measures are computed. Lift is **not null-invariant**, so Kulczynski, Imbalance Ratio, and Cosine are added; Kulczynski runs 0.281 to 0.482, all below the 0.5 mark for unrelated items. Second, several items are accumulation states recording whether something was **ever** observed, and the parent-child schema means longer relationships produce more opportunity to display them, so every rule with an accumulation consequent receives a **directly standardised Confidence**, stratified by history depth and re-weighted to the population profile. Rules whose consequent is a single application-time value cannot accumulate and are returned unchanged, which doubles as a control on the correction.

The independence assumption behind the cross-source screen is tested rather than asserted: gradient-boosted models predicting each observed external score from bureau aggregates alone reach out-of-sample coefficients of determination of **0.049, 0.016, and 0.368**. The first two scores are genuinely independent of bureau data; the third overlaps moderately and is carried as a caveat.

### Phase 4: Anomaly Detection

All three outlier types are searched for, each defined by the reference it is measured against.

**Point outliers** are extreme against the whole portfolio: a skew-adjusted IQR fence and a calibrated Z-score run on 32 continuous fields, with a record signalled at three or more fields, plus a separate route for any record at least **10 standard deviations** from the mean on one axis.

The two univariate thresholds are set per column rather than borrowed as a constant, so the operating point is a flag rate of about 1 percent per field and the multiplier is whatever produces it. The realised values are reported rather than left implicit. **The calibrated IQR multiplier has a median of 1.42 across the 24 columns that can carry a fence, and 19 of those 24 land between 0.5 and 2.5**, so on well-behaved columns the calibration reproduces Tukey's 1.5 rather than contradicting it. It departs only where the textbook assumption fails: the full range runs from 0.30 on the share of instalments paid late, whose values bunch at zero, to 990.69 on the mean paid-to-due ratio, whose interquartile range is almost zero next to its tail. Eight columns have a zero-width box, where more than half of applicants share one value, and those abstain rather than flagging every applicant who differs at all. **The calibrated absolute-Z threshold has a median of 2.78 and ranges from 0.05 to 6.68**, again close to the textbook 3 in the middle and far from it at the edges. Applied as single constants instead, the textbook **1.5 IQR multiplier** would flag 19.17 percent of the portfolio and the **z above 3** rule 2.28 percent. Full per-column values are in [`univariate_threshold_calibration.csv`](results/phase4_anomaly/univariate_threshold_calibration.csv).

**Contextual outliers** are ordinary portfolio-wide but do not fit their own segment. Shrinkage Mahalanobis with Ledoit-Wolf covariance and Isolation Forest read the whole vector at once, and the label is earned by measuring each record's largest robust deviation from its own segment median on a median-absolute-deviation scale. **Mahalanobis uses an empirical 97.5th-percentile cut-off at squared distance 91.31**; the **chi-square 99.9th percentile at 32 degrees of freedom is 62.49** and would flag 5.15 percent rather than the 0.1 percent normality predicts. **Isolation Forest uses contamination 0.05** after a sweep at 0.01, 0.05, and 0.10.

**Collective outliers** are anomalous as a group. Local Outlier Factor, cross-fitted on two disjoint 20,000-row reference sets so no applicant is scored by a model that saw it, uses an empirical 97.5th-percentile cut-off. A dedicated group test then runs among queued records that are not already point outliers: those in the top decile of distance to the nearest ordinary application are linked when each is among the other's five nearest neighbours and the pair is closer to each other than either is to anything ordinary, and connected components of three to fifty records are retained.

The five detectors flag between 1,295 and 17,813 records each, with pairwise Jaccard overlap from 4.7 to 25.7 percent. **In total 27,740 applications are flagged by at least one detector before the corroboration review that forms the final queue**, and 10,301 by two or more. One further control is run because the segmentation and the detectors read the same matrix: all five are re-run with the six delinquency columns removed, and each segment's change in queue share measures how much of the concentration was independent evidence rather than one signal counted twice.

## Findings

Each finding comes from a different phase and passes the four translation tests. None can be produced by tabulating the source files: the first requires the Phase 2 partition and the Phase 4 queue on one denominator, the second a correction only a reader who knows the parent-child table schema would apply, the third a re-run of the detectors on a deliberately reduced feature set. Each survives a control designed to break it, and where a control reduced a number, the reduced number is stated. Full backing is in the Appendix.

### Finding 1

Larger-Loan Affordability holds 34.62 percent of applications and 53.21 percent of the portfolio's recorded loan value while receiving 10.00 percent of the targeted-review queue, an allocation under which one review in that segment stands behind roughly 116 times more committed loan value than one review in Repayment-Stress History.

**Evidence**

K-Means clustering at K = 5 (Silhouette Score 0.1478 on a fixed 5,000-application evaluation sample, mean seed-to-seed Adjusted Rand Index 0.997, split-half Adjusted Rand Index 0.955) identified Larger-Loan Affordability: 123,344 applications, 34.62 percent of the portfolio, carrying 53.21 percent of all recorded loan amounts and 46.95 percent of all scheduled payment amounts. A Silhouette Score of 0.1478 is low and means these segments are regions of a continuum rather than isolated groups, which is why each is treated as a recurring evidence profile. The split-half figure of 0.955 means two models fitted on non-overlapping halves put essentially the same applications together, which is what makes the segment stable enough to attach a process to.

The Phase 4 ensemble assigned this segment 639 of 6,391 queued applications, or 10.00 percent. In the unit a review manager staffs against, it generates one review per 193 applications and each review stands behind roughly 174.4 million anonymized units of committed value, against one review per 2.6 applications and 1.5 million units in Repayment-Stress History, a ratio of 116.3.

The same segment carries the least verifiable file: a median of 2 previous applications and 16 instalment records against 10 and 49 in History-Rich Credit User, with 14.46 percent holding no bureau record. Its median loan-to-income ratio is 5.20 against 3.16 portfolio-wide, and its median payment-to-income ratio 22.0 against 16.3 percent.

**Corroboration**

Four checks were run. One supports the finding, one adds a third phase to it, one returned a negative result that is reported as one, and one is the strongest available control that the finding survives. A fifth was not available.

First, Phase 4 is methodologically independent of Phase 2: the queue is built on an unclipped matrix by five detectors whose thresholds are calibrated field by field, none reading loan size, so the gap between the two distributions cannot be an artifact of one procedure.

Second, Phase 3 supplies the mechanism, which is what makes this a three-phase finding rather than a two-phase one. If review attention is being allocated by how much history a file contains, that dependence should be visible in a phase that never looks at the queue. It is, twice. **The highest-Lift cross-source pattern that survives the identity screens is an observable card-utilization band implying a deep previous-application history, at Lift 2.67**, which is history depth predicting history depth. And the exposure control on the shortlisted rules measures the same dependence directly: the refusals-to-lateness pattern loses 81.5 percent of its excess association once instalment depth is held constant. Back in Phase 4, the queue rate inside each segment then follows file depth in exact rank order: **15 instalment records and 0.34 percent queued, 16 and 0.52 percent, 49 and 1.93 percent, 97 and 2.70 percent, an 8.03-fold spread across four segments**. Repayment-Stress History is excluded from that ordering on principle rather than convenience, since Control 5 already showed its queue share is largely the delinquency columns that named it. Two cautions belong with this: four segments cannot support a significance claim, and the ordering is an association across segments, not a demonstration that any individual thin file is under-reviewed.

Third, the hierarchical check does not corroborate the boundary and is reported as a negative result. BIRCH over all 356,255 applications agrees with K-Means at an Adjusted Rand Index of only 0.2572, with normalized mutual information 0.3667, because it places 74.59 percent of applications in one group rather than recovering five. An earlier version of this report quoted 0.4355 from a sampled Ward solution assigned by nearest centroid; that procedure produces the same convex partition shape K-Means produces, so it was measuring how close two sets of five centroids are and overstated agreement by 0.178. The honest reading is that no hierarchical method recovers this partition at any scale on this data, which the cluster-tendency diagnostics explain: the portfolio carries several overlapping segmentations, and every agglomerative linkage chains. What carries the segment instead is sample stability, not method agreement: two K-Means models fitted on disjoint halves label the same unseen applications at an Adjusted Rand Index of 0.955. The shares in this finding are computed on that partition, so they inherit its confidence and no more.

Fourth, the ranking survives the strongest available control. Removing the six delinquency fields that most influence the queue and re-running all five detectors redistributes the queue substantially, yet Larger-Loan Affordability still ranks first on committed value per review, at 3.23 against 1.76 for the next segment. The spread narrows from 116-fold to roughly 9-fold, which is the honest magnitude, and the ordering does not change.

The concentration figure was calibrated rather than asserted. Against a null of 34.62 percent and a ceiling of 60.72 percent, the share the same number of applications would carry if chosen purely by loan size, the observed 53.21 percent gives a capture ratio of 0.712 on a Gini of 0.363. Most of the raw concentration is a property of the amount distribution and would appear under almost any segmentation, which is why the concentration alone is not the claim; the claim is its alignment with two separately produced distributions.

No corroboration was possible for applicant performance, since no outcome column is read anywhere in this project.

**Business Implication**

This speaks to the affordability-verification standard for the high-amount cash-loan stream and to how review capacity is allocated across streams. Verification effort currently concentrates on applications carrying enough recorded history for a detector to react to, which are also the applications a reviewer could already assess from the file. The segment holding half the committed value is the one about which the file says least. The exposure is quiet: thin history presents as an absence of adverse signals, that absence presents as comfort, and a large loan can pass with less challenge than a smaller one carrying minor blemishes. In a market built around thin conventional files, that accumulates unverified affordability at the largest exposures. A secondary implication is fairness, since file depth tracks how long an applicant has had access to formal credit at all.

**Recommended Action**

Credit Policy should set a minimum affordability-verification standard for the high-amount stream that does not scale with file depth, applying it to applications in Larger-Loan Affordability with fewer than three previous applications on file, currently the median position and roughly half of its 123,344 applications. Those reviewers should request permitted supporting income evidence and test the scheduled payment under the approved lower-income scenario rather than proceeding on an absence of adverse history. Two supporting changes make it measurable: report committed amount and application volume as separate measures in the monthly pack, and re-plan review capacity against committed value per review with a stated tolerance for drift. Progress is a narrowing spread achieved by adding verification to the high-amount stream, not by removing it elsewhere.

### Finding 2

After standardising for the number of instalment records each applicant has on file, the association between at least three prior refused applications and recorded instalment lateness falls from a Lift of 1.351 to 1.065, and two further shortlisted patterns fall to or below a Lift of 1.0.

**Evidence**

Apriori (minimum Support 3 percent, minimum Confidence 35 percent, minimum Lift 1.20, maximum itemset length 3), cross-checked by FP-Growth and ECLAT, retained the portfolio-wide rule linking at least three prior refused applications to some recorded instalment lateness: Support 6.22 percent, Confidence 60.08 percent, Lift 1.351, covering 22,151 of 36,868 applications against a 44.47 percent portfolio baseline. A Lift of 1.351 means the condition raises the observed co-occurrence rate 35 percent above statistical independence; at face value that reads as a 15.6 percentage-point behavioural signal.

The two items are not independent of history depth. Requiring three refusals forces at least three previous applications, and `installments_payments` is a child of `previous_application`, so applicants meeting the condition carry 1.59 times the portfolio's instalment records. The consequent is at least one late instalment among all instalments on file, so a longer record set raises the observed rate with no difference in conduct.

Direct standardisation of the condition group to the portfolio's distribution of instalment depth, across five strata, moves Confidence to 47.36 percent and Lift to 1.065: **81.5 percent of the excess association is attributable to the quantity of history observed**, and the residual gap is 2.9 percentage points rather than 15.6. Two further patterns invert, from 1.228 to 0.977 and from 1.271 to 0.939. A Lift below 1.0 means the condition is associated with the outcome slightly less often than chance.

**Corroboration**

Apriori, FP-Growth, and ECLAT enumerated the raw rule identically with matching Support, Confidence, and Lift, so the starting figure is not an artifact of one search strategy, and the standardisation re-weights that same enumerated rule rather than mining again.

Two design features show the correction is not blanket shrinkage. Six of the twelve rules have a consequent that is a single application-time value, which cannot accumulate, and are returned unchanged by construction. Among the six that can accumulate, two score **higher** after standardisation, from 1.213 to 1.242 and from 1.238 to 1.272, meaning history depth had been masking them. A correction moving results in one direction only would warrant suspicion; this one moves them in both.

Null-invariant measures agree with the modest picture: Kulczynski runs 0.281 to 0.482 across the retained set, all below the 0.5 level for unrelated items, and this rule carries an Imbalance Ratio of 0.702, so the relationship is strongly one-directional.

The independence of the surviving bureau-to-score patterns was tested rather than assumed. Gradient-boosted models predicting each observed external score from bureau aggregates alone reach 0.049, 0.016, and 0.368. The first two are not reconstructible from bureau data, so rules joining them to bureau states connect genuinely different evidence; the third overlaps moderately and is carried as a caveat.

No corroboration was possible for a causal reading: a mechanism would require refusal reason codes and a time-ordered outcome, neither of which exists in the supplied files.

**Business Implication**

This speaks to the design of manual-underwriting review triggers and applies to every trigger phrased as an event ever having occurred. Such a trigger directs reviewer attention toward the bank's longest-standing applicants, who have had the most opportunity to accumulate a single blemish: an applicant who has repaid through fifteen prior schedules meets an "ever late" condition more readily than one with three schedules and a worse record. The operational consequence is reviewer hours spent on files informative about tenure rather than conduct; the governance consequence is a trigger difficult to defend if challenged. For a lender whose applicants vary widely in file depth, this is the default behaviour of any uncorrected cumulative measure, not an edge case.

**Recommended Action**

Manual Underwriting, together with the policy team that maintains the review-trigger catalogue, should retire the prior-refusals-to-lateness prompt as a standalone trigger, since at an adjusted Lift of 1.065 it does not justify reviewer time. Every remaining history-based trigger should be re-expressed as a rate over observed records, for example the share of instalments paid late, and normalised for the number of records on file before two applicants are compared. This applies to all applicants with any previous Home Credit relationship and most sharply to the 36,868 applications currently meeting the retired condition. Each existing internal trigger built on cumulative history should be subjected to the same standardisation before its next re-approval, and the check is simple: compare the average file depth of the applicants a trigger pulls against the portfolio average, where a sound trigger sits near 1.0 and the retired one sits at 1.59.

### Finding 3

The targeted-review queue holds 6,391 applications, 1.79 percent of the portfolio, including 126 carrying data-quality faults that no single-field test would surface, and the 45.17 percent of that queue sitting in Repayment-Stress History falls to 6.09 percent when the six delinquency fields defining that segment are withheld from the detectors.

**Evidence**

Five detectors were applied to every application: skew-adjusted IQR and calibrated Z-score on 32 continuous fields at a 1 percent per-field operating point; shrinkage Mahalanobis with Ledoit-Wolf covariance at an empirical 97.5th-percentile cut-off of 91.31; Isolation Forest at 0.05 contamination; and cross-fitted Local Outlier Factor at an empirical 97.5th-percentile cut-off. Records enter through two routes: 3,983 on agreement among at least three of five, and 2,408 on a single value at least 10 standard deviations from the mean, totalling 6,391. That 1.79 percent is a workload a review function can absorb; the textbook 1.5 interquartile-range fence would have flagged 19.17 percent.

Within the queue, 6,224 applications raise an affordability or repayment question, 126 a data or source-reconciliation question, and 41 are rare but plausible. The clearest data-quality case, application 161584 in Appendix C, records an average paid-to-due ratio of 1,272.58 times, 45.8 standard deviations from the mean, which is physically implausible and would distort any affordability calculation on that file. The typology is assigned by the reference each record is measured against rather than by elimination: 4,334 point outliers are extreme against the whole portfolio; 1,982 contextual outliers are ordinary portfolio-wide but do not fit the shape of their own segment, of which 1,489 sit at least three robust deviations from their segment median and 493 are unusual only as a combination; and 75 collective outliers form 11 mutually linked groups whose members sit closer to each other than any of them sits to the ordinary portfolio.

Repayment-Stress History, 2.14 percent of the portfolio, holds 2,887 queued applications, 45.17 percent of the queue. Withholding the six delinquency fields (`INST_DPD_MEAN`, `INST_DPD_MAX`, `INST_LATE_RATIO`, `INST_SEVERE_LATE_RATIO`, `POS_SK_DPD_MEAN`, `CC_SK_DPD_MEAN`) and re-running all five detectors leaves that segment with 6.09 percent of the queue, a retained ratio of 0.135, while History-Rich Credit User rises from 15.55 to 29.95 percent and Historical Card-Use Intensity from 23.02 to 38.55 percent.

**Corroboration**

The queue is built on multi-method agreement, and that agreement is informative rather than mechanical: pairwise Jaccard overlap between the five detectors ranges from 4.7 to 25.7 percent, so a record admitted on three-of-five agreement has satisfied three materially different definitions of unusual. Of 27,740 applications flagged by at least one detector, 10,301 were flagged by two or more, and the queue is the subset where agreement or a single extreme value justifies review.

The 126 data-quality records are corroborated by construction rather than statistically. Each is flagged by a deterministic check against unscaled source values: a non-positive amount, an age outside a feasible range, tenure exceeding feasible working life, a payment ratio outside a plausible band, or a score outside its documented zero-to-one range. These do not depend on any threshold choice.

The segment-concentration element was tested and did not survive as independent evidence. The leave-one-family-out result shows the segmentation and the detector ensemble were reading the same six fields, so the apparent convergence of two methods on one group is one signal expressed twice. This report therefore withdraws the claim that the queue independently identifies which segment needs specialist attention. The records themselves remain valid: those applications do carry extreme recorded delinquency values.

A fourth check comes from Phase 2 and is genuinely independent, because DBSCAN reads the clipped clustering matrix while the detectors read the unclipped anomaly matrix. Density in that separate space marks **3,875 of the 6,391 queued applications (60.63 percent) as isolated, against 3.48 percent of the portfolio**, an enrichment of 17.4 times, and the effect is stronger on the consensus route (74.2 percent) than on the single-axis route (38.2 percent), which is the direction a multivariate density measure should move. That supports the queue as a whole and nothing narrower. It cannot support the collective category, for two separate reasons. First it does not discriminate at that resolution: among the 2,057 queued records eligible for the group test it flags 1,469, or 71.4 percent, where the dedicated group test flags 75. Second the density result is partly a property of the space it is read in, since the same applications judged in a UMAP embedding give a noise set agreeing at a Jaccard of 0.043. This is why the collective category comes from a dedicated group test in the detection space rather than from DBSCAN noise, and why the density flag never votes in admission.

**Business Implication**

This speaks to two operational decisions. First, data-operations ownership: 126 applications carry values that cannot be correct, and an unreconciled fault of that kind distorts every affordability calculation later performed on that file. That is a defined correction task with an unambiguous owner and a measurable end state. Second, review-workforce planning: a staffing case treating the Phase 2 segment result and the Phase 4 queue result as two independent reasons to fund a specialist team counts one reason twice, and would over-provision the stream Finding 1 shows already receives the most attention per unit of committed value. The independent components of this queue are the data-quality lane and the single-axis extreme route, neither of which depends on which fields defined a segment.

**Recommended Action**

Data Operations should take the 126 source-reconciliation applications as a closed correction task, verifying sign, units, joins, reversals, and duplicate rows on each before it proceeds to credit assessment, and recording each outcome as a confirmed error or a confirmed value. Review Operations should run the remaining 6,265 as a controlled workload in two lanes: repayment-timeline review for Repayment-Stress History, and confirming whether a historical revolving facility remains open for Historical Card-Use Intensity. Segment-based and queue-based staffing estimates must be reconciled rather than summed, with the shared-field overlap stated in the staffing paper, and outcomes logged by entry route so the two cut-offs can be reset on observed yield rather than capacity.

## Limitations

This section states the boundaries of what the analysis can and cannot claim. It is not a defence of the work.

One limitation governs everything built on the segments, so it is stated before the subsections rather than inside one. **This portfolio does not contain a single natural segmentation, and the five segments are one defensible cut through several.** Clustered on its own, card history separates at a Silhouette Score of 0.8452 and instalment delinquency at 0.6849, against 0.1542 when all 41 governed features are used together. Each family draws a different, strong, and mutually incompatible line through the same applications: card history splits the portfolio into applicants with and without a card record, delinquency into those with and without recorded lateness, and affordability varies continuously with no gap anywhere. One Euclidean partition cannot serve three of those at once, and the low combined score is that compromise rather than a failed run. Findings 1 and 3 both read shares off this partition and therefore inherit the limit: the shares are correct for this cut and would differ under a segmentation built on one family alone.

A second, narrower caution belongs with it, because it changes how every silhouette in this report should be read. **A Silhouette Score on this data cannot be compared with a textbook threshold.** On the same rows, a column-wise shuffle that destroys all joint structure while preserving every marginal distribution scores 0.6740 at K = 2, well above the real data, by isolating 0.91 percent of applications against the remaining 99.09 percent. Silhouette rewards that degenerate split, so a high value here would be evidence of a skewed axis rather than of structure. The defensible comparison is against the null on the same data, and by that comparison the operating resolution clears both nulls (0.1542 against 0.1103 shuffled and 0.1029 uniform) by a margin that is real but small.

### Scope of Outlier Detection

All three types were searched for, but not to equal confidence.

**Point outliers** were assessed across the full portfolio by five detectors and are the most secure category. Their weakness is that both admission routes use operating points chosen for review volume, not estimated from any known rate of error, because none exists in this data.

**Contextual outliers** are measured against each record's own Phase 2 segment rather than assigned by elimination. The reference is nonetheless a K-Means partition with a Silhouette Score of 0.148 and a K-Means-to-BIRCH Adjusted Rand Index of 0.2572, so a peer group here is a statistical convenience rather than a natural population, and a record's contextual status would change under a different but equally defensible partition. Of 1,982 contextual records, 493 rest on multivariate agreement with no single field beyond three robust deviations from its segment centre, so for those the label describes an unusual combination rather than an identifiable unusual value.

**Collective outliers** remain the weakest category. They come from a dedicated group test in the detection space rather than from DBSCAN noise, which removes the projection dependence, and every queued record that is not already a point outlier is eligible, so the coverage gap an earlier version carried is closed. Two limits remain. The test is confined to the review queue, so a jointly unusual group where no member reached the queue would not be found, and only 75 records in 11 groups qualify. And **no aggregate time-window feature was built** to detect collective anomalies across the raw transaction-level histories, which is the analysis that would make this category strong rather than merely defensible. The density view that previously supplied this label now covers the whole portfolio but still cannot replace the group test: it marks 71.4 percent of the eligible records as isolated, and it agrees with a UMAP repeat of itself at a Jaccard of 0.043.

The queue has no verified ground truth, so its thresholds set review volume rather than measure a true anomaly rate, and the detectors see only 41 prepared applicant-level fields: collusion across applicants or document forgery is invisible.

### Correlation versus Causation

The association rules in Phase 3, and every finding drawn from them, establish co-occurrence and not causation.

Finding 2 is where a causal reading is most tempting, and the competing non-causal explanation is quantified rather than only named. It would be natural to read prior refusals as a cause of later lateness, or both as symptoms of one underlying risk; neither is supported. Because the instalment table is a child of the previous-application table, applicants meeting the refusal condition carry 1.59 times the portfolio's instalment records, and the consequent is at least one late instalment among all on file. Standardising for that confound removes 81.5 percent of the excess association, leaving a 2.9 percentage-point co-occurrence with no established mechanism.

Standardisation removes that one confound and no other: product mix and past approval policy still shape which combinations can be observed, and neither is controlled. Four retained rules link bureau-derived fields to external scores of undocumented construction; bureau records explain 4.9 and 1.6 percent of the first two scores but 36.8 percent of the third, so rules involving the third carry a partial-restatement caveat the others do not.

Finding 1 carries the same caution differently. The amount concentration describes the segment collectively and says nothing about whether any individual applicant within it is less affordable; treating a group average as an individual property would be an ecological fallacy. Finding 1 also deliberately avoids asserting why scrutiny and committed value are misaligned: it states that they are misaligned and that the detectors do not read loan size, without claiming that thin files cause low review rates.

Finding 3 withdraws a claim on exactly these grounds. An earlier version presented the segmentation and the anomaly queue as two independent methods converging on one customer group. The leave-one-family-out test showed they were reading the same six columns, so the convergence was one signal expressed twice and cannot serve as corroboration.

### Dataset Representativeness

The portfolio is the supplied set of 356,255 applications: people who applied to Home Credit, passed whatever intake occurred, and reached the recorded files. It says nothing about applicants who never applied, applied elsewhere, or were filtered before recording, so every share is conditional on that intake.

The competition data is a historical extract of unspecified collection dates, so no age-of-data claim can be made and segment sizes would shift under a different intake policy, product mix, or economic period. The geographic scope is a single lender's market and is not stated at country or region level, so nothing should be generalized to other markets. Amounts are anonymized without currency or payment-frequency metadata, so no absolute monetary claim survives outside this dataset; the 174.4 million units behind each review in Finding 1 is meaningful only as a ratio against the 1.5 million units elsewhere in the same data.

Source-table exposure is uneven by construction, since the behavioural tables are children of the previous-application table. That is the confound Finding 2 corrects for, and it still colours any statement about observed history.

Several source fields were deliberately excluded and their absence bounds the analysis. Gender, age, family status, region rating, education, income type, organisation type, and social-circle arrears are held out as protected or proxy attributes, so no finding can describe how segments differ on those dimensions even where a difference exists and would matter for fairness monitoring. The first external score is excluded from the mining matrices, so whatever it measures reaches the segments only through its availability flag.

### What Additional Data Would Improve These Findings

Six additions would allow stronger conclusions, in order of how much each would change.

**Verified income and current obligations**, rather than declared income, would convert the amount concentration in Finding 1 from a coverage observation into a measurable affordability control and would test directly whether thin-file, high-amount applications are under-verified. This is the single most valuable addition.

**Account open or closed flags with closure dates** on card and bureau records would resolve the central uncertainty in the Historical Card-Use Intensity segment, whether an intense historical facility is still live. Every recommendation for that segment currently begins by asking a reviewer to establish something the data should already contain.

**Refusal reason codes** on previous applications would let Finding 2 move from a retired trigger to an operational rule; the exposure correction removes the confound but leaves the residual pattern uninformative without knowing why an application was refused.

**Recorded outcomes of the review queue itself**, meaning confirmed errors, verified rare cases, and no-issue results per entry route, would let the anomaly thresholds be tuned on real review yield rather than review capacity. Nothing in this project can currently establish that a queued application was worth reviewing.

**Construction documentation for the external scores** would settle whether the bureau-to-score patterns are independent findings or partial restatements, replacing a statistical provenance test with a definitive answer.

**Transaction timestamps with explicit currency, unit, and schema metadata** would enable the time-window aggregation collective outlier detection needs and convert several data-quality checks from statistical inference into deterministic validation.

One known defect is recorded rather than resolved: the residual correlation of 0.891 between mean and maximum historical card utilization was retained on the argument that one describes sustained and the other peak use. That argument is reasonable but untested, and a sensitivity run with one removed would settle it.

Finally, the boundary of use. Segment membership, association patterns, and queue entry are prompts for documented human review. None approves, declines, prices, ranks, or changes a limit, and none may be used as an adverse-action reason. Before operational use this work would need a time-based stability check, segment drift monitoring, rule and queue-yield monitoring, a fairness assessment across permitted groups, and lineage and recency controls on external-score inputs.

## Appendix

All full technical outputs are here. The Findings section references these appendices but does not reproduce them.

### Appendix A: Full Cluster Profiles

The five K-Means segments and the DBSCAN noise population are profiled below. Sizes: Lower-Intensity Credit Footprint 119,127 applications (33.44 percent); Repayment-Stress History 7,626 (2.14 percent); History-Rich Credit User 51,614 (14.49 percent); Larger-Loan Affordability 123,344 (34.62 percent); Historical Card-Use Intensity 54,544 (15.31 percent). The DBSCAN noise population is 12,402 records, 3.48 percent of the portfolio, profiled against all 356,255 applications because the density view now assesses every one of them; it is a density state and not an anomaly label, and it overlaps the segments rather than competing with them. The recommended action per segment appears in Appendix E. Numeric features are shown as mean with standard deviation in parentheses; flag, ordinal, and frequency-encoded features are shown as the modal value with the share of the population holding it. Amounts are in anonymized currency units. The complete export is [`segment_full_profiles.csv`](results/phase2_clustering/segment_full_profiles.csv).

**A1. Numeric features: mean (standard deviation)**

| Feature | Lower-Int | Repay-Stress | Hist-Rich | Larger-Loan | Card-Use | DBSCAN noise |
|---|---:|---:|---:|---:|---:|---:|
| AMT_INCOME_TOTAL | 140,942 (68,868) | 155,236 (77,050) | 188,887 (86,991) | 179,537 (89,442) | 179,955 (84,370) | 169,726 (92,882) |
| AMT_CREDIT | 276,632 (121,054) | 567,700 (368,674) | 525,673 (310,605) | 903,333 (375,831) | 615,258 (367,523) | 613,135 (424,707) |
| AMT_ANNUITY | 17,309 (7,647.5) | 26,606 (13,317) | 27,192 (13,243) | 37,189 (14,671) | 27,774 (13,153) | 28,847 (15,568) |
| CREDIT_TO_INCOME | 2.215 (1.066) | 4.051 (2.716) | 3.031 (1.756) | 5.794 (2.808) | 3.806 (2.443) | 4.292 (3.545) |
| ANNUITY_TO_INCOME | 0.138 (0.065) | 0.191 (0.096) | 0.158 (0.074) | 0.237 (0.102) | 0.172 (0.086) | 0.200 (0.123) |
| CREDIT_TO_ANNUITY | 16.750 (5.484) | 21.022 (7.890) | 19.545 (7.094) | 25.329 (7.596) | 21.901 (7.660) | 20.673 (8.119) |
| YEARS_EMPLOYED | 5.557 (5.762) | 7.013 (6.704) | 6.971 (6.422) | 7.132 (6.805) | 6.974 (6.390) | 7.177 (6.742) |
| OWN_CAR_AGE | 3.850 (9.134) | 4.194 (9.060) | 3.966 (8.755) | 4.429 (9.104) | 3.913 (8.418) | 9.138 (16.933) |
| EXT_SOURCE_2 | 0.490 (0.195) | 0.500 (0.193) | 0.512 (0.189) | 0.540 (0.180) | 0.518 (0.190) | 0.493 (0.199) |
| EXT_SOURCE_3 | 0.522 (0.170) | 0.502 (0.179) | 0.459 (0.188) | 0.541 (0.165) | 0.491 (0.176) | 0.445 (0.199) |
| BUREAU_COUNT | 3.906 (3.901) | 4.776 (4.400) | 6.958 (5.553) | 4.520 (4.132) | 5.463 (4.955) | 5.760 (5.375) |
| BUREAU_ACTIVE_RATIO | 0.346 (0.338) | 0.342 (0.313) | 0.382 (0.285) | 0.333 (0.314) | 0.382 (0.314) | 0.380 (0.318) |
| BUREAU_DEBT_TO_CREDIT_RATIO | 0.233 (0.295) | 0.233 (0.285) | 0.284 (0.279) | 0.216 (0.571) | 0.277 (0.296) | 0.273 (0.309) |
| BUREAU_DAYS_CREDIT_MEAN | -819.2 (648.8) | -988.6 (661.6) | -1,033.7 (561.4) | -973.3 (653.6) | -970.0 (626.9) | -1,054.9 (647.3) |
| BUREAU_BB_DPD_RATIO_MEAN | 0.005 (0.028) | 0.017 (0.067) | 0.010 (0.040) | 0.005 (0.026) | 0.007 (0.031) | 0.058 (0.108) |
| PREV_APPROVAL_RATE | 0.762 (0.300) | 0.735 (0.277) | 0.511 (0.225) | 0.752 (0.319) | 0.673 (0.254) | 0.612 (0.297) |
| INST_DPD_MEAN | 0.435 (1.080) | 25.190 (53.113) | 0.617 (1.099) | 0.387 (1.008) | 0.467 (0.784) | 11.843 (42.177) |
| INST_DPD_MAX | 4.539 (12.493) | 474.4 (539.8) | 11.027 (26.128) | 4.346 (12.685) | 14.586 (31.513) | 246.2 (451.9) |
| INST_COUNT | 20.090 (16.925) | 42.689 (36.095) | 55.277 (35.103) | 21.080 (18.553) | 99.615 (52.715) | 72.729 (56.380) |
| INST_LATE_RATIO | 0.064 (0.113) | 0.298 (0.194) | 0.091 (0.108) | 0.057 (0.105) | 0.066 (0.076) | 0.177 (0.165) |
| INST_SEVERE_LATE_RATIO | 0.001 (0.006) | 0.075 (0.066) | 0.002 (0.007) | 0.001 (0.006) | 0.001 (0.006) | 0.028 (0.052) |
| INST_PAYMENT_RATIO_MEAN | 1.177 (18.742) | 1.983 (97.131) | 1.816 (42.005) | 1.233 (23.366) | 1.113 (6.447) | 3.332 (94.724) |
| POS_SK_DPD_MEAN | 1.097 (33.263) | 94.116 (219.9) | 4.634 (72.104) | 1.965 (46.219) | 2.181 (44.313) | 69.548 (228.0) |
| POS_MONTHS_COUNT | 20.096 (15.962) | 41.959 (28.674) | 53.154 (32.379) | 21.020 (17.167) | 35.773 (27.354) | 48.425 (35.966) |
| CC_UTILIZATION_MEAN | 0.007 (0.049) | 0.059 (0.161) | 0.018 (0.079) | 0.005 (0.038) | 0.550 (0.262) | 0.251 (0.327) |
| CC_UTILIZATION_MAX | 0.019 (0.118) | 0.170 (0.376) | 0.059 (0.209) | 0.018 (0.111) | 1.008 (0.128) | 0.490 (0.510) |
| CC_SK_DPD_MEAN | 0.025 (1.789) | 19.942 (84.586) | 0.010 (0.967) | 0.025 (3.198) | 4.890 (51.519) | 21.570 (96.672) |
| CC_AMT_BALANCE_MEAN | 1,039.6 (7,964.1) | 9,299.8 (36,867) | 3,550.5 (16,249) | 1,060.4 (8,044.0) | 123,524 (123,453) | 53,702 (103,627) |
| CC_MONTHS_COUNT | 2.183 (9.012) | 14.523 (30.684) | 7.360 (16.954) | 3.127 (12.184) | 49.572 (35.388) | 29.044 (36.697) |
| GOODS_TO_CREDIT | 0.913 (0.121) | 0.894 (0.098) | 0.900 (0.104) | 0.897 (0.085) | 0.883 (0.095) | 0.893 (0.093) |
| YEARS_BIRTH | 42.502 (13.103) | 44.977 (11.351) | 45.732 (12.160) | 44.445 (11.142) | 44.154 (10.464) | 44.987 (11.070) |
| SOURCE_EXT_SOURCE_1 | 0.464 (0.213) | 0.497 (0.205) | 0.508 (0.210) | 0.530 (0.204) | 0.513 (0.205) | 0.506 (0.204) |
| SOURCE_EXT_SOURCE_2 | 0.490 (0.195) | 0.500 (0.193) | 0.512 (0.189) | 0.540 (0.181) | 0.518 (0.190) | 0.493 (0.199) |
| SOURCE_EXT_SOURCE_3 | 0.518 (0.195) | 0.494 (0.200) | 0.451 (0.196) | 0.543 (0.184) | 0.482 (0.193) | 0.431 (0.211) |
| SOURCE_AMT_INCOME_TOTAL | 142,607 (346,730) | 156,118 (82,084) | 191,423 (105,838) | 183,439 (132,431) | 181,866 (99,320) | 172,475 (111,635) |
| SOURCE_AMT_CREDIT | 276,632 (121,054) | 567,700 (368,674) | 525,673 (310,605) | 903,333 (375,831) | 615,258 (367,523) | 613,135 (424,707) |
| SOURCE_AMT_ANNUITY | 17,309 (7,647.5) | 26,606 (13,317) | 27,192 (13,243) | 37,189 (14,671) | 27,774 (13,153) | 28,847 (15,568) |
| SOURCE_AMT_GOODS_PRICE | 250,904 (111,078) | 506,970 (337,286) | 472,844 (286,591) | 812,586 (356,336) | 544,505 (335,903) | 548,389 (390,214) |

**A2. Categorical and flag features: modal value (share of population)**

| Feature | Lower-Int | Repay-Stress | Hist-Rich | Larger-Loan | Card-Use | DBSCAN noise |
|---|---:|---:|---:|---:|---:|---:|
| FLAG_SENTINEL_EMPLOYED | 0 (80%) | 0 (80%) | 0 (78%) | 0 (83%) | 0 (86%) | 0 (81%) |
| NAME_CONTRACT_TYPE | 1 (81%) | 1 (95%) | 1 (93%) | 1 (98%) | 1 (99%) | 1 (98%) |
| FLAG_NO_CAR | 1 (70%) | 1 (67%) | 1 (65%) | 1 (62%) | 1 (67%) | 1 (57%) |
| FLAG_NO_HOUSING_DATA | 0 (50%) | 1 (54%) | 0 (54%) | 0 (53%) | 0 (53%) | 1 (51%) |
| FLAG_EXT_SOURCE_1_MISSING | 1 (56%) | 1 (58%) | 1 (55%) | 1 (54%) | 1 (52%) | 1 (54%) |
| FLAG_EXT_SOURCE_2_MISSING | 0 (100%) | 0 (100%) | 0 (100%) | 0 (100%) | 0 (100%) | 0 (100%) |
| FLAG_EXT_SOURCE_3_MISSING | 0 (75%) | 0 (79%) | 0 (91%) | 0 (80%) | 0 (83%) | 0 (86%) |
| AMT_REQ_CREDIT_BUREAU_YEAR | 1 (41%) | 1 (37%) | 3 (19%) | 1 (38%) | 1 (28%) | 1 (26%) |
| FLAG_NO_BUREAU | 0 (81%) | 0 (85%) | 0 (95%) | 0 (86%) | 0 (88%) | 0 (92%) |
| BUREAU_BB_SEVERE_DPD_MEAN | 0.000 (0.012) | 0.005 (0.038) | 0.001 (0.020) | 0.001 (0.013) | 0.001 (0.015) | 0.016 (0.065) |
| PREV_COUNT | 1 (24%) | 4.287 (3.348) | 10.751 (5.125) | 2.954 (2.214) | 6.630 (4.328) | 7.707 (6.626) |
| PREV_REFUSED_COUNT | 0 (79%) | 0 (61%) | 2.934 (3.101) | 0 (82%) | 1.186 (1.985) | 2.257 (3.588) |
| CNT_CHILDREN | 0 (69%) | 0 (69%) | 0 (73%) | 0 (69%) | 0 (71%) | 0 (70%) |
| REGION_RATING_CLIENT_W_CITY | 2 (76%) | 2 (77%) | 2 (76%) | 2 (72%) | 2 (74%) | 2 (75%) |
| NAME_EDUCATION_TYPE | 1 (72%) | 1 (76%) | 1 (73%) | 1 (67%) | 1 (73%) | 1 (73%) |
| NAME_INCOME_TYPE_FREQ | 0.514539 (54%) | 0.514539 (52%) | 0.514539 (48%) | 0.514539 (50%) | 0.514539 (52%) | 0.514539 (51%) |
| ORGANIZATION_TYPE_FREQ | 0.27434 (27%) | 0.27434 (25%) | 0.27434 (26%) | 0.27434 (28%) | 0.27434 (29%) | 0.27434 (26%) |
| DEF_30_CNT_SOCIAL_CIRCLE_BIN | 0 (89%) | 0 (87%) | 0 (87%) | 0 (89%) | 0 (87%) | 0 (86%) |
| CODE_GENDER | 1 (65%) | 1 (67%) | 1 (68%) | 1 (66%) | 1 (67%) | 1 (66%) |
| SOURCE_AMT_REQ_CREDIT_BUREAU_MON | 0 (90%) | 0 (88%) | 0 (84%) | 0.209 (0.833) | 0 (85%) | 0 (84%) |
| SOURCE_AMT_REQ_CREDIT_BUREAU_QRT | 0 (83%) | 0 (83%) | 0 (73%) | 0 (82%) | 0 (79%) | 0 (78%) |
| SOURCE_AMT_REQ_CREDIT_BUREAU_YEAR | 1 (41%) | 1 (37%) | 3.658 (2.159) | 1 (38%) | 2.598 (1.876) | 1 (26%) |

The noise profile is worth a short interpretation, because it says what density actually separates on. Measured in portfolio standard deviations, the isolated applications sit at +0.94 on the share of instalments paid late, +0.84 on the number of instalment records, +0.80 on previous refusals, +0.70 on average card utilization, and +0.69 on previous applications, but only +0.03 on recorded loan amount and +0.08 on scheduled payment. Density in this space is therefore separating on depth and quality of recorded history, not on borrowing scale: on the readable scale these records average 73 instalment records against 20 for the largest segment, a longest instalment delay of 246 days against 4.5, and a late-instalment share of 17.7 percent against 6.4. That is a coherent population, which is exactly why it is reported as a density state rather than as an anomaly label: sitting in a sparse neighbourhood of a history-rich region is not by itself a reason for review, and 12,402 applications is far more than a review function could absorb.

### Appendix B: Full Association Rule Table

All 12 retained rules, ranked by Lift descending. Support, Confidence, and Lift use each rule's own context as denominator, portfolio-wide or the named segment, as registered in [`business_rules_final.csv`](results/phase3_association/business_rules_final.csv). Band definitions are analytical categories from Phase 3, not policy thresholds.

The two right-hand columns carry information Lift cannot. **Adjusted Lift** re-measures a rule with history depth held constant, and applies only where the consequent is an accumulation state that a longer customer relationship could inflate; a consequent that is a single application-time value is marked not applicable. **Kulczynski** is a null-invariant measure, so it does not depend on how many applications lack both items; 0.5 indicates unrelated items. Where raw and adjusted Lift differ materially, the adjusted figure is the one this report treats as the finding.

| Antecedent | Consequent | Context | Support | Confidence | Lift | Adjusted Lift | Kulczynski |
|---|---|---|---:|---:|---:|---:|---:|
| Bureau debt at least 80% of bureau credit | External scores in the lower band | Lower-Intensity | 3.62% | 55.9% | 1.475 | not applicable | 0.327 |
| Observed average card utilization at least 80% | External scores in the lower band | Card-Use | 10.30% | 47.1% | 1.362 | not applicable | 0.384 |
| At least three prior refused applications | Some recorded instalment lateness | Portfolio-wide | 6.22% | 60.1% | 1.351 | **1.065** | 0.370 |
| Bureau debt 30% to 80% plus at least three prior refusals | External scores in the lower band | History-Rich | 8.77% | 52.0% | 1.335 | not applicable | 0.373 |
| Loan in upper third plus at least 75% prior approvals | External scores in the upper band | Card-Use | 6.86% | 41.1% | 1.323 | not applicable | 0.316 |
| Loan in upper third plus no recorded lateness | External scores in the upper band | Portfolio-wide | 6.14% | 42.9% | 1.289 | not applicable | 0.307 |
| Card utilization below 80% plus at least 75% prior approvals | Some recorded instalment lateness | Lower-Intensity | 3.48% | 46.7% | 1.271 | **0.939** | 0.281 |
| Bureau debt 30% to 80% plus external scores in the upper band | Scheduled payment below 20% of income | Larger-Loan | 4.38% | 51.3% | 1.243 | not applicable | 0.310 |
| Observed instalments with no recorded lateness | Mixed prior-application outcomes | Card-Use | 10.13% | 49.2% | 1.238 | 1.272 | 0.373 |
| Payment below 20% of income plus external scores in the lower band | Bureau debt 30% to 80% of bureau credit | History-Rich | 13.22% | 44.7% | 1.237 | 1.213 | 0.406 |
| Loan above six times income plus no recorded lateness | At least 75% prior approvals | Portfolio-wide | 4.94% | 64.4% | 1.228 | **0.977** | 0.369 |
| External scores in the upper band | Bureau debt below 30% of bureau credit | History-Rich | 17.03% | 64.3% | 1.213 | 1.242 | 0.482 |

Six of the twelve rules have an accumulation consequent and are re-measured; the other six are unchanged by construction because their consequent is a single application-time value. Of the six re-measured, three in bold lose at least half of their excess Lift once history depth is held constant, and two of those fall below 1.0, meaning the condition carries no information. Two rules gain, from 1.213 to 1.242 and from 1.238 to 1.272, and one falls slightly, from 1.237 to 1.213. That the correction moves results in both directions is what shows it is not a blanket shrinkage.

Exposure variable per consequent family: `INST_COUNT` for instalment states, `PREV_COUNT` for previous-application states, `CC_MONTHS_COUNT` for card states, `BUREAU_COUNT` for bureau states, and none for income, loan size, leverage, burden, and external-score states. Full working is in [`rule_exposure_adjustment.csv`](results/phase3_association/rule_exposure_adjustment.csv) and [`rule_interestingness_measures.csv`](results/phase3_association/rule_interestingness_measures.csv).

**External-score provenance test.** The cross-source screen treats external scores and bureau history as different sources, which is an assumption. Gradient-boosted models predicting each observed score from one source alone, scored on a held-out subset, give:

| Score | Observed applications | Explained by bureau records alone | Explained by application fields alone | Verdict |
|---|---:|---:|---:|---|
| EXT_SOURCE_1 | 162,345 | 0.049 | 0.069 | Not reconstructible from bureau data |
| EXT_SOURCE_2 | 355,587 | 0.016 | 0.037 | Not reconstructible from bureau data |
| EXT_SOURCE_3 | 286,622 | 0.368 | 0.036 | Partly overlapping; carried as a caveat |

### Appendix C: Anomaly Detection Results

Representative queue records covering every outlier type, every typology basis, and every review type. IQR and Z-score report the number of continuous fields that triggered, where a record signals at three or more. Mahalanobis reports the squared distance. Isolation Forest reports its score, where more negative is easier to isolate. Local Outlier Factor reports its score, where above roughly 1.5 is materially sparse. DBSCAN reports each record's portfolio density status and never affects admission. The typology basis states the evidence that earned the label rather than the route that admitted the record. The full table of all 6,391 queue records is [`anomaly_investigation.csv`](results/phase4_anomaly/anomaly_investigation.csv).

| Record ID | Methods flagged by | Key scores | Outlier type | Typology basis | Business interpretation |
|---:|---|---|---|---|---|
| 161584 | IQR (3), Z-score (3), Mahalanobis, LOF | D-sq 2,301; ISO -0.470; LOF 12.69 | Point | Portfolio: average paid-to-due ratio at +45.8 SD | An average paid-to-due ratio of 1,272.58 times is physically impossible and would distort any affordability calculation taken from this file. Reconcile instalment rows, reversals, duplicates, and units before assessment. This is the clearest data-quality case in the queue and the one Finding 3 cites. Data consistency check. |
| 345161 | IQR (3), Z-score (3), Mahalanobis, IsoForest, LOF | D-sq 1,178; ISO -0.523; LOF 3.20 | Point | Portfolio: previous refusal count at +29.6 SD | 54 recorded prior refusals is far outside any plausible application history; reconcile the previous-application join and check for duplicated rows before the file is assessed. Data consistency check. |
| 100784 | IQR (5), Z-score (4), Mahalanobis, IsoForest, LOF | D-sq 628; ISO -0.590; LOF 2.74 | Point | Portfolio: payment-to-income at +12.6 SD | Scheduled payment equals 137.4 percent of declared income, which no affordability policy could accept as stated; verify income and current obligations. Affordability review. |
| 265042 | IQR (4), Z-score (4), Mahalanobis, IsoForest, LOF | D-sq 240; ISO -0.536; LOF 1.83 | Point | Portfolio: 295 POS or cash-loan months at +10.8 SD | An extreme but physically possible depth of history; confirm the source, then continue standard review. Rare but plausible. |
| 100205 | IQR (3), Z-score (6), Mahalanobis, IsoForest, LOF | D-sq 119; ISO -0.583; LOF 1.48 | Contextual | Segment: loan-to-income 4.4 robust deviations from its segment median | Loan equals 12.8 times income with a 356-day longest instalment delay. Ordinary for the portfolio, not for this peer group. Affordability review. |
| 177061 | IQR (3), Z-score (3), Mahalanobis, IsoForest, LOF | D-sq 114; ISO -0.578; LOF 1.52 | Contextual | Segment: paid-to-due ratio 146.0 robust deviations from its segment median | A 3.65x mean paid-to-due ratio is plausible portfolio-wide but not inside this segment; reconcile reversals, duplicates, and units on the instalment source. Data consistency check. |
| 237453 | IQR (3), Z-score (5), Mahalanobis, IsoForest, LOF | D-sq 121; ISO -0.621; LOF 1.50 | Contextual | Combination: no single field beyond 3 robust deviations; five detectors agree | No individual value is impossible, but the combined delay, utilisation, and history pattern is unusual under every multivariate view. Affordability review. |
| 232520 | IQR (3), Z-score (4), Mahalanobis, IsoForest, LOF | D-sq 193; ISO -0.633; LOF 1.86 | Collective | Group: member of a mutually linked group of 4 | Payment equals 70.1 percent of income at 21.9 times income leverage, and three other applications sit closer to this one than any of them sits to the ordinary portfolio. Verify the shared pattern before reviewing each file separately. |

Typology totals and the evidence that earned each label, from [`anomaly_typology_basis.csv`](results/phase4_anomaly/anomaly_typology_basis.csv):

| Outlier type | Basis | Records | Median peer deviation |
|---|---|---:|---:|
| Point (globally extreme single value) | Portfolio reference | 4,334 | 3.85 |
| Contextual (unusual against its own segment) | Segment reference | 1,489 | 5.85 |
| Contextual (unusual against its own segment) | Combination reference | 493 | 2.13 |
| Collective (mutually linked separated group) | Group reference | 75 | 3.46 |

The three types are disjoint by construction. Point takes precedence because a record extreme on its own needs no context to be called unusual. The collective test therefore runs only on the 2,057 queued records that are not point outliers, which is what makes its result informative: it asks whether records are unusual together while none is unusual alone. Of those, 206 sit in the top decile of distance from the ordinary portfolio, above a separation floor of 6.539, and 194 mutual nearest-neighbour links join 75 of them into 11 groups of three to fifty members; the largest holds 19 and no component was rejected for exceeding the ceiling. The Phase 2 DBSCAN density view, applied to the same question, flags 1,469 of those same 2,057 records. Its 72-record overlap with the group test covers 96 percent of the collective class, so the two agree about what they both flag, but at 71.4 percent of the eligible base the density view cannot select a group from a queue and is reported as corroboration rather than criterion.

### Appendix D: Evaluation Metrics Summary

One reference table of the quantitative evaluation metrics produced across all phases. Each value is written by the phase that produced it and re-checked by the validation script.

| Phase | Metric | Value |
|---|---|---|
| Phase 1 | Portfolio size | 356,255 applications |
| Phase 1 | Exact duplicate rows removed | 0 |
| Phase 1 | Mining features after selection | 41 (from 60 prepared business fields) |
| Phase 1 | Documented keep or drop decisions | 74 (41 keep, 33 drop) |
| Phase 1 | Columns removed by correlation redundancy | 31 |
| Phase 1 | Fields below 0.10 normalized unsupervised entropy | 18 of 120 scored |
| Phase 1 | Only candidate field dropped on entropy alone | FLAG_MOBIL, 0.0001 (99.999% share one value) |
| Phase 1 | Residual feature pairs with absolute correlation above 0.85 | 1 (card utilization mean vs max, 0.891) |
| Phase 2 | PCA components retained / cumulative variance | 10 / 64.79% |
| Phase 2 | Adjusted Rand Index, 10 PCs vs 16 / 21 / 41 dimensions | 0.970 / 0.971 / 0.969 |
| Phase 2 | Elbow method result | K = 5 |
| Phase 2 | Silhouette Score (primary method, final K) | 0.1478 |
| Phase 2 | Silhouette Score (K = 2 / K = 3 / K = 6 comparison points) | 0.2639 / 0.2681 / 0.1523 |
| Phase 2 | Per-segment Silhouette range | 0.084 (History-Rich) to 0.222 (Repayment-Stress) |
| Phase 2 | Davies-Bouldin index (K = 5) | 1.7241 |
| Phase 2 | Hopkins statistic (10 PCs / 41 dimensions / uniform control) | 0.8814 / 0.8338 / 0.4982 |
| Phase 2 | Null-model Silhouette at K = 5 (real / shuffled / uniform) | 0.1542 / 0.1103 / 0.1029 |
| Phase 2 | Degenerate null warning: shuffled Silhouette at K = 2 and its group split | 0.6740 on a 0.91% / 99.09% split |
| Phase 2 | Silhouette by feature family, clustered alone (card / delinquency / depth / affordability) | 0.8452 / 0.6849 / 0.3469 / 0.2643 |
| Phase 2 | Silhouette, all 41 governed features together (same sample) | 0.1542 |
| Phase 2 | Seed-to-seed Adjusted Rand Index (K = 5 / 6 / 7) | 0.997 / 0.743 / 0.900 |
| Phase 2 | Split-half Adjusted Rand Index (K = 5 / 6 / 7) | 0.955 / 0.670 / 0.815 |
| Phase 2 | Cophenetic Correlation (ward / complete / average) | 0.4627 / 0.6337 / 0.8022 |
| Phase 2 | Largest group share at K = 5 (ward / complete / average) | 33.7% / 94.1% / 98.8% |
| Phase 2 | Exact agglomerative clustering at full scale | Not computable: 63.46 billion distances, fails at 242 GiB |
| Phase 2 | BIRCH threshold / CF-tree subclusters (full portfolio) | 2.0 / 9,381 |
| Phase 2 | Adjusted Rand Index (K-Means vs Hierarchical, BIRCH over all 356,255) | 0.2572 |
| Phase 2 | Normalized mutual information (K-Means vs Hierarchical) | 0.3667 |
| Phase 2 | BIRCH largest group share | 74.59% |
| Phase 2 | Adjusted Rand Index, sampled Ward nearest-centre contrast (biased upward) | 0.4355 |
| Phase 2 | DBSCAN noise, full portfolio (operating view) | 12,402 of 356,255 (3.48%) in 9 pockets, eps 2.075 |
| Phase 2 | DBSCAN noise, UMAP picture (decides nothing) | 519 of 30,000 (1.73%) in 29 pockets, eps 0.102 |
| Phase 2 | DBSCAN noise agreement, UMAP vs PCA space | Jaccard 0.043 (67 shared of 1,547) |
| Phase 2 | Amount concentration: observed / null / ceiling / capture ratio | 53.21% / 34.62% / 60.72% / 0.712 |
| Phase 2 | Portfolio Gini of recorded loan amount | 0.363 |
| Phase 3 | Number of rules generated | 4,492 |
| Phase 3 | Number of rules retained after filtering | 12 |
| Phase 3 | Support range of retained rules (own context) | 3.48% to 17.03% |
| Phase 3 | Confidence range of retained rules | 41.1% to 64.4% |
| Phase 3 | Highest Lift value in retained rules | 1.475 |
| Phase 3 | Kulczynski range of retained rules | 0.281 to 0.482 |
| Phase 3 | Exposure-sensitive rules / losing half their excess Lift / falling below 1.0 | 6 of 12 / 3 / 2 |
| Phase 3 | Largest single exposure correction | Lift 1.351 to 1.065 (81.5% of excess was exposure) |
| Phase 3 | External score explained by bureau records (EXT_SOURCE_1 / 2 / 3) | 0.049 / 0.016 / 0.368 |
| Phase 4 | Mahalanobis review threshold (empirical 97.5%) | 91.31 |
| Phase 4 | Chi-square 99.9% threshold (df = 32) / diagnostic flag rate | 62.49 / 5.15% |
| Phase 4 | Calibrated IQR fence multiplier (per column) | median 1.42, range 0.30 to 990.69; 19 of 24 within 0.5 to 2.5 |
| Phase 4 | Calibrated absolute-Z threshold (per column) | median 2.78, range 0.05 to 6.68 |
| Phase 4 | Univariate columns abstaining on a zero-width box | 8 of 32 |
| Phase 4 | Conventional IQR 1.5x flag rate (rejected operating point) | 19.17% |
| Phase 4 | Conventional z above 3 flag rate (rejected operating point) | 2.28% |
| Phase 4 | Detector pairwise Jaccard overlap range | 4.7% (IQR vs Isolation Forest) to 25.7% (Z-score vs Mahalanobis) |
| Phase 4 | Total anomaly candidates before corroboration | 27,740 (7.79%) |
| Phase 4 | Candidates corroborated by two or more detectors | 10,301 (2.89%) |
| Phase 4 | Detector-consensus route (3 of 5) | 3,983 |
| Phase 4 | Extreme single-axis additions (10+ SD) | 2,408 |
| Phase 4 | Targeted review queue | 6,391 (1.79%) |
| Phase 4 | Outlier typology: point / contextual / collective | 4,334 / 1,982 / 75 |
| Phase 4 | Contextual records earned by segment reference / combination only | 1,489 / 493 |
| Phase 4 | Collective groups found / members | 11 / 75 |
| Phase 4 | Collective test: eligible / separated candidates / mutual links / flagged | 2,057 / 206 / 194 / 75 |
| Phase 4 | Density corroboration of the queue (noise share inside vs outside) | 60.63% of 6,391 against 3.48% of the portfolio (17.4x) |
| Phase 4 | Repayment-Stress queue share, full vs delinquency-free features | 45.17% to 6.09% (retained ratio 0.135) |
| Phase 4 | Committed value per review, highest vs lowest segment | 174.4M vs 1.5M anonymized units (116.3x) |
| Phase 4 | Committed value per review after the delinquency-free re-run | Ordering unchanged, spread narrows to roughly 9x |

The template lists a row comparing predictions against a label. That row is deleted rather than left blank: this project reads no outcome label at any point, so no label-based accuracy figure exists or could be produced without violating the project's stated scope. Evaluation rests instead on internal validity, seed and sample stability, dimensional and threshold sensitivity, multi-method agreement, and the six controls in Appendix G.

### Appendix E: Segment Recommended Actions and Governance

| Segment | Applications | Recommended review response |
|---|---:|---|
| Lower-Intensity Credit Footprint | 119,127 | Use standard underwriting and request permitted supporting evidence only where a relevant source is genuinely unavailable. This is not a thin-file group in the sense of having no evidence; its defining feature is lower product activity and smaller amounts. |
| Repayment-Stress History | 7,626 | Review timing, severity, recency, cure status, disputes, and current affordability, and follow hardship policy where verified. Note for staffing: this segment's 45.17 percent share of the review queue falls to 6.09 percent once the delinquency fields that define it are withheld, so the segment label and queue membership are the same evidence twice and must not be added. |
| History-Rich Credit User | 51,614 | Use the additional evidence to reconcile earlier refusals, arrears, and current obligations rather than assuming that more history is favourable or adverse. This segment has the weakest internal cohesion (per-segment Silhouette 0.084), so its boundary should not be treated as sharp. |
| Larger-Loan Affordability | 123,344 | Verify sustainable income and current obligations and test affordability under a lower-income scenario. This is the segment of Finding 1: it carries 53.21 percent of recorded loan value on a median of 2 previous applications and 16 instalment records, and receives 10.00 percent of the review queue. Its verification standard must not depend on how much history happens to exist. |
| Historical Card-Use Intensity | 54,544 | Confirm whether a revolving facility is still open before treating any historical balance or limit as current, then verify current balance, utilization, and arrears. |

Before any operational use, add a time-based stability check, segment drift monitoring, rule and queue-yield monitoring, a fairness assessment across permitted groups, lineage and recency controls on external-score inputs, and an explicit prohibition on using any segment, rule, or anomaly label as an adverse-action reason.

### Appendix F: Methods Considered and Rejected

Every substantive choice had a credible competitor. This register records what was tested, what it scored, and why it was not adopted. The six clustering-phase rows are exported with their full supporting numbers in [`method_alternatives_register.csv`](results/phase2_clustering/method_alternatives_register.csv), written by the phase that made those decisions; the remaining rows are documented in the phase that made them and are recorded here.

| Decision | Chosen | Alternatives tested | Why the alternative was rejected | Cost accepted |
|---|---|---|---|---|
| Number of segments | K = 5 | K = 2 to 10; three seeds and five split-half trials at K = 5, 6, 7 | K = 2 and K = 3 score higher on Silhouette but place over 81 percent of applications in one group; K = 6 edges K = 5 on Silhouette and Davies-Bouldin but reproduces at only 0.743 across seeds and 0.670 across disjoint halves | K = 5 is not the Silhouette optimum (0.148 against 0.268 at K = 3) |
| Hierarchical clustering at full scale | BIRCH over all 356,255 applications, threshold 2.0 | exact agglomerative clustering on all rows; Ward on a k-nearest-neighbour connectivity graph; BIRCH at thresholds 0.5 to 3.0; sampled Ward with nearest-centre assignment | Exact linkage needs 63.46 billion pairwise distances and fails with a 242 GiB allocation error; BIRCH at threshold 0.5 leaves about 254,000 subclusters and hits the same wall; the connectivity-graph agglomeration had not finished after 40 minutes; sampled nearest-centre assignment produces a convex partition of the shape K-Means produces and so biases the comparison toward agreement | BIRCH results depend materially on the threshold, and the full-portfolio solution places 74.6 percent of applications in one group, so it validates K-Means weakly rather than confirming it |
| Hierarchical linkage | Ward | complete, average, on the same 2,000-application sample | Average and complete chain 98.8 and 94.1 percent of the sample into one group at K = 5, which cannot support five review workflows | Ward has the lowest cophenetic correlation of the three at 0.463 |
| Clustering space | 10 principal components | 16, 21, and all 41 dimensions | Labels reproduce at Adjusted Rand Index 0.970, 0.971, 0.969 and Silhouette falls as dimensions are added | 64.79 percent retained variance is below a conventional 80 percent rule |
| Categorical encoding | ordinal and frequency | one-hot encoding | 15 sparse axes from a 16-sector field would jointly outweigh one standardized continuous feature and force all sector pairs equidistant | Frequency encoding can place two unrelated sectors at one coordinate, so both encoded fields stay out of the mining matrix |
| Density algorithm and space | DBSCAN over all 356,255 applications in the 10-component PCA space | DBSCAN on a 30,000-application UMAP embedding; full-portfolio UMAP | An earlier version called the full run intractable, which was wrong: the expensive step is UMAP, not DBSCAN, and the linear space needs no embedding. Full-portfolio UMAP does remain impractical, so the embedding is kept only as a picture, and the two spaces agree at Jaccard 0.043 | The eps knee is estimated from 30,000 query rows against an index fitted on all rows, and the run takes roughly 25 minutes |
| External score EXT_SOURCE_1 | excluded from mining matrices, flag retained | median imputation with the flag alongside | 54.43 percent imputation parks the majority of the portfolio on one coordinate, duplicating the flag and creating an artificial dense mode | Observed values for 162,345 applications no longer shape the segments; they remain available for rule mining and record review |
| Collective outlier definition | mutual nearest neighbours plus joint separation, in the detection space | DBSCAN noise borrowed from Phase 2; a radius-based intermediate version | DBSCAN noise does not discriminate at this resolution, flagging 1,469 of the 2,057 eligible records where the group test flags 75, and it disagrees with a UMAP repeat of itself at Jaccard 0.043; the radius-based version chained into one component covering 77 percent of the queue | The test runs on the review queue rather than the full portfolio, so a jointly unusual group where no member was queued would be missed |
| Anomaly matrix | unclipped standardized matrix | the p0.5/p99.5-clipped clustering matrix | A global extreme cannot exist on a truncated axis | A separate matrix must be built and kept in sync, which the phase asserts on load |
| Rule interestingness | Support, Confidence, Lift, plus null-invariant measures and exposure standardisation | raw Lift ranking alone | Lift is not null-invariant and ranks exposure artifacts above genuine cross-source patterns in this schema | The correction needs an explicit exposure variable per consequent family, which is a modelling judgement |

### Appendix G: Controls Against Self-Confirming Findings

Every headline number in this report was first produced in a larger, more striking form and then tested against the way it was constructed. These six tests are why the reported figures are smaller than the ones the mining produced. Each is enforced by the validation script, so losing one fails the build.

**1. Cluster tendency and the null-model Silhouette (Phase 2).** A Silhouette Score of 0.148 can mean the data has no structure, that the method is losing structure, or that the data carries several incompatible structures at once, and those three call for opposite responses. Three diagnostics separate them: a Hopkins statistic against a uniform reference scored by the same code, the same Silhouette computed on a column-wise shuffle and on a uniform draw, and a Silhouette per feature family clustered alone. This is a control rather than a diagnostic because of what it forbids: the shuffled null out-scores the real data at K = 2 by isolating 0.91 percent of rows, so no Silhouette in this report may be read against a textbook threshold, and the per-family result forbids describing the five segments as the portfolio's segmentation rather than one of several. Artefacts: [`cluster_tendency.csv`](results/phase2_clustering/cluster_tendency.csv), [`silhouette_by_feature_family.csv`](results/phase2_clustering/silhouette_by_feature_family.csv).

**2. Concentration calibration (Phase 2).** A segment share of recorded loan value is uninterpretable without knowing how much concentration was available. The observed share is placed between a null, where the segment carries exactly its population share, and a ceiling, the share the same number of applications would carry if chosen purely by sorting on loan size. A capture ratio of 0.712 on a Gini of 0.363 means the segment concentration is most of the way to the arithmetic maximum, which is why the concentration is reported as a calibrated fact and Finding 1 is built on alignment instead. Artefact: [`segment_amount_concentration_calibrated.csv`](results/phase2_clustering/segment_amount_concentration_calibrated.csv).

**3. Split-half stability (Phase 2).** Seed stability answers whether the optimiser lands in the same place twice; it cannot answer whether the segments are a property of the portfolio. Two models fitted on disjoint halves label the same unseen applications, and their agreement is reported beside the seed figure. Artefact: [`k_split_half_stability.csv`](results/phase2_clustering/k_split_half_stability.csv).

**4. Exposure standardisation (Phase 3).** The repayment, card, and POS tables are children of the previous-application table, so a longer relationship contributes more rows and more opportunity to display any state that was ever observed. Every rule with an accumulation consequent is re-measured with history depth held constant. Rules with an application-time consequent are returned unchanged, which doubles as the control on the method itself. Artefact: [`rule_exposure_adjustment.csv`](results/phase3_association/rule_exposure_adjustment.csv).

**5. Leave-one-family-out circularity test (Phase 4).** The segmentation and the detectors read the same feature matrix, so a segment defined by delinquency attracts delinquency-driven flags by construction. All five detectors are re-run with the six delinquency columns removed, and each segment's change in queue share measures how much of the concentration was independent. Artefact: [`anomaly_circularity_check.csv`](results/phase4_anomaly/anomaly_circularity_check.csv).

**6. Two-space density check (Phase 2).** DBSCAN in a UMAP projection can report structure belonging to the embedding rather than the data, so the whole portfolio is clustered in the distance-preserving PCA space and the embedded view is re-run on 30,000 of the same applications. Jaccard 0.043 is a negative result and is reported as one: the picture illustrates, the linear space decides. Artefact: [`dbscan_space_comparison.csv`](results/phase2_clustering/dbscan_space_comparison.csv).

Two supporting tests were added for the same reason. The external-score provenance test (Appendix B) checks whether the cross-source screen's independence assumption holds, and the typology basis column records the evidence that earned each outlier label so the contextual class cannot be a residual bucket.

### Appendix H: Dashboard and Presentation Structure

The interactive dashboard (Python Dash) presents the work in business order: Key findings, then Data, Segments, Rules, and Anomalies.

**Key findings** carries the three findings with their evidence, corroboration, implication, and action, plus the charts that make Finding 1 readable without the report: committed value standing behind each review beside applications per review, the three-distribution comparison labelled with amount-to-attention ratios, and the calibrated concentration view showing observed share against its null and ceiling.

**Data** opens with a six-panel distribution view of declared income, recorded loan amount, scheduled payment, loan-to-income, payment-to-income, and the second external score. Each panel marks the median and states the share of applications beyond the visible range, because these fields are right-skewed and an average alone would mislead. Bins are precomputed by the Phase 1 notebook, so the dashboard shows the same distribution the analysis saw without loading the full feature file.

**Segments** compares the five profiles on one standardized scale with sizes, business medians, K-selection evidence, PCA sensitivity, and per-segment evidence coverage. It also carries the two figures that keep the segmentation honest. The **cluster-tendency panel** puts the observed Silhouette beside the value two null models reach on the same data, annotating the bars where a null wins by isolating 0.91 percent of applications, and beside it shows each feature family clustered alone: card history 0.845 and delinquency 0.685 against 0.154 for all 41 together. The **linkage comparison** shows Ward, complete, and average on one sample with each cophenetic correlation and largest group printed on it, so the reader can see that higher distance fidelity coexists with unusable group sizes.

**Rules** shows the 12 patterns against their own context baselines, plus a **rule network** in which each node is an evidence state coloured by source table and each edge is a shortlisted pattern, making visible in one image that all 19 antecedent-to-consequent connections cross between two different sources, and the **exposure control**, showing raw Lift beside Lift after standardising for history depth with the bars that cross below 1.0 clearly visible.

**Anomalies** explains the two queue routes, workload sensitivity across the detector-count and standard-deviation grid, record-level evidence in a filterable table with per-record drill-down, and the two honesty controls: what earns each outlier its typology label, and how much segment concentration survives removal of the segment-defining fields.

Interactivity is section navigation, a sortable and filterable record table with drill-down, and hover detail on every chart. Full algorithm outputs stay in the notebooks and CSV artefacts.

### Appendix I: Reproducibility and Evidence Map

Run from the repository root in this order: `python src/run_pipeline.py`; the four notebooks via `python scripts/execute_notebook.py` in the order exploratory_data_analysis, phase2_clustering, phase3_association, phase4_anomaly; `python scripts/build_linkage_comparison.py` and `python scripts/build_cluster_tendency_plot.py` after Phase 2; then `python scripts/build_business_artifacts.py`; then `python scripts/validate_business_findings.py`; then `python dashboard/app.py`. Order matters because each phase reads the previous phase's outputs. Phase 2 owns the cophenetic and cluster-tendency evidence, and both figure scripts read those numbers back rather than recomputing them, so a figure and its table cannot disagree. Random states and analytical samples are fixed, so with identical inputs, code, and library versions the outputs are reproducible. Segment integers permute between runs, so downstream interpretation joins through the stable names in `cluster_names.csv`.

The validation script fails the build on stale identifiers, names, counts, rule metrics, queue logic, population denominators, any reappearance of outcome-label vocabulary on a business surface, and on the loss of any control in Appendix G.

| Question | Source of truth |
|---|---|
| Population and scope | [`portfolio_context.csv`](results/phase1_preprocessing/portfolio_context.csv) |
| Cleaning and feature decisions | [`data_quality_summary.csv`](results/phase1_preprocessing/data_quality_summary.csv), [`feature_selection_decisions.csv`](results/phase1_preprocessing/feature_selection_decisions.csv) |
| Entropy screen | [`feature_entropy_screen.csv`](results/phase1_preprocessing/feature_entropy_screen.csv) |
| Distribution shapes shown to non-technical readers | [`portfolio_distributions.csv`](results/phase1_preprocessing/portfolio_distributions.csv) |
| K and dimensional sensitivity | [`k_selection.csv`](results/phase2_clustering/k_selection.csv), [`k_stability.csv`](results/phase2_clustering/k_stability.csv), [`k_split_half_stability.csv`](results/phase2_clustering/k_split_half_stability.csv), [`pca_cluster_sensitivity.csv`](results/phase2_clustering/pca_cluster_sensitivity.csv) |
| Per-segment separation | [`cluster_silhouette_detail.csv`](results/phase2_clustering/cluster_silhouette_detail.csv) |
| Does the portfolio cluster at all, and how many ways | [`cluster_tendency.csv`](results/phase2_clustering/cluster_tendency.csv), [`silhouette_by_feature_family.csv`](results/phase2_clustering/silhouette_by_feature_family.csv) |
| Hierarchical validation at both scales | [`method_agreement.csv`](results/phase2_clustering/method_agreement.csv) |
| Linkage cophenetic and group-size evidence | [`linkage_cophenetic.csv`](results/phase2_clustering/linkage_cophenetic.csv) |
| Density view, its two spaces, and what its noise looks like | [`dbscan_space_comparison.csv`](results/phase2_clustering/dbscan_space_comparison.csv), [`dbscan_noise_profile.csv`](results/phase2_clustering/dbscan_noise_profile.csv) |
| Amount concentration against its null and ceiling | [`segment_amount_concentration_calibrated.csv`](results/phase2_clustering/segment_amount_concentration_calibrated.csv) |
| Methods considered and rejected | [`method_alternatives_register.csv`](results/phase2_clustering/method_alternatives_register.csv) |
| Segment names, sizes, actions | [`cluster_names.csv`](results/phase2_clustering/cluster_names.csv), [`cluster_business_summary.csv`](results/phase2_clustering/cluster_business_summary.csv) |
| Final association patterns | [`business_rules_final.csv`](results/phase3_association/business_rules_final.csv) |
| Rule screening, thresholds, interestingness | [`rule_rejection_audit.csv`](results/phase3_association/rule_rejection_audit.csv), [`association_threshold_register.csv`](results/phase3_association/association_threshold_register.csv), [`rule_interestingness_measures.csv`](results/phase3_association/rule_interestingness_measures.csv) |
| External-score provenance | [`external_score_provenance.csv`](results/phase3_association/external_score_provenance.csv) |
| Rule network structure | [`rule_item_catalog.csv`](results/phase3_association/rule_item_catalog.csv), [`rule_network_edges.csv`](results/phase3_association/rule_network_edges.csv) |
| Queue size and sensitivity | [`anomaly_summary.csv`](results/phase4_anomaly/anomaly_summary.csv), [`ensemble_single_axis_sensitivity.csv`](results/phase4_anomaly/ensemble_single_axis_sensitivity.csv) |
| Per-column univariate thresholds actually used | [`univariate_threshold_calibration.csv`](results/phase4_anomaly/univariate_threshold_calibration.csv), [`anomaly_threshold_sensitivity.csv`](results/phase4_anomaly/anomaly_threshold_sensitivity.csv) |
| Outlier typology and collective criterion | [`anomaly_typology_basis.csv`](results/phase4_anomaly/anomaly_typology_basis.csv), [`collective_outlier_criteria.csv`](results/phase4_anomaly/collective_outlier_criteria.csv) |
| How much segment concentration survives the circularity test | [`anomaly_circularity_check.csv`](results/phase4_anomaly/anomaly_circularity_check.csv) |
| Amount, attention, and evidence alignment | [`segment_amount_attention_alignment.csv`](results/phase4_anomaly/segment_amount_attention_alignment.csv) |
| Record-level review actions | [`anomaly_investigation.csv`](results/phase4_anomaly/anomaly_investigation.csv) |

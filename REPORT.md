# Home Credit application portfolio discovery

## Report purpose and decision boundary

This project applies the course KDD process to the Home Credit application portfolio. Its purpose is to discover useful portfolio structure, recurring evidence patterns, and unusual records that deserve human review. It is not an underwriting model and it does not recommend approvals, declines, prices, limits, or collections actions.

The portfolio is analyzed as one unlabeled population of 356,255 applications. One raw source file carries a loan-outcome column from its original competition packaging; the pipeline removes that column at ingestion, and no later phase, finding, chart, or business interpretation reads it. Every pattern in this report comes from the applications themselves: amounts, ratios, histories, and their combinations.

Amounts in the data are anonymized. The report does not assume a currency, and the recorded loan amount is a contract value at application, not an outstanding balance, an exposure measure, or a loss estimate.

The course Dataset Reference Document lists eight assigned datasets, but Home Credit is not among them. This report evaluates the Home Credit data supplied in the repository. Confirmation that the dataset was approved for the course remains an administrative dependency that the analysis cannot prove.

## What the project discovered

The portfolio does not fall along one simple low-to-high risk line. It contains recurring profiles with different evidence and review needs. The three findings below turn those profiles, cross-source relationships, and unusual records into decisions the business can act on. They do not turn the mining output into customer risk grades.

Each finding references the appendices for its complete technical backing instead of reproducing it: Appendix A holds the full segment profiles, Appendix B the full retained rule table, Appendix C representative anomaly records, and Appendix D the consolidated evaluation metrics.

### Finding 1: two history-heavy profiles account for most of the specialist queue

| Decision element | Interpretation |
|---|---|
| Evidence | Repayment-Stress History and Historical Card-Use Intensity contain 62,140 applications, or 17.44% of the portfolio. They account for 4,437 of the 6,404 targeted reviews, or 69.28%. Repayment-Stress History contributes 2,955 reviews and Historical Card-Use Intensity contributes 1,482. |
| Corroboration | The source profiles explain why the work concentrates there. Recorded instalment delays sit 3.30 portfolio standard deviations above average in Repayment-Stress History, and historical revolving-card activity sits 1.96 standard deviations above average in Historical Card-Use Intensity. The queue concentration follows from the evidence inside each profile, not from any outside score. |
| Business implication | Most specialist work is concentrated in two relatively small parts of the portfolio, but the work is not interchangeable. One group needs a repayment chronology and possible hardship review. The other needs confirmation that a historical revolving facility is still open before its balance or limit is treated as current. |
| Recommended action | Plan two review lanes. For Repayment-Stress History, verify dates, severity, recency, cure, disputes, current obligations, and affordability. For Historical Card-Use Intensity, first establish current facility status, then check current balance, limit, arrears, and affordability. Apply hardship procedures only when verified current circumstances call for them. |
| Evidence boundary | Clustering and anomaly detection reuse some repayment and card inputs, so queue concentration is not independent confirmation of the profiles. It shows where review effort will land, not how any application will perform. Full profiles of both segments: Appendix A; queue composition: Appendix C and D. |

### Finding 2: one third of applications carry more than half of the recorded loan amounts

| Decision element | Interpretation |
|---|---|
| Evidence | Larger-Loan Affordability contains 122,395 applications, or 34.36% of the portfolio, yet it carries 52.98% of all recorded loan amounts and 46.63% of all scheduled payment amounts. Its median loan is 5.24 times income, against 3.16 portfolio-wide, and its median scheduled payment takes 22.0% of income, against 16.3% portfolio-wide. |
| Corroboration | A cross-source pattern sharpens the concern. Among 27,332 applications with a loan above six times income and a clean observed instalment record, 17,598 also had at least three quarters of their earlier applications approved. That is 64.39%, compared with 52.42% in the portfolio. Earlier approvals and clean recorded history accompany exactly the loans where affordability matters most, and neither settles it. |
| Business implication | Application volume and amount concentration answer different control questions. Where the recorded amounts concentrate, a weakness in affordability verification touches a disproportionate share of the money the portfolio has committed. Routine-looking history in this segment is not a substitute for income verification, because the pattern shows that clean history and prior approvals are common exactly here. |
| Recommended action | Verify sustainable income and current obligations, then test the recorded payment under a lower-income scenario before any credit action. Track application volume and amount concentration as separate portfolio measures, and keep affordability standards independent of how routine the segment's history looks. |
| Evidence boundary | Recorded loan and payment amounts are anonymized contract values, not outstanding balance, exposure, recovery, or loss. The portfolio reflects the existing selection process and product mix, so the analysis cannot establish a causal policy effect. Full profile of the segment: Appendix A; the supporting cross-source pattern: Appendix B. |

### Finding 3: prior refusals and late repayment often appear together

| Decision element | Interpretation |
|---|---|
| Evidence | Among 36,868 applications with at least three previous refusals, 22,151 also have some recorded instalment lateness. That is 60.08%, compared with 44.47% across the portfolio, a difference of 15.61 percentage points. |
| Corroboration | A separate cross-source pattern appears inside Lower-Intensity Credit Footprint. Among 7,919 applications with bureau debt of at least 80% of bureau credit, 4,508 also have available external scores in the lower band. That is 56.93%, compared with 38.91% in that segment, a difference of 18.02 percentage points. Both patterns show that a second source can sharpen the review question. They come from the same supplied data, so this is internal corroboration rather than external validation. |
| Business implication | Repeated refusals become more useful as a review prompt when repayment evidence points in the same direction. They still do not explain why an earlier application was refused, whether lateness was severe or recent, or whether it was cured or disputed. The bureau and external-score pattern has the same limitation: agreement across sources identifies what to verify, not what decision to make. |
| Recommended action | Review earlier refusal reasons and dates, then inspect repayment severity, recency, cure, and dispute status before assessing current affordability. For the bureau pattern, reconcile balances, limits, and reporting dates and verify the lineage and recency of the available external score. Record the verified facts instead of turning either pattern into an automatic decline reason. |
| Evidence boundary | These are exploratory co-occurrences. The patterns are not causal, source-table exposure is uneven, and neither relationship is a customer-level outcome prediction or lending rule. The full retained rule table with support, confidence, and lift: Appendix B. |

## Business questions

The analysis answers three business questions.

1. Which applicant profiles recur across current application, bureau, prior Home Credit, instalment, POS or cash-loan, and historical card records?
2. Which relationships between those sources are frequent enough and strong enough to support a focused review?
3. Which records are unusual for reasons that suggest source reconciliation, repayment or affordability investigation, or confirmation of a rare valid case?

The intended users are credit-review, data-operations, and portfolio-monitoring teams. The outputs support evidence gathering and workload design. They do not replace permitted source checks, documented affordability assessment, customer-contact policy, or human judgment.

## Data scope and lineage

### One portfolio, eight source files

The application table holds 356,255 applications, assembled from two raw application files that are stacked at load. The out-of-scope outcome column present in one of those files is removed at that moment and never read again. Five behavioural history sources then join the analysis: external bureau records with their monthly statuses, previous Home Credit applications, POS and cash-loan monthly snapshots, instalment payments, and revolving card balances.

The history tables contain many rows per application. Joining them directly would duplicate applicants and distort counts, so the pipeline first summarizes them to one row per applicant. The summaries retain business dimensions that can be interpreted at applicant level:

- bureau depth, active-record share, recorded debt relative to bureau credit, and monthly delinquency history;
- counts and outcomes of previous Home Credit applications;
- POS or cash-loan observation depth and recorded days past due;
- instalment timing, late-payment share, severe-late share, and paid-to-due ratio; and
- historical Home Credit card observation depth, balance, utilization, and delay measures.

The applicant identifier remains an identifier, never a mining feature. It lets every cluster label and anomaly reason trace back to the correct application.

## Phase 1: data understanding and preprocessing

### Cleaning decisions follow the meaning of the field

Missingness is not treated as one generic problem. The pipeline first records why a value was absent, then applies the relevant treatment.

| Data issue | Observed scope | Treatment | Business reason |
|---|---:|---|---|
| Employment-duration sentinel | 64,648 applications, 18.15% | Replace the impossible duration with missing and retain a sentinel flag | The value encodes a pensioner or non-employed status; it is not roughly 1,000 years of employment |
| No housing detail | 171,055 applications, 48.01% | Preserve one no-housing-data indicator and use structural zero in the prepared numeric fields | Missing property detail is not evidence of poor payment behaviour |
| External score 1 unavailable | 193,910 applications, 54.43% | Preserve the source missingness flag, then median-impute the model-facing field | An unavailable score is uncertainty, not a weak observed score |
| No car-age value | 235,241 applications, 66.03% | Use zero with an explicit no-car flag | For most records this is structural absence, not a zero-year-old car |
| Income above the 99th percentile | 3,549 applications, about 1.0% | Bound the clustering value while preserving the source value | A rare amount can dominate Euclidean distance without being a data error |

Aggregated-history fields use zero only when the absence of rows means no recorded activity in that source. The report and dashboard distinguish "not observed" from "observed at zero" wherever that distinction affects interpretation.

### Feature construction and selection

The pipeline creates ratios that answer recognizable credit-review questions:

- the loan amount relative to declared income (leverage);
- the scheduled payment relative to income (payment burden);
- the loan amount relative to the scheduled payment, used only as a dimensionless payment-size proxy;
- bureau debt relative to bureau credit; and
- recorded repayment and historical card-use measures.

The loan-to-payment field is not called a loan term. The source dictionary does not establish payment frequency, interest, fees, or amortization, so converting it into months would add a unit that the data does not support.

Correlation and unsupervised entropy drive the keep/drop audit. Redundant building-measurement variants are removed in favor of one statistical form per measurement. Near-constant and almost duplicate columns are also removed. The final mining matrix has one remaining correlation above 0.85: mean and maximum historical card utilization sit at 0.892. Both stay because one describes sustained use and the other peak use; the overlap remains a sensitivity caveat.

Gender and fields that create a high risk of socioeconomic, family, age, location, education, employment, or social-circle proxying do not form the governed mining segments. They remain available in the readable business view for description and future fairness testing. This reduces direct proxy exposure, but it does not make the analysis fairness-cleared. Tenure, asset availability, housing availability, and missingness can still act as residual proxies.

### Three matrices prevent one treatment from serving conflicting purposes

The pipeline produces three views of the same 356,255 applications.

| Matrix | Fields | Treatment | Downstream use |
|---|---:|---|---|
| `features_business.csv` | 63 business and audit columns | Readable amounts, source values, and missingness evidence | Rules, dashboard interpretation, and record review |
| `features_clustering.csv` | ID plus 42 mining features | Continuous axes bounded at p0.5 and p99.5, then standardized; binary flags remain 0/1 | PCA, K-Means, DBSCAN inputs, and the Ward benchmark |
| `features_anomaly.csv` | ID plus the same 42 mining features | Standardized without clipping | Portfolio anomaly detectors |

Clipping is appropriate for broad distance-based segmentation because a few extreme records should not capture a centroid. It is inappropriate for anomaly detection because it would erase the tail that Phase 4 is meant to inspect. The unmodified business value is retained for every reviewer-facing explanation.

### Phase 1 result

Phase 1 produces one auditable applicant-level population with consistent IDs, separate readable and mathematical views, and a documented decision for every retained or removed mining feature. Later findings can therefore be explained with actual source-scale values without using those raw extremes to distort the cluster geometry.

Evidence: [portfolio context](results/phase1_preprocessing/portfolio_context.csv), [data-quality summary](results/phase1_preprocessing/data_quality_summary.csv), [feature decisions](results/phase1_preprocessing/feature_selection_decisions.csv), and [clustering clip limits](results/phase1_preprocessing/clustering_clip_limits.csv).

## Phase 2: portfolio segmentation

### Why PCA and K-Means are used

K-Means gives every application one broad portfolio profile and scales to 356,255 rows. It is suitable for an operating segmentation, but only after continuous fields are placed on comparable scales and extreme distances are bounded.

PCA compresses correlated directions before clustering. The primary solution uses 10 components, which retain 63.28% of the total variance. That is a practical distance-space choice, not a claim that 63% is a universal sufficiency rule. The check against 16 components, 22 components, and all 42 dimensions gives ARI values of 0.977, 0.970, and 0.966 relative to the 10-component labels. The portfolio structure therefore remains close when more variance is retained.

### Why five segments are retained

K is assessed on one fixed 15,000-application sample, with the same fixed 5,000 applications used for every validity metric. This keeps the K comparison from being confounded by a different evaluation sample each time.

| Option | Silhouette | Davies-Bouldin | Smallest share | Largest share | Mean seed ARI | Interpretation |
|---|---:|---:|---:|---:|---:|---|
| K=2 | 0.262 | 1.741 | 16.63% | 83.37% | Not tested | Best separation, but collapses most of the portfolio into one group |
| K=5 | 0.147 | 1.731 | 2.26% | 34.22% | 0.995 | Elbow solution with highly stable labels and usable business resolution |
| K=6 | 0.138 | 1.732 | 2.18% | 26.37% | 0.745 | More detail, but materially unstable across seeds |
| K=7 | 0.159 | 1.534 | 1.37% | 31.97% | 0.728 | Slightly better geometry on some metrics, but unstable and creates a very small group |

K=5 is retained because it balances the elbow, repeatability, segment size, and business interpretability. It is not selected because it has the highest silhouette; K=2 does. The comparison makes the trade-off explicit instead of treating one metric as an automatic answer.

Three seeds produce K=5 ARI values from 0.9950 to 0.9965, with a mean of 0.9955. That result is strong evidence that the five-profile solution is not an accident of one random initialization.

### What DBSCAN and hierarchical clustering contribute

DBSCAN is run as an exploratory density view on a fixed 30,000-application sample after a two-dimensional UMAP embedding. `min_samples=15` and the knee of the normalized 15-neighbor distance curve determine `eps=0.104`. It finds 493 sampled noise points. UMAP can distort global distance, and 326,255 applications had no opportunity to receive a DBSCAN label. DBSCAN therefore supplies visual and sampled corroboration only. Its noise label cannot be treated as a full-portfolio anomaly rate.

Ward hierarchical clustering is fitted on 5,000 applications because its memory cost prevents an exact full-portfolio fit. Full-data labels are approximated by assigning each application to the nearest sampled-Ward center. Agreement with K-Means is moderate, with ARI 0.584 and normalized mutual information 0.593. The two methods see related structure, but not the same partition. That is useful caution: K-Means is an operating view of the portfolio, not the only possible truth.

The linkage choice is defended with a number rather than dendrogram shape alone. On one 2,000-application sample in the same 10-component space, the cophenetic correlation is 0.447 for Ward, 0.674 for complete, and 0.809 for average linkage. Average linkage preserves pairwise distances most faithfully, but its dendrogram merges most applications into one chained group with a few tiny satellites, which cannot serve as an operating segmentation. Ward is retained for its balanced merge structure, and its lower distance fidelity is reported as the cost of that choice instead of being hidden.

### The five business profiles

Cluster integers are arbitrary, so the dashboard and downstream scripts use the stable business names below. Each profile's share of the portfolio's recorded loan amounts is shown next to its size, because the two answers differ and both matter for control design.

| Segment | Applications | Portfolio share | Share of recorded loan amounts | Distinguishing pattern | Review response |
|---|---:|---:|---:|---|---|
| Lower-Intensity Credit Footprint | 120,294 | 33.8% | 16.1% | Borrowing scale is 0.75 portfolio SD below average; product activity is lower, but most applications still have useful history | Use standard underwriting and request permitted supporting evidence only when a relevant source is genuinely unavailable |
| Repayment-Stress History | 7,622 | 2.1% | 2.1% | Recorded instalment delays are 3.30 portfolio SD above average; the median recorded late-instalment share is 28.6% | Review timing, severity, recency, cure status, disputes, and current affordability; follow hardship policy where verified |
| History-Rich Credit User | 51,426 | 14.4% | 12.9% | Credit-history depth is 0.71 portfolio SD above average | Use the additional evidence to reconcile earlier refusals, arrears, and current obligations rather than assuming more history is good or bad |
| Larger-Loan Affordability | 122,395 | 34.4% | 53.0% | Borrowing scale is 0.75 portfolio SD above average and payment burden is also above average | Verify sustainable income and current obligations; test affordability under a lower-income scenario |
| Historical Card-Use Intensity | 54,518 | 15.3% | 16.0% | Historical revolving-card intensity is 1.96 portfolio SD above average | Confirm whether a revolving facility is still open, then verify current balance, utilization, arrears, and affordability |

Two names deserve special explanation. Lower-Intensity Credit Footprint is not a "thin-file" group: 81.4% have bureau history, 94.5% have instalment history, 94.4% have previous-application history, and 99.9% have at least one external score. Its defining feature is lower activity and smaller amounts relative to the other segments. Historical Card-Use Intensity describes past Home Credit card records. It does not prove that a card facility is open today.

Evidence: [K comparison](results/phase2_clustering/k_selection.csv), [seed stability](results/phase2_clustering/k_stability.csv), [PCA sensitivity](results/phase2_clustering/pca_cluster_sensitivity.csv), [method agreement](results/phase2_clustering/method_agreement.csv), [linkage cophenetic correlations](results/phase2_clustering/linkage_cophenetic.csv), [cluster names and actions](results/phase2_clustering/cluster_names.csv), and [business comparison](results/phase2_clustering/cluster_comparison_long.csv). Appendix A holds the full per-segment profile of every business field, including the sampled DBSCAN noise population.

## Phase 3: association patterns for evidence review

### What the rules mean

Continuous values are converted into readable bands before mining. The bands cover loan scale and affordability, bureau debt, available external-score tiers, previous application outcomes, recorded instalment behaviour, and historical card utilization. A band is an analytical category, not a bank policy threshold.

The selected discovery setting requires at least 3% support in the relevant population, 35% confidence, and 1.20 lift. Support always uses the rule's own context. A 3% portfolio-wide rule represents at least about 10,688 applications; a 3% rule inside the smallest segment represents at least about 229. Confidence is the share of records meeting the condition that also show the associated evidence. Lift compares that confidence with the associated evidence's baseline in the same context.

Apriori, FP-Growth, and ECLAT return the same 1,077 portfolio-wide rules and matching metrics. This is an implementation cross-check, not three independent samples. Segment-level FP-Growth contributes 3,439 more candidates with segment-specific denominators.

### How trivial rules are removed

The first screen starts with 4,516 candidates. It rejects 2,460 algebraic financial identities, 538 nested previous-count definitions, 469 same-bureau derived relationships, 274 same-source missingness identities, and 86 schema-induced missingness identities. That leaves 689 cross-source candidates.

The business screen then removes 364 rules with decorative antecedents, 124 driven by history depth or missingness context, and 50 low-information bands. The remaining 151 business-signal candidates reduce to 80 unique patterns after equivalent forms are combined. A diversity screen selects 12 patterns. The course minimum of 10 is met without padding, per-cluster quotas, or reintroducing trivial identities.

### The 12 selected patterns

The table states each relationship in plain language. "Upper band" and "lower band" refer only to observed and available external-score tiers in this dataset. They do not reveal how those proprietary scores were constructed.

| Rank | Context | Observed association | Confidence versus context baseline | Business interpretation and review response |
|---:|---|---|---:|---|
| 1 | History-Rich Credit User | Available external scores in the upper band are associated with bureau debt below 30% of bureau credit | 64.3% vs 53.1% | Lower-concern evidence agrees. Check score and bureau reporting dates before relying on that consistency |
| 2 | Historical Card-Use Intensity | Observed average historical card utilization of at least 80% is associated with available external scores in the lower band | 47.1% vs 34.5% | Concern signals meet. Confirm current facility status, then review limits, balances, payment behaviour, and score timing |
| 3 | Portfolio-wide | At least three prior refused applications are associated with some recorded instalment lateness | 60.1% vs 44.5% | Prior decisions and repayment history point to the same review need. Check reasons, timing, severity, disputes, and cure status |
| 4 | Lower-Intensity Credit Footprint | Bureau debt of at least 80% of bureau credit is associated with available external scores in the lower band | 56.9% vs 38.9% | Concern signals meet even in the lower-intensity segment. Reconcile bureau balances, limits, score inputs, and reporting dates |
| 5 | History-Rich Credit User | Bureau debt between 30% and 80% of bureau credit is associated with available external scores in the lower band | 46.4% vs 38.6% | More history makes reconciliation possible; it does not settle the current credit decision |
| 6 | Historical Card-Use Intensity | Observed instalments with no recorded lateness are associated with mixed prior-application outcomes | 49.2% vs 39.7% | Evidence conflicts. Compare earlier decision reasons with current obligations and repayment recency |
| 7 | History-Rich Credit User | A loan amount in the lower portfolio third plus available external scores in the lower band is associated with at least three prior refusals | 55.9% vs 44.3% | Several concern signals meet. Recheck current income, payment burden, score inputs, and prior decision reasons |
| 8 | Historical Card-Use Intensity | A loan amount in the upper portfolio third plus at least 75% prior approvals is associated with available external scores in the upper band | 41.0% vs 31.1% | Lower-concern evidence agrees, but the current amount still requires its own affordability assessment |
| 9 | Portfolio-wide | A loan above six times income plus no recorded instalment lateness is associated with at least 75% prior approvals | 64.4% vs 52.4% | Evidence conflicts. Clean history and earlier approvals do not answer whether the current amount is affordable now |
| 10 | Portfolio-wide | A loan amount in the upper portfolio third plus no recorded instalment lateness is associated with available external scores in the upper band | 42.9% vs 33.3% | Lower-concern evidence agrees. Verify income, payment burden, repayment recency, and score timing before acting |
| 11 | Larger-Loan Affordability | Bureau debt between 30% and 80% plus available external scores in the upper band is associated with a scheduled payment below 20% of income | 51.8% vs 41.3% | The sources do not form a single risk direction. Reconcile bureau obligations, score timing, income, and payment burden |
| 12 | Lower-Intensity Credit Footprint | Historical card utilization below 80% plus at least 75% prior approvals is associated with some recorded instalment lateness | 46.6% vs 36.7% | Positive-looking card and approval history can coexist with lateness. Review the repayment timeline rather than averaging the evidence away |

Five patterns are categorized as concern-signal convergence, three as lower-concern agreement, and four as evidence conflict to reconcile. None establishes causality. A rule can be frequent because the same type of applicant has more observable history; exposure to the source tables affects what can be found.

The recommended use is a review checklist. A rule tells the reviewer which sources should be examined together. It does not add votes to the anomaly queue and it does not become an approval or decline rule.

Evidence: [final rule table](results/phase3_association/business_rules_final.csv), [identity rejection audit](results/phase3_association/rule_rejection_audit.csv), [business screen audit](results/phase3_association/rule_business_screen_audit.csv), [shortlist status](results/phase3_association/rule_shortlist_status.csv), and [threshold register](results/phase3_association/association_threshold_register.csv).

## Phase 4: targeted anomaly review

### Five portfolio checks and one sampled corroboration

Each detector answers a different question about unusualness.

| Check | What it notices | Why it remains in the comparison | Main limitation |
|---|---|---|---|
| Skew-adjusted IQR | Extreme values on individual continuous fields after allowing for each field's skew | A source-value check that is less sensitive to a few extreme observations | Cannot see unusual combinations; abstains where the middle half collapses to one value |
| Calibrated Z-score | Values far from a field's mean and standard deviation | A simple symmetry-based comparison at a matched per-field operating point | Sensitive to skew and heavy tails |
| Shrinkage Mahalanobis | Unusual combinations after accounting for covariance | Finds multivariate departures that are not extreme on one field | Represents one global covariance shape |
| Isolation Forest | Nonlinear pockets that are easy to isolate through random partitions | Does not assume a normal distribution | Its contamination parameter sets workload, not a true anomaly prevalence |
| Local Outlier Factor | Applications that are sparse relative to their nearest peers | Adds a local density view | Depends on neighborhood and reference design |
| Phase 2 DBSCAN sample | Sparse points inside the sampled UMAP view | Adds sampled density context | Only 30,000 rows were assessed, so it never votes on queue admission |

The univariate checks run on 33 continuous fields. Each field is calibrated to roughly a 1% tail opportunity, and a row receives an IQR or Z-score detector signal only when at least three fields trigger. Shrinkage Mahalanobis and LOF use the empirical top 2.5% as review-volume points. Isolation Forest uses 5% after 1%, 5%, and 10% sensitivity runs.

The Mahalanobis covariance has full rank across 33 fields, a minimum eigenvalue of 0.0226, a condition number of 174.3, and finite scores for all 356,255 applications. LOF uses two disjoint 20,000-row reference samples; every application is scored by a novelty model that did not fit that row. These checks address two common implementation failures: unstable covariance inversion and scoring LOF training rows as if they were unseen.

Detector counts differ because the methods and operating points differ: adjusted IQR flags 1,295 records, calibrated Z-score 5,906, shrinkage Mahalanobis 8,907, Isolation Forest 17,813, and LOF 8,907. Pairwise Jaccard overlap among the five portfolio checks ranges from about 4.3% to 25.8%. The disagreement is expected. It shows that the methods detect different shapes; it does not show which detector is "right."

### How the review queue is formed

The selected queue has two entry routes.

- Detector consensus admits 3,980 records flagged by at least three of the five portfolio-wide checks.
- The extreme single-axis route adds 2,424 non-consensus records with at least one prepared value 10 standard deviations from the portfolio mean.

Together they produce 6,404 records, or 1.80% of 356,255 applications. The 3-of-5 and 10-standard-deviation settings are project workload choices, not Home Credit policy. The saved sensitivity grid shows how much that choice matters: scenarios range from 3,875 records, or 1.09%, at 4-of-5 plus 12 standard deviations to 11,439 records, or 3.21%, at 2-of-5 plus 8 standard deviations.

The detectors have equal opportunity to assess every portfolio row, but their flags are not equally prevalent, calibrated to one risk scale, or interchangeable in business meaning. "Three votes" is a transparent queue rule, not a probability.

DBSCAN is joined only after admission. Within the queue, 5,837 records were not assessed by the Phase 2 sample, 539 were assessed and not isolated, and 28 were assessed and isolated. The tri-state wording prevents an unsampled record from being misread as a DBSCAN non-anomaly.

Every queued record is also classified in the standard outlier typology, because the three kinds of unusualness ask different review questions.

| Outlier type | Records | Definition used here | Review consequence |
|---|---:|---|---|
| Point | 4,334 | At least one prepared value is 10 or more standard deviations from the portfolio mean; no context is needed to see it | Check the field's source inputs, sign, units, joins, and aggregation first |
| Contextual | 2,056 | Every individual value is plausible; only the combination is unusual under detector agreement | Read the exported record evidence to see which combination of sources conflicts |
| Collective | 14 | No globally extreme value, but the record sits in a sparse micro-group isolated by the sampled Phase 2 density view | Treat the sampled group evidence as tentative; verify the shared pattern before reviewing members individually |

Precedence is deliberate: a 10-standard-deviation single value is the least contestable form of anomaly, so it outranks the sampled density label. Of the 28 density-corroborated queue records, 14 also carry such a value and are therefore counted as point outliers.

### What the queue asks the business to do

| Review type | Records | Share of queue | Required response |
|---|---:|---:|---|
| Affordability or repayment review | 6,247 | 97.55% | Inspect current income and obligations, the repayment timeline, severity, recency, cure or dispute status, and whether a historical facility remains open |
| Data or source reconciliation | 121 | 1.89% | Check sign, unit, currency, duplicate joins, aggregation, reversals, and the contributing source rows before using the field |
| Rare but plausible profile | 36 | 0.56% | Confirm the source value and document why the case is valid; rarity alone is not adverse evidence |

The Repayment-Stress History segment accounts for 2,955 queue records, or 46.1% of the queue, despite representing 2.1% of the portfolio. This concentration is useful for workload planning. It is not an independent validation of the segment because some repayment fields contribute to both segmentation and anomaly scoring. Historical Card-Use Intensity contributes another 1,482 queue records, which supports a focused historical-card review but does not prove that a current card account exists.

The record-level CSV does more than repeat a template. Each row contains the methods that fired, queue route, outlier type, sampled-density status, primary driver, actual business-scale evidence, a record-specific interpretation, a recommended action, an owner, and `Automatic Decision Allowed = No`. An extreme paid-to-due ratio, for example, directs data operations to reconcile contributing instalments, reversals, duplicate rows, and units. If the value is confirmed, it remains evidence for the appropriate affordability or repayment review; it does not become a payment-difficulty diagnosis.

Evidence: [queue summary](results/phase4_anomaly/anomaly_summary.csv), [queue sensitivity](results/phase4_anomaly/ensemble_single_axis_sensitivity.csv), [review mix by segment](results/phase4_anomaly/anomaly_review_by_segment.csv), [route and typology summary](results/phase4_anomaly/anomaly_queue_route_summary.csv), [driver summary](results/phase4_anomaly/anomaly_driver_summary.csv), [record-level investigation table](results/phase4_anomaly/anomaly_investigation.csv), [LOF cross-fit check](results/phase4_anomaly/lof_crossfit_diagnostic.csv), and [Mahalanobis diagnostics](results/phase4_anomaly/mahalanobis_diagnostics.csv). Appendix C shows representative queue records with their methods, scores, outlier type, and interpretation.

## Business recommendations

### Use segments to shape the review, not decide the outcome

Lower-Intensity Credit Footprint should follow the standard process unless a relevant source is genuinely unavailable. Repayment-Stress History should move the reviewer directly to the repayment timeline, current affordability, and any applicable hardship or restructuring process. History-Rich Credit User benefits from reconciliation across more evidence, but history depth is not a risk direction. Larger-Loan Affordability needs verified income, current obligations, and a lower-income affordability scenario. Historical Card-Use Intensity needs confirmation that the facility remains open before any current-limit or utilization response.

### Reconcile agreeing and conflicting history before acting

Repeated refusals plus recorded lateness deserve a focused chronology review, but neither is an automatic decline reason. Reviewers should confirm why and when earlier applications were refused, then check late-payment severity, recency, cure, and dispute status. The same discipline applies when bureau utilization and an available external score agree or conflict: verify balances, limits, source lineage, and reporting dates before relying on the pattern. A past approval or clean observed instalment history must not cancel a current affordability concern.

### Run the anomaly queue as a controlled review workload

The 6,404-record queue is the selected analytical workload, not a permanent threshold. It should be piloted only if the operations team confirms that review capacity exists. Operations should record outcomes by route and driver: confirmed source issue, confirmed rare valid case, verified repayment concern, no issue found, and unavailable evidence. Those outcomes can show whether 3-of-5 plus 10 standard deviations is too broad or too narrow. Changes to the threshold should be made from workload and review-yield evidence, not from a desire to improve a retrospective metric.

### Fix source problems before interpreting them as applicant behaviour

The 121 source-reconciliation cases need data-operations ownership. Extreme payment ratios and delays can result from valid events, but they can also reflect reversals, duplicate joins, unit inconsistencies, or aggregation errors. The source row should be reconciled before it enters affordability or repayment judgment.

### Add governance before any operational use

An operational pilot needs a time-based stability check, segment drift monitoring, rule and queue-yield monitoring, a fairness assessment across permitted groups, and documented rules for when missing evidence can be requested. External-score inputs need lineage and recency controls. Reviewers also need a clear prohibition against using cluster, rule, or anomaly labels as adverse-action reasons.

## Limitations and claims the project cannot make

### Scope of outlier detection

The queue is a workload, not a truth set. There is no verified anomaly ground truth, so the 3-of-5 consensus rule and the 10-standard-deviation single-axis rule set review volume rather than measure a true anomaly rate, and detector agreement is not a calibrated probability. The detectors see only the 42 prepared applicant-level fields: an application that is unusual in a way those fields do not encode, such as collusion across applicants, document forgery, or behaviour visible only in raw monthly rows, is invisible to every method used here. DBSCAN assessed a 30,000-application sample, so its noise label exists for 8.4% of the portfolio and the collective-outlier count is a sampled lower bound, not a portfolio total. Extremity is also not wrongdoing in either direction: a flagged record can be a legitimate rare profile, and a fraudulent record crafted to look ordinary would pass every check.

### Correlation versus causation

Nothing in this project establishes a causal claim. The association rules are exploratory co-occurrences selected after testing thousands of candidates; a surviving rule shows that two evidence patterns appear together more often than chance in the supplied files, not that one causes the other. Plausible non-causal explanations remain open for every retained pattern: applicants with more recorded history simply have more opportunity to show any pattern, and product mix, approval policy, and data-capture practices shape which combinations can be observed at all. The same discipline applies to segment differences: a segment's profile describes its members collectively, and treating a group average as a statement about an individual applicant would be an ecological fallacy.

### Dataset representativeness

The portfolio is the supplied 356,255 applications: people who applied to Home Credit, passed whatever intake occurred, and reached the recorded files. It says nothing about applicants who never applied, applied elsewhere, or were filtered before recording, so no market-level or future-time claim is available. The segments describe this supplied portfolio, and their sizes, boundaries, and shares can all shift under a different intake policy, product mix, or time window. Amounts are anonymized, without currency or payment-frequency metadata, so no absolute monetary claim survives outside this dataset. The course reference document also does not list Home Credit, so dataset approval must be confirmed outside the analysis.

### What additional data would improve these findings

- **Current account status for historical facilities.** Open or closed flags and closure dates for card and bureau records would resolve the main uncertainty in Historical Card-Use Intensity: whether an intense historical facility is still active.
- **Reporting timestamps and lineage for bureau records and external scores.** Recency, dispute status, and cure information would let reviewers weight agreeing or conflicting sources instead of only reconciling them manually.
- **Refusal reason codes for previous applications.** The refusals-with-lateness pattern (Finding 3) can only become operational when the reason for each earlier refusal is known.
- **Verified income and current obligations.** Affordability observations here rest on declared income; verified figures would turn the amount concentration (Finding 2) from a review prompt into a measurable control.
- **Outcomes of the review queue itself.** Recording confirmed source errors, verified rare cases, and no-issue results per route would let the 3-of-5 and 10-standard-deviation thresholds be tuned on review yield instead of retrospective judgment.
- **Currency, unit, and schema metadata.** Explicit units would convert several data-consistency checks from statistical inference into deterministic validation.
- **Time-stamped repeat observations.** A second observation window would support stability, drift, and generalization checks that a single cross-section cannot.
- **Loan repayment outcomes under governance.** If the business later chooses to evaluate review effectiveness, properly governed post-decision performance data would allow it; the current analysis contains no outcome information by design.

### Other boundaries

- Historical sources do not always reveal current account status, reporting recency, dispute status, or whether arrears were cured.
- Source-table exposure is uneven. An applicant with more prior Home Credit activity has more opportunities to show a historical pattern.
- Structural zeros and missingness flags preserve useful context but can still shape distance and act as socioeconomic or life-stage proxies.
- K=5 is a stable operating resolution, but Ward only partially agrees and DBSCAN is a sampled UMAP view.
- Dashboard responsiveness and the rubric's sub-100-millisecond interaction expectation require measured browser performance. A visual inspection alone cannot prove that threshold.
- Presentation timing, team contribution, and the team's ability to answer questions must be demonstrated during rehearsal and delivery; repository artifacts cannot certify them.

## Dashboard and presentation structure

The dashboard should be presented in the same order as the business story.

1. Key findings contains exactly the three findings above. Each one states the evidence, corroboration, business implication, action, and evidence boundary.
2. Data explains the single application portfolio, its eight source files, evidence availability, and preprocessing decisions.
3. Segments compares all five named profiles in one view, including each segment's share of recorded loan amounts, and provides the review response for each.
4. Rules shows the 12 selected cross-source patterns, their own context baselines, and the question each pattern adds to a review.
5. Anomalies explains queue admission, the point, contextual, and collective typology, workload sensitivity, review ownership, and record-specific evidence.

Technical plots belong in the relevant method section, not as the main finding. A chart earns space when it helps the audience compare a workload, a profile, or a decision implication. Full algorithm outputs remain in the notebooks and CSV artifacts for audit.

For a 10-minute presentation, use about one minute for scope and boundaries and roughly two minutes for each finding. Use the remaining time for implementation priorities and limitations. The team should be ready to explain why K=5 was selected, why association-rule denominators differ, why DBSCAN does not vote, and why the portfolio is analyzed as one unlabeled population.

The course expo asks four comparison questions, and the project's answers are prepared in advance.

1. **Most surprising rule.** The portfolio-wide link between repeated refusals and recorded instalment lateness, surprising less for its direction than for what the search around it revealed: every candidate with lift above 2 turned out to restate an arithmetic identity or a table join, so the honest lift ceiling of 1.46 is itself the discovery.
2. **Most interpretable clustering method.** K-Means at K=5 with named business profiles. Ward corroborates related structure but chains at the sample level (the cophenetic comparison shows why higher distance fidelity does not mean a usable segmentation), and DBSCAN contributes a sampled density check rather than an operating view.
3. **What the anomalies suggest in a real banking context.** Three different operational responses, not one risk list: source-capture reconciliation for the 121 data-consistency records, affordability and repayment verification for the 6,247-record majority, and documented validation for the 36 rare-but-plausible profiles.
4. **Comparison with other domains.** The five-phase methodology is domain-agnostic, but every finding here took its meaning from the credit-review context. The same mathematics on a fraud or churn dataset would surface structurally similar but semantically different knowledge, which is the expo's own point.

## Rubric traceability

The supplied presentation rubric assesses insight, visualization, and method rigor. The course project document also asks for documented preprocessing, three clustering methods, at least 10 non-trivial association rules, anomaly cross-referencing, business interpretation, an interactive dashboard, and a plain-language report.

| Rubric area | Evidence in this project | Remaining proof or caveat |
|---|---|---|
| Insight depth | Three findings connect workload concentration, amount concentration, cross-source history, and specific review actions | Business value still needs confirmation in a controlled review pilot |
| Corroboration | K stability, PCA sensitivity, Ward agreement with cophenetic linkage evidence, sampled DBSCAN, exact portfolio-rule enumeration across three algorithms, detector overlap, and source-scale profiles; Appendix D consolidates the metrics | Most corroboration is internal to the supplied data; algorithm agreement is not external validation |
| Domain relevance | Every segment, rule, and anomaly type points to a specific credit-review or data-operations action | No action is an approval, decline, price, limit, or collections rule |
| Visualization accuracy | Dashboard numbers read from validated CSV artifacts with explicit denominators | Browser performance must be measured, not inferred |
| Interpretability | Full segment names, common denominators, plain-language hover text, and no profile dropdown are used for comparison | A non-technical rehearsal is still needed |
| Design quality | The dashboard follows the business sequence and uses responsive layouts | Final scoring remains a reviewer judgment |
| Pipeline correctness | Applicant-grain aggregation, ID alignment, separate business, clustering, and anomaly matrices, LOF cross-fit, covariance diagnostics, and the point, contextual, and collective outlier typology are explicit | Future-data generalization is not tested |
| Rationale | Alternatives and rejected choices are recorded for missingness, feature selection, K, PCA dimensions, linkage, rule screening, detectors, and queue thresholds | Some operating thresholds remain project workload choices |
| Honesty of limitations | The report states administrative, representativeness, causal, fairness, threshold, and deployment boundaries | Dataset approval and presentation readiness require external confirmation |

The repository supports the rubric with traceable evidence, correct denominators, and defensible reasoning. It cannot determine the final score. Administrative approval, measured interaction latency, team rehearsal, and evaluator judgment remain outside the code.

## Reproducibility and evidence map

Run the project from the repository root in this order:

```powershell
python src/run_pipeline.py
python scripts/execute_notebook.py notebooks/exploratory_data_analysis.ipynb --timeout 900
python scripts/execute_notebook.py notebooks/phase2_clustering.ipynb --timeout 1200
python scripts/build_linkage_comparison.py
python scripts/execute_notebook.py notebooks/phase3_association.ipynb --timeout 1800
python scripts/execute_notebook.py notebooks/phase4_anomaly.ipynb --timeout 3600
python scripts/build_business_artifacts.py
python scripts/validate_business_findings.py
python dashboard/app.py
```

The order matters. Each phase reads outputs from the earlier phase, and the validation script is designed to fail on stale IDs, names, counts, rule metrics, queue logic, or population denominators. The validator also rejects any reappearance of outcome-label vocabulary on a business surface.

| Question | Source of truth |
|---|---|
| Population and scope | [`portfolio_context.csv`](results/phase1_preprocessing/portfolio_context.csv) |
| Cleaning and feature decisions | [`data_quality_summary.csv`](results/phase1_preprocessing/data_quality_summary.csv), [`feature_selection_decisions.csv`](results/phase1_preprocessing/feature_selection_decisions.csv) |
| K and dimensional sensitivity | [`k_selection.csv`](results/phase2_clustering/k_selection.csv), [`k_stability.csv`](results/phase2_clustering/k_stability.csv), [`pca_cluster_sensitivity.csv`](results/phase2_clustering/pca_cluster_sensitivity.csv) |
| Segment names, sizes, and actions | [`cluster_names.csv`](results/phase2_clustering/cluster_names.csv), [`cluster_business_summary.csv`](results/phase2_clustering/cluster_business_summary.csv) |
| Segment amount concentration | [`segment_credit_concentration.csv`](results/phase4_anomaly/segment_credit_concentration.csv) |
| Final association patterns | [`business_rules_final.csv`](results/phase3_association/business_rules_final.csv), [`rule_shortlist_status.csv`](results/phase3_association/rule_shortlist_status.csv) |
| Rule screening and thresholds | [`rule_rejection_audit.csv`](results/phase3_association/rule_rejection_audit.csv), [`rule_business_screen_audit.csv`](results/phase3_association/rule_business_screen_audit.csv), [`association_threshold_register.csv`](results/phase3_association/association_threshold_register.csv) |
| Queue size and sensitivity | [`anomaly_summary.csv`](results/phase4_anomaly/anomaly_summary.csv), [`ensemble_single_axis_sensitivity.csv`](results/phase4_anomaly/ensemble_single_axis_sensitivity.csv) |
| Record-specific review actions | [`anomaly_investigation.csv`](results/phase4_anomaly/anomaly_investigation.csv) |

Random states and analytical samples are fixed where randomness is used. With identical input files, code, and library versions, the outputs are reproducible. Cluster integers can still change after a data, feature, or software change, so downstream interpretation must always use `cluster_names.csv` rather than assuming that a numeric cluster ID carries stable meaning.

## Appendix A: full cluster profiles

The complete profile, covering the mean and standard deviation of every business field, the modal value of every flag and categorical field, and whether each field entered the mining matrix, is written per population to [`segment_full_profiles.csv`](results/phase2_clustering/segment_full_profiles.csv) (6 populations x 61 fields). The sampled DBSCAN noise population is profiled as its own group, against its own 30,000-application sample base, because the density view never assessed the rest of the portfolio. The table below condenses that artifact to the fields that differentiate the populations; values are mean with standard deviation on the readable business scale, in anonymized currency units.

| Population | Applications (share) | Declared income | Loan amount | Loan / income | Payment / income | Instalment late share | Card utilization | Prior refusals |
|---|---|---|---|---|---|---|---|---|
| Lower-Intensity Credit Footprint | 120,294 (33.8%) | 141,167 (68,820) | 279,348 (123,638) | 2.23 (1.08) | 0.14 (0.07) | 0.06 (0.11) | 0.01 (0.05) | 0.31 (0.70) |
| Repayment-Stress History | 7,622 (2.1%) | 155,317 (77,144) | 567,928 (368,643) | 4.05 (2.72) | 0.19 (0.10) | 0.30 (0.19) | 0.06 (0.16) | 0.85 (1.62) |
| History-Rich Credit User | 51,426 (14.4%) | 188,750 (86,922) | 524,917 (310,350) | 3.03 (1.75) | 0.16 (0.07) | 0.09 (0.11) | 0.02 (0.08) | 2.94 (3.11) |
| Larger-Loan Affordability | 122,395 (34.4%) | 179,747 (89,686) | 906,337 (376,103) | 5.81 (2.81) | 0.24 (0.10) | 0.06 (0.11) | 0.01 (0.04) | 0.26 (0.65) |
| Historical Card-Use Intensity | 54,518 (15.3%) | 179,964 (84,386) | 615,154 (367,361) | 3.81 (2.44) | 0.17 (0.09) | 0.07 (0.08) | 0.55 (0.26) | 1.19 (1.99) |
| DBSCAN sampled noise | 493 (1.6% of the 30,000 sample) | 152,556 (79,866) | 629,035 (385,382) | 4.94 (3.87) | 0.22 (0.12) | 0.09 (0.12) | 0.16 (0.28) | 1.24 (2.13) |

The noise profile explains why DBSCAN corroboration is worth keeping despite its sampled coverage: noise records combine above-average borrowing scale, payment burden, card activity, and refusals without matching any single segment's signature. They are mixed, not extreme on one axis. The recommended action per segment appears in the five-business-profiles table in the Phase 2 section.

## Appendix B: full association rule table

All 12 retained rules, ranked by lift descending. Support, confidence, and lift use the rule's own context as denominator (portfolio-wide or the named segment), as registered per rule in [`business_rules_final.csv`](results/phase3_association/business_rules_final.csv). Band definitions are analytical categories from Phase 3, not policy thresholds.

| # | Context | Antecedent | Consequent | Support | Confidence | Lift |
|---:|---|---|---|---:|---:|---:|
| 1 | Lower-Intensity Credit Footprint | Bureau debt at least 80% of bureau credit | External scores in the lower band | 3.76% | 56.9% | 1.463 |
| 2 | Historical Card-Use Intensity | Observed average card utilization of at least 80% | External scores in the lower band | 10.30% | 47.1% | 1.363 |
| 3 | Portfolio-wide | At least three prior refused applications | Some recorded instalment lateness | 6.22% | 60.1% | 1.351 |
| 4 | Historical Card-Use Intensity | Loan amount in upper portfolio third plus at least 75% prior approvals | External scores in the upper band | 6.83% | 41.0% | 1.319 |
| 5 | Portfolio-wide | Loan amount in upper portfolio third plus no recorded lateness | External scores in the upper band | 6.14% | 42.9% | 1.289 |
| 6 | Lower-Intensity Credit Footprint | Card utilization below 80% plus at least 75% prior approvals | Some recorded instalment lateness | 3.46% | 46.6% | 1.270 |
| 7 | History-Rich Credit User | Loan amount in lower portfolio third plus external scores in the lower band | At least three prior refusals | 7.17% | 55.9% | 1.263 |
| 8 | Larger-Loan Affordability | Bureau debt 30% to 80% plus external scores in the upper band | Scheduled payment below 20% of income | 4.52% | 51.8% | 1.253 |
| 9 | Historical Card-Use Intensity | Observed instalments with no recorded lateness | Mixed prior-application outcomes | 10.13% | 49.2% | 1.239 |
| 10 | Portfolio-wide | Loan above six times income plus no recorded lateness | At least 75% prior approvals | 4.94% | 64.4% | 1.228 |
| 11 | History-Rich Credit User | External scores in the upper band | Bureau debt below 30% of bureau credit | 17.19% | 64.3% | 1.210 |
| 12 | History-Rich Credit User | Bureau debt 30% to 80% of bureau credit | External scores in the lower band | 16.75% | 46.4% | 1.202 |

The lift ceiling of 1.46 is itself informative: after algebraic, nested, same-source, and schema-induced identities are rejected, no honest cross-source relationship in this portfolio is dramatic. Rules with lift above 2 existed among the rejected candidates, but each restated an arithmetic identity or a join artifact rather than a discovery.

## Appendix C: anomaly detection results

Representative queue records, chosen to cover every outlier type and review type. The full record-level table, holding all 6,404 queue records with methods, route, scores, driver, business-scale evidence, record-specific interpretation, recommended action, and owner, is [`anomaly_investigation.csv`](results/phase4_anomaly/anomaly_investigation.csv). Score reading: max |z| is the largest standardized distance on any single prepared field; D-squared is the shrinkage Mahalanobis squared distance; LOF above roughly 1.5 means materially sparser than its nearest peers; more negative Isolation Forest scores mean easier to isolate.

| Record ID | Methods flagged by | Key scores | Outlier type | Business interpretation |
|---:|---|---|---|---|
| 161584 | Adjusted IQR, Calibrated Z-score, Shrinkage Mahalanobis, LOF | max \|z\| 45.8, D2 2301, LOF 12.1 | Point | The recorded average paid-to-due ratio of 1,272.58 times is physically implausible; reconcile contributing instalment rows, reversals, duplicates, and units before any use. Data consistency check. |
| 100784 | All five portfolio checks | max \|z\| 12.6, D2 630, LOF 2.7 | Point | The scheduled payment equals 137.4% of declared income; verify income and obligations, because a payment above income cannot be sustained as recorded. Affordability review. |
| 265042 | Adjusted IQR, Calibrated Z-score, Shrinkage Mahalanobis, LOF | max \|z\| 10.8, D2 240 | Point | 295 monthly POS or cash-loan records is an extreme but possible depth of history; confirm the source and, if correct, continue standard underwriting. Rare but plausible profile. |
| 190549 | All five portfolio checks | max \|z\| 7.7, D2 164 | Contextual | No single field is impossible, but the combined payment-burden pattern is unusual under every multivariate view; targeted affordability review. |
| 177061 | All five portfolio checks | max \|z\| 7.1, D2 114 | Contextual | Payment-ratio evidence conflicts with the rest of the record; reconcile the instalment source before interpreting behaviour. Data consistency check. |
| 197583 | All five portfolio checks | max \|z\| 8.8, D2 147 | Contextual | Unusual previous-application count in combination with its history depth; verify and document. Rare but plausible profile. |
| 303289 | All five portfolio checks; DBSCAN sample: isolated | max \|z\| 6.7, D2 129, LOF 1.7 | Collective | Sits in a sparse micro-group in the sampled density view while carrying a high payment burden; verify the shared pattern, then review affordability. |

## Appendix D: evaluation metrics summary

One reference table of the quantitative evaluation metrics produced across the phases. Each value is written by the phase that produced it and re-checked by `validate_business_findings.py`.

| Phase | Metric | Value |
|---|---|---|
| Phase 1 | Portfolio size | 356,255 applications |
| Phase 1 | Mining features after governance screen | 42 (from 61 business fields) |
| Phase 1 | Residual feature pairs with \|r\| > 0.85 | 1 (card utilization mean vs max, 0.892) |
| Phase 2 | PCA components retained / cumulative variance | 10 / 63.28% |
| Phase 2 | Silhouette score (K=5, fixed 5,000-application sample) | 0.147 |
| Phase 2 | Silhouette score (K=2 comparison point) | 0.262 |
| Phase 2 | Davies-Bouldin index (K=5) | 1.731 |
| Phase 2 | Mean seed-to-seed ARI (K=5, three seeds) | 0.995 |
| Phase 2 | ARI, 10-component vs full 42-dimension labels | 0.966 |
| Phase 2 | Cophenetic correlation, chosen Ward linkage | 0.447 (complete 0.674, average 0.809 on the same sample) |
| Phase 2 | ARI, K-Means vs sampled-Ward hierarchical | 0.584 |
| Phase 2 | Normalized mutual information, K-Means vs sampled-Ward | 0.593 |
| Phase 2 | DBSCAN sampled noise | 493 of 30,000 (1.64%) |
| Phase 3 | Candidate rules generated | 4,516 |
| Phase 3 | Identical portfolio-wide rules across Apriori, FP-Growth, ECLAT | 1,077 |
| Phase 3 | Rules retained after identity and business screening | 12 |
| Phase 3 | Support range of retained rules (own context) | 3.46% to 17.19% |
| Phase 3 | Confidence range of retained rules | 41.0% to 64.4% |
| Phase 3 | Highest lift among retained rules | 1.463 |
| Phase 4 | Anomaly candidates flagged by at least one detector | 27,385 (7.69%) |
| Phase 4 | Candidates corroborated by two or more detectors | 9,685 (2.72%) |
| Phase 4 | Detector-consensus route (3 of 5) | 3,980 |
| Phase 4 | Extreme single-axis additions (at least 10 SD) | 2,424 |
| Phase 4 | Targeted review queue | 6,404 (1.80%) |
| Phase 4 | Outlier typology: point / contextual / collective | 4,334 / 2,056 / 14 |
| Phase 4 | Queue records corroborated by the sampled density view | 28 |

No outcome-scored metric appears in this table. The portfolio is analyzed as one unlabeled population, so the evaluation rests on internal validity, stability, sensitivity, and corroboration evidence rather than on any label comparison.

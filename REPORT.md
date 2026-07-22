# Home Credit Default Risk: Knowledge Discovery Report

A single end-to-end record of the project: the domain reasoning, every method decision and why it was chosen, the validation evidence, and the business interpretation of the results.

**Status:** `VERIFIED`. 71 independent checks, 70 passed, 1 warning, 0 failed.

---

## 1. What this project is, and what it is not

The brief asks for knowledge discovery on the Home Credit portfolio: prepare the data, find structure, mine patterns, review anomalies, and present the findings so a business audience can act on them. It does not ask for a competition-grade default classifier.

That distinction drives every choice below. When a method decision came down to "which option separates TARGET better" versus "which option produces a defensible, interpretable portfolio view", this project chose the second, and then measured the cost of that choice honestly in Section 8.

The one thing this report refuses to do is present an unsupervised result as if it were a credit decision. A segment is a cohort description. An anomaly flag is a request for human review. Neither is a probability of default, and neither authorises approving, declining, repricing, or reducing a limit for any individual applicant.

---

## 1b. Methodology audit and corrections

A full reasoning-led review of the workflow found four defects serious enough to change results, not just wording. All four had passed every automated check, because the existing quality filters tested the *surface form* of an output rather than whether it carried independent information. They are recorded here rather than quietly patched, since the reasoning is the substance of the correction.

The fourth was found only by checking whether the third fix had actually worked. That is worth noting as a method in itself: verifying a correction end to end, rather than confirming the code changed, is what exposed it.

### F1: Protected and proxy attributes were shaping the segmentation

The clustering matrix contained `YEARS_BIRTH` (age), `CNT_CHILDREN` (familial status), `REGION_RATING_CLIENT_W_CITY` (a geographic rating, the classic redlining proxy), `NAME_EDUCATION_TYPE`, `NAME_INCOME_TYPE_FREQ` and `ORGANIZATION_TYPE_FREQ` (socioeconomic proxies), and `DEF_30_CNT_SOCIAL_CIRCLE_BIN`, the number of the applicant's acquaintances who fell into arrears.

The governance was inconsistent in the worst possible direction. Phase 3 already rejected protected and life-stage vocabulary from association rules. The supervised diagnostic already excluded age, education, income type, organisation type, and region rating. Both of those are secondary outputs; the diagnostic is explicitly labelled as not for deployment. Meanwhile the segmentation, the actual deliverable, the thing that drives review actions and portfolio strategy, was built from exactly the attributes the other two phases refused to touch.

The social-circle feature is the hardest to defend. Judging an applicant by whether their acquaintances paid their loans is guilt by association: it is not the applicant's conduct, they cannot contest it, and it correlates strongly with neighbourhood, which is to say with the protected characteristics that geography encodes.

**Correction:** all seven attributes were removed from the clustering feature set, 49 features down to 42. They remain in `features_business.csv` and are still used to *describe* segments after the fact and to support fairness monitoring. They simply no longer get to *form* the segments. Frequency encoding had an independent problem worth recording: it maps a category to how common it is, so two unrelated employer sectors with similar frequency collapse onto the same coordinate, manufacturing similarity between applicants with nothing in common.

### F2: Anomaly detection was running on pre-clipped data

Phase 1 clips 34 continuous axes at the 0.5th and 99.5th percentiles so that a handful of extreme files cannot capture K-Means centroids. That is the correct treatment for centre-based clustering. Phase 4 was then pointed at the same matrix.

The consequences compound, and all three run against the purpose of outlier detection:

1. A "global extreme value" cannot be found on an axis whose extremes were truncated by construction. The largest possible deviation *is* the clip boundary, so the category was measuring "sits at the boundary", not "is genuinely extreme".
2. Clipping collapses roughly 1,800 records per axis onto one identical value. Those records, the most extreme in the portfolio, thereby acquire a large crowd of exact neighbours, which *lowers* their local outlier factor and their density-based scores. The treatment was actively hiding the records it was supposed to surface.
3. The boundary pile-up is a non-Gaussian point mass that distorts the covariance matrix Mahalanobis distance depends on.

The scale of the distortion is best seen directly. On `BUREAU_DEBT_TO_CREDIT_RATIO`, the most extreme record measures **2.68 standard deviations in the clipped matrix and 426.59 in the unclipped one**. An applicant whose external debt is wildly out of proportion to their credit lines, precisely the file underwriting most needs to see, was being presented to every detector as unremarkable. On `CREDIT_TO_INCOME`, 1,782 records sat on one identical boundary value; unclipped, one record holds the maximum.

Notably, the source comment in `build_matrices.py` had always stated the correct intent: *"Those rows remain fully available to Phase 4; only their contribution to broad segmentation distance is bounded here."* The design was right and the wiring contradicted it.

**Correction:** the pipeline now writes a second matrix, `features_anomaly.csv`, carrying the same features standardised **without** clipping. Phase 4 detects on that, and asserts on load that the widest absolute standardised value exceeds 4 SD, so a future regression to the clipped matrix fails loudly instead of silently degrading. The supervised diagnostic keeps the clipped matrix, where bounded inputs genuinely suit a linear model.

### F4: Restoring the tails exposed a second defect in the queue architecture

Checking whether the corrected matrix actually surfaced the extreme records showed that it largely did not, and the reason was structural rather than a bug.

Take the most extreme record in the portfolio: applicant 244750, at **-426.6 standard deviations** on `BUREAU_DEBT_TO_CREDIT_RATIO`. After the F2 fix its true value reaches the detectors, and it still scored `detection_count = 1` and never entered the review queue. Only LOF flagged it.

Every other detector is built in a way that cannot see a single-axis catastrophe:

- adjusted IQR and empirical Z-score both apply `MULTI_COL_RULE = 3`, requiring extremity in **three or more columns** before flagging a record at all;
- Isolation Forest looks for records that are globally easy to isolate, not ones with a single wild coordinate;
- Mahalanobis ranks on overall distance under a robust covariance, which deliberately downweights exactly this kind of point.

So the consensus rule, three or more detectors agreeing, is structurally incapable of surfacing the very records most likely to be data-entry errors. Across the portfolio, **3,423 records lie beyond 10 SD on at least one axis and never reached the queue: 79% of all such records.** At 20 SD, 70% were still missed. Among the fifty most extreme records on the bureau-debt axis, only two reached consensus.

This qualifies the F2 correction rather than undoing it. F2 was necessary, because without it these values did not exist to be found. It was not sufficient, because the aggregation layer above it discards single-axis evidence.

**Correction:** the queue now has two independent routes, kept separately labelled rather than blended:

| Route | Basis | What it is good at |
|---|---|---|
| **Detector consensus** | 3+ detectors agree, >=50% of those available | Records unusual *in combination* |
| **Implausible single value** | Any axis at or beyond 10 SD | Records catastrophic *in one field* |

The threshold is not tuned. Under any roughly normal distribution a 10-SD value should not appear once in 356,255 records, so its presence indicates either a capture error or a genuinely exceptional file, and both need a human. This mirrors ordinary credit practice, where plausibility and hard-bound checks run as a separate control from statistical review, precisely because they answer a different question. No lender requires three algorithms to agree that a single number is impossible.

### F3: Association rules that restated their own construction

Two distinct artefact families were passing the rejection filter.

**Circular rules.** Four of the fifteen final rules contained cluster membership as an item. The clearest was `{card_utilisation_high} -> {cluster_0_card_intensive}` at lift 6.44, where cluster 0 is *defined* by `CC_UTILIZATION_MAX` sitting 217% above the portfolio mean. The rule rediscovers the Phase 2 clustering; its lift is an artefact of how the segment was built, not a portfolio pattern. These four rows had empty `antecedents` columns, which is why earlier inspection had missed them.

**Schema-induced missingness.** Six further rules, carrying the table's highest lifts at 11.3 to 17.46, were consequences of the relational model. `installments_payments`, `credit_card_balance`, and `POS_CASH_balance` are all child tables of `previous_application`, keyed on `SK_ID_PREV`. An applicant with no previous application therefore *cannot* have instalment, card, or POS rows attached to one. Their absences co-occur by construction, not because independent reporting systems happen to agree. The old filter caught same-table missingness identities but had no notion of the schema, so these passed as discoveries. Two of the patterns were additionally duplicated across two segments.

Between them, ten of fifteen rules were artefacts of construction rather than findings about borrowers.

**Correction:** cluster membership was removed from the mining vocabulary entirely, segment-specific patterns now come from mining *within* each segment, which is the honest way to obtain them. The rejection filter gained two new categories: `restates_cluster_definition`, and `schema_induced_missingness_identity`, which fires when a rule's consequent is a previous-application-descendant absence and one of its antecedents is another. A rule such as `{income_q1} -> {no repayment history}` still survives, because that one genuinely describes *who* lacks history rather than restating the join. The selector now also reports a shortfall honestly rather than padding a segment to three rules with artefacts.

### What the audit confirmed as sound

The cross-fitted backtest design, the two-view model/evidence separation, the anomaly scope classification, the orphan `bureau_balance` handling, and the base-rate discipline throughout all survived scrutiny unchanged.

---

## 2. Domain foundation

Everything in the pipeline rests on how consumer credit risk actually works. This section states that basis explicitly, because the preprocessing and interpretation decisions are only defensible in its terms.

### 2.1 What the data represents

The unit of analysis is a loan application, keyed by `SK_ID_CURR`. The public `TARGET` flag marks a payment-difficulty outcome on labelled training applications. It is not a legal definition of default, not a fraud marker, and not a judgment about lifetime creditworthiness. Home Credit has never published its full operational threshold or the downstream decision policy attached to it, so the honest reading of `TARGET` is "this account hit a payment problem the lender chose to record", nothing more.

Around that application sit six relational histories: credit bureau records and their monthly balances, the applicant's previous applications with Home Credit, and the POS, instalment, and credit-card behaviour attached to those previous loans.

### 2.2 Capacity and affordability

Lenders separate *can they pay* from *will they pay*. Capacity comes from the money fields, but raw amounts are almost useless for comparison, an annuity of 30,000 means something completely different at an income of 60,000 than at 600,000. So the project works in ratios:

| Ratio | What it proxies |
|---|---|
| Credit  /  income | Leverage, how large the ask is relative to means |
| Annuity  /  income | Repayment burden, the recurring squeeze on monthly cash flow |
| Credit  /  annuity | Estimated term, how long the commitment runs |
| Goods price  /  credit | Exposure structure, how much is financed beyond the asset |

These are screening evidence, never policy cut-offs. A high leverage ratio can be entirely reasonable once verified income, existing obligations, household costs, collateral, and product terms are on the table. That is exactly why the outputs route to a reviewer instead of to a decision.

### 2.3 Willingness and observed repayment behaviour

The instalment, POS, card, and bureau histories carry the behavioural signal: lateness, delinquency depth, utilisation, payment-to-due ratios, and how much credit history exists at all.

Underwriting practice weights four properties of any arrears record, **recency, severity, persistence, and cure status**. A 60-day delinquency that was cured three years ago is a very different file from a 30-day delinquency still open today. The public data is aggregated to applicant level, which flattens exactly that ordering. This is a real limitation, and it is why every anomaly recommendation asks the reviewer to go back to source records for the timeline rather than acting on the aggregate.

### 2.4 Thin files and missing history

This is the single most consequential domain principle in the project.

Absence of history is not evidence of good history. A missing bureau record can mean a genuinely new borrower, a customer whose products simply are not covered by the reporting agency, a limited reporting footprint, or a broken key linkage. None of those is "clean repayment", and none is "high risk" either. It is uncertainty.

Treating a missing value as zero delinquency would silently reward invisibility. The pipeline therefore keeps availability and absence as first-class information:

- `INST_COUNT` distinguishes *no observed instalment history* from *observed and clean*.
- `FLAG_NO_BUREAU` marks the absence of a matched bureau parent rather than imputing zero arrears.
- Card-history and previous-application availability become explicit items in the association vocabulary, so "no history" can appear in a rule as itself.
- Anomaly recommendations for thin files request permitted alternative evidence instead of inferring risk from the gap.

### 2.5 External scores

`EXT_SOURCE_1/2/3` are externally supplied risk scores whose construction and calibration are not public. They are strong statistical predictors, but an opaque score cannot carry a causal or explanatory story. Lower values are treated as adverse *context* at a descriptive level only.

Missingness here is informative in itself: `EXT_SOURCE_1` is unavailable for 54.43% of the combined portfolio, which correlates with thin credit files. Median imputation supports a complete numeric matrix for distance computation, but the case-review text always uses the preserved source value and never presents an imputed median as an observed score.

### 2.6 Revolving credit utilisation

High card utilisation is genuinely ambiguous. It can indicate liquidity pressure, or an active transactor who clears the balance monthly, or simply a limit set too low for normal spending, or a statement-timing artefact. Utilisation is therefore always paired with balance, payment capacity, delinquency, and limit suitability, never used as a standalone adverse signal.

### 2.7 Previous refusals

A prior refusal records an earlier decision under earlier circumstances and an earlier policy. It may reflect affordability at the time, a documentation gap, product fit, or a duplicate application. The correct treatment is to reconcile the historic reason against current evidence, not to treat a refusal count as immutable risk.

### 2.8 Time and aggregation

Most `DAYS_*` fields are negative offsets from the application date, so values closer to zero are more recent. For `DAYS_DECISION` the maximum is the *most recent* previous decision and the minimum the earliest, a direction that is easy to invert by accident, and which the pipeline handles explicitly.

Aggregating relational histories to applicant grain makes clustering tractable but discards event order and within-account detail. That trade is accepted for mining and compensated at review time by sending the reviewer back to source.

---

## 3. Evaluation boundary

| Population | Rows | Permitted use |
|---|---:|---|
| Combined train + test | 356,255 | Unlabelled discovery and portfolio profiling |
| Labelled train | 307,511 | Train-only outcome diagnostics |
| Unlabelled test | 48,744 | Discovery only, never enters precision, recall, lift, AUC, or calibration |

Train and test are combined for discovery, with a source flag preserved throughout. This is legitimate for unsupervised profiling of a known, fixed portfolio: the segmentation describes the applications actually in front of us. It would **not** be a valid way to estimate deployment performance, because the model has seen the evaluation distribution. The report labels this transductive throughout and never calls it validation.

The observed train default rate is **8.07%**. This base rate must accompany every precision or lift statement in this document. A precision of 10.05% sounds low in isolation and is genuinely weak, but it is 1.25x the base rate, not worse than random.

---

## 4. Phase 1: Data construction and preprocessing

### 4.1 Why the tables are combined

An application row on its own describes a request, not a borrower. The bureau, previous-application, POS, instalment, and card tables are aggregated to `SK_ID_CURR` with counts, recency, delinquency, utilisation, approval history, and payment ratios, giving each application a behavioural context to be compared on.

### 4.2 Data quality findings and their treatment

| Issue | Affected | Business meaning | Treatment and why |
|---|---:|---|---|
| `DAYS_EMPLOYED = 365243` | 64,648 (18.15%) | A coded state for pensioners and the non-employed, not 1,000 years of service | Replace with missing, retain a sentinel flag. Leaving it numeric would corrupt every distance and every employment-tenure statistic |
| `EXT_SOURCE_1` unavailable | 193,910 (54.43%) | Score uncertainty or a thin file; not adverse behaviour | Median-impute for computation, keep an explicit missing flag so absence stays visible |
| Housing detail unavailable | 171,055 (48.01%) | Property record not captured; not proof of poor credit quality | Structural zero plus a no-housing-data indicator |
| No car-age value | 235,241 (66.03%) | Usually structural, the applicant has no car | Set to zero, retain a no-car indicator |
| Income above p99 | 3,549 (1.00%) | Rare but frequently genuine amounts | Cap the *clustering* value only; preserve the source value and the audit trail |

The pattern is consistent: the model-facing value is made robust, and the true value is preserved for anyone who has to explain a decision to a customer.

### 4.3 Outliers, scaling, and the two-view design

Financial amounts and behaviour ratios are heavily right-skewed. Log transforms compress positive amounts; 34 continuous distance axes are clipped at the 0.5th and 99.5th percentiles before standardisation for the clustering matrix only.

The clipping decision was tested rather than assumed. Without it, a handful of extreme files capture K-Means centroids and seed agreement collapses to roughly ARI 0.73. With it, sampled seed agreement rises to about 0.99-1.00. Stabilising the geometry is worth it, but stability of the *model view* never licenses rewriting the *evidence*, so original values persist in `SOURCE_*` columns.

This produces the deliberate two-view design that runs through the whole project:

- **Clustering sees** robust, clipped, standardised values, so distances behave.
- **Reviewers see** source values plus whether each was observed, capped, or imputed.

Final artefacts: 65 readable business/audit columns and 42 clustering features, plus a parallel unclipped 42-feature matrix for anomaly detection. Binary flags stay 0/1; continuous and ordinal axes are standardised. Gender is excluded from clustering. Mutual information against train `TARGET` is computed as a feature-relevance *check* only and never enters clustering. One correlated pair above 0.85 remains, mean versus maximum card utilisation at 0.892, kept deliberately because the two carry different business meaning (typical behaviour versus peak stress).

### 4.4 The one data warning

`bureau_balance.csv` contains 3,120,184 monthly rows (11.43% of the table) whose `SK_ID_BUREAU` has no parent in `bureau.csv`. Without the parent they cannot be mapped to an applicant.

These rows are excluded from aggregation and the count is recorded. The pipeline does not guess an applicant ID or invent a bureau relationship. This limits completeness but preserves key integrity, the right trade, since a fabricated linkage would contaminate every downstream behavioural feature.

---

## 5. Phase 2: Segmentation

### 5.1 Dimensionality reduction

Ten principal components retain **63.28%** of variance across the 42-feature matrix. The justification is not "it captures the signal", it is that the segmentation barely moves when more components are retained:

| Components | Variance retained | Silhouette | ARI vs 10 PCs |
|---:|---:|---:|---:|
| 10 | 63.28% | 0.153 | 1.000 |
| 16 | 80.01% | 0.113 | 0.979 |
| 22 | 91.45% | 0.092 | 0.973 |
| 42 | 100.00% | 0.079 | 0.973 |

Labels agree at ARI >= 0.973 all the way to the full space, and the compact view scores best on silhouette. So 10 components is a sensitivity-supported choice.

Retention improved from 55.59% to 63.28% when the seven protected and proxy attributes were removed (Section 1b, F1). That is the expected direction: those axes carried variance that was largely independent of credit behaviour, so the principal components had been spending capacity describing demographic spread rather than borrowing and repayment patterns.

*A correction worth recording:* an earlier version of this project justified 10 components by claiming PC11 added only 0.08 percentage points. That was wrong, and the claim was replaced by the stability argument above.

### 5.2 Choosing K

| K | Silhouette | Davies-Bouldin | Smallest share | Largest share |
|---:|---:|---:|---:|---:|
| 2 | 0.250 | 1.741 | 17.26% | 82.74% |
| 3 | **0.263** | **1.429** | 2.28% | 80.69% |
| 4 | 0.149 | 1.772 | 2.20% | 42.61% |
| 5 | 0.150 | 1.709 | 2.17% | 34.31% |
| 6 | 0.155 | 1.575 | 1.24% | 33.83% |

**K=3 wins on both geometric metrics, and K=5 was chosen anyway.** That needs justifying rather than hiding.

K=3 achieves its score by producing one dominant blob holding 80.69% of the portfolio. Geometrically tidy; operationally useless, because "80% of applications" is not a segment anyone can staff or act on. K=5 splits that mass into distinct, non-empty, interpretable operating profiles, the smallest still holds 2.17%, at a modest silhouette cost.

This is a business-resolution decision, and the report states it as such. Claiming K=5 as the statistical optimum would be false.

Stability is strong regardless: pairwise adjusted Rand indices across seeds 42/52/62 are 0.9986, 0.9941, and 0.9936.

### 5.3 Method sensitivity

**Hierarchical (Ward)** is fitted on a sample and extended by nearest-centre assignment: ARI 0.603, NMI 0.600 against K-Means.

This weakened after the F1 correction, it was ARI 0.719 / NMI 0.726 on the 49-feature matrix, and the drop is reported rather than buried. The most plausible reading is that the removed demographic axes were partly what the two methods had been agreeing *about*: age, region, and education spread applicants along directions that both a centroid method and a linkage method pick up easily. With only behavioural and capacity axes left, the remaining structure is more genuinely credit-shaped but also more diffuse, and the two algorithms agree less about where to cut it.

The honest conclusion is that corroboration is now moderate rather than strong. The K-Means partition is stable under reseeding and under added dimensions, but a different family of algorithm would draw somewhat different boundaries. That is a limitation on how much authority any single partition carries, and it argues for treating segments as review-routing conveniences rather than as discovered natural kinds.

**DBSCAN** runs on a reproducible, distribution-checked 50,000-row sample in UMAP space and marks 568 points as density noise. UMAP distorts global distance and density by design, so this is an exploratory density view only. Those 568 points are **not** fraud, not defaults, and not a portfolio-wide anomaly label.

### 5.4 The five segments

| Segment | Applications | Median income | Median credit | Credit  /  income | Annuity  /  income | Median late instalment share |
|---|---:|---:|---:|---:|---:|---:|
| High-Exposure Applicant | 122,395 | 157,500 | 808,649 | 5.24x | 22.01% | 0.00% observed |
| Thin-File / Low-Intensity | 120,294 | 135,000 | 269,550 | 2.06x | 12.98% | 0.00% observed |
| Intensive Card User | 54,518 | 157,500 | 544,490 | 3.26x | 15.66% | 3.97% |
| History-Rich Credit User | 51,426 | 175,500 | 463,284 | 2.67x | 14.54% | 5.17% |
| Repayment-Stress History | 7,622 | 135,000 | 497,520 | 3.35x | 17.26% | 28.57% |

These names describe dominant portfolio geometry. They are not character judgments and not decision labels.

**The segments barely moved when the protected attributes were removed.** Against the previous 49-feature run, membership shifted by -0.03% (Intensive Card User), -0.2% (Repayment-Stress History), -1.3% (Thin-File), -1.7% (History-Rich), and +2.0% (High-Exposure). The naming logic, which keys on instalment delinquency, card utilisation, relationship depth, and borrowing scale, assigned all five labels to the same profiles.

This is the most important result of the F1 correction, and it is worth stating plainly: age, number of children, region rating, education, income type, employer sector, and social-circle arrears were carrying **regulatory and ethical exposure without carrying analytical weight**. The portfolio's structure is driven by how people borrow and repay, not by who they are demographically. Removing them cost essentially nothing and improved the compactness of the representation at the same time.

| Segment | What dominates | What a reviewer should ask |
|---|---|---|
| Thin-File / Low-Intensity | Limited product exposure and observed history | Is evidence genuinely absent, or is this a low-activity but sound applicant? Seek permitted alternative evidence; do not read absence as either safety or risk |
| High-Exposure Applicant | Largest requested credit, leverage, and annuity burden | Does verified income support this exposure under stress? Confirm total obligations, not just this one |
| Intensive Card User | Revolving history and utilisation | Are balances, payments, and limits sustainable now? Check limit suitability before changing exposure |
| History-Rich Credit User | Depth of internal and external history | Which historical concerns still matter today? Use the depth to verify current position, never to assume it |
| Repayment-Stress History | Instalment and POS lateness | How recent, how severe, and was it cured? Existing hardship must route through policy, not through this dashboard |

---

## 6. Phase 3: Association rules

### 6.1 Vocabulary and search

Transactions use domain bins for income, requested credit, leverage, repayment burden, external-score availability, instalment behaviour, card utilisation, bureau depth and debt, previous-application depth and outcome, and cluster membership. Itemsets are capped at length three with a single consequent, keeping rules readable and reviewable.

Apriori, FP-Growth, and ECLAT are compared **on the same 356,255 full-portfolio transactions** and return an identical 1,943 rules, as they must, since the three algorithms differ in traversal strategy, not in the itemsets they are capable of finding. This is an implementation-correctness check, not three independent confirmations of a finding. Per-segment FP-Growth (3,503 rules) keeps its own segment denominators and is reported separately, never counted as a fourth confirming algorithm.

### 6.2 What gets rejected, and why it matters

| Rejection reason | Rules removed |
|---|---:|
| Algebraic financial identity (two or more affordability families) | 2,460 |
| Same-source missingness identity | 274 |
| Schema-induced missingness identity (parent-child key) | 76 |
| **Accepted as non-trivial** | **1,706** |

This matters more than it sounds. A rule like `high credit + low income -> high leverage` has enormous lift and is worthless: leverage is *defined* as credit divided by income, so the rule rediscovers arithmetic. Without these filters the top of any lift-ranked table fills with restatements of the feature engineering.

**18 rules are displayed**, three per segment plus three portfolio-wide, with lift from 1.20 to 3.23. Every exported rule carries support count, support, confidence, lift, and its population denominator.

### 6.3 The honest read: this vocabulary yields few independent patterns

The 18 displayed rules reduce to 10 distinct patterns once duplicates across segments are collapsed. Of those, **four are structural and six carry genuine cross-source information.**

The structural four all live inside the previous-application family:

> `{previous_one} -> {previous_approval_high}` (confidence 99.4%) - `{previous_refusals_repeated} -> {previous_deep}` - `{previous_two_to_four} -> {previous_approval_high}` - `{card_utilisation_moderate, previous_outcome_mixed} -> {previous_deep}`

An applicant with exactly one previous application has an approval rate of either 0 or 1, so "approval rate >= 0.75" simply means that single application was approved, and most applications are approved. Likewise, three or more refusals cannot occur without at least three applications. These are arithmetic consequences of counting, dressed as discoveries.

The six informative ones are more interesting, and three of them are genuinely cross-source:

> `{external_score_strong} -> {bureau_debt_low}` (lift 1.21) - `{bureau_debt_moderate} -> {external_score_weak}` (lift 1.20) - `{credit_small, external_score_weak} -> {previous_refusals_repeated}` (lift 1.26)

The first two say that an opaque external score agrees with independently reported bureau debt, a useful convergent-validity check on a score whose construction is not public. The third is the most business-relevant rule in the table: applicants with weak external scores and small requested amounts are disproportionately those Home Credit has repeatedly refused. In other words the lender's own historical decisions align with external assessment, which is reassuring for consistency and also a caution, since it means the two signals are not independent evidence.

### 6.4 Why the filter was not tightened further, and what that reveals

The rejection filter went through three tightenings during this project. Each was individually justified: removing cluster items, adding the schema-induced category, then requiring at most one affordability family per rule.

That third change had an instructive result. It eliminated every affordability artefact, and the table immediately filled with previous-application count structure instead. The same defect reappeared in a different table.

The root cause is now clear and is a property of the vocabulary, not of any one filter. **The item set contains several derived views of the same few underlying quantities.** Income, credit size, leverage, and burden are four vocabularies over three raw amounts. Previous depth and previous outcome are two vocabularies over the same application counts. Any rule connecting two views of one quantity will show high confidence, because it is partly restating a definition.

A fourth tightening would have removed the previous-application pairs too. It was not applied, deliberately. Tuning a filter repeatedly until the surviving table looks satisfying is exactly the garden-of-forking-paths error this report polices elsewhere, and at some point the correct output of the analysis is the finding itself rather than a prettier table.

**That finding is:** association mining over this vocabulary produces very few independent patterns. Three rules carry real cross-source information. The rest largely re-describe how the features were built. For a future iteration the fix is at the vocabulary level, one item family per underlying source quantity, not at the filter level.

### 6.5 Reading the rules honestly

Rules mentioning absent history are **data-availability findings**. `{card_history_not_observed, previous_one} -> {repayment_clean_observed}` describes information coverage: a customer with one previous application and no card record still has an observable, clean instalment record. That is useful for knowing what evidence exists, and it says nothing about whether the applicant is a good risk.

Each rule is linked on the dashboard to a review action rather than to a decline rule.

Association is not causation. A rule is a portfolio pattern worth monitoring, not a credit policy. Three limitations stand:

- **Multiplicity.** Thresholds, search length, rejection counts, and final selections are all exported, but rule discovery has no external holdout, so these remain exploratory.
- **Vocabulary redundancy.** Described in 6.4: several item families are derived views of the same underlying quantities, which inflates confidence for rules that connect them.
- **Non-independence of the informative rules.** The external-score and bureau-debt rules are convergent by nature. They confirm that two risk assessments agree; they do not supply two independent pieces of evidence about an applicant.

---

## 7. Phase 4a: Anomaly review

### 7.0 Two routes into one queue

A record reaches human review by either of two independent paths, and the paths answer different questions:

- **Detector consensus**, at least three detectors agree the record is unusual, and they represent at least half of those available for it. This finds records that are unusual *in combination*.
- **Implausible single value**, any standardised axis at or beyond 10 SD. This finds records that are catastrophic *in one field*, which detector consensus is structurally unable to see (Section 1b, F4).

They are reported separately throughout. Blending them would hide the fact that they have different evidential status: consensus says several methods agree something is odd, while a 10-SD value says one number is almost certainly wrong.

### 7.1 Six detectors, and why more than one

Every detector encodes an assumption. Adjusted IQR and empirical Z-score are per-column and assume a shape for each margin. Mahalanobis assumes an elliptical joint distribution. Isolation Forest is non-parametric but sensitive to its contamination setting. LOF is local-density based. DBSCAN noise is sampled and UMAP-distorted.

Requiring agreement across independent assumptions is what makes the queue conservative, a record has to look unusual under several different definitions of unusual.

| Detector | Records flagged | How the count is set |
|---|---:|---|
| Adjusted IQR | 1,295 | Discovered from the data's own dispersion |
| Empirical Z-score | 5,906 | Empirical 99th percentile |
| Robust Mahalanobis | 8,907 | Fixed 2.5% quantile |
| Isolation Forest | 17,813 | Fixed 5% contamination |
| Local Outlier Factor | 8,907 | Fixed 2.5% quantile |
| DBSCAN noise (50k sample) | 568 | Discovered from density |

Only the 50,000-row DBSCAN sample has all six signals available; every other row has five. The agreement denominator is therefore record-specific, which the consensus rule accounts for.

One property of this table deserves stating rather than glossing. Mahalanobis and LOF report **exactly** 8,907 records each, and Isolation Forest exactly 17,813, because all three are configured to flag a fixed share of the portfolio. Those detectors do not discover how many anomalies exist; the count is chosen in advance and they rank records to fill it. Only adjusted IQR and DBSCAN respond to how unusual the data actually is. This matters when reading detector-agreement statistics: part of any overlap between Mahalanobis and LOF is a consequence of both having been told to flag 2.5%.

### 7.2 Threshold sensitivity is the real finding

| Setting | Records | Share |
|---|---:|---:|
| Conventional IQR 1.5x, 3+ columns | 68,297 | 19.17% |
| Adjusted IQR calibrated, 3+ columns | 1,295 | 0.36% |
| Conventional \|z\| > 3, 3+ columns | 8,199 | 2.30% |
| Empirical 99th percentile Z, 3+ columns | 5,906 | 1.66% |
| Isolation Forest, 1% contamination | 3,563 | 1.00% |
| Isolation Forest, 5% contamination | 17,813 | 5.00% |
| Isolation Forest, 10% contamination | 35,626 | 10.00% |

A textbook 1.5x IQR rule would refer 68,297 applications, roughly one application in five, to manual review. No credit operation can staff that, and a queue that large is functionally the same as no queue at all. The same detector family, calibrated to the data's actual dispersion, refers 1,295.

Nothing about the underlying portfolio changed between those two rows. Only a convention did. That is the argument for requiring detector agreement and human evidence review rather than trusting any single threshold.

The conventional Z-score row moved noticeably after the F2 correction, from 13,395 records to 8,199. This is the expected direction and worth understanding: restoring the true tails widens each axis's standard deviation, so a fixed \|z\| > 3 cut sits further out in absolute terms and catches fewer records. It is a reminder that a "3 sigma" rule is a statement about the spread you measured, not about the applicant.

### 7.3 The consensus queue

| Category | Records | Share |
|---|---:|---:|
| **Review queue (both routes)** | **5,914** | **1.66%** |
| , detector consensus | 2,491 | 0.70% |
| , implausible single value | 3,423 | 0.96% |
| Moderate, 2 signals | 5,599 | 1.57% |
| Weak, 1 signal | 20,632 | 5.79% |
| No flag | 324,110 | 90.98% |

The two routes are mutually exclusive as labelled, a record satisfying both is counted under consensus, and 911 consensus records also carry an implausible single value, which is a reassuring sign that the routes are looking at overlapping but not identical evidence.

DBSCAN independently corroborates 39 queued records. "Consensus" means agreement on *unusualness*, never a calibrated probability of default.

The queue shrank by a third after the F2 correction, from 3,758 records to 2,491, while independent DBSCAN corroboration *rose* from 22 to 37, and rose despite there being fewer noise points to corroborate with (568 against 914). Both movements point the same way. On the clipped matrix, thousands of records had been collapsed onto identical boundary values, so several detectors flagged the same artificial pile-ups together and manufactured agreement. With the true tails restored, the detectors agree less often but agree about records that an unrelated density-based method also considers unusual. A smaller queue that a fourth method independently supports is a better queue.

### 7.4 Three kinds of unusual

Detector count says *how* unusual a record is. It does not say *what kind*, and the kind determines who reviews it and what they check first. Each queued record is classified by scope:

| Scope | Records | What it means | Why it is a credit problem |
|---|---:|---|---|
| **Global** | 1,037 | A value sits outside the plausible range for the whole portfolio | Either the figure was captured wrongly or the file is genuinely extreme. Either way, affordability tables and cut-offs calibrated on the bulk of the book do not apply. Confirm at source before assessment continues |
| **Contextual** | 4,838 | Each value is ordinary alone; the *combination* is unusual for the applicant's peer group | The hardest kind to catch and the most consequential. No single-field rule fires, so these files pass rule-based controls untouched. Only a multivariate view sees that the pattern does not fit applicants who otherwise look identical |
| **Collective** | 39 | A small group shares a shape that is rare for the portfolio | When records cluster in a sparse pocket, the cause is usually systemic rather than individual, one channel, branch, product, or intake period behaving differently. Investigate as a group; reviewing them one at a time hides the common cause |

This classification only became trustworthy after the F2 correction. On the clipped matrix, a "global extreme" could not exist in any meaningful sense, because every axis had been truncated at its 0.5th and 99.5th percentile, the category was really measuring "sits on the clip boundary".

Two cross-tabulations carry real information:

**Contextual anomalies concentrate in the repayment-stress population.** Of 4,838 contextual records, 2,475 sit in Repayment-Stress History, a segment of only 7,622 applicants, roughly one in three of that entire segment. Intensive Card User holds a further 1,205. The concentration is less extreme than before the correction (it was 85% in a single segment) and the spread across two behaviourally distinct segments is more credible.

**Every data-consistency check is a global extreme.** All 114 of them; none are contextual. This is exactly what the domain predicts: a mistyped or wrongly-scaled figure lands outside the plausible range and trips a margin detector, whereas a suspicious *combination* of individually valid figures points at affordability rather than at data capture. The pattern survived the F2 correction unchanged, which is meaningful, it held under a completely different detection matrix, so it reflects how capture errors behave rather than an artefact of one preprocessing choice.

| Scope | Affordability / repayment | Data consistency | Rare but plausible |
|---|---:|---:|---:|
| Global | 915 | 114 | 8 |
| Contextual | 4,825 | 0 | 13 |
| Collective | 38 | 0 | 1 |

**What the correction surfaced.** The drivers behind the queue shifted in exactly the way the F2 diagnosis predicted. "High card utilisation" rose from 115 records to 342, and "High payment burden" from 136 to 219. Those are precisely the axes clipping had flattened: `CC_UTILIZATION_MAX` topped out at 2.49 standard deviations in the old matrix and reaches 4.77 in the corrected one. Applicants running genuinely extreme revolving balances had been rendered statistically ordinary before any detector saw them.

### 7.5 What a reviewer receives

Each of the 5,914 rows carries the applicant ID, actual evidence values, the value basis (observed, capped, or imputed), primary and supporting drivers, a business interpretation, review priority, review owner, and a specific next action written from that record's own evidence.

The recommendations are generated from each record's actual figures, not selected from a template list. A row reads, for example, that the longest observed instalment delay is 481 days, that bureau history shows 6.4% of months late and 4.1% severely late, and that average card utilisation is 64.8% against a maximum of 105.4%, then asks the reviewer to check recency, dispute status, and cure status before any credit action.

Every row states **Automatic Decision Allowed = No**. Statistical rarity can equally be a data problem, a legitimately unusual applicant, or a genuine affordability concern, and only evidence separates them.

---

## 8. Phase 4b: Does cluster membership predict default?

This section answers a limited, explicitly bounded question: **do the unsupervised segments separate observed payment difficulty better than the portfolio base rate?**

### 8.1 Method, and why it is constructed this way

The cluster label is turned into a risk flag and scored against the real `TARGET`, using train IDs only.

1. `TARGET` is loaded from `application_train.csv` alone, then inner-joined to cluster labels on `SK_ID_CURR` with `validate="one_to_one"` and a hard assertion that the matched row count equals 307,511.
2. Rows are split into five stratified folds. For each fold, per-segment default rates and the portfolio baseline are estimated **only from the other four folds**.
3. A validation row is flagged when its out-of-fold segment rate is at least 1.10x that fold's baseline.
4. Precision, recall, specificity, F1, lift, average precision, and ROC AUC are computed on the resulting flags.

**Audit of this design, the four things that could invalidate it:**

- **Test contamination.** Structurally impossible. `target` contains only train IDs, and the one-to-one merge plus row-count assertion means any test row entering the join would raise rather than silently score. `test_rows_scored` is recorded as 0.
- **Target leakage through the clusters.** K-Means never saw `TARGET`; it was fitted on the 42 clustering features, from which `TARGET`, gender, and every protected or proxy attribute are excluded. Using cluster membership as a predictor is therefore not leakage.
- **Leakage through the rate estimates.** This is the real risk, and cross-fitting is what addresses it. Without it, each row's own outcome would contribute to the segment rate used to score that same row, inflating every metric. The out-of-fold construction removes that.
- **Transductive segmentation.** The clusters were fitted on train and test combined, so the segmentation has seen the evaluation distribution. This does not leak labels, but it does mean the result is *not* an inductive estimate of future performance. It is reported as outcome alignment, never as validation.

Three honest caveats on the implementation, none of which change the conclusion:

- **The smoothing term is nearly inert.** Rates are smoothed toward the baseline with a weight of 200 against segments holding 6,870 to 106,558 applicants. Even the smallest segment moves by under 3%. It is harmless insurance against a small-segment artefact, not an active component.
- **AUC and average precision are computed on a step function.** With five segments across five folds there are only 25 distinct score values, so an AUC of 0.557 describes a very coarse ranking. It is reported because it is the conventional metric, but precision, recall, and lift are the meaningful numbers here.
- **The threshold sits on a plateau.** Uplift settings from 1.10 through 1.30 produce byte-identical results, because a five-level score cannot respond continuously to a moving cut. This makes the 1.10 choice robust rather than arbitrary, but it also means review capacity cannot be tuned smoothly, which is itself a limitation of segment-level flagging.

### 8.2 Result

| Metric | Value |
|---|---:|
| Evaluation rows | 307,511 |
| Test rows scored | 0 |
| Flagged share | 28.52% |
| **Precision** | **10.05%** |
| **Recall** | **35.51%** |
| Specificity | 72.10% |
| F1 | 15.67% |
| Lift over the 8.07% base rate | 1.25x |
| Average precision | 9.51% |
| ROC AUC | 0.553 |

| | Not flagged | Flagged | Total |
|---|---:|---:|---:|
| Actual non-default | 203,810 | 78,876 | 282,686 |
| Actual default | 16,010 | 8,815 | 24,825 |
| Total | 219,820 | 87,691 | 307,511 |

Observed default rate by segment:

| Segment | Train applicants | Defaults | Default rate | Lift |
|---|---:|---:|---:|---:|
| Repayment-Stress History | 6,858 | 814 | 11.87% | 1.47x |
| Intensive Card User | 46,565 | 4,965 | 10.66% | 1.32x |
| History-Rich Credit User | 42,828 | 3,842 | 8.97% | 1.11x |
| Thin-File / Low-Intensity | 102,555 | 8,164 | 7.96% | 0.99x |
| High-Exposure Applicant | 108,705 | 7,040 | 6.48% | 0.80x |

The flagged share moved from 17.38% to 28.52% between runs without the threshold being touched. The cause is visible in the table above: History-Rich Credit User rose from 8.51% to 8.97%, crossing the 1.10x uplift line, so a third segment now qualifies. Nothing about the rule changed, the segment did, because it is built from a different feature set.

This is worth pausing on, because it is a general property of segment-level flagging rather than a quirk of this run. A five-level score cannot respond smoothly to a threshold. One segment drifting slightly changes review volume by eleven percentage points of the portfolio, which is tens of thousands of applications. Any operational use of such a flag would need volume monitoring, not just a threshold.

### 8.3 Why precision is low, and why that is not a bug

The ceiling is arithmetic. The worst-performing complete segment defaults at **11.87%**. Any rule that can only select *whole segments* cannot exceed that precision, because it must take every member of whichever segments it picks, and in the highest-rate segment, 88% of members did not default.

The trade-off is visible in the policy sweep:

| Uplift threshold | Flagged share | Precision | Recall |
|---:|---:|---:|---:|
| 1.00-1.05 | 31.30% | 10.00% | 38.76% |
| 1.10 | 28.52% | 10.05% | 35.51% |
| 1.15-1.30 | 17.37% | 10.82% | 23.28% |
| 1.35-1.40 | 2.23% | 11.87% | 3.28% |
| 1.45 | 1.34% | 11.56% | 1.93% |

Flagging only the single highest-rate segment achieves the 11.87% ceiling and captures just 3.28% of defaults. Higher recall requires broader segments and accepts proportionally more false positives. There is no setting at which segment membership becomes an accurate individual predictor.

**A note on not re-tuning the threshold.** In the previous run, 1.10 through 1.30 produced identical results, so the choice sat on a wide, robust plateau. It no longer does: 1.10 now occupies a narrow ledge of its own, and moving to 1.15 would improve precision from 10.05% to 10.82% while nearly halving review volume. The 1.10 setting was pre-registered before the segments were rebuilt and has been kept. Changing it now, after seeing which value flatters the result, would be precisely the garden-of-forking-paths error catalogued in Section 9, and reporting the weaker pre-registered number is the point of pre-registering it.

A striking domain observation sits in the segment table: **High-Exposure Applicant has the *lowest* observed default rate at 6.48%**, well below the portfolio's 8.07%. The segment with the largest requested credit, highest leverage, and heaviest annuity burden defaults least, and it held this position across both feature sets, so it is not an artefact of one segmentation.

The most plausible reading is selection. Large exposures attract the most stringent underwriting and are approved only for the best-documented applicants, so the observed cohort has already been filtered. The data cannot show us the high-exposure applicants who were declined; it shows only those who survived the existing credit policy. This is a clean illustration of Berkson's paradox in a live portfolio, and of why an observed cohort rate must never be read as the risk of an individual within it. "This segment looks safe, so relax the criteria" would be exactly the wrong conclusion, the segment looks safe *because* the criteria were strict.

### 8.4 The objective-mismatch test

To confirm the low precision reflects the *objective* rather than a broken pipeline, a separate logistic regression is trained for outcome separation on the same 307,511 train rows, five-fold out-of-fold, cut at the identical 28.52% review capacity. Since the F1 correction it draws on the same 42 features, so the two methods now differ only in what they optimise.

| Metric | Cluster alignment | Logistic diagnostic |
|---|---:|---:|
| Precision | 10.05% | **17.67%** |
| Recall | 35.51% | **62.43%** |
| Lift | 1.25x | 2.19x |
| Average precision | 9.51% | 23.25% |
| ROC AUC | 0.553 | 0.750 |
| Brier score |, | 0.0683 |

At identical review capacity, the outcome-trained model improves both precision and recall by a factor of 1.76. The signal was available in the features; clustering simply was not optimising for it. Clustering minimises within-group distance, which groups applicants who *look alike*. Applicants who look alike do not necessarily default alike.

Two cross-run observations strengthen this reading. First, the diagnostic's ROC AUC (0.750 against 0.751) and average precision (0.2325 against 0.2333) are essentially unchanged from the 49-feature run, removing the seven protected and proxy attributes cost the supervised model nothing measurable either. Second, its headline precision fell from 21.75% to 17.67% only because the review capacity it is matched to grew from 17.38% to 28.52%; precision necessarily falls as a queue widens. The model's intrinsic discrimination is the same, and the comparison remains like for like because both methods are cut at the same capacity.

This is a methodological reference and nothing more. It is not calibrated for deployment, has no out-of-time test, and is not production-ready.

### 8.5 The conclusion this supports

1. **Keep clustering** for portfolio segmentation, rule context, review design, and communication. It does that job well and stably.
2. **Do not use cluster membership as an applicant-level default model.** At best it reaches 11.87% precision, and it cannot rank applicants within a segment at all.

Reporting a weak predictive result is part of the analysis, not a defect to conceal. The negative result is what justifies recommendation 2.

---

## 8b. What this means commercially

Everything above measures how often customers fall behind. A lender loses money, not percentages, and the two rank the portfolio very differently. Multiplying each segment's observed defaults by its median loan gives a first-order view of money at risk:

| Segment | Default rate | Share of customers | Share of defaults | Share of money at risk | Share of lending | Median loan |
|---|---:|---:|---:|---:|---:|---:|
| High-Exposure Applicant | 6.48% | 35.3% | 28.4% | **44.5%** | 52.5% | 808,649 |
| Intensive Card User | 10.66% | 15.1% | 20.0% | 21.2% | 15.7% | 544,490 |
| Thin-File / Low-Intensity | 7.96% | 33.4% | 32.9% | 17.2% | 17.2% | 269,550 |
| History-Rich Credit User | 8.97% | 13.9% | 15.5% | 13.9% | 12.6% | 463,284 |
| Repayment-Stress History | 11.87% | 2.2% | 3.3% | 3.2% | 2.0% | 497,520 |

Read down the default-rate column and then down the money-at-risk column, and the ordering inverts almost completely.

**The safest segment carries the most money at risk.** High-Exposure Applicant fails least often, 6.48% against the 8.07% book average, and still accounts for 44.5% of money at risk, because its typical loan is three times the smallest segment's. A low failure rate applied to a large balance costs more than a high failure rate applied to a small one. Any capacity plan built from the default-rate column alone would direct the most scrutiny to the least expensive problem.

**The worst segment is financially marginal.** Repayment-Stress History fails at 1.47x the book average and is the group any reviewer would name first. It is 6,858 labelled customers holding 3.2% of money at risk. Eliminating its losses entirely would move total portfolio loss by roughly three percent. It deserves a treatment queue, and its small size makes one genuinely feasible. It does not deserve to be the centre of loss strategy.

**Revolving credit is the one concentrated, actionable risk.** Intensive Card User is 15.1% of customers, 20.0% of defaults, and 21.2% of money at risk: over-represented on every measure, with median utilisation at 54.5% of limit. It is also the only segment where the lender retains a live instrument. An instalment loan is fixed at signing; a card limit can be reviewed while the customer is still performing. Utilisation-triggered limit and affordability review is the highest-leverage intervention the portfolio offers.

**A third of the book is unmeasured rather than risky.** Thin-File / Low-Intensity is 33.4% of customers and fails at 7.96%, *below* the book average, while 54.4% of the whole portfolio has no `EXT_SOURCE_1` at all. The commercial error here is treating absent information as adverse information. These customers perform slightly better than average; what is missing is evidence, not quality. Collecting permitted alternative evidence turns an underserved population into a priceable one.

### The caution that governs all of the above

High-Exposure Applicant looks safe partly *because* it was screened hardest. Large exposures attract the strictest underwriting, so the approved cohort is the one that passed those checks, and the declined applicants are invisible to this data. The low observed rate is evidence that existing controls work, not evidence that they are unnecessary. Reading it as headroom to relax criteria would remove the mechanism producing the result, a textbook selection effect, and the most expensive misreading available in this report.

Two further limits apply to the table itself. Median loan size is a crude stand-in for exposure at default: it ignores amortisation, recoveries, and loss given default, so the money-at-risk column ranks segments rather than valuing them. And every figure derives from labelled training applications only, so it describes the book as observed, not as it will behave.

---

## 9. Statistical and interpretive governance

| Risk | Status | Control applied |
|---|---|---|
| Simpson's paradox | Limitation | Portfolio and all segment rates shown; the extract has no product, market, or calendar strata for a full reversal test |
| Ecological fallacy | Mitigated | Applicant-level decisions from segment averages are prohibited throughout |
| Berkson's paradox | Limitation | Claims restricted to observed applicants; Home Credit's selection mechanism is unknown |
| Collider bias | Mitigated | No causal effects estimated after conditioning on cluster |
| Base-rate neglect | Mitigated | Base rate, precision, lift, AP, and false-positive counts always reported together |
| Regression to the mean | Not applicable | No before/after treatment-effect claim is made |
| Survivorship bias | Limitation | No history separated from clean history; observability still shapes the data |
| Look-elsewhere effect | Limitation | Thresholds, search length, rejections, and final counts all exported |
| Garden of forking paths | Mitigated | Seeds, K range, thresholds, and sensitivity tables fixed in code |
| Causation fallacy | Mitigated | Every mined relationship labelled descriptive |
| Reverse causality | Mitigated | Repayment history used as context, not as mechanism |

### Fairness

Gender is excluded from clustering. The supervised diagnostic additionally excludes direct age, education, income-type frequency, organisation-type frequency, and region-rating proxies.

These exclusions reduce obvious risk but **do not prove fairness**. Financial variables can still act as proxies for protected characteristics, and demonstrating fairness would require disparate-impact testing that this project has not performed.

No unsupervised output authorises rejection, pricing, limit reduction, or adverse action.

### Claims this project explicitly does not make

- That DBSCAN noise indicates fraud or default.
- That detector consensus is a calibrated probability.
- That a segment average applies to any individual member.
- That a high-lift rule is causal.
- That train/test combined discovery constitutes deployment validation.
- That the logistic reference is production-ready.

---

## 10. Validation

`VERIFIED`. 71 checks, 70 passed, 1 warning, 0 failed. Machine-readable outputs in `results/validation/`.

The material passport records SHA-256 hashes, byte sizes, and row/column contracts for all eight raw files. Train and test contribute 307,511 and 48,744 unique IDs with no overlap; all applicant-level outputs retain exactly 356,255 unique IDs.

| Contract | Result |
|---|---|
| Business artefact | 356,255 rows x 65 columns |
| Clustering artefact | 356,255 rows, ID + 42 features |
| Duplicate applicant IDs | 0 |
| Non-finite clustering values | 0 |
| `TARGET` in clustering matrix | No |
| Gender in clustering matrix | No |
| Source-value columns in distance matrix | No |
| External-score missingness flags | Present |
| Continuous robust clipping | 34 axes at p0.5/p99.5 (clustering matrix only) |
| Correlation pairs above 0.85 | 1 (documented) |
| Final association rules | 18: three per segment plus three portfolio-wide |
| Pure algebraic rules surviving | 0 |
| Same-source missingness identities surviving | 0 |
| Anomaly review rows / unique applicants | 5,914 / 5,914 |
| Rows permitting automatic decisions | 0 |

The single warning is the bureau_balance orphan-row issue described in Section 4.4. It is surfaced rather than suppressed.

---

## 11. Dashboard

Six sections behind a left navigation rail: Key findings, Data, Segments, Rules, Anomalies, Outcome. Sections render lazily, so the initial payload stays small and only the active section's plots are built.

**Key findings** is the landing section and carries the conclusions; the five phase sections behind it are the evidence. It presents six numbered findings, each paired with the chart that supports it: segment sizes and the profile matrix, observed default rate by segment, the cluster-versus-supervised comparison, surviving rule strength, the funnel from 356,255 applications down to a 5,914-record review queue, and the scope split. It closes on the guardrail, that no output here decides a credit outcome.

Each view pairs a chart with the interpretation a business reader needs, and the guardrails travel with the numbers rather than sitting in a footnote. The anomaly section additionally breaks the queue down by scope, global, contextual, and collective, with the reasoning from Section 7.4, because the kind of anomaly determines the response.

Run it with `python dashboard/app.py` (default `http://127.0.0.1:8050`).

---

## 11b. Decision register: why each choice was made

### 11b.1 Feature selection: correlation decides, TARGET only reports

Two formal measures run over the feature set, and they have deliberately unequal authority.

**Pearson correlation is what actually removes features.** A full correlation matrix is computed across every candidate feature, and pairs above |r| = 0.85 are treated as redundant. This drove real deletions, all traceable to the EDA:

| Removed | Reason |
|---|---|
| 28 housing columns (`*_AVG`, `*_MEDI`) | Triplicated with `*_MODE` at r > 0.99, the same measurement recorded three ways |
| `OBS_60_CNT_SOCIAL_CIRCLE` | r = 0.998 with `OBS_30` |
| `FLAG_EMP_PHONE` | r = -1.0 with `DAYS_EMPLOYED` after sentinel handling, it *is* the sentinel |
| `FLAG_MOBIL` | Near-constant (all 1s); zero variance carries zero information |
| `REGION_RATING_CLIENT` | r > 0.85 with the city variant; the finer one was kept at the time |

Thirty-seven redundant columns are dropped in total at step 7. After that, one pair above 0.85 survives into the final matrix: mean versus maximum card utilisation at r = 0.892. It was kept on purpose, because the two measure different things in credit terms, typical behaviour versus peak stress, and a customer who *averages* 55% utilisation but *peaks* at 105% is a different case from one who sits flat at 55%. Dropping either would erase that distinction to satisfy a threshold.

**Mutual information against TARGET is computed and published, but never removes anything.** `check_features.py` states this in its own docstring: it does not rewrite `features_clustering.csv`. It writes `feature_importance.csv` and stops.

That restraint is the whole point, and there are three reasons for it.

*First, it would make an unsupervised result covertly supervised.* This project's deliverable is a segmentation described as discovered from borrowing behaviour. If TARGET picked the features, the segments would be a coarse supervised model wearing unsupervised clothing, and every statement about "discovering structure in the portfolio" would be false.

*Second, it would make the Phase 4 backtest circular.* Section 8 tests whether cluster membership aligns with observed default. That test is only meaningful because TARGET never touched the clustering. Select features by their mutual information with TARGET, then measure the resulting clusters against TARGET, and you have built the answer into the question, the reported precision would partly reflect the feature selection, not the discovered structure.

*Third, it would quietly reintroduce the F1 problem.* The highest-MI features are not always the ones a lender may act on. Selecting on outcome association is exactly how proxies for protected characteristics earn their place in a model.

Correlation has none of these problems. It is computed feature-to-feature, never involves the label, and answers a different question: *are two columns saying the same thing?* Redundancy is a property of the data alone, so acting on it is safe. Discriminative power is a property of the data *and the outcome*, so acting on it is a modelling decision that this phase is not entitled to make.

MI is still worth computing and publishing. It shows the feature set is not inert, the top-ranked features are `CREDIT_TERM_MONTHS`, card utilisation mean and max, card balance, and instalment late ratio, which is a credible ordering for credit risk, and publishing it lets a reader check that claim. Note also how low the absolute values are: the strongest feature scores 0.018. That is a useful early warning that no single feature separates default cleanly, and it foreshadows the modest AUCs in Section 8 rather than contradicting them.

### 11b.2 Cluster naming: how the labels are assigned

Names are not chosen by hand after looking at the clusters, because that invites reading a story into whatever appeared. They are assigned mechanically from four business scores, each an average of the standardised cluster profile over a themed group of features:

| Score | Built from | Business meaning |
|---|---|---|
| `repayment_stress` | Instalment DPD mean/max, late and severe-late ratios, POS and card DPD | How badly this group has fallen behind |
| `card_intensity` | Card utilisation mean/max, card balance, months of card history | How central revolving credit is |
| `relationship_depth` | Previous-application count, bureau count, POS and card months | How much history exists to look at |
| `borrowing_scale` | Credit amount, annuity, credit-to-income | How large the commitment is |

Each name is then claimed by the cluster scoring highest on its theme, in a fixed order, repayment stress, then card intensity, then relationship depth, then borrowing scale, and the one cluster left over is named Thin-File / Low-Intensity.

The reason for assigning rather than describing is repeatability. K-Means cluster *numbering* permutes between runs, so any hand-written mapping from a number to a name breaks silently on the next execution. Deriving the name from the profile means the label follows the behaviour wherever it lands, which is why the same five names reappeared after the feature set changed from 49 columns to 42.

Every name is corroborated by the exported profile:

| Segment | Strongest evidence |
|---|---|
| Repayment-Stress History | Instalment DPD mean +548%, severe-late ratio +501% |
| Intensive Card User | Card utilisation max +217%, mean +203%, balance +164% |
| History-Rich Credit User | Previous applications +146%, refusals +125%, bureau enquiries +106% |
| High-Exposure Applicant | Credit amount +83%, credit-to-income +76%, annuity +70% |
| Thin-File / Low-Intensity | Credit -87%, annuity -75%, instalment count -45%, previous count -41% |

**Three weaknesses in this scheme, stated plainly.**

*The claim order is a priority, not a neutral rule.* Repayment stress is claimed first. If a cluster were both the most delinquent *and* the most card-intensive, it would be named for delinquency and the card label would pass to the runner-up. The order encodes a judgement, that arrears matter most for describing a group, and that judgement is defensible but it is a judgement.

*The last name is assigned by elimination.* Thin-File / Low-Intensity is whatever remains, not what evidence selected. In this run the leftover cluster genuinely is low-intensity on both dimensions the name claims, small amounts and thin history, so the label happens to be accurate. That is a fact to verify each run, not a property the method guarantees.

*Nothing measures how well a name fits.* A cluster scoring marginally highest on card intensity receives the same confident label as one scoring 217% above average. The profile table is the only place a reader can see the difference, which is why it is exported and shown on the dashboard.

The names themselves are deliberately descriptive of portfolio geometry rather than of customers. "Repayment-Stress History" states what the records show. It is not a character judgement, and Section 8 shows that 88% of that segment kept paying.

### 11b.3 Everything else, in one place

| Decision | Choice | Why | Where it is argued |
|---|---|---|---|
| Unit of analysis | Applicant (`SK_ID_CURR`) | The decision unit is the application | Section 2.1 |
| Discovery population | Train + test combined | Full unlabelled portfolio; transductive by design | Section 3 |
| Raw amounts vs ratios | Ratios for comparison, amounts preserved | Amounts are not comparable across incomes | Section 2.2 |
| Skew handling | Log transform on positive amounts | Prevents large amounts dominating Euclidean distance | Section 4.3 |
| Extreme values (clustering) | Clip at p0.5 / p99.5, 34 axes | Stops a few files capturing centroids; ARI 0.73 -> ~0.99 | Section 4.3 |
| Extreme values (anomaly) | No clipping, separate matrix | A truncated axis cannot contain an outlier | Section 1b F2 |
| Missing history | Flags plus counts, never zero-filled as behaviour | Absence is uncertainty, not clean conduct | Section 2.4 |
| Missing external score | Median-impute for maths, flag separately, show source value in review | Distinguish unavailable from average | Section 2.5 |
| Categorical encoding | Ordinal or frequency, no one-hot | One-hot forces all category pairs equidistant and inflates dimensionality | Section 11b.1 note |
| Protected attributes | Excluded from clustering, retained for profiling | Governance consistency; cost measured at <2% membership shift | Section 1b F1 |
| Dimensionality | 10 principal components (63.28%) | Labels stable to ARI >= 0.973 against the full space | Section 5.1 |
| Segment count | K = 5 | K = 3 wins on silhouette but puts 80.69% in one blob | Section 5.2 |
| Naming | Derived from four business scores | Cluster numbering permutes between runs | Section 11b.2 |
| Rule vocabulary | No cluster items | Otherwise rules restate Phase 2 | Section 1b F3 |
| Rule rejection | Algebraic, same-source, schema-induced | Filters test independence, not surface form | Section 6.2, Section 6.4 |
| Anomaly consensus | 3+ detectors, >=50% available | Different assumptions must agree | Section 7.1 |
| Anomaly second route | Any axis >= 10 SD | Consensus structurally misses single-axis extremes | Section 1b F4 |
| Backtest threshold | 1.10x uplift, pre-registered | Not re-tuned after seeing results | Section 8.3 |
| Outcome scope | Train IDs only | Test has no TARGET | Section 3, Section 8.1 |

---

## 12. Limitations and what a prediction project would require

Known limits:

- The extract lacks product, market, and calendar strata needed for a complete Simpson's-paradox test.
- Home Credit's applicant-selection mechanism is unknown, so nothing here generalises to the wider consumer population.
- Association rules are exploratory, without a multiplicity-adjusted external holdout.
- The rule-rejection filter catches same-table missingness identities but not missingness propagating along a parent-child key, which inflates the lift of thin-file availability rules (Section 6.3). Extending the filter to walk the schema's foreign keys is the obvious next fix.
- No intervention data exist, so no causal claim is supportable.
- Aggregation to applicant grain removes event ordering, cure status, and dispute detail that underwriting genuinely needs.

If the objective changed to applicant-level default prediction, the next workflow would need: an out-of-time train/validation/test design, calibrated probabilities, cost-sensitive thresholds tied to actual loss and review economics, stability and drift monitoring, proxy and disparate-impact testing, reason-code governance for adverse-action notices, and documented human override. Cluster membership could serve as one candidate feature; it should never be the prediction.

---

## 13. Reproducibility

From the project root:

```powershell
python src/run_pipeline.py
python scripts/execute_notebook.py notebooks/exploratory_data_analysis.ipynb --timeout 900
python scripts/execute_notebook.py notebooks/phase2_clustering.ipynb --timeout 1200
python scripts/execute_notebook.py notebooks/phase3_association.ipynb --timeout 1200
python scripts/execute_notebook.py notebooks/phase4_anomaly.ipynb --timeout 1800
python scripts/validate_end_to_end.py
python dashboard/app.py
```

Order matters: Phase 3 and Phase 4 assert against stale artefacts and fail hard rather than silently mixing runs.

Cluster *numbering* permutes between runs even though the K-Means seed is fixed, because centroid initialisation order is not stable. Every downstream consumer reads `cluster_names.csv` and matches segments by **name**, never by integer ID. Any new analysis must do the same.

---

## 14. Final judgment

The workflow is sound for its stated purpose. It produces stable, interpretable portfolio segments; denominator-safe association patterns with algebraic and missingness artefacts removed; and a two-route, evidence-backed anomaly queue of 5,914 records that no automated process may act on.

It also produces a clear negative result: cluster membership is too coarse for applicant-level default decisions, capped at 11.87% precision, while an objective-matched model reaches 17.67% at the same review capacity.

That boundary is the most useful finding in the project. It tells the business exactly which decisions this analysis can support, portfolio strategy, segment-specific review design, monitoring, and queue prioritisation, and which it cannot.

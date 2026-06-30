# Home Credit Default Risk: Knowledge Discovery Report

A single written report covering the whole project, from raw data to business recommendations. The notebooks and the pipeline produce the tables, plots, and the interactive dashboard; this document is the narrative that ties them together. It is written by hand, not generated from any cell.

The dataset is the Home Credit Default Risk data from Kaggle. The work follows the KDD process across five phases. The goal is discovery and interpretation, not a prediction score: we want to understand who these customers are, how they cluster, what patterns connect their attributes, and which records deserve a closer look.

One ground rule shapes everything below. This is an unsupervised study, so the default label is never used to build the segments, the rules, or the anomaly scores. We only open the label at the very end, to check whether the structure we found lines up with real risk. Because the algorithms never saw it, that check is honest evidence rather than circular reasoning.

All applications are used: 307,511 from the training file and 48,744 from the test file, 356,255 in total. Since there is no prediction target here, combining them is correct and gives the clustering more data to work with.

---

## Phase 1: Data understanding and preprocessing

### What the raw data looked like

Before changing anything we read the data closely. A few conditions stood out, and each one drove a specific preprocessing decision rather than a reflex.

A sentinel value hides in employment length. `DAYS_EMPLOYED` carries the value 365243, which is exactly 1000 years in days, for 18 percent of applicants. Every one of them is a pensioner or unemployed: employment length simply does not apply, so the data uses a placeholder. Left as a number it would wreck every distance calculation, so we flag it and set it to missing. Its own default rate, 5.4 percent against 8.7 percent for everyone else, confirms it marks a real state.

Income is extremely skewed. The median is around 147 thousand, but the maximum is about 795 times that. In a distance-based method a handful of extreme earners would swamp everyone else, so income is capped at the 99th percentile and then log-transformed. The same log transform goes on the other right-skewed money columns (credit, annuity, goods price).

Missing values are rarely just missing. A blank `OWN_CAR_AGE` means the applicant has no car. A blank `EXT_SOURCE_1`, missing for 56 percent of rows, usually means the credit bureau could not score them, which is itself a sign of a thin file and a risk signal. So before filling anything we create flags (no car, no housing data, no external score 1) that preserve the fact that a value was absent.

Several columns are near-duplicates. Every building measurement is reported three ways (average, mode, median) at correlation above 0.99, so keeping all three would triple the weight of building attributes. We keep one version and drop the rest. That leaves 47 clean features.

### How missing values were handled, by reason

The imputation matched the kind of absence rather than using one rule for all. Structural absence (no car, no apartment record) becomes zero, because zero means "none". Random gaps in numeric fields get the median. `OCCUPATION_TYPE` gets the most common occupation within the same income type, which is more informative than a global mode. Relational-table aggregates that are empty become zero, because no record means no activity. And `ORGANIZATION_TYPE` of "XNA", which coincides with the pensioner group, becomes a legitimate "Unknown" category rather than being discarded.

One honest caveat: filling the median into the 56 percent of rows that lack `EXT_SOURCE_1` piles most of them onto one value, which creates a slightly artificial dense plane for clustering. We keep it because the missingness flag separates that group and the median is neutral, and because dropping the feature would throw away the strongest single predictor for the 44 percent who do have it. It is a deliberate compromise.

### Encoding categoricals for a distance-based method

This is the choice that matters most for clustering, and it is where the project corrected an earlier mistake. The three categorical variables (education, income type, organization type) were originally one-hot encoded, which produced about 21 sparse binary columns.

One-hot encoding hurts Euclidean distance twice. It adds many sparse axes that together outweigh a single genuine feature, so "which sector you work in" quietly beats "how heavy your repayment burden is". And it forces every category to sit the same distance from every other, even when some are clearly more alike. "Higher education" is closer to "Incomplete higher" than to "Lower secondary", and one-hot throws that fact away.

So we match the encoding to the variable. Education becomes a single ordinal integer from 0 to 4, because it is a real ladder; the EDA even shows a clean gradient between education level and loan size. Income type and organization type are nominal with no order, so each becomes one frequency-encoded column: we replace the category with how common it is, collapsing the variable into a single "mainstream to niche" axis. Pensioners stay separately flagged, so this does not bring back the perfect collinearity that one-hot produced (where the sentinel flag, the "Unknown" organization dummy, and the "Pensioner" income dummy were all the same column).

The result is a tighter, cleaner space: 47 features instead of 65, only one remaining correlated pair above 0.85, and no redundant axes. A smaller space with fewer noise dimensions is a better space for distance.

### Feature selection: correlation and entropy

The project brief asks for feature selection by both correlation and entropy, and both are present. The correlation audit lists the pairs above 0.85 and removes the perfectly collinear ones. The entropy side computes mutual information of each feature against the default label, which catches non-linear relationships that a linear correlation misses. Low mutual-information features are not dropped automatically, because clustering does not have to follow the supervised signal, but the scores serve as formal evidence that the selection used an entropy measure, not just correlation.

The pipeline runs as ten modular steps under Prefect (with a plain-Python fallback), and the output is one clean, fully numeric, standardized file, one row per applicant, ready for the mining phases.

---

## Phase 2: Segmentation via clustering

### Reducing dimensions, two spaces for two purposes

K-Means and hierarchical clustering both work on Euclidean distance, which loses meaning in high dimensions, so they run on a PCA projection. We keep 9 components, just under the required limit of 10. The number is not arbitrary: on the scree plot each component contributes a little less than the last, then drops more sharply from the ninth to the tenth, so the tenth onward adds almost nothing. Nine components hold nearly all the signal while staying compact.

DBSCAN is handled differently, because it works on density rather than variance. PCA flattens dense clumps, so DBSCAN in PCA space tended to see one large mass. UMAP maps the non-linear shape of the data while preserving local density, so tight groups stay tight and genuinely isolated applicants get pushed to the edge. DBSCAN therefore runs on a 2D UMAP embedding, and its radius is chosen automatically from the knee of the k-distance curve, the standard DBSCAN heuristic.

### Choosing the number of segments

We tried K from 2 to 10 with the elbow method and the silhouette score. The silhouette peaks at K=2, but two segments are too coarse to act on. The elbow points to K=5, and among the genuinely granular options (K of 3 or more) K=5 has the best silhouette. So K=5 is both defensible and useful.

### The five segments

The clustering is driven by behaviour, not demographics. The strongest differentiators are repayment history, loan size relative to income, and card use, not age or gender.

| Segment | Share | What sets it apart | Actual default rate |
|---|---|---|---|
| Minimal Borrower | about 36% | small loans, short terms, light burden | 8.4% |
| Ambitious Borrower | about 35% | large loans relative to income, usually new borrowers | 6.1% |
| Active Veteran | about 13% | a dense history of applications, often rejected | 9.2% |
| Troubled Borrower | about 1% | extreme repayment delays across products | 11.8% |
| Intensive Card User | about 15% | card utilisation two to three times average | 10.8% |

The portfolio default rate is 8.1 percent.

### Three methods, checked against each other

We do not lean on one algorithm. K-Means builds the main segments, then two methods with very different logic check it. Hierarchical clustering (Ward) builds the data up like a family tree; it agrees substantially with K-Means, with an adjusted Rand score of about 0.55. DBSCAN, in the UMAP space, finds about 30 dense pockets and sets aside roughly 2 percent of applicants as isolated outliers, which then flow into the anomaly phase. Three different viewpoints pointing at a similar structure is good reason to trust the five segments.

### Naming is a human job

The algorithm only finds the grouping. A human reads the top differentiating features of each cluster and gives it a business name, a risk level, and a recommendation. Those names are saved to an artefact so every later phase and the dashboard read them, rather than hard-coding a numbering that shifts between runs.

---

## Phase 3: Association rule mining

### Turning numbers into categories

Association rules work on categories, so the continuous features are binned with quantile cuts, which keep each bin a similar size and avoid empty bins. Simple dimensions get three bins (low, medium, high); income gets four. Each applicant's segment is added as one more item, so rules can connect behaviour to segment membership.

### Three algorithms, one answer

Apriori, FP-Growth, and ECLAT all run on the same data. They work in completely different ways, and they find the same 1,204 rules. When three different methods agree, a rule is almost certainly real and not an artefact of one technique. We keep rules with lift at least 1.2 and confidence at least 0.35, then drop near-duplicates (any pair overlapping more than 65 percent), and keep the strongest few per segment. That leaves 15 final rules with lift from about 1.8 to 4.6.

### What the rules say

The most useful patterns are simple to state. A small loan with a heavy repayment burden almost always means low income (confidence above 98 percent), which is the signature of a cash-poor, credit-hungry sub-population: a small loan is not automatically a safe one. Senior applicants in the Minimal segment with a heavy burden are very likely to be low income with a small loan, a profile that fits micro-credit plus financial education rather than rejection. And very high income inside the Ambitious segment goes with large loans, confirming that big loans concentrate among people who can carry them.

One rule deserves attention: the Troubled segment has an internal pattern with confidence around 99 percent, which means chronic-default behaviour has a very consistent fingerprint that can be wired into an early-warning rule.

---

## Phase 4: Anomaly and outlier detection

### Three methods, then a cross-check

Every applicant is scored by IQR, by Z-score, and by Isolation Forest, then cross-referenced with the DBSCAN noise from Phase 2. The more independent methods agree that a record is unusual, the more confident we are. Records flagged by three or four methods are "high confidence", and there are 5,359 of them.

### Two labels per anomaly

A flat list of outliers is not actionable, so each high-confidence case gets two labels.

The first follows the classic framework (Chandola et al., 2009). A global (point) anomaly is extreme against the whole population, which is what IQR and Z-score catch, often a data error or a tail-of-distribution customer; there are 3,766 of these. A contextual anomaly looks fine in general but is odd for its own segment, like heavy card use showing up in the Minimal segment; there are 1,493, and this is the kind most worth investigating as a risk signal. A collective anomaly is part of a small pocket that UMAP and DBSCAN split off from the main mass; there are 100, watched as a recurring pattern rather than a one-off.

The second label decides the action. Type A, data error (3,215 cases): a deviation more than 50 times the segment median, fixed at the data-ingest stage. Type B, rare but valid (2,005 cases): extreme yet coherent, routed to priority service rather than rejected. Type C, risk signal (139 cases): a contradictory financial combination such as low income with a large loan, sent to manual underwriting. Each case also gets a recommendation tailored to the segment it sits in, and every record carries a real applicant ID so the operations team can follow up.

---

## Phase 5: The dashboard and the central question

The dashboard (Plotly Dash) presents all of this for a non-technical reader. It reads every number from the result artefacts, so re-running the analysis keeps it in sync, and the technical column names are translated into business language throughout. It has tabs for an executive summary, the initial data condition, the segments with per-segment recommendations, the rules, and the anomalies.

The central question the project asks is: what did we discover that was not already obvious from the raw data? Three things.

First, risk is about behaviour, not loan size. The biggest borrowers, the Ambitious segment, are the safest. What separates risk is the repayment trail and card dependence, information scattered across five relational tables that only becomes visible after aggregation and clustering.

Second, one percent of the portfolio carries the densest risk, and that one percent has a consistent enough pattern to be detected early with a rule of very high confidence.

Third, statistical "strangeness" is a real, graded risk dimension. The more unusual an applicant looks to the anomaly methods, the more often they actually default, even though the methods never saw the label.

---

## Does the structure capture real risk?

This is the honesty test for the whole study. The segments and anomalies were built without the default label. Only afterwards did we open the real outcomes and measure them. If the grouping were arbitrary, every group would default near the 8.1 percent average. Instead the numbers spread out cleanly and rise in order.

By segment: Ambitious 6.1 percent, Minimal 8.4 percent, Active Veteran 9.2 percent, Intensive Card User 10.8 percent, Troubled 11.8 percent.

By anomaly level, the default rate climbs without a single exception: normal 6.9 percent, weak signal 8.7 percent, moderate 11.3 percent, high confidence 12.9 percent.

A clean, monotonic gradient from methods that never saw the label is strong evidence that the structure is real, not a statistical accident.

---

## Recommendations by segment

Minimal Borrower: a volume engine. Serve many, automate the decisions, keep costs low. Micro-credit and short-term products fit, and financial education grows them into more valuable customers over time. The profit comes from scale and efficiency, not margin per customer.

Ambitious Borrower: a growth engine, but with a seatbelt. This is where the healthiest growth sits, since the lowest default rate proves the screening already works. Push mortgages and vehicle loans, and protect the large exposures with a stress test (can they still pay if income drops 20 to 30 percent?) and with credit insurance.

Active Veteran: investigate before deciding. A dense history of rejections is a yellow flag, not a red one. Understanding why they were refused prevents two costly mistakes at once: rejecting a good customer and accepting an over-extended one. Tighten the debt-to-income check and steer toward secured products.

Troubled Borrower: protect the balance sheet. Only one percent of the portfolio but the densest concentration of loss. For new applications, decline or require collateral; for existing customers, offer restructuring before the arrears deepen. The biggest value here is using their consistent pattern as an early-warning filter on incoming applications.

Intensive Card User: relieve the pressure before it breaks. These customers live on their cards at two to three times average utilisation. They are fine while income flows, but a shock can cascade into default across products. Monitor utilisation, offer debt consolidation, and hold limit increases until utilisation falls below 70 percent.

Across all segments, the anomaly score is worth adding as an extra screening layer alongside the conventional credit score, since it tracks real default in a graded way.

---

## How to run

Install the dependencies from `requirements.txt`, then run the phases in order. Phase 1 is a pipeline script (`python src/run_pipeline.py`); Phases 2 to 4 are notebooks executed in order; Phase 5 is the dashboard (`python dashboard/app.py`, then open the local address it prints).

The cluster numbering is not deterministic between runs, so always read the segments by name from the saved naming artefact rather than by number. All random seeds are fixed at 42, so the grouping itself is stable.

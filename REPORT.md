# Home Credit Default Risk: Knowledge Discovery Report

A report covering the whole project, from raw data to business recommendations. The notebooks and the pipeline produce the tables, plots, and the interactive dashboard; this document is the narrative that ties them together.

The dataset is the Home Credit Default Risk data from Kaggle. The work follows the KDD process from end to end. The goal is discovery and interpretation, not a prediction score: we want to understand who these customers are, how they cluster, what patterns connect their attributes, and which records deserve a closer look.

One ground rule shapes everything below. This is an unsupervised study, so the default label is never used to build the segments, the rules, or the anomaly scores. We only open the label at the very end, to check whether the structure we found lines up with real risk. Because the algorithms never saw it, that check is honest evidence rather than circular reasoning.

All 356,255 applications are used: 307,511 from the training file and 48,744 from the test file. Since there is no prediction target here, combining them is correct and gives the clustering more data to work with.

---

## Data understanding and preparation

### What we found in the raw data

Before changing anything we read the data closely. A few conditions stood out, and each one drove a specific preparation decision rather than a reflex.

A placeholder value hides in the employment-length column. About 18 percent of applicants have an entry that translates to exactly one thousand years of employment. Every one of them is a pensioner or unemployed: employment length simply does not apply to them, so the data uses a stand-in figure. Left as-is it would throw off every similarity calculation, so we flagged those applicants as a separate group and treated the field as blank. Their actual default rate, 5.4 percent against 8.7 percent for everyone else, confirms that this flag marks a real and meaningful state.

Income is extremely skewed. The typical applicant earns around 147 thousand, but the highest earner brings in about 795 times that. In a method that measures similarity by distance, a handful of extreme earners would swamp everyone else and make all ordinary customers look identical to each other. So income was capped at the top one percent and then smoothed with a log transform. The same smoothing was applied to the other money columns.

Missing values are rarely just missing. A blank car-age field means the applicant has no car. A missing bureau score, absent for 56 percent of applicants, usually means the credit bureau could not score them at all, which is itself a signal of a thin financial history. So before filling anything we created flags that preserve the fact that a value was absent, because the absence is part of the story.

Several columns measure the same thing three different ways. Every building measurement is reported as an average, a mode, and a median, all correlated above 0.99. Keeping all three would give building attributes three times the weight of everything else. We kept one version and dropped the rest, ending up with 47 clean features.

### How we handled missing values

The approach matched the reason for the gap rather than using one rule for everything. When a blank genuinely means "none" (no car, no apartment record), we filled it with zero. Random gaps in numeric fields got the midpoint value for that field. Occupation type got the most common occupation among applicants in the same income bracket, which is more informative than a single global default. Credit history aggregates that were empty became zero, because no record means no activity.

One honest note: filling the midpoint into the 56 percent of rows that lack a bureau score piles most of them onto one value, which creates a slightly artificial cluster in the analysis. We kept it because the separate "no score" flag already separates that group, and dropping the feature entirely would throw away valuable information for the 44 percent who do have a score. It is a deliberate compromise, not an oversight.

### Preparing categories for a distance-based method

The three categorical fields (education, income type, and work sector) were originally turned into a long list of yes/no columns. We reversed that decision, because yes/no columns cause two problems for similarity-based grouping. They add many nearly-empty columns that quietly dominate the distance calculations, and they force every category to be exactly as different from every other as possible, even when two categories are clearly similar.

Instead, education became a single number from zero to four, because it is a genuine ladder: the data shows a clean relationship between education level and loan size. Income type and work sector, which have no natural order, each became a single "how common is this?" number. This gives a tighter, more honest picture of similarity.

The result was 47 features instead of 65, only one remaining closely-correlated pair, and no redundant columns. A smaller, cleaner space is a better space for finding real groups.

### Choosing which features to keep

The selection used two measures. A correlation check identified columns that were nearly identical to each other and removed the redundant ones. An importance measure (how much information each feature carries about which customers eventually defaulted) identified which features were genuinely useful, including non-linear relationships that a simple correlation would miss. Low-importance features were not dropped automatically, because the goal is to find natural groups rather than to predict a number, but the scores gave us a principled, documented basis for the selection.

The full preparation runs as a ten-step pipeline, and the output is one clean, standardized table, one row per applicant, ready for the grouping and pattern-finding steps.

---

## Customer segmentation

### Reducing to a workable space

K-Means and hierarchical grouping both work on distance, which loses its meaning in 47 dimensions. So they run on a compressed version of the data that keeps nine components, capturing nearly all the useful variation while staying compact. The number is not arbitrary: a scree chart shows a clear drop-off after the ninth component, so the tenth and beyond add very little.

The density-based method (DBSCAN) is handled differently. Distance-based compression flattens tight groups, so DBSCAN on that space tends to see one undifferentiated mass. Instead it runs on a two-dimensional layout that preserves the local neighbourhood structure of the data, so tight groups stay tight and genuinely isolated applicants get pushed to the edge. Its radius is chosen automatically from the data itself.

### Choosing the number of groups

We tested from two to ten groups using both an elbow chart and a separation score. The separation peaks at two groups, but two segments are too coarse for any business decision. The elbow points to five, and among the genuinely useful options (three or more groups) five has the best separation. So five is both justified by the data and actionable for the business.

### The five customer segments

The grouping is driven by financial behaviour, not demographics. The strongest differences come from repayment history, loan size relative to income, and card usage, not from age or gender.

| Segment | Share | What sets it apart | Actual default rate |
|---|---|---|---|
| Minimal Borrower | about 36% | small loans, short terms, light repayment burden | 8.4% |
| Ambitious Borrower | about 35% | large loans relative to income, usually newer borrowers | 6.1% |
| Active Veteran | about 13% | a dense history of applications, often rejected | 9.2% |
| Troubled Borrower | about 1% | severe repayment delays across every product | 11.8% |
| Intensive Card User | about 15% | card usage two to three times the average | 10.8% |

The portfolio default rate is 8.1 percent.

### Three methods, checked against each other

We did not rely on a single algorithm. K-Means builds the main segments. Ward hierarchical grouping, which builds the data up like a family tree, checked it independently and reached a similar structure (agreement score around 0.55 out of 1). The density-based method found about 30 tight pockets and set aside roughly 2 percent of applicants as isolated cases, which then went into the anomaly review. Three very different ways of looking at the data pointing at a similar structure is good reason to trust the five segments.

### Naming is a human job

The algorithm only finds the grouping. A person reads the top distinguishing features of each group and gives it a name, a risk level, and a recommendation grounded in domain knowledge. Those names are saved so every later step and the dashboard reads them, rather than relying on a numbering that can change between runs.

---

## Patterns and behaviour rules

### Turning numbers into categories

Behaviour rules work on categories, so the continuous features are binned into equal-sized groups. Simple features get three bins (low, medium, high); income gets four. Each applicant's segment is added as one more item, so rules can connect behaviour to segment membership.

### Three methods, one answer

Three well-established rule-finding algorithms all ran on the same data. They work in completely different ways and they found the same 1,204 rules. When three different methods agree, a rule is almost certainly real and not an artefact of one technique. We kept rules with a strength ratio of at least 1.2 and a reliability of at least 35 percent, then removed near-duplicates and kept the strongest few per segment. That leaves 15 final rules, with strength ratios from about 1.8 to 4.6.

### What the rules say

The most useful patterns are simple to state. A small loan with a heavy repayment burden almost always points to low income (reliability above 98 percent), which is the signature of a cash-poor customer who is credit-hungry: a small loan is not automatically a safe one. Senior applicants in the Minimal segment with a heavy burden very likely fit that same pattern, which suggests micro-credit plus financial education rather than rejection. And very high income inside the Ambitious segment goes with large loans, confirming that big loans concentrate among people who can carry them.

One rule deserves particular attention: the Troubled segment has an internal pattern with reliability around 99 percent, which means this segment's behaviour is so consistent that it can be built directly into a lending early-warning filter.

---

## Anomaly detection and investigation

### Five detectors, because unusual is not one concept

Every application is scored by five signals that each define "unusual" differently. Two read one column at a time: one is the robust view that handles the heavy tails typical of financial data, and one is the more sensitive complement. Both are openly blind to combinations, which is why three additional signals join them.

One signal is combination-aware: it measures how far a row sits from the bulk along the natural correlations of the data, so it catches an applicant whose income and loan amount are each ordinary but wrong together. An important calibration note: the standard textbook threshold for this signal would flag a third of the entire portfolio, which is a sign that the data does not follow a perfect bell curve rather than a sign that a third of applicants are unusual. The notebook demonstrates that failure, then uses the top 2.5 percent of scores instead, keeping the flag rate in the same range as the other signals.

A fourth signal uses random partitioning to isolate easy-to-separate rows quickly, with no assumption about the shape of the data, catching non-linear pockets that no single threshold can describe. The fifth is an independent density-based check from the segmentation step, computed with different machinery in a different part of the process.

A record flagged by three or more of the five is a high-confidence anomaly. There are 7,640 of them, which is 2.1 percent of the portfolio.

### Two labels per anomaly: what kind, and what to do

A flat list of unusual cases is not actionable, so each high-confidence case gets two labels.

The first classifies the type of deviation. A global anomaly is extreme against the whole population, often a data entry issue or a genuinely rare customer. There are 5,052 of these. A contextual anomaly looks fine in general but stands out sharply within its own customer group, like heavy card use in the Minimal segment. There are 2,486 of these, and they are the most valuable to investigate as risk signals. A collective anomaly is part of a small group of customers who together sit apart from the main population. There are 102, watched as a recurring pattern rather than a one-off.

The second label decides the business response. Data entry anomalies (4,429 cases): a figure is so extreme it almost certainly reflects a recording mistake; the application should be verified before a decision is made. Rare but valid cases (3,070 cases): extreme yet internally consistent, routed to appropriate handling rather than rejected. Risk signals (141 cases): a contradictory financial combination such as low income paired with a large loan, requiring manual credit review. This small group defaults at 16.8 percent, more than twice the portfolio average. Every case carries a real applicant ID so the operations team can follow up directly.

---

## The dashboard

The dashboard presents all of this for a business reader. It reads every number from the result files, so re-running the analysis keeps it in sync, and all technical column names are translated into plain language throughout. A sidebar navigates six sections: the executive summary, the initial data condition, the segments with per-segment recommendations, the behaviour rules, the anomalies with the five-detector comparison, and the methodology.

---

## Does the structure capture real risk?

This is the honesty test for the whole study. The segments and anomalies were built without the default label. Only afterwards did we open the real outcomes and measure them. If the grouping were arbitrary, every group would default near the 8.1 percent average. Instead the numbers spread out cleanly and rise in order.

By segment: Ambitious 6.1 percent, Minimal 8.4 percent, Active Veteran 9.2 percent, Intensive Card User 10.8 percent, Troubled 11.8 percent.

By anomaly level, the default rate climbs without a single exception: normal 6.9 percent, weak signal 8.5 percent, moderate 11.7 percent, high confidence 13.0 percent. The risk-signal subset inside the high tier defaults at 16.8 percent, more than twice the baseline.

A clean, consistent gradient from methods that never saw the label is strong evidence that the structure is real, not a statistical accident.

---

## Recommendations by segment

**Minimal Borrower: a volume engine.** Serve many customers, automate the decisions, keep costs low. Micro-credit and short-term products are the right fit, and financial education grows these customers into more valuable relationships over time. The profit comes from scale and efficiency, not margin per customer.

**Ambitious Borrower: a growth engine, but with a safety check.** This is where the healthiest growth sits, since the lowest default rate proves the existing screening already works well. Push mortgages and vehicle loans toward this segment, and protect the larger exposures with an income stress test (can they still pay if income drops 20 to 30 percent?) and with credit insurance.

**Active Veteran: investigate before deciding.** A dense history of rejections is a yellow flag, not a red one. Understanding why they were refused previously prevents two costly mistakes at once: turning away a good customer and accepting an over-extended one. Tighten the debt-to-income check and steer toward secured products that use their long relationship with the bank.

**Troubled Borrower: protect the balance sheet.** Only one percent of the portfolio but the densest concentration of loss. For new applications, decline or require collateral; for existing customers, offer restructuring before the arrears deepen further. The biggest value here is using their consistent behaviour pattern as an early-warning filter on incoming applications.

**Intensive Card User: relieve the pressure before it breaks.** These customers live on their cards at two to three times average usage. They manage while income flows, but an income shock can cascade into defaults across every product at once. Monitor card usage, offer debt consolidation to bring the revolving balance down, and hold limit increases until usage falls below 70 percent.

Across all segments, the anomaly score is worth adding as an extra screening layer alongside the conventional credit score, since it tracks real default in a graded and proven way.

---

## How to run

Install the dependencies from `requirements.txt`, then run the steps in order. The first step is a pipeline script; the middle steps are notebooks executed in sequence; the final step is the dashboard (`python dashboard/app.py`, then open the local address it prints).

The cluster numbering is not fixed between runs, so always read the segments by name from the saved naming file rather than by number. All random seeds are fixed at 42, so the groupings themselves are stable.

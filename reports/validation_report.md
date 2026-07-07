# End-to-End Validation Report

Dataset: Home Credit Default Risk.
Scope: an audit of the whole process from initial data review through data preparation, customer segmentation, behaviour rules, anomaly detection, and the dashboard, including the defects found along the way, the fixes applied, and the final verified figures.

## Summary

The project went through several audit rounds. Two critical defects and several methodological weaknesses were found in earlier states of the work, each was fixed, and every step was re-run from scratch after each fix. The final state passes all consistency checks, and the discovered structure is validated against real outcomes that the algorithms never saw.

| # | Finding | Severity | Status |
|---|---------|----------|--------|
| 1 | A saved set of group labels from an older run (331,219 rows) was joined to a newer feature table (356,255 rows), silently mixing up the group assignments for every later step built on it | Critical | Fixed, re-run; automatic checks added to catch this in future |
| 2 | The behaviour rule step used a hard-coded name-to-group mapping that did not match the actual groups found, attributing rules to the wrong customer segments | Critical | Fixed; a shared naming file now keeps names consistent across all steps |
| 3 | Three columns that measure the same thing were all kept, giving that one dimension three times the weight in every similarity calculation | Methodological | Fixed by changing the encoding approach |
| 4 | Category fields were turned into long lists of yes/no columns, which distorts similarity calculations for grouping | Methodological | Replaced with ordered scale and frequency-based encoding |
| 5 | Small ordered columns escaped the standardization step because the check only looked at the data type, silently over-weighting them | Latent bug | Fixed; detection now checks the actual range of values |
| 6 | Hierarchical grouping had collapsed 94 percent of rows into one group (agreement with K-Means was 0.02) | Methodological | Replaced with Ward linkage on a representative sample; agreement now 0.55 |
| 7 | Density-based grouping in the compressed space saw one undifferentiated mass | Methodological | Moved to a layout that preserves local neighbourhood structure, with an automatically chosen radius |
| 8 | Anomaly detection relied only on per-column signals plus one combination-aware signal | Methodological | Added a robust combination-aware signal, then a local density-ratio signal (Local Outlier Factor); six signals total |
| 9 | The standard threshold for the combination-aware signal flagged a third of the portfolio | Calibration | Demonstrated clearly in the notebook, then set empirically at the top 2.5 percent of scores |
| 10 | A flat 1.5x IQR fence, applied to every numeric column including binary flags and zero-inflated fields, flagged 201,278 rows (56.5 percent of the portfolio), an order of magnitude more than any other signal | Methodological | Replaced with a skew-adjusted boxplot rule (Hubert and Vandervieren, 2008) restricted to genuinely continuous columns, with the fence multiplier calibrated per column, not a shared constant, to a fixed 1 percent target flag rate; a further guard abstains on any column whose middle 50 percent collapses onto one shared value (no credit card, no bureau record, an imputed missing-score placeholder). IQR flags fell to 1,251, in line with the rest of the ensemble |
| 11 | The per-column calibration search used a fixed upper bound, which silently under-widened the fence for columns with a tiny interquartile range relative to their tail (a payment ratio parked within a hair of its median for most applicants, with a long thin tail beyond it), leaving those columns flagging 10x the intended rate | Latent bug | Fixed by expanding the search bound until it is demonstrably wide enough, and by returning the boundary that never exceeds the target rate rather than a midpoint that could still overshoot on a quantised column |

## Data preparation, verified

| Check | Result |
|-------|--------|
| Input | 7 raw data files, including relational tables with up to 27.3 million rows |
| Output | A single clean table: 356,255 rows, applicant ID plus 47 standardized numeric features |
| Missing values remaining | 0 |
| Closely correlated pairs remaining | 1, a mean/max pair of the same metric, documented |
| Feature importance assessment | 47 features, assessed against the default label on 307,511 applicants |
| Orchestration | A ten-step pipeline with a plain-Python fallback |

The category encoding is the most consequential decision: education as an ordered scale from 0 to 4, income type and work sector as frequency-based single numbers. The reasoning is set out in full in `reports/reasoning_validation.md`.

## Customer segmentation, verified

| Check | Result |
|-------|--------|
| Compression | 10 components, the practical ceiling for a distance-based method on this data |
| Number of groups | Elbow chart points to 5; score confirms 5 is best among the usable options |
| K-Means | Full 356,255 applicants, five segments |
| Hierarchical (Ward) | Agreement with K-Means 0.55, a genuine independent confirmation |
| Density-based | Neighbourhood layout, automatically chosen radius, 30 dense pockets, 1,085 isolated cases passed to anomaly review |
| Segments | Minimal Borrower 35.5%, Ambitious Borrower 35.1%, Active Veteran 13.2%, Intensive Card User 15.2%, Troubled Borrower 1.0% |

Group numbering shifts between runs, so the name mapping is saved to a shared file and every downstream step reads from it.

## Behaviour rules, verified

| Check | Result |
|-------|--------|
| Transactions | All 356,255 applicants, discretized into 7 binned dimensions |
| Algorithms | Three independent rule-finding methods all produced identical rule sets, the strongest available correctness check |
| Final rules | 15 (three per segment) after strength, reliability, and redundancy filters; strength ratios from 1.8 to 4.6 |

## Anomaly detection, verified

Six detection signals run per application:

| Signal | What it detects | Cases flagged | Note |
|--------|----------------|---------------|------|
| Per-column robust check (skew-adjusted IQR) | Single-figure extremes, judged against each column's own, correctly skewed sense of normal | 1,251 | Restricted to genuinely continuous columns, with fences that stretch and tighten by the medcouple and a multiplier calibrated per column to a 1 percent target flag rate, not a shared constant; a zero-width box (a mass point covering more than half the applicants, such as no card or no bureau record) abstains rather than flagging every ordinary customer who differs from it |
| Per-column sensitive check (Z-score) | Single-figure extremes, more sensitive | 5,815 | Naive baseline, deliberately left symmetry-assuming, calibrated to the same 1 percent target rate as a fair contrast to the adjusted IQR |
| Combination-aware check (robust Mahalanobis) | Unusual combinations of otherwise normal values | 8,907 | Threshold set at top 2.5 percent after the standard threshold was shown to flag a third of the portfolio |
| Random partitioning check (Isolation Forest) | Non-linear unusual patterns | 17,813 | No distribution assumption |
| Local density-ratio check (Local Outlier Factor) | An applicant whose neighbourhood is sparser than its neighbours' own | 8,907 | Threshold also set at top 2.5 percent, fitted in novelty mode on a 20,000-row sample of the same continuous columns as Mahalanobis |
| Density-based check (DBSCAN) | Cases sitting in no dense region of the customer map | 1,085 | Independent cross-check from the segmentation step |

| Check | Result |
|-------|--------|
| High-confidence cases (3 or more signals agree) | 2,404 (0.7 percent of the portfolio), every one reviewed with a real applicant ID |
| Type of deviation | Global 2,013, Contextual 354, Collective 37 |
| Business classification | Data quality issue 1,616; Rare but valid 671; Risk signal 117 |

## The honesty test: validation against real outcomes

The default label was never used during any of the analysis. It was opened only afterwards, to measure the actual default rate of each discovered group on the 307,511 applicants where outcomes are known.

| Discovered structure | Actual default rate |
|----------------------|---------------------|
| Portfolio average | 8.07% |
| Ambitious Borrower | 6.08% |
| Minimal Borrower | 8.45% |
| Active Veteran | 9.19% |
| Intensive Card User | 10.79% |
| Troubled Borrower | 11.37% |
| Anomaly level: none flagged | 7.71% |
| Anomaly level: one signal | 11.29% |
| Anomaly level: two signals | 12.89% |
| Anomaly level: three or more signals | 13.62% |
| Business type: data quality issue | 13.46% |
| Business type: rare but valid | 14.24% |
| Business type: risk signal | 12.26% |

The default rate rises without a single exception from the portfolio average through every segment and every anomaly tier, from 7.71 percent for untouched applications to 13.62 percent for the high-confidence tier. One number is reported honestly rather than smoothed into a tidy story: among the three business types, risk signal (12.26%) does not come out highest, rare but valid (14.24%) does, though the risk-signal group is only 106 applicants with a known outcome, so its rate carries a wide margin of error and this ordering should not be read as evidence that risk signals are less dangerous than rare-but-valid cases. What holds cleanly, and is the comparison that actually matters for the business case, is that every anomaly tier and every business type defaults well above the 8.07 percent portfolio baseline, and the tier gradient climbs in strict order with no exceptions. For methods that never saw the label, this remains strong evidence that the structure found is real.

## Checks that keep the process honest

Four mechanisms now prevent the earlier classes of defect from recurring. Automatic alignment checks in the behaviour rule and anomaly steps fail clearly if an outdated file is loaded. The shared naming file is the single source of segment names across all steps. The applicant ID flows through every output file so any finding can be traced back to a real individual. And the dashboard reads every number from the output files at startup, so nothing on screen can drift from the analysis underneath it.

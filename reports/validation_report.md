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
| 8 | Anomaly detection relied only on per-column signals plus one combination-aware signal | Methodological | Added a robust combination-aware signal; five signals total |
| 9 | The standard threshold for the combination-aware signal flagged a third of the portfolio | Calibration | Demonstrated clearly in the notebook, then set empirically at the top 2.5 percent of scores |

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
| Compression | 9 components, chosen at the point where adding more stops helping |
| Number of groups | Elbow chart points to 5; score confirms 5 is best among the usable options |
| K-Means | Full 356,255 applicants, five segments |
| Hierarchical (Ward) | Agreement with K-Means 0.55, a genuine independent confirmation |
| Density-based | Neighbourhood layout, automatically chosen radius, 30 dense pockets, 1,085 isolated cases passed to anomaly review |
| Segments | Minimal Borrower 35.4%, Ambitious Borrower 35.1%, Active Veteran 13.2%, Intensive Card User 15.2%, Troubled Borrower 1.1% |

Group numbering shifts between runs, so the name mapping is saved to a shared file and every downstream step reads from it.

## Behaviour rules, verified

| Check | Result |
|-------|--------|
| Transactions | All 356,255 applicants, discretized into 7 binned dimensions |
| Algorithms | Three independent rule-finding methods all produced identical rule sets, the strongest available correctness check |
| Final rules | 15 (three per segment) after strength, reliability, and redundancy filters; strength ratios from 1.8 to 4.6 |

## Anomaly detection, verified

Five detection signals run per application:

| Signal | What it detects | Cases flagged | Note |
|--------|----------------|---------------|------|
| Per-column robust check | Single-figure extremes, robust to heavy tails | 201,278 | Intentionally broad; tightened by the agreement requirement |
| Per-column sensitive check | Single-figure extremes, more sensitive | 8,822 | Complement to the robust check |
| Combination-aware check (robust) | Unusual combinations of otherwise normal values | 8,907 | Threshold set at top 2.5 percent after the standard threshold was shown to flag a third of the portfolio |
| Random partitioning check | Non-linear unusual patterns | 17,813 | No distribution assumption |
| Density-based check | Cases sitting in no dense region of the customer map | 1,085 | Independent cross-check from the segmentation step |

| Check | Result |
|-------|--------|
| High-confidence cases (3 or more signals agree) | 7,640 (2.1 percent of the portfolio), every one reviewed with a real applicant ID |
| Type of deviation | Global 5,052, Contextual 2,486, Collective 102 |
| Business classification | Data entry anomaly 4,429; Rare but genuine 3,070; Risk signal 141 |

## The honesty test: validation against real outcomes

The default label was never used during any of the analysis. It was opened only afterwards, to measure the actual default rate of each discovered group on the 307,511 applicants where outcomes are known.

| Discovered structure | Actual default rate |
|----------------------|---------------------|
| Portfolio average | 8.07% |
| Ambitious Borrower | 6.07% |
| Minimal Borrower | 8.42% |
| Active Veteran | 9.24% |
| Intensive Card User | 10.79% |
| Troubled Borrower | 11.82% |
| Anomaly level: none flagged | 6.88% |
| Anomaly level: one signal | 8.53% |
| Anomaly level: two signals | 11.69% |
| Anomaly level: three or more signals | 13.02% |
| Risk-signal cases | 16.79% |

The default rate rises at every step without a single exception, and the staircase became steeper after the combination-aware signal was added and properly calibrated. For methods that never saw the label, this is strong evidence that the structure found is real.

## Checks that keep the process honest

Four mechanisms now prevent the earlier classes of defect from recurring. Automatic alignment checks in the behaviour rule and anomaly steps fail clearly if an outdated file is loaded. The shared naming file is the single source of segment names across all steps. The applicant ID flows through every output file so any finding can be traced back to a real individual. And the dashboard reads every number from the output files at startup, so nothing on screen can drift from the analysis underneath it.

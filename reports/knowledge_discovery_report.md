# Knowledge Discovery Report: Executive Brief

A business-facing summary of what the analysis found in 356,255 Home Credit applications. The full narrative, step by step, is in the project-root `REPORT.md`; this brief is the short version for a decision-maker.

One rule shaped everything: the default label was never shown to any algorithm. Segments, rules, and anomalies were all found without it, then tested against the defaults that actually happened. Everything below passed that test.

## The three findings

**The biggest borrowers are the safest.** When we grouped customers by their financial behaviour, five distinct profiles emerged. The group that borrows the most relative to income, about 35 percent of the portfolio, turns out to default the least: 6.1 percent against the 8.1 percent portfolio average. Risk does not live in the loan amount. It lives in the repayment trail and the card behaviour, information scattered across five relational tables that only becomes visible after you bring it together.

**One percent of customers carries the densest risk, and their behaviour has a clear fingerprint.** The Troubled Borrower group is 1 percent of the book but defaults at 11.4 percent, with repayment delays many times the norm across every product type. Their behaviour is so consistent that one of the patterns found in their data holds with 99 percent reliability, which makes it directly usable as an early-warning filter in the lending process.

**The more unusual an application looks, the more likely it is to default, and not every unusual application is really an outlier.** Every application was scored by six independent detectors, two that look at individual figures (using a fence that adjusts for the natural skew of financial data and is calibrated per column, not a shared flat rule) and four that look at the whole financial picture at once. Flagged applications default higher at every step, without exception: 7.7 percent when none flag, 11.3 percent at one signal, 12.9 percent at two, 13.6 percent at three or more. Of the 2,404 high-confidence cases, most (1,616) turn out to be data quality issues rather than genuine customer oddities, a deviation so extreme that it far more likely reflects a recording mistake than real behaviour; these are routed to verification, not a risk decision. The 117 applications classified as risk signals sit well above the 8.1 percent portfolio baseline; among the three business types their own ordering does not come out strictly by severity at this sample size (the risk-signal group is only 106 applicants with a known outcome), which we report plainly rather than smooth over. None of these detectors ever saw the default label.

## What we recommend

| Team | Action | Grounding |
|------|--------|-----------|
| Credit officers | Manual review for the 117 risk-signal cases; watch the low-income-paired-with-large-loan pattern closely | Findings 2 and 3 |
| Risk team | Add the anomaly agreement score and customer segment as inputs to the credit scoring process | The consistent staircase in Finding 3 |
| Operations | Verify data on the 1,616 cases where a figure looks like a recording mistake before making a decision; these are data quality issues, not real customer outliers | Finding 3 |
| Product team | Micro-credit plus financial education for senior Minimal Borrowers; priority routing for the 671 rare-but-valid cases | Findings 1 and 2 |
| Growth team | Shift mortgage and vehicle-loan growth toward the Ambitious segment, protected by an income stress test | Finding 1 |
| Collections | Prioritise monitoring of Troubled Borrowers and Intensive Card Users, who default at 10.8 to 11.4 percent | Finding 1 |

## Where to look

The interactive dashboard walks through every finding with plain-language explanations: the initial data condition, the customer segments with per-segment recommendations, the 15 behaviour rules as readable sentences, and the full list of flagged cases with real applicant IDs. The full written report is `REPORT.md` at the project root; the reasoning behind every methodological choice is in `reports/reasoning_validation.md`; the audit trail with all verified figures is in `reports/validation_report.md`.

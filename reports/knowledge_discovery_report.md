# Knowledge Discovery Report: Executive Brief

A business-facing summary of what the analysis found in 356,255 Home Credit applications. The full narrative, step by step, is in the project-root `REPORT.md`; this brief is the short version for a decision-maker.

One rule shaped everything: the default label was never shown to any algorithm. Segments, rules, and anomalies were all found without it, then tested against the defaults that actually happened. Everything below passed that test.

## The three findings

**The biggest borrowers are the safest.** When we grouped customers by their financial behaviour, five distinct profiles emerged. The group that borrows the most relative to income, about 35 percent of the portfolio, turns out to default the least: 6.1 percent against the 8.1 percent portfolio average. Risk does not live in the loan amount. It lives in the repayment trail and the card behaviour, information scattered across five relational tables that only becomes visible after you bring it together.

**One percent of customers carries the densest risk, and their behaviour has a clear fingerprint.** The Troubled Borrower group is 1 percent of the book but defaults at 11.8 percent, with repayment delays many times the norm across every product type. Their behaviour is so consistent that one of the patterns found in their data holds with 99 percent reliability, which makes it directly usable as an early-warning filter in the lending process.

**The more unusual an application looks, the more likely it is to default.** Every application was scored by five independent detectors, two that look at individual figures and three that look at the whole financial picture at once. The more detectors agree that an application is unusual, the higher the actual default rate turns out to be: 6.9 percent when none flag, 8.5 percent at one, 11.7 percent at two, 13.0 percent at three or more. The 141 applications classified as genuine risk signals default at 16.8 percent, more than twice the portfolio average. None of these detectors ever saw the default label.

## What we recommend

| Team | Action | Grounding |
|------|--------|-----------|
| Credit officers | Manual review for the 141 risk-signal cases; watch the low-income-paired-with-large-loan pattern closely | Findings 2 and 3 |
| Risk team | Add the anomaly agreement score and customer segment as inputs to the credit scoring process | The consistent staircase in Finding 3 |
| Operations | Verify data on the 4,429 cases where a figure looks like a recording mistake before making a decision | Finding 3 |
| Product team | Micro-credit plus financial education for senior Minimal Borrowers; priority routing for the 3,070 rare-but-genuine cases | Findings 1 and 2 |
| Growth team | Shift mortgage and vehicle-loan growth toward the Ambitious segment, protected by an income stress test | Finding 1 |
| Collections | Prioritise monitoring of Troubled Borrowers and Intensive Card Users, who default at 10.8 to 11.8 percent | Finding 1 |

## Where to look

The interactive dashboard walks through every finding with plain-language explanations: the initial data condition, the customer segments with per-segment recommendations, the 15 behaviour rules as readable sentences, and the full list of flagged cases with real applicant IDs. The full written report is `REPORT.md` at the project root; the reasoning behind every methodological choice is in `reports/reasoning_validation.md`; the audit trail with all verified figures is in `reports/validation_report.md`.

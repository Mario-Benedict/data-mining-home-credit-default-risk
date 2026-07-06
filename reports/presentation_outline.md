# 10-Minute Presentation Outline

Five members, each presenting their own area of the work. Visual support: the live dashboard or the figures in the results folders.

| Minutes | Section | Presenter | Key content |
|---------|---------|-----------|-------------|
| 0 - 1 | Opening | Insight Communicator | 356 thousand credit applications, 7 data sources, 27 million rows of repayment history. One question: what is actually hidden in all of this? |
| 1 - 2.5 | Data preparation | Data Engineer 1 | Ten preparation steps turn 7 raw files into 47 clean features. The decisions that mattered: handling the employment placeholder that affects 18 percent of the data, bringing together 5 relational data sources at the applicant level, and encoding category fields for similarity-based grouping (ordered scale and frequency-based encoding instead of yes/no columns) after a correlation check exposed a redundancy problem |
| 2.5 - 4.5 | Customer segmentation | Segmentation Specialist | Two standard charts both point to 5 groups. Three methods run: K-Means as the primary segmenter, Ward hierarchical as the independent check (agreement 0.55), and a density-based method as the noise detector. Five named customer segments. The number that stops the room: the biggest borrowers default the least |
| 4.5 - 6.5 | Behaviour rules | Pattern Analyst | Seven dimensions binned into equal-sized categories, then three independent rule-finding algorithms each find the same rule set. Fifteen final rules survive the strength, reliability, and redundancy filters. Strongest example: senior applicants with a heavy repayment burden in the Minimal Borrower group, occurring 4.6 times more often than chance. The Troubled Borrower group carries an internal rule with 99 percent reliability |
| 6.5 - 8.5 | Anomaly investigation | Data Engineer 2 | Five signals, two per-column and three combination-aware, including a robust combination signal whose standard textbook threshold visibly fails on credit data and is calibrated on the data itself. Final verdict by agreement: three or more signals. Each flagged case gets a deviation type (global, contextual, collective), a business classification (data entry error, rare but genuine, risk signal), and a segment-specific action. Closing number: default rates climb at every anomaly level, and the detectors never saw the default label |
| 8.5 - 10 | Synthesis | Insight Communicator | Three findings, five segment recommendations, a 30-second dashboard demonstration |

## Answers for the Mining Expo

### Which rule was the most surprising, and why?

"A small loan with a heavy repayment burden means low income", holding with reliability above 98 percent and covering about a tenth of the portfolio. The common assumption is that large loans are the dangerous ones. The data says the opposite twice over: the segment with the largest loans has the lowest default rate, and it is actually the small loans that hide a fragile, shock-sensitive sub-population, because their incomes are just as small as their loans.

### Which grouping method produced the most interpretable segments?

K-Means with five groups. The segments come out compact and easy to name because the features were standardized and compressed first. Ward hierarchical grouping shows a similar five-group structure, confirming it is real. The density-based method is a poor segmenter on this data (it finds one large group plus isolated fringes) but an excellent noise detector: the isolated points it identifies default well above average.

### What unusual cases were found, and what do they mean in a real banking context?

Three kinds with three different responses. First, cases where a figure was almost certainly entered incorrectly, which need to be caught and verified before any credit decision is made. Second, rare but legitimate profiles that represent a business opportunity if routed to appropriate handling instead of being automatically declined. Third, genuine risk signals where the financial details simply do not add up together, which must be reviewed individually by a credit officer. The lesson: unusual cases are not one category to be discarded; each type calls for a different response from the business.

### How do the findings compare with work in other financial domains?

The approach is the same, but the meaning of what is found depends on the domain. In credit risk, unusual cases split into three types with different business responses. In fraud detection or financial crime prevention, almost every unusual case is an investigation lead. Customer segmentation works the same way across domains too: the groups found here are credit personalities, while in a customer retention project the groups are typically customer lifecycle stages. The same analytical approach, but different knowledge comes out of it.

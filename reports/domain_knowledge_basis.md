# Domain basis for the Home Credit case

## What the data represents

The unit of analysis is a Home Credit application identified by `SK_ID_CURR`. The public TARGET marks a payment-difficulty outcome for labeled train applications. It should not be presented as a legal definition of default, fraud, or lifetime creditworthiness. The public description does not expose the lender's complete operational threshold or downstream decision policy.

The assignment asks for knowledge discovery: data preparation, segmentation, association patterns, anomaly review, and an interactive business presentation. Prediction accuracy is not the main success criterion. Outcome metrics are useful only as a boundary check on whether discovered segments contain historical signal.

## Credit-risk concepts used in the project

### Capacity and affordability

`AMT_INCOME_TOTAL`, `AMT_CREDIT`, and `AMT_ANNUITY` have different roles. Income is a stated or verified resource measure; credit is requested exposure; annuity is scheduled payment commitment. Raw amounts are hard to compare across applicants, so the project uses:

- credit-to-income as a leverage proxy;
- annuity-to-income as a repayment-burden proxy;
- estimated term from credit divided by annuity; and
- goods-price-to-credit as an exposure structure check.

These ratios are screening evidence, not policy cutoffs. A high ratio can be explainable after income verification, other obligations, household costs, collateral, and product terms are considered.

### Willingness and observed repayment behavior

Installment, POS, credit-card, and bureau histories contain lateness, delinquency, utilization, payment ratios, and exposure depth. Recency, severity, persistence, and cure status matter more than a single lifetime maximum.

The public data is aggregated, so the dashboard recommends a record review when these signals appear. It does not claim that historical delinquency causes a future default.

### Thin files and missing history

No history can mean a new borrower, a customer without a matching product record, a limited reporting footprint, or missing linkage. It is not evidence of good or bad repayment.

This principle changes several implementation choices:

- `INST_COUNT` separates no observed installment history from observed clean history.
- `FLAG_NO_BUREAU` separates no matched bureau parent from zero bureau delinquency.
- card-history and previous-application availability become explicit association-rule items.
- anomaly recommendations request permitted alternative evidence instead of assigning a risk label from absence alone.

### External scores

`EXT_SOURCE_1`, `EXT_SOURCE_2`, and `EXT_SOURCE_3` are external risk-related scores, but their construction and calibration are not public. Lower values can be treated as adverse context only at a descriptive level.

Missing external scores are flagged. Median imputation supports a complete numeric matrix, but the case-review text uses the preserved source values and never calls an imputed median an observed score.

### Revolving credit utilization

High credit-card utilization may indicate liquidity pressure, active transacting, a low limit, or timing effects. Utilization is therefore paired with balance, payment capacity, delinquency, and limit suitability. It is not a stand-alone decline rule.

### Previous refusals

A prior refusal records an earlier decision under earlier circumstances. It may reflect affordability, policy, documentation, product fit, or duplicate applications. The correct action is to reconcile the old reason with current evidence, not to treat refusal count as immutable risk.

## Time and aggregation

Most `DAYS_*` fields are offsets relative to the current application date. Values closer to zero are more recent. For `DAYS_DECISION`, the maximum is the most recent previous decision and the minimum is the earliest. The pipeline now uses that direction correctly.

Relational histories are aggregated to applicant grain with counts, means, maxima, ratios, and recency summaries. This makes clustering feasible but removes event order and within-account detail. A reviewer must return to source records for recency, cure status, disputed payments, and other case facts.

## Preprocessing rules grounded in the domain

| Data issue | Treatment | Business reason |
|---|---|---|
| `DAYS_EMPLOYED=365243` | Replace with missing and retain a sentinel flag | It is a coded state, not 1,000 years of employment |
| Positive skew in monetary values | Preserve source value, log model value | Prevent large amounts from dominating distances |
| Extreme continuous values | Clip model axis at p0.5/p99.5 | Stabilize center-based clustering without falsifying case evidence |
| Missing external score | Flag and impute for computation | Distinguish unavailable score from observed median risk |
| No linked history | Explicit availability/count flags | Do not confuse no data with zero delinquency |
| Categorical variables | Binary, ordinal, or frequency encoding | Avoid a very wide sparse matrix for distance-based mining |
| Train and test | Combine with source flag for discovery | Use the full unlabeled portfolio while preserving the scoring boundary |

## How to interpret the segments

The five labels are neutral summaries of dominant feature patterns:

- Intensive Card User: revolving-credit history and utilization dominate.
- Repayment-Stress History: installment and POS lateness dominate.
- Thin-File / Low-Intensity: product exposure and observed history are limited.
- High-Exposure Applicant: requested credit, leverage, and annuity burden are larger.
- History-Rich Credit User: internal and external history depth is larger.

A segment is a cohort description. It does not say that every member has the same risk, needs the same decision, or caused the segment's observed outcome rate. This is the ecological-fallacy guardrail used throughout the dashboard.

## How to interpret association rules

Support is the share of the stated population containing the full rule. Confidence is the consequent rate among rows with the antecedent. Lift compares that confidence with the consequent's baseline in the same population.

A high lift can arise from rare categories or from how features were constructed. The project therefore rejects algebraic identities and same-source missingness identities, reports support counts, labels the denominator, and keeps data-availability patterns separate from repayment behavior.

Association is not causation. A rule suggests a portfolio pattern worth monitoring or investigating. It does not establish a credit policy.

## How to interpret anomalies

An anomaly is statistically unusual relative to the modeled portfolio. It can be:

- a data inconsistency;
- a rare but legitimate applicant profile; or
- a record with affordability or repayment evidence that needs review.

Detector agreement increases confidence that a row is unusual. It does not estimate probability of default. The review queue preserves source values, lists the evidence, and prohibits automatic decisions.

## Outcome use and the base rate

Only `application_train.csv` IDs have TARGET. Test IDs must not enter precision or recall calculations.

The train base rate is 8.07%. Cluster outcome alignment has 10.83% precision, so the flagged cohort is riskier than the portfolio average but still contains mostly observed non-defaults. The highest complete segment rate is 11.91%, which places a natural ceiling on broad segment precision.

The separate logistic diagnostic reaches 21.75% precision at the same review capacity because it is trained for outcome separation. It remains a diagnostic. Deployment would require an out-of-time test, calibration, policy cost analysis, fairness review, model governance, and monitoring.

## Fairness and customer treatment

Gender is excluded from clustering. The supervised diagnostic also excludes direct age, education, income-type frequency, organization-type frequency, and region-rating proxies. These exclusions reduce obvious risk, but they do not prove fairness; other financial variables may still act as proxies.

No unsupervised output authorizes rejection, pricing, limit reduction, or adverse action. The dashboard recommends evidence checks, affordability review, hardship routing under policy, or ordinary underwriting. Customer-impact decisions need approved policy and human accountability.

## Claims the project does not make

The project does not claim that:

- DBSCAN noise is fraud or default;
- anomaly consensus is calibrated probability;
- a cluster average applies to every member;
- a high-lift rule is causal;
- train/test combined discovery is deployment validation; or
- the logistic reference is production ready.

These boundaries are part of the business interpretation, not footnotes.

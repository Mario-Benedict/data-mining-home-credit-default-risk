# Live knowledge-discovery companion

## What the analysis found

The portfolio contains five stable application profiles. The segmentation is useful because the profiles call for different review questions, not because one cluster is "good" and another is "bad."

| Segment | Applications | Dominant pattern | Practical question |
|---|---:|---|---|
| Intensive Card User | 54,535 | High revolving-credit history and utilization | Are balances, payments, and limits sustainable now? |
| Repayment-Stress History | 7,637 | Much higher installment and POS lateness | How recent and severe were arrears, and were they cured? |
| Thin-File / Low-Intensity | 121,820 | Lower exposure and limited observed history | Is evidence absent, or is the applicant genuinely low activity? |
| High-Exposure Applicant | 119,937 | Largest requested credit, leverage, and burden | Does verified income support the exposure under stress? |
| History-Rich Credit User | 52,326 | Deeper bureau and previous-application history | Which historical concerns still matter under current obligations? |

The K=5 partition is highly stable across seeds. It is not the best silhouette solution; K=3 is. Five segments are retained because they add usable business resolution without creating empty or tiny artifacts.

## Patterns worth discussing

The final association table has 15 denominator-labeled rules. A few examples:

- High card utilization strongly identifies the Intensive Card User segment. Review balance, payment capacity, and limit suitability before exposure changes.
- Within the Repayment-Stress segment, serious lateness co-occurs with lower leverage and burden in many records. That does not make the lateness harmless; it shifts the review toward recency, severity, and cure status rather than leverage alone.
- Repeated previous refusals co-occur with deeper previous-application history. Reconcile the old reasons with current evidence.
- In thin-file and high-exposure segments, missing card, installment, and previous histories co-occur. These are data-availability patterns, not clean-repayment findings.

The selector rejects arithmetic identities and deterministic missingness relationships. Support counts and metric scope are visible on the dashboard.

## Anomaly review queue

Detector consensus routes 3,758 applications for human review, 1.05% of the portfolio. Most are affordability or repayment reviews:

| Segment | Affordability / repayment | Data consistency | Rare but plausible |
|---|---:|---:|---:|
| Intensive Card User | 491 | 18 | 1 |
| Repayment-Stress History | 2,768 | 11 | 0 |
| Thin-File / Low-Intensity | 46 | 2 | 3 |
| High-Exposure Applicant | 81 | 7 | 0 |
| History-Rich Credit User | 297 | 26 | 7 |

The leading evidence drivers are current delinquency, material installment lateness, persistent underpayment, repeated severe lateness, card utilization, and high credit-to-income leverage. The table shows the observed values and source basis for each record.

No row authorizes an automatic decision. Statistical rarity can also be a data problem or a legitimate unusual profile.

## Why prediction looked weak

At a 17.38% review share, cluster outcome alignment produces:

| Metric | Cluster alignment | Supervised diagnostic |
|---|---:|---:|
| Precision | 10.83% | 21.75% |
| Recall | 23.33% | 46.84% |
| Lift | 1.34x | 2.69x |
| Average precision | 9.53% | 23.33% |
| ROC AUC | 0.557 | 0.751 |

The comparison uses train IDs only and five out-of-fold splits. It does not score test TARGET because test TARGET does not exist.

Cluster scores are broad cohort averages. The highest complete-segment default rate is 11.91%, which limits achievable precision. The logistic diagnostic uses applicant features and is trained against outcomes, so it separates outcomes better.

This result supports two decisions:

1. Keep clustering for portfolio segmentation, rule context, and review design.
2. Do not use cluster membership as the applicant default model.

## Claims to avoid during the presentation

- "Repayment-Stress members will default." Most did not.
- "High-Exposure members are safe." Their lower observed cohort rate does not override applicant evidence.
- "DBSCAN found fraud." It found sampled density noise.
- "Three detectors mean high default probability." They mean agreement on unusualness.
- "High lift proves causation." It describes co-occurrence in the stated denominator.
- "The logistic model is ready." It is a train-only diagnostic without time-based deployment validation.

## Recommended business use

Use the dashboard for portfolio sizing, segment-specific review prompts, rule-led monitoring, and a documented anomaly queue. If Home Credit wants automated default scoring, build a separate governed supervised workflow with temporal validation, calibration, fairness testing, reason codes, and drift monitoring.

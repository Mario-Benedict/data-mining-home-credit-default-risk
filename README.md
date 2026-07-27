# Home Credit: application portfolio discovery

This project follows the KDD process to study the Home Credit application portfolio through preprocessing, segmentation, association-rule mining, anomaly review, and an interactive dashboard.

The dataset was assigned by the course instructor in place of the options listed in the reference document; the five-phase KDD methodology is unchanged. The goal is business discovery, not applicant scoring. The portfolio is analyzed as one unlabeled population of 356,255 applications. An out-of-scope outcome column present in one raw source file is removed at ingestion; no phase, finding, or chart reads it.

The full method rationale, evidence boundaries, and business interpretation are in [REPORT.md](REPORT.md).

## What we discovered that was not obvious from the raw data

Each of these began as a larger number and shrank once it was tested against the way it was built. The figures below are the ones that survived.

1. **Committed value, application volume, and review attention are three different distributions, and they are close to inverted.** Larger-Loan Affordability holds 34.62% of applications and 53.21% of recorded loan value, but only 10.00% of the targeted-review queue. One review there stands behind about 116 times more committed money than a review in the most-scrutinised segment, and it is the thinnest file in the portfolio: a median of 2 previous applications and 16 instalment records. The ranking survives removing the features that drive the queue.
2. **The strongest history-based review trigger is measuring tenure, not repayment.** Prior refusals co-occurring with instalment lateness reads as lift 1.351. Those applicants carry 1.59 times the portfolio's instalment records, and lateness is counted per instalment. Holding history depth constant moves the lift to 1.065, and two further shortlisted patterns fall below 1.0.
3. **The apparent agreement between the segmentation and the anomaly queue is one signal counted twice.** Repayment-Stress History holds 45.17% of the queue. Removing the six delinquency columns that define that segment and re-running all five detectors leaves it with 6.09%, a retained ratio of 0.135.

## Portfolio results

| Result | Value |
|---|---:|
| Application portfolio | 356,255 applications |
| Governed mining features | 41 (from 60 prepared business fields) |
| Business segments | 5 |
| K=5 seed stability / split-half stability | ARI 0.997 / 0.955 |
| K-Means vs hierarchical validation (BIRCH over all applications) | ARI 0.257, NMI 0.367 (weak; BIRCH puts 74.6% in one group) |
| Per-segment silhouette range | 0.084 to 0.222 |
| Silhouette, best feature family alone vs all 41 together | 0.845 vs 0.154 |
| Density view (DBSCAN, full portfolio) | 12,402 noise points, 3.48%, 9 pockets |
| Density agreement between the PCA space and the UMAP picture | Jaccard 0.043 |
| Selected cross-source patterns | 12 non-trivial review patterns |
| Patterns losing half their lift to exposure | 3 of 12 |
| Targeted-review queue | 6,391 applications, or 1.79% of the portfolio |
| Queue entry routes | 3,983 by detector consensus; 2,408 by an extreme single-axis value |
| Outlier typology | 4,334 point; 1,982 contextual; 75 collective in 11 groups |
| Contextual records earned by a segment-relative deviation | 1,489 of 1,982 |

Cluster names describe recurring evidence profiles, not grades of customer risk. Association patterns describe co-occurrence, not causality. Anomaly flags determine what a reviewer should verify next; they do not approve, decline, price, rank, or change a limit.

One caveat governs every segment figure above. This portfolio does not hold a single natural segmentation: card history clustered alone separates at a silhouette of 0.845 and instalment delinquency at 0.685, against 0.154 for all 41 features together. Each family cuts a different and equally strong line through the same applications, so the five segments are one defensible cut through several rather than the portfolio's structure. That is also why no hierarchical method reproduces them, and why the segments are defended on split-half stability rather than on method agreement.

## Six controls against self-confirming findings

The project runs six explicit tests that a headline number is not simply restating its own construction. Each is described in Appendix G of [REPORT.md](REPORT.md) and enforced by the validator.

| Control | Phase | What it protects against |
|---|---|---|
| Cluster tendency and null-model silhouette | 2 | Reading a silhouette against a textbook threshold, and calling one cut through several overlapping segmentations the segmentation |
| Concentration null and ceiling calibration | 2 | Reporting an amount share that any subset of that size would produce |
| Split-half stability | 2 | Reporting seed stability as if it were sample stability |
| Two-space density check | 2 | Reporting density structure that belongs to the UMAP projection |
| Exposure standardisation | 3 | Reporting relationship length as if it were repayment behaviour |
| Leave-one-family-out circularity test | 4 | Treating a segment and a queue built on the same columns as independent |

## Run the project

From the repository root:

```powershell
python src/run_pipeline.py
python scripts/execute_notebook.py notebooks/exploratory_data_analysis.ipynb --timeout 2400
python scripts/execute_notebook.py notebooks/phase2_clustering.ipynb --timeout 1800
python scripts/build_linkage_comparison.py
python scripts/build_cluster_tendency_plot.py
python scripts/execute_notebook.py notebooks/phase3_association.ipynb --timeout 2400
python scripts/execute_notebook.py notebooks/phase4_anomaly.ipynb --timeout 5400
python scripts/build_business_artifacts.py
python scripts/validate_business_findings.py
python dashboard/app.py
```

The dashboard runs at `http://127.0.0.1:8050`.

Run the phases in order. Phase 2 owns the cophenetic and cluster-tendency evidence; `build_linkage_comparison.py` and `build_cluster_tendency_plot.py` read those numbers back rather than recomputing them, so a figure and its table cannot disagree. Phase 3, Phase 4, and the final validator reject stale IDs, names, counts, and evidence instead of silently combining incompatible runs, and the validator also fails if any of the six controls above stops running.

With fixed data, code, library versions, and random states, the results are reproducible. Cluster integers remain arbitrary and may change when the data or software changes. Downstream interpretation therefore joins through the names in `cluster_names.csv`.

`src/run_pipeline.py` uses direct local execution by default. Set `HOME_CREDIT_USE_PREFECT=1` only when a compatible Prefect and FastAPI environment is available.

## Repository layout

```text
src/run_pipeline.py    Phase 1 entry point
src/domain_credit.py   domain logic and record-level review reasoning
src/pipeline/          preprocessing steps in execution order
notebooks/             EDA and Phases 2-4
scripts/               notebook runner, evidence rebuilders, final validator
results/               auditable CSV and PNG artifacts by phase
dashboard/             Plotly Dash application
datasets/              raw inputs and prepared feature tables
```

Phase 1 creates three applicant-level views because segmentation, review explanations, and anomaly detection need different treatments.

| Matrix | Treatment | Used by |
|---|---|---|
| `features_business.csv` | Readable source-scale values and audit fields | Association rules, record review, dashboard text |
| `features_clustering.csv` | Continuous values bounded at p0.5 and p99.5, then standardized | PCA, K-Means, BIRCH, DBSCAN, Ward |
| `features_anomaly.csv` | Standardized without clipping | Phase 4 anomaly detectors |

Each pipeline step consumes the applicant-level frame returned by the previous step. Historical tables are aggregated to `SK_ID_CURR` before joining so that one applicant is never multiplied by transaction-level rows.

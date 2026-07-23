# Home Credit: application portfolio discovery

This project follows the KDD process to study the Home Credit application portfolio through preprocessing, segmentation, association-rule mining, anomaly review, and an interactive dashboard.

The goal is business discovery, not applicant scoring. The portfolio is analyzed as one unlabeled population of 356,255 applications. An out-of-scope outcome column present in one raw source file is removed at ingestion; no phase, finding, or chart reads it.

The full method rationale, evidence boundaries, and business interpretation are in [REPORT.md](REPORT.md).

## Three findings that matter

1. Repayment-Stress History and Historical Card-Use Intensity contain 17.44% of applications but account for 69.28% of the targeted-review queue. They need separate specialist workflows rather than one broad risk label.
2. Larger-Loan Affordability contains 34.36% of applications yet carries 52.98% of the portfolio's recorded loan amounts and 46.63% of its scheduled payment amounts. Amount concentration and application volume are different control questions, and affordability verification matters most exactly where history looks routine.
3. Prior refusals and late repayment often appear together. Among 36,868 applications with at least three prior refusals, 60.08% also have recorded instalment lateness, compared with 44.47% across the portfolio. This is a review prompt, not an automatic decline reason.

## Portfolio results

| Result | Value |
|---|---:|
| Application portfolio | 356,255 applications |
| Governed clustering features | 42 |
| Business segments | 5 |
| K=5 seed stability | ARI 0.9950-0.9965; mean 0.9955 |
| Selected cross-source patterns | 12 non-trivial review patterns |
| Targeted-review queue | 6,404 applications, or 1.80% of the portfolio |
| Queue entry routes | 3,980 by detector consensus; 2,424 by an extreme single-axis value |
| Outlier typology | 4,334 point; 2,056 contextual; 14 collective (sampled) |

Cluster names describe recurring evidence profiles, not grades of customer risk. Association patterns describe co-occurrence, not causality. Anomaly flags determine what a reviewer should verify next; they do not approve, decline, price, rank, or change a limit.

## Run the project

From the repository root:

```powershell
python src/run_pipeline.py
python scripts/execute_notebook.py notebooks/exploratory_data_analysis.ipynb --timeout 900
python scripts/execute_notebook.py notebooks/phase2_clustering.ipynb --timeout 1200
python scripts/build_linkage_comparison.py
python scripts/execute_notebook.py notebooks/phase3_association.ipynb --timeout 1200
python scripts/execute_notebook.py notebooks/phase4_anomaly.ipynb --timeout 3600
python scripts/build_business_artifacts.py
python scripts/validate_business_findings.py
python dashboard/app.py
```

The dashboard runs at `http://127.0.0.1:8050`.

Run the phases in order. Phase 3, Phase 4, and the final validator reject stale IDs, names, counts, and evidence instead of silently combining incompatible runs.

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
| `features_clustering.csv` | Continuous values bounded at p0.5 and p99.5, then standardized | PCA, K-Means, DBSCAN, Ward |
| `features_anomaly.csv` | Standardized without clipping | Phase 4 anomaly detectors |

Each pipeline step consumes the applicant-level frame returned by the previous step. Historical tables are aggregated to `SK_ID_CURR` before joining so that one applicant is never multiplied by transaction-level rows.

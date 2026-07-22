# Home Credit Default Risk: Knowledge Discovery

KDD-process analysis of the Home Credit Default Risk portfolio: preprocessing, segmentation, association-rule mining, anomaly review, and an interactive dashboard.

The goal is portfolio discovery and business interpretation. Default prediction appears only as a train-only diagnostic, and the analysis is explicit that cluster membership is not accurate enough for applicant-level credit decisions.

**Full write-up, domain reasoning, every method decision, validation evidence, and business interpretation, is in [REPORT.md](REPORT.md).**

## Headline results

| Check | Result |
|---|---:|
| Combined applications | 356,255 |
| Train rows used for outcome metrics | 307,511 |
| Test rows used for outcome metrics | 0 |
| Clustering features | 42 (protected/proxy attributes excluded) |
| K-Means segments | 5 |
| K=5 seed stability (ARI) | 0.9936-0.9986 |
| Final association rules | 18 (3 per segment + 3 portfolio-wide) |
| Anomaly review queue | 5,914 (1.66%): 2,491 by detector consensus + 3,423 implausible single values |
| Cluster alignment precision / recall | 10.05% / 35.51% |
| Supervised diagnostic precision / recall | 17.67% / 62.43% |
| End-to-end verification | 70 pass, 1 warning, 0 fail |

The low cluster precision is expected rather than a defect. Clustering groups applications that look alike; it does not optimise `TARGET`. At a matched 28.52% review capacity an outcome-trained model improves both precision and recall by 1.76x. Use the segmentation for portfolio strategy and review design, not for decline decisions.

## Run it

From the repository root:

```powershell
python src/run_pipeline.py
python scripts/execute_notebook.py notebooks/exploratory_data_analysis.ipynb --timeout 900
python scripts/execute_notebook.py notebooks/phase2_clustering.ipynb --timeout 1200
python scripts/execute_notebook.py notebooks/phase3_association.ipynb --timeout 1200
python scripts/execute_notebook.py notebooks/phase4_anomaly.ipynb --timeout 1800
python dashboard/app.py
```

The dashboard serves on `http://127.0.0.1:8050`.

Order matters, Phase 3 and Phase 4 assert against stale artefacts and fail rather than silently mixing runs.

Cluster numbering permutes between runs even with a fixed seed, because centroid initialisation order is not stable. Everything downstream matches segments by **name** via `cluster_names.csv`; new analysis must do the same.

`src/run_pipeline.py` uses direct local execution by default. Set `HOME_CREDIT_USE_PREFECT=1` only when a compatible Prefect/FastAPI environment is available.

## Layout

```
src/run_pipeline.py    single entry point for Phase 1
src/domain_credit.py   domain logic, cluster backtest, anomaly reasoning
src/pipeline/          the ten preprocessing steps, in execution order:
    load_raw_tables          read the eight source CSVs
    aggregate_histories      roll up 5 credit histories to applicant grain
    join_to_applicant        stack train+test, join the histories
    clean_structure          sentinels, rare categories, redundant columns
    flag_and_impute_missing  flag missingness first, then impute
    treat_outliers           winsorize, cap, bin
    engineer_ratios          leverage and burden ratios, log transforms
    encode_categoricals      ordinal and frequency encoding, no one-hot
    build_matrices           the three output views (see below)
    check_features          correlation + MI report; selects nothing
notebooks/             EDA + phases 2-4
results/               CSV and PNG artefacts per phase, plus validation/
dashboard/             Plotly Dash app
datasets/              raw CSVs and final feature tables
```

Step 9 produces three views of the same applicants, because each downstream
phase needs a different trade-off:

| Matrix | Treatment | Used by |
|---|---|---|
| `features_business.csv` | Readable values plus audit trail | Case review, rules, dashboard text |
| `features_clustering.csv` | Clipped at p0.5/p99.5, standardized | K-Means, DBSCAN, Ward |
| `features_anomaly.csv` | Standardized, **not** clipped | Phase 4 detectors |

The step number is the execution order and it is strict: each step consumes the
frame the previous one returned.

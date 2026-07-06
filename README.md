# Home Credit Default Risk, a KDD Project (Phases 1 to 5)

An academic data mining project that applies the KDD (Knowledge Discovery in Databases) methodology to the Home Credit Default Risk dataset. All 356,255 applications are used (307,511 train plus 48,744 test, combined because the process is unsupervised) together with 5 relational tables, the largest holding 27.3 million rows.

The full written report is [REPORT.md](REPORT.md) at the project root. Supporting documents (per-phase rationale, process validation, presentation outline) live in `reports/`.

## Folder structure

```
.
├── datasets/                         # Raw CSVs (Kaggle) + Phase 1 output
│   ├── application_train.csv         # 307K rows, 122 columns + TARGET
│   ├── application_test.csv          # 48K rows
│   ├── bureau.csv, bureau_balance.csv
│   ├── credit_card_balance.csv, installments_payments.csv
│   ├── POS_CASH_balance.csv, previous_application.csv
│   └── final/
│       ├── features_clustering.csv   # Phase 1 output (356,255 x SK_ID_CURR + 47 features)
│       ├── cluster_labels.csv        # Phase 2 output (ROW_ID + SK_ID_CURR + labels from 3 algorithms)
│       └── cluster_names.csv         # Phase 2 output: cluster_id to business-name mapping.
│                                     #   Downstream MUST read this file, because cluster
│                                     #   numbering shifts between runs.
│
├── docs/                             # Project brief (PDF)
│
├── notebooks/
│   ├── exploratory_data_analysis.ipynb   # Phase 1 EDA
│   ├── phase2_clustering.ipynb           # Phase 2, segmentation
│   ├── phase3_association.ipynb          # Phase 3, rule mining (full data)
│   └── phase4_anomaly.ipynb              # Phase 4, anomaly detection (full data, 5 detectors)
│
├── src/
│   ├── run_pipeline.py               # Phase 1 entry point. Prefect flow; falls back to
│   │                                 #   plain Python when Prefect is not installed
│   └── pipeline/                     # 10 modular steps; config.py holds every threshold
│                                     #   with its EDA justification
│
├── dashboard/
│   └── app.py                        # Phase 5, interactive Plotly Dash dashboard
│
├── REPORT.md                         # The hand-written knowledge discovery report (all phases)
├── reports/                          # Supporting hand-written documents
│   ├── reasoning_validation.md       # Detailed rationale behind every decision, per phase
│   ├── validation_report.md          # End-to-end process audit with the final figures
│   ├── knowledge_discovery_report.md # Business-facing summary of the findings
│   └── presentation_outline.md       # 10-minute presentation plan + Mining Expo answers
│
└── results/                          # Per-phase artefacts (CSV/PNG, all regenerated on re-run)
    ├── phase1_preprocessing/
    ├── phase2_clustering/
    ├── phase3_association/
    └── phase4_anomaly/
```

## Setup

```bash
python -m venv env
./env/Scripts/activate           # Windows
source env/bin/activate          # Linux/Mac
pip install -r requirements.txt
```

## How to run (the order is mandatory)

```bash
# Phase 1, preprocessing (pipeline script, Prefect orchestration)     ~13 minutes
PYTHONIOENCODING=utf-8 python src/run_pipeline.py

# Phase 2, clustering                                                  ~8 minutes
PYTHONIOENCODING=utf-8 jupyter nbconvert --to notebook --execute --inplace notebooks/phase2_clustering.ipynb --ExecutePreprocessor.timeout=3000

# Phase 3, association rules                                           ~4 minutes
PYTHONIOENCODING=utf-8 jupyter nbconvert --to notebook --execute --inplace notebooks/phase3_association.ipynb --ExecutePreprocessor.timeout=2400

# Phase 4, anomaly detection                                           ~10 minutes
PYTHONIOENCODING=utf-8 jupyter nbconvert --to notebook --execute --inplace notebooks/phase4_anomaly.ipynb --ExecutePreprocessor.timeout=3600

# Phase 5, dashboard
python dashboard/app.py          # open http://127.0.0.1:8050
```

Phases 3 and 4 carry a guard: if `cluster_labels.csv` does not align with `features_clustering.csv` (a stale artefact from an older run), execution fails loudly with a clear message. The fix is to re-run Phase 2.

## What each phase does, in one paragraph

Phase 1 turns 7 raw CSVs into one clean table: 356,255 rows with 47 standardized numeric features and zero missing values, plus `SK_ID_CURR` as an identifier. Feature selection uses both required measures: a Pearson correlation audit (perfectly collinear columns removed, remaining pairs documented) and entropy-based mutual information against the default label.

Phase 2 finds 5 customer segments with K-Means (K=5, chosen by elbow and silhouette), validates them with Ward hierarchical clustering (agreement 0.55) and dendrograms across three linkage methods, and uses DBSCAN on a UMAP embedding as a density-based noise detector whose isolated points feed the anomaly phase. The id-to-name mapping is stored in `cluster_names.csv` because numbering permutes between runs.

Phase 3 discretizes 7 dimensions by quantile and runs Apriori, FP-Growth, and ECLAT over all 356,255 transactions. The three algorithms find identical rule sets, and 15 final rules survive the lift, confidence, and redundancy filters, three per segment.

Phase 4 scores every application with five detectors: IQR and Z-score (univariate), robust Mahalanobis distance and Isolation Forest (multivariate), and the Phase 2 DBSCAN noise flag (density). A row flagged by three or more is a high-confidence anomaly. Each case gets a theory label (global, contextual, collective), a business label (data error, rare but valid, risk signal), and a segment-specific recommendation, all tied to real applicant IDs.

Phase 5 is the Plotly Dash dashboard for a business audience and the written reports. Every number on the dashboard is read from the result artefacts, so a re-run keeps it in sync. The honesty test is shown up front: segments and anomaly tiers stratify real default rates monotonically even though the label was never used during mining.

## Technical notes

Always run with `PYTHONIOENCODING=utf-8` on Windows so the logs do not hit encoding errors. Hierarchical clustering on 356K rows cannot use quadratic memory, so Ward runs on a representative sample and the rest of the data is assigned to the nearest centre; DBSCAN is limited to a 50K sample for a similar reason. All random seeds are 42, so the groupings are stable between runs, but the cluster numbering is not: always read `cluster_names.csv`. `SK_ID_CURR` flows from the pipeline through to the anomaly investigation so every finding can be traced to a real applicant.

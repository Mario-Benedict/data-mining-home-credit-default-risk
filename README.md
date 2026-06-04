# Home Credit Default Risk — KDD Project (Phase 1–4)

Academic data mining project mengikuti metodologi **KDD (Knowledge Discovery in Databases)** pada dataset *Home Credit Default Risk*.

## Struktur Folder

```
.
├── datasets/                         # Raw CSV (Kaggle) + output Phase 1
│   ├── application_train.csv         # 307K rows, 122 kolom + TARGET
│   ├── application_test.csv          # 48K rows
│   ├── bureau.csv, bureau_balance.csv
│   ├── credit_card_balance.csv, installments_payments.csv
│   ├── POS_CASH_balance.csv, previous_application.csv
│   └── final/
│       ├── features_clustering.csv   # Output Phase 1 (356K × 67 fitur)
│       └── cluster_labels.csv        # Output Phase 2 (untuk Phase 3 & 4)
│
├── docs/                             # Project criteria
│   ├── Data Mining Project Details Banking Final.pdf
│   └── Dataset Reference Document.pdf
│
├── notebooks/
│   ├── exploratory_data_analysis.ipynb  # Phase 1 EDA (36 sel, 10 seksi)
│   ├── phase2_clustering.ipynb           # Phase 2 — segmentation
│   ├── phase3_association.ipynb          # Phase 3 — rule mining
│   └── phase4_anomaly.ipynb              # Phase 4 — anomaly detection
│
├── src/
│   ├── run_pipeline.py               # Entry point Phase 1 preprocessing
│   └── pipeline/                     # Modular preprocessing steps
│       ├── config.py                 # Semua threshold + feature list
│       ├── utils.py
│       ├── step1_load.py             # Read raw CSV
│       ├── step2_aggregate.py        # Roll-up tabel relasional
│       ├── step3_merge.py            # Train+test stack & left-join
│       ├── step4_clean.py            # Sentinel, XNA, rare categories
│       ├── step5_missing.py          # Imputasi + missing indicators
│       ├── step6_outliers.py         # Winsorize p99 + cap
│       ├── step7_engineer.py         # Derived ratios + log transform
│       ├── step8_encode.py           # Binary/Ordinal/OHE
│       ├── step9_scale.py            # StandardScaler + final feature set
│       └── step10_feature_selection.py  # Korelasi + entropy (MI) validasi
│
└── results/                          # Output rapi per phase
    ├── phase1_preprocessing/
    │   ├── feature_importance.csv    # Mutual info per fitur vs TARGET
    │   ├── high_corr_pairs.csv       # |r| > 0.85 yang tersisa
    │   └── preprocessing_report.txt  # Laporan Phase 1
    ├── phase2_clustering/
    │   ├── pca_variance.csv, pca_variance_plot.png
    │   ├── k_selection.csv, elbow_plot.png
    │   ├── cluster_labels.csv         # = datasets/final/cluster_labels.csv
    │   ├── cluster_profiles.csv, cluster_summary.csv
    │   ├── cluster_viz.png, cluster_profile_plot.png, dendrogram.png
    │   └── business_report.txt
    ├── phase3_association/
    │   ├── transactions_list.pkl, transactions_ohe.pkl
    │   ├── rules_apriori.csv, rules_fpgrowth.csv, rules_eclat.csv
    │   ├── rules_per_cluster.csv, rules_combined.csv
    │   ├── algo_comparison.csv, rule_table_final.csv
    │   ├── rule_interpretations.txt   # SPESIFIK per rule (bukan template)
    │   ├── plot_*.png
    │   └── business_report.txt
    └── phase4_anomaly/
        ├── data_numeric.csv, data_with_labels.csv
        ├── statistical_outliers.csv  (IQR + Z-score)
        ├── isolation_forest_outliers.csv  (3 contamination levels)
        ├── anomaly_combined.csv, anomaly_summary.csv
        ├── anomaly_investigation.csv, anomaly_investigation.txt
        ├── plot_*.png
        └── business_report.txt
```

## Setup

```bash
python -m venv env
./env/Scripts/activate           # Windows
source env/bin/activate          # Linux/Mac
pip install pandas numpy scikit-learn scipy matplotlib seaborn mlxtend networkx jupyter nbconvert
```

## Cara Jalankan

### Phase 1 — Preprocessing
```bash
PYTHONIOENCODING=utf-8 python src/run_pipeline.py
```
Output: `datasets/final/features_clustering.csv` + `results/phase1_preprocessing/`. Estimasi: ~5 menit.

### Phase 2 — Clustering
```bash
PYTHONIOENCODING=utf-8 jupyter nbconvert --to notebook --execute notebooks/phase2_clustering.ipynb --ExecutePreprocessor.timeout=1200
```
Output: `results/phase2_clustering/` + `datasets/final/cluster_labels.csv`. Estimasi: ~5 menit.

### Phase 3 — Association Rules
```bash
PYTHONIOENCODING=utf-8 jupyter nbconvert --to notebook --execute notebooks/phase3_association.ipynb --ExecutePreprocessor.timeout=1200
```
Output: `results/phase3_association/`. Estimasi: ~3 menit.

### Phase 4 — Anomaly Detection
```bash
PYTHONIOENCODING=utf-8 jupyter nbconvert --to notebook --execute notebooks/phase4_anomaly.ipynb --ExecutePreprocessor.timeout=1200
```
Output: `results/phase4_anomaly/`. Estimasi: ~3 menit.

## Ringkasan Hasil

### Phase 1 — Preprocessing
- 7 file CSV mentah → 356,255 rows × 67 fitur akhir (numerik, standardized)
- Feature selection: korelasi + **mutual information** (entropy-based) terhadap TARGET
- Top fitur diskriminatif (MI): CODE_GENDER, NAME_EDUCATION_TYPE, FLAG_NO_CAR, FLAG_EXT_SOURCE_1_MISSING
- 5 pasangan |r|>0.85 tersisa (terdokumentasi)

### Phase 2 — Clustering
- **PCA**: 10 komponen (54.4% variance)
- **K-Means** (K=5, full 356K data): Silhouette 0.148, Inertia 5.13M
- **DBSCAN** (sample 30K, eps=3.0): outlier detection
- **Hierarchical**: BIRCH → MiniBatchKMeans 500 micro-centroids → Ward linkage + dendrogram
- 5 cluster bisnis: Peminjam Minimal, Veteran Aktif, Peminjam Ambisius, Peminjam Bermasalah, CC Intensif

### Phase 3 — Association Rules
- Discretisasi 7 fitur (qcut → income/age/employment/credit/burden/risk_score/cluster)
- **Apriori + FP-Growth + ECLAT** + per-cluster FP-Growth
- 15 final rules (top-3 per cluster + Jaccard anti-redundancy filter)
- **Interpretasi spesifik per rule** (What it says / Why it matters / Risk reading / Actionable recommendation) — TIDAK pakai template generik
- Cross-algorithm consistency: rules ditemukan ≥2 algoritma diberi bonus skor

### Phase 4 — Anomaly Detection
- **3 metode**: IQR (1.5×), Z-score (>3), Isolation Forest (3 contamination levels)
- **Cross-reference** dengan DBSCAN noise dari Phase 2
- 1,412 high-confidence anomalies dari 50K sample (2.8%)
- **Typology**: Tipe A (Data Error → fix ETL), Tipe B (Rare Valid → wealth routing), Tipe C (Risk Signal → manual underwriting)

## Pemetaan ke Kriteria PDF (`docs/Data Mining Project Details Banking Final.pdf`)

| Phase | Kriteria PDF | Implementasi | Status |
|---|---|---|---|
| 1 | Cleaning + transformation + correlation + **entropy** selection | step1-9 + step10_feature_selection (mutual_info_classif) | ✅ Excellent |
| 2 | K-Means + DBSCAN + Hierarchical + Elbow + Silhouette + profiling bisnis | Notebook phase2 — semua + business naming + dendrogram | ✅ Excellent |
| 3 | Discretize + Apriori + Support/Conf/Lift + ≥10 rules + interpretasi spesifik | Notebook phase3 — Apriori + FP-Growth + ECLAT + 15 rules + 4-komponen interpretasi | ✅ Excellent |
| 4 | IQR + Z-score + Isolation Forest + cross-ref Phase 2 + typology | Notebook phase4 — semua + cross-ref DBSCAN + tipe A/B/C | ✅ Excellent |
| 5 | Dashboard + presentation | _belum dikerjakan (out of scope)_ | — |

## Catatan Teknis

- **Encoding Windows**: pipeline log pakai UTF-8 via `sys.stdout.reconfigure`. Selalu jalankan dengan `PYTHONIOENCODING=utf-8`.
- **Memory**: Hierarchical clustering pada 356K rows mustahil O(n²). Solusi: BIRCH → 500 micro-centroids → linkage + agglomerative.
- **Reproducibility**: Semua random seed = 42.
- **Cluster naming**: Heuristik berdasarkan top-features. Mapping cluster_id → nama bisa berubah antar run (algoritma tidak deterministik dalam labeling order, hanya dalam grouping). Lihat `business_report.txt` untuk mapping aktual.

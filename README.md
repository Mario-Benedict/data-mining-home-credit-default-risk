# Project Setup and Installation Guide

This guide provides instructions on how to set up a Python virtual environment, install the required dependencies, and run the program.

## Prerequisites

Before starting, make sure you have the following installed on your system:
* **Python 3.x**
* **pip** (Python package installer)

## Installation Steps

### 1. Clone the Repository
If you haven't already, clone this repository to your local machine and navigate into the directory:

```bash
git clone https://github.com/Mario-Benedict/data-mining-home-credit-default-risk.git
cd data-mining-home-credit-default-risk
```

### 2. Create a Virtual Environment
It is highly recommended to use a virtual environment to avoid dependency conflicts. Run the following command in your project root directory:

```bash
python -m venv venv
```
*(This creates a folder named `venv` containing your isolated Python environment).*

### 3. Activate the Virtual Environment
Before installing any packages or running the code, you must activate the virtual environment. Use the command specific to your operating system:

**Windows (Command Prompt):**
```cmd
venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
source venv/bin/activate
```
*(Once activated, you should see `(venv)` at the beginning of your terminal prompt).*

### 4. Install Dependencies
With the environment activated, install all required packages listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Import the datasets
Make sure to place the datasets in the `datasets` directory as specified in the `.gitignore` file. This directory is ignored by Git to prevent large files from being tracked. Copy the datasets from [Kaggle](https://www.kaggle.com/competitions/home-credit-default-risk/data) into the `datasets` folder.

## Running the Preprocessing Pipeline

Make sure your virtual environment is still activated, then execute the pipeline Python script to run the application:

```bash
python src/run_pipeline.py
```

## Deactivating the Environment

When you are finished working, you can safely exit the virtual environment and return to your global Python environment by running:

```bash
deactivate
```

---

## Phase 2 — Segmentation via Clustering (COMPLETED)

Phase 2 is fully complete. All clustering work has been done and results are ready to be handed over to Phase 3.

### Dataset Structure After Phase 2

```
datasets/
├── (raw Kaggle files — application_train.csv, bureau.csv, etc.)
├── final/
│   ├── features_clustering.csv   ← 356,255 rows × 67 features (output Phase 1, input Phase 3)
│   └── cluster_labels.csv        ← ROW_ID, CLUSTER_KMEANS, CLUSTER_DBSCAN, IS_OUTLIER (output Phase 2)
└── clustering/                   ← all Phase 2 intermediate outputs
    ├── features_pca10.csv        ← PCA 10 components used for clustering
    ├── features_pca2.csv         ← PCA 2 components for 2D visualization
    ├── features_pca50.csv        ← old/unused file (kept for reference)
    ├── pca_variance.csv          ← explained variance per component
    ├── pca_variance_plot.png
    ├── k_selection.csv           ← inertia + silhouette per K
    ├── elbow_plot.png
    ├── silhouette_plot.png
    ├── clustering_viz.png        ← scatter plot of cluster results
    ├── dendrogram.png            ← hierarchical clustering dendrogram
    ├── cluster_profiles.csv      ← mean of all features per cluster
    ├── cluster_summary.csv       ← top 10 differentiating features per cluster
    ├── cluster_profile_plot.png  ← bar chart of top features per cluster
    └── business_report.txt       ← full business interpretation + DM concepts explanation
```

### Scripts (src/clustering/)

| Script | Dijalankan di | Status |
|--------|--------------|--------|
| `step1_pca.py` | Laptop (VS Code) | Done |
| `step2_elbow.py` | Laptop (VS Code) | Done |
| `step3_clustering_kaggle.ipynb` | Kaggle | Done |
| `step4_profiling.py` | Laptop (VS Code) | Done |
| `step5_business_report.py` | Laptop (VS Code) | Done |

### Phase 2 Results Summary

**Configuration:** K=5, PCA N_components=10, Silhouette=0.1348, Inertia=5,221,730

**Cluster Profiles:**

| Cluster | Name | Count | % | Risk |
|---------|------|-------|---|------|
| 0 | Veteran Aktif — High income, high rejection rate | 66,102 | 18.6% | MEDIUM-HIGH |
| 1 | Peminjam Minimal — Low income, small credit | 114,077 | 32.0% | LOW-MEDIUM |
| 2 | Pengguna CC Intensif — Revolving credit dependent | 55,476 | 15.6% | MEDIUM-HIGH |
| 3 | Peminjam Ambisius — Large credit, high debt-to-income | 117,074 | 32.9% | MEDIUM |
| 4 | Peminjam Bermasalah — Chronic defaulter | 3,526 | 1.0% | VERY HIGH |

Full business interpretation is in `datasets/clustering/business_report.txt`.

### Notes for Phase 3

- `SK_ID_CURR` is **not present** in `features_clustering.csv` — Phase 1 pipeline did not save the ID column. All joins must use `ROW_ID` (row position index 0, 1, 2, ...).
- `CLUSTER_DBSCAN` in `cluster_labels.csv` was run on a 30K sample only (full 356K is too heavy for CPU). `CLUSTER_KMEANS` covers all 356,255 rows and is the primary label to use.
- `IS_OUTLIER` column marks rows flagged as DBSCAN outliers (312 rows, ~1% of the sample).
- Cluster 4 (Peminjam Bermasalah) is the smallest but most extreme group — pay special attention to it in Phase 3 analysis.

---

## Phase 3 — Association Rule Mining (COMPLETED)

Phase 3 is fully complete. All association rule mining work has been done
and results are ready to be handed over to Phase 5 (Dashboard).

### Dataset Structure After Phase 3

`
datasets/
├── final/
│   ├── features_clustering.csv   ← input Phase 3 (from Phase 1)
│   └── cluster_labels.csv        ← input Phase 3 (from Phase 2)
└── association/                  ← all Phase 3 outputs
    ├── transactions.csv          ← discretized transactions
    ├── transactions_list.pkl     ← list format for ECLAT/Apriori
    ├── transactions_ohe.pkl      ← one-hot encoded for FP-Growth
    ├── rules_apriori.csv         ← rules from Apriori (sample 50K)
    ├── rules_fpgrowth.csv        ← rules from FP-Growth (full 356K)
    ├── rules_eclat.csv           ← rules from ECLAT (sample 50K)
    ├── rules_per_cluster.csv     ← rules from per-cluster FP-Growth
    ├── algo_comparison.csv       ← performance comparison table
    ├── rules_combined.csv        ← all rules merged + consistency flags
    ├── rule_table_final.csv      ← 15 final rules for report ★
    ├── rule_interpretations.txt  ← business interpretation detail ★
    ├── business_report.txt       ← full business report ★
    ├── plot_algo_comparison.png
    ├── plot_cluster_heatmap.png
    ├── plot_consistency.png
    ├── plot_rule_network.png
    └── plot_scatter_per_algo.png
`

★ = files to be handed over to Phase 5 (Insight Communicator)

### Scripts (src/association/)

| Script | Dijalankan di | Status |
|--------|--------------|--------|
| \step1_discretize.py\ | Laptop (VS Code) | Done |
| \step2a_apriori.py\ | Laptop (VS Code) | Done |
| \step2b_fpgrowth.py\ | Laptop (VS Code) | Done |
| \step2c_eclat.py\ | Laptop (VS Code) | Done |
| \step2d_per_cluster.py\ | Laptop (VS Code) | Done |
| \step3_compare.py\ | Laptop (VS Code) | Done |
| \step4_filter_interpret.py\ | Laptop (VS Code) | Done |
| \step4b_diverse_rules.py\ | Laptop (VS Code) | Done |
| \step5_visualize.py\ | Laptop (VS Code) | Done |
| \step6_business_report.py\ | Laptop (VS Code) | Done |

### Phase 3 Results Summary

**Algorithms Used:** Apriori, FP-Growth, ECLAT + Per-Cluster FP-Growth
**Total Unique Rules Discovered:** 408
**Validated Rules (≥2 algorithms):** 348 (85.3%)
**Final Rules Selected for Report:** 15

**Algorithm Performance:**

| Algorithm | Sample Size | Frequent Itemsets | Rules | Time |
|-----------|-------------|-------------------|-------|------|
| Apriori | 50K | 45 | varies | ~0.03s |
| FP-Growth | 356K (full) | 45 | varies | ~0.68s |
| ECLAT | 50K | 45 | varies | ~0.13s |
| Per-Cluster FP-Growth | per cluster | — | varies | — |

**Cluster Coverage in Final Rules:**

| Cluster | Name | Rules |
|---------|------|-------|
| 0 | Veteran Aktif | 2 rules |
| 1 | Peminjam Minimal | 3 rules |
| 2 | Pengguna CC Intensif | 0 (documented — no explicit rules found) |
| 3 | Peminjam Ambisius | 2 rules |
| 4 | Peminjam Bermasalah | 0 (documented — insufficient support due to 1% population) |

**Key Findings:**
- Rule dengan lift tertinggi (9.56): nasabah senior + kredit kecil + beban tinggi
  hampir selalu masuk Cluster 1 (Peminjam Minimal) dengan status karyawan baru
- Cluster 0 (Veteran Aktif) selalu berasosiasi kuat dengan income sangat tinggi
- Nasabah income rendah + kredit kecil konsisten menunjukkan beban cicilan tinggi

Full business interpretation: \datasets/association/rule_interpretations.txtFull business report: \datasets/association/business_report.txt
### Notes for Phase 5

- ule_table_final.csv\ → tabel rules siap ditampilkan di dashboard
- ule_interpretations.txt\ → narasi bisnis untuk setiap rule
- \usiness_report.txt\ → laporan lengkap untuk section Association Rules
- Semua file PNG siap digunakan sebagai visual di dashboard
- Cluster 2 & 4 tidak menghasilkan explicit rules — penjelasan ada di business_report.txt

---

## Phase 4 — Anomaly & Outlier Detection (COMPLETED)

Phase 4 is fully complete. All anomaly detection work has been done
and results are ready to be handed over to Phase 5 (Dashboard).

### Dataset Structure After Phase 4

`	ext
datasets/
├── final/
│   ├── features_clustering.csv   ← input Phase 4 (from Phase 1)
│   └── cluster_labels.csv        ← input Phase 4 (from Phase 2)
└── anomaly/                      ← all Phase 4 outputs
    ├── data_numeric.csv          ← cleaned numeric features
    ├── data_with_labels.csv      ← numeric + cluster labels
    ├── statistical_outliers.csv  ← IQR + Z-score results
    ├── isolation_forest_outliers.csv ← Isolation Forest results
    ├── anomaly_combined.csv      ← all methods merged ★
    ├── anomaly_summary.csv       ← statistics summary ★
    ├── anomaly_investigation.csv ← Tipe A/B/C classification ★
    ├── anomaly_investigation.txt ← narrative investigation ★
    ├── business_report.txt       ← full business report ★
    ├── plot_method_overlap.png
    ├── plot_pca_anomaly.png
    ├── plot_anomaly_per_cluster.png
    ├── plot_anomaly_heatmap.png
    └── plot_isolation_score_dist.png
`

★ = files to be handed over to Phase 5 (Insight Communicator)

### Scripts (src/anomaly/)

| Script | Dijalankan di | Status |
|--------|--------------|--------|
| step0_check.py | Laptop (VS Code) | Done |
| step1_load_prepare.py | Laptop (VS Code) | Done |
| step2_statistical.py | Laptop (VS Code) | Done |
| step3_isolation_forest.py | Laptop (VS Code) | Done |
| step4_crossreference.py | Laptop (VS Code) | Done |
| step5_investigate.py | Laptop (VS Code) | Done |
| step6_visualize.py | Laptop (VS Code) | Done |
| step7_business_report.py | Laptop (VS Code) | Done |

### Phase 4 Results Summary

**Methods Used:** IQR, Z-score, Isolation Forest, Cross-reference DBSCAN (Phase 2)
**Sample Size:** 50.000 baris (random_state=42)

**Detection Results:**

| Method | Flagged | % of Sample |
|--------|---------|-------------|
| IQR (≥3 columns) | ~39.000 | ~78% |
| Z-score (≥3 columns) | ~4.000 | ~8% |
| Isolation Forest (5% contamination) | 2.500 | 5% |
| DBSCAN Phase 2 (IS_OUTLIER) | 312 | <1% |

**Anomaly Categories (after cross-reference):**

| Category | Count | % of Sample |
|----------|-------|-------------|
| HIGH_CONFIDENCE_ANOMALY | 1.402 | 2.8% |
| MODERATE_ANOMALY | — | — |
| WEAK_SIGNAL | 34.752 | ~70% |
| NORMAL | — | — |

**Anomaly Type Classification (HIGH_CONFIDENCE only):**

| Type | Count | Description |
|------|-------|-------------|
| Tipe A — Data Error | 898 | Nilai tidak masuk akal / kode error dataset |
| Tipe B — Rare but Valid | 482 | Kasus ekstrem tapi logis (e.g. nasabah kaya) |
| Tipe C — Risk Signal | 22 | Kombinasi finansial mencurigakan → eskalasi |

**Key Finding — Cluster Analysis:**
- Cluster 4 (Peminjam Bermasalah): **64.6% anggotanya adalah HIGH_CONFIDENCE_ANOMALY**
  → Konsisten dengan Phase 2 (cluster paling berisiko) dan Phase 3
  (tidak ada pola asosiasi yang bisa ditemukan karena profil terlalu heterogen)
- Cluster 2 (CC Intensif): 7.7% anomali — tertinggi kedua

**Cross-Phase Consistency:**
Temuan Phase 4 konsisten dengan Phase 2 dan Phase 3:
- Phase 2 mendeteksi Cluster 4 sebagai kelompok risiko sangat tinggi
- Phase 3 tidak menemukan pola asosiasi eksplisit di Cluster 4
  (karena profil terlalu heterogen)
- Phase 4 mengkonfirmasi: 64.6% anggota Cluster 4 adalah anomali murni

### Notes for Phase 5

- nomaly_combined.csv → data lengkap untuk filter/drill-down di dashboard
- nomaly_summary.csv → ringkasan statistik untuk chart overview
- nomaly_investigation.csv → tabel tipe A/B/C untuk visualisasi detail
- usiness_report_phase4.txt → narasi untuk section anomaly di laporan
- Semua PNG siap digunakan sebagai visual di dashboard
- **Highlight untuk dashboard:** Cluster 4 dengan 64.6% anomali rate
  adalah temuan paling signifikan dari Phase 4

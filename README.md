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
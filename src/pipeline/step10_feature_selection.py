"""
Step 10 — Feature Selection Report (correlation + entropy / mutual information).

Tujuan:
  Memvalidasi kualitas feature set hasil step1-9 dengan dua pengukuran formal:
    1. Pearson correlation antar-fitur → deteksi multikolinearitas tersisa
    2. Mutual Information (entropy-based) vs TARGET → kekuatan diskriminatif

Tidak menulis ulang features_clustering.csv — hanya menghasilkan laporan
yang membenarkan mengapa setiap fitur dipertahankan.

Output:
  results/phase1_preprocessing/feature_importance.csv
  results/phase1_preprocessing/high_corr_pairs.csv
  results/phase1_preprocessing/preprocessing_report.txt
"""
import os
import numpy as np
import pandas as pd
from sklearn.feature_selection import mutual_info_classif

from .config import BASE_DIR, OUTPUT_DIR, PATHS
from .utils import log


REPORT_DIR = os.path.join(BASE_DIR, "results", "phase1_preprocessing")
FEATURES_PATH = os.path.join(OUTPUT_DIR, "features_clustering.csv")


def compute_mutual_info(features: pd.DataFrame, target: pd.Series) -> pd.DataFrame:
    """
    Hitung mutual_info_classif untuk setiap fitur terhadap TARGET.
    MI = 0 → fitur tidak memberi informasi tentang TARGET (default vs non-default).
    MI > 0 → ada hubungan non-linear yang terdeteksi.

    Menggunakan random_state untuk reproduksibilitas.
    """
    log(f"  Computing mutual_info_classif on {features.shape[1]} features ...")
    mi_scores = mutual_info_classif(
        features.values,
        target.values,
        discrete_features=False,
        random_state=42,
        n_neighbors=3,
    )
    df = pd.DataFrame({
        "feature": features.columns,
        "mutual_info": mi_scores,
    }).sort_values("mutual_info", ascending=False).reset_index(drop=True)
    df["rank"] = df.index + 1
    return df


def compute_correlation_pairs(features: pd.DataFrame, threshold: float = 0.85) -> pd.DataFrame:
    """Pearson correlation pairs |r| > threshold, exclude self-pairs."""
    log(f"  Computing correlation matrix ({features.shape[1]} × {features.shape[1]}) ...")
    corr = features.corr().abs()
    upper = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool))
    pairs = (
        upper.stack()
        .reset_index()
        .rename(columns={"level_0": "feature_1", "level_1": "feature_2", 0: "abs_corr"})
    )
    high = pairs[pairs["abs_corr"] > threshold].sort_values("abs_corr", ascending=False).reset_index(drop=True)
    return high


def build_preprocessing_report(
    n_features: int,
    n_train_rows: int,
    mi_df: pd.DataFrame,
    high_corr: pd.DataFrame,
) -> str:
    lines = []
    lines.append("# Phase 1 — Preprocessing Report")
    lines.append("**Dataset:** Home Credit Default Risk")
    lines.append("")
    lines.append("Laporan ini merangkum apa yang dilakukan pipeline terhadap 7 file CSV mentah dan")
    lines.append("memberi bukti bahwa feature set akhir layak dipakai untuk mining: multikolinearitas")
    lines.append("yang berbahaya sudah dibuang, dan daya pisah tiap fitur terhadap default diukur")
    lines.append("dengan mutual information. Setiap keputusan merujuk ke temuan EDA, bukan selera.")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## Pipeline Steps (`src/pipeline/`)")
    lines.append("")
    lines.append("| Step | Deskripsi |")
    lines.append("|------|-----------|")
    lines.append("| `step1_load` | Membaca 7 file CSV mentah |")
    lines.append("| `step2_aggregate` | Roll-up 5 tabel relasional → grain SK_ID_CURR |")
    lines.append("| `step3_merge` | Stack train+test, left-join semua agregat |")
    lines.append("| `step4_clean` | Sentinel value (DAYS_EMPLOYED=365243), XNA → NaN, rare categories |")
    lines.append("| `step5_missing` | Indikator missingness + imputasi (median/zero/mode) |")
    lines.append("| `step6_outliers` | Winsorize p99 + cap + bin DPD social-circle |")
    lines.append("| `step7_engineer` | Derived ratios + log transform + drop kolom redundan |")
    lines.append("| `step8_encode` | Binary / ordinal (pendidikan) / frequency (income, organization) — bukan OHE |")
    lines.append("| `step9_scale` | StandardScaler pada fitur kontinu & ordinal; hanya flag {0,1} dibiarkan |")
    lines.append("| `step10_feature_selection` | Validasi feature selection — korelasi + entropy (MI) |")
    lines.append("")
    lines.append(f"> **Final Feature Set:** {n_features} fitur × {n_train_rows:,} baris train")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## Feature Selection — Korelasi (Pearson)")
    lines.append("")
    lines.append("**Multikolinearitas yang sudah di-drop di step1–7** (justifikasi EDA §7):")
    lines.append("")
    lines.append("- Housing triplication: 14 kolom `*_AVG` dan `*_MEDI` (r > 0.99 dengan `*_MODE`)")
    lines.append("- `OBS_60_CNT_SOCIAL_CIRCLE` (r = 0.998 dgn OBS_30)")
    lines.append("- `FLAG_EMP_PHONE` (r = -1.0 dgn DAYS_EMPLOYED setelah sentinel)")
    lines.append("- `FLAG_MOBIL` (near-constant)")
    lines.append("- `REGION_RATING_CLIENT` (r > 0.85 dgn varian _W_CITY)")
    lines.append("")
    lines.append("**Encoding kategorikal yang ramah-clustering (bukan OHE).** Variabel "
                 "nominal sengaja TIDAK di-one-hot. Pada K-Means yang memakai jarak "
                 "Euclidean, OHE memecah satu kolom menjadi banyak sumbu biner sparse "
                 "yang membuat setiap kategori berjarak sama — padahal sebagian kategori "
                 "jelas lebih mirip. Tiga variabel kategorikal diperlakukan sesuai sifatnya:")
    lines.append("")
    lines.append("- `NAME_EDUCATION_TYPE` → **ordinal 0–4** (Lower secondary … Academic "
                 "degree). Jenjang pendidikan punya urutan nyata; satu integer terurut "
                 "menjaga 'Higher education lebih dekat ke Incomplete higher daripada ke "
                 "Lower secondary'.")
    lines.append("- `NAME_INCOME_TYPE` → **frequency encoding** (`NAME_INCOME_TYPE_FREQ`). "
                 "Nominal tanpa urutan; dipetakan ke seberapa umum kategori itu, menjadi "
                 "satu sumbu 'umum ↔ langka'.")
    lines.append("- `ORGANIZATION_TYPE` → **frequency encoding** (`ORGANIZATION_TYPE_FREQ`). "
                 "12 sektor → satu sumbu, alih-alih 11 dummy sparse yang mendominasi jarak.")
    lines.append("")
    lines.append("Pendekatan ini juga menghapus sumber kolinearitas sempurna pada run lama "
                 "(`FLAG_SENTINEL_EMPLOYED` ≡ `ORGANIZATION_TYPE_Unknown` ≡ "
                 "`NAME_INCOME_TYPE_Pensioner`, r ≈ 1.0) yang muncul justru karena OHE pada "
                 "kategori 'Unknown' yang berimpit dengan flag pensiunan. Pensiunan tetap "
                 "teridentifikasi terpisah lewat `FLAG_SENTINEL_EMPLOYED`.")
    lines.append("")
    lines.append(f"**Pasangan |r| > 0.85 yang TERSISA di feature set final:** {len(high_corr)}")
    lines.append("")
    if len(high_corr) == 0:
        lines.append("> Tidak ada multikolinearitas tinggi yang tersisa.")
    else:
        lines.append("| Feature 1 | Feature 2 | \\|r\\| |")
        lines.append("|-----------|-----------|-------|")
        for _, row in high_corr.iterrows():
            lines.append(f"| `{row['feature_1']}` | `{row['feature_2']}` | {row['abs_corr']:.3f} |")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## Feature Selection — Entropy (Mutual Information)")
    lines.append("")
    lines.append("**Metode:** `sklearn.feature_selection.mutual_info_classif`")
    lines.append("")
    lines.append("- Mengukur informasi mutual antara setiap fitur dengan TARGET")
    lines.append("- Berbasis entropy: `I(X;Y) = H(Y) - H(Y|X)`")
    lines.append("- Mendeteksi hubungan **non-linear** (tidak ditangkap korelasi Pearson)")
    lines.append("- `random_state=42`, `n_neighbors=3` (k-NN density estimator)")
    lines.append("")

    lines.append("### Top 15 Fitur — Kekuatan Diskriminatif Default")
    lines.append("")
    lines.append("| Rank | Feature | MI Score |")
    lines.append("|------|---------|----------|")
    for _, row in mi_df.head(15).iterrows():
        lines.append(f"| {int(row['rank'])} | `{row['feature']}` | {row['mutual_info']:.5f} |")
    lines.append("")

    lines.append("### Bottom 10 Fitur — Kandidat Drop (MI ≈ 0)")
    lines.append("")
    lines.append("| Rank | Feature | MI Score |")
    lines.append("|------|---------|----------|")
    for _, row in mi_df.tail(10).iterrows():
        lines.append(f"| {int(row['rank'])} | `{row['feature']}` | {row['mutual_info']:.5f} |")
    lines.append("")
    n_zero = int((mi_df["mutual_info"] <= 1e-6).sum())
    lines.append(f"- **Total fitur dengan MI ≈ 0 (tidak informatif):** {n_zero} / {len(mi_df)}")
    lines.append(f"- **Mean MI:** {mi_df['mutual_info'].mean():.5f}")
    lines.append(f"- **Median MI:** {mi_df['mutual_info'].median():.5f}")
    lines.append("")
    lines.append("Fitur dengan MI rendah tidak otomatis dibuang. Clustering bekerja tanpa label,")
    lines.append("jadi fitur yang lemah memprediksi default bisa tetap penting untuk membedakan")
    lines.append("perilaku nasabah. Skor MI di sini berfungsi sebagai audit: bukti terukur bahwa")
    lines.append("seleksi fitur memakai ukuran entropy, bukan hanya korelasi linear.")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## Deliverable — Clean Dataset")
    lines.append("")
    lines.append(f"| Item | Nilai |")
    lines.append(f"|------|-------|")
    lines.append(f"| File | `datasets/final/features_clustering.csv` |")
    lines.append(f"| Shape | {n_features} fitur × {n_train_rows:,} rows (numerik, terstandardisasi) |")
    lines.append(f"| Siap untuk | Phase 2 (K-Means, DBSCAN, Hierarchical clustering) |")
    lines.append("")
    lines.append("**File pendukung:**")
    lines.append("")
    lines.append("- [`feature_importance.csv`](feature_importance.csv) — MI score per fitur")
    lines.append("- [`high_corr_pairs.csv`](high_corr_pairs.csv) — pasangan korelasi tinggi yang tersisa")
    lines.append("- [`preprocessing_report.md`](preprocessing_report.md) — laporan ini")
    lines.append("")
    return "\n".join(lines)


def run() -> None:
    log("Step 10 — Feature selection report (correlation + entropy) ...")

    os.makedirs(REPORT_DIR, exist_ok=True)

    log(f"  Loading {FEATURES_PATH} ...")
    features_df = pd.read_csv(FEATURES_PATH)
    log(f"  features_clustering: {features_df.shape[0]:,} × {features_df.shape[1]}")

    log(f"  Loading TARGET from application_train.csv ...")
    target_df = pd.read_csv(PATHS["application_train"], usecols=["SK_ID_CURR", "TARGET"])
    n_train = len(target_df)
    log(f"  application_train: {n_train:,} rows (TARGET available)")

    if "SK_ID_CURR" in features_df.columns:
        # Robust ID-based alignment (no reliance on row order)
        aligned = features_df.merge(target_df, on="SK_ID_CURR", how="inner")
        train_target = aligned["TARGET"].reset_index(drop=True)
        train_features = aligned.drop(columns=["SK_ID_CURR", "TARGET"]).reset_index(drop=True)
    else:
        # Fallback: positional alignment (train rows stacked first in step3)
        train_features = features_df.iloc[:n_train].reset_index(drop=True)
        train_target = target_df["TARGET"].reset_index(drop=True)
    log(f"  Aligned for MI: {train_features.shape[0]:,} train rows, {train_features.shape[1]} features")

    mi_df = compute_mutual_info(train_features, train_target)
    mi_path = os.path.join(REPORT_DIR, "feature_importance.csv")
    mi_df.to_csv(mi_path, index=False)
    log(f"  Saved {mi_path}")

    high_corr = compute_correlation_pairs(train_features, threshold=0.85)
    corr_path = os.path.join(REPORT_DIR, "high_corr_pairs.csv")
    high_corr.to_csv(corr_path, index=False)
    log(f"  Saved {corr_path} ({len(high_corr)} pairs |r|>0.85)")

    report = build_preprocessing_report(
        n_features=train_features.shape[1],
        n_train_rows=n_train,
        mi_df=mi_df,
        high_corr=high_corr,
    )
    report_path = os.path.join(REPORT_DIR, "preprocessing_report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)
    log(f"  Saved {report_path}")
    log("  Phase 1 preprocessing report complete.")

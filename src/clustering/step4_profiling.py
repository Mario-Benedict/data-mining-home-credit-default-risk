"""
Step 4 — Cluster Profiling
===========================
Tujuan:
  - Gabungkan cluster labels dengan fitur asli (features_clustering.csv)
  - Hitung statistik deskriptif per cluster untuk setiap fitur
  - Identifikasi fitur yang paling membedakan tiap cluster
  - Hasilkan ringkasan profil bisnis tiap cluster

Cara kerja:
  - Untuk setiap fitur, hitung mean per cluster
  - Bandingkan mean cluster vs mean keseluruhan (dalam bentuk %)
  - Fitur dengan perbedaan terbesar = karakteristik utama cluster itu

Jalankan di: Laptop (VS Code)
Input:
  - datasets/final/cluster_labels.csv  (ROW_ID + CLUSTER_KMEANS)
  - datasets/final/features_clustering.csv (67 fitur asli)
Output:
  - datasets/final/cluster_profiles.csv      → statistik lengkap per cluster
  - datasets/final/cluster_summary.csv       → ringkasan fitur terpenting
  - datasets/final/cluster_profile_plot.png  → visualisasi radar/bar chart
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import os

# ── Konfigurasi ────────────────────────────────────────────────────────────

LABELS_PATH   = "datasets/final/cluster_labels.csv"
FEATURES_PATH = "datasets/final/features_clustering.csv"
OUTPUT_DIR    = "datasets/final"

# Jumlah fitur terpenting yang ditampilkan per cluster
TOP_N_FEATURES = 10

# Kolom yang di-skip saat profiling (bukan fitur behavioral)
SKIP_COLS = []


# ── Helper ─────────────────────────────────────────────────────────────────

def log(msg: str):
    print(f"[PROFILING] {msg}")


def load_data() -> pd.DataFrame:
    """
    Load cluster labels dan fitur asli, lalu gabungkan jadi satu DataFrame.

    ROW_ID dipakai sebagai kunci join — posisi baris harus sama
    antara cluster_labels.csv dan features_clustering.csv karena
    keduanya berasal dari pipeline yang sama tanpa shuffle.

    Returns:
        df : DataFrame dengan kolom CLUSTER_KMEANS + 67 fitur
    """
    log("Loading data ...")

    labels   = pd.read_csv(LABELS_PATH)
    features = pd.read_csv(FEATURES_PATH)

    log(f"  cluster_labels   : {labels.shape[0]:,} rows x {labels.shape[1]} cols")
    log(f"  features         : {features.shape[0]:,} rows x {features.shape[1]} cols")

    # Gabungkan berdasarkan posisi baris (ROW_ID = index baris)
    # Keduanya sudah urut 0,1,2,... jadi bisa langsung concat
    assert len(labels) == len(features), \
        f"Jumlah baris tidak sama! labels={len(labels)}, features={len(features)}"

    df = pd.concat([
        labels[["ROW_ID", "CLUSTER_KMEANS", "IS_OUTLIER"]].reset_index(drop=True),
        features.reset_index(drop=True)
    ], axis=1)

    log(f"  Gabungan         : {df.shape[0]:,} rows x {df.shape[1]} cols")
    return df


def compute_cluster_profiles(df: pd.DataFrame, df_full: pd.DataFrame = None) -> tuple[pd.DataFrame, pd.DataFrame]:
    # df_full dipakai untuk hitung std global — kalau None pakai df itu sendiri
    if df_full is None:
        df_full = df
    """
    Hitung statistik deskriptif per cluster untuk setiap fitur numerik.

    Untuk setiap fitur, kita hitung:
      - mean per cluster
      - std per cluster
      - perbedaan relatif vs mean keseluruhan (dalam %)
        → positif = cluster ini di atas rata-rata
        → negatif = cluster ini di bawah rata-rata

    Args:
        df : DataFrame gabungan (cluster + fitur)

    Returns:
        profiles : DataFrame mean per cluster, shape (n_clusters, n_features)
        rel_diff : DataFrame perbedaan relatif %, shape (n_clusters, n_features)
    """
    log("Menghitung profil cluster ...")

    # Kolom fitur numerik saja
    skip = ["ROW_ID", "CLUSTER_KMEANS", "CLUSTER_DBSCAN", "IS_OUTLIER"] + SKIP_COLS
    feature_cols = [c for c in df.columns if c not in skip
                    and pd.api.types.is_numeric_dtype(df[c])]

    log(f"  Jumlah fitur yang diprofil: {len(feature_cols)}")

    # Mean per cluster
    profiles = df.groupby("CLUSTER_KMEANS")[feature_cols].mean()

    # Mean keseluruhan (baseline)
    global_mean = df_full[feature_cols].mean()

    # Perbedaan relatif: (mean_cluster - mean_global) / std_global * 100
    # Pakai std global sebagai pembagi (bukan mean) supaya tidak meledak
    # ketika mean global mendekati 0.
    # Hasilnya = "berapa standar deviasi cluster ini di atas/bawah rata-rata"
    # dikali 100 supaya terbaca sebagai persentase standar deviasi
    global_std = df_full[feature_cols].std().replace(0, np.nan)
    rel_diff = profiles.sub(global_mean).div(global_std) * 100

    return profiles, rel_diff


def find_top_features(rel_diff: pd.DataFrame, top_n: int) -> dict:
    """
    Untuk setiap cluster, cari fitur yang paling membedakannya
    dari rata-rata keseluruhan.

    Fitur yang "paling membedakan" = fitur dengan |perbedaan relatif| terbesar.
    Dibagi dua arah:
      - Jauh di atas rata-rata (ciri khas positif cluster ini)
      - Jauh di bawah rata-rata (ciri khas negatif cluster ini)

    Args:
        rel_diff : DataFrame perbedaan relatif %
        top_n    : berapa fitur teratas yang diambil

    Returns:
        dict dengan key = cluster_id, value = DataFrame top features
    """
    top_features = {}

    for cluster_id in rel_diff.index:
        row = rel_diff.loc[cluster_id].abs().sort_values(ascending=False)
        top_cols = row.head(top_n).index.tolist()

        top_df = pd.DataFrame({
            "fitur"           : top_cols,
            "rel_diff_pct"    : rel_diff.loc[cluster_id, top_cols].values,
            "arah"            : ["LEBIH TINGGI" if v > 0 else "LEBIH RENDAH"
                                  for v in rel_diff.loc[cluster_id, top_cols].values],
        }).sort_values("rel_diff_pct", key=abs, ascending=False)

        top_features[cluster_id] = top_df

    return top_features


def print_cluster_profiles(
    df: pd.DataFrame,
    profiles: pd.DataFrame,
    top_features: dict,
):
    """
    Print ringkasan profil tiap cluster ke terminal.

    Untuk setiap cluster ditampilkan:
      - Jumlah dan persentase applicant
      - 10 fitur yang paling membedakannya
      - Interpretasi bisnis awal (berdasarkan pola fitur)

    Args:
        df          : DataFrame gabungan (untuk hitung distribusi)
        profiles    : mean per cluster
        top_features: dict top fitur per cluster
    """
    total = len(df)
    n_clusters = df["CLUSTER_KMEANS"].nunique()

    print()
    print("=" * 65)
    print("RINGKASAN PROFIL CLUSTER")
    print("=" * 65)

    for cluster_id in sorted(top_features.keys()):
        n_members = (df["CLUSTER_KMEANS"] == cluster_id).sum()
        pct       = n_members / total * 100

        print(f"\n{'─' * 65}")
        print(f"  CLUSTER {cluster_id}  —  {n_members:,} applicants ({pct:.1f}%)")
        print(f"{'─' * 65}")
        print(f"  {'FITUR':45s} {'DIFF%':>8}  {'ARAH'}")
        print(f"  {'-'*45} {'-'*8}  {'-'*12}")

        top_df = top_features[cluster_id]
        for _, row in top_df.iterrows():
            arrow = "▲" if row["arah"] == "LEBIH TINGGI" else "▼"
            print(f"  {row['fitur']:45s} {row['rel_diff_pct']:>+7.1f}%  {arrow} {row['arah']}")

    print(f"\n{'=' * 65}")


def plot_top_features(
    rel_diff: pd.DataFrame,
    top_features: dict,
    save_path: str,
):
    """
    Plot bar chart horizontal untuk top fitur tiap cluster.

    Setiap subplot = satu cluster.
    Bar hijau = fitur di atas rata-rata global.
    Bar merah = fitur di bawah rata-rata global.

    Args:
        rel_diff   : DataFrame perbedaan relatif %
        top_features: dict top fitur per cluster
        save_path  : path simpan gambar
    """
    n_clusters = len(top_features)
    fig, axes  = plt.subplots(1, n_clusters, figsize=(6 * n_clusters, 8))

    if n_clusters == 1:
        axes = [axes]

    for ax, cluster_id in zip(axes, sorted(top_features.keys())):
        top_df  = top_features[cluster_id].head(TOP_N_FEATURES)
        values  = top_df["rel_diff_pct"].values
        labels  = top_df["fitur"].values
        colors  = ["#059669" if v > 0 else "#DC2626" for v in values]

        bars = ax.barh(range(len(values)), values, color=colors, alpha=0.8)
        ax.set_yticks(range(len(values)))
        ax.set_yticklabels(labels, fontsize=9)
        ax.axvline(x=0, color="black", linewidth=0.8)
        ax.set_xlabel("Perbedaan dari rata-rata global (%)")
        ax.set_title(f"Cluster {cluster_id}", fontsize=13, fontweight="bold")
        ax.invert_yaxis()

        # Tambahkan nilai di ujung bar
        for bar, val in zip(bars, values):
            x_pos = val + (2 if val >= 0 else -2)
            ax.text(x_pos, bar.get_y() + bar.get_height()/2,
                    f"{val:+.0f}%", va="center", fontsize=8,
                    ha="left" if val >= 0 else "right")

    plt.suptitle(
        "Cluster Profiles — Top Differentiating Features\n(% perbedaan dari rata-rata global)",
        fontsize=14, fontweight="bold"
    )
    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches="tight")
    plt.close()
    log(f"  Plot tersimpan: '{save_path}'")


def save_outputs(
    profiles : pd.DataFrame,
    rel_diff : pd.DataFrame,
    top_features: dict,
):
    """
    Simpan semua output ke CSV.

    File yang dihasilkan:
      cluster_profiles.csv  → mean semua fitur per cluster (lengkap)
      cluster_summary.csv   → top N fitur per cluster (ringkasan)

    Args:
        profiles    : mean per cluster
        rel_diff    : perbedaan relatif %
        top_features: dict top fitur per cluster
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 1. Profil lengkap — mean semua fitur per cluster
    profiles.to_csv(os.path.join(OUTPUT_DIR, "cluster_profiles.csv"))
    log(f"  cluster_profiles.csv tersimpan")

    # 2. Ringkasan — top fitur per cluster (untuk laporan)
    summary_rows = []
    for cluster_id, top_df in top_features.items():
        for _, row in top_df.iterrows():
            summary_rows.append({
                "cluster_id"   : cluster_id,
                "fitur"        : row["fitur"],
                "rel_diff_pct" : round(row["rel_diff_pct"], 2),
                "arah"         : row["arah"],
            })
    summary_df = pd.DataFrame(summary_rows)
    summary_df.to_csv(os.path.join(OUTPUT_DIR, "cluster_summary.csv"), index=False)
    log(f"  cluster_summary.csv tersimpan")


# ── Main ───────────────────────────────────────────────────────────────────

def run():
    """
    Jalankan seluruh pipeline profiling:
      1. Load dan gabungkan data
      2. Hitung statistik per cluster
      3. Identifikasi top fitur per cluster
      4. Print ringkasan ke terminal
      5. Plot visualisasi
      6. Simpan output
    """
    log("=" * 55)
    log("STEP 4 — CLUSTER PROFILING")
    log("=" * 55)

    # 1. Load
    df = load_data()

    # Distribusi cluster
    log("\nDistribusi cluster:")
    dist = df["CLUSTER_KMEANS"].value_counts().sort_index()
    for cid, cnt in dist.items():
        log(f"  Cluster {cid}: {cnt:,} ({cnt/len(df)*100:.1f}%)")

    # 2. Hitung profil
    profiles, rel_diff = compute_cluster_profiles(df)

    # 3. Top fitur per cluster
    top_features = find_top_features(rel_diff, TOP_N_FEATURES)

    # 4. Print ke terminal
    print_cluster_profiles(df, profiles, top_features)

    # 5. Plot
    log("\nMembuat plot ...")
    plot_top_features(
        rel_diff, top_features,
        save_path=os.path.join(OUTPUT_DIR, "cluster_profile_plot.png")
    )

    # 6. Simpan
    log("\nMenyimpan output ...")
    save_outputs(profiles, rel_diff, top_features)

    log("\n✅ Step 4 selesai!")
    log("Output files:")
    log("  - datasets/final/cluster_profiles.csv     → statistik lengkap")
    log("  - datasets/final/cluster_summary.csv      → top fitur per cluster")
    log("  - datasets/final/cluster_profile_plot.png → visualisasi bar chart")
    log("")
    log("Buka cluster_summary.csv dan cluster_profile_plot.png")
    log("untuk interpretasi bisnis tiap cluster.")


if __name__ == "__main__":
    run()
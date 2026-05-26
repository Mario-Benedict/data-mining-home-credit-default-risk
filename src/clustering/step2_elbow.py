"""
Step 2 — Elbow Method & Silhouette Score
=========================================
Tujuan:
  - Cari nilai K optimal untuk K-Means clustering
  - Pakai dua metode sekaligus: Elbow Method + Silhouette Score
  - Jalankan di sample data dulu (bukan full 355K) biar cepet di laptop

Dua metode yang dipakai:
  1. Elbow Method
     → Plot inertia (total jarak tiap point ke centroid cluster-nya)
     → Cari titik "siku" di mana penambahan K sudah tidak banyak
       mengurangi inertia — itulah K optimal

  2. Silhouette Score
     → Mengukur seberapa "pas" tiap data point di cluster-nya
     → Nilai antara -1 sampai 1:
         1.0  = sangat bagus (point jauh dari cluster lain)
         0.0  = ambigu (point di batas antar cluster)
        -1.0  = salah cluster (lebih dekat ke cluster lain)
     → Pilih K dengan silhouette score tertinggi

Jalankan di: Laptop (VS Code)
Input : datasets/final/features_pca50.csv
Output:
  - datasets/final/elbow_plot.png        → grafik elbow method
  - datasets/final/silhouette_plot.png   → grafik silhouette score
  - datasets/final/k_selection.csv       → tabel inertia + silhouette per K
"""

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import os
import time

# ── Konfigurasi ────────────────────────────────────────────────────────────

INPUT_PATH  = "datasets/final/features_pca50.csv"
OUTPUT_DIR  = "datasets/final"

# Berapa komponen PCA yang dipakai
# → Hasil Step 1: 28 komponen = 90% variance, kita pakai 30 biar aman
N_COMPONENTS = 30

# Range K yang akan dicoba (dari 2 sampai 12)
K_MIN = 2
K_MAX = 12

# Jumlah sample untuk Elbow & Silhouette
# → None  = pakai semua data (lebih akurat, tapi lebih lama)
# → angka = pakai sebanyak itu saja, misal: 20_000
SAMPLE_SIZE = None

# Random seed biar hasilnya reproducible (sama setiap kali dijalankan)
RANDOM_SEED = 42


# ── Helper Functions ───────────────────────────────────────────────────────

def log(msg: str):
    """Print pesan dengan format yang rapi."""
    print(f"[ELBOW] {msg}")


def load_and_prepare(path: str, n_components: int, sample_size) -> np.ndarray:
    """
    Load PCA result, ambil N komponen pertama, lalu sample.

    Args:
        path        : path ke features_pca50.csv
        n_components: jumlah komponen PCA yang dipakai (misal: 30)
        sample_size : jumlah baris yang di-sample
                      → None  = pakai semua data
                      → angka = pakai sebanyak itu, misal 20_000

    Returns:
        X_sample : numpy array shape (sample_size, n_components)
    """
    log(f"Loading '{path}' ...")
    df = pd.read_csv(path)
    log(f"  Shape asli: {df.shape[0]:,} rows x {df.shape[1]:,} cols")

    # Ambil kolom PC1 sampai PC{n_components} saja
    pc_cols = [f"PC{i+1}" for i in range(n_components)]
    # Pastikan kolom yang diminta ada di file
    pc_cols = [c for c in pc_cols if c in df.columns]
    log(f"  Menggunakan {len(pc_cols)} komponen PCA: {pc_cols[0]} s/d {pc_cols[-1]}")

    # Sample acak — kalau None, pakai semua data
    if sample_size is None:
        df_sample = df[pc_cols]
        log(f"  Sample size: semua data ({len(df_sample):,} rows)")
    else:
        df_sample = df[pc_cols].sample(n=min(sample_size, len(df)), random_state=RANDOM_SEED)
        log(f"  Sample size: {len(df_sample):,} rows")

    return df_sample.values


def run_elbow_and_silhouette(X: np.ndarray, k_min: int, k_max: int) -> pd.DataFrame:
    """
    Jalankan KMeans untuk setiap K dan catat inertia + silhouette score.

    Proses:
      Untuk setiap nilai K dari k_min sampai k_max:
        1. Fit KMeans dengan K cluster
        2. Catat inertia (total within-cluster sum of squares)
        3. Hitung silhouette score dari hasil clustering

    Args:
        X     : numpy array fitur
        k_min : K terkecil yang dicoba
        k_max : K terbesar yang dicoba

    Returns:
        DataFrame dengan kolom: k, inertia, silhouette_score, waktu_detik
    """
    results = []
    total_k = k_max - k_min + 1

    log(f"\nMenjalankan KMeans untuk K = {k_min} sampai {k_max} ...")
    log(f"  (ini butuh beberapa menit, sabar ya)\n")

    for k in range(k_min, k_max + 1):
        start = time.time()

        # Fit KMeans
        # n_init=10 → coba 10 inisialisasi berbeda, ambil yang terbaik
        # max_iter=300 → maksimal iterasi per run
        kmeans = KMeans(n_clusters=k, n_init=10, max_iter=300, random_state=RANDOM_SEED)
        labels = kmeans.fit_predict(X)

        inertia = kmeans.inertia_

        # Silhouette score butuh minimal 2 cluster dan semua cluster terisi
        sil_score = silhouette_score(X, labels, sample_size=5_000, random_state=RANDOM_SEED)

        elapsed = time.time() - start

        results.append({
            "k"               : k,
            "inertia"         : inertia,
            "silhouette_score": sil_score,
            "waktu_detik"     : round(elapsed, 2),
        })

        # Progress log
        bar = "█" * k + "░" * (total_k - (k - k_min + 1))
        log(f"  K={k:2d} | inertia={inertia:12.1f} | silhouette={sil_score:.4f} | {elapsed:.1f}s [{bar}]")

    return pd.DataFrame(results)


def find_elbow(inertias: list) -> int:
    """
    Cari titik elbow secara otomatis menggunakan metode jarak ke garis lurus.

    Cara kerja:
      - Tarik garis lurus dari titik pertama ke titik terakhir
      - Hitung jarak tegak lurus setiap titik ke garis tersebut
      - Titik dengan jarak terbesar = elbow

    Args:
        inertias : list nilai inertia untuk setiap K

    Returns:
        index titik elbow (0-based dari list inertias)
    """
    n = len(inertias)
    # Koordinat titik pertama dan terakhir
    p1 = np.array([0, inertias[0]])
    p2 = np.array([n - 1, inertias[-1]])

    # Hitung jarak tegak lurus setiap titik ke garis p1-p2
    distances = []
    for i, val in enumerate(inertias):
        p = np.array([i, val])
        # Rumus jarak titik ke garis
        d = np.abs(np.cross(p2 - p1, p1 - p)) / np.linalg.norm(p2 - p1)
        distances.append(d)

    return int(np.argmax(distances))


def plot_elbow(df_results: pd.DataFrame, elbow_k: int, save_path: str):
    """
    Plot grafik Elbow Method.

    Sumbu X = nilai K
    Sumbu Y = inertia
    Titik elbow ditandai dengan lingkaran merah

    Args:
        df_results : DataFrame hasil run_elbow_and_silhouette
        elbow_k    : nilai K yang terdeteksi sebagai elbow
        save_path  : path untuk simpan gambar
    """
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(df_results["k"], df_results["inertia"],
            marker="o", linewidth=2, color="#2563EB", markersize=6, label="Inertia")

    # Tandai titik elbow
    elbow_row = df_results[df_results["k"] == elbow_k].iloc[0]
    ax.scatter(elbow_row["k"], elbow_row["inertia"],
               color="red", s=150, zorder=5, label=f"Elbow → K={elbow_k}")

    ax.set_xlabel("Jumlah Cluster (K)", fontsize=12)
    ax.set_ylabel("Inertia (Within-Cluster Sum of Squares)", fontsize=12)
    ax.set_title("Elbow Method — Cari K Optimal", fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
    log(f"  Plot elbow tersimpan: '{save_path}'")


def plot_silhouette(df_results: pd.DataFrame, best_k: int, save_path: str):
    """
    Plot grafik Silhouette Score.

    Sumbu X = nilai K
    Sumbu Y = silhouette score (makin tinggi makin bagus)
    Titik terbaik ditandai dengan lingkaran hijau

    Args:
        df_results : DataFrame hasil run_elbow_and_silhouette
        best_k     : nilai K dengan silhouette score tertinggi
        save_path  : path untuk simpan gambar
    """
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(df_results["k"], df_results["silhouette_score"],
            marker="o", linewidth=2, color="#059669", markersize=6, label="Silhouette Score")

    # Tandai K terbaik
    best_row = df_results[df_results["k"] == best_k].iloc[0]
    ax.scatter(best_row["k"], best_row["silhouette_score"],
               color="red", s=150, zorder=5, label=f"Best K → {best_k}")

    ax.set_xlabel("Jumlah Cluster (K)", fontsize=12)
    ax.set_ylabel("Silhouette Score", fontsize=12)
    ax.set_title("Silhouette Score — Makin Tinggi Makin Bagus", fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
    log(f"  Plot silhouette tersimpan: '{save_path}'")


# ── Main ───────────────────────────────────────────────────────────────────

def run():
    """
    Jalankan seluruh pipeline Elbow + Silhouette:
      1. Load PCA data dan ambil sample
      2. Jalankan KMeans untuk K=2 sampai K=12
      3. Plot Elbow Method
      4. Plot Silhouette Score
      5. Rekomendasikan K terbaik
    """
    log("=" * 55)
    log("STEP 2 — Elbow Method & Silhouette Score")
    log("=" * 55)

    # 1. Load data
    X = load_and_prepare(INPUT_PATH, N_COMPONENTS, SAMPLE_SIZE)

    # 2. Jalankan Elbow + Silhouette
    df_results = run_elbow_and_silhouette(X, K_MIN, K_MAX)

    # 3. Simpan tabel hasil
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    table_path = os.path.join(OUTPUT_DIR, "k_selection.csv")
    df_results.to_csv(table_path, index=False)
    log(f"\nTabel hasil tersimpan: '{table_path}'")

    # 4. Cari K optimal dari dua metode
    elbow_idx = find_elbow(df_results["inertia"].tolist())
    elbow_k   = df_results.iloc[elbow_idx]["k"]
    best_sil_k = df_results.loc[df_results["silhouette_score"].idxmax(), "k"]

    # 5. Plot
    log("\nMembuat plot ...")
    plot_elbow(
        df_results, elbow_k,
        save_path=os.path.join(OUTPUT_DIR, "elbow_plot.png")
    )
    plot_silhouette(
        df_results, best_sil_k,
        save_path=os.path.join(OUTPUT_DIR, "silhouette_plot.png")
    )

    # 6. Rekomendasikan K
    log("\n" + "=" * 55)
    log("HASIL ANALISIS K OPTIMAL")
    log("=" * 55)
    log(f"  Elbow Method    → K = {int(elbow_k)}")
    log(f"  Silhouette Score → K = {int(best_sil_k)}")

    if elbow_k == best_sil_k:
        log(f"\n  ✅ Kedua metode sepakat: gunakan K = {int(elbow_k)}")
        recommended_k = int(elbow_k)
    else:
        # Kalau beda, ambil rata-rata atau yang lebih masuk akal
        recommended_k = int(elbow_k)   # elbow biasanya lebih konservatif
        log(f"\n  ⚠️  Kedua metode beda hasil.")
        log(f"      Rekomendasi: gunakan K = {recommended_k} (dari Elbow)")
        log(f"      Tapi coba juga K = {int(best_sil_k)} (dari Silhouette)")
        log(f"      → Lihat grafik dan diskusi dengan tim!")

    log(f"\n  📌 Catat nilai K ini — akan dipakai di Step 3 (K-Means di Colab)")
    log("\n✅ Step 2 selesai!")


if __name__ == "__main__":
    run()
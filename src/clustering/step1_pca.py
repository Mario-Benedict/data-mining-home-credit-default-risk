"""
Step 1 — Principal Component Analysis (PCA)
============================================
Tujuan:
  - Kurangi dimensi dari ~200 fitur → 50 komponen (untuk clustering)
  - Kurangi dimensi → 2 komponen (untuk visualisasi 2D)
  - Simpan hasil PCA ke CSV biar bisa dipakai di Colab nanti

Kenapa PCA dulu sebelum clustering?
  - 200 fitur itu terlalu banyak → "curse of dimensionality"
  - Distance metric (Euclidean) jadi tidak akurat kalau fiturnya terlalu banyak
  - PCA kompres informasi penting ke lebih sedikit dimensi
  - Clustering jadi lebih cepat dan lebih akurat

Jalankan di: Laptop (VS Code)
Output:
  - datasets/final/features_pca50.csv   → dipakai untuk clustering
  - datasets/final/features_pca2.csv    → dipakai untuk visualisasi
  - datasets/final/pca_variance.csv     → info berapa % variansi tiap komponen
"""

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import os

# ── Konfigurasi ────────────────────────────────────────────────────────────

# Sesuaikan path ini dengan lokasi file di laptop lo
INPUT_PATH  = "datasets/final/features_clustering.csv"
OUTPUT_DIR  = "datasets/final"

# Jumlah komponen PCA
N_COMPONENTS_CLUSTERING = 10   # untuk clustering (K-Means, DBSCAN, Hierarchical)
N_COMPONENTS_VIZ        = 2    # untuk visualisasi 2D scatter plot

# Berapa baris yang dibaca saat testing (None = baca semua)
# Kalau mau test dulu pakai: DEBUG_ROWS = 10_000
DEBUG_ROWS = None


# ── Helper Functions ───────────────────────────────────────────────────────

def log(msg: str):
    """Print pesan dengan format yang rapi."""
    print(f"[PCA] {msg}")


def load_data(path: str, nrows=None) -> pd.DataFrame:
    """
    Load file CSV features_clustering.csv.

    Args:
        path   : path ke file CSV
        nrows  : jumlah baris yang dibaca (None = semua)

    Returns:
        DataFrame yang sudah di-load
    """
    log(f"Loading data dari '{path}' ...")
    df = pd.read_csv(path, nrows=nrows)
    log(f"  Shape: {df.shape[0]:,} rows × {df.shape[1]:,} cols")
    return df


def prepare_features(df: pd.DataFrame) -> tuple[np.ndarray, list[str]]:
    """
    Pisahkan ID dari fitur numerik.

    SK_ID_CURR adalah identifier, bukan fitur — harus dikeluarkan
    sebelum PCA supaya tidak mempengaruhi hasil.

    Args:
        df : DataFrame hasil load

    Returns:
        X          : numpy array fitur (tanpa ID)
        feature_cols: list nama kolom fitur
    """
    # Kolom yang bukan fitur (identifier)
    id_cols = ["SK_ID_CURR"]
    feature_cols = [c for c in df.columns if c not in id_cols]

    log(f"Jumlah fitur untuk PCA: {len(feature_cols)}")

    X = df[feature_cols].values
    return X, feature_cols


def run_pca(X: np.ndarray, n_components: int, label: str) -> tuple[np.ndarray, PCA]:
    """
    Jalankan PCA dengan n_components komponen.

    Args:
        X            : numpy array fitur
        n_components : jumlah komponen PCA yang diinginkan
        label        : nama untuk logging (misal: "50-component", "2-component")

    Returns:
        X_pca : hasil transformasi PCA
        pca   : objek PCA yang sudah di-fit (untuk analisis variance)
    """
    log(f"Menjalankan PCA ({label}) ...")
    pca = PCA(n_components=n_components, random_state=42)
    X_pca = pca.fit_transform(X)

    total_variance = pca.explained_variance_ratio_.sum() * 100
    log(f"  {n_components} komponen menjelaskan {total_variance:.1f}% total variansi")

    return X_pca, pca


def save_pca_result(
    df_original: pd.DataFrame,
    X_pca: np.ndarray,
    n_components: int,
    output_path: str
):
    """
    Gabungkan hasil PCA dengan SK_ID_CURR lalu simpan ke CSV.

    Kenapa SK_ID_CURR disimpan?
    → Biar nanti hasil cluster bisa di-join balik ke data original

    Args:
        df_original  : DataFrame original (berisi SK_ID_CURR)
        X_pca        : hasil transformasi PCA
        n_components : jumlah komponen
        output_path  : path file output CSV
    """
    # Buat nama kolom: PC1, PC2, ..., PC50
    pc_cols = [f"PC{i+1}" for i in range(n_components)]

    df_pca = pd.DataFrame(X_pca, columns=pc_cols)

    # Tambahkan ID di kolom pertama
    # Kalau SK_ID_CURR ada → pakai itu
    # Kalau tidak ada → buat ROW_ID (0, 1, 2, ...) sebagai pengganti
    if "SK_ID_CURR" in df_original.columns:
        df_pca.insert(0, "SK_ID_CURR", df_original["SK_ID_CURR"].values)
    else:
        # Pipeline Phase 1 tidak menyimpan SK_ID_CURR — buat ROW_ID pengganti
        # ROW_ID = nomor baris, dipakai untuk join hasil cluster nanti
        df_pca.insert(0, "ROW_ID", np.arange(len(df_pca)))
        log("  Catatan: SK_ID_CURR tidak ditemukan → pakai ROW_ID sebagai pengganti")

    df_pca.to_csv(output_path, index=False)
    log(f"  Tersimpan: '{output_path}' — shape: {df_pca.shape}")


def save_variance_info(pca: PCA, output_path: str):
    """
    Simpan informasi explained variance ke CSV.

    Berguna untuk:
    - Memilih berapa komponen yang optimal
    - Membuat plot cumulative variance

    Args:
        pca         : objek PCA yang sudah di-fit
        output_path : path file output CSV
    """
    variance_df = pd.DataFrame({
        "component"              : [f"PC{i+1}" for i in range(len(pca.explained_variance_ratio_))],
        "explained_variance_ratio": pca.explained_variance_ratio_,
        "cumulative_variance"    : pca.explained_variance_ratio_.cumsum(),
    })
    variance_df.to_csv(output_path, index=False)
    log(f"  Variance info tersimpan: '{output_path}'")


def plot_cumulative_variance(pca: PCA, save_path: str = None):
    """
    Plot grafik cumulative explained variance.

    Grafik ini membantu lo memutuskan berapa komponen yang cukup.
    Biasanya pilih komponen di mana cumulative variance ≥ 80-90%.

    Args:
        pca       : objek PCA yang sudah di-fit (50-component)
        save_path : path untuk simpan gambar (None = hanya ditampilkan)
    """
    cumulative = pca.explained_variance_ratio_.cumsum() * 100
    n = len(cumulative)

    plt.figure(figsize=(10, 5))
    plt.plot(range(1, n + 1), cumulative, marker="o", markersize=3, linewidth=2, color="#2563EB")
    plt.axhline(y=80, color="orange", linestyle="--", label="80% threshold")
    plt.axhline(y=90, color="red",    linestyle="--", label="90% threshold")
    plt.xlabel("Jumlah Komponen PCA")
    plt.ylabel("Cumulative Explained Variance (%)")
    plt.title("PCA — Cumulative Explained Variance")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150)
        log(f"  Plot tersimpan: '{save_path}'")
    else:
        plt.show()


# ── Main ───────────────────────────────────────────────────────────────────

def run():
    """
    Jalankan seluruh pipeline PCA:
      1. Load data
      2. PCA 50 komponen → untuk clustering di Colab
      3. PCA 2 komponen  → untuk visualisasi
      4. Simpan semua output
      5. Plot variance chart
    """
    log("=" * 55)
    log("STEP 1 — PCA (Principal Component Analysis)")
    log("=" * 55)

    # 1. Load data
    df = load_data(INPUT_PATH, nrows=DEBUG_ROWS)

    # 2. Pisahkan fitur dari ID
    X, feature_cols = prepare_features(df)

    # 3. PCA 50 komponen (untuk clustering)
    X_pca50, pca50 = run_pca(X, N_COMPONENTS_CLUSTERING, "50-component")

    # 4. PCA 2 komponen (untuk visualisasi)
    #    Catatan: fit ulang dari data asli, bukan dari hasil PCA-50
    X_pca2, pca2 = run_pca(X, N_COMPONENTS_VIZ, "2-component")

    # 5. Simpan hasil
    log("\nMenyimpan output ...")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    save_pca_result(
        df, X_pca50, N_COMPONENTS_CLUSTERING,
        os.path.join(OUTPUT_DIR, "features_pca10.csv")
    )
    save_pca_result(
        df, X_pca2, N_COMPONENTS_VIZ,
        os.path.join(OUTPUT_DIR, "features_pca2.csv")
    )
    save_variance_info(
        pca50,
        os.path.join(OUTPUT_DIR, "pca_variance.csv")
    )

    # 6. Plot cumulative variance
    log("\nMembuat plot variance ...")
    plot_cumulative_variance(
        pca50,
        save_path=os.path.join(OUTPUT_DIR, "pca_variance_plot.png")
    )

    log("\n✅ Step 1 selesai!")
    log(f"   Output files:")
    log(f"   - datasets/final/features_pca50.csv   → upload ke Colab untuk clustering")
    log(f"   - datasets/final/features_pca2.csv    → untuk visualisasi scatter plot")
    log(f"   - datasets/final/pca_variance.csv     → info variance tiap komponen")
    log(f"   - datasets/final/pca_variance_plot.png → grafik cumulative variance")


if __name__ == "__main__":
    run()
"""
Step 5 — Business Interpretation & Final Report
=================================================
Tujuan:
  - Menetapkan nama bisnis untuk tiap cluster
  - Mencetak ringkasan interpretasi bisnis yang siap digunakan di laporan
  - Menyimpan laporan teks final ke file

Input:
  - datasets/final/cluster_summary.csv   (top fitur per cluster)
  - datasets/final/cluster_profiles.csv  (mean fitur per cluster)
  - datasets/final/cluster_labels.csv    (distribusi cluster)

Output:
  - datasets/final/business_report.txt   (laporan teks final)

Jalankan di: Laptop (VS Code)
"""

import pandas as pd
import os

# ── Konfigurasi ────────────────────────────────────────────────────────────

SUMMARY_PATH  = "datasets/final/cluster_summary.csv"
PROFILES_PATH = "datasets/final/cluster_profiles.csv"
LABELS_PATH   = "datasets/final/cluster_labels.csv"
OUTPUT_DIR    = "datasets/final"

# ── Nama & Interpretasi Bisnis Tiap Cluster ────────────────────────────────
#
# Ditetapkan berdasarkan top 10 fitur pembeda dari Step 4.
# Format: cluster_id → (nama_pendek, nama_lengkap, deskripsi, risiko)

CLUSTER_PROFILES = {
    0: {
        "nama": "Veteran Aktif",
        "nama_lengkap": "Veteran Peminjam — Berpendapatan Tinggi, Sering Ditolak",
        "karakteristik": [
            "Banyak riwayat pengajuan kredit (PREV_COUNT +88.7%)",
            "Sering ditolak di masa lalu (PREV_REFUSED_COUNT +72.5%)",
            "Pendapatan di atas rata-rata (AMT_INCOME_TOTAL +69.9%)",
            "Aktif dicek di credit bureau (AMT_REQ_CREDIT_BUREAU_YEAR +69.1%)",
            "Riwayat panjang di produk POS (POS_MONTHS_COUNT +61.7%)",
            "Approval rate rendah (PREV_APPROVAL_RATE -52.6%)",
            "Banyak catatan di bureau kredit (BUREAU_COUNT +51.6%)",
            "Jumlah kredit & cicilan di atas rata-rata",
            "Utilisasi kartu kredit rendah (CC_UTILIZATION_MAX -37.8%)",
        ],
        "interpretasi": (
            "Kelompok ini terdiri dari peminjam berpengalaman dengan pendapatan tinggi "
            "yang secara aktif dan agresif mencari kredit. Meskipun penghasilan tinggi, "
            "mereka sering ditolak — kemungkinan karena rasio hutang-terhadap-kredit "
            "yang bermasalah atau terlalu sering mengajukan kredit dalam waktu singkat. "
            "Utilisasi CC yang rendah menunjukkan mereka mengelola kartu kredit dengan baik, "
            "namun histori penolakan yang tinggi menandakan profil risiko yang perlu diperhatikan."
        ),
        "profil_risiko": "SEDANG-TINGGI",
        "rekomendasi": (
            "Evaluasi lebih lanjut alasan penolakan historis. Cocok untuk produk kredit "
            "berjaminan (mortgage) mengingat pendapatan tinggi, namun perlu verifikasi "
            "debt-to-income ratio secara ketat."
        ),
    },
    1: {
        "nama": "Peminjam Minimal",
        "nama_lengkap": "Peminjam Sederhana — Berpendapatan Rendah, Kredit Kecil",
        "karakteristik": [
            "Jumlah kredit jauh di bawah rata-rata (AMT_CREDIT -101.7%)",
            "Cicilan sangat rendah (AMT_ANNUITY -91.0%)",
            "Rasio kredit-per-pendapatan rendah (CREDIT_TO_INCOME -68.1%)",
            "Tenor pinjaman pendek (CREDIT_TERM_MONTHS -59.1%)",
            "Pendapatan di bawah rata-rata (AMT_INCOME_TOTAL -41.2%)",
            "Tidak banyak menggunakan kartu kredit (CC_MONTHS_COUNT -32.4%)",
            "Utilisasi CC juga rendah (CC_UTILIZATION_MAX -41.6%)",
        ],
        "interpretasi": (
            "Kelompok terbesar kedua (32%) yang didominasi oleh peminjam berpendapatan rendah "
            "dengan kebutuhan kredit minimal. Mereka meminjam dalam jumlah kecil dengan tenor "
            "pendek — kemungkinan untuk kebutuhan konsumsi sehari-hari atau darurat kecil. "
            "Tidak aktif menggunakan kartu kredit menunjukkan keterbatasan akses produk keuangan. "
            "Profil risiko relatif rendah karena exposure kecil, namun kapasitas bayar terbatas "
            "jika terjadi guncangan pendapatan."
        ),
        "profil_risiko": "RENDAH-SEDANG",
        "rekomendasi": (
            "Segmen ideal untuk produk micro-credit atau kredit multiguna kecil. "
            "Prioritaskan edukasi keuangan dan program inklusi untuk mendorong "
            "peningkatan kapasitas finansial. Pemantauan ringan cukup memadai."
        ),
    },
    2: {
        "nama": "Pengguna CC Intensif",
        "nama_lengkap": "Pengguna Kartu Kredit Intensif — Revolving Credit Dependent",
        "karakteristik": [
            "Utilisasi CC maksimum sangat tinggi (CC_UTILIZATION_MAX +219.0%)",
            "Utilisasi CC rata-rata sangat tinggi (CC_UTILIZATION_MEAN +204.7%)",
            "Saldo kartu kredit besar (CC_AMT_BALANCE_MEAN +156.2%)",
            "Riwayat panjang penggunaan CC (CC_MONTHS_COUNT +151.5%)",
            "Aktif mengajukan kredit baru (PREV_COUNT +51.0%)",
            "Sering dicek di credit bureau (AMT_REQ_CREDIT_BUREAU_YEAR +49.1%)",
        ],
        "interpretasi": (
            "Kelompok ini sangat bergantung pada kredit berputar (revolving credit), "
            "terutama kartu kredit. Utilisasi CC lebih dari 2x rata-rata dengan saldo "
            "yang besar menunjukkan penggunaan CC mendekati atau melampaui limit. "
            "Riwayat CC yang panjang menandakan mereka adalah nasabah lama yang aktif. "
            "Namun ketergantungan tinggi pada revolving credit merupakan sinyal risiko: "
            "jika pendapatan terganggu, mereka berisiko default di banyak produk sekaligus."
        ),
        "profil_risiko": "SEDANG-TINGGI",
        "rekomendasi": (
            "Monitor utilisasi CC secara berkala. Pertimbangkan penawaran produk konsolidasi "
            "hutang untuk mengurangi ketergantungan CC. Batasi peningkatan limit kredit "
            "sampai utilisasi turun ke level yang lebih sehat (<70%)."
        ),
    },
    3: {
        "nama": "Peminjam Ambisius",
        "nama_lengkap": "Peminjam Kredit Besar Pertama Kali — Debt-to-Income Tinggi",
        "karakteristik": [
            "Rasio kredit-per-pendapatan sangat tinggi (CREDIT_TO_INCOME +75.3%)",
            "Jumlah kredit besar (AMT_CREDIT +68.6%)",
            "Cicilan besar relatif pendapatan (ANNUITY_TO_INCOME +67.5%)",
            "Cicilan nominal besar (AMT_ANNUITY +58.5%)",
            "Tenor panjang (CREDIT_TERM_MONTHS +44.9%)",
            "Sedikit riwayat pengajuan sebelumnya (PREV_COUNT -50.0%)",
            "Utilisasi CC rendah (CC_UTILIZATION_MAX -42.4%)",
            "Jarang dicek di credit bureau (AMT_REQ_CREDIT_BUREAU_YEAR -44.1%)",
        ],
        "interpretasi": (
            "Kelompok terbesar (32.9%) yang mengajukan pinjaman besar relative terhadap pendapatan "
            "mereka, dengan tenor yang panjang. Yang menarik: mereka memiliki sedikit riwayat "
            "pengajuan sebelumnya dan utilisasi CC yang rendah — menandakan ini mungkin peminjam "
            "pertama kali atau yang jarang mengakses kredit. Debt-to-income ratio yang tinggi "
            "adalah risiko utama: jika ada perubahan pendapatan, beban cicilan bisa menjadi berat."
        ),
        "profil_risiko": "SEDANG",
        "rekomendasi": (
            "Verifikasi stabilitas pendapatan sebelum persetujuan. Ideal untuk produk KPR "
            "atau kendaraan bermotor. Perlu stress-test kemampuan bayar pada skenario "
            "pendapatan berkurang 20-30%. Pertimbangkan asuransi jiwa/kesehatan sebagai syarat."
        ),
    },
    4: {
        "nama": "Peminjam Bermasalah",
        "nama_lengkap": "Peminjam Kronis Gagal Bayar — Profil Risiko Ekstrem",
        "karakteristik": [
            "Keterlambatan pembayaran ekstrem (INST_DPD_MAX +701.2%)",
            "Rasio keterlambatan parah sangat tinggi (INST_SEVERE_LATE_RATIO +547.0%)",
            "Rata-rata DPD installment sangat tinggi (INST_DPD_MEAN +477.9%)",
            "DPD di produk POS sangat tinggi (POS_SK_DPD_MEAN +423.3%)",
            "DPD di CC juga tinggi (CC_SK_DPD_MEAN +225.9%)",
            "Rasio keterlambatan umum tinggi (INST_LATE_RATIO +187.9%)",
            "Riwayat DPD parah di bureau (BUREAU_BB_SEVERE_DPD_MEAN +46.3%)",
        ],
        "interpretasi": (
            "Kelompok terkecil (hanya 1%) namun dengan profil risiko paling ekstrem. "
            "Days Past Due (DPD) mereka 7x lebih tinggi dari rata-rata di produk installment, "
            "dan gagal bayar tersebar di semua jenis produk: installment, POS, CC, dan bureau. "
            "Ini bukan sekadar keterlambatan sesekali — ini adalah pola gagal bayar yang kronis "
            "dan sistemik. Cluster ini merepresentasikan peminjam yang sudah dalam kondisi "
            "financial distress yang serius."
        ),
        "profil_risiko": "SANGAT TINGGI",
        "rekomendasi": (
            "Tolak pengajuan kredit baru atau terapkan syarat jaminan sangat ketat. "
            "Aktifkan proses restrukturisasi hutang untuk nasabah existing. "
            "Lakukan debt collection intensif. Flagging sebagai high-risk di sistem "
            "untuk monitoring prioritas."
        ),
    },
}

# ── DM Concepts ─────────────────────────────────────────────────────────────

DM_CONCEPTS = """
═══════════════════════════════════════════════════════════════════════════
PENJELASAN DATA MINING CONCEPTS — PHASE 2: CLUSTERING
═══════════════════════════════════════════════════════════════════════════

1. UNSUPERVISED PATTERN DISCOVERY
   ─────────────────────────────────
   Berbeda dengan supervised learning yang membutuhkan label (misal: default/non-default),
   clustering adalah teknik UNSUPERVISED — algoritma menemukan pola tersembunyi
   dari data itu sendiri tanpa arahan label. Dalam proyek ini, 356,255 peminjam
   dikelompokkan berdasarkan 67 fitur perilaku finansial, menghasilkan 5 segmen
   yang masing-masing memiliki karakteristik unik yang tidak terlihat sebelumnya.

2. DISTANCE METRICS
   ─────────────────
   K-Means menggunakan Euclidean Distance untuk mengukur kemiripan antar data poin.
   Setiap titik data ditetapkan ke cluster dengan centroid terdekat. Karena data
   berdimensi tinggi (67 fitur), dilakukan PCA untuk mereduksi ke 10 komponen
   utama — sehingga distance metric bekerja lebih efektif tanpa terdistorsi
   oleh the "curse of dimensionality".

   DBSCAN menggunakan konsep distance yang berbeda: eps = 3.5 mendefinisikan
   "radius ketetanggaan". Titik dengan min_samples ≥ 10 tetangga dalam radius itu
   adalah "core point". Titik yang tidak masuk radius manapun adalah outlier.

3. CLUSTER VALIDITY INDICES
   ──────────────────────────
   • Silhouette Score = 0.1348 (K-Means, K=5)
     Mengukur seberapa baik setiap data poin cocok di clusternya sendiri vs cluster
     lain. Rentang [-1, 1]; nilai 0.13 adalah wajar untuk data finansial berdimensi
     tinggi yang tidak memiliki pemisahan cluster yang tegas.

   • Inertia = 5,221,730
     Jumlah kuadrat jarak setiap poin ke centroid clusternya (within-cluster SSE).
     Digunakan dalam Elbow Method: nilai ini menurun semakin besar K, dan titik
     "siku" (K=5) dipilih sebagai K optimal.

   • Elbow Method → K = 5 (penurunan inertia mulai melandai di K=5)
   • Silhouette Score per K → puncak di K=2, namun K=5 dipilih karena lebih
     informatif secara bisnis.

4. DENDROGRAM ANALYSIS
   ──────────────────────
   Hierarchical Clustering dijalankan pada sampel 2,000 data menggunakan tiga
   metode linkage: Ward, Complete, dan Average. Dendrogram memvisualisasikan
   hierarki penggabungan cluster dari bawah (individual) ke atas (satu cluster besar).

   • Ward Linkage: meminimalkan variance dalam cluster → menghasilkan cluster
     berukuran seimbang, cocok untuk validasi K-Means.
   • Complete Linkage: menggunakan jarak maksimum antar cluster → menghasilkan
     cluster yang lebih kompak.
   • Average Linkage: kompromi antara Ward dan Complete.

   Ketiga metode konsisten menunjukkan 4–6 cluster utama, memvalidasi pilihan K=5
   dari K-Means.
"""


# ── Helper & Runner ─────────────────────────────────────────────────────────

def load_data():
    summary  = pd.read_csv(SUMMARY_PATH)
    labels   = pd.read_csv(LABELS_PATH)
    dist     = labels["CLUSTER_KMEANS"].value_counts().sort_index()
    total    = len(labels)
    return summary, dist, total


def build_report(dist, total) -> str:
    lines = []
    lines.append("=" * 75)
    lines.append("  PHASE 2 — SEGMENTATION VIA CLUSTERING")
    lines.append("  FINAL BUSINESS INTERPRETATION REPORT")
    lines.append("  Home Credit Default Risk Dataset")
    lines.append("=" * 75)
    lines.append("")
    lines.append("RINGKASAN EKSEKUTIF")
    lines.append("─" * 75)
    lines.append(f"  Total applicants : {total:,}")
    lines.append(f"  Jumlah cluster   : 5 (K-Means, PCA 10 komponen)")
    lines.append(f"  Silhouette Score : 0.1348  (wajar untuk data finansial)")
    lines.append(f"  Inertia          : 5,221,730")
    lines.append("")
    lines.append("  DISTRIBUSI CLUSTER:")
    for cid in sorted(dist.index):
        pct  = dist[cid] / total * 100
        name = CLUSTER_PROFILES[cid]["nama"]
        bar  = "#" * int(pct / 2)
        lines.append(f"  Cluster {cid} ({name:20s}): {dist[cid]:>7,} ({pct:5.1f}%) {bar}")
    lines.append("")

    for cid in sorted(CLUSTER_PROFILES.keys()):
        p    = CLUSTER_PROFILES[cid]
        n    = dist[cid]
        pct  = n / total * 100

        lines.append("=" * 75)
        lines.append(f"  CLUSTER {cid}  -->  \"{p['nama']}\"")
        lines.append(f"  {p['nama_lengkap']}")
        lines.append(f"  {n:,} applicants ({pct:.1f}%) | Profil Risiko: {p['profil_risiko']}")
        lines.append("─" * 75)

        lines.append("  KARAKTERISTIK UTAMA:")
        for k in p["karakteristik"]:
            lines.append(f"    • {k}")

        lines.append("")
        lines.append("  INTERPRETASI BISNIS:")
        for para in p["interpretasi"].split("\n"):
            lines.append(f"    {para.strip()}")

        lines.append("")
        lines.append("  REKOMENDASI:")
        for para in p["rekomendasi"].split("\n"):
            lines.append(f"    {para.strip()}")
        lines.append("")

    lines.append(DM_CONCEPTS)
    lines.append("=" * 75)
    lines.append("  END OF REPORT")
    lines.append("=" * 75)

    return "\n".join(lines)


def run():
    print("[REPORT] Memuat data ...")
    summary, dist, total = load_data()

    print("[REPORT] Membangun laporan ...")
    report = build_report(dist, total)

    print()
    print(report.encode("ascii", errors="replace").decode("ascii"))

    # Simpan ke file
    out_path = os.path.join(OUTPUT_DIR, "business_report.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\n[REPORT] SELESAI. Laporan tersimpan: '{out_path}'")


if __name__ == "__main__":
    run()
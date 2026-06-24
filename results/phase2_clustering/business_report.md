# Phase 2 — Segmentation via Clustering
**Dataset:** Home Credit Default Risk

---

## Ringkasan Eksekutif

| Metrik | Nilai |
|--------|-------|
| Total applicants | 356,255 |
| Jumlah cluster | 5 (K-Means) |
| Komponen PCA | 10 (52.1% variance) |
| Silhouette Score | 0.1468 |
| Inertia (K-Means) | 5,199,206.0 |
| K dari Elbow Method | 5 |
| K dari Silhouette | 2 |

Silhouette mengukur seberapa terpisah cluster satu sama lain (skala -1 sampai 1).
Untuk data finansial berdimensi tinggi, nilai 0,10-0,25 adalah rentang yang wajar;
silhouette tinggi mudah didapat dengan K=2, tetapi dua segmen terlalu kasar untuk dipakai bisnis.
Inertia hanya berguna untuk membandingkan antar-K, bukan sebagai angka absolut.

**Algoritma dijalankan:**

1. **K-Means** — full data, K=5 (segmentasi utama)
2. **DBSCAN** — sample 50K, `eps=3.0`, `min_samples=10` (outlier detection)
3. **Hierarchical** — BIRCH (500 micro-clusters) + Ward linkage

## Distribusi Cluster K-Means

| Cluster | Nama | Jumlah | Persentase | Profil Risiko |
|---------|------|--------|------------|---------------|
| 0 | Peminjam Bermasalah | 3,582 | 1.0% | sangat tinggi |
| 1 | Peminjam Ambisius | 125,071 | 35.1% | sedang |
| 2 | Veteran Aktif | 46,905 | 13.2% | sedang-tinggi |
| 3 | Pengguna CC Intensif | 54,215 | 15.2% | sedang-tinggi |
| 4 | Peminjam Minimal | 126,482 | 35.5% | rendah-sedang |

Nama segmen ditetapkan manusia setelah membaca 10 fitur paling menyimpang di tiap cluster.
Profil risiko di tabel ini adalah penilaian kualitatif tim; angka default aktual per segmen
dihitung terpisah di laporan validasi (TARGET tidak pernah dipakai saat clustering).

---

## Cluster 0 — Peminjam Bermasalah

> **Peminjam Kronis Gagal Bayar — Profil Risiko Ekstrem**  
> 3,582 applicants (1.0%) | Profil Risiko: sangat tinggi

### Karakteristik Utama

| Fitur & Nilai | Arah |
|---------------|------|
| `INST_DPD_MAX +692.7%` | ▲ LEBIH TINGGI |
| `INST_SEVERE_LATE_RATIO +549.1%` | ▲ LEBIH TINGGI |
| `INST_DPD_MEAN +473.4%` | ▲ LEBIH TINGGI |
| `POS_SK_DPD_MEAN +420.6%` | ▲ LEBIH TINGGI |
| `CC_SK_DPD_MEAN +212.9%` | ▲ LEBIH TINGGI |
| `INST_LATE_RATIO +190.4%` | ▲ LEBIH TINGGI |
| `POS_MONTHS_COUNT +93.0%` | ▲ LEBIH TINGGI |
| `BUREAU_BB_SEVERE_DPD_MEAN +49.1%` | ▲ LEBIH TINGGI |
| `BUREAU_BB_DPD_RATIO_MEAN +40.8%` | ▲ LEBIH TINGGI |
| `CC_MONTHS_COUNT +37.6%` | ▲ LEBIH TINGGI |

### Interpretasi Bisnis

Kelompok kecil namun profil risiko ekstrem. Days Past Due (DPD) berlipat ganda di multiple produk (installment, POS, CC) — pola gagal bayar kronis dan sistemik, bukan keterlambatan insidental. Mereka sudah dalam kondisi financial distress serius.

### Rekomendasi

> Tolak pengajuan baru atau syarat jaminan ketat. Aktifkan restrukturisasi hutang nasabah existing. Lakukan debt collection intensif. Flag sebagai high-risk monitoring prioritas.

---

## Cluster 1 — Peminjam Ambisius

> **Peminjam Kredit Besar — Debt-to-Income Tinggi**  
> 125,071 applicants (35.1%) | Profil Risiko: sedang

### Karakteristik Utama

| Fitur & Nilai | Arah |
|---------------|------|
| `AMT_CREDIT +83.3%` | ▲ LEBIH TINGGI |
| `CREDIT_TO_INCOME +74.0%` | ▲ LEBIH TINGGI |
| `AMT_ANNUITY +69.6%` | ▲ LEBIH TINGGI |
| `CREDIT_TERM_MONTHS +57.6%` | ▲ LEBIH TINGGI |
| `ANNUITY_TO_INCOME +56.9%` | ▲ LEBIH TINGGI |
| `CC_UTILIZATION_MAX -41.7%` | ▼ LEBIH RENDAH |
| `CC_UTILIZATION_MEAN -38.6%` | ▼ LEBIH RENDAH |
| `PREV_COUNT -37.7%` | ▼ LEBIH RENDAH |
| `AMT_REQ_CREDIT_BUREAU_YEAR -31.5%` | ▼ LEBIH RENDAH |
| `PREV_REFUSED_COUNT -30.4%` | ▼ LEBIH RENDAH |

### Interpretasi Bisnis

Mengajukan pinjaman besar relatif terhadap pendapatan dengan tenor panjang. Sedikit riwayat pengajuan sebelumnya + utilisasi CC rendah menandakan peminjam pertama kali. Debt-to-income tinggi adalah risiko utama: rentan terhadap guncangan pendapatan.

### Rekomendasi

> Verifikasi stabilitas pendapatan sebelum persetujuan. Ideal untuk KPR/kendaraan. Stress-test kemampuan bayar pada skenario pendapatan turun 20-30%. Pertimbangkan asuransi jiwa/kesehatan sebagai syarat.

---

## Cluster 2 — Veteran Aktif

> **Veteran Peminjam — Berpendapatan Tinggi, Sering Ditolak**  
> 46,905 applicants (13.2%) | Profil Risiko: sedang-tinggi

### Karakteristik Utama

| Fitur & Nilai | Arah |
|---------------|------|
| `PREV_COUNT +155.4%` | ▲ LEBIH TINGGI |
| `PREV_REFUSED_COUNT +134.1%` | ▲ LEBIH TINGGI |
| `AMT_REQ_CREDIT_BUREAU_YEAR +114.2%` | ▲ LEBIH TINGGI |
| `POS_MONTHS_COUNT +103.1%` | ▲ LEBIH TINGGI |
| `PREV_APPROVAL_RATE -72.9%` | ▼ LEBIH RENDAH |
| `BUREAU_COUNT +52.0%` | ▲ LEBIH TINGGI |
| `CREDIT_TO_INCOME -33.2%` | ▼ LEBIH RENDAH |
| `EXT_SOURCE_3 -33.1%` | ▼ LEBIH RENDAH |
| `CC_UTILIZATION_MEAN -30.2%` | ▼ LEBIH RENDAH |
| `CC_UTILIZATION_MAX -28.2%` | ▼ LEBIH RENDAH |

### Interpretasi Bisnis

Peminjam berpengalaman dengan pendapatan tinggi yang aktif & agresif mencari kredit. Meski pendapatan tinggi sering ditolak — kemungkinan rasio hutang-terhadap-kredit bermasalah atau over-application. Utilisasi CC rendah = mengelola CC dengan baik, namun histori penolakan tinggi = profil risiko perlu diperhatikan.

### Rekomendasi

> Evaluasi alasan penolakan historis. Cocok untuk kredit berjaminan (mortgage) mengingat pendapatan tinggi. Verifikasi debt-to-income ratio ketat.

---

## Cluster 3 — Pengguna CC Intensif

> **Pengguna Kartu Kredit Intensif — Revolving Credit Dependent**  
> 54,215 applicants (15.2%) | Profil Risiko: sedang-tinggi

### Karakteristik Utama

| Fitur & Nilai | Arah |
|---------------|------|
| `CC_UTILIZATION_MAX +218.8%` | ▲ LEBIH TINGGI |
| `CC_UTILIZATION_MEAN +205.6%` | ▲ LEBIH TINGGI |
| `CC_AMT_BALANCE_MEAN +157.7%` | ▲ LEBIH TINGGI |
| `CC_MONTHS_COUNT +152.2%` | ▲ LEBIH TINGGI |
| `AMT_REQ_CREDIT_BUREAU_YEAR +45.4%` | ▲ LEBIH TINGGI |
| `PREV_COUNT +41.9%` | ▲ LEBIH TINGGI |
| `POS_MONTHS_COUNT +27.0%` | ▲ LEBIH TINGGI |
| `NAME_CONTRACT_TYPE +26.0%` | ▲ LEBIH TINGGI |
| `AMT_INCOME_TOTAL +17.2%` | ▲ LEBIH TINGGI |
| `PREV_REFUSED_COUNT +16.7%` | ▲ LEBIH TINGGI |

### Interpretasi Bisnis

Sangat bergantung pada revolving credit (kartu kredit). Utilisasi CC jauh di atas rata-rata dengan saldo besar menunjukkan penggunaan mendekati atau melampaui limit. Riwayat CC panjang = nasabah lama yang aktif. Risiko: jika pendapatan terganggu, default berantai di banyak produk sekaligus.

### Rekomendasi

> Monitor utilisasi CC berkala. Tawarkan produk konsolidasi hutang. Batasi peningkatan limit kredit sampai utilisasi turun di bawah 70%.

---

## Cluster 4 — Peminjam Minimal

> **Peminjam Sederhana — Berpendapatan Rendah, Kredit Kecil**  
> 126,482 applicants (35.5%) | Profil Risiko: rendah-sedang

### Karakteristik Utama

| Fitur & Nilai | Arah |
|---------------|------|
| `AMT_CREDIT -83.6%` | ▼ LEBIH RENDAH |
| `AMT_ANNUITY -71.6%` | ▼ LEBIH RENDAH |
| `CREDIT_TO_INCOME -59.8%` | ▼ LEBIH RENDAH |
| `CREDIT_TERM_MONTHS -54.2%` | ▼ LEBIH RENDAH |
| `CC_UTILIZATION_MAX -42.5%` | ▼ LEBIH RENDAH |
| `ANNUITY_TO_INCOME -41.9%` | ▼ LEBIH RENDAH |
| `CC_UTILIZATION_MEAN -38.5%` | ▼ LEBIH RENDAH |
| `PREV_COUNT -37.9%` | ▼ LEBIH RENDAH |
| `CC_MONTHS_COUNT -34.2%` | ▼ LEBIH RENDAH |
| `NAME_CONTRACT_TYPE -33.9%` | ▼ LEBIH RENDAH |

### Interpretasi Bisnis

Peminjam berpendapatan rendah dengan kebutuhan kredit minimal. Pinjaman kecil tenor pendek — kemungkinan konsumsi sehari-hari atau darurat. Tidak aktif CC menunjukkan keterbatasan akses produk keuangan. Exposure kecil = risiko rendah, namun kapasitas bayar terbatas saat ada guncangan.

### Rekomendasi

> Segmen ideal micro-credit atau multiguna kecil. Prioritaskan edukasi keuangan & program inklusi. Pemantauan ringan cukup memadai.

---

## Data Mining Concepts — Phase 2

### 1. Unsupervised Pattern Discovery
Tidak ada label TARGET digunakan saat training. Algoritma menemukan grouping dari struktur 47 fitur behavioral saja.

### 2. Distance Metrics
- **K-Means**: Euclidean distance di ruang PCA 10-komponen (curse-of-dim teratasi).
- **DBSCAN**: `eps=3.0` = radius neighborhood; `min_samples=10` = density threshold.

### 3. Cluster Validity Indices

| Indeks | Nilai | Keterangan |
|--------|-------|------------|
| Silhouette Score | 0.1468 | Wajar untuk financial data berdimensi tinggi |
| Inertia (WCSS) | 5,199,206.0 | Total within-cluster sum of squares |
| Elbow Method | K = 5 | Titik penurunan inertia melambat |
| Silhouette peak | K = 2 | K = 5 dipilih untuk granularitas bisnis |

### 4. Dendrogram Analysis
Ward / Complete / Average linkage pada **500 BIRCH micro-cluster centroids**.
Ketiga metode konsisten menunjukkan struktur 5 cluster, memvalidasi pilihan K.

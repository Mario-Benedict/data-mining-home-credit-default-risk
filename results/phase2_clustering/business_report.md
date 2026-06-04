# Phase 2 — Segmentation via Clustering
**Dataset:** Home Credit Default Risk

---

## Ringkasan Eksekutif

| Metrik | Nilai |
|--------|-------|
| Total applicants | 331,219 |
| Jumlah cluster | 5 (K-Means) |
| Komponen PCA | 10 (54.4% variance) |
| Silhouette Score | 0.1492 |
| Inertia (K-Means) | 4,788,055.5 |
| K dari Elbow Method | 5 |
| K dari Silhouette | 2 |

**Algoritma dijalankan:**

1. **K-Means** — full data, K=5 (segmentasi utama)
2. **DBSCAN** — sample 30K, `eps=3.0`, `min_samples=10` (outlier detection)
3. **Hierarchical** — BIRCH (500 micro-clusters) + Ward linkage

## Distribusi Cluster K-Means

| Cluster | Nama | Jumlah | Persentase | Profil Risiko |
|---------|------|--------|------------|---------------|
| 0 | **Veteran Aktif** | 44,102 | 13.3% | 🟠 SEDANG-TINGGI |
| 1 | **Peminjam Ambisius** | 116,056 | 35.0% | 🟡 SEDANG |
| 2 | **Peminjam Minimal** | 117,406 | 35.4% | 🟢 RENDAH-SEDANG |
| 3 | **Pengguna CC Intensif** | 50,264 | 15.2% | 🟠 SEDANG-TINGGI |
| 4 | **Peminjam Bermasalah** | 3,391 | 1.0% | 🔴 SANGAT TINGGI |

---

## Cluster 0 — Veteran Aktif

> **Veteran Peminjam — Berpendapatan Tinggi, Sering Ditolak**  
> 44,102 applicants (13.3%) | Profil Risiko: 🟠 SEDANG-TINGGI

### Karakteristik Utama

| Fitur & Nilai | Arah |
|---------------|------|
| `PREV_COUNT +153.2%` | ▲ LEBIH TINGGI |
| `PREV_REFUSED_COUNT +131.9%` | ▲ LEBIH TINGGI |
| `AMT_REQ_CREDIT_BUREAU_YEAR +114.8%` | ▲ LEBIH TINGGI |
| `POS_MONTHS_COUNT +101.8%` | ▲ LEBIH TINGGI |
| `PREV_APPROVAL_RATE -71.5%` | ▼ LEBIH RENDAH |
| `BUREAU_COUNT +51.0%` | ▲ LEBIH TINGGI |
| `EXT_SOURCE_3 -33.7%` | ▼ LEBIH RENDAH |
| `CREDIT_TO_INCOME -33.3%` | ▼ LEBIH RENDAH |
| `CC_UTILIZATION_MEAN -30.6%` | ▼ LEBIH RENDAH |
| `CC_UTILIZATION_MAX -28.8%` | ▼ LEBIH RENDAH |

### Interpretasi Bisnis

Peminjam berpengalaman dengan pendapatan tinggi yang aktif & agresif mencari kredit. Meski pendapatan tinggi sering ditolak — kemungkinan rasio hutang-terhadap-kredit bermasalah atau over-application. Utilisasi CC rendah = mengelola CC dengan baik, namun histori penolakan tinggi = profil risiko perlu diperhatikan.

### Rekomendasi

> Evaluasi alasan penolakan historis. Cocok untuk kredit berjaminan (mortgage) mengingat pendapatan tinggi. Verifikasi debt-to-income ratio ketat.

---

## Cluster 1 — Peminjam Ambisius

> **Peminjam Kredit Besar — Debt-to-Income Tinggi**  
> 116,056 applicants (35.0%) | Profil Risiko: 🟡 SEDANG

### Karakteristik Utama

| Fitur & Nilai | Arah |
|---------------|------|
| `AMT_CREDIT +83.4%` | ▲ LEBIH TINGGI |
| `CREDIT_TO_INCOME +75.3%` | ▲ LEBIH TINGGI |
| `AMT_ANNUITY +69.5%` | ▲ LEBIH TINGGI |
| `CREDIT_TERM_MONTHS +58.6%` | ▲ LEBIH TINGGI |
| `ANNUITY_TO_INCOME +58.0%` | ▲ LEBIH TINGGI |
| `CC_UTILIZATION_MAX -41.5%` | ▼ LEBIH RENDAH |
| `CC_UTILIZATION_MEAN -38.5%` | ▼ LEBIH RENDAH |
| `PREV_COUNT -37.6%` | ▼ LEBIH RENDAH |
| `AMT_REQ_CREDIT_BUREAU_YEAR -31.9%` | ▼ LEBIH RENDAH |
| `PREV_REFUSED_COUNT -30.3%` | ▼ LEBIH RENDAH |

### Interpretasi Bisnis

Mengajukan pinjaman besar relatif terhadap pendapatan dengan tenor panjang. Sedikit riwayat pengajuan sebelumnya + utilisasi CC rendah menandakan peminjam pertama kali. Debt-to-income tinggi adalah risiko utama: rentan terhadap guncangan pendapatan.

### Rekomendasi

> Verifikasi stabilitas pendapatan sebelum persetujuan. Ideal untuk KPR/kendaraan. Stress-test kemampuan bayar pada skenario pendapatan turun 20-30%. Pertimbangkan asuransi jiwa/kesehatan sebagai syarat.

---

## Cluster 2 — Peminjam Minimal

> **Peminjam Sederhana — Berpendapatan Rendah, Kredit Kecil**  
> 117,406 applicants (35.4%) | Profil Risiko: 🟢 RENDAH-SEDANG

### Karakteristik Utama

| Fitur & Nilai | Arah |
|---------------|------|
| `AMT_CREDIT -84.2%` | ▼ LEBIH RENDAH |
| `AMT_ANNUITY -72.2%` | ▼ LEBIH RENDAH |
| `CREDIT_TO_INCOME -60.8%` | ▼ LEBIH RENDAH |
| `CREDIT_TERM_MONTHS -55.1%` | ▼ LEBIH RENDAH |
| `ANNUITY_TO_INCOME -42.8%` | ▼ LEBIH RENDAH |
| `CC_UTILIZATION_MAX -42.5%` | ▼ LEBIH RENDAH |
| `CC_UTILIZATION_MEAN -38.5%` | ▼ LEBIH RENDAH |
| `PREV_COUNT -38.1%` | ▼ LEBIH RENDAH |
| `NAME_CONTRACT_TYPE -35.6%` | ▼ LEBIH RENDAH |
| `CC_MONTHS_COUNT -34.2%` | ▼ LEBIH RENDAH |

### Interpretasi Bisnis

Peminjam berpendapatan rendah dengan kebutuhan kredit minimal. Pinjaman kecil tenor pendek — kemungkinan konsumsi sehari-hari atau darurat. Tidak aktif CC menunjukkan keterbatasan akses produk keuangan. Exposure kecil = risiko rendah, namun kapasitas bayar terbatas saat ada guncangan.

### Rekomendasi

> Segmen ideal micro-credit atau multiguna kecil. Prioritaskan edukasi keuangan & program inklusi. Pemantauan ringan cukup memadai.

---

## Cluster 3 — Pengguna CC Intensif

> **Pengguna Kartu Kredit Intensif — Revolving Credit Dependent**  
> 50,264 applicants (15.2%) | Profil Risiko: 🟠 SEDANG-TINGGI

### Karakteristik Utama

| Fitur & Nilai | Arah |
|---------------|------|
| `CC_UTILIZATION_MAX +219.6%` | ▲ LEBIH TINGGI |
| `CC_UTILIZATION_MEAN +206.2%` | ▲ LEBIH TINGGI |
| `CC_AMT_BALANCE_MEAN +157.8%` | ▲ LEBIH TINGGI |
| `CC_MONTHS_COUNT +152.9%` | ▲ LEBIH TINGGI |
| `AMT_REQ_CREDIT_BUREAU_YEAR +45.9%` | ▲ LEBIH TINGGI |
| `PREV_COUNT +42.5%` | ▲ LEBIH TINGGI |
| `POS_MONTHS_COUNT +27.0%` | ▲ LEBIH TINGGI |
| `NAME_CONTRACT_TYPE +26.9%` | ▲ LEBIH TINGGI |
| `AMT_INCOME_TOTAL +17.4%` | ▲ LEBIH TINGGI |
| `PREV_REFUSED_COUNT +17.1%` | ▲ LEBIH TINGGI |

### Interpretasi Bisnis

Sangat bergantung pada revolving credit (kartu kredit). Utilisasi CC jauh di atas rata-rata dengan saldo besar menunjukkan penggunaan mendekati atau melampaui limit. Riwayat CC panjang = nasabah lama yang aktif. Risiko: jika pendapatan terganggu, default berantai di banyak produk sekaligus.

### Rekomendasi

> Monitor utilisasi CC berkala. Tawarkan produk konsolidasi hutang. Batasi peningkatan limit kredit sampai utilisasi turun di bawah 70%.

---

## Cluster 4 — Peminjam Bermasalah

> **Peminjam Kronis Gagal Bayar — Profil Risiko Ekstrem**  
> 3,391 applicants (1.0%) | Profil Risiko: 🔴 SANGAT TINGGI

### Karakteristik Utama

| Fitur & Nilai | Arah |
|---------------|------|
| `INST_DPD_MAX +687.6%` | ▲ LEBIH TINGGI |
| `INST_SEVERE_LATE_RATIO +546.4%` | ▲ LEBIH TINGGI |
| `INST_DPD_MEAN +469.7%` | ▲ LEBIH TINGGI |
| `POS_SK_DPD_MEAN +415.0%` | ▲ LEBIH TINGGI |
| `CC_SK_DPD_MEAN +206.5%` | ▲ LEBIH TINGGI |
| `INST_LATE_RATIO +190.3%` | ▲ LEBIH TINGGI |
| `POS_MONTHS_COUNT +93.1%` | ▲ LEBIH TINGGI |
| `BUREAU_BB_SEVERE_DPD_MEAN +53.3%` | ▲ LEBIH TINGGI |
| `BUREAU_BB_DPD_RATIO_MEAN +44.9%` | ▲ LEBIH TINGGI |
| `CC_MONTHS_COUNT +37.2%` | ▲ LEBIH TINGGI |

### Interpretasi Bisnis

Kelompok kecil namun profil risiko ekstrem. Days Past Due (DPD) berlipat ganda di multiple produk (installment, POS, CC) — pola gagal bayar kronis dan sistemik, bukan keterlambatan insidental. Mereka sudah dalam kondisi financial distress serius.

### Rekomendasi

> Tolak pengajuan baru atau syarat jaminan ketat. Aktifkan restrukturisasi hutang nasabah existing. Lakukan debt collection intensif. Flag sebagai high-risk monitoring prioritas.

---

## Data Mining Concepts — Phase 2

### 1. Unsupervised Pattern Discovery
Tidak ada label TARGET digunakan saat training. Algoritma menemukan grouping dari struktur 67 fitur behavioral saja.

### 2. Distance Metrics
- **K-Means**: Euclidean distance di ruang PCA 10-komponen (curse-of-dim teratasi).
- **DBSCAN**: `eps=3.0` = radius neighborhood; `min_samples=10` = density threshold.

### 3. Cluster Validity Indices

| Indeks | Nilai | Keterangan |
|--------|-------|------------|
| Silhouette Score | 0.1492 | Wajar untuk financial data berdimensi tinggi |
| Inertia (WCSS) | 4,788,055.5 | Total within-cluster sum of squares |
| Elbow Method | K = 5 | Titik penurunan inertia melambat |
| Silhouette peak | K = 2 | K = 5 dipilih untuk granularitas bisnis |

### 4. Dendrogram Analysis
Ward / Complete / Average linkage pada **500 BIRCH micro-cluster centroids**.
Ketiga metode konsisten menunjukkan struktur 5 cluster, memvalidasi pilihan K.

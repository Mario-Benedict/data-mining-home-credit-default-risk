# Phase 4 — Anomaly & Outlier Detection
**Dataset:** Home Credit Default Risk

---

## Metodologi

| Parameter | Nilai |
|-----------|-------|
| Sample size | 356,255 dari 356,255 total aplikasi |
| IQR multiplier | 1.5 |
| Z-score threshold | 3.0 |
| Isolation Forest contaminations | [0.01, 0.05, 0.1] (default = 0.05) |
| Multi-col rule | flagged jika anomali di >= 3 kolom |
| Cross-reference | Phase 2 DBSCAN noise (`IS_OUTLIER`) sebagai sumber ke-4 |
| DBSCAN coverage | 50,000 rows (sample Phase 2) — baris lain dinilai 3 sinyal |

---

## Ringkasan Hasil

Setiap aplikasi dinilai oleh empat sinyal yang saling independen: IQR, Z-score,
Isolation Forest, dan noise DBSCAN dari Phase 2. Makin banyak sinyal yang setuju,
makin tinggi keyakinan bahwa aplikasi itu benar-benar menyimpang, bukan kebetulan statistik.

| Kategori | Jumlah | Persentase |
|----------|--------|------------|
| WEAK_SIGNAL | 179,784 | 50.5% |
| NORMAL | 154,967 | 43.5% |
| MODERATE_ANOMALY | 15,993 | 4.5% |
| HIGH_CONFIDENCE_ANOMALY | 5,511 | 1.5% |

609 dari 5511 anomali high-confidence juga ditandai sebagai noise oleh DBSCAN.
Dua keluarga metode yang berbeda pendekatan (kepadatan vs pohon isolasi) menunjuk titik yang sama.

---

## Distribusi High-Confidence per Cluster

| Cluster | Nama | Anomali High-Confidence |
|---------|------|--------------------------|
| 0 | Peminjam Bermasalah | **1,989** |
| 1 | Peminjam Ambisius | **216** |
| 2 | Veteran Aktif | **1,040** |
| 3 | Pengguna CC Intensif | **2,044** |
| 4 | Peminjam Minimal | **222** |

> **Interpretasi:** Cluster 3 (Pengguna CC Intensif) menyumbang anomali high-confidence terbanyak
> (2,044 kasus) — prioritas review underwriting.

---

## Tipologi Anomali

| Tipe | Jumlah | Justifikasi | Aksi Bisnis |
|------|--------|-------------|-------------|
| Tipe A - Data Error | 3,455 | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |
| Tipe C - Risk Signal | 137 | Kombinasi finansial kontradiktif (mis. rasio cicilan/pendapatan ekstrem, income rendah + credit besar, atau skor eksternal tinggi di cluster bermasalah). | Underwriting: matikan auto-approve, wajibkan manual review oleh underwriter senior + verifikasi pendapatan fisik. |
| Tipe B - Rare but Valid | 1,919 | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## Rekomendasi untuk Bank

### 1. ETL Hardening (Tipe A — Data Error)
Tambahkan capping otomatis di pipeline ingestion: setiap nilai dengan
Z-score > 5 di-flag untuk QA manual sebelum masuk warehouse.
Fitur prioritas: `DAYS_EMPLOYED`, `INST_DPD_MAX`, `AMT_INCOME_TOTAL`.

### 2. Underwriting Alert (Tipe C — Risk Signal)
137 kasus dengan profil kontradiktif → matikan auto-approve.
Wajibkan verifikasi pendapatan fisik + manual review oleh underwriter senior.
Rule deteksi terpenting: `income_low + credit_large + burden_high`.

### 3. Priority Routing (Tipe B — Rare Valid)
1,919 tail-end customer berpotensi VHNW (Very High Net Worth Individual).
Routing ke divisi Wealth Management untuk cross-sell produk premium.

### 4. Phase 2 Integration
DBSCAN noise sebagai indikator independen — tambahkan ke daily monitoring dashboard.
Rekening baru yang masuk DBSCAN noise + statistical outlier patut di-flag untuk audit.

---

## Data Mining Concepts — Phase 4

| Metode | Cara Kerja | Keunggulan |
|--------|------------|------------|
| **IQR** | Rentang interkuartil [Q1-1.5IQR, Q3+1.5IQR] | Robust terhadap distribusi skewed |
| **Z-score** | Standar deviasi dari mean (\|z\| > 3) | Sensitif terhadap Gaussian outlier |
| **Isolation Forest** | Tree ensemble, path length pendek = anomali | Multivariate, menangkap interaksi fitur |
| **DBSCAN (Phase 2)** | Density-based noise detection | Independen dari threshold statistik |

> **Cross-Method Validation:** Anomali yang ditemukan ≥2 metode = HIGH_CONFIDENCE.
> Jauh lebih reliabel daripada single-method detection.

> **Anomaly Typology:** Tipe A = perbaiki ETL; Tipe C = eskalasi underwriting; Tipe B = route ke wealth.

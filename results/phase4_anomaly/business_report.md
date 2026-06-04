# Phase 4 — Anomaly & Outlier Detection
**Dataset:** Home Credit Default Risk

---

## Metodologi

| Parameter | Nilai |
|-----------|-------|
| Sample size | 50,000 dari 356,255 total aplikasi |
| IQR multiplier | 1.5 |
| Z-score threshold | 3.0 |
| Isolation Forest contaminations | [0.01, 0.05, 0.1] (default = 0.05) |
| Multi-col rule | flagged jika anomali di >= 3 kolom |
| Cross-reference | Phase 2 DBSCAN noise (`IS_OUTLIER`) sebagai sumber ke-4 |

---

## Ringkasan Hasil

| Kategori | Jumlah | Persentase |
|----------|--------|------------|
| 🟡 **WEAK_SIGNAL** | 34,741 | 69.5% |
| 🟢 **NORMAL** | 10,072 | 20.1% |
| 🟠 **MODERATE_ANOMALY** | 3,775 | 7.5% |
| 🔴 **HIGH_CONFIDENCE_ANOMALY** | 1,412 | 2.8% |

> **Phase 2 DBSCAN cross-validation:** 42 dari 1412 high-confidence
> → konsistensi density-based (DBSCAN) dan tree-based (Isolation Forest) memperkuat reliabilitas.

---

## Distribusi High-Confidence per Cluster

| Cluster | Nama | Anomali High-Confidence |
|---------|------|--------------------------|
| 0 | Veteran Aktif | **165** |
| 1 | Peminjam Minimal | **242** |
| 2 | CC Intensif | **137** |
| 3 | Peminjam Ambisius | **319** |
| 4 | Peminjam Bermasalah | **549** |

> **Interpretasi:** Cluster 4 (Peminjam Bermasalah) dan Cluster 3 (Ambisius) mendominasi anomali —
> konsisten dengan temuan Phase 3 bahwa profil demografis keduanya sangat bervariasi.

---

## Tipologi Anomali

| Tipe | Jumlah | Justifikasi | Aksi Bisnis |
|------|--------|-------------|-------------|
| 🔴 **Tipe A - Data Error** | 844 | Deviasi fitur > 50x median klaster — kemungkinan kesalahan input/ETL (overflow, salah unit, atau sentinel value tidak ter-handle). | Data Engineering: tambahkan capping rule (Z-score>3 di tahap ingest) untuk mencegah kontaminasi model. |
| 🟠 **Tipe C - Risk Signal** | 23 | Kombinasi finansial kontradiktif (mis. rasio cicilan/pendapatan ekstrem, income rendah + credit besar, atau skor eksternal tinggi di cluster bermasalah). | Underwriting: matikan auto-approve, wajibkan manual review oleh underwriter senior + verifikasi pendapatan fisik. |
| 🟢 **Tipe B - Rare but Valid** | 545 | Ekstrem secara statistik tapi koheren — kemungkinan tail-end legitimate customer (VHNW, kasus khusus). | Routing: alihkan ke divisi Wealth Management / Priority Banking untuk potensi cross-sell. |

---

## Rekomendasi untuk Bank

### 1. ETL Hardening (Tipe A — Data Error)
Tambahkan capping otomatis di pipeline ingestion: setiap nilai dengan
Z-score > 5 di-flag untuk QA manual sebelum masuk warehouse.
Fitur prioritas: `DAYS_EMPLOYED`, `INST_DPD_MAX`, `AMT_INCOME_TOTAL`.

### 2. Underwriting Alert (Tipe C — Risk Signal)
23 kasus dengan profil kontradiktif → matikan auto-approve.
Wajibkan verifikasi pendapatan fisik + manual review oleh underwriter senior.
Rule deteksi terpenting: `income_low + credit_large + burden_high`.

### 3. Priority Routing (Tipe B — Rare Valid)
545 tail-end customer berpotensi VHNW (Very High Net Worth Individual).
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

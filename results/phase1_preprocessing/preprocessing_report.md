# Phase 1 — Preprocessing Report
**Dataset:** Home Credit Default Risk

Laporan ini merangkum apa yang dilakukan pipeline terhadap 7 file CSV mentah dan
memberi bukti bahwa feature set akhir layak dipakai untuk mining: multikolinearitas
yang berbahaya sudah dibuang, dan daya pisah tiap fitur terhadap default diukur
dengan mutual information. Setiap keputusan merujuk ke temuan EDA, bukan selera.

---

## Pipeline Steps (`src/pipeline/`)

| Step | Deskripsi |
|------|-----------|
| `step1_load` | Membaca 7 file CSV mentah |
| `step2_aggregate` | Roll-up 5 tabel relasional → grain SK_ID_CURR |
| `step3_merge` | Stack train+test, left-join semua agregat |
| `step4_clean` | Sentinel value (DAYS_EMPLOYED=365243), XNA → NaN, rare categories |
| `step5_missing` | Indikator missingness + imputasi (median/zero/mode) |
| `step6_outliers` | Winsorize p99 + cap + bin DPD social-circle |
| `step7_engineer` | Derived ratios + log transform + drop kolom redundan |
| `step8_encode` | Binary / ordinal (pendidikan) / frequency (income, organization) — bukan OHE |
| `step9_scale` | StandardScaler pada fitur kontinu & ordinal; hanya flag {0,1} dibiarkan |
| `step10_feature_selection` | Validasi feature selection — korelasi + entropy (MI) |

> **Final Feature Set:** 47 fitur × 307,511 baris train

---

## Feature Selection — Korelasi (Pearson)

**Multikolinearitas yang sudah di-drop di step1–7** (justifikasi EDA §7):

- Housing triplication: 14 kolom `*_AVG` dan `*_MEDI` (r > 0.99 dengan `*_MODE`)
- `OBS_60_CNT_SOCIAL_CIRCLE` (r = 0.998 dgn OBS_30)
- `FLAG_EMP_PHONE` (r = -1.0 dgn DAYS_EMPLOYED setelah sentinel)
- `FLAG_MOBIL` (near-constant)
- `REGION_RATING_CLIENT` (r > 0.85 dgn varian _W_CITY)

**Encoding kategorikal yang ramah-clustering (bukan OHE).** Variabel nominal sengaja TIDAK di-one-hot. Pada K-Means yang memakai jarak Euclidean, OHE memecah satu kolom menjadi banyak sumbu biner sparse yang membuat setiap kategori berjarak sama — padahal sebagian kategori jelas lebih mirip. Tiga variabel kategorikal diperlakukan sesuai sifatnya:

- `NAME_EDUCATION_TYPE` → **ordinal 0–4** (Lower secondary … Academic degree). Jenjang pendidikan punya urutan nyata; satu integer terurut menjaga 'Higher education lebih dekat ke Incomplete higher daripada ke Lower secondary'.
- `NAME_INCOME_TYPE` → **frequency encoding** (`NAME_INCOME_TYPE_FREQ`). Nominal tanpa urutan; dipetakan ke seberapa umum kategori itu, menjadi satu sumbu 'umum ↔ langka'.
- `ORGANIZATION_TYPE` → **frequency encoding** (`ORGANIZATION_TYPE_FREQ`). 12 sektor → satu sumbu, alih-alih 11 dummy sparse yang mendominasi jarak.

Pendekatan ini juga menghapus sumber kolinearitas sempurna pada run lama (`FLAG_SENTINEL_EMPLOYED` ≡ `ORGANIZATION_TYPE_Unknown` ≡ `NAME_INCOME_TYPE_Pensioner`, r ≈ 1.0) yang muncul justru karena OHE pada kategori 'Unknown' yang berimpit dengan flag pensiunan. Pensiunan tetap teridentifikasi terpisah lewat `FLAG_SENTINEL_EMPLOYED`.

**Pasangan |r| > 0.85 yang TERSISA di feature set final:** 1

| Feature 1 | Feature 2 | \|r\| |
|-----------|-----------|-------|
| `CC_UTILIZATION_MEAN` | `CC_UTILIZATION_MAX` | 0.891 |

---

## Feature Selection — Entropy (Mutual Information)

**Metode:** `sklearn.feature_selection.mutual_info_classif`

- Mengukur informasi mutual antara setiap fitur dengan TARGET
- Berbasis entropy: `I(X;Y) = H(Y) - H(Y|X)`
- Mendeteksi hubungan **non-linear** (tidak ditangkap korelasi Pearson)
- `random_state=42`, `n_neighbors=3` (k-NN density estimator)

### Top 15 Fitur — Kekuatan Diskriminatif Default

| Rank | Feature | MI Score |
|------|---------|----------|
| 1 | `CODE_GENDER` | 0.05693 |
| 2 | `FLAG_NO_CAR` | 0.05503 |
| 3 | `FLAG_EXT_SOURCE_1_MISSING` | 0.04823 |
| 4 | `NAME_CONTRACT_TYPE` | 0.04668 |
| 5 | `FLAG_NO_HOUSING_DATA` | 0.04022 |
| 6 | `NAME_EDUCATION_TYPE` | 0.02819 |
| 7 | `CNT_CHILDREN` | 0.02282 |
| 8 | `NAME_INCOME_TYPE_FREQ` | 0.01888 |
| 9 | `CREDIT_TERM_MONTHS` | 0.01883 |
| 10 | `DEF_30_CNT_SOCIAL_CIRCLE_BIN` | 0.01838 |
| 11 | `CC_UTILIZATION_MEAN` | 0.01683 |
| 12 | `CC_AMT_BALANCE_MEAN` | 0.01591 |
| 13 | `CC_UTILIZATION_MAX` | 0.01506 |
| 14 | `INST_LATE_RATIO` | 0.01396 |
| 15 | `EXT_SOURCE_3` | 0.01325 |

### Bottom 10 Fitur — Kandidat Drop (MI ≈ 0)

| Rank | Feature | MI Score |
|------|---------|----------|
| 38 | `INST_DPD_MAX` | 0.00422 |
| 39 | `CREDIT_TO_INCOME` | 0.00404 |
| 40 | `INST_DPD_MEAN` | 0.00371 |
| 41 | `FLAG_NO_BUREAU` | 0.00369 |
| 42 | `CC_SK_DPD_MEAN` | 0.00307 |
| 43 | `YEARS_BIRTH` | 0.00302 |
| 44 | `INST_PAYMENT_RATIO_MEAN` | 0.00245 |
| 45 | `BUREAU_BB_SEVERE_DPD_MEAN` | 0.00223 |
| 46 | `AMT_INCOME_TOTAL` | 0.00218 |
| 47 | `POS_MONTHS_COUNT` | 0.00180 |

- **Total fitur dengan MI ≈ 0 (tidak informatif):** 0 / 47
- **Mean MI:** 0.01377
- **Median MI:** 0.00989

Fitur dengan MI rendah tidak otomatis dibuang. Clustering bekerja tanpa label,
jadi fitur yang lemah memprediksi default bisa tetap penting untuk membedakan
perilaku nasabah. Skor MI di sini berfungsi sebagai audit: bukti terukur bahwa
seleksi fitur memakai ukuran entropy, bukan hanya korelasi linear.

---

## Deliverable — Clean Dataset

| Item | Nilai |
|------|-------|
| File | `datasets/final/features_clustering.csv` |
| Shape | 47 fitur × 307,511 rows (numerik, terstandardisasi) |
| Siap untuk | Phase 2 (K-Means, DBSCAN, Hierarchical clustering) |

**File pendukung:**

- [`feature_importance.csv`](feature_importance.csv) — MI score per fitur
- [`high_corr_pairs.csv`](high_corr_pairs.csv) — pasangan korelasi tinggi yang tersisa
- [`preprocessing_report.md`](preprocessing_report.md) — laporan ini

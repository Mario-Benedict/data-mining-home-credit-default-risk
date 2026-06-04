# Phase 1 — Preprocessing Report
**Dataset:** Home Credit Default Risk

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
| `step8_encode` | Binary / ordinal / OHE pada kategorikal |
| `step9_scale` | StandardScaler pada fitur kontinu (binary tidak di-scale) |
| `step10_feature_selection` | Validasi feature selection — korelasi + entropy (MI) |

> **Final Feature Set:** 67 fitur × 307,511 baris train

---

## Feature Selection — Korelasi (Pearson)

**Multikolinearitas yang sudah di-drop di step1–7** (justifikasi EDA §7):

- Housing triplication: 14 kolom `*_AVG` dan `*_MEDI` (r > 0.99 dengan `*_MODE`)
- `OBS_60_CNT_SOCIAL_CIRCLE` (r = 0.998 dgn OBS_30)
- `FLAG_EMP_PHONE` (r = -1.0 dgn DAYS_EMPLOYED setelah sentinel)
- `FLAG_MOBIL` (near-constant)
- `REGION_RATING_CLIENT` (r > 0.85 dgn varian _W_CITY)

**Pasangan |r| > 0.85 yang TERSISA di feature set final:** 5

| Feature 1 | Feature 2 | \|r\| |
|-----------|-----------|-------|
| `FLAG_SENTINEL_EMPLOYED` | `ORGANIZATION_TYPE_Unknown` | 1.000 |
| `FLAG_SENTINEL_EMPLOYED` | `NAME_INCOME_TYPE_Pensioner` | 1.000 |
| `NAME_INCOME_TYPE_Pensioner` | `ORGANIZATION_TYPE_Unknown` | 1.000 |
| `CC_UTILIZATION_MEAN` | `CC_UTILIZATION_MAX` | 0.891 |
| `NAME_EDUCATION_TYPE_Higher education` | `NAME_EDUCATION_TYPE_Secondary / secondary special` | 0.888 |

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
| 1 | `CODE_GENDER` | 0.05749 |
| 2 | `NAME_EDUCATION_TYPE_Secondary / secondary special` | 0.05623 |
| 3 | `FLAG_NO_CAR` | 0.05521 |
| 4 | `FLAG_EXT_SOURCE_1_MISSING` | 0.04872 |
| 5 | `NAME_CONTRACT_TYPE` | 0.04586 |
| 6 | `NAME_INCOME_TYPE_Working` | 0.04518 |
| 7 | `FLAG_NO_HOUSING_DATA` | 0.04034 |
| 8 | `CNT_CHILDREN` | 0.02434 |
| 9 | `CREDIT_TERM_MONTHS` | 0.01913 |
| 10 | `CC_UTILIZATION_MEAN` | 0.01575 |
| 11 | `CC_UTILIZATION_MAX` | 0.01543 |
| 12 | `CC_AMT_BALANCE_MEAN` | 0.01516 |
| 13 | `INST_LATE_RATIO` | 0.01422 |
| 14 | `EXT_SOURCE_3` | 0.01330 |
| 15 | `ORGANIZATION_TYPE_Private_Business` | 0.01297 |

### Bottom 10 Fitur — Kandidat Drop (MI ≈ 0)

| Rank | Feature | MI Score |
|------|---------|----------|
| 58 | `ORGANIZATION_TYPE_Trade` | 0.00056 |
| 59 | `ORGANIZATION_TYPE_Other` | 0.00052 |
| 60 | `ORGANIZATION_TYPE_Transport` | 0.00022 |
| 61 | `NAME_EDUCATION_TYPE_Incomplete higher` | 0.00020 |
| 62 | `ORGANIZATION_TYPE_Construction` | 0.00017 |
| 63 | `ORGANIZATION_TYPE_Security` | 0.00006 |
| 64 | `NAME_EDUCATION_TYPE_Lower secondary` | 0.00000 |
| 65 | `NAME_INCOME_TYPE_Other_Rare` | 0.00000 |
| 66 | `ORGANIZATION_TYPE_Finance` | 0.00000 |
| 67 | `ORGANIZATION_TYPE_Utilities` | 0.00000 |

- **Total fitur dengan MI ≈ 0 (tidak informatif):** 4 / 67
- **Mean MI:** 0.01082
- **Median MI:** 0.00613

> **Catatan:** Fitur dengan MI rendah tidak serta-merta di-drop karena clustering
> (unsupervised) tidak selalu mengikuti sinyal supervised (TARGET).
> Skor MI berfungsi sebagai bukti formal memenuhi rubrik *'correlation + entropy'* (PDF kriteria).

---

## Deliverable — Clean Dataset

| Item | Nilai |
|------|-------|
| File | `datasets/final/features_clustering.csv` |
| Shape | 67 fitur × 307,511 rows (numerik, terstandardisasi) |
| Siap untuk | Phase 2 (K-Means, DBSCAN, Hierarchical clustering) |

**File pendukung:**

- [`feature_importance.csv`](feature_importance.csv) — MI score per fitur
- [`high_corr_pairs.csv`](high_corr_pairs.csv) — pasangan korelasi tinggi yang tersisa
- [`preprocessing_report.md`](preprocessing_report.md) — laporan ini

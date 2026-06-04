# Phase 3 — Association Rule Mining
**Dataset:** Home Credit Default Risk

---

## Ringkasan Eksekutif

| Parameter | Nilai |
|-----------|-------|
| Transaksi dianalisis | 50,000 aplikasi (sample dari 356,255) |
| Algoritma | Apriori, FP-Growth, ECLAT, FP-Growth per-cluster |
| `min_support` | 0.03 |
| `min_confidence` | 0.35 |
| `min_lift` | 1.2 |
| Anti-redundansi (Jaccard) | > 0.65 dianggap duplikat |
| Final rules | **15** (top 3 per cluster + global fallback) |

## Statistik Per Algoritma

| Algoritma | Sample | Rules Ditemukan |
|-----------|--------|-----------------|
| `apriori` | 50K | 1,248 |
| `fpgrowth` | 50K | 1,248 |
| `eclat` | 50K | 1,248 |
| `fpgrowth_per_cluster` | subset | 1,029 |
| **Cross-algo consistent (≥2 algo)** | — | **1,248** |

---

## Top 15 Final Rules

| R# | Cluster Target | Support | Confidence | Lift | Algoritma |
|----|----------------|---------|------------|------|-----------|
| R1 | `cluster_0_veteran` | 0.052 | 0.897 | **4.52** | apriori... |
| R2 | `cluster_0_veteran` | 0.108 | 0.983 | **3.33** | apriori... |
| R3 | `cluster_0_veteran` | 0.065 | 0.933 | **2.67** | apriori... |
| R4 | `cluster_1_minimal` | 0.053 | 0.819 | **2.25** | fpgrowth_cluster1... |
| R5 | `cluster_1_minimal` | 0.093 | 0.734 | **2.07** | apriori... |
| R6 | `cluster_1_minimal` | 0.099 | 0.589 | **2.24** | apriori... |
| R7 | `cluster_2_cc_intensif` | 0.033 | 0.912 | **2.86** | apriori... |
| R8 | `cluster_2_cc_intensif` | 0.036 | 0.850 | **2.66** | apriori... |
| R9 | `cluster_2_cc_intensif` | 0.041 | 0.849 | **2.66** | apriori... |
| R10 | `cluster_4_bermasalah` | 0.057 | 0.843 | **2.49** | fpgrowth_cluster4... |
| R11 | `cluster_4_bermasalah` | 0.063 | 0.690 | **2.20** | fpgrowth_cluster4... |
| R12 | `cluster_4_bermasalah` | 0.058 | 0.653 | **2.29** | fpgrowth_cluster4... |
| R13 | `global` | 0.037 | 0.798 | **2.38** | apriori... |
| R14 | `global` | 0.033 | 0.758 | **2.26** | apriori... |
| R15 | `global` | 0.034 | 0.719 | **2.14** | apriori... |

> Detail lengkap dengan interpretasi per rule: [`rule_interpretations.md`](rule_interpretations.md)

---

## Temuan Non-Obvious

### 1. Pola "Cash-Poor, Credit-Hungry"
Aplikasi dengan jumlah kredit kecil + beban tinggi → income rendah dengan confidence **>98%**.
Ini adalah signature populasi mikro yang terdesak butuh cash flow walaupun nominal kecil.

### 2. Pola "Veteran High-Income, Rejected"
Kredit besar + beban menengah + Cluster 0 → income sangat tinggi (lift ~3).
Pendapatan tinggi tidak otomatis = approve jika riwayat penolakan padat.

### 3. Cluster 2 & 4 Tidak Muncul sebagai Antecedent Kuat
Kedua cluster ini scattered di berbagai profil demografi.
Jangan andalkan rules statis — pakai anomaly detection (Phase 4) atau scoring multivariat.

### 4. Senior + Employment-Baru = Sinyal Validasi
Kombinasi usia senior + masa kerja baru bukan jarang — kemungkinan pensiunan yang baru usaha.
Tambahkan validasi sumber pendapatan saat aplikasi.

---

## Data Mining Concepts — Phase 3

| Konsep | Formula | Interpretasi |
|--------|---------|--------------|
| **Support** | `count(itemset) / N` | Seberapa sering muncul di data |
| **Confidence** | `support(A∪B) / support(A)` | Keandalan: jika A maka B |
| **Lift** | `confidence / P(B)` | > 1 = asosiasi positif; = 1 = independen |

| Algoritma | Cara Kerja | Keunggulan |
|-----------|------------|------------|
| **Apriori** | Level-wise candidate generation | Exhaustive, mudah dimengerti |
| **FP-Growth** | Trie-based (FP-tree) | Jauh lebih cepat di memori besar |
| **ECLAT** | Vertical tidset intersection | Efisien depth-first traversal |

> **Multi-Algorithm Validation:** Rules yang ditemukan ≥2 algoritma diberi bonus skor (+0.3).
> Konsistensi membuktikan rule bukan artefak metode.

> **Jaccard Filtering:** Rules dengan overlap items > 65% dianggap redundan.
> Hanya rule skor tertinggi yang disimpan.

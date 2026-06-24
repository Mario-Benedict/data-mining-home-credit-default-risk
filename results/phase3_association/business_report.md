# Phase 3 — Association Rule Mining
**Dataset:** Home Credit Default Risk

---

## Ringkasan Eksekutif

| Parameter | Nilai |
|-----------|-------|
| Transaksi dianalisis | 356,255 dari 356,255 aplikasi |
| Algoritma | Apriori, FP-Growth, ECLAT, FP-Growth per-cluster |
| `min_support` | 0.03 |
| `min_confidence` | 0.35 |
| `min_lift` | 1.2 |
| Anti-redundansi (Jaccard) | > 0.65 dianggap duplikat |
| Final rules | **15** (top 3 per cluster + global fallback) |

## Statistik Per Algoritma

| Algoritma | Sample | Rules Ditemukan |
|-----------|--------|-----------------|
| `apriori` | 356,255 | 1,212 |
| `fpgrowth` | 356,255 | 1,212 |
| `eclat` | 356,255 | 1,212 |
| `fpgrowth_per_cluster` | subset | 1,209 |
| **Cross-algo consistent (≥2 algo)** | — | **1,212** |

---

## Top 15 Final Rules

| R# | Cluster Target | Support | Confidence | Lift | Algoritma |
|----|----------------|---------|------------|------|-----------|
| R1 | `cluster_0_bermasalah` | 0.107 | 0.982 | **3.24** | apriori... |
| R2 | `cluster_0_bermasalah` | 0.059 | 0.991 | **2.74** | fpgrowth_cluster0... |
| R3 | `cluster_0_bermasalah` | 0.062 | 0.760 | **2.18** | apriori... |
| R4 | `cluster_1_ambisius` | 0.034 | 0.909 | **2.82** | apriori... |
| R5 | `cluster_1_ambisius` | 0.041 | 0.847 | **2.63** | apriori... |
| R6 | `cluster_1_ambisius` | 0.036 | 0.844 | **2.62** | apriori... |
| R7 | `cluster_2_veteran` | 0.065 | 0.839 | **2.31** | apriori... |
| R8 | `cluster_2_veteran` | 0.063 | 0.786 | **2.20** | apriori... |
| R9 | `cluster_2_veteran` | 0.093 | 0.734 | **2.08** | apriori... |
| R10 | `cluster_3_cc_intensif` | 0.062 | 0.689 | **2.22** | fpgrowth_cluster3... |
| R11 | `cluster_3_cc_intensif` | 0.057 | 0.603 | **1.84** | apriori... |
| R12 | `cluster_3_cc_intensif` | 0.056 | 0.626 | **2.24** | fpgrowth_cluster3... |
| R13 | `cluster_4_minimal` | 0.048 | 0.898 | **4.60** | apriori... |
| R14 | `cluster_4_minimal` | 0.061 | 0.938 | **2.72** | apriori... |
| R15 | `cluster_4_minimal` | 0.045 | 0.925 | **2.68** | apriori... |

> Detail lengkap dengan interpretasi per rule: [`rule_interpretations.md`](rule_interpretations.md)

---

## Temuan Non-Obvious (top-lift dari final rules)

### 1. Peminjam Minimal (C4), usia senior, rasio cicilan-pendapatan tinggi → jumlah kredit kecil, pendapatan rendah
Lift **4.60**, confidence 89.8%, support 4.8% (target: `cluster_4_minimal`).

> Risiko likuiditas — meski nominal kecil, beban cicilan relatif berat. Sensitif terhadap shock pendapatan kecil sekalipun.

### 2. jumlah kredit kecil, rasio cicilan-pendapatan tinggi → pendapatan rendah
Lift **3.24**, confidence 98.2%, support 10.7% (target: `cluster_0_bermasalah`).

> Risiko likuiditas — meski nominal kecil, beban cicilan relatif berat. Sensitif terhadap shock pendapatan kecil sekalipun.

### 3. Peminjam Ambisius (C1), rasio cicilan-pendapatan tinggi, pendapatan sangat tinggi → jumlah kredit besar
Lift **2.82**, confidence 90.9%, support 3.4% (target: `cluster_1_ambisius`).

> Pola signature Cluster 3 — pengajuan besar oleh peminjam baru. Stress-test diperlukan untuk skenario pendapatan turun 20-30%.

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

Rules yang ditemukan minimal dua algoritma diberi bonus skor 0,3 saat ranking.
Apriori, FP-Growth, dan ECLAT bekerja dengan cara yang sangat berbeda; kalau ketiganya
menemukan rule yang sama, hampir pasti polanya memang ada di data.

Rules yang itemnya tumpang-tindih lebih dari 65% dianggap duplikat dan hanya yang
skornya tertinggi yang disimpan, supaya 15 rule final benar-benar 15 cerita berbeda.

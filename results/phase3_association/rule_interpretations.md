# Phase 3 — Rule Interpretations
**Dataset:** Home Credit Default Risk
**Total final rules:** 15 | **Sample size:** 50,000

---

## Rule #1 — Cluster 0 Veteran

```
{'burden_high', 'age_senior', 'cluster_0_veteran'} -> {'credit_small', 'income_low'}
```

| Metrik | Nilai |
|--------|-------|
| Support | 0.0520 (5.2%) |
| Confidence | 0.8974 (89.7%) |
| Lift | **4.5195** |
| Ditemukan di | `apriori+eclat+fpgrowth+fpgrowth_cluster0` |
| Multi-algo validated | ✅ Ya (4 algoritma) |

### 📖 What It Says

Bila aplikasi memiliki **[rasio cicilan-pendapatan tinggi, usia senior, Veteran Aktif (C0)]**,  
maka cenderung juga memiliki **[jumlah kredit kecil, pendapatan rendah]**.

### 📊 Why It Matters

- Asosiasi **kuat (lift 4.52×)**
- Confidence **sangat tinggi (89.7%)**
- terdapat di ~2,601 dari 50,000 aplikasi (5.2%)
- ✅ Tervalidasi lintas **4 algoritma** → bukan artefak metode

### ⚠️ Risk Reading

> Risiko likuiditas — meski nominal kecil, beban cicilan relatif berat. Sensitif terhadap shock pendapatan kecil sekalipun.

### ✅ Actionable Recommendation

> Gunakan sebagai feature engineering dalam scoring model. Validasi pada window holdout 6 bulan sebelum production rollout.

---

## Rule #2 — Cluster 0 Veteran

```
{'burden_high', 'credit_small'} -> {'income_low'}
```

| Metrik | Nilai |
|--------|-------|
| Support | 0.1085 (10.8%) |
| Confidence | 0.9833 (98.3%) |
| Lift | **3.3259** |
| Ditemukan di | `apriori+eclat+fpgrowth+fpgrowth_cluster0+fpgrowth_cluster1+fpgrowth_cluster4` |
| Multi-algo validated | ✅ Ya (6 algoritma) |

### 📖 What It Says

Bila aplikasi memiliki **[rasio cicilan-pendapatan tinggi, jumlah kredit kecil]**,  
maka cenderung juga memiliki **[pendapatan rendah]**.

### 📊 Why It Matters

- Asosiasi **kuat (lift 3.33×)**
- Confidence **hampir pasti (98.3%)**
- terdapat di ~5,423 dari 50,000 aplikasi (10.8%)
- ✅ Tervalidasi lintas **6 algoritma** → bukan artefak metode

### ⚠️ Risk Reading

> Risiko likuiditas — meski nominal kecil, beban cicilan relatif berat. Sensitif terhadap shock pendapatan kecil sekalipun.

### ✅ Actionable Recommendation

> Gunakan sebagai feature engineering dalam scoring model. Validasi pada window holdout 6 bulan sebelum production rollout.

---

## Rule #3 — Cluster 0 Veteran

```
{'burden_high', 'cluster_0_veteran', 'emp_new'} -> {'income_low'}
```

| Metrik | Nilai |
|--------|-------|
| Support | 0.0654 (6.5%) |
| Confidence | 0.9326 (93.3%) |
| Lift | **2.6747** |
| Ditemukan di | `apriori+eclat+fpgrowth+fpgrowth_cluster0` |
| Multi-algo validated | ✅ Ya (4 algoritma) |

### 📖 What It Says

Bila aplikasi memiliki **[rasio cicilan-pendapatan tinggi, Veteran Aktif (C0), masa kerja baru (<3 thn)]**,  
maka cenderung juga memiliki **[pendapatan rendah]**.

### 📊 Why It Matters

- Asosiasi **moderat (2.67×)**
- Confidence **sangat tinggi (93.3%)**
- terdapat di ~3,268 dari 50,000 aplikasi (6.5%)
- ✅ Tervalidasi lintas **4 algoritma** → bukan artefak metode

### ⚠️ Risk Reading

> Pola karakteristik dari segmen profil veteran berpenghasilan tinggi yang aktif mengajukan kredit tapi sering ditolak; mengkonfirmasi profil segmentasi.

### ✅ Actionable Recommendation

> Gunakan sebagai feature engineering dalam scoring model. Validasi pada window holdout 6 bulan sebelum production rollout.

---

## Rule #4 — Cluster 1 Minimal

```
{'credit_small', 'income_med'} -> {'burden_low', 'cluster_1_minimal'}
```

| Metrik | Nilai |
|--------|-------|
| Support | 0.0529 (5.3%) |
| Confidence | 0.8194 (81.9%) |
| Lift | **2.2532** |
| Ditemukan di | `fpgrowth_cluster1` |
| Multi-algo validated | ⬜ Single algo |

### 📖 What It Says

Bila aplikasi memiliki **[jumlah kredit kecil, pendapatan menengah]**,  
maka cenderung juga memiliki **[rasio cicilan-pendapatan rendah, Peminjam Minimal (C1)]**.

### 📊 Why It Matters

- Asosiasi **moderat (2.25×)**
- Confidence **sangat tinggi (81.9%)**
- terdapat di ~2,645 dari 50,000 aplikasi (5.3%)

### ⚠️ Risk Reading

> Pola karakteristik dari segmen profil peminjam mikro berpenghasilan rendah dengan kebutuhan kredit kecil; mengkonfirmasi profil segmentasi.

### ✅ Actionable Recommendation

> Cocok untuk produk micro-credit dengan tenor pendek + financial literacy program. Pemantauan ringan cukup.

---

## Rule #5 — Cluster 1 Minimal

```
{'emp_new', 'cluster_1_minimal'} -> {'age_senior'}
```

| Metrik | Nilai |
|--------|-------|
| Support | 0.0927 (9.3%) |
| Confidence | 0.7339 (73.4%) |
| Lift | **2.0737** |
| Ditemukan di | `apriori+eclat+fpgrowth+fpgrowth_cluster1` |
| Multi-algo validated | ✅ Ya (4 algoritma) |

### 📖 What It Says

Bila aplikasi memiliki **[masa kerja baru (<3 thn), Peminjam Minimal (C1)]**,  
maka cenderung juga memiliki **[usia senior]**.

### 📊 Why It Matters

- Asosiasi **moderat (2.07×)**
- Confidence **tinggi (73.4%)**
- terdapat di ~4,637 dari 50,000 aplikasi (9.3%)
- ✅ Tervalidasi lintas **4 algoritma** → bukan artefak metode

### ⚠️ Risk Reading

> Anomali kombinasi — usia senior dengan masa kerja baru biasanya = pensiunan yang baru mulai usaha kecil. Perlu validasi sumber pendapatan saat aplikasi.

### ✅ Actionable Recommendation

> Tambahkan field verifikasi: "sumber pendapatan utama pensiun atau usaha baru?". Sesuaikan tenor maksimum dengan usia harapan kerja.

---

## Rule #6 — Cluster 1 Minimal

```
{'credit_large', 'burden_med'} -> {'income_very_high'}
```

| Metrik | Nilai |
|--------|-------|
| Support | 0.0989 (9.9%) |
| Confidence | 0.5892 (58.9%) |
| Lift | **2.2421** |
| Ditemukan di | `apriori+eclat+fpgrowth+fpgrowth_cluster1+fpgrowth_cluster2+fpgrowth_cluster4` |
| Multi-algo validated | ✅ Ya (6 algoritma) |

### 📖 What It Says

Bila aplikasi memiliki **[jumlah kredit besar, rasio cicilan-pendapatan menengah]**,  
maka cenderung juga memiliki **[pendapatan sangat tinggi]**.

### 📊 Why It Matters

- Asosiasi **moderat (2.24×)**
- Confidence **moderat (58.9%)**
- terdapat di ~4,944 dari 50,000 aplikasi (9.9%)
- ✅ Tervalidasi lintas **6 algoritma** → bukan artefak metode

### ⚠️ Risk Reading

> Risiko terkelola — kapasitas finansial mampu menanggung nominal besar dengan beban moderat. Segmen prospektif untuk produk premium.

### ✅ Actionable Recommendation

> Gunakan sebagai feature engineering dalam scoring model. Validasi pada window holdout 6 bulan sebelum production rollout.

---

## Rule #7 — Cluster 2 Cc Intensif

```
{'burden_high', 'income_very_high', 'cluster_2_cc_intensif'} -> {'credit_large'}
```

| Metrik | Nilai |
|--------|-------|
| Support | 0.0333 (3.3%) |
| Confidence | 0.9122 (91.2%) |
| Lift | **2.8566** |
| Ditemukan di | `apriori+eclat+fpgrowth` |
| Multi-algo validated | ✅ Ya (3 algoritma) |

### 📖 What It Says

Bila aplikasi memiliki **[rasio cicilan-pendapatan tinggi, pendapatan sangat tinggi, CC Intensif (C2)]**,  
maka cenderung juga memiliki **[jumlah kredit besar]**.

### 📊 Why It Matters

- Asosiasi **moderat (2.86×)**
- Confidence **sangat tinggi (91.2%)**
- terdapat di ~1,663 dari 50,000 aplikasi (3.3%)
- ✅ Tervalidasi lintas **3 algoritma** → bukan artefak metode

### ⚠️ Risk Reading

> Pola karakteristik dari segmen pengguna kartu kredit dengan utilisasi tinggi — sensitif terhadap shock pendapatan; mengkonfirmasi profil segmentasi.

### ✅ Actionable Recommendation

> Segmen prioritas untuk cross-sell produk premium (KPR jangka panjang, kartu kredit gold, asuransi jiwa). Risk-based pricing diskon 0.25-0.50%.

---

## Rule #8 — Cluster 2 Cc Intensif

```
{'age_mid', 'cluster_2_cc_intensif', 'income_very_high'} -> {'credit_large'}
```

| Metrik | Nilai |
|--------|-------|
| Support | 0.0359 (3.6%) |
| Confidence | 0.8503 (85.0%) |
| Lift | **2.6627** |
| Ditemukan di | `apriori+eclat+fpgrowth` |
| Multi-algo validated | ✅ Ya (3 algoritma) |

### 📖 What It Says

Bila aplikasi memiliki **[usia menengah, CC Intensif (C2), pendapatan sangat tinggi]**,  
maka cenderung juga memiliki **[jumlah kredit besar]**.

### 📊 Why It Matters

- Asosiasi **moderat (2.66×)**
- Confidence **sangat tinggi (85.0%)**
- terdapat di ~1,795 dari 50,000 aplikasi (3.6%)
- ✅ Tervalidasi lintas **3 algoritma** → bukan artefak metode

### ⚠️ Risk Reading

> Pola karakteristik dari segmen pengguna kartu kredit dengan utilisasi tinggi — sensitif terhadap shock pendapatan; mengkonfirmasi profil segmentasi.

### ✅ Actionable Recommendation

> Segmen prioritas untuk cross-sell produk premium (KPR jangka panjang, kartu kredit gold, asuransi jiwa). Risk-based pricing diskon 0.25-0.50%.

---

## Rule #9 — Cluster 2 Cc Intensif

```
{'burden_high', 'income_high', 'cluster_2_cc_intensif'} -> {'credit_large'}
```

| Metrik | Nilai |
|--------|-------|
| Support | 0.0406 (4.1%) |
| Confidence | 0.8490 (84.9%) |
| Lift | **2.6587** |
| Ditemukan di | `apriori+eclat+fpgrowth` |
| Multi-algo validated | ✅ Ya (3 algoritma) |

### 📖 What It Says

Bila aplikasi memiliki **[rasio cicilan-pendapatan tinggi, pendapatan tinggi, CC Intensif (C2)]**,  
maka cenderung juga memiliki **[jumlah kredit besar]**.

### 📊 Why It Matters

- Asosiasi **moderat (2.66×)**
- Confidence **sangat tinggi (84.9%)**
- terdapat di ~2,029 dari 50,000 aplikasi (4.1%)
- ✅ Tervalidasi lintas **3 algoritma** → bukan artefak metode

### ⚠️ Risk Reading

> Pola karakteristik dari segmen pengguna kartu kredit dengan utilisasi tinggi — sensitif terhadap shock pendapatan; mengkonfirmasi profil segmentasi.

### ✅ Actionable Recommendation

> Gunakan sebagai feature engineering dalam scoring model. Validasi pada window holdout 6 bulan sebelum production rollout.

---

## Rule #10 — Cluster 4 Bermasalah

```
{'credit_small', 'income_high'} -> {'burden_low', 'cluster_4_bermasalah'}
```

| Metrik | Nilai |
|--------|-------|
| Support | 0.0575 (5.7%) |
| Confidence | 0.8427 (84.3%) |
| Lift | **2.4876** |
| Ditemukan di | `fpgrowth_cluster4` |
| Multi-algo validated | ⬜ Single algo |

### 📖 What It Says

Bila aplikasi memiliki **[jumlah kredit kecil, pendapatan tinggi]**,  
maka cenderung juga memiliki **[rasio cicilan-pendapatan rendah, Peminjam Bermasalah (C4)]**.

### 📊 Why It Matters

- Asosiasi **moderat (2.49×)**
- Confidence **sangat tinggi (84.3%)**
- terdapat di ~2,874 dari 50,000 aplikasi (5.7%)

### ⚠️ Risk Reading

> PERHATIAN MAKSIMUM — Cluster 4 memiliki DPD rata-rata 4–7× di atas baseline. Setiap pola yang sering muncul di sini layak dijadikan rule deteksi dini.

### ✅ Actionable Recommendation

> Tambahkan ke rule-engine early-warning. Jika pola ini terdeteksi pada existing customer → trigger account review + outreach proaktif.

---

## Rule #11 — Cluster 4 Bermasalah

```
{'risk_score_high', 'cluster_4_bermasalah', 'emp_new'} -> {'age_senior'}
```

| Metrik | Nilai |
|--------|-------|
| Support | 0.0633 (6.3%) |
| Confidence | 0.6898 (69.0%) |
| Lift | **2.2014** |
| Ditemukan di | `fpgrowth_cluster4` |
| Multi-algo validated | ⬜ Single algo |

### 📖 What It Says

Bila aplikasi memiliki **[skor eksternal tinggi, Peminjam Bermasalah (C4), masa kerja baru (<3 thn)]**,  
maka cenderung juga memiliki **[usia senior]**.

### 📊 Why It Matters

- Asosiasi **moderat (2.20×)**
- Confidence **tinggi (69.0%)**
- terdapat di ~3,166 dari 50,000 aplikasi (6.3%)

### ⚠️ Risk Reading

> Sinyal positif dari bureau eksternal — kredibilitas terdokumentasi di sistem credit bureau pihak ketiga.

### ✅ Actionable Recommendation

> Tambahkan ke rule-engine early-warning. Jika pola ini terdeteksi pada existing customer → trigger account review + outreach proaktif.

---

## Rule #12 — Cluster 4 Bermasalah

```
{'age_senior', 'cluster_4_bermasalah', 'income_low'} -> {'emp_new'}
```

| Metrik | Nilai |
|--------|-------|
| Support | 0.0580 (5.8%) |
| Confidence | 0.6528 (65.3%) |
| Lift | **2.2938** |
| Ditemukan di | `fpgrowth_cluster4` |
| Multi-algo validated | ⬜ Single algo |

### 📖 What It Says

Bila aplikasi memiliki **[usia senior, Peminjam Bermasalah (C4), pendapatan rendah]**,  
maka cenderung juga memiliki **[masa kerja baru (<3 thn)]**.

### 📊 Why It Matters

- Asosiasi **moderat (2.29×)**
- Confidence **tinggi (65.3%)**
- terdapat di ~2,901 dari 50,000 aplikasi (5.8%)

### ⚠️ Risk Reading

> PERHATIAN MAKSIMUM — Cluster 4 memiliki DPD rata-rata 4–7× di atas baseline. Setiap pola yang sering muncul di sini layak dijadikan rule deteksi dini.

### ✅ Actionable Recommendation

> Tambahkan ke rule-engine early-warning. Jika pola ini terdeteksi pada existing customer → trigger account review + outreach proaktif.

---

## Rule #13 — Global

```
{'risk_score_high', 'emp_new', 'income_low'} -> {'age_senior'}
```

| Metrik | Nilai |
|--------|-------|
| Support | 0.0374 (3.7%) |
| Confidence | 0.7983 (79.8%) |
| Lift | **2.3806** |
| Ditemukan di | `apriori+eclat+fpgrowth` |
| Multi-algo validated | ✅ Ya (3 algoritma) |

### 📖 What It Says

Bila aplikasi memiliki **[skor eksternal tinggi, masa kerja baru (<3 thn), pendapatan rendah]**,  
maka cenderung juga memiliki **[usia senior]**.

### 📊 Why It Matters

- Asosiasi **moderat (2.38×)**
- Confidence **tinggi (79.8%)**
- terdapat di ~1,872 dari 50,000 aplikasi (3.7%)
- ✅ Tervalidasi lintas **3 algoritma** → bukan artefak metode

### ⚠️ Risk Reading

> Sinyal positif dari bureau eksternal — kredibilitas terdokumentasi di sistem credit bureau pihak ketiga.

### ✅ Actionable Recommendation

> Pakai sebagai positive flag dalam scoring model — bobot tambahan untuk approval rate dan limit increase.

---

## Rule #14 — Global

```
{'burden_high', 'emp_new', 'risk_score_high'} -> {'age_senior'}
```

| Metrik | Nilai |
|--------|-------|
| Support | 0.0330 (3.3%) |
| Confidence | 0.7583 (75.8%) |
| Lift | **2.2612** |
| Ditemukan di | `apriori+eclat+fpgrowth` |
| Multi-algo validated | ✅ Ya (3 algoritma) |

### 📖 What It Says

Bila aplikasi memiliki **[rasio cicilan-pendapatan tinggi, masa kerja baru (<3 thn), skor eksternal tinggi]**,  
maka cenderung juga memiliki **[usia senior]**.

### 📊 Why It Matters

- Asosiasi **moderat (2.26×)**
- Confidence **tinggi (75.8%)**
- terdapat di ~1,650 dari 50,000 aplikasi (3.3%)
- ✅ Tervalidasi lintas **3 algoritma** → bukan artefak metode

### ⚠️ Risk Reading

> Sinyal positif dari bureau eksternal — kredibilitas terdokumentasi di sistem credit bureau pihak ketiga.

### ✅ Actionable Recommendation

> Pakai sebagai positive flag dalam scoring model — bobot tambahan untuk approval rate dan limit increase.

---

## Rule #15 — Global

```
{'age_senior', 'risk_score_med', 'income_low'} -> {'emp_new'}
```

| Metrik | Nilai |
|--------|-------|
| Support | 0.0335 (3.4%) |
| Confidence | 0.7188 (71.9%) |
| Lift | **2.1429** |
| Ditemukan di | `apriori+eclat+fpgrowth` |
| Multi-algo validated | ✅ Ya (3 algoritma) |

### 📖 What It Says

Bila aplikasi memiliki **[usia senior, skor eksternal menengah, pendapatan rendah]**,  
maka cenderung juga memiliki **[masa kerja baru (<3 thn)]**.

### 📊 Why It Matters

- Asosiasi **moderat (2.14×)**
- Confidence **tinggi (71.9%)**
- terdapat di ~1,677 dari 50,000 aplikasi (3.4%)
- ✅ Tervalidasi lintas **3 algoritma** → bukan artefak metode

### ⚠️ Risk Reading

> Anomali kombinasi — usia senior dengan masa kerja baru biasanya = pensiunan yang baru mulai usaha kecil. Perlu validasi sumber pendapatan saat aplikasi.

### ✅ Actionable Recommendation

> Tambahkan field verifikasi: "sumber pendapatan utama pensiun atau usaha baru?". Sesuaikan tenor maksimum dengan usia harapan kerja.

---

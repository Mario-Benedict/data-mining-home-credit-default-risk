# Phase 3 — Rule Interpretations
**Dataset:** Home Credit Default Risk
Total final rules: 15 | Transaksi dianalisis: 356,255

Cara membaca metrik: support = seberapa sering kombinasi ini muncul di seluruh data.
Confidence = bila sisi kiri rule terpenuhi, berapa persen kasus sisi kanan ikut terjadi.
Lift = berapa kali lebih sering kombinasi ini muncul dibanding jika keduanya tidak berhubungan;
lift 1 berarti kebetulan biasa, lift 3 berarti tiga kali lebih sering dari kebetulan.

---

## Rule #1 — Cluster 0 Bermasalah

```
{'credit_small', 'burden_high'} -> {'income_low'}
```

| Metrik | Nilai |
|--------|-------|
| Support | 0.1066 (10.7%) |
| Confidence | 0.9823 (98.2%) |
| Lift | 3.2407 |
| Ditemukan di | `apriori+eclat+fpgrowth+fpgrowth_cluster0+fpgrowth_cluster2+fpgrowth_cluster3+fpgrowth_cluster4` |
| Validasi lintas algoritma | ya, ditemukan 7 algoritma |

### Apa isi rule ini

Jika sebuah aplikasi punya profil jumlah kredit kecil, rasio cicilan-pendapatan tinggi,
biasanya ia juga pendapatan rendah.

### Mengapa layak dipercaya

- Asosiasi **kuat (lift 3.24×)**
- Confidence **hampir pasti (98.2%)**
- terdapat di ~37,979 dari 356,255 aplikasi (10.7%)
- Ditemukan oleh 7 algoritma yang cara kerjanya berbeda, jadi polanya nyata dan bukan artefak satu metode

### Artinya untuk risiko kredit

> Risiko likuiditas — meski nominal kecil, beban cicilan relatif berat. Sensitif terhadap shock pendapatan kecil sekalipun.

### Yang sebaiknya dilakukan

> Gunakan sebagai feature engineering dalam scoring model. Validasi pada window holdout 6 bulan sebelum production rollout.

---

## Rule #2 — Cluster 0 Bermasalah

```
{'emp_new', 'credit_small', 'cluster_0_bermasalah', 'burden_high'} -> {'income_low'}
```

| Metrik | Nilai |
|--------|-------|
| Support | 0.0589 (5.9%) |
| Confidence | 0.9906 (99.1%) |
| Lift | 2.7443 |
| Ditemukan di | `fpgrowth_cluster0` |
| Validasi lintas algoritma | hanya 1 algoritma |

### Apa isi rule ini

Jika sebuah aplikasi punya profil masa kerja baru (<3 thn), jumlah kredit kecil, Peminjam Bermasalah (C0), rasio cicilan-pendapatan tinggi,
biasanya ia juga pendapatan rendah.

### Mengapa layak dipercaya

- Asosiasi **moderat (2.74×)**
- Confidence **hampir pasti (99.1%)**
- terdapat di ~20,985 dari 356,255 aplikasi (5.9%)

### Artinya untuk risiko kredit

> Risiko likuiditas — meski nominal kecil, beban cicilan relatif berat. Sensitif terhadap shock pendapatan kecil sekalipun.

### Yang sebaiknya dilakukan

> Tambahkan ke rule-engine early-warning. Jika pola ini terdeteksi pada existing customer → trigger account review + outreach proaktif.

---

## Rule #3 — Cluster 0 Bermasalah

```
{'credit_small', 'age_senior', 'income_low'} -> {'emp_new'}
```

| Metrik | Nilai |
|--------|-------|
| Support | 0.0622 (6.2%) |
| Confidence | 0.7603 (76.0%) |
| Lift | 2.1827 |
| Ditemukan di | `apriori+eclat+fpgrowth+fpgrowth_cluster0+fpgrowth_cluster2+fpgrowth_cluster4` |
| Validasi lintas algoritma | ya, ditemukan 6 algoritma |

### Apa isi rule ini

Jika sebuah aplikasi punya profil jumlah kredit kecil, usia senior, pendapatan rendah,
biasanya ia juga masa kerja baru (<3 thn).

### Mengapa layak dipercaya

- Asosiasi **moderat (2.18×)**
- Confidence **tinggi (76.0%)**
- terdapat di ~22,159 dari 356,255 aplikasi (6.2%)
- Ditemukan oleh 6 algoritma yang cara kerjanya berbeda, jadi polanya nyata dan bukan artefak satu metode

### Artinya untuk risiko kredit

> Anomali kombinasi — usia senior dengan masa kerja baru biasanya = pensiunan yang baru mulai usaha kecil. Perlu validasi sumber pendapatan saat aplikasi.

### Yang sebaiknya dilakukan

> Tambahkan field verifikasi: "sumber pendapatan utama pensiun atau usaha baru?". Sesuaikan tenor maksimum dengan usia harapan kerja.

---

## Rule #4 — Cluster 1 Ambisius

```
{'cluster_1_ambisius', 'burden_high', 'income_very_high'} -> {'credit_large'}
```

| Metrik | Nilai |
|--------|-------|
| Support | 0.0335 (3.4%) |
| Confidence | 0.9086 (90.9%) |
| Lift | 2.8215 |
| Ditemukan di | `apriori+eclat+fpgrowth` |
| Validasi lintas algoritma | ya, ditemukan 3 algoritma |

### Apa isi rule ini

Jika sebuah aplikasi punya profil Peminjam Ambisius (C1), rasio cicilan-pendapatan tinggi, pendapatan sangat tinggi,
biasanya ia juga jumlah kredit besar.

### Mengapa layak dipercaya

- Asosiasi **moderat (2.82×)**
- Confidence **sangat tinggi (90.9%)**
- terdapat di ~11,946 dari 356,255 aplikasi (3.4%)
- Ditemukan oleh 3 algoritma yang cara kerjanya berbeda, jadi polanya nyata dan bukan artefak satu metode

### Artinya untuk risiko kredit

> Pola signature Cluster 3 — pengajuan besar oleh peminjam baru. Stress-test diperlukan untuk skenario pendapatan turun 20-30%.

### Yang sebaiknya dilakukan

> Segmen prioritas untuk cross-sell produk premium (KPR jangka panjang, kartu kredit gold, asuransi jiwa). Risk-based pricing diskon 0.25-0.50%.

---

## Rule #5 — Cluster 1 Ambisius

```
{'income_high', 'cluster_1_ambisius', 'burden_high'} -> {'credit_large'}
```

| Metrik | Nilai |
|--------|-------|
| Support | 0.0407 (4.1%) |
| Confidence | 0.8473 (84.7%) |
| Lift | 2.6312 |
| Ditemukan di | `apriori+eclat+fpgrowth` |
| Validasi lintas algoritma | ya, ditemukan 3 algoritma |

### Apa isi rule ini

Jika sebuah aplikasi punya profil pendapatan tinggi, Peminjam Ambisius (C1), rasio cicilan-pendapatan tinggi,
biasanya ia juga jumlah kredit besar.

### Mengapa layak dipercaya

- Asosiasi **moderat (2.63×)**
- Confidence **sangat tinggi (84.7%)**
- terdapat di ~14,503 dari 356,255 aplikasi (4.1%)
- Ditemukan oleh 3 algoritma yang cara kerjanya berbeda, jadi polanya nyata dan bukan artefak satu metode

### Artinya untuk risiko kredit

> Pola signature Cluster 3 — pengajuan besar oleh peminjam baru. Stress-test diperlukan untuk skenario pendapatan turun 20-30%.

### Yang sebaiknya dilakukan

> Wajibkan stress-test in-house: berapa peluang default jika pendapatan turun 30%? Jika > 25%, tawarkan plafon lebih rendah atau tenor lebih pendek.

---

## Rule #6 — Cluster 1 Ambisius

```
{'cluster_1_ambisius', 'age_mid', 'income_very_high'} -> {'credit_large'}
```

| Metrik | Nilai |
|--------|-------|
| Support | 0.0362 (3.6%) |
| Confidence | 0.8444 (84.4%) |
| Lift | 2.6221 |
| Ditemukan di | `apriori+eclat+fpgrowth` |
| Validasi lintas algoritma | ya, ditemukan 3 algoritma |

### Apa isi rule ini

Jika sebuah aplikasi punya profil Peminjam Ambisius (C1), usia menengah, pendapatan sangat tinggi,
biasanya ia juga jumlah kredit besar.

### Mengapa layak dipercaya

- Asosiasi **moderat (2.62×)**
- Confidence **sangat tinggi (84.4%)**
- terdapat di ~12,885 dari 356,255 aplikasi (3.6%)
- Ditemukan oleh 3 algoritma yang cara kerjanya berbeda, jadi polanya nyata dan bukan artefak satu metode

### Artinya untuk risiko kredit

> Pola signature Cluster 3 — pengajuan besar oleh peminjam baru. Stress-test diperlukan untuk skenario pendapatan turun 20-30%.

### Yang sebaiknya dilakukan

> Segmen prioritas untuk cross-sell produk premium (KPR jangka panjang, kartu kredit gold, asuransi jiwa). Risk-based pricing diskon 0.25-0.50%.

---

## Rule #7 — Cluster 2 Veteran

```
{'credit_small', 'income_med'} -> {'burden_low'}
```

| Metrik | Nilai |
|--------|-------|
| Support | 0.0655 (6.5%) |
| Confidence | 0.8394 (83.9%) |
| Lift | 2.3063 |
| Ditemukan di | `apriori+eclat+fpgrowth+fpgrowth_cluster2+fpgrowth_cluster4` |
| Validasi lintas algoritma | ya, ditemukan 5 algoritma |

### Apa isi rule ini

Jika sebuah aplikasi punya profil jumlah kredit kecil, pendapatan menengah,
biasanya ia juga rasio cicilan-pendapatan rendah.

### Mengapa layak dipercaya

- Asosiasi **moderat (2.31×)**
- Confidence **sangat tinggi (83.9%)**
- terdapat di ~23,330 dari 356,255 aplikasi (6.5%)
- Ditemukan oleh 5 algoritma yang cara kerjanya berbeda, jadi polanya nyata dan bukan artefak satu metode

### Artinya untuk risiko kredit

> Pola karakteristik dari segmen profil veteran berpenghasilan tinggi yang aktif mengajukan kredit tapi sering ditolak; mengkonfirmasi profil segmentasi.

### Yang sebaiknya dilakukan

> Gunakan sebagai feature engineering dalam scoring model. Validasi pada window holdout 6 bulan sebelum production rollout.

---

## Rule #8 — Cluster 2 Veteran

```
{'income_high', 'credit_small'} -> {'burden_low'}
```

| Metrik | Nilai |
|--------|-------|
| Support | 0.0633 (6.3%) |
| Confidence | 0.7864 (78.6%) |
| Lift | 2.1971 |
| Ditemukan di | `apriori+eclat+fpgrowth+fpgrowth_cluster2+fpgrowth_cluster3+fpgrowth_cluster4` |
| Validasi lintas algoritma | ya, ditemukan 6 algoritma |

### Apa isi rule ini

Jika sebuah aplikasi punya profil pendapatan tinggi, jumlah kredit kecil,
biasanya ia juga rasio cicilan-pendapatan rendah.

### Mengapa layak dipercaya

- Asosiasi **moderat (2.20×)**
- Confidence **tinggi (78.6%)**
- terdapat di ~22,550 dari 356,255 aplikasi (6.3%)
- Ditemukan oleh 6 algoritma yang cara kerjanya berbeda, jadi polanya nyata dan bukan artefak satu metode

### Artinya untuk risiko kredit

> Pola karakteristik dari segmen profil veteran berpenghasilan tinggi yang aktif mengajukan kredit tapi sering ditolak; mengkonfirmasi profil segmentasi.

### Yang sebaiknya dilakukan

> Gunakan sebagai feature engineering dalam scoring model. Validasi pada window holdout 6 bulan sebelum production rollout.

---

## Rule #9 — Cluster 2 Veteran

```
{'emp_new', 'cluster_2_veteran'} -> {'age_senior'}
```

| Metrik | Nilai |
|--------|-------|
| Support | 0.0932 (9.3%) |
| Confidence | 0.7343 (73.4%) |
| Lift | 2.0769 |
| Ditemukan di | `apriori+eclat+fpgrowth+fpgrowth_cluster2` |
| Validasi lintas algoritma | ya, ditemukan 4 algoritma |

### Apa isi rule ini

Jika sebuah aplikasi punya profil masa kerja baru (<3 thn), Veteran Aktif (C2),
biasanya ia juga usia senior.

### Mengapa layak dipercaya

- Asosiasi **moderat (2.08×)**
- Confidence **tinggi (73.4%)**
- terdapat di ~33,197 dari 356,255 aplikasi (9.3%)
- Ditemukan oleh 4 algoritma yang cara kerjanya berbeda, jadi polanya nyata dan bukan artefak satu metode

### Artinya untuk risiko kredit

> Anomali kombinasi — usia senior dengan masa kerja baru biasanya = pensiunan yang baru mulai usaha kecil. Perlu validasi sumber pendapatan saat aplikasi.

### Yang sebaiknya dilakukan

> Tambahkan field verifikasi: "sumber pendapatan utama pensiun atau usaha baru?". Sesuaikan tenor maksimum dengan usia harapan kerja.

---

## Rule #10 — Cluster 3 Cc Intensif

```
{'emp_new', 'risk_score_high', 'cluster_3_cc_intensif'} -> {'age_senior'}
```

| Metrik | Nilai |
|--------|-------|
| Support | 0.0616 (6.2%) |
| Confidence | 0.6886 (68.9%) |
| Lift | 2.2167 |
| Ditemukan di | `fpgrowth_cluster3` |
| Validasi lintas algoritma | hanya 1 algoritma |

### Apa isi rule ini

Jika sebuah aplikasi punya profil masa kerja baru (<3 thn), skor eksternal tinggi, Pengguna CC Intensif (C3),
biasanya ia juga usia senior.

### Mengapa layak dipercaya

- Asosiasi **moderat (2.22×)**
- Confidence **tinggi (68.9%)**
- terdapat di ~21,927 dari 356,255 aplikasi (6.2%)

### Artinya untuk risiko kredit

> Sinyal positif dari bureau eksternal — kredibilitas terdokumentasi di sistem credit bureau pihak ketiga.

### Yang sebaiknya dilakukan

> Pakai sebagai positive flag dalam scoring model — bobot tambahan untuk approval rate dan limit increase.

---

## Rule #11 — Cluster 3 Cc Intensif

```
{'risk_score_high', 'income_very_high'} -> {'credit_large'}
```

| Metrik | Nilai |
|--------|-------|
| Support | 0.0569 (5.7%) |
| Confidence | 0.6025 (60.3%) |
| Lift | 1.8397 |
| Ditemukan di | `apriori+eclat+fpgrowth+fpgrowth_cluster3` |
| Validasi lintas algoritma | ya, ditemukan 4 algoritma |

### Apa isi rule ini

Jika sebuah aplikasi punya profil skor eksternal tinggi, pendapatan sangat tinggi,
biasanya ia juga jumlah kredit besar.

### Mengapa layak dipercaya

- Asosiasi **lemah (1.84×)**
- Confidence **tinggi (60.3%)**
- terdapat di ~20,284 dari 356,255 aplikasi (5.7%)
- Ditemukan oleh 4 algoritma yang cara kerjanya berbeda, jadi polanya nyata dan bukan artefak satu metode

### Artinya untuk risiko kredit

> Sinyal positif dari bureau eksternal — kredibilitas terdokumentasi di sistem credit bureau pihak ketiga.

### Yang sebaiknya dilakukan

> Pakai sebagai positive flag dalam scoring model — bobot tambahan untuk approval rate dan limit increase.

---

## Rule #12 — Cluster 3 Cc Intensif

```
{'age_senior', 'income_low', 'cluster_3_cc_intensif'} -> {'emp_new'}
```

| Metrik | Nilai |
|--------|-------|
| Support | 0.0560 (5.6%) |
| Confidence | 0.6256 (62.6%) |
| Lift | 2.2363 |
| Ditemukan di | `fpgrowth_cluster3` |
| Validasi lintas algoritma | hanya 1 algoritma |

### Apa isi rule ini

Jika sebuah aplikasi punya profil usia senior, pendapatan rendah, Pengguna CC Intensif (C3),
biasanya ia juga masa kerja baru (<3 thn).

### Mengapa layak dipercaya

- Asosiasi **moderat (2.24×)**
- Confidence **tinggi (62.6%)**
- terdapat di ~19,936 dari 356,255 aplikasi (5.6%)

### Artinya untuk risiko kredit

> Anomali kombinasi — usia senior dengan masa kerja baru biasanya = pensiunan yang baru mulai usaha kecil. Perlu validasi sumber pendapatan saat aplikasi.

### Yang sebaiknya dilakukan

> Tambahkan field verifikasi: "sumber pendapatan utama pensiun atau usaha baru?". Sesuaikan tenor maksimum dengan usia harapan kerja.

---

## Rule #13 — Cluster 4 Minimal

```
{'cluster_4_minimal', 'age_senior', 'burden_high'} -> {'credit_small', 'income_low'}
```

| Metrik | Nilai |
|--------|-------|
| Support | 0.0482 (4.8%) |
| Confidence | 0.8985 (89.8%) |
| Lift | 4.5955 |
| Ditemukan di | `apriori+eclat+fpgrowth+fpgrowth_cluster4` |
| Validasi lintas algoritma | ya, ditemukan 4 algoritma |

### Apa isi rule ini

Jika sebuah aplikasi punya profil Peminjam Minimal (C4), usia senior, rasio cicilan-pendapatan tinggi,
biasanya ia juga jumlah kredit kecil, pendapatan rendah.

### Mengapa layak dipercaya

- Asosiasi **kuat (lift 4.60×)**
- Confidence **sangat tinggi (89.8%)**
- terdapat di ~17,179 dari 356,255 aplikasi (4.8%)
- Ditemukan oleh 4 algoritma yang cara kerjanya berbeda, jadi polanya nyata dan bukan artefak satu metode

### Artinya untuk risiko kredit

> Risiko likuiditas — meski nominal kecil, beban cicilan relatif berat. Sensitif terhadap shock pendapatan kecil sekalipun.

### Yang sebaiknya dilakukan

> Cocok untuk produk micro-credit dengan tenor pendek + financial literacy program. Pemantauan ringan cukup.

---

## Rule #14 — Cluster 4 Minimal

```
{'emp_new', 'cluster_4_minimal', 'burden_high'} -> {'income_low'}
```

| Metrik | Nilai |
|--------|-------|
| Support | 0.0615 (6.1%) |
| Confidence | 0.9376 (93.8%) |
| Lift | 2.7207 |
| Ditemukan di | `apriori+eclat+fpgrowth+fpgrowth_cluster4` |
| Validasi lintas algoritma | ya, ditemukan 4 algoritma |

### Apa isi rule ini

Jika sebuah aplikasi punya profil masa kerja baru (<3 thn), Peminjam Minimal (C4), rasio cicilan-pendapatan tinggi,
biasanya ia juga pendapatan rendah.

### Mengapa layak dipercaya

- Asosiasi **moderat (2.72×)**
- Confidence **sangat tinggi (93.8%)**
- terdapat di ~21,905 dari 356,255 aplikasi (6.1%)
- Ditemukan oleh 4 algoritma yang cara kerjanya berbeda, jadi polanya nyata dan bukan artefak satu metode

### Artinya untuk risiko kredit

> Pola karakteristik dari segmen profil peminjam mikro berpenghasilan rendah dengan kebutuhan kredit kecil; mengkonfirmasi profil segmentasi.

### Yang sebaiknya dilakukan

> Cocok untuk produk micro-credit dengan tenor pendek + financial literacy program. Pemantauan ringan cukup.

---

## Rule #15 — Cluster 4 Minimal

```
{'risk_score_med', 'cluster_4_minimal', 'burden_high'} -> {'income_low'}
```

| Metrik | Nilai |
|--------|-------|
| Support | 0.0450 (4.5%) |
| Confidence | 0.9251 (92.5%) |
| Lift | 2.6842 |
| Ditemukan di | `apriori+eclat+fpgrowth+fpgrowth_cluster4` |
| Validasi lintas algoritma | ya, ditemukan 4 algoritma |

### Apa isi rule ini

Jika sebuah aplikasi punya profil skor eksternal menengah, Peminjam Minimal (C4), rasio cicilan-pendapatan tinggi,
biasanya ia juga pendapatan rendah.

### Mengapa layak dipercaya

- Asosiasi **moderat (2.68×)**
- Confidence **sangat tinggi (92.5%)**
- terdapat di ~16,027 dari 356,255 aplikasi (4.5%)
- Ditemukan oleh 4 algoritma yang cara kerjanya berbeda, jadi polanya nyata dan bukan artefak satu metode

### Artinya untuk risiko kredit

> Pola karakteristik dari segmen profil peminjam mikro berpenghasilan rendah dengan kebutuhan kredit kecil; mengkonfirmasi profil segmentasi.

### Yang sebaiknya dilakukan

> Cocok untuk produk micro-credit dengan tenor pendek + financial literacy program. Pemantauan ringan cukup.

---

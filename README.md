# Home Credit Default Risk, proyek KDD (Phase 1 - 5)

Proyek data mining akademik dengan metodologi KDD (Knowledge Discovery in Databases) pada dataset Home Credit Default Risk. Seluruh 356.255 aplikasi dipakai (train 307.511 + test 48.744, digabung karena prosesnya unsupervised) bersama 5 tabel relasional yang terbesar berisi 27,3 juta baris.

## Struktur folder

```
.
├── datasets/                         # CSV mentah (Kaggle) + output Phase 1
│   ├── application_train.csv         # 307K baris, 122 kolom + TARGET
│   ├── application_test.csv          # 48K baris
│   ├── bureau.csv, bureau_balance.csv
│   ├── credit_card_balance.csv, installments_payments.csv
│   ├── POS_CASH_balance.csv, previous_application.csv
│   └── final/
│       ├── features_clustering.csv   # Output Phase 1 (356.255 x SK_ID_CURR + 65 fitur)
│       ├── cluster_labels.csv        # Output Phase 2 (ROW_ID + SK_ID_CURR + label 3 algoritma)
│       └── cluster_names.csv         # Output Phase 2: pemetaan cluster_id -> nama bisnis.
│                                     #   Downstream WAJIB membaca file ini karena nomor
│                                     #   cluster bisa berubah antar run.
│
├── docs/                             # Kriteria proyek (PDF)
│
├── notebooks/
│   ├── exploratory_data_analysis.ipynb   # EDA Phase 1
│   ├── phase2_clustering.ipynb           # Phase 2, segmentasi
│   ├── phase3_association.ipynb          # Phase 3, rule mining (full data)
│   └── phase4_anomaly.ipynb              # Phase 4, deteksi anomali (full data)
│
├── src/
│   ├── run_pipeline.py               # Entry point Phase 1. Prefect flow; jatuh ke
│   │                                 #   Python biasa bila Prefect tidak terpasang
│   └── pipeline/                     # 10 step modular; config.py berisi semua threshold
│                                     #   beserta justifikasi EDA-nya
│
├── dashboard/
│   └── app.py                        # Phase 5, dashboard interaktif Plotly Dash
│
├── reports/                          # Laporan yang ditulis manual
│   ├── knowledge_discovery_report.md # Jawaban pertanyaan inti untuk pembaca bisnis
│   ├── validation_report.md          # Audit proses end-to-end + defect yang diperbaiki
│   └── presentation_outline.md       # Kerangka presentasi 10 menit + jawaban Mining Expo
│
└── results/                          # Artefak per fase, semuanya hasil generate ulang
    ├── phase1_preprocessing/
    ├── phase2_clustering/
    ├── phase3_association/
    └── phase4_anomaly/
```

## Setup

```bash
python -m venv env
./env/Scripts/activate           # Windows
source env/bin/activate          # Linux/Mac
pip install -r requirements.txt
```

## Cara menjalankan (urutannya wajib)

```bash
# Phase 1, preprocessing (skrip pipeline, orkestrasi Prefect)       ~13 menit
PYTHONIOENCODING=utf-8 python src/run_pipeline.py

# Phase 2, clustering                                                ~6 menit
PYTHONIOENCODING=utf-8 jupyter nbconvert --to notebook --execute --inplace notebooks/phase2_clustering.ipynb --ExecutePreprocessor.timeout=2400

# Phase 3, association rules                                         ~4 menit
PYTHONIOENCODING=utf-8 jupyter nbconvert --to notebook --execute --inplace notebooks/phase3_association.ipynb --ExecutePreprocessor.timeout=2400

# Phase 4, deteksi anomali                                           ~8 menit
PYTHONIOENCODING=utf-8 jupyter nbconvert --to notebook --execute --inplace notebooks/phase4_anomaly.ipynb --ExecutePreprocessor.timeout=3600

# Phase 5, dashboard
python dashboard/app.py          # buka http://127.0.0.1:8050
```

Phase 3 dan 4 punya pengaman: bila cluster_labels.csv tidak sejalan dengan features_clustering.csv (artefak basi dari run lama), eksekusi langsung gagal dengan pesan jelas. Solusinya jalankan ulang Phase 2.

## Ringkasan hasil run final

Phase 1 mengubah 7 CSV mentah menjadi 356.255 baris dengan 65 fitur numerik terstandardisasi tanpa NaN, plus kolom SK_ID_CURR sebagai identitas. Seleksi fitur memakai dua ukuran sesuai rubrik: korelasi Pearson (trio fitur dengan r mendekati 1,0 dibuang; tersisa 2 pasangan yang terdokumentasi) dan mutual information berbasis entropy terhadap TARGET.

Phase 2 menemukan 5 segmen lewat K-Means (K=5, dipilih berdasarkan elbow dan silhouette), divalidasi hierarchical clustering (BIRCH lalu Ward, dendrogram 3 linkage). Reduksi dimensi dipisah sesuai algoritma: K-Means dan hierarchical memakai PCA 9 komponen (di bawah 10, dipilih dari titik belok scree), sedangkan DBSCAN dijalankan di embedding UMAP 2D karena ia berbasis kepadatan, dengan eps otomatis dari knee k-distance. Pemetaan nomor cluster ke nama tersimpan di cluster_names.csv karena penomoran bisa berubah antar run.

Phase 3 menjalankan Apriori, FP-Growth, dan ECLAT pada seluruh 356.255 transaksi. Ketiganya menemukan 1.204 rules yang persis sama, ditambah 1.236 rules per segmen. Lima belas rule final dipilih (tiga per segmen, saringan redundansi Jaccard), lift 1,84 sampai 4,59, masing-masing dengan interpretasi empat bagian.

Phase 4 mengevaluasi seluruh aplikasi dengan IQR, Z-score, dan Isolation Forest, lalu mencocokkannya dengan noise DBSCAN (ruang UMAP) dari Phase 2. Hasilnya 5.359 anomali high-confidence, semuanya diinvestigasi dengan ID pemohon nyata. Tiap kasus diberi dua label: jenis teori (global 3.766, kontekstual 1.493, kolektif 100) dan tipe bisnis (kesalahan data 3.215, langka tapi sah 2.005, sinyal risiko 139), plus rekomendasi sesuai segmennya. Uji silang terhadap TARGET (yang tidak pernah dipakai saat mining) menunjukkan default naik bertingkat dari 6,88% di kelompok normal sampai 12,92% di anomali kuat.

Phase 5 berupa dashboard Plotly Dash untuk presentasi ke klien bisnis dan tiga laporan markdown di folder reports. Dashboard membaca semua angka dari folder results, jadi run ulang otomatis menyinkronkan tampilannya.

## Pemetaan ke kriteria PDF

| Phase | Kriteria | Implementasi |
|---|---|---|
| 1 | Cleaning, transformasi, seleksi fitur korelasi + entropy, pipeline | Pipeline Prefect 10 step; mutual_info_classif; audit korelasi |
| 2 | K-Means + DBSCAN + Hierarchical, Elbow + Silhouette, profiling | Semua, plus dendrogram 3 linkage dan artefak pemetaan nama |
| 3 | Diskretisasi, Apriori, support/confidence/lift, 10+ rules, interpretasi | 15 rules, 3 algoritma saling mengkonfirmasi, interpretasi spesifik |
| 4 | IQR + Z-score + Isolation Forest, cross-ref Phase 2, tipologi | Semua pada full data; kerangka global/contextual/collective + tipe bisnis A/B/C; investigasi per kasus dengan ID nyata & rekomendasi per segmen |
| 5 | Dashboard, knowledge report, presentasi | Plotly Dash + 3 laporan manual |

## Catatan teknis

Selalu jalankan dengan PYTHONIOENCODING=utf-8 di Windows agar log tidak error karakter. Hierarchical clustering pada 356 ribu baris tidak mungkin memakai memori kuadratik, jadi dipakai BIRCH untuk meringkas ke 500 micro-centroid lebih dulu; DBSCAN dibatasi sample 50 ribu dengan alasan serupa. Semua random seed bernilai 42, sehingga pengelompokan stabil antar run, tapi nomor urut cluster tidak; selalu baca cluster_names.csv. SK_ID_CURR mengalir dari pipeline sampai investigasi anomali sehingga setiap temuan bisa ditelusuri ke pemohon aslinya.

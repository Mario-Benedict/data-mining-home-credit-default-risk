# Laporan validasi end-to-end, KDD Phase 1 sampai 5

Dataset: Home Credit Default Risk.
Tanggal validasi: 10 Juni 2026.
Lingkup: audit seluruh proses dari EDA, Phase 1 (preprocessing), Phase 2 (clustering), Phase 3 (association rules), Phase 4 (anomaly detection), sampai Phase 5 (dashboard dan knowledge report), termasuk perbaikan defect dan menjalankan ulang semuanya dari nol.

## Ringkasan

Audit menemukan dua defect kritis dan tiga kelemahan metodologis pada hasil yang tersimpan sebelumnya. Yang paling serius: hasil Phase 3 dan Phase 4 lama ternyata dibangun di atas join antar-file yang korup, sehingga harus dianggap tidak valid. Semua masalah sudah diperbaiki, seluruh pipeline dijalankan ulang, dan hasil akhirnya lolos 31 pemeriksaan konsistensi lintas-artefak.

| # | Temuan | Tingkat | Status |
|---|--------|---------|--------|
| 1 | cluster_labels.csv basi (331.219 baris) di-join secara posisi dengan feature matrix baru (356.255 baris) | Kritis | Diperbaiki, dijalankan ulang |
| 2 | Nama cluster di Phase 3 di-hardcode dan tidak cocok dengan profil aktual Phase 2 | Kritis | Diperbaiki, dijalankan ulang |
| 3 | Tiga fitur berkorelasi sempurna (r mendekati 1,0) semuanya dipertahankan | Metodologis | Diperbaiki |
| 4 | Phase 3 dan 4 hanya memakai sample 50 ribu dari 356 ribu aplikasi | Metodologis | Sekarang full data |
| 5 | Tidak ada SK_ID_CURR di feature matrix, jadi hasil tidak bisa ditelusuri ke pemohon nyata | Metodologis | Diperbaiki |
| 6 | Notebook EDA punya satu sel error (API seaborn lama) dan satu sel yang belum pernah dieksekusi | Minor | Dieksekusi ulang, bersih |

## Defect 1: artefak basi dan join berbasis posisi

File label cluster berisi 331.219 baris, sementara feature matrix hasil pipeline berisi 356.255 baris (307.511 train ditambah 48.744 test). Phase 3 dan Phase 4 menggabungkan keduanya lewat inner join pada ROW_ID, yang sebenarnya hanya nomor urut baris. Akibatnya ada dua masalah sekaligus: 25.036 aplikasi terbuang diam-diam, dan baris ke-N di file label belum tentu pemohon yang sama dengan baris ke-N di file fitur.

Kenapa bisa terjadi? Label ditulis oleh run Phase 2 yang lebih lama, atas versi feature matrix yang berbeda. Phase 1 kemudian dijalankan ulang tanpa menjalankan ulang Phase 2, dan tidak ada satu pun pemeriksaan yang menangkap ketidaksesuaian itu. Inner join justru menyembunyikannya: program tetap jalan, hasil tetap keluar, hanya saja salah.

Perbaikannya tiga lapis. Phase 2 dijalankan ulang atas feature matrix terbaru. Sel pemuatan data di Phase 3 dan Phase 4 sekarang berisi assert yang membandingkan jumlah baris kedua file, jadi kalau artefak basi lagi, eksekusi langsung gagal dengan pesan jelas alih-alih diam-diam membuang baris. Dan SK_ID_CURR sekarang ikut tersimpan di file label, sehingga join berbasis ID nyata selalu bisa dilakukan.

## Defect 2: nama cluster yang di-hardcode

Phase 3 menuliskan pemetaan nomor cluster ke nama segmen langsung di kode: cluster 1 disebut "minimal", cluster 2 "cc_intensif", cluster 3 "ambisius". Padahal business report Phase 2 yang tersimpan menyebut cluster 1 itu "Ambisius", cluster 2 "Minimal", cluster 3 "CC Intensif". Rules jadi dikaitkan ke segmen yang salah.

Akar masalahnya: K-Means menghasilkan pengelompokan yang stabil antar-run (karena seed tetap), tapi nomor urut clusternya tidak dijamin sama. Kami menyaksikannya sendiri selama audit ini: tiga run menghasilkan tiga permutasi penomoran yang berbeda. Hardcoding nama cluster di downstream cepat atau lambat pasti salah.

Sekarang Phase 2 menulis artefak cluster_names.csv yang memetakan nomor cluster ke nama bisnis, slug, profil risiko, dan ukuran segmen. Phase 3, Phase 4, dan dashboard membaca artefak ini. Tidak ada lagi nama segmen yang ditulis tangan di kode downstream.

## Perbaikan metodologis

### Multikolinearitas sempurna

Audit korelasi menemukan trio fitur dengan r mendekati 1,0: FLAG_SENTINEL_EMPLOYED, ORGANIZATION_TYPE_Unknown, dan NAME_INCOME_TYPE_Pensioner. Ketiganya menyimpan informasi yang sama, yaitu "pemohon ini pensiunan atau tidak bekerja". Logikanya sederhana: kalau DAYS_EMPLOYED berisi nilai sentinel, orang itu tidak punya pemberi kerja, maka kolom organisasinya XNA dan tipe pendapatannya pensiunan.

Membiarkan ketiganya berarti dimensi "pensiunan" dihitung tiga kali setiap kali algoritma mengukur jarak antar nasabah. Itu bertentangan dengan tujuan feature selection berbasis korelasi. Pipeline sekarang membuang dua dummy yang redundan setelah one-hot encoding dan mempertahankan FLAG_SENTINEL_EMPLOYED sebagai penanda tunggal. Pasangan korelasi tinggi yang tersisa turun dari lima menjadi dua, dan keduanya bisa dipertanggungjawabkan: rata-rata dan maksimum dari metrik yang sama, serta dua dummy pendidikan yang memang saling melengkapi.

### Cakupan data penuh

Phase 3 sekarang menambang seluruh 356.255 transaksi, bukan sample 50 ribu. Hasil menariknya: Apriori, FP-Growth, dan ECLAT masing-masing menemukan 1.204 rules yang persis sama. Phase 4 juga mengevaluasi seluruh 356.255 aplikasi dengan IQR, Z-score, dan Isolation Forest. Sample DBSCAN di Phase 2 dinaikkan dari 30 ribu ke 50 ribu supaya cross-referencing Phase 4 punya cakupan lebih luas. Train dan test digabung sejak awal karena seluruh proses unsupervised; tidak ada label yang bocor karena memang tidak ada label yang dipakai.

### Penelusuran ke pemohon nyata

SK_ID_CURR sekarang mengalir dari pipeline ke label cluster sampai ke investigasi anomali, sebagai kolom identitas yang tidak ikut di-scale dan tidak ikut dihitung dalam seleksi fitur. Dampak praktisnya: laporan investigasi Phase 4 menunjuk ID pemohon sungguhan yang bisa dicari di sistem, dan penyelarasan TARGET untuk mutual information dilakukan lewat join ID, bukan asumsi urutan baris.

### Orkestrasi pipeline

Dokumen proyek mensyaratkan Mage, Prefect, atau Airflow untuk pipeline. run_pipeline.py sekarang membungkus sepuluh step sebagai task Prefect dalam satu flow, teruji jalan dengan Prefect 3.7.4. Kalau Prefect tidak terpasang, pipeline tetap jalan sebagai skrip Python biasa.

## Hasil run final

### Phase 1, preprocessing (805 detik)

| Pemeriksaan | Hasil |
|-------------|-------|
| Input | 7 CSV mentah, termasuk tabel relasional sampai 27,3 juta baris |
| Output | features_clustering.csv: 356.255 baris, SK_ID_CURR + 65 fitur numerik terstandardisasi |
| NaN tersisa | 0 |
| Pasangan korelasi di atas 0,85 | 2, keduanya terdokumentasi dengan justifikasi |
| Mutual information vs TARGET | 65 fitur, diselaraskan lewat join ID pada 307.511 baris train |

### Phase 2, clustering (eksekusi penuh, nol error)

| Pemeriksaan | Hasil |
|-------------|-------|
| PCA | 10 komponen, 54,5% variance |
| Pemilihan K | Elbow menunjuk K=5; silhouette K=5 (0,1494) terbaik di antara K minimal 3 |
| K-Means full data | silhouette 0,1495; inertia 5.083.583 |
| DBSCAN | sample 50.000, eps 3,0, min_samples 10; 739 noise (1,5%) |
| Hierarchical | BIRCH ke 500 micro-centroid, lalu linkage ward, complete, dan average dengan dendrogram |
| Segmen | Minimal 35,6%; Ambisius 35,0%; Veteran 13,1%; Bermasalah 1,0%; CC Intensif 15,2% |

### Phase 3, association rules (full data, nol error)

| Pemeriksaan | Hasil |
|-------------|-------|
| Transaksi | 356.255, didiskretisasi ke 7 dimensi (income, usia, masa kerja, skor eksternal, kredit, beban, cluster) |
| Tiga algoritma | 1.204 rules dari masing-masing, identik satu sama lain |
| FP-Growth per cluster | 1.236 rules |
| Rules final | 15 (tiga per segmen, saringan redundansi Jaccard 0,65), lift 1,84 sampai 4,59 |
| Interpretasi | Empat bagian per rule, nama segmen dibaca dari artefak Phase 2 |

### Phase 4, anomaly detection (full data, nol error)

| Pemeriksaan | Hasil |
|-------------|-------|
| Dievaluasi | 356.255 aplikasi; IQR 1,5 kali; Z-score di atas 3; Isolation Forest contamination 0,01 / 0,05 / 0,10 |
| High-confidence (minimal 3 metode) | 10.911, atau 3,1% |
| Tervalidasi silang DBSCAN | 587 |
| Tipologi | Data Error 6.084; Rare but Valid 4.617; Risk Signal 210 |
| Investigasi | Semua 10.911 ada di CSV dengan SK_ID_CURR; log markdown merinci 300 kasus paling ekstrem |

### Phase 5, dashboard dan laporan

Dashboard Plotly Dash teruji boot dan merespons HTTP 200 di port 8050. Semua angkanya dibaca dari artefak results, jadi menjalankan ulang pipeline otomatis menyinkronkan dashboard. Knowledge discovery report ditulis manual di reports/knowledge_discovery_report.md.

## Validasi silang terhadap TARGET

TARGET tidak pernah dipakai selama mining. Ia hanya dipakai setelah semuanya selesai, untuk menguji apakah struktur yang ditemukan benar-benar berhubungan dengan risiko nyata. Hasilnya pada 307.511 baris train:

| Struktur yang ditemukan | Default rate aktual |
|--------------------------|---------------------|
| Baseline populasi | 8,07% |
| Segmen Bermasalah | 11,43% |
| Segmen CC Intensif | 10,79% |
| Segmen Veteran | 9,24% |
| Segmen Minimal | 8,35% |
| Segmen Ambisius | 6,16% |
| Tier anomali: normal, lemah, moderat, high-confidence | 7,25% / 8,12% / 9,38% / 11,17% |
| Noise DBSCAN | 11,98% |
| Anomali Tipe C (Risk Signal) | 13,47% |

Gradien tier anomali naik secara monoton tanpa satu pun pengecualian. Untuk proses yang tidak pernah melihat label, itu bukti kuat bahwa struktur yang ditemukan nyata, bukan artefak statistik.

## Pengaman agar defect tidak terulang

Empat hal sekarang menjaga konsistensi proses. Assert alignment di sel pemuatan Phase 3 dan 4 membuat artefak basi langsung menggagalkan eksekusi. Artefak cluster_names.csv menjadi satu-satunya sumber nama segmen untuk semua downstream. SK_ID_CURR tersedia di semua artefak antar-phase sehingga join berbasis ID selalu mungkin. Dan dashboard membaca seluruh angkanya dari folder results, tanpa satu pun angka yang ditulis tangan.

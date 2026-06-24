# Outline presentasi 10 menit

Lima anggota, masing-masing membawakan fasenya sendiri. Alat bantu: dashboard live (`python dashboard/app.py`) atau screenshot dari folder results.

| Menit | Bagian | Pembawa | Isi |
|-------|--------|---------|-----|
| 0 - 1 | Pembuka | Insight Communicator | 356 ribu aplikasi, 7 tabel, 27 juta baris riwayat perilaku. Pertanyaannya satu: apa yang tersembunyi di dalamnya? |
| 1 - 2,5 | Phase 1, data dan preprocessing | Data Engineer 1 | Pipeline 10 step (Prefect) mengubah 7 CSV menjadi 65 fitur bersih. Keputusan paling penting: menangani nilai sentinel DAYS_EMPLOYED yang menimpa 18% populasi, meringkas 5 tabel relasional ke level pemohon, dan membuang trio fitur berkorelasi sempurna yang ketahuan lewat audit korelasi |
| 2,5 - 4,5 | Phase 2, segmentasi | Segmentation Specialist | Elbow dan silhouette sama-sama menunjuk K=5. Tiga algoritma dijalankan: K-Means, DBSCAN, dan hierarchical (BIRCH lalu Ward). Lima segmen bernama. Angka yang bikin orang berhenti: peminjam terbesar justru default terendah, 6,16% |
| 4,5 - 6,5 | Phase 3, association rules | Pattern Analyst | Tujuh dimensi didiskretisasi, lalu Apriori, FP-Growth, dan ECLAT masing-masing menemukan 1.204 rules yang persis sama. Dari sana dipilih 15 rule final. Contoh terkuat: senior dengan beban berat di segmen Minimal, terjadi 4,6 kali lebih sering dari kebetulan. Segmen Bermasalah punya rule berakurasi 99% |
| 6,5 - 8,5 | Phase 4, anomali | Data Engineer 2 | Tiga metode plus cek silang DBSCAN, dijalankan ke seluruh data. 10.911 anomali high-confidence, dipilah jadi tiga tipe dengan tindak lanjut berbeda. Angka penutup: default naik bertingkat dari 7,25% (normal) ke 11,17% (anomali kuat), padahal deteksinya buta label |
| 8,5 - 10 | Sintesis | Insight Communicator | Tiga temuan, lima rekomendasi, demo dashboard 30 detik |

## Jawaban untuk Mining Expo

### Rule mana yang paling mengejutkan, dan mengapa?

"Kredit kecil dengan beban berat berarti pendapatan rendah", akurat 98,3% dan mencakup 10,6% populasi. Intuisi awam bilang pinjaman besar itu yang bahaya. Data bilang sebaliknya dua kali: segmen berkredit terbesar default-nya paling rendah, dan justru pinjaman-pinjaman kecil menyimpan sub-populasi yang rapuh terhadap guncangan, karena pendapatannya juga kecil.

### Metode clustering mana yang paling interpretable untuk dataset ini?

K-Means dengan K=5. Segmennya bersih dan mudah dinamai karena fitur sudah melalui PCA dan standardisasi. Hierarchical (BIRCH lalu Ward) menunjukkan struktur lima cluster yang sama di dendrogram, jadi berfungsi sebagai validasi. DBSCAN kurang cocok sebagai pembagi segmen di data ini (hasilnya satu cluster raksasa plus pinggiran), tapi sangat berguna sebagai detektor noise: 739 titik yang ditandainya punya default 11,98%.

### Anomali apa yang ditemukan, dan apa artinya di konteks bank nyata?

Tiga jenis dengan nasib berbeda. Kesalahan input data (6.084 kasus) yang harus dicegat di ETL sebelum merusak model. Profil langka tapi sah (4.617) yang justru peluang bisnis bila dialihkan ke layanan prioritas alih-alih ditolak mesin. Dan sinyal risiko murni (210) dengan default aktual 13,47% yang harus melewati review manual. Pelajarannya: anomali bukan satu keranjang "buang semua"; tiap tipe butuh respons yang berbeda.

### Bagaimana temuan ini dibanding kelompok lain di domain banking berbeda?

Metodologinya sama persis, lima fase KDD, tapi makna temuannya dibentuk konteks domain. Di credit risk, anomali terpecah jadi tiga tipe dengan respons berbeda. Di fraud atau AML, hampir semua anomali adalah bahan investigasi. Segmentasi juga begitu: segmen kami adalah "kepribadian kredit", sedangkan di churn banking segmen biasanya tahapan siklus hidup nasabah. Teknik yang sama, pengetahuan yang berbeda.

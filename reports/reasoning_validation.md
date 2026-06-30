# Validasi Logika dan Reasoning Tiap Fase

Dokumen ini menilai **kebenaran penalaran** di balik setiap keputusan, bukan sekadar memastikan skrip berjalan. Untuk tiap fase saya tuliskan: apa yang diputuskan, mengapa itu benar, dan apa yang diperbaiki pada putaran ini.

Angka final per fase ada di `reports/validation_report.md`. Di sini fokusnya logika.

---

## Phase 1 — Preprocessing

### Keputusan encoding kategorikal: yang paling penting diperbaiki

Putaran ini mengganti satu pilihan yang keliru untuk clustering. Sebelumnya tiga variabel kategorikal di-**one-hot encode** (OHE): `NAME_EDUCATION_TYPE`, `NAME_INCOME_TYPE`, dan `ORGANIZATION_TYPE`. Hasilnya sekitar 21 kolom biner sparse di ruang fitur.

Mengapa itu salah untuk clustering? K-Means mengukur jarak Euclidean. OHE merusaknya dua kali. Pertama, ia menambah banyak sumbu biner yang bila digabung lebih berat daripada satu fitur kontinu sungguhan, sehingga "sektor pekerjaan" diam-diam mengalahkan "rasio cicilan terhadap pendapatan". Kedua, ia memaksa setiap kategori berjarak sama dari setiap kategori lain. Padahal "Higher education" jelas lebih dekat ke "Incomplete higher" daripada ke "Lower secondary". OHE membuang fakta itu.

Perbaikannya mencocokkan encoding dengan sifat variabel:

- `NAME_EDUCATION_TYPE` menjadi **ordinal 0–4** (Lower secondary sampai Academic degree). Pendidikan punya urutan nyata. Section 9 EDA menunjukkan gradien bersih antara jenjang pendidikan dan besar pinjaman, jadi satu integer terurut itu jujur sekaligus ringkas.
- `NAME_INCOME_TYPE` dan `ORGANIZATION_TYPE` menjadi **frequency encoding**. Keduanya nominal tanpa urutan, jadi masing-masing menjadi satu sumbu "umum sampai langka" alih-alih belasan dummy sparse.

Bonus logis: pendekatan ini menghapus kolinearitas sempurna yang muncul pada run lama (`FLAG_SENTINEL_EMPLOYED` ≡ `ORGANIZATION_TYPE_Unknown` ≡ `NAME_INCOME_TYPE_Pensioner`, r ≈ 1,0). Kolinearitas itu lahir justru karena OHE pada kategori "Unknown" yang berimpit dengan kelompok pensiunan. Pensiunan tetap teridentifikasi terpisah lewat `FLAG_SENTINEL_EMPLOYED`, jadi tidak ada informasi yang hilang.

Dampak: jumlah fitur turun dari 65 menjadi 47. Ruang yang lebih ringkas dan lebih sedikit sumbu noise adalah ruang yang lebih baik untuk algoritma berbasis jarak.

### Bug laten yang ikut ketahuan dan diperbaiki

Saat menulis ulang encoding, terlihat deteksi "kolom biner" di step9 memakai `dtype == int8`. Akibatnya kolom ordinal kecil seperti `DEF_30_CNT_SOCIAL_CIRCLE_BIN` (nilai 0/1/2) **tidak ikut di-scale**, sehingga rentangnya diam-diam melebihi fitur lain yang sudah standar. Setelah education menjadi ordinal int8 0–4, bug yang sama akan menimpanya. Deteksi diperbaiki: sekarang berbasis himpunan nilai, hanya kolom yang benar-benar {0,1} yang dibiarkan apa adanya, ordinal ikut di-scale. Ini memperbaiki bobot jarak yang sebelumnya timpang.

### Reasoning langkah-langkah lain (divalidasi, tetap)

- **Sentinel `DAYS_EMPLOYED = 365.243`.** Nilai 1.000 tahun dalam hari, menimpa 18% data, semuanya pensiunan/penganggur. Di-flag lalu di-NaN-kan. Benar: membiarkannya sebagai angka akan merusak setiap perhitungan jarak. Default rate 5,4% vs 8,7% membuktikan ia menandai keadaan nyata, bukan error.
- **Log transform pada AMT_INCOME/CREDIT/ANNUITY.** Income condong ekstrem (maks 247x median). Tanpa winsorize p99 + log, satu nasabah mendominasi semua jarak. Logis dan standar.
- **Triplikasi housing (`_AVG`/`_MODE`/`_MEDI`, r > 0,99).** Pertahankan `_MODE`, buang dua lainnya. Tanpa ini bobot atribut bangunan terhitung tiga kali. Benar.
- **DAYS ke tahun positif.** Nilai negatif tak bermakna dalam jarak. Benar.

### Handling missing value: divalidasi per konteks EDA

Tiap imputasi punya alasan yang cocok dengan sifat kekosongannya, bukan satu resep untuk semua:

- **Indikator dulu, baru isi.** `FLAG_NO_CAR`, `FLAG_NO_HOUSING_DATA`, `FLAG_EXT_SOURCE_1_MISSING` dibuat sebelum imputasi, supaya sinyal "data ini memang kosong" tidak terhapus oleh nilai isian. Ini prinsip yang tepat: di data perbankan, kosong sering membawa informasi.
- **Imputasi nol untuk ketiadaan struktural.** `OWN_CAR_AGE` kosong berarti tidak punya mobil, kolom MODE bangunan kosong berarti bukan apartemen. Nol di sini bermakna "tidak ada", bukan tebakan.
- **Imputasi median untuk kekosongan acak** (EXT_SOURCE_2/3, AMT_ANNUITY, dst.). Cocok untuk MCAR.
- **Group-mode untuk OCCUPATION_TYPE** (modus per tipe pendapatan). Lebih informatif daripada modus global karena pekerjaan berkorelasi dengan tipe pendapatan.
- **Agregat tabel relasional kosong menjadi 0.** Tidak ada catatan berarti tidak ada aktivitas. Benar.
- **ORGANIZATION_TYPE 'Unknown' (pensiunan)** kini menjadi kategori sah dalam frequency encoding, bukan dibuang. Konsisten dengan penanganan sentinel.

Satu catatan jujur soal `EXT_SOURCE_1` (56% kosong, di-median-impute + flag): mengisi median ke 56% data membuat mayoritas menumpuk di satu nilai. Untuk clustering ini agak menciptakan bidang padat buatan, tapi `FLAG_EXT_SOURCE_1_MISSING` memisahkan kelompok itu, dan nilai median bersifat netral sehingga tidak menarik cluster ke ekstrem. Membuang fitur ini berarti kehilangan prediktor terkuat untuk 44% yang punya skornya. Jadi median + flag adalah kompromi yang dipertahankan secara sadar.

### Feature selection: korelasi + entropy (sesuai dokumen)

Dokumen proyek mewajibkan seleksi fitur dengan korelasi DAN entropy. Keduanya ada: audit korelasi Pearson (pasangan r > 0,85 didokumentasikan, yang sempurna dibuang) dan mutual information terhadap TARGET (berbasis entropy, menangkap hubungan non-linear). Reasoning tetap valid: fitur ber-MI rendah tidak otomatis dibuang karena clustering tak harus mengikuti sinyal supervised, tetapi MI berfungsi sebagai bukti formal pemenuhan rubrik.

---

## Phase 2 — Clustering

### Reduksi dimensi: dua ruang untuk dua tujuan (diperbaiki putaran ini)

Keputusan reduksi dimensi sekarang dipisah sesuai cara kerja masing-masing algoritma, bukan satu ukuran untuk semua.

K-Means dan hierarchical memakai **PCA dengan 9 komponen** (di bawah 10). Angka 9 bukan bulat sembarangan: pada scree plot, sumbangan tiap komponen menurun landai lalu jatuh lebih tajam dari PC9 (3,59%) ke PC10 (2,86%), jadi komponen ke-10 dan seterusnya menambah sangat sedikit. Sembilan komponen menjaga nyaris seluruh sinyal varians sambil memenuhi batas dimensi yang diminta dan tetap ringkas untuk jarak Euclidean.

DBSCAN sekarang dijalankan di **embedding UMAP 2D**, bukan PCA. Alasannya prinsipiil: DBSCAN berbasis kepadatan, sedangkan PCA hanya menjaga varians linear dan cenderung memipihkan gumpalan padat, sehingga DBSCAN di ruang PCA dulu hanya melihat satu massa besar. UMAP memetakan struktur manifold non-linear sambil mempertahankan kepadatan lokal: gumpalan tetap rapat dan titik yang benar-benar terpencil terlihat sebagai noise. Jadi pembagian tugasnya jelas, PCA untuk yang berbasis varians (K-Means, hierarchical), UMAP untuk yang berbasis kepadatan (DBSCAN). Nilai `eps` tidak ditebak manual: dipilih otomatis dari titik belok kurva k-distance, heuristik baku DBSCAN (Ester dkk., 1996), persis trik elbow yang dipakai memilih K.

### Pemilihan K: logikanya benar

Elbow dan silhouette dijalankan pada K = 2..10. Silhouette biasanya memuncak di K = 2, tetapi dua segmen terlalu kasar untuk keputusan bisnis. Elbow menunjuk K = 5, dan K = 5 adalah silhouette terbaik di antara K yang cukup granular (K ≥ 3). Reasoning ini benar: silhouette tertinggi absolut bukan satu-satunya kriteria; granularitas yang dapat ditafsirkan bisnis adalah pertimbangan sah dan dinyatakan eksplisit.

### Tiga algoritma, peran berbeda (benar)

- **K-Means** pada seluruh data sebagai segmentasi utama.
- **DBSCAN** (di ruang UMAP) sebagai detektor noise dan kantong kepadatan, bukan pembagi segmen utama. Di embedding UMAP, gumpalan padat terpisah lebih jelas, sehingga titik noise yang dihasilkan lebih bermakna sebagai kandidat outlier yang diteruskan ke Phase 4.
- **Hierarchical** (BIRCH ke micro-centroid lalu Ward) sebagai validasi struktur. Memakai BIRCH karena hierarchical murni pada 356K baris butuh memori O(n²) yang mustahil. Reasoning komputasi ini benar dan didokumentasikan.

### Profiling: dinamai manusia, bukan template

Nama segmen ditetapkan setelah membaca 10 fitur paling menyimpang per cluster, lalu divalidasi terhadap default rate aktual. Ini sesuai rubrik "named profile with business interpretation". Yang penting, penomoran cluster tidak deterministik antar run, jadi nama disimpan di artefak `cluster_names.csv` dan dibaca downstream. Logika ini sudah benar sejak perbaikan sesi sebelumnya.

Dengan ruang fitur baru yang lebih ringkas, struktur cluster diharapkan lebih bersih. Angka silhouette final dikonfirmasi setelah re-run.

---

## Phase 3 — Association Rules

### Diskretisasi: bermakna, bukan sembarang

Tujuh dimensi kontinu diubah ke kategori via `qcut` (kuantil), sehingga tiap bin berukuran seimbang dan tidak ada bin kosong. Reasoning benar: untuk aturan asosiasi, bin kuantil memberi support yang stabil. Bin diberi label bisnis (income_low/med/high, age_young/mid/senior, dst.), bukan rentang angka mentah, sehingga aturan langsung terbaca.

### Tiga algoritma sebagai validasi silang (benar)

Apriori, FP-Growth, dan ECLAT bekerja dengan mekanisme berbeda (level-wise, FP-tree, tidset vertikal). Ketiganya menemukan himpunan aturan yang sama persis. Logika konsistensi lintas algoritma ini kuat: bila tiga metode berbeda sepakat, aturan itu hampir pasti nyata, bukan artefak satu metode. Support, confidence, dan lift dihitung dan dipakai untuk memfilter. Memenuhi rubrik.

### Interpretasi spesifik per aturan (benar)

Tiap aturan final mendapat empat bagian: apa isinya dalam bahasa sehari-hari, mengapa layak dipercaya (lift/confidence/support), implikasi risikonya, dan tindak lanjutnya. Dibangun dari item aktual dalam aturan dan segmen targetnya, bukan kalimat template. Memenuhi kriteria "specific, accurate, actionable".

---

## Phase 4 — Anomaly Detection

### Tiga metode plus cross-reference (benar)

IQR, Z-score, dan Isolation Forest dijalankan pada seluruh data, lalu dicocokkan dengan noise DBSCAN dari Phase 2. Reasoning penggabungan benar: makin banyak metode independen sepakat sebuah aplikasi menyimpang, makin tinggi keyakinan ia benar-benar anomali, bukan kebetulan satu metode. Kombinasi metode berbasis kepadatan (DBSCAN) dan berbasis pohon (Isolation Forest) saling memperkuat.

### Dua lapis klasifikasi: teori + aksi (diperkuat putaran ini)

Tiap anomali kini diberi dua label yang saling melengkapi.

Lapis pertama adalah kerangka teori klasik outlier (Chandola dkk., 2009), yang memang baku di literatur anomaly detection:

- **Global (point)**: satu fitur ekstrem dibanding seluruh populasi. Karena fitur sudah terstandardisasi, |nilai| besar berarti jauh dari rata-rata global; inilah yang ditangkap IQR dan Z-score.
- **Contextual**: nilainya wajar secara umum, tetapi menyimpang tajam dari pola segmennya sendiri. Pemakaian kartu tinggi normal bagi "CC Intensif" tapi janggal bagi "Minimal". Jenis ini paling layak diselidiki sebagai sinyal risiko karena menandai nasabah yang tidak berperilaku seperti kelompoknya.
- **Collective**: bagian dari kantong kecil yang dipisahkan UMAP/DBSCAN dari massa utama; dipantau sebagai pola berulang, bukan kasus tunggal.

Lapis kedua adalah tipe bisnis yang menentukan aksi: Tipe A (kesalahan data, deviasi > 50x median segmen) diperbaiki di ETL; Tipe B (langka tapi sah) dialihkan ke layanan prioritas; Tipe C (sinyal risiko, kombinasi finansial kontradiktif) masuk review manual. Kedua lapis ini cocok dengan tipologi outlier yang sudah disiapkan di Section 6 EDA, dan tiap kasus mendapat rekomendasi yang disesuaikan dengan domain segmennya (mis. anomali di segmen Bermasalah langsung dieskalasi, di CC Intensif diperiksa lonjakan utilisasinya).

### Validasi terhadap TARGET (benar dan kuat)

Setelah semua selesai, default rate aktual dihitung per tingkat anomali. Gradien naik monoton dari normal sampai anomali kuat membuktikan deteksi menangkap risiko nyata, padahal tidak pernah melihat label. Ini bukti reasoning yang paling meyakinkan di seluruh proyek.

---

## Phase 5 — Dashboard dan Laporan

### Reasoning komunikasi (benar)

Dashboard membaca semua angka dari artefak `results/`, jadi tidak ada nilai yang ditulis tangan dan re-run otomatis menyinkronkan tampilan. Tab disusun mengikuti alur cerita bisnis (ringkasan eksekutif lebih dulu), nama kolom teknis diterjemahkan ke istilah bisnis, dan tiap grafik diberi keterangan cara membaca. Reasoning ini sesuai rubrik "accessible to a non-technical audience".

Tab dirender lazy karena memuat belasan grafik sekaligus membekukan browser. Scatter besar memakai WebGL. Keputusan teknis ini benar untuk presentasi langsung ke klien.

---

## Ringkasan perbaikan putaran ini

| Hal | Sebelum | Sesudah | Alasan |
|---|---|---|---|
| Encoding pendidikan | OHE (4 kolom, jarak sama antar jenjang) | Ordinal 0–4 | Pendidikan berjenjang; ordinal jujur dan ringkas |
| Encoding income & organization | OHE (~17 kolom sparse) | Frequency encoding (2 kolom) | Nominal; OHE mendominasi jarak Euclidean |
| Scaling ordinal | int8 tidak ikut di-scale (bug) | Ordinal ikut di-scale | Mencegah rentang ordinal mendominasi |
| Kolinearitas sempurna | Trio r ≈ 1,0 (artefak OHE) | Hilang | Pensiunan cukup ditandai satu flag |
| Jumlah fitur | 65 | 47 | Ruang lebih ringkas, lebih baik untuk clustering |
| Markdown EDA | Banyak tanda AI (em-dash, bold berlebih) | Prosa natural, reasoning tiap keputusan | Mudah dibaca, tetap detail |

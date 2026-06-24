# Knowledge Discovery Report: Home Credit Default Risk

Laporan Phase 5 untuk pembaca non-teknis.
Data yang diolah: 356.255 aplikasi kredit (seluruh data train dan test, digabung karena prosesnya unsupervised) ditambah lima tabel perilaku historis, yang terbesar berisi 27 juta baris.

## Pertanyaan yang harus dijawab

Apa yang kami temukan yang tidak terlihat dari data mentah?

Data mentah Home Credit memberitahu siapa pemohonnya dan berapa pinjamannya. Setelah lima fase KDD, kami menemukan tiga hal yang tidak mungkin terlihat dari tabulasi biasa. Ketiganya kemudian diuji terhadap default yang benar-benar terjadi, dan lolos, padahal label default sama sekali tidak dipakai selama proses penemuan.

## Temuan 1: nasabah terbagi alami menjadi lima "kepribadian kredit", dan pembedanya perilaku, bukan demografi

Tanpa diberi tahu apa pun soal gagal bayar, algoritma clustering menemukan lima kelompok:

| Segmen | Ukuran | Ciri yang paling membedakan | Default aktual |
|--------|--------|------------------------------|----------------|
| Peminjam Minimal | 35,6% | Kredit kecil, tenor pendek, beban rendah (nilai kredit 84% di bawah rata-rata) | 8,35% |
| Peminjam Ambisius | 35,0% | Kredit besar relatif terhadap pendapatan, umumnya peminjam baru | 6,16% |
| Veteran Aktif | 13,1% | Riwayat aplikasi sangat padat, sering ditolak | 9,24% |
| Peminjam Bermasalah | 1,0% | Keterlambatan bayar ekstrem di semua produk | 11,43% |
| Pengguna CC Intensif | 15,2% | Utilisasi kartu kredit dua sampai tiga kali rata-rata | 10,79% |

Baseline default populasi adalah 8,07%.

Bagian yang menarik, dan sejujurnya agak mengejutkan kami: segmen Ambisius, yang meminjam paling besar relatif terhadap pendapatannya, justru paling jarang gagal bayar. Sementara dua segmen dengan default tertinggi sama-sama dikenali dari jejak perilakunya: riwayat telat bayar (Bermasalah) dan ketergantungan pada kartu kredit (CC Intensif). Pesannya untuk kebijakan kredit cukup gamblang. Besarnya pinjaman bukan sinyal bahaya. Jejak perilaku masa lalu, yang tersebar di lima tabel terpisah dan baru kelihatan setelah digabungkan, itulah sinyalnya.

## Temuan 2: tiap segmen punya sidik jari yang konsisten di tiga algoritma berbeda

Kami menjalankan tiga algoritma pencari pola (Apriori, FP-Growth, ECLAT) atas data yang sama. Ketiganya bekerja dengan cara yang sangat berbeda, dan ketiganya menemukan 1.204 aturan yang persis sama. Itu cara kami memastikan pola yang dilaporkan memang ada di data, bukan keanehan satu metode.

Dari 1.204 itu, 15 aturan terkuat dipilih. Tiga contoh yang paling berguna:

Pertama, pemohon senior di segmen Minimal yang beban cicilannya berat hampir selalu berpendapatan rendah dengan kredit kecil (terjadi 4,6 kali lebih sering daripada kebetulan, akurat 89,7%). Ada sub-populasi pensiunan yang pinjamannya kecil tapi terasa berat bagi kantong mereka. Mereka kandidat program micro-credit dengan pendampingan, bukan kandidat penolakan.

Kedua, kredit kecil yang bebannya berat hampir pasti berarti pendapatan rendah (akurat 98,3%, mencakup 10,6% seluruh aplikasi). Nominal kecil sering dianggap otomatis aman. Data bilang sebaliknya: kalau pendapatannya juga kecil, pinjaman kecil pun berat.

Ketiga, pendapatan sangat tinggi di segmen Ambisius dengan beban tinggi hampir selalu berarti kredit besar. Kredit besar terkonsentrasi pada orang yang mampu menanggungnya, konsisten dengan Temuan 1.

Satu hal lagi yang layak dicatat: segmen Bermasalah punya aturan internal dengan akurasi 99,1%. Artinya perilaku gagal bayar kronis punya pola demografis-finansial yang sangat konsisten, dan pola itu bisa dipasang sebagai aturan deteksi dini di sistem underwriting.

## Temuan 3: "keanehan" statistik ternyata sinyal risiko yang berjenjang

Kami menjalankan tiga metode deteksi anomali (IQR, Z-score, Isolation Forest) plus pengecekan silang DBSCAN ke seluruh 356.255 aplikasi, lalu menghitung berapa metode yang sepakat untuk tiap aplikasi. Setelah selesai, kami baru membuka label default dan mengukur:

| Berapa metode yang sepakat | Default aktual |
|----------------------------|----------------|
| Tidak ada (normal) | 7,25% |
| Satu metode | 8,12% |
| Dua metode | 9,38% |
| Tiga atau empat metode (10.911 aplikasi) | 11,17% |

Tangganya naik terus tanpa pengecualian. Makin banyak metode yang menganggap sebuah aplikasi aneh, makin besar kemungkinan ia benar-benar gagal bayar. Padahal tidak satu pun metode itu pernah melihat label default.

Ke-10.911 anomali teratas kami investigasi satu per satu, dengan ID pemohon nyata, dan terbagi tiga jenis yang masing-masing butuh perlakuan berbeda:

6.084 kasus adalah kesalahan data: nilainya menyimpang lebih dari 50 kali median kelompoknya, hampir pasti salah input atau salah satuan. Tindak lanjutnya di tim data engineering, berupa validasi otomatis saat data masuk.

4.617 kasus ekstrem tapi masuk akal: nasabah dengan profil langka yang sah, sebagian berpotensi nasabah kelas atas. Menolak mereka otomatis berarti kehilangan bisnis; lebih tepat dialihkan ke layanan prioritas.

210 kasus adalah sinyal risiko murni: kombinasi finansial yang saling bertentangan, misalnya pendapatan rendah dengan kredit besar. Default aktual kelompok ini 13,47%, hampir 1,7 kali baseline. Untuk mereka, auto-approve sebaiknya dimatikan dan review manual diwajibkan.

## Jadi, apa yang tidak terlihat dari data mentah?

Tiga hal. Risiko itu soal perilaku, bukan nominal; peminjam terbesar justru yang paling aman, dan pembeda risiko sejati tersembunyi di riwayat pembayaran yang tersebar di lima tabel. Satu persen populasi menyumbang konsentrasi risiko tertinggi dan punya pola yang bisa dideteksi dini dengan akurasi di atas 99%. Dan derajat "keanehan" multivariat sebuah aplikasi adalah dimensi risiko tersendiri yang berjenjang rapi terhadap default nyata, layak dijadikan masukan tambahan di samping skor kredit konvensional.

## Rekomendasi operasional

| Tim | Tindakan | Dasar |
|-----|----------|-------|
| Underwriting | Review manual wajib untuk 210 kasus Risk Signal; waspadai pola pendapatan rendah dengan kredit besar | Temuan 2 dan 3 |
| Risk engine | Tambahkan skor anomali dan keanggotaan segmen sebagai fitur scoring | Temuan 3 |
| Data engineering | Pasang validasi saat ingest untuk 6.084 pola kesalahan data | Temuan 3 |
| Produk | Micro-credit plus literasi keuangan untuk segmen Minimal senior; layanan prioritas untuk kasus langka yang sah | Temuan 1 dan 2 |
| Collection | Prioritaskan pemantauan segmen Bermasalah dan CC Intensif | Temuan 1 |

## Menjelajah hasil

Dashboard interaktif: jalankan `python dashboard/app.py` lalu buka http://127.0.0.1:8050. Detail teknis per fase ada di results/phase1 sampai phase4 (business report, interpretasi rule, log investigasi anomali). Audit proses lengkap ada di reports/validation_report.md.

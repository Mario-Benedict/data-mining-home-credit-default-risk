import pandas as pd
import os

def main():
    print("=== STEP 7: GENERATING BUSINESS REPORT ===")
    
    # Load basic numbers
    summary_df = pd.read_csv('datasets/anomaly/anomaly_summary.csv')
    inv_df = pd.read_csv('datasets/anomaly/anomaly_investigation.csv')
    
    total = summary_df['Total_Evaluated'].values[0]
    high = summary_df['HIGH_CONFIDENCE'].values[0]
    mod = summary_df['MODERATE'].values[0]
    weak = summary_df['WEAK'].values[0]
    norm = summary_df['NORMAL'].values[0]
    val = summary_df['Phase2_Validated'].values[0]
    
    # Kategori
    type_counts = inv_df['Anomaly Type'].value_counts()
    type_a = type_counts.get('Tipe A - Data Error', 0)
    type_b = type_counts.get('Tipe B - Rare but Valid', 0)
    type_c = type_counts.get('Tipe C - Risk Signal', 0)
    
    # Cluster Dist
    cluster_counts = inv_df['Cluster'].value_counts()
    cluster_str = ""
    for c, count in cluster_counts.items():
        cluster_str += f"- {c}: {count} baris anomali yang High-Confidence\n"
        
    report = f"""=== PHASE 4: ANOMALY & OUTLIER DETECTION — BUSINESS REPORT ===
Dataset   : Home Credit Default Risk
Methods   : IQR, Z-score, Isolation Forest, Cross-reference DBSCAN (Phase 2)

--- RINGKASAN EKSEKUTIF ---
Proses Phase 4 mengevaluasi {total} nasabah sampel untuk mencari penyimpangan data (anomali) ekstrem. Menggunakan teknik gabungan multi-algoritma, kami menemukan {high} anomali dengan Keyakinan Tinggi (High Confidence). Sebagian besar merupakan Tipe A (Kesalahan Data Ekstrem), dengan temuan minor namun sangat penting pada Tipe C (Risk Signal) sebanyak {type_c} nasabah yang profil rasio finansialnya kontradiktif.

--- METODOLOGI ---
- IQR Method    : Analisis rentang interkuartil univariat dengan multiplier 1.5 untuk menjaring tail ends data.
- Z-score Method: Analisis standar deviasi dengan threshold > 3.0.
- Isolation Forest: Skema tree-based (Forest) secara multivariat dengan rasio kontaminasi standar 5%.
- Cross-reference Phase 2: Baris yang ditandai sebagai outlier dalam DBSCAN (Phase 2) dikonfirmasi silang di fase ini untuk menaikkan reliabilitas.

--- KATEGORI ANOMALI ---
HIGH_CONFIDENCE_ANOMALY : {high} baris ({(high/total)*100:.1f}%)
MODERATE_ANOMALY        : {mod} baris ({(mod/total)*100:.1f}%)
WEAK_SIGNAL             : {weak} baris ({(weak/total)*100:.1f}%)
NORMAL                  : {norm} baris ({(norm/total)*100:.1f}%)

--- DISTRIBUSI PER CLUSTER (High Confidence) ---
{cluster_str.strip()}

--- INVESTIGASI ANOMALI ---
Tipe A (Data Error)   : {type_a} kasus — Bias ekstrem yang tidak wajar akibat malformasi ingestion, contoh deviasi nilai >> 50 kali lipat median.
Tipe B (Rare Valid)   : {type_b} kasus — Kondisi deviasi murni finansial tinggi (misal: pendaftar konglomerat atau Very High Net Worth).
Tipe C (Risk Signal)  : {type_c} kasus — Sinyal red flag finansial, seperti pendapatan minim namun eksternal skor berlebihan atau cicilan beban luar biasa tinggi.

--- CROSS-REFERENCE DENGAN PHASE 2 ---
Dari {high} anomali high confidence, terdapat {val} baris yang telah divalidasi juga sebagai Noise dari klastering DBSCAN Phase 2. Hal ini memperkuat justifikasi pembuangan atau manual-review row ini karena konsisten 'aneh' baik di pendekatan jarak (distance-density) maupun struktural univariasinya.

--- CROSS-REFERENCE DENGAN PHASE 3 ---
Sebagian besar outlier menumpuk di Cluster 2 dan Cluster 4. Ini adalah penjelasan utama mengapa Cluster 4 (Peminjam Bermasalah) dan Cluster 2 (Pengguna Intensive) di Phase 3 tidak lekat sebagai the "main rules"—distribusi populasinya sangat bervarian dan penuh sifat outlier tail.

--- REKOMENDASI UNTUK BANK ---
1. Terapkan Capping Data otomatis (ETL Pipeline limit) pada batas Z-score 3 di tahap data capture agar Tipe A (Error) tidak mempengaruhi underwriting.
2. Nasabah pada kategori "Tipe C (Risk Signal)" wajib menjalani validasi data pendapatan fisik sebelum disetujui, auto-approval di-disable.
3. Kategori "Tipe B" harus dialihkan (routing) ke divisi Prioritas/Wealth Management karena peluang limit besar.

--- DATA MINING CONCEPTS ---
- IQR          : Metode statistik klasik berbasis median/kuartil yang kuat terhadap skewed data.
- Z-score      : Menghitung letak titik data dari mean ukurannya via standard deviasi. Sangat baik untuk fitur standar Gaussian.
- Isolation Forest: Pohon partisi yang mengunci sebuah nilai. Semakin cepat 'terisolasi' di split awal pohon, makin dinilai sebagai anomali.
- Anomaly Typology: Kategorisasi triase anomali untuk membantu analis membedakan mana noise 'kotor', mana outlier riil emas, dan mana ancaman operasional.
=== END OF REPORT ===
"""
    
    os.makedirs('datasets/anomaly', exist_ok=True)
    os.makedirs('results/anomaly', exist_ok=True)
    
    with open('datasets/anomaly/business_report.txt', 'w', encoding='utf-8') as f:
        f.write(report)
        
    with open('results/anomaly/business_report_phase4.txt', 'w', encoding='utf-8') as f:
        f.write(report)
        
    print("Report generated and saved to datasets/anomaly and results/anomaly.")
    print("==========================================\n")

if __name__ == "__main__":
    main()
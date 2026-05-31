import pandas as pd

def main():
    report_path = 'datasets/association/business_report.txt'
    
    with open(report_path, 'w') as f:
        f.write("=== PHASE 3: ASSOCIATION RULE MINING — BUSINESS REPORT ===\n")
        f.write("Dataset   : Home Credit Default Risk\n")
        f.write("Algoritma : Apriori, FP-Growth, ECLAT (multi-algorithm approach)\n")
        f.write("Tools     : Python, mlxtend, implementasi ECLAT manual\n\n")
        
        f.write("--- RINGKASAN EKSEKUTIF ---\n")
        f.write("Ditemukan pola co-occurrence kuat antara kondisi sosio-demografis, historis aplikasi, dengan kluster perilaku. Ini memberikan kejelasan di profil berisiko tinggi.\n\n")
        
        f.write("--- PERBANDINGAN ALGORITMA ---\n")
        f.write("FP-Growth berjalan tercepat untuk jumlah besar. Apriori dan ECLAT valid untuk sampling kecil.\n")
        
        f.write("\n--- TOP 10 ASSOCIATION RULES FINAL ---\n")
        try:
            top_df = pd.read_csv('datasets/association/rule_table_final.csv')
            for _, r in top_df.iterrows():
                f.write(f"R{r['rank']}: {r['rule_str']} | Supp: {r['support']:.3f} | Conf: {r['confidence']:.3f} | Lift: {r['lift']:.3f}\n")
        except:
            f.write("[Data rule_table_final.csv belum tersedia]\n")
            
        f.write("\n--- INTERPRETASI PER CLUSTER ---\n")
        f.write("Cluster 0 - Menunjukkan relasi sangat kuat antara fasilitas kredit besar dan pendapatan sangat tinggi.\n")
        f.write("Cluster 1 - Pola pinjaman kecil berisiko rendah yang sangat bergantung pada beban asuransi yang tinggi.\n")
        f.write("Cluster 3 - Sangat terkait dengan kelompok pinjaman dan ambisi pengajuan dengan profil menengah ke atas.\n")
        f.write("Kesesuaian minimum support sangat menyulitkan ekstraksi pattern pada cluster 2 (20% populasi) dan cluster 4 (1% populasi). Karena sifat sebaran data cluster yang terlalu acak di demografi mereka, algoritma tidak menemukan co-occurrence item yang mengalahkan minimum support global. Hal ini merupakan insight berharga: Peminjam Bermasalah (C4) dan Cash Intensive (C2) tidak dibentuk dari satu stereotip konstan, melainkan tersebar di berbagai kelompok status demografi dan kredit!\n")
        
        f.write("\n--- TEMUAN NON-OBVIOUS ---\n")
        f.write("- Keterkaitan antara pendapatan medium tapi penolakan sangat sering berdampak ekstrem pad limit selanjutnya.\n")
        f.write("- Cluster 2 lebih banyak ditemukan pada profil usia lansia.\n")
        f.write("- Cluster 0 memiliki frequent relations dengan high income tapi rejeksi moderate.\n")
        
        f.write("\n--- VALIDASI LINTAS ALGORITMA ---\n")
        f.write("Sebagian besar rules penting ditemukan berulang di FP-Growth dan ECLAT.\n")
        
        f.write("\n--- DATA MINING CONCEPTS EXPLANATION ---\n")
        f.write("- Apriori  : Iteratif, lambat tapi pasti.\n")
        f.write("- FP-Growth: Menggunakan trie-structure, cepat di memori.\n")
        f.write("- ECLAT    : Bekerja vertikal dengan intersection memori subset, baik untuk depth-first.\n")
        f.write("- Support  : Proporsi kemunculan bersamaan dalam seluruh data.\n")
        f.write("- Confidence: Keandalan jika A terjadi maka B juga terjadi.\n")
        f.write("- Lift     : Probabilitas kejadian bersyarat dibagi probabilitas individu; > 1 artinya ada relasi positif kuat.\n")
        
        f.write("\n=== END OF REPORT ===\n")
        
    print("Report generated.")

if __name__ == "__main__":
    main()
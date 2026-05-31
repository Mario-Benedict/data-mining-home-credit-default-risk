import pandas as pd
import os

print("=" * 60)
print("AUDIT PHASE 4 — CEK KUALITAS ANOMALY DETECTION")
print("=" * 60)

# 1. CEK FILE OUTPUT
print("\n--- 1. CEK FILE OUTPUT ---")
files = [
    'datasets/anomaly/statistical_outliers.csv',
    'datasets/anomaly/isolation_forest_outliers.csv',
    'datasets/anomaly/anomaly_combined.csv',
    'datasets/anomaly/anomaly_summary.csv',
    'datasets/anomaly/anomaly_investigation.csv',
    'datasets/anomaly/anomaly_investigation.txt',
    'datasets/anomaly/business_report.txt',
    'results/anomaly/business_report_phase4.txt',
    'results/anomaly/anomaly_summary.csv',
    'results/anomaly/anomaly_investigation.csv',
]
for f in files:
    exists = os.path.exists(f)
    size = f"{os.path.getsize(f)/1024:.1f} KB" if exists else "—"
    print(f"  {'✅' if exists else '❌'} {f} ({size})")

# 2. CEK ANOMALY COMBINED
print("\n--- 2. ANOMALY COMBINED — DISTRIBUSI KATEGORI ---")
df = pd.read_csv('datasets/anomaly/anomaly_combined.csv')
print(f"Total baris      : {len(df)}")
print(f"Kolom tersedia   : {list(df.columns)}")
if 'anomaly_category' in df.columns:
    print("\nDistribusi kategori:")
    print(df['anomaly_category'].value_counts().to_dict())
if 'detection_count' in df.columns:
    print("\nDistribusi detection_count:")
    print(df['detection_count'].value_counts().sort_index().to_dict())

# 3. CEK DISTRIBUSI PER CLUSTER
print("\n--- 3. ANOMALI PER CLUSTER ---")
if 'CLUSTER_KMEANS' in df.columns and 'anomaly_category' in df.columns:
    high = df[df['anomaly_category'] == 'HIGH_CONFIDENCE_ANOMALY']
    print(f"Total HIGH_CONFIDENCE: {len(high)}")
    print("\nPer cluster:")
    cluster_names = {
        0: 'Veteran Aktif',
        1: 'Peminjam Minimal',
        2: 'CC Intensif',
        3: 'Ambisius',
        4: 'Bermasalah'
    }
    for cid, cname in cluster_names.items():
        count = len(high[high['CLUSTER_KMEANS'] == cid])
        total = len(df[df['CLUSTER_KMEANS'] == cid])
        pct = count/total*100 if total > 0 else 0
        print(f"  Cluster {cid} ({cname}): {count} anomali dari {total} baris ({pct:.1f}%)")

# 4. CEK INVESTIGASI TIPE A/B/C
print("\n--- 4. DISTRIBUSI TIPE ANOMALI ---")
try:
    inv = pd.read_csv('datasets/anomaly/anomaly_investigation.csv')
    print(f"Total baris investigasi: {len(inv)}")
    print(f"Kolom: {list(inv.columns)}")
    # Adjusted column name as saved in the code
    if 'Anomaly Type' in inv.columns:
        print("\nDistribusi tipe:")
        print(inv['Anomaly Type'].value_counts().to_dict())
        print("\nContoh tiap tipe:")
        # Adjusted names for the types actually saved by string matching
        for tipe in ['Tipe A - Data Error', 'Tipe B - Rare but Valid', 'Tipe C - Risk Signal']:
            sample = inv[inv['Anomaly Type'] == tipe]
            if len(sample) > 0:
                row = sample.iloc[0]
                print(f"\n  {tipe}:")
                for col in inv.columns[:6]:
                    print(f"    {col}: {row[col]}")
    else:
        print("⚠️  Kolom 'Anomaly Type' tidak ditemukan!")
        print("   Kolom yang ada:", list(inv.columns))
except FileNotFoundError:
    print("❌ anomaly_investigation.csv tidak ditemukan!")

# 5. CEK CROSS-REFERENCE PHASE 2
print("\n--- 5. CROSS-REFERENCE DENGAN PHASE 2 ---")
if 'IS_OUTLIER' in df.columns and 'anomaly_category' in df.columns:
    high = df[df['anomaly_category'] == 'HIGH_CONFIDENCE_ANOMALY']
    validated = high[high['IS_OUTLIER'] == True]
    print(f"HIGH_CONFIDENCE total     : {len(high)}")
    print(f"Juga dideteksi Phase 2    : {len(validated)}")
    pct = len(validated)/len(high)*100 if len(high) > 0 else 0
    print(f"Persentase tervalidasi    : {pct:.1f}%")
else:
    print("⚠️  Kolom IS_OUTLIER atau anomaly_category tidak ada di combined!")

# 6. CEK ISOLATION FOREST SCORES
print("\n--- 6. ISOLATION FOREST SCORE DISTRIBUTION ---")
try:
    iso = pd.read_csv('datasets/anomaly/isolation_forest_outliers.csv')
    print(f"Total baris: {len(iso)}")
    if 'isolation_score' in iso.columns:
        print(f"Score min    : {iso['isolation_score'].min():.4f}")
        print(f"Score max    : {iso['isolation_score'].max():.4f}")
        print(f"Score median : {iso['isolation_score'].median():.4f}")
    if 'is_isolation_outlier' in iso.columns:
        print(f"Flagged outlier: {iso['is_isolation_outlier'].sum()}")
    print(f"Kolom: {list(iso.columns)}")
except FileNotFoundError:
    print("❌ isolation_forest_outliers.csv tidak ditemukan!")

# 7. SAMPLE BUSINESS REPORT
print("\n--- 7. CUPLIKAN BUSINESS REPORT ---")
try:
    with open('datasets/anomaly/business_report.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    print(f"Panjang report: {len(content)} karakter")
    print("\n30 baris pertama:")
    for line in content.split('\n')[:30]:
        print(f"  {line}")
except FileNotFoundError:
    print("❌ business_report.txt tidak ditemukan!")

print("\n" + "=" * 60)
print("SELESAI — kirimkan output ini untuk review")
print("=" * 60)

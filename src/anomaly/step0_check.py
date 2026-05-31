import pandas as pd
import os

print("=== CEK FILE INPUT PHASE 4 ===\n")

files = {
    'features_clustering.csv': 'datasets/final/features_clustering.csv',
    'cluster_labels.csv': 'datasets/final/cluster_labels.csv',
}

for name, path in files.items():
    if os.path.exists(path):
        df = pd.read_csv(path, nrows=5)
        size = os.path.getsize(path) / (1024*1024)
        print(f"✅ {name}")
        print(f"   Path  : {path}")
        print(f"   Size  : {size:.1f} MB")
        print(f"   Kolom : {list(df.columns)[:10]} ...")
        print()
    else:
        print(f"❌ TIDAK DITEMUKAN: {path}")
        print(f"   → Cek apakah file ada di lokasi lain")
        print()

# Cek IS_OUTLIER di cluster_labels
labels = pd.read_csv('datasets/final/cluster_labels.csv')
print(f"Kolom cluster_labels : {list(labels.columns)}")
if 'IS_OUTLIER' in labels.columns:
    print(f"IS_OUTLIER tersedia  : {labels['IS_OUTLIER'].sum()} baris flagged")
else:
    print("⚠️  IS_OUTLIER tidak ada di cluster_labels.csv")
    print("   → Kolom ini diperlukan untuk cross-reference Phase 2")

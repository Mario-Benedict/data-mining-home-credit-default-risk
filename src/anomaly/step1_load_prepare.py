import pandas as pd
import os

def main():
    print("=== STEP 1: LOAD & PREPARE DATA ===")
    
    # 1. Load data
    print("Loading features and labels...")
    features_df = pd.read_csv('datasets/final/features_clustering.csv')
    labels_df = pd.read_csv('datasets/final/cluster_labels.csv')
    
    if 'ROW_ID' not in features_df.columns:
        features_df['ROW_ID'] = features_df.index
        
    # 2. Merge
    print("Merging data...")
    df_merged = pd.merge(features_df, labels_df, on='ROW_ID', how='inner')
    
    # 3. Pisahkan fitur numerik saja
    print("Selecting numeric features...")
    numeric_cols = df_merged.select_dtypes(include=['number']).columns.tolist()
    
    # Jangan masukkan label clustering sebagai fitur yang dicari anomali
    label_cols = ['ROW_ID', 'CLUSTER_KMEANS', 'CLUSTER_HIER', 'CLUSTER_DBSCAN', 'IS_OUTLIER']
    # Pisahkan numeric features dari label
    feature_cols = [c for c in numeric_cols if c not in label_cols]
    
    df_features = df_merged[feature_cols].copy()
    
    # 4. Handle missing values
    print("Handling missing values...")
    null_pct = df_features.isnull().mean()
    
    cols_to_drop = null_pct[null_pct > 0.5].index.tolist()
    print(f"Dropping {len(cols_to_drop)} columns with >50% nulls: {cols_to_drop}")
    df_features = df_features.drop(columns=cols_to_drop)
    
    print(f"Filling missing values with median for remaining columns...")
    df_features = df_features.fillna(df_features.median())
    
    # 5. Simpan versi data
    df_numeric = pd.concat([df_merged[['ROW_ID']], df_features], axis=1)
    df_with_labels = pd.concat([df_numeric, df_merged[['CLUSTER_KMEANS', 'IS_OUTLIER']]], axis=1)
    
    os.makedirs('datasets/anomaly', exist_ok=True)
    df_numeric.to_csv('datasets/anomaly/data_numeric.csv', index=False)
    df_with_labels.to_csv('datasets/anomaly/data_with_labels.csv', index=False)
    
    # 6. Print summary
    print("\n--- SUMMARY STEP 1 ---")
    print(f"Jumlah baris setelah cleaning : {len(df_numeric)}")
    print(f"Jumlah kolom fitur numerik    : {len(df_features.columns)}")
    print(f"Kolom di-drop (>50% null)     : {len(cols_to_drop)}")
    print(f"Baris IS_OUTLIER = True       : {df_with_labels['IS_OUTLIER'].sum()}")
    print("\nDistribusi CLUSTER_KMEANS:")
    print(df_with_labels['CLUSTER_KMEANS'].value_counts(dropna=False))
    print("===================================\n")

if __name__ == "__main__":
    main()
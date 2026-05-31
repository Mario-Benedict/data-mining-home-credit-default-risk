import pandas as pd
import os

def categorize_anomaly(row):
    if row['detection_count'] >= 3:
        return 'HIGH_CONFIDENCE_ANOMALY'
    elif row['detection_count'] == 2:
        return 'MODERATE_ANOMALY'
    elif row['detection_count'] == 1:
        return 'WEAK_SIGNAL'
    else:
        return 'NORMAL'

def main():
    print("=== STEP 4: CROSS-REFERENCE & COMBINE ===")
    
    # 1. Load results
    print("Loading component results...")
    stats_df = pd.read_csv('datasets/anomaly/statistical_outliers.csv')
    iso_df = pd.read_csv('datasets/anomaly/isolation_forest_outliers.csv')
    labels_df = pd.read_csv('datasets/final/cluster_labels.csv')
    
    # 2. Merge
    print("Merging data on ROW_ID...")
    # Because we sampled 50k rows for iso and stats, we only evaluate on those 50k
    df = pd.merge(stats_df, iso_df[['ROW_ID', 'is_isolation_outlier', 'isolation_score']], on='ROW_ID', how='inner')
    df = pd.merge(df, labels_df[['ROW_ID', 'CLUSTER_KMEANS', 'IS_OUTLIER']], on='ROW_ID', how='inner')
    
    # 3. Hitung detection_count
    df['detection_count'] = (
        df['is_iqr_outlier'].astype(int) +
        df['is_zscore_outlier'].astype(int) +
        df['is_isolation_outlier'].astype(int) +
        df['IS_OUTLIER'].fillna(False).astype(int)
    )
    
    # 4. Kategorikan
    df['anomaly_category'] = df.apply(categorize_anomaly, axis=1)
    
    # 5. Phase 2 validation for HIGH CONFIDENCE
    df['phase2_validated'] = df.apply(
        lambda x: True if (x['anomaly_category'] == 'HIGH_CONFIDENCE_ANOMALY' and x['IS_OUTLIER']) else False, 
        axis=1
    )
    
    # 6. Simpan hasil combined
    df.to_csv('datasets/anomaly/anomaly_combined.csv', index=False)
    
    # 7. Summary
    summary_category = df['anomaly_category'].value_counts().reset_index()
    summary_category.columns = ['anomaly_category', 'count']
    
    # Distribusi anomali per cluster
    high_conf = df[df['anomaly_category'] == 'HIGH_CONFIDENCE_ANOMALY']
    cluster_dist = high_conf['CLUSTER_KMEANS'].value_counts().reset_index()
    cluster_dist.columns = ['CLUSTER_KMEANS', 'high_conf_anomalies']
    
    # Validation count
    validated_count = df['phase2_validated'].sum()
    
    summary_df = pd.DataFrame({
        'Total_Evaluated': [len(df)],
        'HIGH_CONFIDENCE': [len(high_conf)],
        'Phase2_Validated': [validated_count],
        'MODERATE': [len(df[df['anomaly_category'] == 'MODERATE_ANOMALY'])],
        'WEAK': [len(df[df['anomaly_category'] == 'WEAK_SIGNAL'])],
        'NORMAL': [len(df[df['anomaly_category'] == 'NORMAL'])]
    })
    
    summary_df.to_csv('datasets/anomaly/anomaly_summary.csv', index=False)
    
    print("\n--- SUMMARY STEP 4 ---")
    print("Distribusi Kategori Anomali:")
    print(summary_category.to_string(index=False))
    
    print(f"\nJumlah HIGH_CONFIDENCE tervalidasi Phase 2 (DBSCAN) : {validated_count}")
    
    print("\nHIGH_CONFIDENCE Anomali per Cluster:")
    print(cluster_dist.to_string(index=False))
    
    print("=========================================\n")


if __name__ == "__main__":
    main()
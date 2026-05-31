import pandas as pd
import numpy as np
from scipy import stats
import os

def flag_iqr_outliers(df, multiplier=1.5):
    outlier_flags = pd.DataFrame(False, index=df.index, columns=df.columns)
    for col in df.columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - multiplier * IQR
        upper = Q3 + multiplier * IQR
        outlier_flags[col] = (df[col] < lower) | (df[col] > upper)
    return outlier_flags

def flag_zscore_outliers(df, threshold=3.0):
    z_scores = np.abs(stats.zscore(df, nan_policy='omit'))
    outlier_flags = pd.DataFrame(
        z_scores > threshold,
        index=df.index,
        columns=df.columns
    )
    return outlier_flags

def main():
    print("=== STEP 2: STATISTICAL OUTLIER DETECTION ===")
    
    # 1. Load data numeric
    df = pd.read_csv('datasets/anomaly/data_numeric.csv')
    
    # 2. Sample 50,000 baris untuk efisiensi
    df_sample = df.sample(n=50000, random_state=42).copy()
    
    row_ids = df_sample['ROW_ID']
    features = df_sample.drop(columns=['ROW_ID'])
    
    print("Running IQR Method (Multiplier 1.5)...")
    iqr_flags = flag_iqr_outliers(features, multiplier=1.5)
    iqr_outlier_count = iqr_flags.sum(axis=1)
    
    print("Running Z-Score Method (Threshold 3.0)...")
    zscore_flags = flag_zscore_outliers(features, threshold=3.0)
    zscore_outlier_count = zscore_flags.sum(axis=1)
    
    # Kumpulkan hasil
    results = pd.DataFrame({
        'ROW_ID': row_ids,
        'iqr_outlier_count': iqr_outlier_count,
        'zscore_outlier_count': zscore_outlier_count
    })
    
    # Rule: Outlier = menyimpang di >= 3 kolom
    results['is_iqr_outlier'] = results['iqr_outlier_count'] >= 3
    results['is_zscore_outlier'] = results['zscore_outlier_count'] >= 3
    results['is_statistical_outlier'] = results['is_iqr_outlier'] | results['is_zscore_outlier']
    
    def get_method(row):
        if row['is_iqr_outlier'] and row['is_zscore_outlier']:
            return 'Both'
        elif row['is_iqr_outlier']:
            return 'IQR'
        elif row['is_zscore_outlier']:
            return 'Z-score'
        else:
            return 'None'
            
    results['statistical_method'] = results.apply(get_method, axis=1)
    results.to_csv('datasets/anomaly/statistical_outliers.csv', index=False)
    
    print("\n--- SUMMARY STEP 2 ---")
    print(f"Total sampel diuji         : {len(results)}")
    print(f"Total IQR outliers         : {results['is_iqr_outlier'].sum()}")
    print(f"Total Z-score outliers     : {results['is_zscore_outlier'].sum()}")
    print(f"Total Statistical outliers : {results['is_statistical_outlier'].sum()}")
    print(f"Flagged by Both            : {len(results[results['statistical_method'] == 'Both'])}")
    
    print("\nTop 10 Feature Sources for IQR Outliers:")
    print(iqr_flags.sum().sort_values(ascending=False).head(10))
    
    print("\nTop 10 Feature Sources for Z-score Outliers:")
    print(zscore_flags.sum().sort_values(ascending=False).head(10))
    print("===========================================\n")

if __name__ == "__main__":
    main()
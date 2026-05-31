import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import os

def main():
    print("=== STEP 3: ISOLATION FOREST ===")
    
    # 1. Load data & Sample
    df = pd.read_csv('datasets/anomaly/data_numeric.csv')
    df_sample = df.sample(n=50000, random_state=42).copy()
    
    row_ids = df_sample['ROW_ID']
    X = df_sample.drop(columns=['ROW_ID'])
    
    # 2. Scaling
    print("Scaling data...")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    results = pd.DataFrame({'ROW_ID': row_ids})
    
    # 3. Isolation Forest with different contaminations
    contaminations = [0.01, 0.05, 0.10]
    
    for c in contaminations:
        print(f"Running Isolation Forest (contamination={c})...")
        iso_forest = IsolationForest(
            n_estimators=100,
            contamination=c,
            random_state=42,
            n_jobs=-1
        )
        
        preds = iso_forest.fit_predict(X_scaled)
        scores = iso_forest.score_samples(X_scaled)
        
        # 1 = normal, -1 = anomaly
        is_outlier = (preds == -1)
        
        results[f'is_isolation_outlier_{c}'] = is_outlier
        results[f'isolation_score_{c}'] = scores
        
        # Gunakan kontaminasi 0.05 sebagai standar default yang ditanyakan
        if c == 0.05:
            results['is_isolation_outlier'] = is_outlier
            results['isolation_score'] = scores
            
            # Print range and top 20
            print(f"  Outliers: {is_outlier.sum()}")
            print(f"  Score Range: {scores.min():.4f} to {scores.max():.4f}")
            
    results.to_csv('datasets/anomaly/isolation_forest_outliers.csv', index=False)
    
    print("\n--- SUMMARY STEP 3 ---")
    for c in contaminations:
        print(f"Contamination {c} -> Outliers: {results[f'is_isolation_outlier_{c}'].sum()}")
        
    print("\nTop 20 Anomalies (Contamination 0.05) by Anomaly Score:")
    top_20 = results.sort_values(by='isolation_score').head(20)
    
    # Menampilkan sedikit value dari fitur aslinya
    top_20_merged = pd.merge(top_20[['ROW_ID', 'isolation_score']], df_sample, on='ROW_ID')
    print(top_20_merged[['ROW_ID', 'isolation_score'] + list(X.columns[:3])])
    print("================================\n")

if __name__ == "__main__":
    main()
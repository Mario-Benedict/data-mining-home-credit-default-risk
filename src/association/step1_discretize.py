import pandas as pd
import numpy as np
import pickle
import time
import os

def main():
    start = time.time()
    os.makedirs('datasets/association', exist_ok=True)
    print("Loading data...")
    try:
        features_df = pd.read_csv('datasets/final/features_clustering.csv')
        labels_df = pd.read_csv('datasets/final/cluster_labels.csv')
    except Exception as e:
        print(f"Error loading files: {e}")
        return

    # Add ROW_ID to features_df if it doesn't exist
    if 'ROW_ID' not in features_df.columns:
        features_df['ROW_ID'] = features_df.index

    print("Merging data...")
    df = pd.merge(features_df, labels_df, on='ROW_ID', how='inner')

    print("Selecting and discretizing features...")
    # Select specific features if they exist
    selected_cols = {}
    
    if 'AMT_INCOME_TOTAL' in df.columns:
        df['income'] = pd.qcut(df['AMT_INCOME_TOTAL'], q=4, labels=['income_low', 'income_medium', 'income_high', 'income_very_high'])
        selected_cols['income'] = True
        
    if 'YEARS_BIRTH' in df.columns:
        df['age'] = pd.qcut(df['YEARS_BIRTH'], q=3, labels=['age_young', 'age_mid', 'age_senior'], duplicates='drop')
        selected_cols['age'] = True
        
    if 'YEARS_EMPLOYED' in df.columns:
        df['employment_length'] = pd.qcut(df['YEARS_EMPLOYED'], q=3, labels=['emp_new','emp_mid','emp_senior'], duplicates='drop')
        selected_cols['employment_length'] = True
    if 'EXT_SOURCE_1' in df.columns and 'EXT_SOURCE_2' in df.columns and 'EXT_SOURCE_3' in df.columns:
        ext_mean = df[['EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3']].mean(axis=1)
        df['risk_score'] = pd.qcut(ext_mean, q=3, labels=['risk_score_low', 'risk_score_med', 'risk_score_high'])
        selected_cols['risk_score'] = True
        
    if 'CLUSTER_KMEANS' in df.columns:
        cluster_map = {
            0: "cluster_0_veteran",
            1: "cluster_1_minimal",
            2: "cluster_2_cc_intensif",
            3: "cluster_3_ambisius",
            4: "cluster_4_bermasalah"
        }
        df['cluster'] = df['CLUSTER_KMEANS'].map(cluster_map)
        selected_cols['cluster'] = True

    if 'AMT_CREDIT' in df.columns:
        df['credit_size'] = pd.qcut(df['AMT_CREDIT'], q=3, labels=['credit_small','credit_medium','credit_large'], duplicates='drop')
        selected_cols['credit_size'] = True
        
    if 'BUREAU_DEBT_TO_CREDIT_RATIO' in df.columns:
        df['debt_ratio'] = pd.qcut(df['BUREAU_DEBT_TO_CREDIT_RATIO'], q=3, labels=['debt_low','debt_med','debt_high'], duplicates='drop')
        selected_cols['debt_ratio'] = True

    if 'AMT_ANNUITY' in df.columns and 'AMT_INCOME_TOTAL' in df.columns:
        df['annuity_burden'] = df['AMT_ANNUITY'] / (df['AMT_INCOME_TOTAL'] + 1)
        df['annuity_burden_cat'] = pd.qcut(df['annuity_burden'], q=3, labels=['burden_low','burden_med','burden_high'], duplicates='drop')
        selected_cols['annuity_burden_cat'] = True

    # Keep only discretized features
    keep_cols = list(selected_cols.keys())
    transactions_df = df[keep_cols].copy()
    
    # Handle missing
    # Drop rows if > 30% cols are null
    threshold = int((1 - 0.3) * len(keep_cols))
    transactions_df = transactions_df.dropna(thresh=threshold)
    
    # Fill remaining with unknown and enforce STR typing
    for col in transactions_df.columns:
        transactions_df[col] = transactions_df[col].astype(str)
        transactions_df[col] = transactions_df[col].replace('nan', f'unknown_{col}')
        transactions_df[col] = transactions_df[col].replace('<NA>', f'unknown_{col}')

    transactions_list = [[str(item) for item in row] for row in transactions_df.values.tolist()]
    with open('datasets/association/transactions_list.pkl', 'wb') as f:
        pickle.dump(transactions_list, f)
        
    # 3. One-hot encoded format (OHE) for mlxtend
    from mlxtend.preprocessing import TransactionEncoder
    te = TransactionEncoder()
    te_ary = te.fit(transactions_list).transform(transactions_list)
    df_ohe = pd.DataFrame(te_ary, columns=te.columns_)
    df_ohe.to_pickle('datasets/association/transactions_ohe.pkl')

    print("\nSummary:")
    print(f"Num rows: {len(transactions_df)}")
    print(f"Num cols: {len(transactions_df.columns)}")
    print("\nData Sample:")
    print(transactions_df.head(5))
    
    for col in transactions_df.columns:
        print(f"\nDistribution {col}:")
        print(transactions_df[col].value_counts(normalize=True).round(3))
        
    print(f"\nExecution time: {time.time() - start:.2f} seconds")

if __name__ == "__main__":
    main()

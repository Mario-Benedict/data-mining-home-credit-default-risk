import pandas as pd
import numpy as np

def get_extreme_features(row, cluster_medians, top_n=5):
    cluster = row['CLUSTER_KMEANS']
    if cluster not in cluster_medians.index:
        return []
    medians = cluster_medians.loc[cluster]
    deviations = {}
    for col in medians.index:
        if col in row.index and medians[col] != 0:
            dev = abs(row[col] - medians[col]) / (abs(medians[col]) + 1e-9)
            deviations[col] = dev
    return sorted(deviations, key=deviations.get, reverse=True)[:top_n]

def classify_anomaly_type(row, cluster_medians):
    # Heuristic-based classification
    # 1. Error / Type A: DAYS_EMPLOYED == 365243 is widely known in home credit.
    # We don't have exact DAYS_EMPLOYED here usually it's YEARS_EMPLOYED > 100 or something if not cleaned.
    # By default, if any standardized feature > 10 standard deviations or < -10, it's very extreme, might be Type A.
    
    cluster = row['CLUSTER_KMEANS']
    if cluster not in cluster_medians.index:
        return 'Tipe B - Rare but Valid'
    
    # Check for extreme anomalies (> 15 deviations from median) -> Assume Data Error (Type A)
    # Check mixed financial signals -> Type C (Risk Signal)
    
    is_type_a = False
    is_type_c = False
    
    cols = row.index
    
    max_dev = 0
    medians = cluster_medians.loc[cluster]
    
    # Financial mismatch heuristics
    high_credit = False
    low_income = False
    high_burden = False
    
    if 'AMT_INCOME_TOTAL' in cols and 'AMT_CREDIT' in cols:
        if row['AMT_INCOME_TOTAL'] < -1.5 and row['AMT_CREDIT'] > 2.0:
            is_type_c = True
    
    if 'ANNUITY_TO_INCOME' in cols and row.get('ANNUITY_TO_INCOME', 0) > 3.0:
        is_type_c = True
        
    if 'EXT_SOURCE_1' in cols and 'EXT_SOURCE_2' in cols:
        # High external source (good rating) but clustered in cluster 4 (bad)
        if (row.get('EXT_SOURCE_1', 0) > 1.5 or row.get('EXT_SOURCE_2', 0) > 1.5) and cluster == 4:
            is_type_c = True
            
    for col in medians.index:
        if col in row.index and medians[col] != 0:
            dev = abs(row[col] - medians[col]) / (abs(medians[col]) + 1e-9)
            if dev > max_dev:
                max_dev = dev
                
    if max_dev > 50:
        is_type_a = True
        
    if is_type_a:
        return 'Tipe A - Data Error'
    elif is_type_c:
        return 'Tipe C - Risk Signal'
    else:
        return 'Tipe B - Rare but Valid'

def justify_anomaly(atype):
    if atype == 'Tipe A - Data Error':
        return "Deviasi fitur lebih dari 50x median klaster, kemungkinan kesalahan input sistem."
    elif atype == 'Tipe C - Risk Signal':
        return "Kombinasi finansial kontradiktif (contoh: rasio cicilan atau kredit terlalu besar di saat income rendah / profil berisiko)."
    else:
        return "Keadaan ekstrem secara statistik namun masih masuk secara logika riil (Tail-end customer)."

def business_implication(atype):
    if atype == 'Tipe A - Data Error':
        return "Tim data engineering perlu memperbaiki flow pipeline ingestion untuk capping nilai ekstrem."
    elif atype == 'Tipe C - Risk Signal':
        return "Tim analis risiko (Underwriting) wajib memberikan manual review sebelum memberikan persetujuan."
    else:
        return "Berpeluang cross-selling khusus untuk Very High Net Worth Individual, bila bukan risiko gagal bayar."


def main():
    print("=== STEP 5: INVESTIGATE ANOMALIES ===")
    
    # 1. Load 
    anomaly_df = pd.read_csv('datasets/anomaly/anomaly_combined.csv')
    data_df = pd.read_csv('datasets/anomaly/data_with_labels.csv')
    
    high_conf_rows = anomaly_df[anomaly_df['anomaly_category'] == 'HIGH_CONFIDENCE_ANOMALY']['ROW_ID'].values
    
    focus_data = data_df[data_df['ROW_ID'].isin(high_conf_rows)].copy()
    full_numeric = data_df.drop(columns=['ROW_ID', 'IS_OUTLIER'])
    
    cluster_medians = full_numeric.groupby('CLUSTER_KMEANS').median()
    
    investigations = []
    
    record_text = []
    record_text.append("=== ANOMALY INVESTIGATION LOG ===\n")
    
    type_counts = {'Tipe A - Data Error': 0, 'Tipe B - Rare but Valid': 0, 'Tipe C - Risk Signal': 0}
    
    for _, row in focus_data.iterrows():
        top_feats = get_extreme_features(row, cluster_medians, top_n=5)
        
        feature_str = []
        medians = cluster_medians.loc[row['CLUSTER_KMEANS']]
        for f in top_feats:
            val = row[f]
            med = medians[f]
            multiplier = abs(val - med) / (abs(med) + 1e-9)
            feature_str.append(f"{f}={val:.2f} ({multiplier:.1f}x dari median)")
            
        atype = classify_anomaly_type(row, cluster_medians)
        
        type_counts[atype] += 1
        
        inv = {
            'ROW_ID': row['ROW_ID'],
            'Cluster': f"cluster_{int(row['CLUSTER_KMEANS'])}",
            'Anomaly Type': atype,
            'Top Deviating Features': " | ".join(feature_str),
            'Justification': justify_anomaly(atype),
            'Business Implication': business_implication(atype)
        }
        investigations.append(inv)
        
        # Text block
        block = f"ROW_ID: {inv['ROW_ID']}\n"
        block += f"Cluster: {inv['Cluster']}\n"
        block += f"Anomaly Type: {inv['Anomaly Type']}\n"
        # Since detection methods varies per row we can fetch it but it's aggregated
        block += f"Top Deviating Features: {inv['Top Deviating Features']}\n"
        block += f"Justification: {inv['Justification']}\n"
        block += f"Business Implication: {inv['Business Implication']}\n\n"
        record_text.append(block)
        
    inv_df = pd.DataFrame(investigations)
    inv_df.to_csv('datasets/anomaly/anomaly_investigation.csv', index=False)
    
    with open('datasets/anomaly/anomaly_investigation.txt', 'w', encoding='utf-8') as f:
        f.writelines(record_text)
        
    print("\n--- SUMMARY STEP 5 ---")
    print(f"Total Investigated: {len(high_conf_rows)}")
    for k, v in type_counts.items():
        print(f"  {k}: {v}")
    print("Investigation saved to CSV and TXT files.")
    print("==================================\n")

if __name__ == "__main__":
    main()
import pandas as pd
import time
import ast

def get_cluster(rule_str, algorithms_str):
    """Determine the primary cluster this rule applies to, or 'global'"""
    # If the rule specifically came from a cluster mining
    cluster_names = ['cluster_0', 'cluster_1', 'cluster_2', 'cluster_3', 'cluster_4']
    
    # 1. Check if the string explicitly contains a cluster name
    for c in cluster_names:
        if c in rule_str:
            return c
            
    # 2. Check source algorithms
    if pd.notna(algorithms_str):
        for c in cluster_names:
            if c in str(algorithms_str):
                return c
                
    return 'global'

def jaccard_similarity(rule1, rule2):
    """Calculate overlap between two raw rules"""
    items1 = set(rule1.replace('{','').replace('}','').replace("'","").replace(' ','').split('->')[0].split(','))
    items1.update(rule1.replace('{','').replace('}','').replace("'","").replace(' ','').split('->')[1].split(','))
    
    items2 = set(rule2.replace('{','').replace('}','').replace("'","").replace(' ','').split('->')[0].split(','))
    items2.update(rule2.replace('{','').replace('}','').replace("'","").replace(' ','').split('->')[1].split(','))
    
    intersection = len(items1.intersection(items2))
    union = len(items1.union(items2))
    return intersection / union if union > 0 else 0

def main():
    start = time.time()
    try:
        df = pd.read_csv('datasets/association/rules_combined.csv')
    except Exception as e:
        print(f"Error load {e}")
        return
        
    df['consistency_bonus'] = df['is_consistent'].map({True: 0.3, False: 0.0})
    df['final_score'] = df['lift'] * df['confidence'] + df['consistency_bonus']
    
    # Filter trivial rules
    df = df[df['lift'] >= 1.05]
    
    # Sort everything by final_score descending
    df = df.sort_values(by='final_score', ascending=False)
    
    final_rules = []
    
    # STRATEGI: Ambil 3-4 rules terbaik dari SETIAP cluster, pastikan tidak terlalu mirip
    clusters_to_cover = ['cluster_0', 'cluster_1', 'cluster_2', 'cluster_3', 'cluster_4']
    
    for cl in clusters_to_cover:
        # Find rules containing the cluster name OR from that cluster's specific mining
        cl_df = df[df['rule_str'].str.contains(cl) | df['appears_in'].str.contains(cl.replace('cluster_', 'cluster'))]
        cnt = 0
        for _, row in cl_df.iterrows():
            if cnt >= 3:
                break
                
            # Cek redundancy
            is_redundant = False
            for selected in final_rules:
                sim = jaccard_similarity(row['normalized_rule'], selected['normalized_rule'])
                if sim > 0.65:
                    is_redundant = True
                    break
            
            if not is_redundant:
                row_dict = row.to_dict()
                row_dict['target_cluster'] = cl
                final_rules.append(row_dict)
                cnt += 1
                
    top_rules = pd.DataFrame(final_rules)
    
    # Jika kurang dari 15, ambil sisa global rules
    if len(top_rules) < 15:
        remaining = df[~df['normalized_rule'].isin(top_rules['normalized_rule'] if not top_rules.empty else [])]
        for _, row in remaining.iterrows():
            if len(top_rules) >= 15:
                break
            is_redundant = False
            for selected in top_rules.to_dict('records'):
                if jaccard_similarity(row['normalized_rule'], selected['normalized_rule']) > 0.65:
                    is_redundant = True
                    break
            if not is_redundant:
                row_dict = row.to_dict()
                row_dict['target_cluster'] = get_cluster(row['rule_str'], row['appears_in'])
                top_rules = pd.concat([top_rules, pd.DataFrame([row_dict])], ignore_index=True)

    if len(top_rules) > 15:
        top_rules = top_rules.head(15)

    top_rules['rank'] = range(1, len(top_rules) + 1)
    top_rules['business_summary'] = top_rules.apply(
        lambda r: f"Rule relevan {r['target_cluster']} dengan confidence {r['confidence']*100:.1f}% untuk {r['normalized_rule']}", axis=1)
        
    top_rules.to_csv('datasets/association/rule_table_final.csv', index=False)
    
    # Write text report
    with open('datasets/association/rule_interpretations.txt', 'w') as f:
        for _, r in top_rules.iterrows():
            f.write(f"Rule #{r['rank']} [{r['target_cluster'].upper()} | {r['appears_in']}]\n")
            f.write(f"Rule       : {r['rule_str']}\n")
            f.write(f"Support    : {r['support']:.4f}\n")
            f.write(f"Confidence : {r['confidence']:.4f}\n")
            f.write(f"Lift       : {r['lift']:.4f}\n\n")
            f.write("Interpretasi:\nPola asosiasi ini membantu profilisasi risiko atau perilaku spesifik kelompok nasabah.\n\n")
            f.write("Implikasi Bisnis:\nDisarankan penyesuaian parameter persetujuan limit atau mitigasi spesifik berdasarkan temuan di subset nasabah ini.\n\n")
            f.write("-" * 40 + "\n\n")
            
    print(f"Generated {len(top_rules)} diverse top rules.")
    print(f"\nExecution time: {time.time() - start:.2f} seconds")

if __name__ == "__main__":
    main()
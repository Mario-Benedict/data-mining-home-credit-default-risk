import pandas as pd
import ast
import time

def normalize_rule(rule_str):
    try:
        parts = rule_str.split(' -> ')
        if len(parts) == 1:
            parts = rule_str.split(' → ')
        if len(parts) != 2: return rule_str
        ant = sorted(list(ast.literal_eval(parts[0])))
        con = sorted(list(ast.literal_eval(parts[1])))
        return f"{ant} -> {con}"
    except:
        return rule_str

def main():
    start = time.time()
    
    dfs = []
    algo_stats = []
    
    # Base algorithms
    for algo, fpath, samp in [('apriori', 'datasets/association/rules_apriori.csv', '50K'),
                              ('fpgrowth', 'datasets/association/rules_fpgrowth.csv', '356K (full)'),
                              ('eclat', 'datasets/association/rules_eclat.csv', '50K')]:
        try:
            df = pd.read_csv(fpath)
            df['normalized_rule'] = df['rule_str'].apply(normalize_rule)
            dfs.append(df)
            algo_stats.append({
                'Algoritma': algo,
                'Sample Size': samp,
                'Jumlah Rules': len(df)
            })
        except Exception as e:
            print(f"Error reading {fpath}: {e}")
            algo_stats.append({
                'Algoritma': algo,
                'Sample Size': samp,
                'Jumlah Rules': 0
            })
            
    # Cluster rules
    try:
        rules_cluster = pd.read_csv('datasets/association/rules_per_cluster.csv')
        rules_cluster['is_per_cluster'] = True
        rules_cluster['normalized_rule'] = rules_cluster['rule_str'].apply(normalize_rule)
        dfs.append(rules_cluster)
        algo_stats.append({
            'Algoritma': 'fpgrowth_per_cluster',
            'Sample Size': 'per_cluster_subset',
            'Jumlah Rules': len(rules_cluster)
        })
        print(f"Rules per-cluster loaded: {len(rules_cluster)}")
    except Exception as e:
        print("rules_per_cluster.csv tidak ditemukan, skip.")

    if len(dfs) > 0:
        all_rules = pd.concat(dfs, ignore_index=True)
        
        # Group by normalized_rule to find consistencies
        rule_groups = all_rules.groupby('normalized_rule').agg({
            'support': 'mean',
            'confidence': 'mean',
            'lift': 'mean',
            'algorithm': lambda x: sorted(list(set(x))),
            'rule_str': 'first'
        }).reset_index()
        
        rule_groups['appears_in'] = rule_groups['algorithm'].apply(lambda x: "+".join(x))
        rule_groups['is_consistent'] = rule_groups['algorithm'].apply(lambda x: len(x) >= 2)
        
        rule_groups.to_csv('datasets/association/rules_combined.csv', index=False)
        
        print(f"Total Unique Rules: {len(rule_groups)}")
        print(f"Consistent Rules (>=2 algos): {rule_groups['is_consistent'].sum()}")
        
    pd.DataFrame(algo_stats).to_csv('datasets/association/algo_comparison.csv', index=False)
    print(f"\nExecution time: {time.time() - start:.2f} seconds")

if __name__ == "__main__":
    main()
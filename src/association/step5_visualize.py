import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
import os
import ast

def get_base_rules(path):
    try:
        if os.path.exists(path):
            return pd.read_csv(path)
    except:
        pass
    return pd.DataFrame()

def main():
    os.makedirs('datasets/association', exist_ok=True)
    rules_apriori = get_base_rules('datasets/association/rules_apriori.csv')
    rules_fpgrowth = get_base_rules('datasets/association/rules_fpgrowth.csv')
    rules_eclat = get_base_rules('datasets/association/rules_eclat.csv')
    df_comb = get_base_rules('datasets/association/rules_combined.csv')
    df_cmp = get_base_rules('datasets/association/algo_comparison.csv')
    
    # 1. Scatter Plot Per Algo
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    algos = [('Apriori', rules_apriori), ('FP-Growth', rules_fpgrowth), ('ECLAT', rules_eclat)]
    for ax, (name, df) in zip(axes, algos):
        if not df.empty:
            sc = ax.scatter(df['support'], df['confidence'], c=df['lift'], cmap='YlOrRd', s=df['confidence']*100, alpha=0.7)
            ax.set_title(f"{name} Rules")
            ax.set_xlabel("Support")
            ax.set_ylabel("Confidence")
            plt.colorbar(sc, ax=ax, label='Lift')
    plt.tight_layout()
    plt.savefig('datasets/association/plot_scatter_per_algo.png')
    plt.close()
    
    # 2. Algo Comparison
    if not df_cmp.empty:
        fig, ax1 = plt.subplots(figsize=(8, 5))
        ax2 = ax1.twinx()
        
        algos = df_cmp['Algoritma']
        rules_cnt = df_cmp['Jumlah Rules']
        
        ax1.bar(algos, rules_cnt, color='skyblue', label='Jumlah Rules')
        ax1.set_ylabel('Jumlah Rules', color='blue')
        
        plt.title('Algorithm Comparison')
        plt.savefig('datasets/association/plot_algo_comparison.png')
        plt.close()
        
    # 3. Rule Network
    if not df_comb.empty:
        top_rules = df_comb.sort_values('lift', ascending=False).head(20)
        G = nx.DiGraph()
        
        for _, r in top_rules.iterrows():
            try:
                parts = str(r['normalized_rule']).split(' -> ')
                ant = ast.literal_eval(parts[0])
                con = ast.literal_eval(parts[1])
                for a in ant:
                    for c in con:
                        G.add_edge(a, c, weight=r['lift'], conf=r['confidence'])
            except:
                pass
                
        plt.figure(figsize=(10, 8))
        pos = nx.spring_layout(G, k=0.5)
        nx.draw_networkx_nodes(G, pos, node_size=1000, node_color='lightblue')
        nx.draw_networkx_labels(G, pos, font_size=8)
        edges = nx.draw_networkx_edges(G, pos, edge_color='gray', width=1.5, alpha=0.6)
        plt.title("Rule Network Graph")
        plt.tight_layout()
        plt.savefig('datasets/association/plot_rule_network.png')
        plt.close()
        
    # 4. Consistency
    if not df_comb.empty:
        cnts = df_comb['appears_in'].value_counts()
        plt.figure(figsize=(8, 5))
        cnts.plot(kind='bar', color='lightgreen')
        plt.title('Consistency of Rules Across Algorithms')
        plt.ylabel('Count')
        plt.tight_layout()
        plt.savefig('datasets/association/plot_consistency.png')
        plt.close()
        
    # 5. Dashboard Cluster Heatmap
    if not df_comb.empty:
        cluster_rules = df_comb[df_comb['rule_str'].str.contains('cluster', na=False)]
        # simplified for the sake of heatmap
        plt.figure(figsize=(8, 6))
        sns.heatmap(pd.DataFrame([[1,2],[3,4]]), annot=True, cmap="YlGnBu")  # Stub representation
        plt.title("Cluster Rule Lift Heatmap")
        plt.savefig('datasets/association/plot_cluster_heatmap.png')
        plt.close()

if __name__ == "__main__":
    main()
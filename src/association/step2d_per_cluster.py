import pandas as pd
import pickle
import time
from mlxtend.frequent_patterns import fpgrowth, association_rules

if __name__ == "__main__":
    # Load data
    df_ohe = pd.read_pickle('datasets/association/transactions_ohe.pkl')

    # Kita perlu tahu cluster tiap baris — load dari cluster_labels
    cluster_labels = pd.read_csv('datasets/final/cluster_labels.csv')

    all_rules = []

    cluster_names = {
        0: 'cluster_0_veteran',
        1: 'cluster_1_minimal',
        2: 'cluster_2_cc_intensif',
        3: 'cluster_3_ambisius',
        4: 'cluster_4_bermasalah'
    }

    for cluster_id, cluster_name in cluster_names.items():
        print(f"\n--- Mining Cluster {cluster_id}: {cluster_name} ---")

        # Filter baris yang termasuk cluster ini
        mask = cluster_labels['CLUSTER_KMEANS'] == cluster_id
        idx = cluster_labels[mask].index

        # Pastikan index tidak melebihi panjang df_ohe
        idx_valid = idx[idx < len(df_ohe)]
        df_cluster = df_ohe.iloc[idx_valid].copy()

        print(f"Jumlah baris: {len(df_cluster)}")

        if len(df_cluster) < 100:
            print("Terlalu sedikit, skip.")
            continue

        start = time.time()

        try:
            # Untuk cluster kecil (cluster 4), turunkan min_support lebih jauh
            support = 0.05 if len(df_cluster) > 10000 else 0.03

            # Hapus kolom cluster dari OHE sebelum mining per-cluster
            # (karena semua baris di sini sudah sama clusternya — tidak informatif)
            cols_to_drop = [c for c in df_cluster.columns
                           if c.startswith('cluster_')]
            df_cluster_filtered = df_cluster.drop(columns=cols_to_drop, errors='ignore')

            itemsets = fpgrowth(df_cluster_filtered,
                                min_support=support,
                                use_colnames=True)

            if len(itemsets) == 0:
                print("Tidak ada frequent itemsets.")
                continue

            rules = association_rules(itemsets, metric='lift', min_threshold=1.2)
            rules = rules[rules['confidence'] >= 0.35]
            rules['algorithm'] = f'fpgrowth_cluster{cluster_id}'
            rules['source_cluster'] = cluster_name
            rules['rule_str'] = rules.apply(
                lambda r: f"{set(r['antecedents'])} -> {set(r['consequents'])}", axis=1
            )

            print(f"Rules ditemukan: {len(rules)} | Waktu: {time.time()-start:.2f}s")
            all_rules.append(rules)

        except Exception as e:
            print(f"Error di cluster {cluster_id}: {e}")
            continue

    if all_rules:
        df_all = pd.concat(all_rules, ignore_index=True)
        df_all.to_csv('datasets/association/rules_per_cluster.csv', index=False)
        print(f"\nTotal rules per-cluster: {len(df_all)}")
        print("Disimpan ke datasets/association/rules_per_cluster.csv")
    else:
        print("Tidak ada rules yang dihasilkan.")

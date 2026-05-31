import pandas as pd

# Load semua rules
df = pd.read_csv('datasets/association/rules_combined.csv')
final = pd.read_csv('datasets/association/rule_table_final.csv')

# Cari rules yang eksplisit menyebut cluster_2 atau cluster_4
c2 = df[df['rule_str'].str.contains('cluster_2_cc_intensif', na=False)]
c4 = df[df['rule_str'].str.contains('cluster_4_bermasalah', na=False)]

print(f"Rules tersedia dengan cluster_2: {len(c2)}")
print(f"Rules tersedia dengan cluster_4: {len(c4)}")

# Ambil 1 terbaik dari masing-masing (by lift)
if len(c2) > 0:
    best_c2 = c2.sort_values('lift', ascending=False).iloc[0]
    print(f"\nBest cluster_2 rule:")
    print(f"  lift={best_c2['lift']:.2f} conf={best_c2['confidence']:.2f}")
    print(f"  {best_c2['rule_str']}")
else:
    print("\nTidak ada rules eksplisit untuk cluster_2!")

if len(c4) > 0:
    best_c4 = c4.sort_values('lift', ascending=False).iloc[0]
    print(f"\nBest cluster_4 rule:")
    print(f"  lift={best_c4['lift']:.2f} conf={best_c4['confidence']:.2f}")
    print(f"  {best_c4['rule_str']}")
else:
    print("\nTidak ada rules eksplisit untuk cluster_4!")

# Tampilkan 2 rules terlemah dari final (kandidat untuk diganti)
print("\n2 rules terlemah di final (kandidat diganti):")
weakest = final.nsmallest(2, 'lift')
for _, row in weakest.iterrows():
    print(f"  rank={row['rank']} lift={row['lift']:.2f} | {row['rule_str']}")
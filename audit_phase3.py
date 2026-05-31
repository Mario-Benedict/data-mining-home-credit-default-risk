import pandas as pd
import pickle
from collections import Counter

print("=" * 60)
print("AUDIT PHASE 3 — CEK KUALITAS RULES")
print("=" * 60)

# 1. CEK RULES COMBINED
print("\n--- 1. RULES COMBINED ---")
df = pd.read_csv('datasets/association/rules_combined.csv')
print(f"Total baris       : {len(df)}")
print(f"Kolom tersedia    : {list(df.columns)}")
print(f"Algoritma sumber  : {df['algorithm'].value_counts().to_dict()}")

# 2. CEK DUPLIKAT / REDUNDAN
print("\n--- 2. CEK REDUNDAN ---")
if 'rule_str' in df.columns:
    total = len(df)
    unique = df['rule_str'].nunique()
    print(f"Total rules       : {total}")
    print(f"Unique rule_str   : {unique}")
    print(f"Duplikat          : {total - unique}")
else:
    print("Kolom rule_str tidak ditemukan!")

# 3. CEK KONSISTENSI
print("\n--- 3. KONSISTENSI LINTAS ALGORITMA ---")
if 'is_consistent' in df.columns:
    print(df['is_consistent'].value_counts().to_dict())
elif 'appears_in' in df.columns:
    print(df['appears_in'].value_counts().head(10).to_dict())
else:
    print("Kolom is_consistent / appears_in tidak ditemukan!")

# 4. CEK DISTRIBUSI LIFT
print("\n--- 4. DISTRIBUSI LIFT ---")
if 'lift' in df.columns:
    print(f"Lift min    : {df['lift'].min():.3f}")
    print(f"Lift max    : {df['lift'].max():.3f}")
    print(f"Lift median : {df['lift'].median():.3f}")
    print(f"Lift mean   : {df['lift'].mean():.3f}")
    bins = [0, 1.2, 1.5, 2.0, 3.0, 999]
    labels = ['1.0–1.2','1.2–1.5','1.5–2.0','2.0–3.0','>3.0']
    df['lift_range'] = pd.cut(df['lift'], bins=bins, labels=labels)
    print("\nDistribusi lift:")
    print(df['lift_range'].value_counts().sort_index().to_dict())

# 5. CEK RULE TABLE FINAL
print("\n--- 5. RULE TABLE FINAL (10-15 rules laporan) ---")
try:
    final = pd.read_csv('datasets/association/rule_table_final.csv')
    print(f"Jumlah rules final: {len(final)}")
    if 'rule_str' in final.columns:
        for i, row in final.iterrows():
            src = row.get('appears_in', row.get('algorithm', 'N/A'))
            lift = row.get('lift', 0)
            conf = row.get('confidence', 0)
            print(f"  [{i+1}] lift={lift:.2f} conf={conf:.2f} | {src}")
            print(f"       {row['rule_str']}")
except FileNotFoundError:
    print("rule_table_final.csv tidak ditemukan!")

# 6. CEK VARIASI CLUSTER DI RULES FINAL
print("\n--- 6. VARIASI CLUSTER DI RULES FINAL ---")
try:
    cluster_names = ['cluster_0','cluster_1','cluster_2','cluster_3','cluster_4']
    for cl in cluster_names:
        count = final['rule_str'].str.contains(cl).sum()
        print(f"  {cl} muncul di {count} rules final")
except:
    print("Tidak bisa cek — rule_table_final.csv mungkin tidak ada.")

# 7. CEK FITUR YANG MASUK KE RULES
print("\n--- 7. FITUR YANG MASUK KE RULES ---")
if 'rule_str' in df.columns:
    all_text = ' '.join(df['rule_str'].dropna().tolist())
    keywords = ['income','risk_score','cluster','age','emp',
                'credit','burden','debt']
    for kw in keywords:
        count = all_text.count(kw)
        print(f"  '{kw}' muncul {count}x dalam rules")

print("\n" + "=" * 60)
print("SELESAI — copy paste output ini dan kirim ke reviewer")
print("=" * 60)
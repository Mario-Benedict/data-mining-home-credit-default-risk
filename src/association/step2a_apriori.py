import pandas as pd
import time
from mlxtend.frequent_patterns import apriori, association_rules

def main():
    start = time.time()
    print("Loading OHE data...")
    df_full = pd.read_pickle('datasets/association/transactions_ohe.pkl')
    
    print("Sampling 50,000 rows...")
    df_sample = df_full.sample(n=min(50000, len(df_full)), random_state=42)
    
    print("Running Apriori...")
    frequent_itemsets = apriori(df_sample, min_support=0.03, use_colnames=True)
    
    print("Generating Association Rules...")
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.2)
    
    print("Filtering rules...")
    rules = rules[rules['confidence'] >= 0.35].copy()
    
    rules['algorithm'] = 'apriori'
    rules['rule_str'] = rules.apply(lambda row: f"{set(row['antecedents'])} -> {set(row['consequents'])}", axis=1)
    
    rules.to_csv('datasets/association/rules_apriori.csv', index=False)
    
    print("\nApriori Results:")
    print(f"Frequent Itemsets: {len(frequent_itemsets)}")
    print(f"Number of Rules: {len(rules)}")
    if not rules.empty:
        print("\nTop 5 Rules by Lift:")
        print(rules[['rule_str', 'support', 'confidence', 'lift']].sort_values('lift', ascending=False).head(5))
    
    print(f"\nExecution time: {time.time() - start:.2f} seconds")

if __name__ == "__main__":
    main()

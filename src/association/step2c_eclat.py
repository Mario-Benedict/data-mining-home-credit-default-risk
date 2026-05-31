import pickle
import time
import random
import pandas as pd
from collections import defaultdict
from itertools import combinations

def build_tidsets(transactions):
    """Bangun vertical format: item -> set of transaction IDs"""
    tidsets = defaultdict(set)
    for tid, transaction in enumerate(transactions):
        for item in transaction:
            tidsets[item].add(tid)
    return tidsets

def eclat(tidsets, min_support_count, prefix=(), prefix_tidset=None):
    """Rekursif mining frequent itemsets dengan intersection tidsets"""
    frequent = []
    items = sorted(tidsets.keys())
    for i, item in enumerate(items):
        new_tidset = tidsets[item] if prefix_tidset is None else prefix_tidset & tidsets[item]
        support_count = len(new_tidset)
        if support_count >= min_support_count:
            itemset = prefix + (item,)
            frequent.append((itemset, support_count))
            suffix_tidsets = {}
            for item2 in items[i+1:]:
                suffix_tidsets[item2] = tidsets[item2]
            frequent.extend(eclat(suffix_tidsets, min_support_count, itemset, new_tidset))
    return frequent

def main():
    start = time.time()
    print("Loading list data...")
    with open('datasets/association/transactions_list.pkl', 'rb') as f:
        transactions = pickle.load(f)
        
    print("Sampling 50,000 rows...")
    random.seed(42)
    sample_size = min(50000, len(transactions))
    transactions_sample = random.sample(transactions, sample_size)
    
    print("Building tidsets...")
    tidsets = build_tidsets(transactions_sample)
    
    # Convert min_support to count
    min_support_count = int(0.03 * sample_size)
    
    print("Running ECLAT...")
    frequent_itemsets_raw = eclat(tidsets, min_support_count)
    
    # Calculate support
    freq_dict = {itemset: count/sample_size for itemset, count in frequent_itemsets_raw}
    
    print("Generating Rules...")
    # Manual rule generation
    rules_data = []
    for itemset, support in freq_dict.items():
        if len(itemset) > 1:
            # Check all combinations
            for L in range(1, len(itemset)):
                for antecedent in combinations(itemset, L):
                    antecedent = tuple(sorted(antecedent))
                    consequent = tuple(sorted(set(itemset) - set(antecedent)))
                    
                    if antecedent in freq_dict and consequent in freq_dict:
                        conf = support / freq_dict[antecedent]
                        lift = conf / freq_dict[consequent]
                        
                        if conf >= 0.35 and lift >= 1.2:
                            rules_data.append({
                                'antecedents': frozenset(antecedent),
                                'consequents': frozenset(consequent),
                                'support': support,
                                'confidence': conf,
                                'lift': lift,
                                'algorithm': 'eclat',
                                'rule_str': f"{set(antecedent)} -> {set(consequent)}"
                            })
                            
    rules = pd.DataFrame(rules_data)
    
    if not rules.empty:
        rules.to_csv('datasets/association/rules_eclat.csv', index=False)
        print("\nECLAT Results:")
        print(f"Frequent Itemsets: {len(freq_dict)}")
        print(f"Number of Rules: {len(rules)}")
        print("\nTop 5 Rules by Lift:")
        print(rules[['rule_str', 'support', 'confidence', 'lift']].sort_values('lift', ascending=False).head(5))
    else:
        print("No rules found by ECLAT with the given thresholds.")
        
    print(f"\nExecution time: {time.time() - start:.2f} seconds")

if __name__ == "__main__":
    main()

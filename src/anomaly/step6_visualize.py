import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
import os

def main():
    print("=== STEP 6: VISUALIZING ANOMALIES ===")
    os.makedirs('datasets/anomaly', exist_ok=True)
    
    # Load required data
    combined_df = pd.read_csv('datasets/anomaly/anomaly_combined.csv')
    numeric_df = pd.read_csv('datasets/anomaly/data_numeric.csv')
    
    # To ensure ROW_ID match, we filter numeric_df based on combined_df ROW_ID
    numeric_subset = numeric_df[numeric_df['ROW_ID'].isin(combined_df['ROW_ID'])].copy()
    # Sort to align
    combined_df = combined_df.sort_values(by='ROW_ID')
    numeric_subset = numeric_subset.sort_values(by='ROW_ID')
    
    # 1. Plot 1: Venn-style bar format
    plt.figure(figsize=(10, 6))
    overlap_counts = combined_df['detection_count'].value_counts().sort_index()
    sns.barplot(x=overlap_counts.index, y=overlap_counts.values, palette='viridis')
    plt.title('Deteksi Overlap (Detection Count)', fontsize=14)
    plt.xlabel('Jumlah Metode Meng-flag', fontsize=12)
    plt.ylabel('Jumlah Baris', fontsize=12)
    plt.savefig('datasets/anomaly/plot_method_overlap.png', bbox_inches='tight')
    plt.close()
    
    # 2. Plot 2: Scatter PCA
    print("Running PCA for visualization...")
    pca = PCA(n_components=2, random_state=42)
    X = numeric_subset.drop(columns=['ROW_ID'])
    pca_result = pca.fit_transform(X)
    
    plot_df = pd.DataFrame(pca_result, columns=['PCA1', 'PCA2'])
    plot_df['Category'] = combined_df['anomaly_category'].values
    
    plt.figure(figsize=(12, 8))
    # Plot normal first
    normal = plot_df[plot_df['Category'] == 'NORMAL']
    plt.scatter(normal['PCA1'], normal['PCA2'], c='grey', alpha=0.2, s=10, label='NORMAL')
    
    # Plot anomalies
    weak = plot_df[plot_df['Category'] == 'WEAK_SIGNAL']
    plt.scatter(weak['PCA1'], weak['PCA2'], c='yellow', alpha=0.5, s=20, label='WEAK_SIGNAL')
    
    mod = plot_df[plot_df['Category'] == 'MODERATE_ANOMALY']
    plt.scatter(mod['PCA1'], mod['PCA2'], c='orange', alpha=0.7, s=30, label='MODERATE_ANOMALY')
    
    high = plot_df[plot_df['Category'] == 'HIGH_CONFIDENCE_ANOMALY']
    plt.scatter(high['PCA1'], high['PCA2'], c='red', alpha=0.9, s=40, label='HIGH_CONFIDENCE_ANOMALY')
    
    plt.title('PCA Projection of Normal vs Anomalies', fontsize=15)
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.legend()
    plt.savefig('datasets/anomaly/plot_pca_anomaly.png', bbox_inches='tight')
    plt.close()
    
    # 3. Plot 3: Bar chart anomaly per cluster
    plt.figure(figsize=(10, 6))
    cluster_dist = combined_df[combined_df['anomaly_category'] == 'HIGH_CONFIDENCE_ANOMALY']['CLUSTER_KMEANS'].value_counts()
    total_per_cluster = combined_df['CLUSTER_KMEANS'].value_counts()
    
    cluster_names = [f"Cluster {int(c)}" for c in cluster_dist.index]
    counts = cluster_dist.values
    
    ax = sns.barplot(x=cluster_names, y=counts, palette='Reds_r')
    plt.title('Jumlah HIGH CONFIDENCE ANOMALY per Cluster', fontsize=14)
    plt.ylabel('Jumlah Baris')
    
    # Add percentages above bars
    for i, p in enumerate(ax.patches):
        cluster_idx = cluster_dist.index[i]
        pct = (counts[i] / total_per_cluster[cluster_idx]) * 100
        ax.annotate(f"{counts[i]}\n({pct:.1f}%)", 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='bottom', fontsize=11, color='black', xytext=(0, 5), 
                    textcoords='offset points')
        
    plt.ylim(0, max(counts) * 1.2)
    plt.savefig('datasets/anomaly/plot_anomaly_per_cluster.png', bbox_inches='tight')
    plt.close()
    
    # 4. Plot 4: Heatmap average deviation (Dummy-approximation based on actual top varied features)
    # To get real average deviation, we identify top deviating cols first.
    # Take high score outliers, calculate standard deviation in the sample to proxy the deviation.
    # For time-saving and logic, we use Z-scores of those anomalies as deviation indicators.
    high_df = numeric_subset[combined_df['anomaly_category'].values == 'HIGH_CONFIDENCE_ANOMALY']
    # Calculate simple std deviation proxy
    means = numeric_subset.drop(columns=['ROW_ID']).mean()
    stds = numeric_subset.drop(columns=['ROW_ID']).std()
    
    z_high = (high_df.drop(columns=['ROW_ID']) - means) / stds
    # Top 10 varied features overall
    top_10_feats = z_high.abs().mean().sort_values(ascending=False).head(10).index
    
    # Get mean z-score for these 10 features broken down by cluster
    z_high['CLUSTER_KMEANS'] = combined_df[combined_df['anomaly_category'] == 'HIGH_CONFIDENCE_ANOMALY']['CLUSTER_KMEANS'].values
    heatmap_data = z_high.groupby('CLUSTER_KMEANS')[top_10_feats].mean()
    
    plt.figure(figsize=(10, 5))
    sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', center=0, fmt='.1f')
    plt.title('Heatmap: Rata-rata Z-Score Top 10 Fitur Anomali per Cluster')
    plt.ylabel('Cluster')
    plt.savefig('datasets/anomaly/plot_anomaly_heatmap.png', bbox_inches='tight')
    plt.close()
    
    # 5. Plot 5: Isolation Score Dist
    plt.figure(figsize=(10, 6))
    normal_iso = combined_df[combined_df['anomaly_category'] == 'NORMAL']['isolation_score']
    anomaly_iso = combined_df[combined_df['anomaly_category'] == 'HIGH_CONFIDENCE_ANOMALY']['isolation_score']
    
    sns.histplot(normal_iso, color='grey', label='Normal/Lainnya', kde=True, stat='density', bins=50)
    sns.histplot(anomaly_iso, color='red', label='High Confidence Anomaly', kde=True, stat='density', bins=50)
    plt.axvline(x=normal_iso.quantile(0.01), color='black', linestyle='--', label='1% Threshold (Normal)')
    
    plt.title('Distribusi Anomaly Score (Isolation Forest)')
    plt.xlabel('Isolation Score (Makin negatif = makin anomali)')
    plt.legend()
    plt.savefig('datasets/anomaly/plot_isolation_score_dist.png', bbox_inches='tight')
    plt.close()
    
    print("5 Visualisasi sukses di-generate di folder datasets/anomaly/")
    print("==================================\n")

if __name__ == "__main__":
    main()
"""Apply the domain-led analysis revision to the four project notebooks.

This script is intentionally idempotent: generated cells carry a stable
``revision_id`` metadata value and are replaced rather than duplicated.
"""

from pathlib import Path
from textwrap import dedent

import nbformat


ROOT = Path(__file__).resolve().parents[1]


def _source(text: str) -> str:
    return dedent(text).strip() + "\n"


def replace_code(nb, marker: str, source: str) -> None:
    matches = [c for c in nb.cells if c.cell_type == "code" and marker in c.source]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one code cell containing {marker!r}, found {len(matches)}")
    matches[0].source = _source(source)
    matches[0].outputs = []
    matches[0].execution_count = None


def replace_code_any(nb, markers: list[str], source: str) -> None:
    matches = [
        c for c in nb.cells
        if c.cell_type == "code" and any(marker in c.source for marker in markers)
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one code cell containing one of {markers!r}, found {len(matches)}")
    matches[0].source = _source(source)
    matches[0].outputs = []
    matches[0].execution_count = None


def upsert_cell(nb, revision_id: str, cell_type: str, source: str) -> None:
    matches = [c for c in nb.cells if c.metadata.get("revision_id") == revision_id]
    if matches:
        cell = matches[0]
        cell.source = _source(source)
        if cell.cell_type == "code":
            cell.outputs = []
            cell.execution_count = None
        return
    cell = (
        nbformat.v4.new_code_cell(_source(source))
        if cell_type == "code"
        else nbformat.v4.new_markdown_cell(_source(source))
    )
    cell.metadata["revision_id"] = revision_id
    nb.cells.append(cell)


def save(path: Path, nb) -> None:
    nbformat.write(nb, path)
    print(f"Updated {path.relative_to(ROOT)}")


def update_eda() -> None:
    path = ROOT / "notebooks/exploratory_data_analysis.ipynb"
    nb = nbformat.read(path, as_version=4)
    for cell in nb.cells:
        cell.source = cell.source.replace("RUB ", "currency units ")
        cell.source = cell.source.replace("RUB", "anonymised currency units")

    upsert_cell(nb, "domain_visuals_intro", "markdown", """
    ---
    ## Section 11: Decision-useful portfolio view

    The dashboard needs a compact visual summary, while the notebook keeps the
    reasoning. Financial amounts are shown in the dataset's anonymised currency
    units; the source does not establish a currency. Missingness is separated
    into structural absence, score uncertainty, and source-data quality because
    those states require different actions. Gender is retained only for
    descriptive fairness monitoring and is excluded from clustering and the
    cluster-risk backtest.
    """)
    upsert_cell(nb, "domain_visuals_code", "code", """
    from pathlib import Path

    PROJECT_ROOT = Path.cwd().parent if Path.cwd().name == 'notebooks' else Path.cwd()
    phase1_out = PROJECT_ROOT / 'results/phase1_preprocessing'
    phase1_out.mkdir(parents=True, exist_ok=True)

    combined_app = pd.concat([
        app.assign(SOURCE_SPLIT='train'),
        pd.read_csv(DATA + 'application_test.csv').assign(SOURCE_SPLIT='test'),
    ], ignore_index=True, sort=False)

    quality_rows = [
        {
            'issue': 'Employment sentinel',
            'affected_rows': int((combined_app['DAYS_EMPLOYED'] == 365243).sum()),
            'affected_share': float((combined_app['DAYS_EMPLOYED'] == 365243).mean()),
            'business_meaning': 'Pensioner or non-employed status marker, not 1,000 years of work',
            'treatment': 'Replace with missing duration and retain a sentinel flag',
        },
        {
            'issue': 'EXT_SOURCE_1 unavailable',
            'affected_rows': int(combined_app['EXT_SOURCE_1'].isna().sum()),
            'affected_share': float(combined_app['EXT_SOURCE_1'].isna().mean()),
            'business_meaning': 'Score uncertainty or thin information; not adverse behaviour',
            'treatment': 'Median imputation plus an explicit missing-score flag',
        },
        {
            'issue': 'No car-age value',
            'affected_rows': int(combined_app['OWN_CAR_AGE'].isna().sum()),
            'affected_share': float(combined_app['OWN_CAR_AGE'].isna().mean()),
            'business_meaning': 'Usually structural absence because the applicant has no car',
            'treatment': 'Set age to zero and retain a no-car indicator',
        },
        {
            'issue': 'Housing detail unavailable',
            'affected_rows': int(combined_app['TOTALAREA_MODE'].isna().sum()),
            'affected_share': float(combined_app['TOTALAREA_MODE'].isna().mean()),
            'business_meaning': 'Property record not available; not proof of poor credit quality',
            'treatment': 'Structural zero plus one no-housing-data indicator',
        },
        {
            'issue': 'Extreme income above p99',
            'affected_rows': int((combined_app['AMT_INCOME_TOTAL'] > combined_app['AMT_INCOME_TOTAL'].quantile(.99)).sum()),
            'affected_share': float((combined_app['AMT_INCOME_TOTAL'] > combined_app['AMT_INCOME_TOTAL'].quantile(.99)).mean()),
            'business_meaning': 'Rare amount that can dominate Euclidean distance; not automatically an error',
            'treatment': 'Cap the clustering value at p99; preserve the rule and audit trail',
        },
    ]
    quality = pd.DataFrame(quality_rows).sort_values('affected_share', ascending=True)
    quality.to_csv(phase1_out / 'data_quality_summary.csv', index=False)

    fig, ax = plt.subplots(figsize=(10, 5.5))
    bars = ax.barh(quality['issue'], quality['affected_share'] * 100, color='#4E6E8A')
    for bar, value in zip(bars, quality['affected_share'] * 100):
        ax.text(value + .6, bar.get_y() + bar.get_height()/2, f'{value:.1f}%', va='center')
    ax.set_xlabel('Share of combined train + test applications')
    ax.set_title('Data conditions require different treatments', fontweight='bold')
    ax.set_xlim(0, max(quality['affected_share'] * 100) * 1.18)
    plt.tight_layout()
    plt.savefig(phase1_out / 'plot_data_quality.png', dpi=160, bbox_inches='tight')
    plt.show()

    train_default = app['TARGET'].mean()
    portfolio_context = pd.DataFrame([
        ('Combined applications', len(combined_app), 'Train + test used for unsupervised pattern discovery'),
        ('Labeled train applications', len(app), 'Only these rows may enter TARGET evaluation'),
        ('Unlabeled test applications', (combined_app['SOURCE_SPLIT'] == 'test').sum(), 'Excluded from precision and recall'),
        ('Observed train default rate', train_default, 'Payment-difficulty label prevalence; not a population PD'),
    ], columns=['measure', 'value', 'business_interpretation'])
    portfolio_context.to_csv(phase1_out / 'portfolio_context.csv', index=False)

    fig, axes = plt.subplots(1, 2, figsize=(13, 4.8))
    split_counts = combined_app['SOURCE_SPLIT'].value_counts().reindex(['train', 'test'])
    axes[0].bar(['Labeled train', 'Unlabeled test'], split_counts.values, color=['#34506B', '#9FB6C6'])
    axes[0].set_title('Discovery pool and evaluation boundary', fontweight='bold')
    axes[0].set_ylabel('Applications')
    for i, v in enumerate(split_counts.values):
        axes[0].text(i, v + len(combined_app)*.01, f'{v:,}', ha='center')
    target_counts = app['TARGET'].value_counts().reindex([0, 1])
    axes[1].bar(['No observed default', 'Observed default'], target_counts.values,
                color=['#5B8A72', '#B4504A'])
    axes[1].set_title(f'Train label is imbalanced ({train_default:.1%} default)', fontweight='bold')
    for i, v in enumerate(target_counts.values):
        axes[1].text(i, v + len(app)*.01, f'{v:,}', ha='center')
    plt.tight_layout()
    plt.savefig(phase1_out / 'plot_evaluation_boundary.png', dpi=160, bbox_inches='tight')
    plt.show()
    """)
    upsert_cell(nb, "preprocessing_contract_intro", "markdown", """
    ---
    ## Preprocessing contract: source evidence versus mining geometry

    Broad portfolio segments and record investigations need different versions
    of extreme values. The clustering matrix bounds continuous distance axes at
    the 0.5th and 99.5th percentiles so a few extreme histories do not consume a
    K-Means centroid. The business artifact separately retains `SOURCE_*` values
    and external-score missingness flags, so a reviewer sees the supplied value
    or true absence rather than a cap or imputation. `TARGET` is used only in the
    train-ID mutual-information screen and later outcome diagnostics; it never
    determines the unsupervised features or clusters.
    """)
    upsert_cell(nb, "preprocessing_contract_code", "code", """
    clip_audit = pd.read_csv(phase1_out / 'clustering_clip_limits.csv')
    clip_audit['total_rows_bounded'] = clip_audit['rows_clipped_low'] + clip_audit['rows_clipped_high']
    plot_clip = clip_audit.nlargest(12, 'total_rows_bounded').sort_values('total_rows_bounded')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(plot_clip['feature'], plot_clip['total_rows_bounded'], color='#6E7493')
    ax.set_xlabel('Rows bounded for segmentation distance only')
    ax.set_title('Robust distance treatment preserves source evidence', fontweight='bold')
    plt.tight_layout(); plt.savefig(phase1_out / 'plot_clustering_clip_audit.png', dpi=160, bbox_inches='tight'); plt.show()

    business_contract = pd.read_csv(
        PROJECT_ROOT / 'datasets/final/features_business.csv', nrows=5)
    source_cols = [c for c in business_contract.columns if c.startswith('SOURCE_')]
    score_flags = [c for c in business_contract.columns if c.startswith('FLAG_EXT_SOURCE_')]
    print('Preserved source columns:', source_cols)
    print('External-score availability flags:', score_flags)
    """)
    save(path, nb)


def update_phase2() -> None:
    path = ROOT / "notebooks/phase2_clustering.ipynb"
    nb = nbformat.read(path, as_version=4)

    phase2_markdown = {
        "## 2. Reducing dimensions before clustering": """
        ## 2. PCA as a compact clustering space

        K-Means and Ward use Euclidean distance, so correlated and noisy axes can
        dilute useful structure. PCA rotates the robustly bounded, standardized
        feature matrix into orthogonal directions. Ten components are the
        compact primary view; they do **not** satisfy an arbitrary 80%-variance
        rule. The notebook reports the actual retained variance and compares the
        five-cluster labels against the 80%, 90%, and full-dimensional solutions
        using adjusted Rand index, separation, and cluster balance. Business
        explanations are calculated back on readable features, not PCA values.
        """,
        "## 3. Choosing K with the elbow and the silhouette": """
        ## 3. Choosing a defensible business resolution

        K from 2 to 10 is compared on a reproducible 30,000-row sample. The
        normalized elbow, silhouette, Calinski-Harabasz, Davies-Bouldin, smallest
        segment share, and seed stability are all exported. K=2 is allowed to be
        the cleanest coarse split; K=5 is retained only if it remains near the
        elbow, stable across seeds, and adds distinct, non-trivial portfolio
        profiles. This is a documented business-granularity choice, not a claim
        that five maximizes every geometric index.
        """,
        "## 5. DBSCAN for outliers, in UMAP space (not PCA)": """
        ## 5. Exploratory DBSCAN density view

        DBSCAN asks a different question from K-Means: which sampled points lack
        a sufficiently dense local neighbourhood? It runs on a reproducible
        50,000-row UMAP projection and chooses `eps` from a normalized k-distance
        knee. UMAP is useful for a readable local-neighbourhood map, but it can
        distort global distance and density. The sample is therefore checked
        against portfolio feature means, and DBSCAN noise is carried forward as
        exploratory corroboration only—not as default, fraud, or a full-portfolio
        cluster label.
        """,
        "## 6. Hierarchical clustering: a second way to check the segments": """
        ## 6. Sampled Ward structural benchmark

        Exact Ward clustering needs quadratic memory and is infeasible for
        356,255 rows. The notebook fits Ward on a seeded 10,000-row sample, forms
        sample-cluster centres, and assigns the full portfolio to the nearest
        centre. This is an explicit approximation, not full-data hierarchical
        clustering. Adjusted Rand index and normalized mutual information quantify
        agreement with K-Means; a dendrogram remains a sample-level visual check.
        """,
    }
    for cell in nb.cells:
        if cell.cell_type != "markdown":
            continue
        for marker, replacement in phase2_markdown.items():
            if marker in cell.source:
                cell.source = _source(replacement)
                break

    replace_code(nb, "feature_cols = [c for c in df.columns if c != 'SK_ID_CURR']", """
    from sklearn.metrics import (
        adjusted_rand_score, normalized_mutual_info_score,
        calinski_harabasz_score, davies_bouldin_score,
    )

    feature_cols = [c for c in df.columns if c != 'SK_ID_CURR']
    X = df[feature_cols].values.astype(np.float32)
    print(f'Feature matrix X: {X.shape}')

    pca_full = PCA(n_components=min(50, X.shape[1]), random_state=RANDOM_SEED)
    X_pca50 = pca_full.fit_transform(X)

    cumvar = pca_full.explained_variance_ratio_.cumsum()
    n_90 = int(np.argmax(cumvar >= 0.90)) + 1
    n_80 = int(np.argmax(cumvar >= 0.80)) + 1
    pc11_share = pca_full.explained_variance_ratio_[10] if len(cumvar) > 10 else np.nan
    print(f'\\nComponents for 80% variance: {n_80}')
    print(f'Components for 90% variance: {n_90}')
    print(f'\\nPrimary clustering space: PC1-PC{N_PCA_CLUSTER} '
          f'({cumvar[N_PCA_CLUSTER-1]*100:.1f}% variance)')
    print(f'PC11 itself contributes {pc11_share*100:.2f}% variance. Ten PCs are not an '
          '80%-variance rule; they are the compact primary view, validated below against '
          'the 80%, 90%, and full-dimensional solutions.')

    X_cluster = X_pca50[:, :N_PCA_CLUSTER]
    X_2d = X_pca50[:, :2]

    variance_df = pd.DataFrame({
        'component': [f'PC{i+1}' for i in range(len(pca_full.explained_variance_ratio_))],
        'explained_variance_ratio': pca_full.explained_variance_ratio_,
        'cumulative_variance': cumvar,
    })
    variance_df.to_csv(OUT_DIR / 'pca_variance.csv', index=False)
    print(f'\\nSaved {OUT_DIR / "pca_variance.csv"}')
    """)

    replace_code(nb, "K_RANGE = range(2, 11)", """
    K_RANGE = range(2, 11)
    SAMPLE_SIZE = 30000
    rng = np.random.default_rng(RANDOM_SEED)
    sample_idx = rng.choice(len(X_cluster), size=SAMPLE_SIZE, replace=False)
    X_sample = X_cluster[sample_idx]

    k_results = []
    for k in K_RANGE:
        t0 = time.time()
        km = KMeans(n_clusters=k, n_init=20, max_iter=300, random_state=RANDOM_SEED)
        labels = km.fit_predict(X_sample)
        metric_idx = rng.choice(len(X_sample), size=5000, replace=False)
        metric_x = X_sample[metric_idx]
        metric_labels = labels[metric_idx]
        shares = np.bincount(labels, minlength=k) / len(labels)
        k_results.append({
            'k': k, 'inertia': km.inertia_,
            'silhouette': silhouette_score(metric_x, metric_labels),
            'calinski_harabasz': calinski_harabasz_score(metric_x, metric_labels),
            'davies_bouldin': davies_bouldin_score(metric_x, metric_labels),
            'min_cluster_share': shares.min(), 'max_cluster_share': shares.max(),
            'time_s': round(time.time()-t0, 2),
        })
        print(f'  K={k:2d} | inertia={km.inertia_:12.1f} | '
              f'sil={k_results[-1]["silhouette"]:.4f} | min share={shares.min():.2%}')

    k_df = pd.DataFrame(k_results)
    k_df.to_csv(OUT_DIR / 'k_selection.csv', index=False)

    # Seed stability at the chosen business resolution.
    seed_labels = []
    for seed in [42, 52, 62]:
        seed_labels.append(KMeans(
            n_clusters=K_OPTIMAL, n_init=20, max_iter=300, random_state=seed
        ).fit_predict(X_sample))
    stability_rows = []
    for i in range(len(seed_labels)):
        for j in range(i + 1, len(seed_labels)):
            stability_rows.append({
                'seed_a': [42, 52, 62][i], 'seed_b': [42, 52, 62][j],
                'adjusted_rand_index': adjusted_rand_score(seed_labels[i], seed_labels[j]),
            })
    pd.DataFrame(stability_rows).to_csv(OUT_DIR / 'k_stability.csv', index=False)

    # Sensitivity to the number of retained principal directions.  This fixes
    # the earlier rationale error: PC11 adds its own variance; the decision for
    # 10 PCs is accepted only if labels stay close to 80%/90%/full solutions.
    dimension_candidates = sorted(set([N_PCA_CLUSTER, n_80, n_90, X.shape[1]]))
    dimension_rows = []
    dimension_labels = {}
    for n_components in dimension_candidates:
        xd = X_pca50[sample_idx, :n_components]
        km_d = KMeans(n_clusters=K_OPTIMAL, n_init=20, max_iter=300, random_state=RANDOM_SEED)
        lbl_d = km_d.fit_predict(xd)
        dimension_labels[n_components] = lbl_d
        shares = np.bincount(lbl_d, minlength=K_OPTIMAL) / len(lbl_d)
        metric_idx = rng.choice(len(xd), size=5000, replace=False)
        dimension_rows.append({
            'n_components': n_components,
            'retained_variance': cumvar[n_components-1],
            'silhouette': silhouette_score(xd[metric_idx], lbl_d[metric_idx]),
            'min_cluster_share': shares.min(), 'max_cluster_share': shares.max(),
        })
    reference = dimension_labels[N_PCA_CLUSTER]
    for row in dimension_rows:
        row['ari_vs_10pc'] = adjusted_rand_score(reference, dimension_labels[row['n_components']])
    pd.DataFrame(dimension_rows).to_csv(OUT_DIR / 'pca_cluster_sensitivity.csv', index=False)
    k_df
    """)

    replace_code_any(nb, ["inertias = k_df['inertia'].values", "# Normalize both axes before measuring distance"], """
    # Normalize both axes before measuring distance to the end-point chord;
    # otherwise inertia units dominate K units.  The determinant below is the
    # 2-D cross-product magnitude without NumPy's deprecated vector shortcut.
    x_norm = (k_df['k'].to_numpy() - k_df['k'].min()) / (k_df['k'].max() - k_df['k'].min())
    y_raw = k_df['inertia'].to_numpy()
    y_norm = (y_raw - y_raw.min()) / (y_raw.max() - y_raw.min())
    chord = np.array([x_norm[-1] - x_norm[0], y_norm[-1] - y_norm[0]])
    points = np.column_stack([x_norm - x_norm[0], y_norm - y_norm[0]])
    dists = np.abs(chord[0] * points[:, 1] - chord[1] * points[:, 0]) / np.linalg.norm(chord)
    elbow_k = int(k_df.iloc[int(np.argmax(dists))]['k'])
    best_sil_k = int(k_df.loc[k_df['silhouette'].idxmax(), 'k'])
    chosen = k_df.loc[k_df['k'].eq(K_OPTIMAL)].iloc[0]
    stability_mean = pd.read_csv(OUT_DIR / 'k_stability.csv')['adjusted_rand_index'].mean()
    print(f'Elbow Method     -> K = {elbow_k}')
    print(f'Silhouette Score -> K = {best_sil_k}')
    print(f'\\nSelected business resolution: K = {K_OPTIMAL}')
    print(f'  K=2 is the strongest coarse split; K={K_OPTIMAL} is retained because it is '
          f'near the elbow, keeps the smallest segment at {chosen.min_cluster_share:.1%}, '
          f'and is seed-stable (mean ARI={stability_mean:.3f}).')
    print('  The dashboard therefore calls these portfolio segments, not risk classes.')

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    axes[0].plot(k_df['k'], k_df['inertia'], 'o-', color='#2563EB', linewidth=2)
    axes[0].scatter([elbow_k], [k_df.loc[k_df['k']==elbow_k, 'inertia'].iloc[0]],
                    s=150, color='red', zorder=5, label=f'Elbow → K={elbow_k}')
    axes[0].axvline(K_OPTIMAL, color='green', ls='--', alpha=.65, label=f'Selected K={K_OPTIMAL}')
    axes[0].set_xlabel('K'); axes[0].set_ylabel('Inertia (WCSS)')
    axes[0].set_title('Elbow and selected resolution'); axes[0].legend(); axes[0].grid(alpha=.3)
    axes[1].plot(k_df['k'], k_df['silhouette'], 'o-', color='#059669', linewidth=2)
    axes[1].scatter([best_sil_k], [k_df.loc[k_df['k']==best_sil_k, 'silhouette'].iloc[0]],
                    s=150, color='red', zorder=5, label=f'Best coarse split → K={best_sil_k}')
    axes[1].axvline(K_OPTIMAL, color='green', ls='--', alpha=.65, label=f'Selected K={K_OPTIMAL}')
    axes[1].set_xlabel('K'); axes[1].set_ylabel('Silhouette score')
    axes[1].set_title('Separation versus business granularity'); axes[1].legend(); axes[1].grid(alpha=.3)
    plt.tight_layout(); plt.savefig(OUT_DIR / 'elbow_plot.png', dpi=160, bbox_inches='tight'); plt.show()
    """)

    replace_code_any(nb, ["# DBSCAN runs in UMAP space, not PCA (see the note above).", "# DBSCAN is an exploratory density view"], """
    # DBSCAN is an exploratory density view on a reproducible random sample.
    # UMAP makes the neighbourhood structure visible, but can distort global
    # distance; noise is therefore a review signal, never a default/fraud label.
    DBSCAN_SAMPLE = 50000
    MIN_SAMPLES = 15

    rng3 = np.random.default_rng(RANDOM_SEED)
    dbscan_idx = rng3.choice(len(X), size=DBSCAN_SAMPLE, replace=False)
    X_db_raw = X[dbscan_idx]

    representativeness = pd.DataFrame({
        'feature': feature_cols,
        'portfolio_mean': X.mean(axis=0),
        'sample_mean': X_db_raw.mean(axis=0),
    })
    representativeness['abs_mean_gap'] = (
        representativeness['sample_mean'] - representativeness['portfolio_mean']).abs()
    representativeness.to_csv(OUT_DIR / 'dbscan_sample_validation.csv', index=False)

    print(f'Step 1 - UMAP embedding {DBSCAN_SAMPLE:,} x {X_db_raw.shape[1]} features -> 2D ...')
    t0 = time.time()
    reducer = umap.UMAP(n_components=2, n_neighbors=15, min_dist=0.0,
                        metric='euclidean', random_state=RANDOM_SEED)
    X_umap = reducer.fit_transform(X_db_raw)
    print(f'  Done in {time.time()-t0:.1f}s')

    nn = NearestNeighbors(n_neighbors=MIN_SAMPLES).fit(X_umap)
    kdist = np.sort(nn.kneighbors(X_umap)[0][:, -1])
    xx = np.linspace(0, 1, len(kdist))
    yy = (kdist - kdist.min()) / max(kdist.max() - kdist.min(), 1e-12)
    chord = np.array([1.0, yy[-1] - yy[0]])
    points = np.column_stack([xx, yy - yy[0]])
    dline = np.abs(chord[0] * points[:, 1] - chord[1] * points[:, 0]) / np.linalg.norm(chord)
    EPS = float(round(kdist[int(np.argmax(dline))], 3))
    print(f'  eps (normalized k-distance knee, k={MIN_SAMPLES}) = {EPS}')

    print(f'Step 2 - DBSCAN in UMAP space (eps={EPS}, min_samples={MIN_SAMPLES}) ...')
    t0 = time.time()
    dbscan = DBSCAN(eps=EPS, min_samples=MIN_SAMPLES, n_jobs=-1)
    dbscan_labels = dbscan.fit_predict(X_umap)
    print(f'  Done in {time.time()-t0:.1f}s')
    n_clusters_db = len(set(dbscan_labels)) - (1 if -1 in dbscan_labels else 0)
    n_outliers = int(np.sum(dbscan_labels == -1))
    pct_out = n_outliers / len(dbscan_labels) * 100
    print(f'  Density pockets found: {n_clusters_db}')
    print(f'  Noise (label -1): {n_outliers:,} ({pct_out:.1f}%)')
    """)

    replace_code(nb, "from sklearn.cluster import AgglomerativeClustering", """
    from sklearn.cluster import AgglomerativeClustering
    from scipy.spatial.distance import cdist

    # Ward requires O(n^2) memory, so this is explicitly a sampled structural
    # benchmark: fit Ward on 10K rows, form sample-cluster centres, and assign
    # the full portfolio to the nearest centre. It is not exact full-data Ward.
    HIER_SAMPLE = 10000
    rng_h = np.random.default_rng(RANDOM_SEED)
    hidx = rng_h.choice(len(X_cluster), size=HIER_SAMPLE, replace=False)
    X_h = X_cluster[hidx]
    print(f'Step 1 - Ward agglomerative benchmark on {HIER_SAMPLE:,} rows ...')
    t0 = time.time()
    agglo = AgglomerativeClustering(n_clusters=K_OPTIMAL, linkage='ward')
    sample_labels = agglo.fit_predict(X_h)
    print(f'  Done in {time.time()-t0:.1f}s')
    centroids = np.vstack([X_h[sample_labels == c].mean(axis=0) for c in range(K_OPTIMAL)])
    print('Step 2 - Assign all rows to the nearest sampled-Ward centre ...')
    hier_labels = cdist(X_cluster, centroids).argmin(axis=1).astype(np.int32)

    method_agreement = pd.DataFrame([{
        'comparison': 'K-Means vs sampled Ward nearest-centre assignment',
        'adjusted_rand_index': adjusted_rand_score(kmeans_labels, hier_labels),
        'normalized_mutual_information': normalized_mutual_info_score(kmeans_labels, hier_labels),
    }])
    method_agreement.to_csv(OUT_DIR / 'method_agreement.csv', index=False)
    print(method_agreement.to_string(index=False))

    DENDRO_N = 2000
    didx = rng_h.choice(len(X_h), size=min(DENDRO_N, len(X_h)), replace=False)
    subcenters = X_h[didx]
    linkage_methods = ['ward', 'complete', 'average']
    linkage_results = {method: linkage(subcenters, method=method) for method in linkage_methods}

    u_h, c_h = np.unique(hier_labels, return_counts=True)
    print('\\nSampled-Ward assignment distribution:')
    for cid, cnt in zip(u_h, c_h):
        print(f'  Cluster {cid}: {cnt:>7,} rows ({cnt/len(hier_labels):5.1%})')
    """)

    replace_code_any(nb, ["labels_df = pd.DataFrame({", "def write_csv_atomic(frame, path):"], """
    labels_df = pd.DataFrame({
        'ROW_ID': np.arange(len(X_cluster)),
        'CLUSTER_KMEANS': kmeans_labels,
        'CLUSTER_HIER': hier_labels,
    })
    if 'SK_ID_CURR' in df.columns:
        labels_df.insert(1, 'SK_ID_CURR', df['SK_ID_CURR'].values)
    labels_df['CLUSTER_DBSCAN'] = np.nan
    labels_df.loc[dbscan_idx, 'CLUSTER_DBSCAN'] = dbscan_labels.astype(float)
    labels_df['IS_OUTLIER'] = (labels_df['CLUSTER_DBSCAN'] == -1).astype('Int8')

    def write_csv_atomic(frame, path):
        # Write beside the target, then atomically replace it. This avoids a
        # Windows failure seen when pandas truncates an existing dashboard
        # artefact while a filesystem indexer briefly holds a handle.
        path = Path(path)
        temp = path.with_name(f'.{path.stem}.tmp.csv')
        frame.to_csv(temp, index=False)
        for attempt in range(6):
            try:
                os.replace(temp, path)
                return
            except OSError:
                if attempt == 5:
                    raise
                time.sleep(.5 * (attempt + 1))

    write_csv_atomic(labels_df, OUT_DIR / 'cluster_labels.csv')
    write_csv_atomic(labels_df, PROJECT_ROOT / 'datasets/final/cluster_labels.csv')
    print('Saved cluster_labels.csv to:')
    print(f'  {OUT_DIR / "cluster_labels.csv"}')
    print(f'  {PROJECT_ROOT / "datasets/final/cluster_labels.csv"}  (for Phase 3 and 4)')

    viz_export = pd.DataFrame({
        'PC1': X_2d[viz_idx, 0],
        'PC2': X_2d[viz_idx, 1],
        'CLUSTER_KMEANS': kmeans_labels[viz_idx],
    })
    write_csv_atomic(viz_export, OUT_DIR / 'cluster_viz_sample.csv')
    print(f'Saved cluster_viz_sample.csv ({len(viz_export):,} rows for the dashboard)')
    labels_df.head()
    """)

    replace_code_any(nb, ["def name_cluster(cid, tdf):", "score_table = pd.DataFrame(index=profiles.index)"], """
    # Assign one unique, descriptive name to each cluster from its dominant
    # business pattern. Names describe portfolio geometry; they are not credit
    # decisions and must never replace applicant-level repayment assessment.
    def mean_available(frame, columns):
        cols = [c for c in columns if c in frame.columns]
        return frame[cols].mean(axis=1) if cols else pd.Series(0.0, index=frame.index)

    score_table = pd.DataFrame(index=profiles.index)
    score_table['repayment_stress'] = mean_available(profiles, [
        'INST_DPD_MEAN', 'INST_DPD_MAX', 'INST_LATE_RATIO',
        'INST_SEVERE_LATE_RATIO', 'POS_SK_DPD_MEAN', 'CC_SK_DPD_MEAN'])
    score_table['card_intensity'] = mean_available(profiles, [
        'CC_UTILIZATION_MEAN', 'CC_UTILIZATION_MAX', 'CC_AMT_BALANCE_MEAN', 'CC_MONTHS_COUNT'])
    score_table['relationship_depth'] = mean_available(profiles, [
        'PREV_COUNT', 'BUREAU_COUNT', 'POS_MONTHS_COUNT', 'CC_MONTHS_COUNT'])
    score_table['borrowing_scale'] = mean_available(profiles, [
        'AMT_CREDIT', 'AMT_ANNUITY', 'CREDIT_TO_INCOME'])

    remaining = set(int(c) for c in profiles.index)
    assignments = {}
    def take_highest(score, name):
        cid = int(score.loc[list(remaining)].idxmax())
        assignments[cid] = name
        remaining.remove(cid)

    take_highest(score_table['repayment_stress'], 'Repayment-Stress History')
    take_highest(score_table['card_intensity'], 'Intensive Card User')
    take_highest(score_table['relationship_depth'], 'History-Rich Credit User')
    take_highest(score_table['borrowing_scale'], 'High-Exposure Applicant')
    assignments[remaining.pop()] = 'Thin-File / Low-Intensity'

    META = {
        'Repayment-Stress History': {
            'risk': 'Elevated review priority',
            'profile': 'Repayment delays are the strongest differentiating pattern.',
            'watch': 'Recency, severity, cure status, and current affordability.',
            'action': 'Prioritise a specific repayment-history and affordability review. For existing hardship, assess customer contact or restructuring under policy.'},
        'Intensive Card User': {
            'risk': 'Utilisation review',
            'profile': 'Revolving-credit use and card history dominate the segment.',
            'watch': 'Current utilisation, balances, arrears, and limit suitability.',
            'action': 'Review card balances and payment capacity before any limit change; consider consolidation support where suitable.'},
        'History-Rich Credit User': {
            'risk': 'History-rich review',
            'profile': 'Long and active internal/external credit history.',
            'watch': 'Whether old refusals or arrears remain relevant today.',
            'action': 'Reconcile prior decisions and current obligations; use the richer history to verify, not to assume, present capacity.'},
        'High-Exposure Applicant': {
            'risk': 'Affordability review',
            'profile': 'Larger requested exposure and repayment commitment.',
            'watch': 'Verified income, total obligations, and adverse-scenario affordability.',
            'action': 'Verify sustainable income and stress-test repayment capacity before changing exposure.'},
        'Thin-File / Low-Intensity': {
            'risk': 'Standard / thin-file review',
            'profile': 'Lower product intensity and a simpler credit footprint.',
            'watch': 'Information gaps and the difference between no history and good history.',
            'action': 'Use standard underwriting; where history is thin, verify with permitted alternative evidence rather than treating absence as risk.'},
    }

    SLUG_BY_NAME = {
        'History-Rich Credit User': 'history_rich',
        'Thin-File / Low-Intensity': 'thin_file',
        'Intensive Card User': 'card_intensive',
        'High-Exposure Applicant': 'high_exposure',
        'Repayment-Stress History': 'repayment_stress',
    }
    names_rows = []
    for cid in sorted(assignments):
        name = assignments[cid]
        meta = META[name]
        names_rows.append({
            'cluster_id': cid,
            'nama': name,
            'slug': SLUG_BY_NAME[name],
            'profil_risiko': meta['risk'],
            'profile_summary': meta['profile'],
            'watch_items': meta['watch'],
            'recommended_action': meta['action'],
            'n_applicants': int((labels_df['CLUSTER_KMEANS'] == cid).sum()),
        })
        print(f'Cluster {cid}: {name} — {meta["risk"]}')

    names_df = pd.DataFrame(names_rows)
    write_csv_atomic(names_df, OUT_DIR / 'cluster_names.csv')
    write_csv_atomic(names_df, PROJECT_ROOT / 'datasets/final/cluster_names.csv')
    print('\\nSaved cluster_names.csv (results + datasets/final):')
    print(names_df.to_string(index=False))
    """)

    upsert_cell(nb, "cluster_comparison_intro", "markdown", """
    ---
    ## 11. Comparable business view and DBSCAN map

    The earlier small multiples show the strongest features separately for each
    cluster, but separate axes make comparison unnecessarily hard. The heatmap
    below puts all five segments on one scale using six domain dimensions. Blue
    means “more of the named dimension” and orange means “less”; the colours do
    not mean approve or decline. A second view exposes the actual DBSCAN UMAP
    map so density noise can be inspected rather than reported as a single count.
    """)
    upsert_cell(nb, "cluster_comparison_code", "code", """
    import seaborn as sns

    business = pd.read_csv(PROJECT_ROOT / 'datasets/final/features_business.csv')
    business_labeled = business.merge(
        labels_df[['ROW_ID', 'CLUSTER_KMEANS']], on='ROW_ID', how='inner', validate='one_to_one')
    NAME_BY_CID = dict(zip(names_df['cluster_id'], names_df['nama']))
    business_labeled['Segment'] = business_labeled['CLUSTER_KMEANS'].map(NAME_BY_CID)

    dimension_features = {
        'Repayment burden': ['ANNUITY_TO_INCOME', 'CREDIT_TO_INCOME', 'BUREAU_DEBT_TO_CREDIT_RATIO'],
        'Observed delinquency': ['INST_DPD_MAX', 'INST_LATE_RATIO', 'INST_SEVERE_LATE_RATIO',
                                 'POS_SK_DPD_MEAN', 'CC_SK_DPD_MEAN'],
        'Revolving intensity': ['CC_UTILIZATION_MEAN', 'CC_UTILIZATION_MAX', 'CC_AMT_BALANCE_MEAN'],
        'Credit-history depth': ['BUREAU_COUNT', 'PREV_COUNT', 'POS_MONTHS_COUNT', 'CC_MONTHS_COUNT'],
        'External-score strength': ['EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3'],
        'Borrowing scale': ['AMT_CREDIT', 'AMT_ANNUITY'],
    }

    numeric = business_labeled.select_dtypes(include=np.number).copy()
    standardized = pd.DataFrame(index=numeric.index)
    for col in sorted({c for cols in dimension_features.values() for c in cols if c in numeric.columns}):
        values = numeric[col].replace([np.inf, -np.inf], np.nan)
        lo, hi = values.quantile([.01, .99])
        clipped = values.clip(lo, hi)
        std = clipped.std()
        standardized[col] = (clipped - clipped.mean()) / std if std and np.isfinite(std) else 0.0

    dimensions = pd.DataFrame(index=business_labeled.index)
    for dimension, columns in dimension_features.items():
        use = [c for c in columns if c in standardized.columns]
        dimensions[dimension] = standardized[use].mean(axis=1)
    dimensions['CLUSTER_KMEANS'] = business_labeled['CLUSTER_KMEANS'].values
    comparison = dimensions.groupby('CLUSTER_KMEANS').mean().T
    comparison.columns = [NAME_BY_CID[int(c)] for c in comparison.columns]
    comparison = comparison[names_df.sort_values('cluster_id')['nama'].tolist()]

    comparison_long = comparison.rename_axis('business_dimension').reset_index().melt(
        id_vars='business_dimension', var_name='Segment', value_name='portfolio_sd')
    comparison_long.to_csv(OUT_DIR / 'cluster_comparison_long.csv', index=False)

    business_summary = business_labeled.groupby(['CLUSTER_KMEANS', 'Segment']).agg(
        applicants=('SK_ID_CURR', 'size'),
        median_income=('AMT_INCOME_TOTAL', 'median'),
        median_credit=('AMT_CREDIT', 'median'),
        median_credit_to_income=('CREDIT_TO_INCOME', 'median'),
        median_annuity_to_income=('ANNUITY_TO_INCOME', 'median'),
        median_installment_late_share=('INST_LATE_RATIO', 'median'),
        median_external_score_2=('EXT_SOURCE_2', 'median'),
        median_card_utilisation=('CC_UTILIZATION_MEAN', 'median'),
    ).reset_index()
    business_summary.to_csv(OUT_DIR / 'cluster_business_summary.csv', index=False)
    names_df[['cluster_id', 'nama', 'profile_summary', 'watch_items', 'recommended_action']].to_csv(
        OUT_DIR / 'cluster_action_matrix.csv', index=False)

    fig, ax = plt.subplots(figsize=(12, 6.5))
    sns.heatmap(comparison, cmap='vlag', center=0, annot=True, fmt='+.2f',
                linewidths=.6, cbar_kws={'label': 'Portfolio standard deviations'}, ax=ax)
    ax.set_xlabel('Segment'); ax.set_ylabel('Business dimension')
    ax.set_title('All segments on one comparable business scale', fontweight='bold')
    plt.xticks(rotation=18, ha='right')
    plt.tight_layout()
    plt.savefig(OUT_DIR / 'plot_cluster_comparison.png', dpi=170, bbox_inches='tight')
    plt.show()

    dbscan_export = pd.DataFrame({
        'ROW_ID': dbscan_idx,
        'SK_ID_CURR': df.iloc[dbscan_idx]['SK_ID_CURR'].to_numpy(),
        'UMAP1': X_umap[:, 0],
        'UMAP2': X_umap[:, 1],
        'DBSCAN_LABEL': dbscan_labels,
        'IS_NOISE': (dbscan_labels == -1).astype(int),
        'CLUSTER_KMEANS': kmeans_labels[dbscan_idx],
    })
    dbscan_export['Segment'] = dbscan_export['CLUSTER_KMEANS'].map(NAME_BY_CID)
    dbscan_export.to_csv(OUT_DIR / 'dbscan_umap_sample.csv', index=False)

    fig, ax = plt.subplots(figsize=(11, 7))
    dense = dbscan_export[dbscan_export['IS_NOISE'] == 0]
    noise = dbscan_export[dbscan_export['IS_NOISE'] == 1]
    ax.scatter(dense['UMAP1'], dense['UMAP2'], s=5, alpha=.28, c='#4E6E8A',
               label=f'Density pockets ({len(dense):,})')
    ax.scatter(noise['UMAP1'], noise['UMAP2'], s=14, alpha=.85, c='#B4504A',
               edgecolors='white', linewidths=.15, label=f'Noise for review ({len(noise):,})')
    ax.set_xlabel('UMAP 1'); ax.set_ylabel('UMAP 2')
    ax.set_title('DBSCAN density map: isolated points are review signals, not defaults', fontweight='bold')
    ax.legend(markerscale=2)
    plt.tight_layout()
    plt.savefig(OUT_DIR / 'plot_dbscan_umap.png', dpi=170, bbox_inches='tight')
    plt.show()

    print(f'Saved comparable cluster view, business medians, action matrix, and {len(dbscan_export):,}-row DBSCAN map.')
    """)
    save(path, nb)


def update_phase3() -> None:
    path = ROOT / "notebooks/phase3_association.ipynb"
    nb = nbformat.read(path, as_version=4)

    for cell in nb.cells:
        if cell.cell_type == "markdown" and cell.source.startswith("# Phase 3:"):
            cell.source = _source("""
            # Phase 3: Association Rule Mining

            This phase mines readable co-occurrence patterns from
            `features_business.csv` and the Phase 2 segment labels. Continuous
            amounts and ratios become named analytical bins; absent repayment or
            score history remains explicitly unavailable rather than “clean.”
            Apriori, FP-Growth, and ECLAT enumerate the same compact global
            search space as an implementation check. Segment-context FP-Growth
            keeps a separate denominator and removes the constant cluster item.

            Final rules must have one consequent, at most two antecedents, a
            behavior/history signal, lift at least 1.2, confidence at least 0.35,
            and low redundancy. Rules made only from income, credit, leverage,
            and burden are rejected as algebraic identities. Algorithm agreement
            confirms enumeration consistency; it does not make a rule causal or
            operationally valid.
            """)
        elif cell.cell_type == "markdown" and "## 2. Discretization:" in cell.source:
            cell.source = _source("""
            ## 2. Business-readable transactions

            Quantiles are used for anonymized amount/score ranking where no
            currency policy threshold exists. Affordability, utilization, and
            delinquency use interpretable analytical cut points. `INST_COUNT`,
            card months, bureau count, and score missingness separate no observed
            history from clean or weak observed history. Age and gender are absent
            from the vocabulary. Each item is also mapped to a semantic family so
            deterministic financial identities can be audited and rejected.
            """)
        elif cell.cell_type == "markdown" and "## 7. Cross-algorithm" in cell.source:
            cell.source = _source("""
            ## 7. Algorithm and denominator validation

            Global Apriori, FP-Growth, and ECLAT must return the same normalized
            rules and numerically identical support, confidence, and lift. Only
            those global metrics are compared. Segment rules retain their own
            segment size and support count; their metrics are never averaged with
            full-portfolio metrics or counted as additional algorithms.
            """)
        elif cell.cell_type == "markdown" and "## 8. Filter rules:" in cell.source:
            cell.source = _source("""
            ## 8. Select non-trivial, compact segment findings

            The selection audit records why candidates are removed. A rule is
            rejected if it has a multi-item consequent, more than two antecedents,
            no behavior/history information, or only the algebraically linked
            income/credit/leverage/burden families. Remaining rules are ranked by
            lift, confidence, support, and exact global algorithm agreement, then
            de-duplicated within each segment using Jaccard overlap.
            """)

    replace_code(nb, "FEATURES_PATH =", """
    import os, time, pickle, random, ast
    from pathlib import Path
    from collections import defaultdict
    from itertools import combinations
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import networkx as nx
    from mlxtend.preprocessing import TransactionEncoder
    from mlxtend.frequent_patterns import apriori, fpgrowth, association_rules

    PROJECT_ROOT = Path.cwd().parent if Path.cwd().name == 'notebooks' else Path.cwd()
    OUT_DIR = PROJECT_ROOT / 'results/phase3_association'
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # Business-readable values are required here. Standardized mining values
    # are appropriate for Euclidean distance, but they are not income, credit,
    # utilisation, or repayment ratios and must never be binned as if they were.
    FEATURES_PATH = PROJECT_ROOT / 'datasets/final/features_business.csv'
    LABELS_PATH = PROJECT_ROOT / 'datasets/final/cluster_labels.csv'

    RANDOM_SEED = 42
    SAMPLE_SIZE = None
    MIN_SUPPORT = 0.03
    MIN_CONFIDENCE = 0.35
    MIN_LIFT = 1.2
    JACCARD_REDUNDANCY = 0.65

    print('Loading business-readable features ...')
    features = pd.read_csv(FEATURES_PATH)
    labels = pd.read_csv(LABELS_PATH)
    label_view = labels.drop(columns=[c for c in ['SK_ID_CURR'] if c in labels.columns])
    df_all = pd.merge(features, label_view, on='ROW_ID', how='inner', validate='one_to_one')
    assert len(df_all) == len(features), (
        f'cluster labels ({len(labels):,}) do not align with business features ({len(features):,})')
    print(f'  business features: {features.shape}')
    print(f'  labels           : {labels.shape}')
    print(f'  merged           : {df_all.shape}')

    cluster_names_df = pd.read_csv(PROJECT_ROOT / 'datasets/final/cluster_names.csv')
    print('\\nCluster naming (Phase 2 artefact):')
    print(cluster_names_df.to_string(index=False))
    """)

    replace_code(nb, "discretized = {}", """
    # Bins are named for what they mean. Higher external scores are labelled
    # stronger, not “higher risk”. Age and gender are excluded from action rules
    # so protected/life-stage traits do not become adverse-decision reasons.
    discretized = {}

    discretized['income'] = pd.qcut(
        df_all['AMT_INCOME_TOTAL'], q=4,
        labels=['income_q1', 'income_q2', 'income_q3', 'income_q4'], duplicates='drop')
    discretized['credit_size'] = pd.qcut(
        df_all['AMT_CREDIT'], q=3,
        labels=['credit_small', 'credit_medium', 'credit_large'], duplicates='drop')
    discretized['leverage'] = pd.cut(
        df_all['CREDIT_TO_INCOME'], bins=[-np.inf, 3, 6, np.inf],
        labels=['leverage_under_3x', 'leverage_3_to_6x', 'leverage_over_6x'])
    discretized['burden'] = pd.cut(
        df_all['ANNUITY_TO_INCOME'], bins=[-np.inf, .20, .35, np.inf],
        labels=['burden_under_20pct', 'burden_20_to_35pct', 'burden_over_35pct'])

    ext_mean = df_all[['EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3']].mean(axis=1)
    discretized['external_score'] = pd.qcut(
        ext_mean, q=3,
        labels=['external_score_weak', 'external_score_middle', 'external_score_strong'],
        duplicates='drop')

    any_late = df_all['INST_LATE_RATIO'].fillna(0) > 0
    serious_late = (df_all['INST_DPD_MAX'].fillna(0) > 30) | (df_all['INST_SEVERE_LATE_RATIO'].fillna(0) > 0)
    discretized['repayment_history'] = pd.Categorical(np.select(
        [serious_late, any_late],
        ['repayment_serious_late', 'repayment_some_late'],
        default='repayment_clean_observed'))

    util = df_all['CC_UTILIZATION_MEAN'].fillna(0)
    discretized['card_use'] = pd.Categorical(np.select(
        [util <= 0, util >= .80],
        ['card_no_observed_balance', 'card_utilisation_high'],
        default='card_utilisation_moderate'))

    bureau_count = df_all['BUREAU_COUNT'].fillna(0)
    discretized['credit_file'] = pd.Categorical(np.select(
        [df_all['FLAG_NO_BUREAU'].fillna(0).eq(1), bureau_count <= 2, bureau_count >= 8],
        ['credit_file_none', 'credit_file_thin', 'credit_file_deep'],
        default='credit_file_established'))

    cluster_map = {int(r.cluster_id): f'cluster_{int(r.cluster_id)}_{r.slug}'
                   for r in cluster_names_df.itertuples()}
    discretized['cluster'] = df_all['CLUSTER_KMEANS'].map(cluster_map)

    trans_df = pd.DataFrame(discretized)
    for c in trans_df.columns:
        trans_df[c] = trans_df[c].astype(str).replace({'nan': f'unknown_{c}', '<NA>': f'unknown_{c}'})

    print(f'Transactions table: {trans_df.shape}')
    print(f'Columns: {trans_df.columns.tolist()}')
    for c in trans_df.columns:
        print(f'\\n{c}:')
        print(trans_df[c].value_counts(normalize=True).round(3).to_string())
    """)

    replace_code_any(nb, ["# Heatmap: distribusi rules per cluster", "cluster_order = [cluster_map[cid]"], """
    # Dynamic segment order from Phase 2; never hard-code numeric labels because
    # K-Means cluster IDs can permute between runs.
    cluster_order = [cluster_map[cid] for cid in sorted(cluster_map)] + ['global']
    cluster_counts = top_rules['target_cluster'].value_counts().reindex(cluster_order, fill_value=0)
    display_names = {
        cluster_map[int(r.cluster_id)]: r.nama for r in cluster_names_df.itertuples()
    }
    display_names['global'] = 'Portfolio-wide'
    fig, ax = plt.subplots(figsize=(9, 4.8))
    colors_h = ['#34506B', '#5B8A72', '#B4504A', '#C2914C', '#8A6E9A', '#6B7280']
    bars = ax.barh(range(len(cluster_counts)), cluster_counts.values, color=colors_h[:len(cluster_counts)])
    ax.set_yticks(range(len(cluster_counts)))
    ax.set_yticklabels([display_names.get(x, x) for x in cluster_counts.index], fontsize=10)
    ax.invert_yaxis(); ax.set_xlabel('Final rules')
    ax.set_title('Final rules cover every named segment', fontweight='bold')
    for bar, val in zip(bars, cluster_counts.values):
        ax.text(val + .05, bar.get_y() + bar.get_height()/2, f'{val}', va='center')
    plt.tight_layout()
    plt.savefig(OUT_DIR / 'plot_cluster_heatmap.png', dpi=160, bbox_inches='tight')
    plt.show()
    """)

    upsert_cell(nb, "business_rule_visual_intro", "markdown", """
    ---
    ## 10. Business-readable rule view

    Support says how common a pattern is, confidence says how often its
    consequent follows, and lift says how much more often the combination occurs
    than chance. None of these metrics is causal. The final chart therefore pairs
    statistical strength with a bounded review action, and protected attributes
    are absent from the rule vocabulary.
    """)
    upsert_cell(nb, "business_rule_visual_code", "code", """
    def clean_item_text(text):
        return (str(text).replace('{', '').replace('}', '').replace("'", '')
                .replace('frozenset(', '').replace(')', '').replace('[', '').replace(']', ''))

    def readable_rule(rule):
        left, right = str(rule).split(' -> ', 1)
        return f'{clean_item_text(left)} → {clean_item_text(right)}'

    def rule_action(rule):
        text = str(rule)
        if 'repayment_serious_late' in text:
            return 'Review arrears recency, severity, and cure status'
        if 'burden_over_35pct' in text or 'leverage_over_6x' in text:
            return 'Verify income and run affordability stress review'
        if 'card_utilisation_high' in text:
            return 'Review balances, repayment capacity, and limit suitability'
        if 'credit_file_none' in text or 'credit_file_thin' in text:
            return 'Verify permitted alternative evidence; absence is uncertainty, not default'
        if 'external_score_weak' in text:
            return 'Inspect the underlying bureau reason; do not use the score alone'
        return 'Use for segment communication or standard review, not an individual decision'

    rule_view = top_rules.copy()
    rule_view['short_rule'] = rule_view['rule_str'].map(readable_rule)
    rule_view['Segment'] = rule_view['target_cluster'].map(display_names).fillna('Portfolio-wide')
    rule_view['review_action'] = rule_view['rule_str'].map(rule_action)
    rule_view[['rank', 'short_rule', 'Segment', 'support', 'confidence', 'lift',
               'n_algos', 'review_action']].to_csv(OUT_DIR / 'rule_visual_summary.csv', index=False)

    plot_rules = rule_view.sort_values('lift')
    fig, ax = plt.subplots(figsize=(12, 8))
    y = np.arange(len(plot_rules))
    points = ax.scatter(plot_rules['lift'], y,
                        s=80 + plot_rules['confidence'] * 260,
                        c=plot_rules['confidence'], cmap='viridis', vmin=0, vmax=1,
                        edgecolors='white', linewidth=.5)
    ax.hlines(y, 1, plot_rules['lift'], color='#9FB6C6', linewidth=1.2)
    ax.axvline(1, color='#6B7280', linestyle='--', linewidth=1)
    ax.set_yticks(y)
    ax.set_yticklabels([f'R{int(r)} · {s}' for r, s in zip(plot_rules['rank'], plot_rules['Segment'])])
    ax.set_xlabel('Lift (1 = chance)')
    ax.set_title('Final rules: lift, confidence, and segment coverage', fontweight='bold')
    cbar = plt.colorbar(points, ax=ax); cbar.set_label('Confidence')
    plt.tight_layout()
    plt.savefig(OUT_DIR / 'plot_rule_strength.png', dpi=170, bbox_inches='tight')
    plt.show()

    segment_metrics = rule_view.groupby('Segment').agg(
        rules=('rank', 'count'), mean_support=('support', 'mean'),
        mean_confidence=('confidence', 'mean'), mean_lift=('lift', 'mean')).reset_index()
    segment_metrics.to_csv(OUT_DIR / 'rule_segment_summary.csv', index=False)
    print(f'Saved {len(rule_view)} business-readable final rules and segment summary.')
    """)

    # Final Phase 3 correction: mine compact, context-correct rules and reject
    # algebraic tautologies such as income + credit mechanically implying the
    # derived credit-to-income bin.  These replacements intentionally run after
    # the legacy update calls above so repeated execution stays idempotent.
    replace_code(nb, "FEATURES_PATH =", """
    import time, pickle, random
    from pathlib import Path
    from collections import defaultdict
    from itertools import combinations
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import networkx as nx
    from mlxtend.preprocessing import TransactionEncoder
    from mlxtend.frequent_patterns import apriori, fpgrowth, association_rules

    PROJECT_ROOT = Path.cwd().parent if Path.cwd().name == 'notebooks' else Path.cwd()
    OUT_DIR = PROJECT_ROOT / 'results/phase3_association'
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    FEATURES_PATH = PROJECT_ROOT / 'datasets/final/features_business.csv'
    LABELS_PATH = PROJECT_ROOT / 'datasets/final/cluster_labels.csv'

    RANDOM_SEED = 42
    SAMPLE_SIZE = None
    MIN_SUPPORT = 0.03
    MIN_CONFIDENCE = 0.35
    MIN_LIFT = 1.20
    MAX_LEN = 3                 # one or two antecedents + one consequent
    JACCARD_REDUNDANCY = 0.65

    def canonical_rule(antecedents, consequents):
        left = ', '.join(sorted(map(str, antecedents)))
        right = ', '.join(sorted(map(str, consequents)))
        return f'{{{left}}} -> {{{right}}}'

    print('Loading business-readable features ...')
    features = pd.read_csv(FEATURES_PATH)
    labels = pd.read_csv(LABELS_PATH)
    label_view = labels.drop(columns=[c for c in ['SK_ID_CURR'] if c in labels.columns])
    df_all = pd.merge(features, label_view, on='ROW_ID', how='inner', validate='one_to_one')
    assert len(df_all) == len(features)
    cluster_names_df = pd.read_csv(PROJECT_ROOT / 'datasets/final/cluster_names.csv')
    print(f'  business features: {features.shape}; merged: {df_all.shape}')
    """)

    replace_code(nb, "discretized = {}", """
    # Every item belongs to one semantic family.  History absence is kept
    # separate from clean observed repayment, and unavailable external scores
    # remain unavailable rather than inheriting an imputed score label.
    discretized = {}
    discretized['income'] = pd.qcut(
        df_all['AMT_INCOME_TOTAL'], 4,
        labels=['income_q1', 'income_q2', 'income_q3', 'income_q4'], duplicates='drop')
    discretized['credit_size'] = pd.qcut(
        df_all['AMT_CREDIT'], 3,
        labels=['credit_small', 'credit_medium', 'credit_large'], duplicates='drop')
    discretized['leverage'] = pd.cut(
        df_all['CREDIT_TO_INCOME'], [-np.inf, 3, 6, np.inf],
        labels=['leverage_under_3x', 'leverage_3_to_6x', 'leverage_over_6x'])
    discretized['burden'] = pd.cut(
        df_all['ANNUITY_TO_INCOME'], [-np.inf, .20, .35, np.inf],
        labels=['burden_under_20pct', 'burden_20_to_35pct', 'burden_over_35pct'])

    observed_scores = pd.DataFrame(index=df_all.index)
    for col in ['EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3']:
        source_col = f'SOURCE_{col}' if f'SOURCE_{col}' in df_all.columns else col
        values = df_all[source_col].copy()
        flag_col = f'FLAG_{col}_MISSING'
        if flag_col in df_all.columns:
            values = values.mask(df_all[flag_col].eq(1))
        observed_scores[col] = values
    ext_mean = observed_scores.mean(axis=1, skipna=True)
    external_score = pd.Series('external_score_unavailable', index=df_all.index, dtype=object)
    valid_ext = ext_mean.notna()
    external_score.loc[valid_ext] = pd.qcut(
        ext_mean.loc[valid_ext], 3,
        labels=['external_score_weak', 'external_score_middle', 'external_score_strong'],
        duplicates='drop').astype(str)
    discretized['external_score'] = external_score

    inst_count = df_all['INST_COUNT'].fillna(0)
    serious_late = (df_all['INST_DPD_MAX'].fillna(0) > 30) | (df_all['INST_SEVERE_LATE_RATIO'].fillna(0) > 0)
    any_late = df_all['INST_LATE_RATIO'].fillna(0) > 0
    discretized['repayment_history'] = pd.Categorical(np.select(
        [inst_count.le(0), serious_late, any_late],
        ['repayment_not_observed', 'repayment_serious_late', 'repayment_some_late'],
        default='repayment_clean_observed'))

    card_months = df_all['CC_MONTHS_COUNT'].fillna(0)
    util = df_all['CC_UTILIZATION_MEAN'].fillna(0)
    discretized['card_use'] = pd.Categorical(np.select(
        [card_months.le(0), util.ge(.80)],
        ['card_history_not_observed', 'card_utilisation_high'],
        default='card_utilisation_moderate'))

    bureau_count = df_all['BUREAU_COUNT'].fillna(0)
    discretized['credit_file'] = pd.Categorical(np.select(
        [bureau_count.le(0), bureau_count.le(2), bureau_count.ge(8)],
        ['credit_file_none', 'credit_file_thin', 'credit_file_deep'],
        default='credit_file_established'))
    bureau_debt = df_all['BUREAU_DEBT_TO_CREDIT_RATIO'].fillna(0)
    discretized['bureau_debt'] = pd.Categorical(np.select(
        [bureau_count.le(0), bureau_debt.ge(.80), bureau_debt.ge(.30)],
        ['bureau_debt_not_observed', 'bureau_debt_high', 'bureau_debt_moderate'],
        default='bureau_debt_low'))

    prev_count = df_all['PREV_COUNT'].fillna(0)
    approval = df_all['PREV_APPROVAL_RATE'].fillna(0)
    refused = df_all['PREV_REFUSED_COUNT'].fillna(0)
    discretized['previous_depth'] = pd.Categorical(np.select(
        [prev_count.le(0), prev_count.eq(1), prev_count.ge(5)],
        ['previous_none', 'previous_one', 'previous_deep'], default='previous_two_to_four'))
    discretized['previous_outcome'] = pd.Categorical(np.select(
        [prev_count.le(0), refused.ge(3), approval.ge(.75)],
        ['previous_outcome_not_observed', 'previous_refusals_repeated', 'previous_approval_high'],
        default='previous_outcome_mixed'))

    cluster_map = {int(r.cluster_id): f'cluster_{int(r.cluster_id)}_{r.slug}'
                   for r in cluster_names_df.itertuples()}
    discretized['cluster'] = df_all['CLUSTER_KMEANS'].map(cluster_map)

    trans_df = pd.DataFrame(discretized)
    for col in trans_df.columns:
        trans_df[col] = trans_df[col].astype(str).replace({'nan': f'unknown_{col}', '<NA>': f'unknown_{col}'})
    ITEM_FAMILY = {
        item: family for family in trans_df.columns for item in trans_df[family].unique()
    }
    print(f'Transactions: {trans_df.shape}; semantic families: {list(trans_df.columns)}')
    """)

    replace_code(nb, "rng = random.Random(RANDOM_SEED)", """
    rng = random.Random(RANDOM_SEED)
    trans_sample = trans_df if SAMPLE_SIZE is None else trans_df.sample(
        n=min(SAMPLE_SIZE, len(trans_df)), random_state=RANDOM_SEED)
    transactions_list = trans_sample.values.astype(str).tolist()
    with open(OUT_DIR / 'transactions_list.pkl', 'wb') as f:
        pickle.dump(transactions_list, f)
    te = TransactionEncoder()
    df_ohe = pd.DataFrame(te.fit(transactions_list).transform(transactions_list), columns=te.columns_)
    df_ohe.to_pickle(OUT_DIR / 'transactions_ohe.pkl')
    print(f'Encoded {len(transactions_list):,} transactions × {df_ohe.shape[1]} items')
    """)

    replace_code(nb, "print('Running Apriori ...')", """
    print('Running Apriori ...')
    t0 = time.time()
    freq_apriori = apriori(
        df_ohe, min_support=MIN_SUPPORT, use_colnames=True,
        max_len=MAX_LEN, low_memory=True)
    rules_apriori = association_rules(freq_apriori, metric='lift', min_threshold=MIN_LIFT)
    rules_apriori = rules_apriori[
        (rules_apriori['confidence'] >= MIN_CONFIDENCE) &
        (rules_apriori['consequents'].map(len) == 1)
    ].copy()
    rules_apriori['algorithm'] = 'apriori'
    rules_apriori['context'] = 'Portfolio-wide'
    rules_apriori['context_n'] = len(trans_sample)
    rules_apriori['support_count'] = (rules_apriori['support'] * len(trans_sample)).round().astype(int)
    rules_apriori['rule_str'] = rules_apriori.apply(
        lambda r: canonical_rule(r['antecedents'], r['consequents']), axis=1)
    rules_apriori['normalized_rule'] = rules_apriori['rule_str']
    rules_apriori.to_csv(OUT_DIR / 'rules_apriori.csv', index=False)
    print(f'  {len(freq_apriori):,} itemsets; {len(rules_apriori):,} compact rules in {time.time()-t0:.1f}s')
    """)

    replace_code(nb, "print('Running FP-Growth ...')", """
    print('Running FP-Growth ...')
    t0 = time.time()
    freq_fp = fpgrowth(df_ohe, min_support=MIN_SUPPORT, use_colnames=True, max_len=MAX_LEN)
    rules_fp = association_rules(freq_fp, metric='lift', min_threshold=MIN_LIFT)
    rules_fp = rules_fp[
        (rules_fp['confidence'] >= MIN_CONFIDENCE) &
        (rules_fp['consequents'].map(len) == 1)
    ].copy()
    rules_fp['algorithm'] = 'fpgrowth'
    rules_fp['context'] = 'Portfolio-wide'; rules_fp['context_n'] = len(trans_sample)
    rules_fp['support_count'] = (rules_fp['support'] * len(trans_sample)).round().astype(int)
    rules_fp['rule_str'] = rules_fp.apply(lambda r: canonical_rule(r['antecedents'], r['consequents']), axis=1)
    rules_fp['normalized_rule'] = rules_fp['rule_str']
    rules_fp.to_csv(OUT_DIR / 'rules_fpgrowth.csv', index=False)
    print(f'  {len(freq_fp):,} itemsets; {len(rules_fp):,} compact rules in {time.time()-t0:.1f}s')
    """)

    replace_code(nb, "def build_tidsets(transactions):", """
    def build_tidsets(transactions):
        tidsets = defaultdict(set)
        for tid, transaction in enumerate(transactions):
            for item in transaction:
                tidsets[item].add(tid)
        return tidsets

    def eclat_recursive(tidsets, min_count, prefix=(), prefix_tids=None, max_len=3):
        frequent = []
        items = sorted(tidsets)
        for i, item in enumerate(items):
            tids = tidsets[item] if prefix_tids is None else prefix_tids & tidsets[item]
            if len(tids) < min_count:
                continue
            itemset = tuple(sorted(prefix + (item,)))
            frequent.append((itemset, len(tids)))
            if len(itemset) < max_len:
                suffix = {it: tidsets[it] for it in items[i+1:]}
                frequent.extend(eclat_recursive(suffix, min_count, itemset, tids, max_len))
        return frequent

    print('Running ECLAT ...')
    t0 = time.time()
    tidsets = build_tidsets(transactions_list)
    min_count = int(np.ceil(MIN_SUPPORT * len(transactions_list)))
    freq_dict = {items: count / len(transactions_list)
                 for items, count in eclat_recursive(tidsets, min_count, max_len=MAX_LEN)}
    eclat_rows = []
    for itemset, support in freq_dict.items():
        if len(itemset) < 2:
            continue
        for consequent in itemset:
            ant = tuple(sorted(set(itemset) - {consequent}))
            con = (consequent,)
            if ant not in freq_dict or con not in freq_dict:
                continue
            confidence = support / freq_dict[ant]
            lift = confidence / freq_dict[con]
            if confidence >= MIN_CONFIDENCE and lift >= MIN_LIFT:
                eclat_rows.append({
                    'antecedents': frozenset(ant), 'consequents': frozenset(con),
                    'support': support, 'confidence': confidence, 'lift': lift,
                    'algorithm': 'eclat', 'context': 'Portfolio-wide',
                    'context_n': len(trans_sample),
                    'support_count': int(round(support * len(trans_sample))),
                    'rule_str': canonical_rule(ant, con),
                    'normalized_rule': canonical_rule(ant, con),
                })
    rules_eclat = pd.DataFrame(eclat_rows)
    rules_eclat.to_csv(OUT_DIR / 'rules_eclat.csv', index=False)
    print(f'  {len(freq_dict):,} itemsets; {len(rules_eclat):,} compact rules in {time.time()-t0:.1f}s')
    """)

    replace_code(nb, "per_cluster_rows = []", """
    # Segment-context metrics retain their own denominators.  The constant
    # cluster item is removed before mining so it cannot manufacture lift.
    per_cluster_rows = []
    feature_transactions = trans_sample.drop(columns='cluster')
    for cluster_name in trans_sample['cluster'].unique():
        mask = trans_sample['cluster'].eq(cluster_name).to_numpy()
        segment_frame = feature_transactions.loc[mask]
        context_n = len(segment_frame)
        te_sub = TransactionEncoder()
        segment_list = segment_frame.values.astype(str).tolist()
        encoded = pd.DataFrame(te_sub.fit(segment_list).transform(segment_list), columns=te_sub.columns_)
        freq_sub = fpgrowth(encoded, min_support=0.03, use_colnames=True, max_len=MAX_LEN)
        r_sub = association_rules(freq_sub, metric='lift', min_threshold=MIN_LIFT)
        r_sub = r_sub[
            (r_sub['confidence'] >= MIN_CONFIDENCE) &
            (r_sub['consequents'].map(len) == 1)
        ].copy()
        r_sub['algorithm'] = 'fpgrowth_segment'
        r_sub['context'] = cluster_name; r_sub['context_n'] = context_n
        r_sub['support_count'] = (r_sub['support'] * context_n).round().astype(int)
        r_sub['rule_str'] = r_sub.apply(lambda r: canonical_rule(r['antecedents'], r['consequents']), axis=1)
        r_sub['normalized_rule'] = r_sub['rule_str']
        per_cluster_rows.append(r_sub)
        print(f'  {cluster_name}: {context_n:,} rows, {len(r_sub):,} context-specific rules')
    rules_per_cluster = pd.concat(per_cluster_rows, ignore_index=True)
    rules_per_cluster.to_csv(OUT_DIR / 'rules_per_cluster.csv', index=False)
    """)

    replace_code_any(nb, ["def normalize_rule(rule_str):", "# Compare the three global algorithms only."], """
    # Compare the three global algorithms only.  Segment FP-Growth is a
    # different population, not a fourth independent confirmation.
    global_all = pd.concat([rules_apriori, rules_fp, rules_eclat], ignore_index=True)
    algo_df = pd.DataFrame([
        {'Algoritma': 'apriori', 'Sample': f'{len(trans_sample):,}', 'Rules': len(rules_apriori)},
        {'Algoritma': 'fpgrowth', 'Sample': f'{len(trans_sample):,}', 'Rules': len(rules_fp)},
        {'Algoritma': 'eclat', 'Sample': f'{len(trans_sample):,}', 'Rules': len(rules_eclat)},
        {'Algoritma': 'fpgrowth_per_cluster', 'Sample': 'segment denominators', 'Rules': len(rules_per_cluster)},
    ])
    algo_df.to_csv(OUT_DIR / 'algo_comparison.csv', index=False)

    rule_groups = global_all.groupby('normalized_rule', as_index=False).agg(
        support=('support', 'mean'), confidence=('confidence', 'mean'), lift=('lift', 'mean'),
        support_min=('support', 'min'), support_max=('support', 'max'),
        confidence_min=('confidence', 'min'), confidence_max=('confidence', 'max'),
        lift_min=('lift', 'min'), lift_max=('lift', 'max'),
        algorithm=('algorithm', lambda x: sorted(set(x))),
        rule_str=('rule_str', 'first'), context_n=('context_n', 'first'),
        support_count=('support_count', 'first'),
    )
    rule_groups['appears_in'] = rule_groups['algorithm'].map(lambda x: '+'.join(x))
    rule_groups['n_algos'] = rule_groups['algorithm'].map(len)
    rule_groups['metric_spread'] = rule_groups[
        ['support_max','support_min','confidence_max','confidence_min','lift_max','lift_min']
    ].apply(lambda r: max(r.support_max-r.support_min,
                          r.confidence_max-r.confidence_min,
                          r.lift_max-r.lift_min), axis=1)
    rule_groups['is_consistent'] = (rule_groups['n_algos'] == 3) & (rule_groups['metric_spread'] < 1e-10)
    rule_groups['context'] = 'Portfolio-wide'
    rule_groups.to_csv(OUT_DIR / 'rules_combined.csv', index=False)
    print(algo_df.to_string(index=False))
    print(f'Exact three-algorithm global rules: {rule_groups.is_consistent.sum():,}')
    """)

    replace_code(nb, "def jaccard(rule1, rule2):", """
    def rule_items(rule):
        left, right = str(rule).split(' -> ', 1)
        clean = lambda text: {x.strip() for x in text.strip('{}').split(',') if x.strip()}
        return clean(left), clean(right)

    def jaccard(rule1, rule2):
        a = set().union(*rule_items(rule1)); b = set().union(*rule_items(rule2))
        return len(a & b) / max(len(a | b), 1)

    def redundant_with(rule, selected_rows):
        antecedents, _ = rule_items(rule)
        for selected_row in selected_rows:
            other_rule = selected_row['rule_str']
            other_antecedents, _ = rule_items(other_rule)
            if antecedents == other_antecedents:
                return True
            if jaccard(rule, other_rule) > JACCARD_REDUNDANCY:
                return True
        return False

    history_families = {
        'repayment_history', 'card_use', 'credit_file', 'bureau_debt',
        'previous_depth', 'previous_outcome', 'external_score',
    }
    algebraic_families = {'income', 'credit_size', 'leverage', 'burden'}
    deterministic_item_groups = [
        {'previous_none', 'previous_outcome_not_observed'},
        {'credit_file_none', 'bureau_debt_not_observed'},
    ]

    def nontrivial_reason(rule):
        antecedents, consequents = rule_items(rule)
        if len(consequents) != 1 or len(antecedents) > 2:
            return 'not_compact_single_consequent'
        families = {ITEM_FAMILY.get(item, 'unknown') for item in antecedents | consequents}
        items = antecedents | consequents
        if any(group.issubset(items) for group in deterministic_item_groups):
            return 'same_source_missingness_identity'
        if len(families) == 1:
            return 'same_family_restatement'
        if families.issubset(algebraic_families):
            return 'algebraic_financial_identity'
        if not (families & history_families):
            return 'no_behavior_or_history_signal'
        return 'accepted_nontrivial'

    global_candidates = rule_groups.copy()
    global_candidates['target_cluster'] = global_candidates['rule_str'].map(
        lambda rule: next((item for item in rule_items(rule)[0] | rule_items(rule)[1]
                           if str(item).startswith('cluster_')), 'global'))
    segment_candidates = rules_per_cluster.copy()
    segment_candidates['n_algos'] = 1
    segment_candidates['appears_in'] = 'fpgrowth_segment'
    segment_candidates['is_consistent'] = False
    segment_candidates['target_cluster'] = segment_candidates['context']
    candidate_pool = pd.concat([global_candidates, segment_candidates], ignore_index=True, sort=False)
    candidate_pool['selection_reason'] = candidate_pool['rule_str'].map(nontrivial_reason)
    candidate_pool['selection_reason'].value_counts().rename_axis('reason').reset_index(name='rules').to_csv(
        OUT_DIR / 'rule_rejection_audit.csv', index=False)
    eligible = candidate_pool[candidate_pool['selection_reason'].eq('accepted_nontrivial')].copy()
    eligible['consistency_bonus'] = eligible['is_consistent'].fillna(False).astype(float) * .15
    eligible['final_score'] = (
        eligible['lift'] * eligible['confidence'] * np.sqrt(eligible['support']) +
        eligible['consistency_bonus'])

    CLUSTER_SLUGS = [cluster_map[cid] for cid in sorted(cluster_map)]
    selected = []
    for cluster_name in CLUSTER_SLUGS:
        chosen_here = []
        sub = eligible[eligible['target_cluster'].eq(cluster_name)].sort_values('final_score', ascending=False)
        for _, row in sub.iterrows():
            if len(chosen_here) >= 3:
                break
            if not redundant_with(row['rule_str'], chosen_here):
                chosen_here.append(row.to_dict())
        if len(chosen_here) < 3:
            raise ValueError(f'Only {len(chosen_here)} non-trivial rules available for {cluster_name}')
        selected.extend(chosen_here)

    top_rules = pd.DataFrame(selected).reset_index(drop=True)
    top_rules['rank'] = np.arange(1, len(top_rules) + 1)
    top_rules['metric_scope'] = np.where(
        top_rules['context'].eq('Portfolio-wide'),
        'Full portfolio; Apriori/FP-Growth/ECLAT exact agreement',
        'Within-segment FP-Growth; metrics use the segment denominator')
    top_rules.to_csv(OUT_DIR / 'rule_table_final.csv', index=False)
    print(top_rules[['rank','target_cluster','rule_str','support_count','support','confidence','lift','metric_scope']].to_string(index=False))
    """)

    upsert_cell(nb, "business_rule_visual_code", "code", """
    def clean_item_text(text):
        return str(text).replace('{', '').replace('}', '').strip()

    def readable_rule(rule):
        left, right = str(rule).split(' -> ', 1)
        return f'{clean_item_text(left)} → {clean_item_text(right)}'

    def rule_action(rule):
        text = str(rule)
        if 'repayment_serious_late' in text or 'repayment_some_late' in text:
            return 'Review arrears recency, severity, and cure status'
        if 'burden_over_35pct' in text or 'leverage_over_6x' in text:
            return 'Verify income and run an affordability stress review'
        if 'card_utilisation_high' in text:
            return 'Review balances, payment capacity, and limit suitability'
        if any(token in text for token in [
            'credit_file_none', 'repayment_not_observed', 'card_history_not_observed',
            'previous_none', 'previous_outcome_not_observed', 'external_score_unavailable']):
            return 'Treat absence as uncertainty; verify permitted alternative evidence'
        if 'bureau_debt_high' in text or 'previous_refusals_repeated' in text:
            return 'Reconcile current obligations and whether historical concerns remain current'
        return 'Use for segment communication or standard review, not an individual decision'

    display_names = {cluster_map[int(r.cluster_id)]: r.nama for r in cluster_names_df.itertuples()}
    display_names['global'] = 'Portfolio-wide'
    rule_view = top_rules.copy()
    rule_view['short_rule'] = rule_view['rule_str'].map(readable_rule)
    rule_view['Segment'] = rule_view['target_cluster'].map(display_names).fillna('Portfolio-wide')
    rule_view['Context'] = rule_view['context'].map(display_names).fillna(rule_view['context'])
    rule_view['review_action'] = rule_view['rule_str'].map(rule_action)
    export_cols = [
        'rank', 'short_rule', 'Segment', 'Context', 'support_count', 'support',
        'confidence', 'lift', 'n_algos', 'metric_scope', 'review_action']
    rule_view[export_cols].to_csv(OUT_DIR / 'rule_visual_summary.csv', index=False)

    plot_rules = rule_view.sort_values('lift')
    fig, ax = plt.subplots(figsize=(12, 8))
    y = np.arange(len(plot_rules))
    points = ax.scatter(plot_rules['lift'], y,
                        s=70 + plot_rules['confidence'] * 250,
                        c=plot_rules['confidence'], cmap='viridis', vmin=0, vmax=1,
                        edgecolors='white', linewidth=.5)
    ax.hlines(y, 1, plot_rules['lift'], color='#9FB6C6', linewidth=1.2)
    ax.axvline(1, color='#6B7280', linestyle='--', linewidth=1)
    ax.set_yticks(y)
    ax.set_yticklabels([f'R{int(r)} · {s}' for r, s in zip(plot_rules['rank'], plot_rules['Segment'])])
    ax.set_xlabel('Lift (1 = chance)')
    ax.set_title('Non-trivial rules: strength, confidence, and segment context', fontweight='bold')
    plt.colorbar(points, ax=ax, label='Confidence')
    plt.tight_layout(); plt.savefig(OUT_DIR / 'plot_rule_strength.png', dpi=170, bbox_inches='tight'); plt.show()

    segment_metrics = rule_view.groupby('Segment').agg(
        rules=('rank', 'count'), support_records=('support_count', 'sum'),
        mean_support=('support', 'mean'), mean_confidence=('confidence', 'mean'),
        mean_lift=('lift', 'mean')).reset_index()
    segment_metrics.to_csv(OUT_DIR / 'rule_segment_summary.csv', index=False)
    print(f'Saved {len(rule_view)} non-trivial, denominator-labelled rules.')
    """)
    save(path, nb)


def update_phase4() -> None:
    path = ROOT / "notebooks/phase4_anomaly.ipynb"
    nb = nbformat.read(path, as_version=4)

    replace_code(nb, "merged_a = pd.merge(stats_df", """
    merged_a = pd.merge(stats_df, iso_df[['ROW_ID','is_isolation_outlier','isolation_score']], on='ROW_ID', how='inner')
    merged_a = pd.merge(merged_a, mahal_df[['ROW_ID','is_mahalanobis_outlier','mahalanobis_d2']], on='ROW_ID', how='inner')
    merged_a = pd.merge(merged_a, lof_df[['ROW_ID','is_lof_outlier','lof_score']], on='ROW_ID', how='inner')
    merged_a = pd.merge(
        merged_a, labels[['ROW_ID','CLUSTER_KMEANS','CLUSTER_DBSCAN','IS_OUTLIER']],
        on='ROW_ID', how='inner')

    detector_flag_cols = [
        'is_iqr_outlier', 'is_zscore_outlier', 'is_mahalanobis_outlier',
        'is_isolation_outlier', 'is_lof_outlier', 'IS_OUTLIER']
    merged_a['detection_count'] = sum(
        merged_a[col].fillna(0).astype(int) for col in detector_flag_cols)
    merged_a['available_detector_count'] = 5 + merged_a['CLUSTER_DBSCAN'].notna().astype(int)
    merged_a['agreement_share'] = merged_a['detection_count'] / merged_a['available_detector_count']

    def categorize(r):
        if r['detection_count'] >= 3 and r['agreement_share'] >= .50:
            return 'HIGH_CONFIDENCE_ANOMALY'  # internal name: 3+ detector consensus
        if r['detection_count'] == 2: return 'MODERATE_ANOMALY'
        if r['detection_count'] == 1: return 'WEAK_SIGNAL'
        return 'NORMAL'
    merged_a['anomaly_category'] = merged_a.apply(categorize, axis=1)
    merged_a['phase2_corroborated'] = (
        merged_a['anomaly_category'].eq('HIGH_CONFIDENCE_ANOMALY') &
        merged_a['IS_OUTLIER'].eq(1))
    merged_a.to_csv(OUT_DIR / 'anomaly_combined.csv', index=False)

    cat_dist = merged_a['anomaly_category'].value_counts()
    high_conf = merged_a[merged_a['anomaly_category'].eq('HIGH_CONFIDENCE_ANOMALY')]
    cluster_dist = high_conf['CLUSTER_KMEANS'].value_counts().sort_index()
    corroborated = int(merged_a['phase2_corroborated'].sum())
    summary_df = pd.DataFrame({
        'Total_Evaluated': [len(merged_a)],
        'HIGH_CONFIDENCE': [int(cat_dist.get('HIGH_CONFIDENCE_ANOMALY', 0))],
        'Phase2_Corroborated_DBSCAN': [corroborated],
        'MODERATE': [int(cat_dist.get('MODERATE_ANOMALY', 0))],
        'WEAK': [int(cat_dist.get('WEAK_SIGNAL', 0))],
        'NORMAL': [int(cat_dist.get('NORMAL', 0))],
        'N_IQR': [int(merged_a['is_iqr_outlier'].sum())],
        'N_ZSCORE': [int(merged_a['is_zscore_outlier'].sum())],
        'N_MAHALANOBIS': [int(merged_a['is_mahalanobis_outlier'].sum())],
        'N_ISOFOREST': [int(merged_a['is_isolation_outlier'].sum())],
        'N_LOF': [int(merged_a['is_lof_outlier'].sum())],
        'N_DBSCAN': [int(merged_a['IS_OUTLIER'].fillna(0).sum())],
    })
    summary_df.to_csv(OUT_DIR / 'anomaly_summary.csv', index=False)
    print(f'DBSCAN coverage: {merged_a.CLUSTER_DBSCAN.notna().sum():,} rows have six available detectors; '
          f'the rest have five. DBSCAN corroborates {corroborated:,} consensus records.')
    print(cat_dist.to_string())
    """)

    for cell in nb.cells:
        if cell.cell_type == 'markdown' and '## 7. Investigating and labelling the anomalies' in cell.source:
            cell.source = _source("""
            ## 7. Record-level business investigation

            Detector agreement identifies statistically unusual records; it does
            not say why they matter. Every 3+ detector-consensus record is joined
            to readable model values and preserved source values, then tested in
            this order:

            1. **Data consistency:** impossible or internally inconsistent values
               are reconciled before underwriting.
            2. **Affordability and repayment evidence:** burden, leverage,
               delinquency, utilisation, and bureau history trigger a specific
               human review with the applicant's actual values.
            3. **Rare but plausible:** if neither condition is present, rarity is
               documented but is not converted into a risk conclusion.

            Missing or thin history is uncertainty rather than bad behaviour, and
            no anomaly row is authorised for an automatic credit decision.
            """)
            break

    replace_code_any(nb, ["data_with = pd.read_csv", "build_anomaly_investigation("], """
    import sys
    sys.path.insert(0, str(PROJECT_ROOT))
    from src.domain_credit import build_anomaly_investigation

    business_values = pd.read_csv(PROJECT_ROOT / 'datasets/final/features_business.csv')
    investigations, driver_summary = build_anomaly_investigation(
        business=business_values,
        combined=merged_a,
        labels=labels,
        cluster_names=cluster_names_df,
    )
    investigations.to_csv(OUT_DIR / 'anomaly_investigation.csv', index=False)
    driver_summary.to_csv(OUT_DIR / 'anomaly_driver_summary.csv', index=False)

    print(f'Investigated 3+ detector-consensus records: {len(investigations):,}')
    print('\\nReview type distribution:')
    print(investigations['Review Type'].value_counts().to_string())
    print('\\nPriority distribution:')
    print(investigations['Priority'].value_counts().to_string())
    print('\\nEvery row contains applicant-specific evidence and a human-review action.')
    print('Automatic Decision Allowed:', investigations['Automatic Decision Allowed'].unique().tolist())
    """)

    upsert_cell(nb, "anomaly_business_visuals_intro", "markdown", """
    ---
    ## 9. Business drivers and detector agreement

    Counts alone do not explain operational workload. The first view shows what
    actually drives review; the second shows whether methods agree on the same
    records. Jaccard overlap is used because detector flag rates differ. High
    agreement raises confidence in unusualness, but still does not prove default.
    """)
    upsert_cell(nb, "anomaly_business_visuals_code", "code", """
    import seaborn as sns

    top_drivers = driver_summary.head(14).sort_values('records')
    fig, ax = plt.subplots(figsize=(11, 7))
    colors = top_drivers['Review Type'].map({
        'Data consistency check': '#C2914C',
        'Affordability / repayment review': '#B4504A',
        'Rare but plausible profile': '#4E6E8A',
    }).fillna('#6B7280')
    bars = ax.barh(top_drivers['Driver'], top_drivers['records'], color=colors)
    for bar, value in zip(bars, top_drivers['records']):
        ax.text(value + max(top_drivers['records']) * .01,
                bar.get_y() + bar.get_height()/2, f'{value:,}', va='center')
    ax.set_xlabel('High-confidence anomaly records')
    ax.set_title('Why records are routed for review', fontweight='bold')
    plt.tight_layout()
    plt.savefig(OUT_DIR / 'plot_anomaly_business_drivers.png', dpi=170, bbox_inches='tight')
    plt.show()

    review_by_segment = pd.crosstab(investigations['Segment'], investigations['Review Type'])
    review_by_segment.to_csv(OUT_DIR / 'anomaly_review_by_segment.csv')
    fig, ax = plt.subplots(figsize=(11, 5.5))
    order = ['Rare but plausible profile', 'Affordability / repayment review', 'Data consistency check']
    use = [c for c in order if c in review_by_segment.columns]
    review_by_segment[use].plot(kind='barh', stacked=True, ax=ax,
        color=['#4E6E8A', '#B4504A', '#C2914C'][:len(use)])
    ax.set_xlabel('High-confidence records'); ax.set_ylabel('Segment')
    ax.set_title('Review workload by segment and business meaning', fontweight='bold')
    ax.legend(title='Review type', bbox_to_anchor=(1.02, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(OUT_DIR / 'plot_anomaly_review_by_segment.png', dpi=170, bbox_inches='tight')
    plt.show()

    detector_cols = list({
        'Adjusted IQR': 'is_iqr_outlier',
        'Z-score': 'is_zscore_outlier',
        'Mahalanobis': 'is_mahalanobis_outlier',
        'Isolation Forest': 'is_isolation_outlier',
        'LOF': 'is_lof_outlier',
        'DBSCAN': 'IS_OUTLIER',
    }.items())
    overlap = pd.DataFrame(index=[x[0] for x in detector_cols], columns=[x[0] for x in detector_cols], dtype=float)
    for name_a, col_a in detector_cols:
        a = merged_a[col_a].fillna(0).astype(bool)
        for name_b, col_b in detector_cols:
            b = merged_a[col_b].fillna(0).astype(bool)
            union = (a | b).sum()
            overlap.loc[name_a, name_b] = (a & b).sum() / union if union else 0
    overlap.to_csv(OUT_DIR / 'detector_jaccard_overlap.csv')
    fig, ax = plt.subplots(figsize=(8, 6.5))
    sns.heatmap(overlap.astype(float), annot=True, fmt='.2f', cmap='Blues', vmin=0, vmax=1,
                square=True, cbar_kws={'label': 'Jaccard overlap'}, ax=ax)
    ax.set_title('Which detectors flag the same records?', fontweight='bold')
    plt.xticks(rotation=30, ha='right'); plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig(OUT_DIR / 'plot_detector_agreement_heatmap.png', dpi=170, bbox_inches='tight')
    plt.show()
    """)

    upsert_cell(nb, "cluster_backtest_intro", "markdown", """
    ---
    ## 10. Train-only cluster outcome alignment

    This answers a limited question: *do the unsupervised segments separate
    observed payment difficulty better than the portfolio base rate?* It is not a
    probability-of-default model or an inductive prediction test: the segments
    were discovered transductively on the combined unlabeled portfolio. Only
    `application_train` IDs are evaluated; every row receives a cross-fitted
    cluster rate estimated without its own TARGET, and every unlabeled test row
    is excluded. Precision, recall, lift, errors, and the empirical cluster-level
    precision ceiling make the granularity limit visible.
    """)
    upsert_cell(nb, "cluster_backtest_code", "code", """
    from src.domain_credit import cluster_risk_backtest

    target_train = pd.read_csv(
        PROJECT_ROOT / 'datasets/application_train.csv',
        usecols=['SK_ID_CURR', 'TARGET'])
    labels_backtest = pd.read_csv(LABELS_PATH)  # retain SK_ID_CURR for ID-based evaluation
    backtest = cluster_risk_backtest(
        labels=labels_backtest,
        cluster_names=cluster_names_df,
        target=target_train,
        n_splits=5,
        threshold_uplift=1.10,
    )
    artifact_names = {
        'predictions': 'cluster_default_backtest_predictions.csv',
        'metrics': 'cluster_default_backtest_metrics.csv',
        'cluster_rates': 'cluster_default_rates.csv',
        'confusion_matrix': 'cluster_default_confusion_matrix.csv',
        'pr_curve': 'cluster_default_pr_curve.csv',
        'policy_sweep': 'cluster_default_policy_sweep.csv',
    }
    for key, filename in artifact_names.items():
        backtest[key].to_csv(OUT_DIR / filename, index=False)

    metric_values = dict(zip(backtest['metrics']['metric'], backtest['metrics']['value']))
    print('Train-only, cross-fitted cluster outcome alignment:')
    for metric in ['evaluation_rows', 'observed_default_rate', 'flagged_share',
                   'precision', 'recall', 'specificity', 'f1', 'lift_vs_baseline',
                   'average_precision', 'roc_auc', 'test_rows_scored']:
        value = metric_values[metric]
        print(f'  {metric:24s}: {value:,.4f}' if metric not in ['evaluation_rows', 'test_rows_scored']
              else f'  {metric:24s}: {int(value):,}')

    rates = backtest['cluster_rates'].sort_values('default_rate')
    fig, axes = plt.subplots(1, 3, figsize=(18, 5.5))
    axes[0].barh(rates['Segment'], rates['default_rate'] * 100,
                 color=['#5B8A72' if not x else '#B4504A' for x in rates['descriptive_risk_flag']])
    axes[0].axvline(metric_values['observed_default_rate'] * 100, color='#34506B', ls='--',
                    label=f"Portfolio {metric_values['observed_default_rate']:.1%}")
    axes[0].set_xlabel('Observed train default rate (%)')
    axes[0].set_title('Outcome rate by segment', fontweight='bold'); axes[0].legend()

    cm_values = backtest['confusion_matrix'].set_index('actual').to_numpy()
    sns.heatmap(cm_values, annot=True, fmt=',.0f', cmap='Blues', cbar=False, ax=axes[1],
                xticklabels=['Flag non-default', 'Flag default'],
                yticklabels=['Actual non-default', 'Actual default'])
    axes[1].set_title('Out-of-fold confusion matrix', fontweight='bold')
    axes[1].set_xlabel('Cluster flag'); axes[1].set_ylabel('Observed TARGET')

    sweep = backtest['policy_sweep']
    axes[2].plot(sweep['threshold_uplift'], sweep['precision'], marker='o', label='Precision')
    axes[2].plot(sweep['threshold_uplift'], sweep['recall'], marker='o', label='Recall')
    axes[2].plot(sweep['threshold_uplift'], sweep['flagged_share'], marker='o', label='Flagged share')
    axes[2].axvline(1.10, color='#B4504A', ls='--', label='Chosen 1.10x')
    axes[2].set_xlabel('Cluster-rate threshold / portfolio baseline')
    axes[2].set_ylim(0, 1); axes[2].set_title('Policy trade-off', fontweight='bold')
    axes[2].legend()
    plt.tight_layout()
    plt.savefig(OUT_DIR / 'plot_cluster_default_backtest.png', dpi=180, bbox_inches='tight')
    plt.show()

    print('\\nLimitation: five cluster-level scores are too coarse for production underwriting; this is descriptive outcome alignment only.')
    """)

    upsert_cell(nb, "anomaly_threshold_sensitivity_intro", "markdown", """
    ---
    ## 11. Threshold sensitivity

    The assignment requires IQR, Z-score, and Isolation Forest. Conventional
    textbook thresholds are shown beside the skew-adjusted/calibrated operating
    choices so the queue is not presented as threshold-free truth. A detector's
    forced flag rate is an analytical choice, not confidence in default.
    """)
    upsert_cell(nb, "anomaly_threshold_sensitivity_code", "code", """
    conventional_iqr = pd.DataFrame(False, index=feat_sample.index, columns=cont_cols)
    conventional_z = pd.DataFrame(False, index=feat_sample.index, columns=cont_cols)
    for col in cont_cols:
        values = feat_sample[col]
        q1, q3 = values.quantile([.25, .75]); iqr = q3 - q1
        if iqr > 0:
            conventional_iqr[col] = (values < q1 - 1.5 * iqr) | (values > q3 + 1.5 * iqr)
        z = np.abs(stats.zscore(values, nan_policy='omit'))
        conventional_z[col] = z > 3
    threshold_sensitivity = pd.DataFrame([
        {'detector': 'IQR conventional 1.5x; 3+ columns',
         'records': int((conventional_iqr.sum(axis=1) >= MULTI_COL_RULE).sum())},
        {'detector': 'Adjusted IQR calibrated; 3+ columns',
         'records': int(stats_df['is_iqr_outlier'].sum())},
        {'detector': 'Z-score conventional |z|>3; 3+ columns',
         'records': int((conventional_z.sum(axis=1) >= MULTI_COL_RULE).sum())},
        {'detector': 'Z-score empirical 99th percentile; 3+ columns',
         'records': int(stats_df['is_zscore_outlier'].sum())},
    ] + [
        {'detector': f'Isolation Forest contamination {c:.0%}',
         'records': int(iso_df[f"is_isolation_outlier_{c}"].sum())}
        for c in CONTAMINATIONS
    ])
    threshold_sensitivity['share'] = threshold_sensitivity['records'] / len(feat_sample)
    threshold_sensitivity.to_csv(OUT_DIR / 'anomaly_threshold_sensitivity.csv', index=False)
    print(threshold_sensitivity.to_string(index=False))
    """)

    upsert_cell(nb, "supervised_reference_intro", "markdown", """
    ---
    ## 12. Objective-matched supervised diagnostic

    Low cluster precision is not repaired by changing an honest threshold. To
    test whether the weakness comes from the *method objective*, an interpretable
    logistic regression is fitted only on labeled train IDs and evaluated with
    five out-of-fold splits at the same review capacity as the cluster flag.
    Life-stage and socioeconomic proxy axes are excluded. This diagnostic is not
    a deployment PD model: preprocessing is still transductive and there is no
    temporal holdout, calibration approval, fairness validation, or policy cost
    function.
    """)
    upsert_cell(nb, "supervised_reference_code", "code", """
    from src.domain_credit import supervised_reference_benchmark

    reference_features = pd.read_csv(FEATURES_PATH)
    reference = supervised_reference_benchmark(
        features=reference_features,
        target=target_train,
        flagged_share=metric_values['flagged_share'],
        n_splits=5,
    )
    reference['metrics'].to_csv(OUT_DIR / 'supervised_reference_metrics.csv', index=False)
    reference['predictions'].to_csv(OUT_DIR / 'supervised_reference_predictions.csv', index=False)
    reference['coefficients'].to_csv(OUT_DIR / 'supervised_reference_coefficients.csv', index=False)
    reference_metrics = dict(zip(reference['metrics']['metric'], reference['metrics']['value']))

    comparison_rows = []
    for method, values in [
        ('Cluster outcome alignment', metric_values),
        ('Supervised logistic diagnostic', reference_metrics),
    ]:
        for metric_name in ['precision','recall','lift_vs_baseline','average_precision','roc_auc']:
            comparison_rows.append({'method': method, 'metric': metric_name, 'value': values[metric_name]})
    outcome_comparison = pd.DataFrame(comparison_rows)
    outcome_comparison.to_csv(OUT_DIR / 'outcome_method_comparison.csv', index=False)

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    for ax, metrics_here, title in [
        (axes[0], ['precision','recall','average_precision'], 'Positive-class identification'),
        (axes[1], ['lift_vs_baseline','roc_auc'], 'Lift and ranking'),
    ]:
        pivot = outcome_comparison[outcome_comparison.metric.isin(metrics_here)].pivot(
            index='metric', columns='method', values='value')
        pivot.plot(kind='bar', ax=ax, color=['#4E6E8A','#5B8A72'])
        ax.set_title(title, fontweight='bold'); ax.set_xlabel(''); ax.tick_params(axis='x', rotation=20)
    plt.tight_layout(); plt.savefig(OUT_DIR / 'plot_objective_comparison.png', dpi=170, bbox_inches='tight'); plt.show()
    print(outcome_comparison.pivot(index='metric', columns='method', values='value').round(4).to_string())
    """)
    save(path, nb)


def main() -> None:
    update_eda()
    update_phase2()
    update_phase3()
    update_phase4()


if __name__ == "__main__":
    main()

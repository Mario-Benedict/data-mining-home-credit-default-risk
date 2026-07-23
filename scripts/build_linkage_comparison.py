"""Rebuild the sampled Ward/complete/average linkage evidence plot.

Also writes the cophenetic correlation of each linkage on the same sample, so
the linkage choice is defended with a number rather than dendrogram shape
alone. Cophenetic correlation measures how faithfully the merge heights
reproduce the original pairwise distances; a chained but faithful linkage can
score higher than a balanced one, so the coefficient is reported next to the
cluster-balance evidence, not instead of it.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import cophenet, dendrogram, linkage
from scipy.spatial.distance import pdist
from sklearn.decomposition import PCA


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "datasets" / "final" / "features_clustering.csv"
OUTPUT = ROOT / "results" / "phase2_clustering" / "linkage_comparison.png"
COPHENETIC_OUTPUT = ROOT / "results" / "phase2_clustering" / "linkage_cophenetic.csv"
RANDOM_SEED = 42


def main() -> None:
    frame = pd.read_csv(INPUT)
    features = frame.drop(columns="SK_ID_CURR").to_numpy(dtype=np.float32)
    compact = PCA(n_components=min(50, features.shape[1]), random_state=RANDOM_SEED).fit_transform(
        features
    )[:, :10]

    rng = np.random.default_rng(RANDOM_SEED)
    ward_sample = compact[rng.choice(len(compact), size=10_000, replace=False)]
    comparison_sample = ward_sample[
        rng.choice(len(ward_sample), size=2_000, replace=False)
    ]
    methods = ["ward", "complete", "average"]
    results = {method: linkage(comparison_sample, method=method) for method in methods}

    pairwise = pdist(comparison_sample)
    cophenetic_rows = []
    for method in methods:
        coefficient, _ = cophenet(results[method], pairwise)
        cophenetic_rows.append({
            "linkage": method,
            "cophenetic_correlation": float(coefficient),
            "sample_size": len(comparison_sample),
            "space": "10-component clustering PCA space",
            "note": (
                "Chosen operating linkage; balanced merges suit portfolio segmentation"
                if method == "ward"
                else "Comparison linkage; higher fidelity can coexist with chained, unusable groups"
            ),
        })
    cophenetic_frame = pd.DataFrame(cophenetic_rows)
    cophenetic_frame.to_csv(COPHENETIC_OUTPUT, index=False)
    coefficients = dict(
        zip(cophenetic_frame["linkage"], cophenetic_frame["cophenetic_correlation"])
    )

    fig, axes = plt.subplots(1, 3, figsize=(18, 5.8))
    colors = ["#356A8A", "#4F7D65", "#B98535"]
    for axis, method, color in zip(axes, methods, colors):
        dendrogram(
            results[method],
            ax=axis,
            truncate_mode="lastp",
            p=30,
            show_leaf_counts=True,
            leaf_rotation=90,
            leaf_font_size=8,
            color_threshold=0,
            above_threshold_color=color,
        )
        axis.set_title(
            f"{method.title()} — cophenetic r = {coefficients[method]:.3f}",
            fontsize=12,
            fontweight="bold",
        )
        axis.set_xlabel("Truncated groups (30 leaves)")
        axis.set_ylabel("Merge distance")
        axis.grid(axis="y", color="#E7ECEF", linewidth=.7)

    fig.suptitle(
        "Hierarchical linkage comparison on the same 2,000-application sample",
        fontsize=14,
        fontweight="bold",
        y=1.02,
    )
    fig.text(
        .5,
        .005,
        "Sample-level structural check in the 10-component clustering space; not full-data hierarchical clustering",
        ha="center",
        fontsize=10,
        color="#526875",
    )
    fig.tight_layout(rect=(0, .04, 1, .98))
    fig.savefig(OUTPUT, dpi=160, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved {OUTPUT}")
    print(f"Saved {COPHENETIC_OUTPUT}")
    print(cophenetic_frame[["linkage", "cophenetic_correlation"]].to_string(index=False))


if __name__ == "__main__":
    main()

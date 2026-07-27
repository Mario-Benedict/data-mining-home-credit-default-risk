"""Rebuild the sampled Ward/complete/average linkage evidence plot.

The cophenetic correlations themselves are computed and written by Phase 2
(`notebooks/phase2_clustering.ipynb`, Section 6), so the evidence for the
linkage choice lives inside the phase that made the choice. This script only
renders the standalone comparison figure and reads those coefficients back,
which keeps a single source of truth: if the notebook and this figure ever
disagreed, one of them would be quoting a stale run.

Cophenetic correlation measures how faithfully the merge heights reproduce the
original pairwise distances. A chained but faithful linkage can score higher
than a balanced one, so the coefficient is shown next to the group-size
evidence, not instead of it.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.decomposition import PCA


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "datasets" / "final" / "features_clustering.csv"
OUTPUT = ROOT / "results" / "phase2_clustering" / "linkage_comparison.png"
COPHENETIC_INPUT = ROOT / "results" / "phase2_clustering" / "linkage_cophenetic.csv"
RANDOM_SEED = 42
SAMPLE_SIZE = 2_000


def main() -> None:
    if not COPHENETIC_INPUT.exists():
        raise SystemExit(
            f"{COPHENETIC_INPUT.name} is missing. Run notebooks/phase2_clustering.ipynb "
            "first; it owns the cophenetic evidence."
        )
    cophenetic_frame = pd.read_csv(COPHENETIC_INPUT)
    coefficients = dict(
        zip(cophenetic_frame["linkage"], cophenetic_frame["cophenetic_correlation"])
    )
    largest = dict(
        zip(cophenetic_frame["linkage"], cophenetic_frame["largest_group_share"])
    )
    methods = list(cophenetic_frame["linkage"])

    frame = pd.read_csv(INPUT)
    features = frame.drop(columns="SK_ID_CURR").to_numpy(dtype=np.float32)
    compact = PCA(
        n_components=min(50, features.shape[1]), random_state=RANDOM_SEED
    ).fit_transform(features)[:, :10]

    # Same draw as the notebook, so the figure shows the merges behind the
    # coefficients printed in its title rather than a different sample.
    rng = np.random.default_rng(RANDOM_SEED)
    comparison_sample = compact[rng.choice(len(compact), size=SAMPLE_SIZE, replace=False)]
    results = {method: linkage(comparison_sample, method=method) for method in methods}

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
            f"{method.title()}: cophenetic r = {coefficients[method]:.3f}, "
            f"largest group {largest[method]:.0%}",
            fontsize=12,
            fontweight="bold",
        )
        axis.set_xlabel("Truncated groups (30 leaves)")
        axis.set_ylabel("Merge distance")
        axis.grid(axis="y", color="#E7ECEF", linewidth=.7)

    fig.suptitle(
        f"Hierarchical linkage comparison on the same {SAMPLE_SIZE:,}-application sample",
        fontsize=14,
        fontweight="bold",
        y=1.02,
    )
    fig.text(
        .5,
        .005,
        "Higher distance fidelity does not imply usable segments: average linkage chains the "
        "sample into one dominant group. Sample-level structural check in the 10-component "
        "clustering space, not full-data hierarchical clustering.",
        ha="center",
        fontsize=10,
        color="#526875",
    )
    fig.tight_layout(rect=(0, .04, 1, .98))
    fig.savefig(OUTPUT, dpi=160, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved {OUTPUT}")
    print(f"Read coefficients from {COPHENETIC_INPUT.name} (written by Phase 2)")
    print(
        cophenetic_frame[
            ["linkage", "cophenetic_correlation", "largest_group_share"]
        ].to_string(index=False)
    )


if __name__ == "__main__":
    main()

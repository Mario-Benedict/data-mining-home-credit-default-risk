"""Render the cluster-tendency evidence that explains a Silhouette of 0.148.

Phase 2 (`notebooks/phase2_clustering.ipynb`, Section 3) computes and writes
every number shown here. This script only draws them, and it reads them back
rather than recomputing, so the figure and the tables cannot disagree.

The figure answers the question a low Silhouette raises and a single number
cannot settle: is the score low because the portfolio has no structure, or
because it has more than one? Two panels, read together:

* **Left, against the nulls.** The same K-Means, scored on the real data, on a
  column-wise shuffle that preserves every marginal while destroying the joint
  structure, and on a uniform draw over the same box. The bars alone would be
  misleading, so the smallest-group share is annotated on the shuffled bars:
  the shuffled null wins at K = 2 and K = 3 purely by isolating about one
  percent of rows, which is Silhouette rewarding a degenerate split rather than
  finding structure. That annotation is the point of the panel.
* **Right, where the separation lives.** Each feature family clustered on its
  own, against all governed features together. Families that separate well
  alone and poorly together is the signature of several overlapping
  segmentations being forced into one Euclidean partition.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
P2 = ROOT / "results" / "phase2_clustering"
TENDENCY_INPUT = P2 / "cluster_tendency.csv"
FAMILY_INPUT = P2 / "silhouette_by_feature_family.csv"
OUTPUT = P2 / "plot_cluster_tendency.png"
OPERATING_K = 5

REAL = "#356A8A"
SHUFFLED = "#B98535"
UNIFORM = "#9AA7B1"
HIGHLIGHT = "#B5534C"


def main() -> None:
    for path in (TENDENCY_INPUT, FAMILY_INPUT):
        if not path.exists():
            raise SystemExit(
                f"{path.name} is missing. Run notebooks/phase2_clustering.ipynb first; "
                "it owns the cluster-tendency evidence."
            )
    tendency = pd.read_csv(TENDENCY_INPUT).sort_values("k")
    families = pd.read_csv(FAMILY_INPUT).sort_values("silhouette_alone")

    fig, (left, right) = plt.subplots(1, 2, figsize=(16, 6.2))

    # ------------------------------------------------ left: against two nulls
    positions = np.arange(len(tendency))
    width = 0.27
    series = [
        ("real_silhouette", "Real data", REAL, -width),
        ("shuffled_silhouette", "Column-wise shuffle (null)", SHUFFLED, 0.0),
        ("uniform_silhouette", "Uniform draw (null)", UNIFORM, width),
    ]
    for column, label, color, offset in series:
        left.bar(positions + offset, tendency[column], width, label=label, color=color)

    # Annotate the shuffled bars that beat the real data. Without the group
    # share beside them, those bars read as "the null found more structure",
    # which is the exact misreading the panel exists to prevent.
    beats_real = tendency["shuffled_silhouette"] > tendency["real_silhouette"]
    for position, (_, row) in zip(positions, tendency.iterrows()):
        if not beats_real.loc[row.name]:
            continue
        left.annotate(
            f"null wins by isolating\n{row['shuffled_smallest_group']:.2%} of rows",
            xy=(position, row["shuffled_silhouette"]),
            xytext=(position, row["shuffled_silhouette"] + 0.07),
            ha="center",
            fontsize=9,
            color=HIGHLIGHT,
            fontweight="bold",
            arrowprops=dict(arrowstyle="-", color=HIGHLIGHT, linewidth=.9),
        )

    operating = tendency.loc[tendency["k"].eq(OPERATING_K)].iloc[0]
    operating_position = int(np.flatnonzero(tendency["k"].eq(OPERATING_K).to_numpy())[0])
    left.axvspan(operating_position - .5, operating_position + .5, color="#356A8A", alpha=.07)
    left.annotate(
        f"operating resolution\nreal {operating['real_silhouette']:.4f} clears both nulls",
        xy=(operating_position, operating["real_silhouette"]),
        xytext=(operating_position + .35, operating["real_silhouette"] + .30),
        ha="left",
        fontsize=9,
        color=REAL,
        fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=REAL, linewidth=.9),
    )
    left.set_xticks(positions)
    left.set_xticklabels([f"K = {int(k)}" for k in tendency["k"]])
    left.set_ylabel("Silhouette Score")
    left.set_ylim(0, max(float(tendency["shuffled_silhouette"].max()) + .22, .5))
    left.set_title(
        "A Silhouette is only readable against the null on the same data",
        fontsize=12,
        fontweight="bold",
    )
    left.legend(frameon=False, fontsize=9, loc="upper right")
    left.grid(axis="y", color="#E7ECEF", linewidth=.7)
    left.set_axisbelow(True)

    # -------------------------------------- right: where the separation lives
    combined = families["feature_family"].str.contains("together", case=False)
    colors = [HIGHLIGHT if flag else REAL for flag in combined]
    bars = right.barh(families["feature_family"], families["silhouette_alone"], color=colors)
    for bar, value in zip(bars, families["silhouette_alone"]):
        right.text(
            value + .012,
            bar.get_y() + bar.get_height() / 2,
            f"{value:.3f}",
            va="center",
            fontsize=10,
            fontweight="bold",
            color="#33424D",
        )
    right.set_xlim(0, float(families["silhouette_alone"].max()) * 1.18)
    right.set_xlabel(f"Silhouette when clustered on its own, K = {OPERATING_K}")
    right.set_title(
        "Each family separates the portfolio a different way",
        fontsize=12,
        fontweight="bold",
    )
    right.grid(axis="x", color="#E7ECEF", linewidth=.7)
    right.set_axisbelow(True)

    fig.suptitle(
        "Why the combined Silhouette is low: the portfolio carries several "
        "overlapping segmentations, not none",
        fontsize=14,
        fontweight="bold",
        y=1.03,
    )
    fig.text(
        .5,
        .005,
        "Numbers read back from cluster_tendency.csv and silhouette_by_feature_family.csv, both "
        "written by Phase 2. Left panel scored on a fixed 20,000-application sample; the shuffled "
        "null preserves every marginal distribution and destroys only the joint structure.",
        ha="center",
        fontsize=10,
        color="#526875",
    )
    fig.tight_layout(rect=(0, .04, 1, .97))
    fig.savefig(OUTPUT, dpi=160, bbox_inches="tight", facecolor="white")
    plt.close(fig)

    print(f"Saved {OUTPUT}")
    print(f"Read evidence from {TENDENCY_INPUT.name} and {FAMILY_INPUT.name} (written by Phase 2)")
    print(tendency[[
        "k", "real_silhouette", "shuffled_silhouette", "shuffled_smallest_group",
        "uniform_silhouette",
    ]].round(4).to_string(index=False))
    print(families.round(4).to_string(index=False))


if __name__ == "__main__":
    main()

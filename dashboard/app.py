"""Responsive, artifact-driven dashboard for Home Credit portfolio discovery."""

from __future__ import annotations

import math
import os
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, Input, Output, State, dash_table, dcc, html
from dash.dash_table.Format import Format, Scheme


ROOT = Path(__file__).resolve().parents[1]
P1 = ROOT / "results/phase1_preprocessing"
P2 = ROOT / "results/phase2_clustering"
P3 = ROOT / "results/phase3_association"
P4 = ROOT / "results/phase4_anomaly"


def read_csv(path: Path, **kwargs) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Missing dashboard artifact: {path}. Re-run the notebooks in phase order.")
    return pd.read_csv(path, **kwargs)


def read_optional(path: Path, columns: list[str] | None = None) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame(columns=columns or [])
    return pd.read_csv(path)


quality = read_csv(P1 / "data_quality_summary.csv")
feature_importance = read_csv(P1 / "feature_importance.csv")
portfolio = read_csv(P1 / "portfolio_context.csv")
cluster_names = read_csv(P2 / "cluster_names.csv").sort_values("cluster_id")
cluster_comparison = read_csv(P2 / "cluster_comparison_long.csv")
cluster_viz = read_csv(P2 / "cluster_viz_sample.csv")
dbscan_viz = read_csv(P2 / "dbscan_umap_sample.csv")
k_selection = read_csv(P2 / "k_selection.csv")
pca_sensitivity = read_optional(P2 / "pca_cluster_sensitivity.csv")
method_agreement = read_optional(P2 / "method_agreement.csv")
rule_view = read_csv(P3 / "rule_visual_summary.csv")
rule_segment = read_csv(P3 / "rule_segment_summary.csv")
algo_comparison = read_csv(P3 / "algo_comparison.csv")
anomaly_summary = read_csv(P4 / "anomaly_summary.csv").iloc[0]
anomaly_investigation = read_csv(P4 / "anomaly_investigation.csv")
anomaly_drivers = read_csv(P4 / "anomaly_driver_summary.csv")
anomaly_by_segment = read_csv(P4 / "anomaly_review_by_segment.csv", index_col=0)
detector_overlap = read_csv(P4 / "detector_jaccard_overlap.csv", index_col=0)
anomaly_pca = read_csv(P4 / "pca_anomaly_sample.csv")
backtest_metrics = read_csv(P4 / "cluster_default_backtest_metrics.csv")
cluster_rates = read_csv(P4 / "cluster_default_rates.csv")
backtest_cm = read_csv(P4 / "cluster_default_confusion_matrix.csv")
policy_sweep = read_csv(P4 / "cluster_default_policy_sweep.csv")
reference_metrics = read_optional(P4 / "supervised_reference_metrics.csv")
outcome_comparison = read_optional(P4 / "outcome_method_comparison.csv")

# Transitional fallbacks keep the app importable while a user is rerunning the
# phase notebooks; the verified run replaces these with denominator-labelled
# fields from the corrected Phase 3 artefact.
if "support_count" not in rule_view:
    rule_view["support_count"] = (rule_view["support"] * 356_255).round().astype(int)
if "metric_scope" not in rule_view:
    rule_view["metric_scope"] = "Re-run Phase 3 for explicit metric denominator"
if "Context" not in rule_view:
    rule_view["Context"] = rule_view["Segment"]


NAME_BY_ID = dict(zip(cluster_names["cluster_id"].astype(int), cluster_names["nama"]))
SEGMENT_ORDER = cluster_names["nama"].tolist()
SEGMENT_COLORS = {
    "Intensive Card User": "#64748B",
    "History-Rich Credit User": "#356A8A",
    "Thin-File / Low-Intensity": "#4F7D65",
    "Repayment-Stress History": "#B5534C",
    "High-Exposure Applicant": "#B98535",
}
REVIEW_COLORS = {
    "Affordability / repayment review": "#B5534C",
    "Data consistency check": "#B98535",
    "Rare but plausible profile": "#356A8A",
}
SEVERITY_COLORS = {
    "NORMAL": "#CBD5E1",
    "WEAK_SIGNAL": "#D5AE5D",
    "MODERATE_ANOMALY": "#C97543",
    "HIGH_CONFIDENCE_ANOMALY": "#A93F3A",
}
FEATURE_LABELS = {
    "EXT_SOURCE_1": "External score 1",
    "EXT_SOURCE_2": "External score 2",
    "EXT_SOURCE_3": "External score 3",
    "AMT_INCOME_TOTAL": "Income",
    "AMT_CREDIT": "Requested credit",
    "AMT_ANNUITY": "Annuity",
    "CREDIT_TO_INCOME": "Credit / income",
    "ANNUITY_TO_INCOME": "Annuity / income",
    "INST_DPD_MAX": "Maximum installment DPD",
    "INST_LATE_RATIO": "Installment late share",
    "BUREAU_COUNT": "Bureau history depth",
    "PREV_COUNT": "Prior application depth",
    "INST_COUNT": "Observed installments",
}


def metric(name: str, frame: pd.DataFrame = backtest_metrics, default: float = np.nan) -> float:
    if frame.empty or "metric" not in frame:
        return float(default)
    values = frame.loc[frame["metric"].eq(name), "value"]
    return float(values.iloc[0]) if len(values) else float(default)


def fmt_int(value: float) -> str:
    return f"{int(round(value)):,}"


def fmt_pct(value: float, digits: int = 1) -> str:
    return "—" if not np.isfinite(value) else f"{value * 100:.{digits}f}%"


def stratified_sample(frame: pd.DataFrame, group: str, limit: int, seed: int = 42) -> pd.DataFrame:
    if len(frame) <= limit:
        return frame.copy()
    rng = np.random.default_rng(seed)
    pieces = []
    for _, part in frame.groupby(group, dropna=False):
        take = max(1, int(round(limit * len(part) / len(frame))))
        indices = rng.choice(part.index.to_numpy(), size=min(take, len(part)), replace=False)
        pieces.append(frame.loc[indices])
    sampled = pd.concat(pieces)
    if len(sampled) > limit:
        sampled = sampled.sample(limit, random_state=seed)
    return sampled


def chart_layout(fig: go.Figure, *, legend: bool = True, left: int = 48, bottom: int = 48) -> go.Figure:
    fig.update_layout(
        template="plotly_white",
        autosize=True,
        margin=dict(l=left, r=22, t=18, b=bottom),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="#FFFFFF",
        font=dict(family="Inter, Segoe UI, sans-serif", size=12, color="#203746"),
        legend=dict(title_text="", orientation="h", yanchor="bottom", y=1.01, x=0),
        showlegend=legend,
        hoverlabel=dict(bgcolor="#173647", font_color="white"),
    )
    fig.update_xaxes(gridcolor="#E6EDF1", zeroline=False, automargin=True)
    fig.update_yaxes(gridcolor="#E6EDF1", zeroline=False, automargin=True)
    return fig


def graph(fig: go.Figure, size: str = "standard", min_width: int | None = None):
    component = dcc.Graph(
        figure=fig,
        responsive=True,
        className=f"plot plot-{size}",
        style={"height": "var(--plot-height)", "minHeight": "var(--plot-height)",
               **({"minWidth": f"{min_width}px"} if min_width else {})},
        config={"displaylogo": False, "responsive": True, "modeBarButtonsToRemove": ["lasso2d", "select2d"]},
    )
    return html.Div(component, className="plot-scroll" if min_width else "plot-wrap")


def card(label: str, value: str, note: str, tone: str = "blue") -> html.Div:
    return html.Div([
        html.Div(label, className="metric-label"),
        html.Div(value, className="metric-value"),
        html.Div(note, className="metric-note"),
    ], className=f"metric-card tone-{tone}")


def panel(title: str, content, caption: str | None = None, wide: bool = False) -> html.Div:
    children = [html.Div(title, className="panel-title")]
    if caption:
        children.append(html.Div(caption, className="panel-caption"))
    children.append(content)
    return html.Div(children, className=f"panel{' panel-wide' if wide else ''}")


def heading(kicker: str, title: str, subtitle: str) -> html.Div:
    return html.Div([
        html.Div(kicker, className="section-kicker"),
        html.H2(title),
        html.P(subtitle),
    ], className="section-heading")


# Overview figures
quality_plot = quality.sort_values("affected_share")
fig_quality = px.bar(
    quality_plot, x=quality_plot["affected_share"] * 100, y="issue", orientation="h",
    color_discrete_sequence=["#356A8A"], custom_data=["business_meaning", "treatment"],
)
fig_quality.update_traces(
    texttemplate="%{x:.1f}%", textposition="outside",
    hovertemplate="<b>%{y}</b><br>%{x:.1f}% of applications<br>%{customdata[0]}<br>Action: %{customdata[1]}<extra></extra>",
)
fig_quality.update_xaxes(title="Combined portfolio (%)", range=[0, quality_plot.affected_share.max() * 118])
fig_quality.update_yaxes(title="")
chart_layout(fig_quality, legend=False, left=150)

fi = feature_importance.head(10).sort_values("mutual_info").copy()
fi["label"] = fi["feature"].map(FEATURE_LABELS).fillna(fi["feature"].str.replace("_", " ").str.title())
fig_importance = px.bar(fi, x="mutual_info", y="label", orientation="h", color_discrete_sequence=["#4F7D65"])
fig_importance.update_traces(hovertemplate="<b>%{y}</b><br>Mutual information: %{x:.4f}<extra></extra>")
fig_importance.update_xaxes(title="Mutual information with train TARGET")
fig_importance.update_yaxes(title="")
chart_layout(fig_importance, legend=False, left=155)


# Segmentation figures
comparison_matrix = cluster_comparison.pivot(
    index="business_dimension", columns="Segment", values="portfolio_sd"
).reindex(columns=SEGMENT_ORDER)
fig_segment_heatmap = go.Figure(go.Heatmap(
    z=comparison_matrix.values,
    x=comparison_matrix.columns,
    y=comparison_matrix.index,
    colorscale=[[0, "#C97543"], [.5, "#F7F7F2"], [1, "#356A8A"]],
    zmid=0,
    text=np.round(comparison_matrix.values, 2),
    texttemplate="%{text:.2f}",
    colorbar=dict(title="Portfolio<br>SD", thickness=14),
    hovertemplate="<b>%{x}</b><br>%{y}: %{z:.2f} SD<extra></extra>",
))
chart_layout(fig_segment_heatmap, left=135, bottom=75)

fig_sizes = px.bar(
    cluster_names, x="n_applicants", y="nama", orientation="h", color="nama",
    color_discrete_map=SEGMENT_COLORS, category_orders={"nama": SEGMENT_ORDER},
    custom_data=["profile_summary", "watch_items"],
)
fig_sizes.update_traces(
    texttemplate="%{x:,}", textposition="outside",
    hovertemplate="<b>%{y}</b><br>%{x:,} applications<br>%{customdata[0]}<br>Watch: %{customdata[1]}<extra></extra>",
)
fig_sizes.update_xaxes(title="Applications", range=[0, cluster_names.n_applicants.max() * 1.20])
fig_sizes.update_yaxes(title="", categoryorder="array", categoryarray=SEGMENT_ORDER[::-1])
chart_layout(fig_sizes, legend=False, left=120)

kmeans_plot = cluster_viz.copy()
kmeans_plot["Segment"] = kmeans_plot["CLUSTER_KMEANS"].map(NAME_BY_ID)
kmeans_plot = stratified_sample(kmeans_plot, "Segment", 8_000)
fig_kmeans = px.scatter(
    kmeans_plot, x="PC1", y="PC2", color="Segment", color_discrete_map=SEGMENT_COLORS,
    opacity=.48, render_mode="webgl",
)
fig_kmeans.update_traces(marker=dict(size=4), hovertemplate="%{fullData.name}<br>PC1 %{x:.2f} · PC2 %{y:.2f}<extra></extra>")
chart_layout(fig_kmeans, bottom=60)

dense_db = dbscan_viz[dbscan_viz["IS_NOISE"].eq(0)]
noise_db = dbscan_viz[dbscan_viz["IS_NOISE"].eq(1)]
dense_db = dense_db.sample(min(11_000, len(dense_db)), random_state=42)
dbscan_plot = pd.concat([dense_db, noise_db], ignore_index=True)
dbscan_plot["Density status"] = np.where(dbscan_plot["IS_NOISE"].eq(1), "Noise — review", "Density pocket")
fig_dbscan = px.scatter(
    dbscan_plot.sort_values("IS_NOISE"), x="UMAP1", y="UMAP2", color="Density status",
    color_discrete_map={"Density pocket": "#356A8A", "Noise — review": "#B5534C"},
    opacity=.48, render_mode="webgl", custom_data=["SK_ID_CURR", "Segment", "DBSCAN_LABEL"],
)
fig_dbscan.update_traces(
    marker=dict(size=4),
    hovertemplate="Applicant %{customdata[0]}<br>%{customdata[1]}<br>DBSCAN label %{customdata[2]}<extra></extra>",
)
chart_layout(fig_dbscan, bottom=55)

fig_k_selection = go.Figure()
fig_k_selection.add_trace(go.Scatter(
    x=k_selection["k"], y=k_selection["silhouette"], mode="lines+markers",
    name="Silhouette", line=dict(color="#356A8A", width=3),
    hovertemplate="K=%{x}<br>Silhouette %{y:.3f}<extra></extra>",
))
fig_k_selection.add_vline(x=5, line_dash="dash", line_color="#B98535", annotation_text="Selected K=5")
fig_k_selection.update_xaxes(title="Number of segments (K)", dtick=1)
fig_k_selection.update_yaxes(title="Silhouette", rangemode="tozero")
chart_layout(fig_k_selection, legend=False)

if not pca_sensitivity.empty:
    fig_pca_sensitivity = px.scatter(
        pca_sensitivity, x="retained_variance", y="ari_vs_10pc", size="n_components",
        color="silhouette", color_continuous_scale="Blues",
        custom_data=["n_components", "silhouette", "min_cluster_share"],
    )
    fig_pca_sensitivity.update_traces(
        marker=dict(line=dict(width=1, color="white")),
        hovertemplate="%{customdata[0]} PCs<br>Variance %{x:.1%}<br>ARI vs 10PC %{y:.3f}<br>Silhouette %{customdata[1]:.3f}<extra></extra>",
    )
    fig_pca_sensitivity.update_xaxes(title="Retained variance", tickformat=".0%")
    fig_pca_sensitivity.update_yaxes(title="Label agreement with 10-PC solution", range=[0, 1.02])
    chart_layout(fig_pca_sensitivity, legend=False)
else:
    fig_pca_sensitivity = go.Figure().add_annotation(text="Re-run Phase 2 for PCA sensitivity", showarrow=False)
    chart_layout(fig_pca_sensitivity, legend=False)


# Rule figures
fig_rules = px.scatter(
    rule_view.sort_values("rank"), x="lift", y="rank", color="Segment", size="confidence",
    color_discrete_map=SEGMENT_COLORS,
    custom_data=["short_rule", "support", "confidence", "support_count", "metric_scope"],
)
fig_rules.update_traces(
    hovertemplate="<b>Rule %{y}</b><br>%{customdata[0]}<br>Lift %{x:.2f} · support %{customdata[1]:.1%} (%{customdata[3]:,} rows)<br>Confidence %{customdata[2]:.1%}<br>%{customdata[4]}<extra></extra>"
)
fig_rules.update_xaxes(title="Lift (1 = chance)")
fig_rules.update_yaxes(title="Rule rank", autorange="reversed", dtick=1)
chart_layout(fig_rules, bottom=60)

algo_plot = algo_comparison.copy()
algo_plot["label"] = algo_plot["Algoritma"].replace({
    "apriori": "Apriori", "fpgrowth": "FP-Growth", "eclat": "ECLAT",
    "fpgrowth_per_cluster": "Segment FP-Growth",
})
fig_algorithms = px.bar(algo_plot, x="label", y="Rules", color_discrete_sequence=["#64748B"])
fig_algorithms.update_traces(texttemplate="%{y:,}", textposition="outside")
fig_algorithms.update_xaxes(title=""); fig_algorithms.update_yaxes(title="Candidate rules")
chart_layout(fig_algorithms, legend=False, bottom=70)

if "support_records" in rule_segment.columns:
    fig_rule_segments = px.bar(
        rule_segment, x="mean_lift", y="Segment", orientation="h", color="Segment",
        color_discrete_map=SEGMENT_COLORS, custom_data=["mean_confidence", "support_records"],
    )
    fig_rule_segments.update_traces(
        texttemplate="%{x:.2f}×", textposition="outside",
        hovertemplate="%{y}<br>Mean lift %{x:.2f}×<br>Mean confidence %{customdata[0]:.1%}<br>Summed support count %{customdata[1]:,}<extra></extra>",
    )
    fig_rule_segments.update_xaxes(title="Mean lift of selected rules")
    fig_rule_segments.update_yaxes(title="")
    chart_layout(fig_rule_segments, legend=False, left=120)
else:
    fig_rule_segments = go.Figure().add_annotation(text="Re-run Phase 3", showarrow=False)
    chart_layout(fig_rule_segments, legend=False)


# Anomaly figures
detector_counts = pd.DataFrame({
    "Detector": ["Adjusted IQR", "Z-score", "Mahalanobis", "Isolation Forest", "LOF", "DBSCAN noise", "3+ consensus"],
    "Records": [anomaly_summary.N_IQR, anomaly_summary.N_ZSCORE, anomaly_summary.N_MAHALANOBIS,
                anomaly_summary.N_ISOFOREST, anomaly_summary.N_LOF, anomaly_summary.N_DBSCAN,
                anomaly_summary.HIGH_CONFIDENCE],
}).sort_values("Records")
fig_detectors = px.bar(detector_counts, x="Records", y="Detector", orientation="h", color_discrete_sequence=["#64748B"])
fig_detectors.update_traces(texttemplate="%{x:,}", textposition="outside")
fig_detectors.update_xaxes(title="Applications", range=[0, detector_counts.Records.max() * 1.35])
fig_detectors.update_yaxes(title="")
chart_layout(fig_detectors, legend=False, left=120)

fig_overlap = go.Figure(go.Heatmap(
    z=detector_overlap.values.astype(float), x=detector_overlap.columns, y=detector_overlap.index,
    colorscale="Blues", zmin=0, zmax=1, text=np.round(detector_overlap.values.astype(float), 2),
    texttemplate="%{text:.2f}", colorbar=dict(title="Jaccard", thickness=14),
    hovertemplate="%{y} × %{x}<br>Jaccard overlap %{z:.2f}<extra></extra>",
))
chart_layout(fig_overlap, left=105, bottom=85)

driver_plot = anomaly_drivers.head(12).sort_values("records")
fig_drivers = px.bar(
    driver_plot, x="records", y="Driver", orientation="h", color="Review Type",
    color_discrete_map=REVIEW_COLORS,
)
fig_drivers.update_traces(texttemplate="%{x:,}", textposition="outside")
fig_drivers.update_xaxes(title="Consensus records"); fig_drivers.update_yaxes(title="")
chart_layout(fig_drivers, left=170)

review_long = anomaly_by_segment.reset_index(names="Segment").melt(
    id_vars="Segment", var_name="Review Type", value_name="Records"
)
fig_review_segment = px.bar(
    review_long, x="Records", y="Segment", color="Review Type", orientation="h",
    color_discrete_map=REVIEW_COLORS,
)
fig_review_segment.update_yaxes(title="", categoryorder="array", categoryarray=SEGMENT_ORDER[::-1])
fig_review_segment.update_xaxes(title="Consensus records")
chart_layout(fig_review_segment, left=120)

anomaly_plot = anomaly_pca.copy()
high = anomaly_plot[anomaly_plot["anomaly_category"].eq("HIGH_CONFIDENCE_ANOMALY")]
other = anomaly_plot[~anomaly_plot.index.isin(high.index)]
other = stratified_sample(other, "anomaly_category", max(1, 12_000 - len(high)))
anomaly_plot = pd.concat([other, high], ignore_index=True)
fig_anomaly_pca = px.scatter(
    anomaly_plot, x="PC1", y="PC2", color="anomaly_category",
    color_discrete_map=SEVERITY_COLORS, opacity=.50, render_mode="webgl",
    category_orders={"anomaly_category": list(SEVERITY_COLORS)},
)
fig_anomaly_pca.update_traces(marker=dict(size=4), hovertemplate="%{fullData.name}<br>PC1 %{x:.2f} · PC2 %{y:.2f}<extra></extra>")
chart_layout(fig_anomaly_pca, bottom=60)


# Outcome figures
rates = cluster_rates.set_index("Segment").reindex(SEGMENT_ORDER).reset_index()
fig_rates = px.bar(
    rates, x="default_rate", y="Segment", orientation="h", color="descriptive_risk_flag",
    color_discrete_map={True: "#B5534C", False: "#356A8A"},
    custom_data=["train_applicants", "defaults", "lift_vs_portfolio"],
)
fig_rates.add_vline(
    x=metric("observed_default_rate"), line_dash="dash", line_color="#203746",
    annotation_text=f"Portfolio {fmt_pct(metric('observed_default_rate'))}",
)
fig_rates.update_traces(
    texttemplate="%{x:.1%}", textposition="outside",
    hovertemplate="<b>%{y}</b><br>Rate %{x:.2%}<br>%{customdata[1]:,} defaults / %{customdata[0]:,} train rows<br>Lift %{customdata[2]:.2f}×<extra></extra>",
)
fig_rates.update_xaxes(title="Observed TARGET=1 rate", tickformat=".0%", range=[0, rates.default_rate.max() * 1.28])
fig_rates.update_yaxes(title="")
chart_layout(fig_rates, legend=False, left=120)

cm = backtest_cm.set_index("actual")[["Flag non-default", "Flag default"]]
fig_cm = go.Figure(go.Heatmap(
    z=cm.values, x=["Not flagged", "Cluster flag"], y=["Observed non-default", "Observed default"],
    colorscale="Blues", text=cm.values, texttemplate="%{text:,}", showscale=False,
    hovertemplate="%{y} / %{x}<br>%{z:,} train rows<extra></extra>",
))
chart_layout(fig_cm, left=120, bottom=65)

fig_policy = go.Figure()
for col, label, color in [
    ("precision", "Precision", "#B5534C"),
    ("recall", "Recall", "#356A8A"),
    ("flagged_share", "Flagged share", "#B98535"),
]:
    fig_policy.add_trace(go.Scatter(
        x=policy_sweep["threshold_uplift"], y=policy_sweep[col], mode="lines+markers",
        name=label, line=dict(color=color, width=3),
        hovertemplate=f"{label}: %{{y:.1%}}<br>Threshold %{{x:.2f}}× baseline<extra></extra>",
    ))
fig_policy.add_vline(x=1.10, line_dash="dash", line_color="#203746", annotation_text="Chosen 1.10×")
fig_policy.update_xaxes(title="Cluster-rate threshold / fold baseline")
fig_policy.update_yaxes(title="Share", tickformat=".0%", range=[0, 1])
chart_layout(fig_policy)

if not outcome_comparison.empty:
    metric_labels = {
        "precision": "Precision", "recall": "Recall", "average_precision": "Average precision",
        "roc_auc": "ROC AUC", "lift_vs_baseline": "Lift / baseline",
    }
    comparison_plot = outcome_comparison.copy()
    comparison_plot["Metric"] = comparison_plot["metric"].map(metric_labels)
    fig_objective = px.bar(
        comparison_plot, x="Metric", y="value", color="method", barmode="group",
        color_discrete_map={
            "Cluster outcome alignment": "#64748B",
            "Supervised logistic diagnostic": "#4F7D65",
        },
    )
    fig_objective.update_traces(texttemplate="%{y:.2f}", textposition="outside")
    fig_objective.update_yaxes(title="Metric value", rangemode="tozero")
    fig_objective.update_xaxes(title="")
    chart_layout(fig_objective, bottom=80)
else:
    fig_objective = go.Figure().add_annotation(text="Re-run Phase 4 for supervised diagnostic", showarrow=False)
    chart_layout(fig_objective, legend=False)


TABLE_BASE = {
    "style_header": {
        "backgroundColor": "#E8EFF2", "fontWeight": "700", "color": "#173647",
        "border": "0", "padding": "10px",
    },
    "style_cell": {
        "fontFamily": "Inter, Segoe UI, sans-serif", "fontSize": 12, "padding": "9px",
        "textAlign": "left", "border": "1px solid #E4EBEF", "whiteSpace": "nowrap",
        "overflow": "hidden", "textOverflow": "ellipsis", "maxWidth": "280px",
    },
    "style_table": {"overflowX": "auto", "minWidth": "100%"},
}


def segment_cards() -> html.Div:
    cards = []
    for row in cluster_names.itertuples():
        cards.append(html.Article([
            html.Div([
                html.H3(row.nama), html.Span(f"{row.n_applicants:,}", className="segment-count"),
            ], className="segment-card-head"),
            html.P(row.profile_summary),
            html.Div([html.Strong("Watch"), html.Span(row.watch_items)], className="segment-line"),
            html.Div([html.Strong("Review"), html.Span(row.recommended_action)], className="segment-line"),
        ], className="segment-card", style={"--segment-color": SEGMENT_COLORS.get(row.nama, "#64748B")}))
    return html.Div(cards, className="segment-grid")


rules_table = dash_table.DataTable(
    data=rule_view[["rank", "Segment", "short_rule", "support", "confidence", "lift", "metric_scope"]].to_dict("records"),
    columns=[
        {"name": "#", "id": "rank"}, {"name": "Segment", "id": "Segment"},
        {"name": "Non-trivial rule", "id": "short_rule"},
        {"name": "Support", "id": "support", "type": "numeric", "format": Format(precision=1, scheme=Scheme.percentage)},
        {"name": "Confidence", "id": "confidence", "type": "numeric", "format": Format(precision=1, scheme=Scheme.percentage)},
        {"name": "Lift", "id": "lift", "type": "numeric", "format": Format(precision=2, scheme=Scheme.fixed)},
        {"name": "Metric scope", "id": "metric_scope"},
    ],
    page_size=8,
    sort_action="native",
    filter_action="native",
    tooltip_data=[
        {column: {"value": str(value), "type": "markdown"} for column, value in row.items()}
        for row in rule_view[["rank", "Segment", "short_rule", "support", "confidence", "lift", "metric_scope"]].to_dict("records")
    ],
    tooltip_duration=None,
    **TABLE_BASE,
)


ANOMALY_TABLE_COLUMNS = ["SK_ID_CURR", "Segment", "Review Type", "Priority", "Primary Driver", "Detected By"]


def anomaly_page(frame: pd.DataFrame, page_current: int = 0, page_size: int = 10) -> list[dict]:
    start = page_current * page_size
    return frame.iloc[start:start + page_size][ANOMALY_TABLE_COLUMNS].to_dict("records")


def anomaly_table_component() -> dash_table.DataTable:
    return dash_table.DataTable(
        id="anomaly-table",
        data=anomaly_page(anomaly_investigation),
        columns=[{"name": c.replace("SK_ID_CURR", "Applicant ID"), "id": c} for c in ANOMALY_TABLE_COLUMNS],
        page_current=0,
        page_size=10,
        page_count=max(1, math.ceil(len(anomaly_investigation) / 10)),
        page_action="custom",
        sort_action="custom",
        sort_mode="multi",
        sort_by=[],
        filter_action="custom",
        filter_query="",
        cell_selectable=True,
        style_data_conditional=[
            {"if": {"filter_query": '{Review Type} = "Data consistency check"', "column_id": "Review Type"},
             "backgroundColor": "#FFF3DA", "fontWeight": "700"},
            {"if": {"filter_query": '{Review Type} = "Affordability / repayment review"', "column_id": "Review Type"},
             "backgroundColor": "#FBE9E7", "fontWeight": "700"},
            {"if": {"state": "active"}, "backgroundColor": "#DCEBF2", "border": "1px solid #356A8A"},
        ],
        **TABLE_BASE,
    )


def overview_layout() -> html.Section:
    return html.Section([
        heading("01 · PORTFOLIO", "Data boundary before discovery",
                "Combined train + test supports unlabeled mining; TARGET evaluation stays train-only."),
        html.Div([
            card("Discovery rows", "356,255", "307,511 train + 48,744 test", "blue"),
            card("Observed train default", fmt_pct(metric("observed_default_rate"), 2), "TARGET=1 base rate", "amber"),
            card("Named segments", "5", "Robust K-Means + Ward check", "green"),
            card("3+ detector consensus", fmt_int(anomaly_summary.HIGH_CONFIDENCE), "Human-review queue", "red"),
        ], className="metric-grid"),
        html.Div([
            panel("Different data conditions, different treatments", graph(fig_quality, "standard"),
                  "Absence, uncertainty, and implausible values are not interchangeable."),
            panel("Train-label information screen", graph(fig_importance, "standard"),
                  "Post-hoc relevance only; TARGET did not build the clusters."),
        ], className="two-col"),
        html.Div([
            html.Strong("Interpretation boundary"),
            html.Span("This project discovers portfolio knowledge. It does not produce a production PD, approval rule, price, or adverse-action reason."),
        ], className="guardrail"),
    ], className="tab-section")


def segments_layout() -> html.Section:
    ward_text = "not yet rerun"
    if not method_agreement.empty:
        ward_text = f"ARI {method_agreement.adjusted_rand_index.iloc[0]:.3f}"
    return html.Section([
        heading("02 · SEGMENTATION", "Compare every segment on one scale",
                "The heatmap carries the comparison; cards keep profiles and bounded actions visible without a dropdown."),
        panel("Business-dimension comparison", graph(fig_segment_heatmap, "tall", min_width=720),
              "Positive means more of the named dimension—not better or worse.", wide=True),
        html.Div([
            panel("Portfolio reach", graph(fig_sizes, "standard")),
            panel("K selection", graph(fig_k_selection, "standard"),
                  "K=3 has the highest sampled silhouette; K=5 is the stable business resolution."),
        ], className="two-col"),
        html.Div([
            panel("PCA sensitivity", graph(fig_pca_sensitivity, "standard"),
                  "Label agreement tests whether 10 PCs discard material segment structure."),
            panel("Method check", html.Div([
                html.Div(ward_text, className="method-value"),
                html.P("K-Means versus sampled Ward nearest-centre assignment."),
                html.P("DBSCAN remains a separate sampled density diagnostic."),
            ], className="method-box")),
        ], className="two-col"),
        html.Div([
            panel("K-Means centre geometry", graph(fig_kmeans, "map", min_width=620),
                  "8K stratified display sample; first two PCs are a viewing surface."),
            panel("DBSCAN local density", graph(fig_dbscan, "map"),
                  f"All {int(anomaly_summary.N_DBSCAN):,} noise points retained; dense points downsampled for responsiveness."),
        ], className="two-col"),
        html.H3("Profiles and bounded review actions", className="subsection-title"),
        segment_cards(),
    ], className="tab-section")


def rules_layout() -> html.Section:
    return html.Section([
        heading("03 · ASSOCIATIONS", "Keep only non-trivial co-occurrence",
                "Algebraic identities are rejected; segment metrics keep their own denominators."),
        html.Div([
            panel("Rule strength and confidence", graph(fig_rules, "tall")),
            panel("Selected-rule lift by segment", graph(fig_rule_segments, "tall")),
        ], className="two-col"),
        panel("Enumeration and context checks", graph(fig_algorithms, "compact"),
              "Apriori, FP-Growth, and ECLAT validate the same global search; segment FP-Growth is a different denominator.", wide=True),
        panel("Final rule evidence", html.Div(rules_table, className="table-shell"),
              "Filter by segment or condition. Support and confidence mean what the metric-scope column says.", wide=True),
    ], className="tab-section")


def anomalies_layout() -> html.Section:
    counts = anomaly_investigation["Review Type"].value_counts()
    return html.Section([
        heading("04 · ANOMALIES", "Unusualness becomes a review route—not a decision",
                "Source values, detector agreement, and business evidence determine what a reviewer should verify."),
        html.Div([
            card("3+ consensus", fmt_int(anomaly_summary.HIGH_CONFIDENCE), "Internal agreement tier", "red"),
            card("Repayment / affordability", fmt_int(counts.get("Affordability / repayment review", 0)), "Specific human review", "red"),
            card("Data consistency", fmt_int(counts.get("Data consistency check", 0)), "Reconcile before use", "amber"),
            card("Rare but plausible", fmt_int(counts.get("Rare but plausible profile", 0)), "Rarity is not risk", "blue"),
        ], className="metric-grid"),
        html.Div([
            panel("Detector workload", graph(fig_detectors, "standard")),
            panel("Detector overlap", graph(fig_overlap, "standard", min_width=600),
                  "Jaccard accounts for different detector flag rates."),
        ], className="two-col"),
        html.Div([
            panel("Business review drivers", graph(fig_drivers, "tall")),
            panel("Review workload by segment", graph(fig_review_segment, "tall")),
        ], className="two-col"),
        panel("Consensus in PCA space", graph(fig_anomaly_pca, "map"),
              "All consensus rows are retained; non-consensus rows are downsampled.", wide=True),
        panel("Applicant review queue", html.Div([
            html.P("Filter or sort, then select a row to read its full evidence and action.", className="table-instruction"),
            html.Div(anomaly_table_component(), className="table-shell"),
            html.Div("Select a row to inspect the record-specific evidence.", id="anomaly-detail", className="record-detail"),
        ]), "The table pages on the server, so 3,758 detailed records do not block initial rendering.", wide=True),
    ], className="tab-section")


def outcome_layout() -> html.Section:
    ref_precision = metric("precision", reference_metrics)
    ref_recall = metric("recall", reference_metrics)
    return html.Section([
        heading("05 · OUTCOME DIAGNOSTIC", "Low cluster precision is an objective mismatch",
                "Cluster rates test outcome alignment. A separate train-only logistic diagnostic shows what changes when TARGET is the actual objective."),
        html.Div([
            card("Cluster precision", fmt_pct(metric("precision"), 2), "Whole-segment flag", "red"),
            card("Cluster recall", fmt_pct(metric("recall"), 2), "Whole-segment flag", "blue"),
            card("Cluster ceiling", fmt_pct(metric("cluster_precision_ceiling"), 2), "Best complete segment", "amber"),
            card("Supervised diagnostic", f"{fmt_pct(ref_precision, 1)} / {fmt_pct(ref_recall, 1)}", "Precision / recall at same capacity", "green"),
        ], className="metric-grid"),
        panel("Objective-matched comparison", graph(fig_objective, "standard"),
              "The logistic result diagnoses available applicant-level signal; it is not deployment validation.", wide=True),
        html.Div([
            panel("Observed segment rates", graph(fig_rates, "standard")),
            panel("Cluster-flag errors", graph(fig_cm, "standard")),
        ], className="two-col"),
        panel("Cluster threshold trade-off", graph(fig_policy, "standard"),
              "Changing the cutoff trades workload and recall; it cannot create within-segment ranking.", wide=True),
        html.Div([
            html.Strong("Governance boundary"),
            html.Span("Neither result may approve, decline, price, or explain an individual decision without temporal validation, calibration, fairness/proxy testing, policy review, and monitored human outcomes."),
        ], className="guardrail"),
    ], className="tab-section")


TAB_BUILDERS = {
    "overview": overview_layout,
    "segments": segments_layout,
    "rules": rules_layout,
    "anomalies": anomalies_layout,
    "outcome": outcome_layout,
}


app = Dash(
    __name__,
    title="Home Credit Portfolio Discovery",
    assets_folder=str(ROOT / "dashboard/assets"),
    suppress_callback_exceptions=True,
)
server = app.server

app.layout = html.Div([
    html.Header([
        html.Div([
            html.Div("HOME CREDIT · DOMAIN-LED KDD", className="eyebrow"),
            html.H1("Portfolio discovery with explicit decision boundaries"),
            html.P("Segments, non-trivial associations, anomaly review, and an honest TARGET diagnostic."),
        ]),
        html.Div([
            html.Span("356,255 discovery rows"),
            html.Span("307,511 labeled rows"),
            html.Span("0 test labels invented"),
        ], className="scope-badges"),
    ], className="hero"),
    dcc.Tabs(
        id="phase-tabs",
        value="overview",
        className="phase-tabs",
        parent_className="tabs-shell",
        children=[
            dcc.Tab(label="Overview", value="overview", className="phase-tab", selected_className="phase-tab selected"),
            dcc.Tab(label="Segments", value="segments", className="phase-tab", selected_className="phase-tab selected"),
            dcc.Tab(label="Rules", value="rules", className="phase-tab", selected_className="phase-tab selected"),
            dcc.Tab(label="Anomalies", value="anomalies", className="phase-tab", selected_className="phase-tab selected"),
            dcc.Tab(label="Outcome", value="outcome", className="phase-tab", selected_className="phase-tab selected"),
        ],
    ),
    dcc.Store(id="tab-scroll-signal"),
    html.Main(id="tab-content", className="phase-content"),
    html.Footer([
        html.Span("Detailed reasoning: REPORT.md and reports/reasoning_validation.md"),
        html.Span("All visible results come from executed notebook artifacts"),
    ]),
], className="app-shell")


@app.callback(Output("tab-content", "children"), Input("phase-tabs", "value"))
def render_tab(value: str):
    return TAB_BUILDERS.get(value, overview_layout)()


app.clientside_callback(
    """
    function(value) {
        window.requestAnimationFrame(function() {
            const content = document.getElementById('tab-content');
            const tabs = document.querySelector('.tabs-shell');
            if (content) {
                const offset = tabs ? tabs.offsetHeight : 0;
                const top = content.getBoundingClientRect().top + window.scrollY - offset;
                window.scrollTo({top: Math.max(0, top), behavior: 'auto'});
            }
        });
        return Date.now();
    }
    """,
    Output("tab-scroll-signal", "data"),
    Input("phase-tabs", "value"),
    prevent_initial_call=True,
)


FILTER_OPERATORS = [
    (" ge ", ">="), (" le ", "<="), (" lt ", "<"), (" gt ", ">"),
    (" ne ", "!="), (" eq ", "="),
    (" scontains ", "contains"), (" contains ", "contains"),
]


def split_filter_part(filter_part: str):
    for token, operator in FILTER_OPERATORS:
        if token not in filter_part:
            continue
        name_part, value_part = filter_part.split(token, 1)
        column = name_part[name_part.find("{") + 1:name_part.rfind("}")]
        value_part = value_part.strip()
        if value_part and value_part[0] in {'"', "'", "`"}:
            value = value_part[1:-1].replace("\\" + value_part[0], value_part[0])
        else:
            try:
                value = float(value_part)
            except ValueError:
                value = value_part
        return column, operator, value
    return None, None, None


@app.callback(
    Output("anomaly-table", "data"),
    Output("anomaly-table", "page_count"),
    Input("anomaly-table", "page_current"),
    Input("anomaly-table", "page_size"),
    Input("anomaly-table", "sort_by"),
    Input("anomaly-table", "filter_query"),
    prevent_initial_call=False,
)
def update_anomaly_table(page_current, page_size, sort_by, filter_query):
    frame = anomaly_investigation.copy()
    for filter_part in (filter_query or "").split(" && "):
        column, operator, value = split_filter_part(filter_part)
        if not column or column not in frame.columns:
            continue
        series = frame[column]
        if operator == "contains":
            frame = frame[series.astype(str).str.contains(str(value), case=False, na=False)]
        elif operator == "=":
            frame = frame[series == value]
        elif operator == "!=":
            frame = frame[series != value]
        elif operator == ">=":
            frame = frame[series >= value]
        elif operator == "<=":
            frame = frame[series <= value]
        elif operator == "<":
            frame = frame[series < value]
        elif operator == ">":
            frame = frame[series > value]
    if sort_by:
        frame = frame.sort_values(
            [item["column_id"] for item in sort_by],
            ascending=[item["direction"] == "asc" for item in sort_by],
            kind="mergesort",
        )
    page_size = int(page_size or 10)
    page_current = min(int(page_current or 0), max(0, math.ceil(len(frame) / page_size) - 1))
    return anomaly_page(frame, page_current, page_size), max(1, math.ceil(len(frame) / page_size))


@app.callback(
    Output("anomaly-detail", "children"),
    Input("anomaly-table", "active_cell"),
    State("anomaly-table", "data"),
    prevent_initial_call=True,
)
def show_anomaly_detail(active_cell, page_data):
    if not active_cell or not page_data:
        return "Select a row to inspect the record-specific evidence."
    record_id = page_data[active_cell["row"]]["SK_ID_CURR"]
    row = anomaly_investigation.loc[anomaly_investigation.SK_ID_CURR.eq(record_id)].iloc[0]
    return html.Div([
        html.Div([
            html.Span(f"Applicant {int(row.SK_ID_CURR):,}", className="record-id"),
            html.Span(row["Priority"], className="record-priority"),
        ], className="record-head"),
        html.Div([html.Strong("Evidence"), html.P(row["Record Evidence"])]),
        html.Div([html.Strong("Business meaning"), html.P(row["Business Interpretation"])]),
        html.Div([html.Strong("Recommended human action"), html.P(row["Recommended Action"])]),
        html.Div([html.Strong("Owner"), html.P(row["Review Owner"])]),
        html.Div("Automatic decision allowed: No", className="no-auto"),
    ])


if __name__ == "__main__":
    app.run(
        host=os.getenv("DASH_HOST", "127.0.0.1"),
        port=int(os.getenv("DASH_PORT", "8050")),
        debug=False,
    )

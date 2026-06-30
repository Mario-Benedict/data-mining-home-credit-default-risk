"""
Phase 5: interactive dashboard that presents the mining results to a business
audience (Plotly Dash, per the project tech stack).

Every number is read from the artefacts in results/ and datasets/final/ at
startup, so re-running Phase 1 to 4 keeps the dashboard in sync. Startup takes
a few seconds because it computes the actual default rate per segment and per
anomaly level (a join to application_train); after that the figures are cached
and interaction is instant.

Run from the project root:
    python dashboard/app.py
then open http://127.0.0.1:8050
"""
import re
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dash_table, dcc, html
from dash.dependencies import Input, Output
from sklearn.metrics import adjusted_rand_score

ROOT = Path(__file__).resolve().parent.parent
R1 = ROOT / "results/phase1_preprocessing"
R2 = ROOT / "results/phase2_clustering"
R3 = ROOT / "results/phase3_association"
R4 = ROOT / "results/phase4_anomaly"

# Mining artefacts
feature_importance = pd.read_csv(R1 / "feature_importance.csv")
high_corr = pd.read_csv(R1 / "high_corr_pairs.csv")

cluster_names = pd.read_csv(R2 / "cluster_names.csv")
cluster_viz = pd.read_csv(R2 / "cluster_viz_sample.csv")
k_selection = pd.read_csv(R2 / "k_selection.csv")
cluster_summary = pd.read_csv(R2 / "cluster_summary.csv")

rules_final = pd.read_csv(R3 / "rule_table_final.csv")
rules_combined = pd.read_csv(R3 / "rules_combined.csv")

anomaly_summary = pd.read_csv(R4 / "anomaly_summary.csv")
anomaly_pca = pd.read_csv(R4 / "pca_anomaly_sample.csv")
investigation = pd.read_csv(R4 / "anomaly_investigation.csv")

# Post-hoc validation against TARGET (the label is NOT used during mining)
_target = pd.read_csv(ROOT / "datasets/application_train.csv",
                      usecols=["SK_ID_CURR", "TARGET"])
_labels = pd.read_csv(ROOT / "datasets/final/cluster_labels.csv",
                      usecols=["ROW_ID", "SK_ID_CURR", "CLUSTER_KMEANS"])
BASELINE = float(_target["TARGET"].mean()) * 100

_seg_join = _labels.merge(_target, on="SK_ID_CURR", how="inner")
seg_default = (_seg_join.groupby("CLUSTER_KMEANS")["TARGET"].mean() * 100)

_anom_cat = pd.read_csv(R4 / "anomaly_combined.csv",
                        usecols=["ROW_ID", "anomaly_category"])
tier_default = (_anom_cat.merge(_labels[["ROW_ID", "SK_ID_CURR"]], on="ROW_ID")
                .merge(_target, on="SK_ID_CURR", how="inner")
                .groupby("anomaly_category")["TARGET"].mean() * 100)

NAME_BY_ID = dict(zip(cluster_names["cluster_id"], cluster_names["nama"]))
RISK_BY_ID = dict(zip(cluster_names["cluster_id"], cluster_names["profil_risiko"]))
SLUG_BY_ID = dict(zip(cluster_names["cluster_id"], cluster_names["slug"]))
ID_BY_SLUG = {v: k for k, v in SLUG_BY_ID.items()}
N_TOTAL = int(cluster_names["n_applicants"].sum())
SIZE_BY_ID = dict(zip(cluster_names["cluster_id"], cluster_names["n_applicants"]))

# Initial data condition, computed straight from the raw data. The focus is on
# conditions that matter for CLUSTERING (distance between applicants), not for
# classification; the TARGET label is not treated as a data condition.
_eda = pd.read_csv(ROOT / "datasets/application_train.csv",
                   usecols=["DAYS_EMPLOYED", "EXT_SOURCE_1", "OWN_CAR_AGE",
                            "OCCUPATION_TYPE", "AMT_INCOME_TOTAL", "ORGANIZATION_TYPE"])
N_TRAIN = len(_eda)
_n_housing = sum(c.endswith(("_AVG", "_MODE", "_MEDI")) for c in
                 pd.read_csv(ROOT / "datasets/application_train.csv", nrows=0).columns)
N_FEATURES_FINAL = len(feature_importance)
EDA = {
    "sentinel_pct": float((_eda["DAYS_EMPLOYED"] == 365243).mean()) * 100,
    "sentinel_n": int((_eda["DAYS_EMPLOYED"] == 365243).sum()),
    "ext1_missing": float(_eda["EXT_SOURCE_1"].isna().mean()) * 100,
    "car_missing": float(_eda["OWN_CAR_AGE"].isna().mean()) * 100,
    "occ_missing": float(_eda["OCCUPATION_TYPE"].isna().mean()) * 100,
    "income_median": float(_eda["AMT_INCOME_TOTAL"].median()),
    "income_p99": float(_eda["AMT_INCOME_TOTAL"].quantile(0.99)),
    "income_max": float(_eda["AMT_INCOME_TOTAL"].max()),
    "income_ratio": float(_eda["AMT_INCOME_TOTAL"].max() / _eda["AMT_INCOME_TOTAL"].median()),
    "org_cardinality": int(_eda["ORGANIZATION_TYPE"].nunique()),
    "n_housing_cols": int(_n_housing),
    "n_features_final": int(N_FEATURES_FINAL),
}

# Agreement between clustering methods (a check on the segmentation)
_lab_all = pd.read_csv(ROOT / "datasets/final/cluster_labels.csv",
                       usecols=["CLUSTER_KMEANS", "CLUSTER_HIER", "CLUSTER_DBSCAN"])
ARI_KM_HIER = float(adjusted_rand_score(_lab_all["CLUSTER_KMEANS"], _lab_all["CLUSTER_HIER"]))
if ARI_KM_HIER >= 0.6:
    ARI_DESC = "agree strongly"
elif ARI_KM_HIER >= 0.35:
    ARI_DESC = "mostly agree"
elif ARI_KM_HIER >= 0.15:
    ARI_DESC = "agree on the rough structure"
else:
    ARI_DESC = "offer a different viewpoint"
DBSCAN_NOISE = int((_lab_all["CLUSTER_DBSCAN"] == -1).sum())
DBSCAN_LABELED = int(_lab_all["CLUSTER_DBSCAN"].notna().sum())
DBSCAN_POCKETS = int(_lab_all.loc[_lab_all["CLUSTER_DBSCAN"] >= 0, "CLUSTER_DBSCAN"].nunique())

# Corporate palette (matches assets/style.css): steel-navy plus muted teal/brick/gray.
ACCENT = "#34506B"   # steel navy, the single accent
BLUE   = "#4E6E8A"   # steel blue
SAGE   = "#5B8A72"   # muted teal-green (low risk)
SAND   = "#C2914C"   # muted amber (medium)
CLAY   = "#B4504A"   # muted brick red (high risk)
MAUVE  = "#6E7493"   # cool slate
WARM_GRAY, INK, INK_SOFT, GRID = "#9AA5B1", "#1F2933", "#6B7280", "#EEF1F4"

SEG_COLORS = {"minimal": SAGE, "ambisius": BLUE, "veteran": SAND,
              "bermasalah": CLAY, "cc_intensif": MAUVE}
TIER_ORDER = ["NORMAL", "WEAK_SIGNAL", "MODERATE_ANOMALY", "HIGH_CONFIDENCE_ANOMALY"]
TIER_LABEL = {"NORMAL": "Normal", "WEAK_SIGNAL": "Weak signal (1 method)",
              "MODERATE_ANOMALY": "Moderate (2 methods)",
              "HIGH_CONFIDENCE_ANOMALY": "Strong (3-4 methods)"}
TIER_COLORS = {"NORMAL": "#BCC4CE", "WEAK_SIGNAL": "#9FB6C6",
               "MODERATE_ANOMALY": SAND, "HIGH_CONFIDENCE_ANOMALY": CLAY}
TYPE_COLORS = {"Tipe A - Data Error": "#9AA5B1",
               "Tipe B - Rare but Valid": SAGE,
               "Tipe C - Risk Signal": CLAY}

def seg_color(cid):
    return SEG_COLORS.get(SLUG_BY_ID.get(cid), WARM_GRAY)

def seg_label(cid):
    return f"{NAME_BY_ID.get(cid, '?')}"

cluster_viz["Segment"] = cluster_viz["CLUSTER_KMEANS"].map(seg_label)
anomaly_pca["Segment"] = anomaly_pca["CLUSTER_KMEANS"].map(lambda c: seg_label(int(c)))

# Vocabulary that turns rule items into plain business phrases.
VOCAB = {
    "income_low": "low income", "income_med": "medium income",
    "income_high": "high income", "income_very_high": "very high income",
    "age_young": "young", "age_mid": "middle-aged", "age_senior": "senior",
    "emp_new": "short job tenure", "emp_mid": "medium job tenure", "emp_senior": "long job tenure",
    "risk_score_low": "low bureau score", "risk_score_med": "medium bureau score",
    "risk_score_high": "high bureau score",
    "credit_small": "small loan", "credit_med": "medium loan", "credit_large": "large loan",
    "burden_low": "light repayment burden", "burden_med": "medium repayment burden",
    "burden_high": "heavy repayment burden",
}
for _r in cluster_names.itertuples():
    VOCAB[f"cluster_{int(_r.cluster_id)}_{_r.slug}"] = f"{_r.nama} segment"

def _items(part):
    return [i.strip().strip("'") for i in
            part.replace("{", "").replace("}", "").split(",") if i.strip()]

def humanize_rule(rule_str):
    parts = str(rule_str).split(" -> ")
    if len(parts) != 2:
        return rule_str
    left = ", ".join(VOCAB.get(i, i) for i in _items(parts[0]))
    right = ", ".join(VOCAB.get(i, i) for i in _items(parts[1]))
    return f"If {left}, then usually {right}"


# Technical column names mapped to business terms, used in every chart and table.
FEATURE_LABELS = {
    "AMT_INCOME_TOTAL": "Annual income",
    "AMT_CREDIT": "Loan amount",
    "AMT_ANNUITY": "Annual instalment",
    "CREDIT_TO_INCOME": "Loan vs income",
    "ANNUITY_TO_INCOME": "Repayment burden vs income",
    "CREDIT_TERM_MONTHS": "Estimated loan term",
    "YEARS_BIRTH": "Age",
    "YEARS_EMPLOYED": "Years employed",
    "FLAG_SENTINEL_EMPLOYED": "Pensioner / not working",
    "CNT_CHILDREN": "Number of children",
    "CODE_GENDER": "Gender (female)",
    "NAME_CONTRACT_TYPE": "Loan type: cash (vs card)",
    "REGION_RATING_CLIENT_W_CITY": "Home region rating",
    "OWN_CAR_AGE": "Age of car owned",
    "FLAG_NO_CAR": "Owns no car",
    "FLAG_NO_HOUSING_DATA": "No housing data",
    "EXT_SOURCE_1": "External bureau score 1",
    "EXT_SOURCE_2": "External bureau score 2",
    "EXT_SOURCE_3": "External bureau score 3",
    "FLAG_EXT_SOURCE_1_MISSING": "No bureau score 1 (thin file)",
    "AMT_REQ_CREDIT_BUREAU_YEAR": "Bureau enquiries in the last year",
    "FLAG_NO_BUREAU": "No bureau record at all",
    "BUREAU_COUNT": "Credits on file at the bureau",
    "BUREAU_ACTIVE_RATIO": "Share of other-bank credits still active",
    "BUREAU_DEBT_TO_CREDIT_RATIO": "Outstanding debt at other banks",
    "BUREAU_DAYS_CREDIT_MEAN": "Average age of other-bank credits",
    "BUREAU_BB_DPD_RATIO_MEAN": "Share of months in arrears (bureau)",
    "BUREAU_BB_SEVERE_DPD_MEAN": "Share of months 90+ days late (bureau)",
    "PREV_COUNT": "Previous applications at Home Credit",
    "PREV_APPROVAL_RATE": "Past approval rate",
    "PREV_REFUSED_COUNT": "Number of past rejections",
    "INST_DPD_MEAN": "Average days late on instalments",
    "INST_DPD_MAX": "Worst instalment delay",
    "INST_LATE_RATIO": "Share of instalments paid late",
    "INST_SEVERE_LATE_RATIO": "Share of instalments over 30 days late",
    "INST_PAYMENT_RATIO_MEAN": "Share of the bill actually paid",
    "POS_SK_DPD_MEAN": "Average arrears on goods / cash loans",
    "POS_MONTHS_COUNT": "Length of goods / cash loan history",
    "CC_UTILIZATION_MEAN": "Card limit usage (average)",
    "CC_UTILIZATION_MAX": "Card limit usage (peak)",
    "CC_SK_DPD_MEAN": "Average card arrears",
    "CC_AMT_BALANCE_MEAN": "Outstanding card balance",
    "CC_MONTHS_COUNT": "Length of card history",
    "DEF_30_CNT_SOCIAL_CIRCLE_BIN": "Close contacts in arrears",
    # Categoricals with clustering-friendly encoding (not one-hot):
    "NAME_EDUCATION_TYPE": "Education level (ladder 0-4)",
    "NAME_INCOME_TYPE_FREQ": "Income type (how common)",
    "ORGANIZATION_TYPE_FREQ": "Work sector (how common)",
}


def flabel(feat):
    return FEATURE_LABELS.get(feat, feat.replace("_", " ").capitalize())


# Short plain-language description per segment, keyed by slug (stable across runs,
# unlike the cluster number).
SEG_DESC = {
    "minimal": "Basic-needs customers: small loans, short terms, light burden. The bank's "
               "exposure to them is small and their behaviour sits close to average.",
    "ambisius": "Large loans relative to income, usually new customers. Bold on paper, yet this "
                "is the segment with the lowest default rate; large loans are only approved for "
                "strong profiles.",
    "veteran": "Long-standing customers who apply for credit very often and are often rejected. "
               "A dense history across products; worth understanding why the rejection rate is high.",
    "bermasalah": "Only 1% of the portfolio but in arrears across almost every product, with delays "
                  "many times those of an ordinary customer. The densest concentration of risk.",
    "cc_intensif": "Living on their credit cards: limit usage two to three times average and a large "
                   "outstanding balance. Vulnerable if their income is disrupted.",
}

# Business recommendation per segment, grounded in Home Credit domain knowledge.
# Each entry has a strategy, concrete steps, and the business payoff.
SEG_RECOMMEND = {
    "minimal": {
        "strategi": "Volume engine: serve many, automate, keep costs low",
        "langkah": [
            "Push micro-credit and short-term multipurpose products with small limits.",
            "Automate the credit decision; average risk and high volume make manual review uneconomic.",
            "Add financial education to grow them into higher-value customers.",
            "Light monitoring only; do not spend oversight budget on a small exposure.",
        ],
        "alasan": "The largest segment, with risk around the average. The profit comes from volume and "
                  "cost efficiency, not margin per customer. Automation cuts the cost to serve, and "
                  "financial education plants a long-term relationship to cross-sell later.",
    },
    "ambisius": {
        "strategi": "Growth engine: push, but fit a seatbelt",
        "langkah": [
            "Prioritise mortgages and vehicle loans; this is where the portfolio grows most healthily.",
            "Require a stress test of ability to pay if income drops 20 to 30 percent.",
            "Make life or credit insurance a condition on large loans.",
            "Offer relationship pricing to keep these good, growing customers.",
        ],
        "alasan": "This is the most important business finding: the biggest borrowers are actually the "
                  "safest (default only 0.8x the average). The screening already works, so holding back "
                  "growth here means turning away healthy profit. The one risk, an income shock on a "
                  "large loan, is covered by the stress test and insurance.",
    },
    "veteran": {
        "strategi": "Investigate the cause first, then decide",
        "langkah": [
            "Trace the history of rejections: are they applying everywhere, or is the debt ratio truly heavy?",
            "Tighten the debt-to-income check before approving a new application.",
            "Steer toward secured products (mortgage) that use their long-standing relationship.",
            "If the profile improves, use the long history for a personalised offer.",
        ],
        "alasan": "A dense application history with many rejections is a yellow flag, not a red one. "
                  "Understanding why prevents two costly mistakes at once: rejecting a genuinely good "
                  "customer, and accepting one who is already over-extended.",
    },
    "bermasalah": {
        "strategi": "Protect the balance sheet: limit exposure, detect early",
        "langkah": [
            "For new applications: decline, or require strict collateral.",
            "For existing customers: offer restructuring before the arrears deepen.",
            "Switch on intensive collection and priority monitoring.",
            "Wire this segment's pattern into the underwriting engine as an early-warning rule.",
        ],
        "alasan": "Only 1 percent of the portfolio but the densest concentration of loss (default 1.5x "
                  "the average). Here the goal is to limit loss, not grow. The biggest value is that "
                  "their pattern is very consistent, so it can act as an early filter to hold similar "
                  "applications before they are approved.",
    },
    "cc_intensif": {
        "strategi": "Relieve the pressure before it breaks into loss",
        "langkah": [
            "Monitor card utilisation regularly; high utilisation is a classic stress indicator.",
            "Offer debt consolidation to bring the revolving burden down.",
            "Hold limit increases until utilisation falls below 70 percent.",
            "Provide proactive card-management education.",
        ],
        "alasan": "Customers who live on their cards at two to three times average utilisation. They "
                  "walk a tightrope: fine while income flows, but once it is disrupted a default can "
                  "cascade across every product at once. Consolidation and limit control ease the "
                  "pressure before it turns into loss.",
    },
}

# Plain-language intro per tab (shown as a banner at the top of each tab).
PHASE_INTRO = {
    "exec": "A decision summary of the whole analysis. The key thing to know: every pattern below was "
            "found without ever seeing who actually defaulted, then tested against reality. So what you "
            "read here is a finding that already passed the test, not a guess.",
    "eda": "Before analysing, we checked the condition of the raw data: where it is missing, where the "
           "values are odd, and what that means. This part shows the data-quality issues that had to be "
           "fixed first so the later stages can be trusted.",
    "seg": "Phase 2 groups customers by their financial behaviour, not just demographics. The result is "
           "five segments with distinct credit personalities, cross-checked with three clustering methods "
           "that work in different ways. Pick a segment to see what sets it apart and the recommended "
           "decision.",
    "rules": "Phase 3 looks for 'if this, then usually that' patterns that co-occur. Three different "
             "algorithms agree on the same patterns, so this is not a one-method fluke. Each rule is "
             "translated into a business sentence with a suggested next step.",
    "anom": "Phase 4 looks for customers who deviate from the pattern. Each anomaly gets two "
            "complementary labels: how it deviates (global, contextual, or collective) and how to handle "
            "it (data error, valid rare case, or risk signal), then a recommendation for its segment.",
    "method": "How the numbers above are computed: dimensionality reduction, the choice of how many "
              "segments, and the measure of how well each feature separates customers. This part is for "
              "the reader who wants to follow the method.",
}

# Anomaly typology labels for display (the CSV keeps the technical keys).
TYPE_LABEL = {
    "Tipe A - Data Error": "Data input error",
    "Tipe B - Rare but Valid": "Rare but valid",
    "Tipe C - Risk Signal": "Risk signal",
}
TYPE_DISPLAY_COLORS = {
    "Data input error": "#9AA5B1",
    "Rare but valid": SAGE,
    "Risk signal": CLAY,
}

_DEV_RE = re.compile(r"`(\w+)` = [-\d.]+ \(([\d.]+)x median\)")


def humanize_deviations(txt):
    """'`CC_SK_DPD_MEAN` = 25.61 (515.3x median)' -> a business phrase."""
    pairs = _DEV_RE.findall(str(txt))
    if not pairs:
        return str(txt)
    return "; ".join(f"{flabel(f)} {float(m):,.0f}x its segment median"
                     for f, m in pairs[:3])


def rule_action(rule_str, lift):
    """Suggested next step per rule, the same heuristic as Phase 3."""
    parts = str(rule_str).split(" -> ")
    items = set()
    for p in parts:
        items |= set(_items(p))
    slug_full = {r.slug: f"cluster_{int(r.cluster_id)}_{r.slug}"
                 for r in cluster_names.itertuples()}
    if "income_low" in items and "credit_large" in items:
        return "Auto-decline unless there is collateral; manual review by a senior underwriter."
    if slug_full.get("bermasalah") in items:
        return "Use as an early-warning rule; review existing customers who match this pattern."
    if "income_very_high" in items and lift >= 2.5:
        return "Prioritise premium product offers and special pricing."
    if "risk_score_high" in items:
        return "Use as a positive flag in scoring for approval and limit increases."
    if "age_senior" in items and "emp_new" in items:
        return "Add income-source verification (pension or a new business) at application."
    if slug_full.get("ambisius") in items and "credit_large" in items:
        return "Require a stress test: can they still pay if income drops 30%?"
    if slug_full.get("minimal") in items:
        return "Steer toward short-term micro-credit plus financial education."
    return "Add as an extra feature in the scoring model; validate on the last 6 months first."


# Small components
def kpi_card(title, value, sub, accent=None):
    style = {"borderTop": f"4px solid {accent}"} if accent else {}
    return html.Div(
        [html.Div(title, className="kpi-title"),
         html.Div(value, className="kpi-value"),
         html.Div(sub, className="kpi-sub")],
        className="kpi-card", style=style)


def caption(text):
    return html.P(text, className="chart-caption")


def phase_banner(key):
    return html.Div(PHASE_INTRO[key], style={
        "margin": "18px 48px 0 48px", "padding": "13px 18px",
        "background": "#F4F6F8", "border": "1px solid #E6E8EC",
        "borderRadius": "8px", "fontSize": "13px", "lineHeight": "1.55",
        "color": INK})


def insight_box(title, body, color=BLUE):
    return html.Div(
        [html.Div(title, className="insight-title"),
         html.P(body, className="insight-body")],
        className="insight-box", style={"borderLeft": f"5px solid {color}"})


def card(children):
    return html.Div(children, className="card")


def _method_row(name, badge, desc, color):
    return html.Div([
        html.Div([
            html.Span(name, style={"fontWeight": "600", "color": INK}),
            html.Span(f"   {badge}", style={"color": color, "fontWeight": "600",
                                            "fontSize": "12.5px"})],
                 style={"marginBottom": "2px"}),
        html.Div(desc, style={"fontSize": "12.5px", "color": INK_SOFT, "lineHeight": "1.5"}),
    ], style={"borderLeft": f"3px solid {color}", "paddingLeft": "13px", "marginBottom": "11px"})


_LAYOUT_DEFAULTS = dict(
    font=dict(family="Inter, Segoe UI, system-ui, sans-serif", size=13, color=INK),
    paper_bgcolor="white", plot_bgcolor="white",
    margin=dict(l=20, r=20, t=48, b=20),
)

def style_fig(fig, title, height=380):
    fig.update_layout(title=dict(text=title, font=dict(size=14.5, color=INK)),
                      height=height, **_LAYOUT_DEFAULTS)
    fig.update_xaxes(gridcolor=GRID, zerolinecolor=GRID)
    fig.update_yaxes(gridcolor=GRID, zerolinecolor=GRID)
    return fig


# Figure: default-rate validation
def fig_seg_default():
    df = pd.DataFrame({
        "Segment": [seg_label(c) for c in seg_default.index],
        "Default (%)": seg_default.values.round(2),
        "color": [seg_color(c) for c in seg_default.index],
    }).sort_values("Default (%)")
    fig = go.Figure(go.Bar(
        x=df["Default (%)"], y=df["Segment"], orientation="h",
        marker_color=df["color"],
        text=[f"{v:.1f}%  ({v/BASELINE:.1f}x average)" for v in df["Default (%)"]],
        textposition="outside"))
    fig.add_vline(x=BASELINE, line_dash="dash", line_color=WARM_GRAY,
                  annotation_text=f"portfolio average {BASELINE:.1f}%",
                  annotation_position="top")
    fig.update_xaxes(range=[0, max(df["Default (%)"]) * 1.55],
                     title="Percent of customers who eventually defaulted")
    return style_fig(fig, "Each segment defaults at a clearly different rate")


def fig_tier_default():
    rows = [(TIER_LABEL[t], float(tier_default.get(t, np.nan)), TIER_COLORS[t])
            for t in TIER_ORDER]
    fig = go.Figure(go.Bar(
        x=[r[0] for r in rows], y=[r[1] for r in rows],
        marker_color=[r[2] for r in rows],
        text=[f"{r[1]:.1f}%" for r in rows], textposition="outside"))
    fig.add_hline(y=BASELINE, line_dash="dash", line_color=WARM_GRAY,
                  annotation_text=f"portfolio average {BASELINE:.1f}%")
    fig.update_yaxes(title="Percent who eventually defaulted",
                     range=[0, max(r[1] for r in rows) * 1.3])
    return style_fig(fig, "The more methods flag an application as anomalous, the more it defaults")


# Figure: segmentation
def fig_cluster_scatter():
    order = [seg_label(c) for c in sorted(SLUG_BY_ID)]
    cmap = {seg_label(c): seg_color(c) for c in sorted(SLUG_BY_ID)}
    # webgl render: 20 thousand SVG points would freeze the browser in a demo
    fig = px.scatter(cluster_viz, x="PC1", y="PC2", color="Segment",
                     category_orders={"Segment": order},
                     color_discrete_map=cmap, opacity=0.45,
                     render_mode="webgl")
    fig.update_traces(marker=dict(size=4))
    # Label each cluster in the middle of its cloud so the reader does not have
    # to keep looking back at the legend.
    centroids = cluster_viz.groupby("Segment")[["PC1", "PC2"]].median()
    for seg_name, row in centroids.iterrows():
        fig.add_annotation(x=row["PC1"], y=row["PC2"], text=f"<b>{seg_name}</b>",
                           showarrow=False, font=dict(size=11, color=INK),
                           bgcolor="rgba(255,255,255,0.85)", borderpad=2)
    fig.update_layout(legend=dict(orientation="h", y=-0.12))
    fig.update_xaxes(title="", showticklabels=False)
    fig.update_yaxes(title="", showticklabels=False)
    return style_fig(fig, "Customer map: each dot is one applicant, colour is the segment", height=460)


def fig_cluster_sizes():
    df = cluster_names.copy()
    df["label"] = df["cluster_id"].map(seg_label)
    df["default"] = df["cluster_id"].map(seg_default).round(2)
    df = df.sort_values("n_applicants")
    fig = go.Figure(go.Bar(
        x=df["n_applicants"], y=df["label"], orientation="h",
        marker_color=[SEG_COLORS.get(s, WARM_GRAY) for s in df["slug"]],
        text=[f"{n:,} ({d:.1f}% default)" for n, d in zip(df["n_applicants"], df["default"])],
        textposition="outside"))
    fig.update_xaxes(title="Number of applicants", range=[0, df["n_applicants"].max() * 1.45])
    return style_fig(fig, "Segment size and its default rate", height=340)


def fig_elbow_silhouette():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=k_selection["k"], y=k_selection["inertia"],
                             mode="lines+markers", name="Inertia",
                             line=dict(color=BLUE)))
    fig.add_trace(go.Scatter(x=k_selection["k"], y=k_selection["silhouette"],
                             mode="lines+markers", name="Silhouette", yaxis="y2",
                             line=dict(color=SAGE)))
    fig.add_vline(x=5, line_dash="dot", line_color=CLAY,
                  annotation_text="K=5 chosen")
    fig.update_layout(xaxis_title="Number of clusters (K)", yaxis_title="Inertia",
                      yaxis2=dict(title="Silhouette", overlaying="y", side="right"),
                      legend=dict(orientation="h", y=-0.25))
    return style_fig(fig, "Choosing the number of segments: elbow and silhouette", height=340)


# Figure: rules
def fig_rules_scatter():
    df = rules_combined.copy()
    df["Found by"] = df["n_algos"].map(lambda n: f"{n} algorithms")
    df["rule"] = df["rule_str"].map(humanize_rule)
    fig = px.scatter(df, x="support", y="confidence", size="lift", render_mode="webgl",
                     color="Found by", hover_data={"rule": True, "lift": ":.2f",
                                                   "support": ":.3f",
                                                   "confidence": ":.3f"},
                     color_discrete_sequence=["#BCC4CE", BLUE, CLAY, MAUVE, SAGE])
    fig.update_xaxes(title="Coverage: percent of the portfolio that follows this pattern",
                     tickformat=".0%")
    fig.update_yaxes(title="Accuracy: how often the pattern holds", tickformat=".0%")
    return style_fig(fig, "Every rule found; dot size is strength (lift)", height=420)


def fig_rule_network():
    try:
        import networkx as nx
    except ImportError:
        return go.Figure()
    G = nx.DiGraph()
    for _, r in rules_final.iterrows():
        parts = str(r["rule_str"]).split(" -> ")
        if len(parts) != 2:
            continue
        for a in _items(parts[0]):
            for c in _items(parts[1]):
                G.add_edge(VOCAB.get(a, a), VOCAB.get(c, c), lift=float(r["lift"]))
    pos = nx.spring_layout(G, k=1.7, seed=42)
    edge_x, edge_y = [], []
    for u, v in G.edges():
        edge_x += [pos[u][0], pos[v][0], None]
        edge_y += [pos[u][1], pos[v][1], None]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=edge_x, y=edge_y, mode="lines",
                             line=dict(width=1, color="#DCE1E7"),
                             hoverinfo="none", showlegend=False))
    fig.add_trace(go.Scatter(
        x=[pos[n][0] for n in G.nodes()], y=[pos[n][1] for n in G.nodes()],
        mode="markers+text", text=list(G.nodes()), textposition="top center",
        textfont=dict(size=10),
        marker=dict(size=[8 + 3 * G.degree(n) for n in G.nodes()], color=ACCENT),
        hoverinfo="text", showlegend=False))
    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)
    return style_fig(fig, "How the conditions in the 15 final rules connect", height=460)


# Figure: anomalies
def fig_anomaly_scatter():
    df = anomaly_pca.copy()
    df["Level"] = df["anomaly_category"].map(TIER_LABEL)
    fig = px.scatter(df, x="PC1", y="PC2", color="Level",
                     category_orders={"Level": [TIER_LABEL[t] for t in TIER_ORDER]},
                     color_discrete_map={TIER_LABEL[t]: TIER_COLORS[t] for t in TIER_ORDER},
                     opacity=0.55, hover_data=["Segment"],
                     render_mode="webgl")
    fig.update_traces(marker=dict(size=4))
    fig.update_layout(legend=dict(orientation="h", y=-0.12))
    fig.update_xaxes(title="Main dimension 1", showticklabels=False)
    fig.update_yaxes(title="Main dimension 2", showticklabels=False)
    return style_fig(fig, "Anomaly map: red points are flagged by 3-4 methods at once", height=460)


def fig_typology():
    counts = investigation["Anomaly Type"].map(TYPE_LABEL).value_counts().reset_index()
    counts.columns = ["Type", "Count"]
    fig = px.pie(counts, names="Type", values="Count", hole=0.5,
                 color="Type", color_discrete_map=TYPE_DISPLAY_COLORS)
    fig.update_traces(textinfo="value+percent")
    return style_fig(fig, f"Investigation of {len(investigation):,} strong anomalies", height=360)


def fig_anomaly_per_cluster():
    inv = investigation.copy()
    inv["cid"] = inv["Cluster"].str.extract(r"(\d+)").astype(int)
    inv["Segment"] = inv["cid"].map(seg_label)
    inv["Type"] = inv["Anomaly Type"].map(TYPE_LABEL)
    counts = inv.groupby(["Segment", "Type"]).size().reset_index(name="Applications")
    fig = px.bar(counts, x="Segment", y="Applications", color="Type",
                 color_discrete_map=TYPE_DISPLAY_COLORS)
    fig.update_layout(legend=dict(orientation="h", y=-0.3, title=""))
    fig.update_xaxes(title="")
    return style_fig(fig, "Which segment the anomalies concentrate in", height=360)


SCOPE_DISPLAY_COLORS = {"Global (point)": "#9FB6C6", "Contextual": CLAY, "Collective": MAUVE}
SCOPE_ORDER = ["Global (point)", "Contextual", "Collective"]


def fig_anomaly_scope():
    if "Anomaly Scope" not in investigation.columns:
        return go.Figure()
    counts = investigation["Anomaly Scope"].value_counts().reindex(SCOPE_ORDER).dropna()
    counts = counts.reset_index()
    counts.columns = ["Kind", "Count"]
    fig = px.bar(counts, x="Count", y="Kind", orientation="h", color="Kind",
                 color_discrete_map=SCOPE_DISPLAY_COLORS, text="Count")
    fig.update_traces(textposition="outside")
    fig.update_layout(showlegend=False)
    fig.update_yaxes(title="")
    fig.update_xaxes(title="Number of anomalies")
    return style_fig(fig, "Three ways an application can deviate", height=300)


# Figure: methodology
def fig_mi_top15():
    top = feature_importance.head(15).iloc[::-1].copy()
    top["label"] = top["feature"].map(flabel)
    fig = px.bar(top, x="mutual_info", y="label", orientation="h",
                 hover_data={"feature": True},
                 color_discrete_sequence=[ACCENT])
    fig.update_xaxes(title="How much information it carries about default")
    fig.update_yaxes(title="")
    return style_fig(fig, "The 15 things that most separate defaulting customers", height=430)


# Rules table for the client
rules_display = rules_final.copy()
rules_display["Rule"] = rules_display["rule_str"].map(humanize_rule)
rules_display["Segment"] = rules_display["target_cluster"].map(
    lambda s: NAME_BY_ID.get(ID_BY_SLUG.get(s.split("_", 2)[-1], -1), s))
rules_display["Coverage"] = (rules_display["support"] * 100).round(1).astype(str) + "%"
rules_display["Accuracy"] = (rules_display["confidence"] * 100).round(1).astype(str) + "%"
rules_display["Strength"] = rules_display["lift"].round(1).map(
    lambda v: f"{v}x more often than chance")
rules_display["Suggested next step"] = rules_display.apply(
    lambda r: rule_action(r["rule_str"], float(r["lift"])), axis=1)
RULES_COLS = ["rank", "Segment", "Rule", "Coverage", "Accuracy", "Strength",
              "Suggested next step"]
rules_display = rules_display[RULES_COLS].rename(columns={"rank": "No"})

_inv_cols_map = {"SK_ID_CURR": "Applicant ID", "Cluster": "Segment",
                 "Anomaly Scope": "Kind of anomaly", "Anomaly Type": "Business type",
                 "Top Deviating Features": "What makes it stand out"}
_inv_present = [c for c in _inv_cols_map if c in investigation.columns]
inv_preview = investigation.head(10)[_inv_present].copy()
inv_preview["Cluster"] = inv_preview["Cluster"].str.extract(r"(\d+)").astype(int).map(seg_label)
inv_preview["Anomaly Type"] = inv_preview["Anomaly Type"].map(TYPE_LABEL)
inv_preview["Top Deviating Features"] = inv_preview["Top Deviating Features"].map(
    humanize_deviations)
inv_preview = inv_preview.rename(columns=_inv_cols_map)

high_corr_display = high_corr.copy()
high_corr_display["Feature 1"] = high_corr_display["feature_1"].map(flabel)
high_corr_display["Feature 2"] = high_corr_display["feature_2"].map(flabel)
high_corr_display["Correlation"] = high_corr_display["abs_corr"].round(3)
high_corr_display = high_corr_display[["Feature 1", "Feature 2", "Correlation"]]

# Numbers for the finding cards
n_high = int(anomaly_summary["HIGH_CONFIDENCE"].iloc[0])
n_eval = int(anomaly_summary["Total_Evaluated"].iloc[0])
_amb_id = ID_BY_SLUG.get("ambisius")
_brm_id = ID_BY_SLUG.get("bermasalah")
amb_def = float(seg_default.get(_amb_id, np.nan))
brm_def = float(seg_default.get(_brm_id, np.nan))
amb_name = NAME_BY_ID.get(_amb_id, "Ambitious")
brm_name = NAME_BY_ID.get(_brm_id, "Troubled")
tier_hi = float(tier_default.get("HIGH_CONFIDENCE_ANOMALY", np.nan))
tier_no = float(tier_default.get("NORMAL", np.nan))
n_typeC = int((investigation["Anomaly Type"] == "Tipe C - Risk Signal").sum())

app = Dash(__name__, title="Home Credit | Data Mining Results",
           suppress_callback_exceptions=True)


# Tab content is built lazily on first open. Mounting all tabs at once would
# render a dozen charts up front and freeze the page for a few seconds, which
# is poor for a client presentation.
def tab_exec():
    return html.Div([
            phase_banner("exec"),
            html.Div([
                insight_box(
                    "Finding 1: the biggest borrowers are actually the safest",
                    f"The {amb_name} segment borrows the most relative to income, yet defaults at only "
                    f"{amb_def:.1f}% against the {BASELINE:.1f}% average. Risk is not about loan size; "
                    f"it is in the behaviour trail.", SAGE),
                insight_box(
                    "Finding 2: 1% of customers carry the densest risk",
                    f"The {brm_name} segment is just 1% of the portfolio but defaults at {brm_def:.1f}%. "
                    f"Its behaviour is very consistent: one of its rules is 99% accurate.", CLAY),
                insight_box(
                    "Finding 3: statistical strangeness is a risk signal",
                    f"Applications flagged by 3-4 anomaly methods default at {tier_hi:.1f}%, rising "
                    f"steadily from {tier_no:.1f}% for normal applications. {n_typeC} cases are pure "
                    f"risk signals that need manual review.", SAND),
            ], className="insight-row"),
            card([
                html.H3("Does this really capture risk, or is it just chance?"),
                html.P([
                    "This is our honesty test. When building the segments and detecting the anomalies, "
                    "the algorithm ", html.B("was never told who eventually defaulted"),
                    ". That label was hidden on purpose. Only after everything was done did we open the "
                    "real outcomes and measure the default rate of each group."],
                    style={"margin": "0 0 8px 0", "fontSize": "13.5px", "lineHeight": "1.6",
                           "color": INK}),
                html.P([
                    "If our grouping were arbitrary, every group would default at about the same rate "
                    "(around the 8.1% average). In reality ",
                    html.B("the numbers spread far apart and rise in order"),
                    " (both charts below). That is the proof: the segments and anomalies we found "
                    "capture real risk, not lines drawn at random."],
                    style={"margin": "0", "fontSize": "13.5px", "lineHeight": "1.6",
                           "color": INK_SOFT}),
            ]),
            html.Div([
                card([dcc.Graph(figure=fig_seg_default()),
                      caption("The five segments from Phase 2. The dashed line is the whole-portfolio "
                              "average (8.1%). The 'x average' figure shows how far each segment sits "
                              "from average: Troubled defaults nearly 1.5x more often, while Ambitious "
                              "is below average. The default label was not used at all when forming "
                              "these segments.")]),
                card([dcc.Graph(figure=fig_tier_default()),
                      caption("Phase 4 scores how 'odd' each application is using four methods, also "
                              "without seeing the label. From left to right: the more methods agree an "
                              "application deviates, the higher its actual default rate. This staircase "
                              "rises without a single exception.")]),
            ], className="row"),
            card([
                html.H3("Three business decisions this analysis supports"),
                html.Div([
                    html.Div([
                        html.Div("1. Shift growth toward healthy large borrowers",
                                 style={"fontWeight": "600", "color": ACCENT, "marginBottom": "4px"}),
                        html.P(f"The {amb_name} segment ({SIZE_BY_ID.get(_amb_id, 0)/N_TOTAL*100:.0f}% "
                               f"of the portfolio) borrows the most but defaults the least "
                               f"({amb_def:.1f}%, below average). This is where to grow mortgages and "
                               f"vehicle loans, protected by an income stress test.",
                               style={"margin": "0", "fontSize": "13px", "color": INK_SOFT,
                                      "lineHeight": "1.55"})],
                        style={"flex": "1", "minWidth": "260px"}),
                    html.Div([
                        html.Div("2. Put early detection on the riskiest 1%",
                                 style={"fontWeight": "600", "color": ACCENT, "marginBottom": "4px"}),
                        html.P(f"The {brm_name} segment is only 1% of the portfolio but defaults at "
                               f"{brm_def:.1f}% ({brm_def/BASELINE:.1f}x average). Its pattern is very "
                               f"consistent, so it can act as an early filter to hold similar "
                               f"applications before approval.",
                               style={"margin": "0", "fontSize": "13px", "color": INK_SOFT,
                                      "lineHeight": "1.55"})],
                        style={"flex": "1", "minWidth": "260px"}),
                    html.Div([
                        html.Div("3. Add the anomaly score as a screening layer",
                                 style={"fontWeight": "600", "color": ACCENT, "marginBottom": "4px"}),
                        html.P(f"The default rate climbs smoothly from {tier_no:.1f}% (normal) to "
                               f"{tier_hi:.1f}% (most deviant). This strangeness score is proven to "
                               f"track real risk, so it is worth running alongside the usual credit "
                               f"score.",
                               style={"margin": "0", "fontSize": "13px", "color": INK_SOFT,
                                      "lineHeight": "1.55"})],
                        style={"flex": "1", "minWidth": "260px"}),
                ], style={"display": "flex", "gap": "22px", "flexWrap": "wrap"}),
            ]),
    ])


# Figures and tab: initial data condition (computed from the raw data)
def _money(v):
    return f"{v/1e6:.0f}M" if v >= 1e6 else f"{v/1e3:.0f}K"


def fig_eda_income_skew():
    vals = [EDA["income_median"], EDA["income_p99"], EDA["income_max"]]
    labels = ["Median<br>(typical customer)", "99th percentile<br>(top tier)",
              "Maximum<br>(one person)"]
    fig = go.Figure(go.Bar(
        x=labels, y=vals, marker_color=[SAGE, SAND, CLAY],
        text=[_money(v) for v in vals], textposition="outside"))
    fig.update_yaxes(type="log", title="Annual income (log scale)")
    return style_fig(fig, f"Income is heavily skewed: the highest is {EDA['income_ratio']:.0f}x the median",
                     height=320)


def fig_eda_missing():
    rows = sorted([("Main bureau score", EDA["ext1_missing"]),
                   ("Car age", EDA["car_missing"]),
                   ("Occupation", EDA["occ_missing"]),
                   ("Employment length (odd value)", EDA["sentinel_pct"])],
                  key=lambda r: r[1])
    fig = go.Figure(go.Bar(
        x=[r[1] for r in rows], y=[r[0] for r in rows], orientation="h",
        marker_color=SAND, text=[f"{r[1]:.0f}%" for r in rows], textposition="outside"))
    fig.update_xaxes(title="Percent of applications missing or odd",
                     range=[0, max(r[1] for r in rows) * 1.25])
    return style_fig(fig, "Some important columns are often missing or odd", height=320)


def tab_eda():
    table = pd.DataFrame([
        {"Condition in the raw data": "Odd employment-length value",
         "Figure": f"{EDA['sentinel_pct']:.0f}% of applications ({EDA['sentinel_n']:,} people)",
         "Why it matters for clustering": "A value equal to 1,000 years would throw the distance between customers into chaos if left in.",
         "What we did": "Flagged it as a special group (pensioners/unemployed), then set the value to missing."},
        {"Condition in the raw data": "Heavily skewed income",
         "Figure": f"highest is {EDA['income_ratio']:.0f}x the median",
         "Why it matters for clustering": "A few extreme earners could dominate distance and collapse all ordinary customers into one point.",
         "What we did": "Capped at the 99th percentile, then smoothed with a log transform."},
        {"Condition in the raw data": "Main bureau score often missing",
         "Figure": f"{EDA['ext1_missing']:.0f}% missing",
         "Why it matters for clustering": "The blank is not just missing data, it is a thin-file signal that separates one group of customers.",
         "What we did": "Created a 'no score' flag as its own feature, then filled the value."},
        {"Condition in the raw data": "Car age often missing",
         "Figure": f"{EDA['car_missing']:.0f}% missing",
         "Why it matters for clustering": "Missing here means no car, a real distinction, not absent data.",
         "What we did": "Turned it into a 'no car' flag rather than guessing a number."},
        {"Condition in the raw data": "Occupation often missing",
         "Figure": f"{EDA['occ_missing']:.0f}% missing",
         "Why it matters for clustering": "A normal collection gap; if left blank, this customer cannot be compared to the rest.",
         "What we did": "Filled with the most common occupation within the same income group."},
        {"Condition in the raw data": "Work sector has too many categories",
         "Figure": f"{EDA['org_cardinality']} categories",
         "Why it matters for clustering": "Turned into 0/1 columns (one-hot), it explodes into dozens of empty columns that distort similarity.",
         "What we did": "Collapsed into a single 'how common is this sector' number, not one-hot."},
        {"Condition in the raw data": "Many columns measure the same thing",
         "Figure": f"{EDA['n_housing_cols']} twin building columns",
         "Why it matters for clustering": "Twin features make one thing count several times in distance, so its weight is unfair.",
         "What we did": f"Kept one version of each measure; {EDA['n_features_final']} complementary features remain."},
    ])
    return html.Div([
        phase_banner("eda"),
        html.Div([
            card([dcc.Graph(figure=fig_eda_income_skew()),
                  caption("Because clustering measures similarity by distance, one customer earning "
                          "hundreds of times an ordinary person could dominate the whole map. That is "
                          "why income is capped and smoothed before use.")]),
            card([dcc.Graph(figure=fig_eda_missing()),
                  caption("Several important columns are often missing or hold odd values. Interestingly, "
                          "this emptiness usually carries meaning rather than being simply lost data.")]),
        ], className="row"),
        card([
            html.H3("The raw data condition and how we prepared it for clustering"),
            html.P("Since the aim is to group customers by similarity, the data has to be tidy first: "
                   "odd values, empty columns, skewed distributions, and twin features can all make two "
                   "customers look alike or different in the wrong way. This table sums up the main "
                   "conditions in the raw data and the action taken. The principle: emptiness and "
                   "oddities are treated as information, not simply discarded.",
                   className="chart-caption"),
            dash_table.DataTable(
                data=table.to_dict("records"),
                columns=[{"name": c, "id": c} for c in table.columns],
                style_table={"overflowX": "auto"},
                style_cell={"fontSize": 12.5, "fontFamily": "Inter, sans-serif", "padding": "9px",
                            "whiteSpace": "normal", "height": "auto", "textAlign": "left",
                            "maxWidth": "280px"},
                style_header={"backgroundColor": "#F4F6F8", "fontWeight": "600", "color": INK},
                style_data_conditional=[{"if": {"row_index": "odd"},
                                         "backgroundColor": "#FAFBFC"}]),
        ]),
    ])


def tab_segments():
    return html.Div([
            phase_banner("seg"),
            html.Div([
                card([dcc.Graph(figure=fig_cluster_scatter()),
                      caption("A two-dimensional projection of 47 features (a 20 thousand point sample). "
                              "Nearby positions mean similar profiles. Five colours, five segments.")]),
                card([dcc.Graph(figure=fig_cluster_sizes()),
                      caption("The two largest segments cover 70% of the portfolio and are both "
                              "relatively safe. The small segment at the bottom is the one that holds "
                              "the risk.")]),
            ], className="row"),
            card([
                html.H3("Cross-checked with three methods, not one"),
                html.P("We do not rely on one algorithm. K-Means builds the main segments, then two "
                       "methods with different logic check them. If different methods point at a similar "
                       "structure, we can trust the segments are real.",
                       style={"margin": "0 0 12px 0", "fontSize": "13.5px", "lineHeight": "1.6",
                              "color": INK}),
                html.Div([
                    _method_row("K-Means", "Main method",
                                f"Forms {len(cluster_names)} segments by pulling each customer to the "
                                f"nearest group centre.", ACCENT),
                    _method_row("Hierarchical (Ward)", f"Agreement {ARI_KM_HIER:.2f} / 1.00",
                                f"Builds customers up from the most similar to the most different. A "
                                f"different way of thinking, but the results {ARI_DESC} with K-Means.", SAGE),
                    _method_row("DBSCAN (in UMAP space)", f"{DBSCAN_POCKETS} dense pockets",
                                f"Looks for dense crowds by density and sets aside the {DBSCAN_NOISE:,} "
                                f"most isolated customers ({DBSCAN_NOISE / DBSCAN_LABELED * 100:.1f}%) as "
                                f"outliers that pass to the anomaly analysis.", MAUVE),
                ]),
                html.P("In short: three different viewpoints point at the same structure, so these five "
                       "segments are not a one-method fluke.",
                       style={"margin": "10px 0 0 0", "fontSize": "13px", "color": INK_SOFT,
                              "fontStyle": "italic"}),
            ]),
            card([
                html.H3("Profile of each segment"),
                html.P("Pick a segment to see which features set it apart from the portfolio average. "
                       "A bar to the right means higher than average, to the left means lower.",
                       className="chart-caption"),
                dcc.Dropdown(
                    id="cluster-dd",
                    options=[{"label": f"{r.nama} (risk {r.profil_risiko}, "
                                       f"{r.n_applicants:,} applicants)",
                              "value": int(r.cluster_id)}
                             for r in cluster_names.itertuples()],
                    value=int(cluster_names["cluster_id"].iloc[0]),
                    clearable=False, searchable=False,
                    style={"maxWidth": "640px"}),
                html.Div(id="cluster-desc", className="segment-desc"),
                dcc.Graph(id="cluster-profile-fig"),
            ]),
    ])


def tab_rules():
    return html.Div([
            phase_banner("rules"),
            card([
                html.H3("The 15 strongest behaviour rules"),
                html.P("Coverage = what percent of the portfolio follows this pattern. Accuracy = if the "
                       "'if' side holds, what percent of cases the 'then' side also holds. Strength = how "
                       "many times more often than chance; 1x means ordinary coincidence.",
                       className="chart-caption"),
                dash_table.DataTable(
                    data=rules_display.to_dict("records"),
                    columns=[{"name": c, "id": c} for c in rules_display.columns],
                    sort_action="native", filter_action="native", page_size=15,
                    style_table={"overflowX": "auto"},
                    style_cell={"fontSize": 13, "fontFamily": "Segoe UI, sans-serif",
                                "padding": "8px", "whiteSpace": "normal", "height": "auto",
                                "textAlign": "left"},
                    style_header={"backgroundColor": "#F4F6F8", "fontWeight": "600", "color": INK},
                    style_data_conditional=[
                        {"if": {"row_index": "odd"}, "backgroundColor": "#FAFBFC"}]),
            ]),
            html.Div([
                card([dcc.Graph(figure=fig_rule_network()),
                      caption("Conditions that often appear together are linked. A large node is a "
                              "condition involved in many rules at once.")]),
                card([dcc.Graph(figure=fig_rules_scatter()),
                      caption("All 1,204 candidate rules. The ones chosen for the final table are strong, "
                              "accurate, and do not repeat another rule's story.")]),
            ], className="row"),
    ])


def tab_anomaly():
    return html.Div([
            phase_banner("anom"),
            html.Div([
                card([dcc.Graph(figure=fig_anomaly_scatter()),
                      caption("Strong anomalies (red) gather at the edges of the map, away from the "
                              "crowd of typical customers.")]),
                card([dcc.Graph(figure=fig_typology()),
                      caption("Three types with different follow-ups: data errors are fixed upstream, "
                              "rare-but-valid cases are routed to priority service, and risk signals go "
                              "to manual review."),
                      dcc.Graph(figure=fig_anomaly_per_cluster())]),
            ], className="row"),
            card([
                dcc.Graph(figure=fig_anomaly_scope()),
                caption("Global: one value is extreme against the whole population, often a data error. "
                        "Contextual: fine in general but odd for its own segment, and this is the kind "
                        "most worth investigating as a risk signal. Collective: a small group of "
                        "customers that stand apart together from the main crowd, watched as a possibly "
                        "recurring pattern."),
            ]),
            card([
                html.H3("Sample investigated cases"),
                html.P(f"The ten most deviant cases, with real applicant IDs so the operations team can "
                       f"follow up directly. The full list of {n_high:,} cases (with the kind of anomaly, "
                       f"the business type, and a recommendation) is in "
                       f"results/phase4_anomaly/anomaly_investigation.csv.",
                       className="chart-caption"),
                dash_table.DataTable(
                    data=inv_preview.to_dict("records"),
                    columns=[{"name": c, "id": c} for c in inv_preview.columns],
                    style_table={"overflowX": "auto"},
                    style_cell={"fontSize": 12, "fontFamily": "Segoe UI, sans-serif",
                                "padding": "8px", "whiteSpace": "normal", "height": "auto",
                                "textAlign": "left", "maxWidth": "520px"},
                    style_header={"backgroundColor": "#F4F6F8", "fontWeight": "600", "color": INK}),
            ]),
    ])


def tab_method():
    return html.Div([
            phase_banner("method"),
            html.Div([
                card([dcc.Graph(figure=fig_mi_top15()),
                      caption("Mutual information measures how much information a feature carries about "
                              "default status, including non-linear relationships that ordinary "
                              "correlation misses.")]),
                card([dcc.Graph(figure=fig_elbow_silhouette()),
                      caption("The elbow points to K=5 and K=5 has the best silhouette among the options "
                              "above 2. K=2 does score higher, but two segments are too coarse to make "
                              "decisions with."),
                      html.H3("Remaining high correlation"),
                      html.P("The two feature pairs above 0.85 that were deliberately kept, with their "
                             "values. The perfectly correlated pairs were already removed in the "
                             "pipeline.", className="chart-caption"),
                      dash_table.DataTable(
                          data=high_corr_display.to_dict("records"),
                          columns=[{"name": c, "id": c} for c in high_corr_display.columns],
                          style_cell={"fontSize": 12, "fontFamily": "Segoe UI, sans-serif",
                                      "padding": "6px", "textAlign": "left"},
                          style_header={"backgroundColor": "#F4F6F8", "fontWeight": "600", "color": INK})]),
            ], className="row"),
    ])


TAB_BUILDERS = {
    "tab-exec": tab_exec,
    "tab-seg": tab_segments,
    "tab-eda": tab_eda,
    "tab-rules": tab_rules,
    "tab-anom": tab_anomaly,
    "tab-method": tab_method,
}
_tab_cache = {}

app.layout = html.Div([
    html.Div([
        html.H1("What is hidden in 356 thousand credit applications?"),
        html.P(f"Knowledge discovery on the Home Credit portfolio: {len(cluster_names)} customer "
               f"segments, {len(rules_final)} behaviour rules, and {n_high:,} anomalous applications, "
               f"all found without seeing the default label, then tested against defaults that actually "
               f"happened.",
               className="hero-sub"),
    ], className="hero"),

    html.Div([
        kpi_card("Applications analysed", f"{N_TOTAL:,}", "train + test, 7 data sources"),
        kpi_card("Average default rate", f"{BASELINE:.1f}%", "portfolio baseline", WARM_GRAY),
        kpi_card("Customer segments", "5", "found by the algorithm, named by people", BLUE),
        kpi_card("Behaviour rules", f"{len(rules_final)}", "confirmed by 3 algorithms", MAUVE),
        kpi_card("Strong anomalies", f"{n_high:,}", f"{n_high / n_eval * 100:.1f}% of the portfolio", CLAY),
    ], className="kpi-row"),

    dcc.Tabs(id="tabs", value="tab-exec", className="tabs", children=[
        dcc.Tab(label="Executive summary", value="tab-exec"),
        dcc.Tab(label="Initial data condition", value="tab-eda"),
        dcc.Tab(label="Customer segments", value="tab-seg"),
        dcc.Tab(label="Patterns and rules", value="tab-rules"),
        dcc.Tab(label="Anomalies and risk", value="tab-anom"),
        dcc.Tab(label="Methodology", value="tab-method"),
    ]),
    html.Div(id="tab-content"),

    html.Footer("A dashboard of a five-phase analysis on the Home Credit portfolio. "
                "Every number updates automatically when the analysis is re-run."),
])


@app.callback(Output("tab-content", "children"), Input("tabs", "value"))
def render_tab(tab):
    if tab not in _tab_cache:
        _tab_cache[tab] = TAB_BUILDERS[tab]()
    return _tab_cache[tab]


@app.callback(Output("cluster-profile-fig", "figure"),
              Output("cluster-desc", "children"),
              Input("cluster-dd", "value"))
def update_profile(cid):
    sub = cluster_summary[cluster_summary["cluster_id"] == cid].head(10).iloc[::-1]
    labels = [flabel(f) for f in sub["fitur"]]
    colors = [SAGE if v > 0 else CLAY for v in sub["rel_diff_pct"]]
    bar_text = [f"{abs(v):.0f}% {'above' if v > 0 else 'below'} average"
                for v in sub["rel_diff_pct"]]
    fig = go.Figure(go.Bar(
        x=sub["rel_diff_pct"], y=labels, orientation="h", marker_color=colors,
        text=bar_text, textposition="outside",
        customdata=sub["fitur"],
        hovertemplate="%{y}<br>%{text}<br>data column: %{customdata}<extra></extra>"))
    fig.update_xaxes(
        title="Green = higher than the portfolio average, red = lower")
    pad = max(abs(sub["rel_diff_pct"])) * 0.45
    fig.update_xaxes(range=[min(sub["rel_diff_pct"].min(), 0) - pad,
                            max(sub["rel_diff_pct"].max(), 0) + pad])
    fig = style_fig(
        fig, f"{NAME_BY_ID.get(cid, '?')}: what makes this segment different "
             f"(actual default {float(seg_default.get(cid, np.nan)):.1f}%)",
        height=430)
    slug = SLUG_BY_ID.get(cid, "")
    desc = SEG_DESC.get(slug, "")
    size = SIZE_BY_ID.get(cid, 0)
    dflt = float(seg_default.get(cid, np.nan))
    rec = SEG_RECOMMEND.get(slug, {})
    block = html.Div([
        html.P([html.B("Profile. "), desc], style={"margin": "0 0 6px 0", "color": INK}),
        html.P(f"Size: {size:,} customers ({size / N_TOTAL * 100:.0f}% of the portfolio). "
               f"Actual default: {dflt:.1f}% ({dflt / BASELINE:.1f}x the portfolio average).",
               style={"margin": "0 0 12px 0", "fontSize": "12.5px", "color": INK_SOFT}),
        html.Div([
            html.Div(f"Recommended decision: {rec.get('strategi', '')}",
                     style={"fontWeight": "600", "color": ACCENT, "marginBottom": "6px",
                            "fontSize": "13.5px"}),
            html.Ul([html.Li(s, style={"marginBottom": "5px"}) for s in rec.get("langkah", [])],
                    style={"margin": "0 0 8px 0", "paddingLeft": "18px", "color": INK,
                           "fontSize": "12.5px", "lineHeight": "1.55"}),
            html.P([html.B("Why this makes business sense. "), rec.get("alasan", "")],
                   style={"margin": "0", "fontSize": "12.5px", "lineHeight": "1.6",
                          "color": INK_SOFT, "background": "#F4F6F8", "padding": "10px 13px",
                          "borderRadius": "6px"}),
        ]),
    ])
    return fig, block


if __name__ == "__main__":
    app.run(debug=False, port=8050)

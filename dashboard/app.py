"""
Phase 5: dashboard interaktif untuk presentasi hasil mining ke klien bisnis.

Tech stack mengikuti dokumen proyek (Plotly Dash). Semua angka dibaca dari
artefak results/ dan datasets/final/ saat startup; tidak ada angka yang
ditulis tangan, jadi menjalankan ulang Phase 1-4 otomatis menyinkronkan
seluruh isi dashboard.

Catatan performa: startup butuh beberapa detik karena menghitung default
rate aktual per segmen dan per tingkat anomali (join ke application_train).
Setelah itu semua figure sudah jadi di memori dan interaksi berjalan instan.

Jalankan dari project root:
    python dashboard/app.py
lalu buka http://127.0.0.1:8050
"""
import re
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dash_table, dcc, html
from dash.dependencies import Input, Output

ROOT = Path(__file__).resolve().parent.parent
R1 = ROOT / "results/phase1_preprocessing"
R2 = ROOT / "results/phase2_clustering"
R3 = ROOT / "results/phase3_association"
R4 = ROOT / "results/phase4_anomaly"

# ── Artefak hasil mining ───────────────────────────────────────────────────
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

# ── Validasi post-hoc terhadap TARGET (label TIDAK dipakai saat mining) ────
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

# Palet korporat (selaras dengan assets/style.css): steel-navy + muted teal/brick/gray.
# Nama variabel dipertahankan; hanya nilainya yang profesional & desaturated.
ACCENT = "#34506B"   # steel navy — aksen tunggal
BLUE   = "#4E6E8A"   # steel blue
SAGE   = "#5B8A72"   # muted teal-green (risiko rendah)
SAND   = "#C2914C"   # muted amber (sedang)
CLAY   = "#B4504A"   # muted brick red (risiko tinggi)
MAUVE  = "#6E7493"   # cool slate
WARM_GRAY, INK, INK_SOFT, GRID = "#9AA5B1", "#1F2933", "#6B7280", "#EEF1F4"

SEG_COLORS = {"minimal": SAGE, "ambisius": BLUE, "veteran": SAND,
              "bermasalah": CLAY, "cc_intensif": MAUVE}
TIER_ORDER = ["NORMAL", "WEAK_SIGNAL", "MODERATE_ANOMALY", "HIGH_CONFIDENCE_ANOMALY"]
TIER_LABEL = {"NORMAL": "Normal", "WEAK_SIGNAL": "Sinyal lemah (1 metode)",
              "MODERATE_ANOMALY": "Moderat (2 metode)",
              "HIGH_CONFIDENCE_ANOMALY": "Kuat (3-4 metode)"}
TIER_COLORS = {"NORMAL": "#BCC4CE", "WEAK_SIGNAL": "#9FB6C6",
               "MODERATE_ANOMALY": SAND, "HIGH_CONFIDENCE_ANOMALY": CLAY}
TYPE_COLORS = {"Tipe A - Data Error": "#9AA5B1",
               "Tipe B - Rare but Valid": SAGE,
               "Tipe C - Risk Signal": CLAY}

def seg_color(cid):
    return SEG_COLORS.get(SLUG_BY_ID.get(cid), WARM_GRAY)

def seg_label(cid):
    return f"{NAME_BY_ID.get(cid, '?')}"

cluster_viz["Segmen"] = cluster_viz["CLUSTER_KMEANS"].map(seg_label)
anomaly_pca["Segmen"] = anomaly_pca["CLUSTER_KMEANS"].map(lambda c: seg_label(int(c)))

# ── Kosakata untuk menerjemahkan rule ke kalimat bisnis ────────────────────
VOCAB = {
    "income_low": "pendapatan rendah", "income_med": "pendapatan menengah",
    "income_high": "pendapatan tinggi", "income_very_high": "pendapatan sangat tinggi",
    "age_young": "usia muda", "age_mid": "usia menengah", "age_senior": "usia senior",
    "emp_new": "masa kerja baru", "emp_mid": "masa kerja menengah", "emp_senior": "masa kerja lama",
    "risk_score_low": "skor biro kredit rendah", "risk_score_med": "skor biro kredit menengah",
    "risk_score_high": "skor biro kredit tinggi",
    "credit_small": "pinjaman kecil", "credit_med": "pinjaman menengah", "credit_large": "pinjaman besar",
    "burden_low": "beban cicilan ringan", "burden_med": "beban cicilan sedang", "burden_high": "beban cicilan berat",
}
for _r in cluster_names.itertuples():
    VOCAB[f"cluster_{int(_r.cluster_id)}_{_r.slug}"] = f"segmen {_r.nama}"

def _items(part):
    return [i.strip().strip("'") for i in
            part.replace("{", "").replace("}", "").split(",") if i.strip()]

def humanize_rule(rule_str):
    parts = str(rule_str).split(" -> ")
    if len(parts) != 2:
        return rule_str
    kiri = ", ".join(VOCAB.get(i, i) for i in _items(parts[0]))
    kanan = ", ".join(VOCAB.get(i, i) for i in _items(parts[1]))
    return f"Jika {kiri} → biasanya {kanan}"


# ── Kamus nama kolom teknis -> istilah bisnis ──────────────────────────────
# Dipakai di semua grafik dan tabel supaya audiens bisnis tidak perlu
# menebak arti AMT_CREDIT atau INST_DPD_MAX.
FEATURE_LABELS = {
    "AMT_INCOME_TOTAL": "Pendapatan tahunan",
    "AMT_CREDIT": "Nilai pinjaman",
    "AMT_ANNUITY": "Cicilan per tahun",
    "CREDIT_TO_INCOME": "Pinjaman dibanding pendapatan",
    "ANNUITY_TO_INCOME": "Beban cicilan dibanding pendapatan",
    "CREDIT_TERM_MONTHS": "Perkiraan tenor pinjaman",
    "YEARS_BIRTH": "Usia",
    "YEARS_EMPLOYED": "Lama bekerja",
    "FLAG_SENTINEL_EMPLOYED": "Pensiunan / tidak bekerja",
    "CNT_CHILDREN": "Jumlah anak",
    "CODE_GENDER": "Jenis kelamin (perempuan)",
    "NAME_CONTRACT_TYPE": "Jenis kredit: tunai (vs kartu)",
    "REGION_RATING_CLIENT_W_CITY": "Rating wilayah tempat tinggal",
    "OWN_CAR_AGE": "Umur mobil yang dimiliki",
    "FLAG_NO_CAR": "Tidak punya mobil",
    "FLAG_NO_HOUSING_DATA": "Data hunian tidak tersedia",
    "EXT_SOURCE_1": "Skor biro kredit eksternal 1",
    "EXT_SOURCE_2": "Skor biro kredit eksternal 2",
    "EXT_SOURCE_3": "Skor biro kredit eksternal 3",
    "FLAG_EXT_SOURCE_1_MISSING": "Tanpa skor biro 1 (riwayat tipis)",
    "AMT_REQ_CREDIT_BUREAU_YEAR": "Berapa kali dicek biro kredit setahun terakhir",
    "FLAG_NO_BUREAU": "Tanpa catatan biro kredit sama sekali",
    "BUREAU_COUNT": "Jumlah kredit tercatat di biro",
    "BUREAU_ACTIVE_RATIO": "Porsi kredit di bank lain yang masih berjalan",
    "BUREAU_DEBT_TO_CREDIT_RATIO": "Sisa utang di bank lain",
    "BUREAU_DAYS_CREDIT_MEAN": "Rata-rata umur kredit di bank lain",
    "BUREAU_BB_DPD_RATIO_MEAN": "Porsi bulan menunggak (catatan biro)",
    "BUREAU_BB_SEVERE_DPD_MEAN": "Porsi bulan menunggak 90+ hari (biro)",
    "PREV_COUNT": "Jumlah pengajuan sebelumnya di Home Credit",
    "PREV_APPROVAL_RATE": "Tingkat persetujuan pengajuan sebelumnya",
    "PREV_REFUSED_COUNT": "Jumlah pengajuan yang pernah ditolak",
    "INST_DPD_MEAN": "Rata-rata hari telat bayar cicilan",
    "INST_DPD_MAX": "Keterlambatan cicilan terparah",
    "INST_LATE_RATIO": "Porsi cicilan yang telat dibayar",
    "INST_SEVERE_LATE_RATIO": "Porsi cicilan telat lebih dari 30 hari",
    "INST_PAYMENT_RATIO_MEAN": "Porsi tagihan yang benar-benar dibayar",
    "POS_SK_DPD_MEAN": "Rata-rata tunggakan kredit barang / tunai",
    "POS_MONTHS_COUNT": "Lama riwayat kredit barang / tunai",
    "CC_UTILIZATION_MEAN": "Pemakaian limit kartu kredit (rata-rata)",
    "CC_UTILIZATION_MAX": "Pemakaian limit kartu kredit (tertinggi)",
    "CC_SK_DPD_MEAN": "Rata-rata tunggakan kartu kredit",
    "CC_AMT_BALANCE_MEAN": "Saldo terutang kartu kredit",
    "CC_MONTHS_COUNT": "Lama riwayat kartu kredit",
    "DEF_30_CNT_SOCIAL_CIRCLE_BIN": "Kenalan dekat yang menunggak",
    # Kategorikal dengan encoding ramah-clustering (bukan one-hot):
    "NAME_EDUCATION_TYPE": "Tingkat pendidikan (jenjang 0-4)",
    "NAME_INCOME_TYPE_FREQ": "Tipe pendapatan (seberapa umum)",
    "ORGANIZATION_TYPE_FREQ": "Sektor pekerjaan (seberapa umum)",
}


def flabel(feat):
    return FEATURE_LABELS.get(feat, feat.replace("_", " ").capitalize())


# Deskripsi singkat tiap segmen dalam bahasa sehari-hari, kunci = slug
# (stabil antar run, tidak seperti nomor cluster).
SEG_DESC = {
    "minimal": "Nasabah kebutuhan dasar: pinjaman kecil, tenor pendek, beban ringan. "
               "Eksposur bank terhadap mereka kecil, dan perilakunya dekat dengan rata-rata.",
    "ambisius": "Pinjaman besar dibanding pendapatannya dan umumnya nasabah baru. Terlihat "
                "berani di atas kertas, tapi justru segmen dengan gagal bayar terendah; "
                "pinjaman besar memang hanya disetujui untuk profil yang kuat.",
    "veteran": "Pelanggan lama yang sangat sering mengajukan kredit dan sering ditolak. "
               "Riwayatnya padat di semua produk; perlu dilihat kenapa penolakannya tinggi.",
    "bermasalah": "Hanya 1% portofolio tapi menunggak hampir di semua produk, dengan "
                  "keterlambatan berkali-kali lipat nasabah biasa. Konsentrasi risiko tertinggi.",
    "cc_intensif": "Hidup dari kartu kredit: pemakaian limit dua sampai tiga kali rata-rata "
                   "dan saldo terutang besar. Rentan kalau pendapatannya terganggu.",
}

# Label tipologi anomali untuk tampilan (file CSV tetap memakai istilah teknis)
TYPE_LABEL = {
    "Tipe A - Data Error": "Kesalahan input data",
    "Tipe B - Rare but Valid": "Langka tapi sah",
    "Tipe C - Risk Signal": "Sinyal risiko",
}
TYPE_DISPLAY_COLORS = {
    "Kesalahan input data": "#9AA5B1",
    "Langka tapi sah": SAGE,
    "Sinyal risiko": CLAY,
}

_DEV_RE = re.compile(r"`(\w+)` = [-\d.]+ \(([\d.]+)x median\)")


def humanize_deviations(txt):
    """'`CC_SK_DPD_MEAN` = 25.61 (515.3x median)' -> kalimat bisnis."""
    pairs = _DEV_RE.findall(str(txt))
    if not pairs:
        return str(txt)
    return "; ".join(f"{flabel(f)} {float(m):,.0f}x lipat median segmennya"
                     for f, m in pairs[:3])


def rule_action(rule_str, lift):
    """Saran tindak lanjut per rule, heuristik yang sama dengan Phase 3."""
    parts = str(rule_str).split(" -> ")
    items = set()
    for p in parts:
        items |= set(_items(p))
    slug_full = {r.slug: f"cluster_{int(r.cluster_id)}_{r.slug}"
                 for r in cluster_names.itertuples()}
    if "income_low" in items and "credit_large" in items:
        return "Tolak otomatis kecuali ada agunan; review manual oleh underwriter senior."
    if slug_full.get("bermasalah") in items:
        return "Pasang sebagai aturan deteksi dini; nasabah lama yang cocok pola ini ditinjau ulang."
    if "income_very_high" in items and lift >= 2.5:
        return "Prioritas penawaran produk premium dan pricing khusus."
    if "risk_score_high" in items:
        return "Jadikan penanda positif di scoring untuk approval dan kenaikan limit."
    if "age_senior" in items and "emp_new" in items:
        return "Tambahkan verifikasi sumber pendapatan (pensiun atau usaha baru) saat aplikasi."
    if slug_full.get("ambisius") in items and "credit_large" in items:
        return "Wajibkan uji ketahanan: masih sanggup bayar bila pendapatan turun 30%?"
    if slug_full.get("minimal") in items:
        return "Arahkan ke produk micro-credit bertenor pendek plus edukasi keuangan."
    return "Masukkan sebagai fitur tambahan di model scoring; uji dulu di data 6 bulan terakhir."

# ── Komponen kecil ─────────────────────────────────────────────────────────
def kpi_card(title, value, sub, accent=None):
    style = {"borderTop": f"4px solid {accent}"} if accent else {}
    return html.Div(
        [html.Div(title, className="kpi-title"),
         html.Div(value, className="kpi-value"),
         html.Div(sub, className="kpi-sub")],
        className="kpi-card", style=style)


def caption(text):
    return html.P(text, className="chart-caption")


def insight_box(title, body, color=BLUE):
    return html.Div(
        [html.Div(title, className="insight-title"),
         html.P(body, className="insight-body")],
        className="insight-box", style={"borderLeft": f"5px solid {color}"})


def card(children):
    return html.Div(children, className="card")


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

# ── Figure: validasi default rate ──────────────────────────────────────────
def fig_seg_default():
    df = pd.DataFrame({
        "Segmen": [seg_label(c) for c in seg_default.index],
        "Default (%)": seg_default.values.round(2),
        "warna": [seg_color(c) for c in seg_default.index],
    }).sort_values("Default (%)")
    fig = go.Figure(go.Bar(
        x=df["Default (%)"], y=df["Segmen"], orientation="h",
        marker_color=df["warna"],
        text=[f"{v:.1f}%" for v in df["Default (%)"]], textposition="outside"))
    fig.add_vline(x=BASELINE, line_dash="dash", line_color=WARM_GRAY,
                  annotation_text=f"rata-rata {BASELINE:.1f}%",
                  annotation_position="top")
    fig.update_xaxes(range=[0, max(df["Default (%)"]) * 1.25])
    return style_fig(fig, "Tingkat gagal bayar aktual per segmen")


def fig_tier_default():
    rows = [(TIER_LABEL[t], float(tier_default.get(t, np.nan)), TIER_COLORS[t])
            for t in TIER_ORDER]
    fig = go.Figure(go.Bar(
        x=[r[0] for r in rows], y=[r[1] for r in rows],
        marker_color=[r[2] for r in rows],
        text=[f"{r[1]:.1f}%" for r in rows], textposition="outside"))
    fig.add_hline(y=BASELINE, line_dash="dash", line_color=WARM_GRAY,
                  annotation_text=f"rata-rata {BASELINE:.1f}%")
    fig.update_yaxes(title="Default aktual (%)",
                     range=[0, max(r[1] for r in rows) * 1.25])
    return style_fig(fig, "Makin banyak metode menandai aplikasi sebagai anomali, makin tinggi gagal bayarnya")

# ── Figure: segmentasi ─────────────────────────────────────────────────────
def fig_cluster_scatter():
    order = [seg_label(c) for c in sorted(SLUG_BY_ID)]
    cmap = {seg_label(c): seg_color(c) for c in sorted(SLUG_BY_ID)}
    # render_mode webgl: 20 ribu titik SVG membekukan browser saat presentasi
    fig = px.scatter(cluster_viz, x="PC1", y="PC2", color="Segmen",
                     category_orders={"Segmen": order},
                     color_discrete_map=cmap, opacity=0.45,
                     render_mode="webgl")
    fig.update_traces(marker=dict(size=4))
    # Tulis nama segmen langsung di tengah gerombolannya supaya pembaca
    # tidak harus bolak-balik ke legenda.
    centroids = cluster_viz.groupby("Segmen")[["PC1", "PC2"]].median()
    for seg_name, row in centroids.iterrows():
        fig.add_annotation(x=row["PC1"], y=row["PC2"], text=f"<b>{seg_name}</b>",
                           showarrow=False, font=dict(size=11, color=INK),
                           bgcolor="rgba(255,255,255,0.85)", borderpad=2)
    fig.update_layout(legend=dict(orientation="h", y=-0.12))
    fig.update_xaxes(title="", showticklabels=False)
    fig.update_yaxes(title="", showticklabels=False)
    return style_fig(fig, "Peta nasabah: tiap titik satu pemohon, warna = segmen", height=460)


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
    fig.update_xaxes(title="Jumlah pemohon", range=[0, df["n_applicants"].max() * 1.45])
    return style_fig(fig, "Ukuran segmen dan tingkat gagal bayarnya", height=340)


def fig_elbow_silhouette():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=k_selection["k"], y=k_selection["inertia"],
                             mode="lines+markers", name="Inertia",
                             line=dict(color=BLUE)))
    fig.add_trace(go.Scatter(x=k_selection["k"], y=k_selection["silhouette"],
                             mode="lines+markers", name="Silhouette", yaxis="y2",
                             line=dict(color=SAGE)))
    fig.add_vline(x=5, line_dash="dot", line_color=CLAY,
                  annotation_text="K=5 dipilih")
    fig.update_layout(xaxis_title="Jumlah cluster (K)", yaxis_title="Inertia",
                      yaxis2=dict(title="Silhouette", overlaying="y", side="right"),
                      legend=dict(orientation="h", y=-0.25))
    return style_fig(fig, "Pemilihan jumlah segmen: elbow dan silhouette", height=340)

# ── Figure: rules ──────────────────────────────────────────────────────────
def fig_rules_scatter():
    df = rules_combined.copy()
    df["Ditemukan oleh"] = df["n_algos"].map(lambda n: f"{n} algoritma")
    df["rule"] = df["rule_str"].map(humanize_rule)
    fig = px.scatter(df, x="support", y="confidence", size="lift", render_mode="webgl",
                     color="Ditemukan oleh", hover_data={"rule": True, "lift": ":.2f",
                                                         "support": ":.3f",
                                                         "confidence": ":.3f"},
                     color_discrete_sequence=["#BCC4CE", BLUE, CLAY, MAUVE, SAGE])
    fig.update_xaxes(title="Cakupan: berapa persen portofolio mengikuti pola ini",
                     tickformat=".0%")
    fig.update_yaxes(title="Akurasi: seberapa sering polanya benar", tickformat=".0%")
    return style_fig(fig, "Semua aturan yang ditemukan; ukuran titik = kekuatan (lift)", height=420)


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
    return style_fig(fig, "Keterkaitan antar kondisi dalam 15 aturan final", height=460)

# ── Figure: anomali ────────────────────────────────────────────────────────
def fig_anomaly_scatter():
    df = anomaly_pca.copy()
    df["Tingkat"] = df["anomaly_category"].map(TIER_LABEL)
    fig = px.scatter(df, x="PC1", y="PC2", color="Tingkat",
                     category_orders={"Tingkat": [TIER_LABEL[t] for t in TIER_ORDER]},
                     color_discrete_map={TIER_LABEL[t]: TIER_COLORS[t] for t in TIER_ORDER},
                     opacity=0.55, hover_data=["Segmen"],
                     render_mode="webgl")
    fig.update_traces(marker=dict(size=4))
    fig.update_layout(legend=dict(orientation="h", y=-0.12))
    fig.update_xaxes(title="Dimensi utama 1", showticklabels=False)
    fig.update_yaxes(title="Dimensi utama 2", showticklabels=False)
    return style_fig(fig, "Peta anomali: titik merah ditandai 3-4 metode sekaligus", height=460)


def fig_typology():
    counts = investigation["Anomaly Type"].map(TYPE_LABEL).value_counts().reset_index()
    counts.columns = ["Tipe", "Jumlah"]
    fig = px.pie(counts, names="Tipe", values="Jumlah", hole=0.5,
                 color="Tipe", color_discrete_map=TYPE_DISPLAY_COLORS)
    fig.update_traces(textinfo="value+percent")
    return style_fig(fig, f"Hasil investigasi {len(investigation):,} anomali kuat", height=360)


def fig_anomaly_per_cluster():
    inv = investigation.copy()
    inv["cid"] = inv["Cluster"].str.extract(r"(\d+)").astype(int)
    inv["Segmen"] = inv["cid"].map(seg_label)
    inv["Tipe"] = inv["Anomaly Type"].map(TYPE_LABEL)
    counts = inv.groupby(["Segmen", "Tipe"]).size().reset_index(name="Jumlah aplikasi")
    fig = px.bar(counts, x="Segmen", y="Jumlah aplikasi", color="Tipe",
                 color_discrete_map=TYPE_DISPLAY_COLORS)
    fig.update_layout(legend=dict(orientation="h", y=-0.3, title=""))
    fig.update_xaxes(title="")
    return style_fig(fig, "Di segmen mana anomali terkonsentrasi", height=360)

# ── Figure: metodologi ─────────────────────────────────────────────────────
def fig_mi_top15():
    top = feature_importance.head(15).iloc[::-1].copy()
    top["label"] = top["feature"].map(flabel)
    fig = px.bar(top, x="mutual_info", y="label", orientation="h",
                 hover_data={"feature": True},
                 color_discrete_sequence=[ACCENT])
    fig.update_xaxes(title="Seberapa banyak informasi yang dibawa tentang gagal bayar")
    fig.update_yaxes(title="")
    return style_fig(fig, "15 hal yang paling membedakan nasabah gagal bayar", height=430)

# ── Tabel rules untuk klien ────────────────────────────────────────────────
rules_display = rules_final.copy()
rules_display["Aturan"] = rules_display["rule_str"].map(humanize_rule)
rules_display["Segmen"] = rules_display["target_cluster"].map(
    lambda s: NAME_BY_ID.get(ID_BY_SLUG.get(s.split("_", 2)[-1], -1), s))
rules_display["Cakupan"] = (rules_display["support"] * 100).round(1).astype(str) + "%"
rules_display["Akurasi"] = (rules_display["confidence"] * 100).round(1).astype(str) + "%"
rules_display["Kekuatan"] = rules_display["lift"].round(1).map(
    lambda v: f"{v}x lebih sering dari kebetulan")
rules_display["Tindak lanjut yang disarankan"] = rules_display.apply(
    lambda r: rule_action(r["rule_str"], float(r["lift"])), axis=1)
RULES_COLS = ["rank", "Segmen", "Aturan", "Cakupan", "Akurasi", "Kekuatan",
              "Tindak lanjut yang disarankan"]
rules_display = rules_display[RULES_COLS].rename(columns={"rank": "No"})

inv_preview = investigation.head(10)[
    ["SK_ID_CURR", "Cluster", "Anomaly Type", "Top Deviating Features"]].copy()
inv_preview["Cluster"] = inv_preview["Cluster"].str.extract(r"(\d+)").astype(int).map(seg_label)
inv_preview["Anomaly Type"] = inv_preview["Anomaly Type"].map(TYPE_LABEL)
inv_preview["Top Deviating Features"] = inv_preview["Top Deviating Features"].map(
    humanize_deviations)
inv_preview.columns = ["ID Pemohon", "Segmen", "Tipe",
                       "Apa yang membuatnya menonjol"]

high_corr_display = high_corr.copy()
high_corr_display["Fitur 1"] = high_corr_display["feature_1"].map(flabel)
high_corr_display["Fitur 2"] = high_corr_display["feature_2"].map(flabel)
high_corr_display["Korelasi"] = high_corr_display["abs_corr"].round(3)
high_corr_display = high_corr_display[["Fitur 1", "Fitur 2", "Korelasi"]]

# ── Angka untuk kartu temuan ───────────────────────────────────────────────
n_high = int(anomaly_summary["HIGH_CONFIDENCE"].iloc[0])
n_eval = int(anomaly_summary["Total_Evaluated"].iloc[0])
_amb_id = ID_BY_SLUG.get("ambisius")
_brm_id = ID_BY_SLUG.get("bermasalah")
amb_def = float(seg_default.get(_amb_id, np.nan))
brm_def = float(seg_default.get(_brm_id, np.nan))
tier_hi = float(tier_default.get("HIGH_CONFIDENCE_ANOMALY", np.nan))
tier_no = float(tier_default.get("NORMAL", np.nan))
n_typeC = int((investigation["Anomaly Type"] == "Tipe C - Risk Signal").sum())

app = Dash(__name__, title="Home Credit | Hasil Data Mining",
           suppress_callback_exceptions=True)


# Konten tab dibangun sekali saat pertama kali dibuka (lazy). Kalau kelima
# tab di-mount sekaligus, browser harus merender belasan grafik di muka dan
# halaman membeku beberapa detik; itu buruk untuk presentasi klien.
def tab_exec():
    return html.Div([
            html.Div([
                insight_box(
                    "Temuan 1: peminjam terbesar justru paling aman",
                    f"Segmen Ambisius meminjam paling besar relatif pendapatannya, tapi gagal "
                    f"bayarnya hanya {amb_def:.1f}% melawan rata-rata {BASELINE:.1f}%. Risiko bukan "
                    f"soal nominal; risiko ada di jejak perilaku.", SAGE),
                insight_box(
                    "Temuan 2: 1% nasabah menyumbang risiko terpekat",
                    f"Segmen Bermasalah cuma 1% portofolio tapi gagal bayarnya {brm_def:.1f}%. "
                    f"Pola perilakunya sangat konsisten: salah satu aturannya berakurasi 99%.", CLAY),
                insight_box(
                    "Temuan 3: keanehan statistik adalah sinyal risiko",
                    f"Aplikasi yang ditandai 3-4 metode anomali gagal bayar {tier_hi:.1f}%, "
                    f"naik bertingkat dari {tier_no:.1f}% pada aplikasi normal. {n_typeC} kasus "
                    f"terindikasi sinyal risiko murni dan butuh review manual.", SAND),
            ], className="insight-row"),
            html.Div([
                card([dcc.Graph(figure=fig_seg_default()),
                      caption("Tiap batang satu segmen hasil clustering. Garis putus-putus = "
                              "rata-rata portofolio. Label gagal bayar tidak pernah dipakai saat "
                              "membentuk segmen; perbedaan angka ini murni hasil struktur data.")]),
                card([dcc.Graph(figure=fig_tier_default()),
                      caption("Empat metode deteksi anomali bekerja tanpa label. Makin banyak "
                              "yang sepakat sebuah aplikasi aneh, makin tinggi gagal bayar "
                              "aktualnya. Tangga naik tanpa pengecualian.")]),
            ], className="row"),
    ])


def tab_segments():
    return html.Div([
            html.Div([
                card([dcc.Graph(figure=fig_cluster_scatter()),
                      caption("Proyeksi dua dimensi dari 65 fitur (sampel 20 ribu titik). Posisi "
                              "berdekatan = profil mirip. Lima warna = lima segmen.")]),
                card([dcc.Graph(figure=fig_cluster_sizes()),
                      caption("Dua segmen terbesar mencakup 70% portofolio dan keduanya "
                              "relatif aman. Segmen kecil di bawah justru yang menyimpan risiko.")]),
            ], className="row"),
            card([
                html.H3("Profil tiap segmen"),
                html.P("Pilih segmen untuk melihat fitur apa yang membuatnya berbeda dari "
                       "rata-rata portofolio. Batang ke kanan berarti lebih tinggi dari "
                       "rata-rata, ke kiri berarti lebih rendah.", className="chart-caption"),
                dcc.Dropdown(
                    id="cluster-dd",
                    options=[{"label": f"{r.nama} (risiko {r.profil_risiko}, "
                                       f"{r.n_applicants:,} pemohon)",
                              "value": int(r.cluster_id)}
                             for r in cluster_names.itertuples()],
                    value=int(cluster_names["cluster_id"].iloc[0]), clearable=False,
                    style={"maxWidth": "640px"}),
                html.Div(id="cluster-desc", className="segment-desc"),
                dcc.Graph(id="cluster-profile-fig"),
            ]),
    ])


def tab_rules():
    return html.Div([
            card([
                html.H3("15 aturan perilaku terkuat"),
                html.P("Cakupan = berapa persen portofolio mengikuti pola ini. Akurasi = bila "
                       "sisi 'jika' terpenuhi, berapa persen kasus sisi 'maka' ikut terjadi. "
                       "Kekuatan = berapa kali lebih sering dibanding kebetulan; 1x berarti "
                       "kebetulan biasa.", className="chart-caption"),
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
                      caption("Kondisi yang sering muncul bersama saling terhubung. Simpul besar "
                              "= kondisi yang terlibat di banyak aturan sekaligus.")]),
                card([dcc.Graph(figure=fig_rules_scatter()),
                      caption("Seluruh 1.204 aturan kandidat. Yang dipilih ke tabel final adalah "
                              "yang kuat, akurat, dan tidak mengulang cerita aturan lain.")]),
            ], className="row"),
    ])


def tab_anomaly():
    return html.Div([
            html.Div([
                card([dcc.Graph(figure=fig_anomaly_scatter()),
                      caption("Aplikasi anomali kuat (merah) mengumpul di pinggiran peta, "
                              "jauh dari kerumunan nasabah tipikal.")]),
                card([dcc.Graph(figure=fig_typology()),
                      caption("Tiga tipe dengan tindak lanjut berbeda: kesalahan data diperbaiki "
                              "di hulu, kasus langka-tapi-sah dialihkan ke layanan prioritas, "
                              "sinyal risiko masuk review manual."),
                      dcc.Graph(figure=fig_anomaly_per_cluster())]),
            ], className="row"),
            card([
                html.H3("Contoh kasus hasil investigasi"),
                html.P("Sepuluh kasus paling menyimpang, dengan ID pemohon asli sehingga tim "
                       "operasional bisa menindaklanjuti langsung. Daftar lengkap 10.911 kasus "
                       "ada di results/phase4_anomaly/anomaly_investigation.csv.",
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
            html.Div([
                card([dcc.Graph(figure=fig_mi_top15()),
                      caption("Mutual information mengukur berapa banyak informasi sebuah fitur "
                              "membawa tentang status gagal bayar, termasuk hubungan non-linear "
                              "yang luput dari korelasi biasa.")]),
                card([dcc.Graph(figure=fig_elbow_silhouette()),
                      caption("Elbow menunjuk K=5 dan silhouette K=5 adalah yang terbaik di "
                              "antara pilihan K di atas 2. K=2 memang skornya lebih tinggi, "
                              "tapi dua segmen terlalu kasar untuk dipakai mengambil keputusan."),
                      html.H3("Sisa korelasi tinggi"),
                      html.P("Dua pasangan fitur dengan korelasi di atas 0,85 yang sengaja "
                             "dipertahankan, beserta nilainya. Pasangan dengan korelasi "
                             "sempurna sudah dibuang di pipeline.", className="chart-caption"),
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
    "tab-rules": tab_rules,
    "tab-anom": tab_anomaly,
    "tab-method": tab_method,
}
_tab_cache = {}

app.layout = html.Div([
    html.Div([
        html.H1("Apa yang tersembunyi di 356 ribu aplikasi kredit?"),
        html.P(f"Hasil knowledge discovery pada portofolio Home Credit: {len(cluster_names)} "
               f"segmen nasabah, {len(rules_final)} aturan perilaku, dan {n_high:,} aplikasi "
               f"anomali, semuanya ditemukan tanpa melihat label gagal bayar, lalu diuji "
               f"terhadap gagal bayar yang sungguh terjadi.",
               className="hero-sub"),
    ], className="hero"),

    html.Div([
        kpi_card("Aplikasi dianalisis", f"{N_TOTAL:,}", "train + test, 7 sumber data"),
        kpi_card("Gagal bayar rata-rata", f"{BASELINE:.1f}%", "baseline portofolio", WARM_GRAY),
        kpi_card("Segmen nasabah", "5", "ditemukan algoritma, dinamai manusia", BLUE),
        kpi_card("Aturan perilaku", f"{len(rules_final)}", "dikonfirmasi 3 algoritma", MAUVE),
        kpi_card("Anomali kuat", f"{n_high:,}", f"{n_high / n_eval * 100:.1f}% dari portofolio", CLAY),
    ], className="kpi-row"),

    dcc.Tabs(id="tabs", value="tab-exec", className="tabs", children=[
        dcc.Tab(label="Ringkasan eksekutif", value="tab-exec"),
        dcc.Tab(label="Segmen nasabah", value="tab-seg"),
        dcc.Tab(label="Pola dan aturan", value="tab-rules"),
        dcc.Tab(label="Anomali dan risiko", value="tab-anom"),
        dcc.Tab(label="Metodologi", value="tab-method"),
    ]),
    html.Div(id="tab-content"),

    html.Footer(
        "Sumber: artefak results/phase1-4 dan datasets/final. Semua angka dihitung ulang "
        "otomatis setiap pipeline dijalankan ulang; tidak ada angka yang ditulis tangan. "
        "Seed acak 42 di semua tahap."),
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
    bar_text = [f"{abs(v):.0f}% {'di atas' if v > 0 else 'di bawah'} rata-rata"
                for v in sub["rel_diff_pct"]]
    fig = go.Figure(go.Bar(
        x=sub["rel_diff_pct"], y=labels, orientation="h", marker_color=colors,
        text=bar_text, textposition="outside",
        customdata=sub["fitur"],
        hovertemplate="%{y}<br>%{text}<br>kolom data: %{customdata}<extra></extra>"))
    fig.update_xaxes(
        title="Hijau = lebih tinggi dari rata-rata portofolio, merah = lebih rendah")
    pad = max(abs(sub["rel_diff_pct"])) * 0.45
    fig.update_xaxes(range=[min(sub["rel_diff_pct"].min(), 0) - pad,
                            max(sub["rel_diff_pct"].max(), 0) + pad])
    fig = style_fig(
        fig, f"{NAME_BY_ID.get(cid, '?')}: apa yang membuat segmen ini berbeda "
             f"(gagal bayar aktual {float(seg_default.get(cid, np.nan)):.1f}%)",
        height=430)
    desc = SEG_DESC.get(SLUG_BY_ID.get(cid, ""), "")
    return fig, desc


if __name__ == "__main__":
    app.run(debug=False, port=8050)

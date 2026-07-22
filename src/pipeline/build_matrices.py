"""
Build the three output matrices.

This is where one prepared table becomes three deliberately different views of
the same applicants. Each downstream phase needs a different trade-off, and
serving them all from one matrix is what caused defect F2 (see REPORT.md 1b):

  - features_business.csv   readable values and audit trail, for explaining a
                            case to a human. Never used for distance maths.
  - features_clustering.csv clipped and standardized, so a handful of extreme
                            files cannot capture K-Means centroids.
  - features_anomaly.csv    the same columns standardized WITHOUT clipping,
                            because a truncated axis cannot contain an outlier.

1. Select  - keep SK_ID_CURR (identifier) + the CLUSTERING_FEATURES that exist.
             Protected and proxy attributes are routed to the business artifact
             only, so they can describe a segment but never form one.
2. Fill    - residual NaN -> 0  (YEARS_EMPLOYED is NaN for sentinel rows;
             FLAG_SENTINEL_EMPLOYED already encodes that, so 0 is correct).
3. Scale   - StandardScaler on everything EXCEPT true {0,1} binary flags.
             Ordinal columns (education 0-4, DEF_30 bin 0-2) and the
             frequency-encoded columns ARE scaled: without scaling their raw
             range would silently out-weight the standardized features. Binary
             flags stay in {0,1} so cluster profiles remain readable as
             "share of the cluster that has this trait".

Outputs:
  datasets/final/features_business.csv
    Human-readable model-facing values plus SOURCE_* audit columns. Log-
    transformed monetary fields are inverted back to anonymised currency
    units. Source score columns preserve true missingness, and source amount
    columns preserve values before model-facing caps.

  datasets/final/features_clustering.csv
  First column SK_ID_CURR is an identifier (not scaled, not a feature) so
  Phase 2-5 outputs are traceable to real applicants.
"""
import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from .config import BASE_DIR, OUTPUT_DIR, CLUSTERING_FEATURES, LOG_TRANSFORM_COLS
from .utils import log, log_shape


def run(df: pd.DataFrame) -> pd.DataFrame:
    log("Step 9 - Feature selection + scaling ...")
    df = df.copy().reset_index(drop=True)

    # 1. Select features
    base_cols = [c for c in CLUSTERING_FEATURES if c in df.columns]
    missing_base = [c for c in CLUSTERING_FEATURES if c not in df.columns]
    if missing_base:
        log(f"  WARNING - expected features not found (skipped): {missing_base}", "WARN")

    # DEF_30_CNT_SOCIAL_CIRCLE_BIN used to be appended to the mining matrix here.
    # It is now profile-only: an applicant's acquaintances' arrears are not the
    # applicant's own conduct, and letting it shape a segment is guilt by
    # association. See the protected-attribute note in config.CLUSTERING_FEATURES.
    extra_encoded: list[str] = []

    select_cols = base_cols + extra_encoded

    # Attributes excluded from segmentation but still needed to DESCRIBE the
    # segments afterwards and to run fairness monitoring. They must reach the
    # business artifact even though they never enter a distance calculation.
    PROFILE_ONLY_COLS = [
        "YEARS_BIRTH", "CNT_CHILDREN", "REGION_RATING_CLIENT_W_CITY",
        "NAME_EDUCATION_TYPE", "NAME_INCOME_TYPE_FREQ", "ORGANIZATION_TYPE_FREQ",
        "DEF_30_CNT_SOCIAL_CIRCLE_BIN", "CODE_GENDER",
    ]

    # Save a separate business-readable contract before filling/scaling. The
    # mining matrix is intentionally standardized; explanations and policy
    # thresholds must never be calculated from those z-score-like values.
    audit_cols = [c for c in df.columns if c.startswith("SOURCE_")]
    business_cols = select_cols + [
        c for c in ["GOODS_TO_CREDIT"] + PROFILE_ONLY_COLS + audit_cols
        if c in df.columns and c not in select_cols
    ]
    business_df = df[business_cols].copy()
    for col in LOG_TRANSFORM_COLS:
        if col in business_df.columns:
            business_df[col] = np.expm1(business_df[col]).clip(lower=0)

    business_df.insert(0, "ROW_ID", np.arange(len(business_df), dtype=np.int64))
    if "SK_ID_CURR" in df.columns:
        business_df.insert(1, "SK_ID_CURR", df["SK_ID_CURR"].astype(np.int64))

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    business_path = os.path.join(OUTPUT_DIR, "features_business.csv")
    business_df.to_csv(business_path, index=False)
    log(f"  Saved business-readable values -> {business_path}")
    log_shape("features_business", business_df)

    feature_df = df[select_cols].copy()
    log(f"  Selected {len(select_cols)} features "
        f"({len(base_cols)} base + {len(extra_encoded)} ordinal bin)")

    # 2. Fill residual NaN
    nan_count = feature_df.isna().sum().sum()
    if nan_count > 0:
        feature_df = feature_df.fillna(0)
        log(f"  Filled {nan_count:,} residual NaN -> 0")

    # 3. Robustify and scale everything except true {0,1} binary flags.
    # Detection is by VALUE SET, not dtype: an int8 ordinal (0-4) is NOT
    # binary and must be scaled, otherwise its range silently dominates.
    binary_cols = [
        c for c in feature_df.columns
        if set(pd.unique(feature_df[c].dropna())).issubset({0, 1, 0.0, 1.0})
    ]
    scale_cols = [
        c for c in feature_df.select_dtypes(include=[np.number]).columns
        if c not in binary_cols
    ]
    # K-Means otherwise spends a centroid on a handful of extreme repayment or
    # ratio values.  Those rows remain fully available to Phase 4; only their
    # contribution to broad segmentation distance is bounded here.  Ordinal
    # and frequency-encoded category axes are valid category information and
    # are scaled but not clipped.
    categorical_axes = {
        "NAME_EDUCATION_TYPE", "NAME_INCOME_TYPE_FREQ",
        "ORGANIZATION_TYPE_FREQ", "DEF_30_CNT_SOCIAL_CIRCLE_BIN",
    }
    clip_cols = [c for c in scale_cols if c not in categorical_axes]
    clip_rows = []
    for col in clip_cols:
        lower, upper = feature_df[col].quantile([0.005, 0.995])
        below = int((feature_df[col] < lower).sum())
        above = int((feature_df[col] > upper).sum())
        feature_df[col] = feature_df[col].clip(lower=lower, upper=upper)
        clip_rows.append({
            "feature": col, "lower_model_value": lower,
            "upper_model_value": upper, "rows_clipped_low": below,
            "rows_clipped_high": above,
        })
    report_dir = os.path.join(BASE_DIR, "results", "phase1_preprocessing")
    os.makedirs(report_dir, exist_ok=True)
    pd.DataFrame(clip_rows).to_csv(
        os.path.join(report_dir, "clustering_clip_limits.csv"), index=False
    )
    log(f"  Robust-clipped {len(clip_cols)} distance axes at p0.5/p99.5; source values retained")

    log(f"  Scaling {len(scale_cols)} continuous/ordinal cols; "
        f"{len(binary_cols)} binary flags left as 0/1")

    scaler = StandardScaler()
    scaled_values = pd.DataFrame(
        scaler.fit_transform(feature_df[scale_cols]),
        columns=scale_cols,
        index=feature_df.index,
    )
    feature_df = pd.concat(
        [feature_df.drop(columns=scale_cols), scaled_values],
        axis=1,
    )[select_cols]   # restore original column order

    # 4. Re-attach identifier and save
    if "SK_ID_CURR" in df.columns:
        feature_df.insert(0, "SK_ID_CURR", df["SK_ID_CURR"].astype(np.int64))

    out_path = os.path.join(OUTPUT_DIR, "features_clustering.csv")
    feature_df.to_csv(out_path, index=False)
    log(f"  Saved -> {out_path}")
    log_shape("features_clustering", feature_df)

    # 5. Anomaly-detection matrix: SAME features, standardized, NOT clipped.
    #
    # Clipping is the right treatment for K-Means, which would otherwise spend a
    # centroid on a handful of extreme files. It is the wrong input for outlier
    # detection, and using one matrix for both silently broke Phase 4:
    #   - a "global extreme value" cannot be found on an axis whose extremes
    #     were truncated by construction, because the largest possible deviation
    #     IS the clip boundary;
    #   - clipping collapses roughly 1,800 rows per axis onto one identical
    #     value, so the most extreme records gain a crowd of neighbours and look
    #     LESS anomalous to LOF and DBSCAN - the treatment hides exactly the
    #     records it should surface; and
    #   - that boundary pile-up is a non-Gaussian point mass that distorts the
    #     covariance matrix Mahalanobis depends on.
    #
    # So Phase 4 gets its own matrix, standardized on unclipped values.
    anomaly_df = df[select_cols].copy()
    residual_nan = anomaly_df.isna().sum().sum()
    if residual_nan > 0:
        anomaly_df = anomaly_df.fillna(0)
    anomaly_scaler = StandardScaler()
    anomaly_scaled = pd.DataFrame(
        anomaly_scaler.fit_transform(anomaly_df[scale_cols]),
        columns=scale_cols,
        index=anomaly_df.index,
    )
    anomaly_df = pd.concat(
        [anomaly_df.drop(columns=scale_cols), anomaly_scaled], axis=1
    )[select_cols]
    if "SK_ID_CURR" in df.columns:
        anomaly_df.insert(0, "SK_ID_CURR", df["SK_ID_CURR"].astype(np.int64))

    anomaly_path = os.path.join(OUTPUT_DIR, "features_anomaly.csv")
    anomaly_df.to_csv(anomaly_path, index=False)
    log(f"  Saved unclipped anomaly-detection matrix -> {anomaly_path}")
    log_shape("features_anomaly", anomaly_df)

    return feature_df

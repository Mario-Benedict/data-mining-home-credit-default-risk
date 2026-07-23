"""
Pipeline configuration: paths, column lists, thresholds, and mappings.
All decisions here are grounded in EDA Section 10 (Justification Table).
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "datasets")
OUTPUT_DIR = os.path.join(BASE_DIR, "datasets", "final")

# Input paths
PATHS = {
    "application_train":    os.path.join(DATA_DIR, "application_train.csv"),
    "application_test":     os.path.join(DATA_DIR, "application_test.csv"),
    "bureau":               os.path.join(DATA_DIR, "bureau.csv"),
    "bureau_balance":       os.path.join(DATA_DIR, "bureau_balance.csv"),
    "previous_application": os.path.join(DATA_DIR, "previous_application.csv"),
    "POS_CASH_balance":     os.path.join(DATA_DIR, "POS_CASH_balance.csv"),
    "installments_payments":os.path.join(DATA_DIR, "installments_payments.csv"),
    "credit_card_balance":  os.path.join(DATA_DIR, "credit_card_balance.csv"),
}

# Sentinel value (EDA Section 4, 6)
# DAYS_EMPLOYED = 365243 encodes pensioners/unemployed; not a real duration.
# The train-only TARGET=1 rate differs across the sentinel and non-sentinel
# groups. This is descriptive and does not make the sentinel a risk rule.
DAYS_EMPLOYED_SENTINEL = 365_243

# Housing column triplication (EDA Section 7)
# AVG and MEDI variants are r > 0.99 correlated with MODE. Drop both.
# Only the quantitative measurement bases are triplicated.
BUILDING_BASES = [
    "APARTMENTS", "BASEMENTAREA", "YEARS_BEGINEXPLUATATION", "YEARS_BUILD",
    "COMMONAREA", "ELEVATORS", "ENTRANCES", "FLOORSMAX", "FLOORSMIN",
    "LANDAREA", "LIVINGAPARTMENTS", "LIVINGAREA", "NONLIVINGAPARTMENTS",
    "NONLIVINGAREA",
]
COLS_DROP_AVG  = [f"{b}_AVG"  for b in BUILDING_BASES]
COLS_DROP_MEDI = [f"{b}_MEDI" for b in BUILDING_BASES]
BUILDING_MODE_COLS = [f"{b}_MODE" for b in BUILDING_BASES] + ["TOTALAREA_MODE"]

# Redundant correlated features (EDA Section 7)
# OBS_60 r=0.998 with OBS_30 -> drop OBS_60.
# FLAG_EMP_PHONE r=-1.0 with DAYS_EMPLOYED (after sentinel) -> drop.
# FLAG_MOBIL is near-constant (all 1s) -> drop.
# REGION_RATING_CLIENT r>0.85 with REGION_RATING_CLIENT_W_CITY -> drop non-city variant.
COLS_DROP_REDUNDANT = [
    "OBS_60_CNT_SOCIAL_CIRCLE",
    "FLAG_EMP_PHONE",
    "FLAG_MOBIL",
    "REGION_RATING_CLIENT",
]

# DAYS_* columns to convert to positive years (EDA Section 4, 7)
# All stored as negative integers (days before application date).
DAYS_COLS = [
    "DAYS_BIRTH",
    "DAYS_EMPLOYED",
    "DAYS_REGISTRATION",
    "DAYS_ID_PUBLISH",
    "DAYS_LAST_PHONE_CHANGE",
]

# Rare income types to group (EDA Section 5)
# Total n=55 across 4 categories; too sparse for stable cluster membership.
RARE_INCOME_TYPES = ["Unemployed", "Student", "Businessman", "Maternity leave"]
RARE_INCOME_LABEL = "Other_Rare"

# ORGANIZATION_TYPE macro-sector mapping (EDA Section 5)
# 58 granular categories -> 12 meaningful sectors.
ORG_TYPE_MAP = {
    "Business Entity Type 1": "Private_Business",
    "Business Entity Type 2": "Private_Business",
    "Business Entity Type 3": "Private_Business",
    "Self-employed":          "Self_Employed",
    "Government":             "Government_Military",
    "Military":               "Government_Military",
    "Police":                 "Government_Military",
    "Security Ministries":    "Government_Military",
    "Security":               "Security",
    "Medicine":               "Healthcare",
    "School":                 "Education",
    "University":             "Education",
    "Kindergarten":           "Education",
    "Agriculture":            "Agriculture",
    "Transport: type 1":      "Transport",
    "Transport: type 2":      "Transport",
    "Transport: type 3":      "Transport",
    "Transport: type 4":      "Transport",
    "Trade: type 1":          "Trade",
    "Trade: type 2":          "Trade",
    "Trade: type 3":          "Trade",
    "Trade: type 4":          "Trade",
    "Trade: type 5":          "Trade",
    "Trade: type 6":          "Trade",
    "Trade: type 7":          "Trade",
    "Industry: type 1":       "Industry",
    "Industry: type 2":       "Industry",
    "Industry: type 3":       "Industry",
    "Industry: type 4":       "Industry",
    "Industry: type 5":       "Industry",
    "Industry: type 6":       "Industry",
    "Industry: type 7":       "Industry",
    "Industry: type 8":       "Industry",
    "Industry: type 9":       "Industry",
    "Industry: type 10":      "Industry",
    "Industry: type 11":      "Industry",
    "Industry: type 12":      "Industry",
    "Industry: type 13":      "Industry",
    "Construction":           "Construction",
    "Housing":                "Construction",
    "Bank":                   "Finance",
    "Insurance":              "Finance",
    "Restaurant":             "Services",
    "Hotel":                  "Services",
    "Culture":                "Services",
    "Religion":               "Services",
    "Advertising":            "Services",
    "Realtor":                "Services",
    "Legal Services":         "Services",
    "Services":               "Services",
    "Mobile":                 "Services",
    "Electricity":            "Utilities",
    "Telecom":                "Utilities",
    "Postal":                 "Utilities",
    "Cleaning":               "Utilities",
    "Emergency":              "Utilities",
    # "XNA" never reaches this map in practice: clean_structure converts XNA -> NaN
    # BEFORE applying the mapping, and encode_categoricals later fills that NaN with
    # "Unknown". The entry stays here so the map is complete if anyone
    # reuses it outside the pipeline order.
    "XNA":                    "Inapplicable",
    "Other":                  "Other",
}

# Outlier / winsorize / cap config (EDA Section 6)
# AMT_INCOME_TOTAL: p99 = 472,500; max = 117,000,000 (247x median).
# Cap first, then log-transform.
WINSORIZE_CONFIG = {
    "AMT_INCOME_TOTAL": 0.99,    # cap at p99
    "AMT_REQ_CREDIT_BUREAU_QRT": 0.99, # max=261, p99~5
    "AMT_REQ_CREDIT_BUREAU_MON": 0.99,
    "AMT_REQ_CREDIT_BUREAU_YEAR": 0.99,
}
# Household counts are rare at the upper tail, but rarity alone does not prove
# a capture error and no source rule supports a hard cap. They remain unchanged
# in the readable audit data and do not enter the governed clustering matrix.
CAP_CONFIG = {}

# Log-transform columns (EDA Section 4)
# Applied after winsorizing. All are right-skewed financial amounts.
LOG_TRANSFORM_COLS = [
    "AMT_INCOME_TOTAL", "AMT_CREDIT", "AMT_ANNUITY", "AMT_GOODS_PRICE",
]

# Missing value imputation strategy (EDA Section 3)
# Each decision is grounded in domain reasoning from EDA.

# Median imputation: numeric fields with MCAR / moderate missingness.
MEDIAN_IMPUTE_COLS = [
    "EXT_SOURCE_2",        # 0.21% missing; safe to median-impute
    "EXT_SOURCE_3",        # 19.83% missing; median impute after flag created
    "AMT_ANNUITY",         # 0.0% missing in train, small gap in test
    "AMT_GOODS_PRICE",     # 0.09% missing
    "CNT_FAM_MEMBERS",     # < 1% missing
    "DAYS_LAST_PHONE_CHANGE",
    "AMT_REQ_CREDIT_BUREAU_HOUR",
    "AMT_REQ_CREDIT_BUREAU_DAY",
    "AMT_REQ_CREDIT_BUREAU_WEEK",
    "AMT_REQ_CREDIT_BUREAU_MON",
    "AMT_REQ_CREDIT_BUREAU_QRT",
    "AMT_REQ_CREDIT_BUREAU_YEAR",
    "OBS_30_CNT_SOCIAL_CIRCLE",
    "DEF_30_CNT_SOCIAL_CIRCLE",
    "DEF_60_CNT_SOCIAL_CIRCLE",
]

# Zero imputation: structural absence means the quantity is 0.
# OWN_CAR_AGE: missing = no car, car age = 0.
# Building MODE cols: missing = no formal building record, measurement = 0.
ZERO_IMPUTE_COLS = ["OWN_CAR_AGE"] + BUILDING_MODE_COLS

# Mode imputation: categorical fields.
MODE_IMPUTE_COLS = ["NAME_TYPE_SUITE"]

# EXT_SOURCE_1: 56.4% missing. Impute with median AFTER creating FLAG_EXT_SOURCE_1_MISSING.
# OCCUPATION_TYPE: 31.4% missing. Imputed with mode per income type group in flag_and_impute_missing.

# Categorical fields with structural absence -> fill with explicit label.
CATEGORICAL_FILL_UNKNOWN = [
    "FONDKAPREMONT_MODE",
    "HOUSETYPE_MODE",
    "WALLSMATERIAL_MODE",
    "EMERGENCYSTATE_MODE",
]

# Phase 2 clustering feature set
# Every entry is traceable to EDA Section 10 Justification Table.
# Sections referenced: Section 4 (DAYS encoding), Section 5 (rare cats), Section 6 (outliers),
# Section 10 (justification table), Section 11-12 (EXT_SOURCE independence + age link),
# Section 13 (bureau absence), Section 14 (DEF_30 sub-population), Section 15 (installment DPD).
CLUSTERING_FEATURES = [
    # Financial capacity (EDA Section 6, Section 10: log transform + winsorise justified)
    "AMT_INCOME_TOTAL",          # log-transformed; winsorised at p99
    "AMT_CREDIT",                # log-transformed; skewness 1.2-1.6
    "AMT_ANNUITY",               # log-transformed
    "CREDIT_TO_INCOME",          # leverage ratio (derived from EDA-justified cols)
    "ANNUITY_TO_INCOME",         # debt-service burden ratio
    "CREDIT_TO_ANNUITY",         # payment-size proxy only; not contractual duration

    # Employment and product context.
    #
    # THE SPECIFIED PROTECTED AND HIGH-RISK PROXY ATTRIBUTES ARE EXCLUDED.
    # Removed here on purpose: CODE_GENDER, YEARS_BIRTH (age), CNT_CHILDREN
    # (familial status), REGION_RATING_CLIENT_W_CITY (geographic proxy /
    # redlining risk), NAME_EDUCATION_TYPE, NAME_INCOME_TYPE_FREQ and
    # ORGANIZATION_TYPE_FREQ (socioeconomic proxies), and
    # DEF_30_CNT_SOCIAL_CIRCLE_BIN (guilt-by-association: the applicant's
    # acquaintances' arrears are not the applicant's conduct).
    #
    # The same governance should apply throughout the mining work. Phase 3
    # already rejects protected and life-stage vocabulary from its rules, so
    # these fields should not shape the segmentation that drives review actions.
    #
    # All of these remain in features_business.csv. They are still used to
    # PROFILE and DESCRIBE segments after the fact, and for fairness
    # monitoring. They simply do not get to FORM the segments.
    "YEARS_EMPLOYED",            # abs(DAYS_EMPLOYED)/365; 0 for sentinel rows
    # Structural missingness flag retained so the placeholder is not treated as
    # a real duration. It is a potential life-stage proxy and therefore needs a
    # fairness sensitivity check before any operational use.
    "FLAG_SENTINEL_EMPLOYED",
    "NAME_CONTRACT_TYPE",        # binary Cash=1 Revolving=0
    "OWN_CAR_AGE",               # 0 for no-car applicants (structural imputation)
    "FLAG_NO_CAR",               # EDA Section 10: missingness = no car; binary indicator
    "FLAG_NO_HOUSING_DATA",      # EDA Section 10: 47-70% housing cols absent -> single indicator

    # Opaque external scores. Pairwise correlation is modest, but that does not
    # prove independent source construction or justify double-counting.
    "EXT_SOURCE_1",              # 54.4% missing in combined data -> median + flag
    "EXT_SOURCE_2",
    "EXT_SOURCE_3",
    "FLAG_EXT_SOURCE_1_MISSING", # score unavailable: uncertainty indicator
    "FLAG_EXT_SOURCE_2_MISSING",
    "FLAG_EXT_SOURCE_3_MISSING",

    # Credit enquiry frequency
    "AMT_REQ_CREDIT_BUREAU_YEAR", # winsorised at p99 (EDA Section 10)

    # Bureau evidence availability and observed history
    "FLAG_NO_BUREAU",            # 50,444/356,255 combined applications (14.16%)
    "BUREAU_COUNT",              # credit history depth
    "BUREAU_ACTIVE_RATIO",       # share of bureau records marked active at extract
    "BUREAU_DEBT_TO_CREDIT_RATIO",# external debt burden
    "BUREAU_DAYS_CREDIT_MEAN",   # average age of credit lines
    "BUREAU_BB_DPD_RATIO_MEAN",  # share of months with any DPD
    "BUREAU_BB_SEVERE_DPD_MEAN", # share of months with 90+ DPD

    # Previous applications (behavioural depth signal)
    "PREV_COUNT",                # breadth of prior Home Credit engagement
    "PREV_APPROVAL_RATE",        # historical approval signal
    "PREV_REFUSED_COUNT",        # refusal history - risk signal

    # Installment repayment (EDA Section 15: 8.4% late; "mean DPD, max DPD,
    #   pct late, pct severely late >30d" prescribed in justification table)
    "INST_DPD_MEAN",
    "INST_DPD_MAX",
    "INST_COUNT",                 # distinguishes clean observed history from no history
    "INST_LATE_RATIO",
    "INST_SEVERE_LATE_RATIO",    # >30d DPD
    "INST_PAYMENT_RATIO_MEAN",   # mean(paid/owed) - underpayment signal

    # POS / Cash loans
    "POS_SK_DPD_MEAN",
    "POS_MONTHS_COUNT",

    # Credit card (EDA Section 10: "mean and max utilization; months of history")
    "CC_UTILIZATION_MEAN",
    "CC_UTILIZATION_MAX",
    "CC_SK_DPD_MEAN",
    "CC_AMT_BALANCE_MEAN",
    "CC_MONTHS_COUNT",

    # No encoded socioeconomic categoricals here by design. NAME_EDUCATION_TYPE,
    # NAME_INCOME_TYPE_FREQ and ORGANIZATION_TYPE_FREQ are still produced by the
    # encoding steps and kept in the business artifact for profiling, but they
    # are proxies for socioeconomic status and do not shape the segments.
    #
    # Frequency encoding had a second problem worth recording: it maps a
    # category to how common it is, so two unrelated sectors with similar
    # frequency collapse onto the same coordinate. That manufactures similarity
    # between applicants who have nothing in common.
]

# Categorical encoding for DISTANCE-BASED clustering
# Why not one-hot encoding (OHE)?
#  K-Means works on Euclidean distance. OHE turns one nominal column into N
#  binary columns, which (a) inflates dimensionality with sparse axes, and
#  (b) forces every pair of categories to sit at the SAME distance sqrt2 apart,
#  even when some categories are far more alike than others. For a 12-sector
#  ORGANIZATION_TYPE that means ~11 extra axes that collectively outweigh a
#  single standardized continuous feature. An earlier run also produced a
#  perfectly collinear trio (FLAG_SENTINEL_EMPLOYED == ORGANIZATION_TYPE_Unknown
#  == NAME_INCOME_TYPE_Pensioner, r ~ 1.0) - a direct symptom of OHE on a
#  nominal whose "missing" category coincides with another flag.
#
# Encoding chosen per variable, matched to what the variable actually is:

# 1) ORDINAL - NAME_EDUCATION_TYPE has a real ladder (junior school -> degree).
#   A single ordered integer preserves "Higher education is closer to
#   Incomplete higher than to Lower secondary", which OHE destroys.
EDUCATION_ORDINAL = {
    "Lower secondary":                0,
    "Secondary / secondary special":  1,
    "Incomplete higher":              2,
    "Higher education":               3,
    "Academic degree":                4,
}
# Fallback level if a value is missing/unseen: the population mode (Secondary).
EDUCATION_DEFAULT_LEVEL = 1
ORDINAL_ENCODE_COLS = {"NAME_EDUCATION_TYPE": EDUCATION_ORDINAL}

# 2) FREQUENCY - NAME_INCOME_TYPE and ORGANIZATION_TYPE are nominal with no
#   natural order. Frequency encoding maps each category to how common it is
#   in the population, collapsing the whole variable into ONE continuous
#   "mainstream  to  niche" axis. It keeps the signal that matters for
#   segmentation (typical vs unusual employment/income source) without the
#   dimensionality blow-up. Computed on the full train+test pool (unsupervised,
#   no leakage). Pensioners remain separately identified by
#   FLAG_SENTINEL_EMPLOYED, so the residual overlap is small, not r~1.0.
FREQUENCY_ENCODE_COLS = {
    "NAME_INCOME_TYPE":  "NAME_INCOME_TYPE_FREQ",
    "ORGANIZATION_TYPE": "ORGANIZATION_TYPE_FREQ",
}

# Ordinal encoding for DEF_30_CNT_SOCIAL_CIRCLE_BIN (ordered: 0 < 1 < 2+).
# Same principle as education: the ordering is real, OHE would discard it.
DEF30_BIN_ORDINAL = {"0": 0, "1": 1, "2+": 2}

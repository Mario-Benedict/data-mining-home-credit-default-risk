"""
Step 2 — Aggregate all five relational tables to one row per SK_ID_CURR.

EDA Section 8 established what behavioral dimension each table contributes:
  bureau            → external credit history depth and quality
  bureau_balance    → monthly repayment quality over time (linked via SK_ID_BUREAU)
  previous_application → historical application behavior and outcomes
  POS_CASH_balance  → POS/cash loan repayment snapshots
  installments_payments → actual installment repayment behavior (DPD)
  credit_card_balance → revolving credit utilization patterns

Each aggregation uses only features that add behavioral signal beyond the
main application table. Raw temporal tables are never joined directly;
they are always aggregated first.
"""
import numpy as np
import pandas as pd
from .utils import log, log_shape


# ── Bureau + Bureau Balance ────────────────────────────────────────────────

def _aggregate_bureau_balance(bureau_bal: pd.DataFrame) -> pd.DataFrame:
    """
    Roll up bureau_balance (monthly snapshots per bureau record) to
    one row per SK_ID_BUREAU.

    STATUS encoding:
      C  = closed credit
      0  = on-time (0 DPD)
      X  = unknown / data not available
      1  = 1–29 DPD
      2  = 30–59 DPD
      3  = 60–89 DPD
      4  = 90–119 DPD
      5  = 120+ DPD (severe delinquency)
    """
    bb = bureau_bal.copy()
    bb["DPD_FLAG"] = bb["STATUS"].isin(["1", "2", "3", "4", "5"]).astype(np.int8)
    bb["SEVERE_DPD_FLAG"] = bb["STATUS"].isin(["4", "5"]).astype(np.int8)

    bb_agg = bb.groupby("SK_ID_BUREAU").agg(
        BB_MONTHS_COUNT        = ("MONTHS_BALANCE", "count"),
        BB_DPD_RATIO           = ("DPD_FLAG",        "mean"),   # share of months with any DPD
        BB_SEVERE_DPD_RATIO    = ("SEVERE_DPD_FLAG", "mean"),   # share with 90+ DPD
        BB_MONTHS_BALANCE_MIN  = ("MONTHS_BALANCE",  "min"),    # earliest month observed
    ).reset_index()
    return bb_agg


def aggregate_bureau(bureau: pd.DataFrame, bureau_bal: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate bureau records to one row per SK_ID_CURR.

    Key features produced:
      BUREAU_COUNT             — credit history depth
      BUREAU_ACTIVE_COUNT/RATIO — current leverage level
      BUREAU_CREDIT_SUM/DEBT   — total external debt exposure
      BUREAU_DAYS_CREDIT_MEAN  — average age of credit lines
      BB_DPD/SEVERE_DPD_RATIO  — historical repayment quality
    """
    log("  Aggregating bureau_balance ...")
    bb_agg = _aggregate_bureau_balance(bureau_bal)

    bur = bureau.merge(bb_agg, on="SK_ID_BUREAU", how="left")

    log("  Aggregating bureau to applicant level ...")
    agg = bur.groupby("SK_ID_CURR").agg(
        BUREAU_COUNT                = ("SK_ID_BUREAU",          "count"),
        BUREAU_ACTIVE_COUNT         = ("CREDIT_ACTIVE",         lambda x: (x == "Active").sum()),
        BUREAU_CLOSED_COUNT         = ("CREDIT_ACTIVE",         lambda x: (x == "Closed").sum()),
        BUREAU_CREDIT_SUM           = ("AMT_CREDIT_SUM",        "sum"),
        BUREAU_CREDIT_SUM_DEBT      = ("AMT_CREDIT_SUM_DEBT",   "sum"),
        BUREAU_CREDIT_SUM_OVERDUE   = ("AMT_CREDIT_SUM_OVERDUE","sum"),
        BUREAU_DAYS_CREDIT_MEAN     = ("DAYS_CREDIT",           "mean"),
        BUREAU_DAYS_CREDIT_MAX      = ("DAYS_CREDIT",           "max"),   # most recent credit start
        BUREAU_DAYS_ENDDATE_MEAN    = ("DAYS_CREDIT_ENDDATE",   "mean"),
        BUREAU_CREDIT_TYPE_NUNIQUE  = ("CREDIT_TYPE",           "nunique"),
        BUREAU_BB_MONTHS_MEAN       = ("BB_MONTHS_COUNT",       "mean"),
        BUREAU_BB_DPD_RATIO_MEAN    = ("BB_DPD_RATIO",          "mean"),
        BUREAU_BB_SEVERE_DPD_MEAN   = ("BB_SEVERE_DPD_RATIO",   "mean"),
    ).reset_index()

    agg["BUREAU_ACTIVE_RATIO"] = (
        agg["BUREAU_ACTIVE_COUNT"] / agg["BUREAU_COUNT"].replace(0, np.nan)
    )
    agg["BUREAU_DEBT_TO_CREDIT_RATIO"] = (
        agg["BUREAU_CREDIT_SUM_DEBT"] / agg["BUREAU_CREDIT_SUM"].replace(0, np.nan)
    )
    log_shape("bureau_agg", agg)
    return agg


# ── Previous Application ───────────────────────────────────────────────────

def aggregate_previous(prev: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate previous_application to one row per SK_ID_CURR.

    Key features produced:
      PREV_COUNT             — breadth of prior engagement with Home Credit
      PREV_APPROVAL_RATE     — historical approval signal
      PREV_REFUSED_COUNT     — refusal history (risk signal)
      PREV_AMT_APPLICATION_MEAN — typical amount sought
      PREV_DAYS_DECISION_MIN — days since most recent application decision
    """
    log("  Aggregating previous_application ...")

    # Days since most recent decision (min = closest to application date)
    # DAYS_DECISION is stored as negative (days before current application)
    agg = prev.groupby("SK_ID_CURR").agg(
        PREV_COUNT                = ("SK_ID_PREV",             "count"),
        PREV_APPROVED_COUNT       = ("NAME_CONTRACT_STATUS",   lambda x: (x == "Approved").sum()),
        PREV_REFUSED_COUNT        = ("NAME_CONTRACT_STATUS",   lambda x: (x == "Refused").sum()),
        PREV_CANCELED_COUNT       = ("NAME_CONTRACT_STATUS",   lambda x: (x == "Canceled").sum()),
        PREV_AMT_APPLICATION_MEAN = ("AMT_APPLICATION",        "mean"),
        PREV_AMT_CREDIT_MEAN      = ("AMT_CREDIT",             "mean"),
        PREV_AMT_CREDIT_MAX       = ("AMT_CREDIT",             "max"),
        PREV_DAYS_DECISION_MEAN   = ("DAYS_DECISION",          "mean"),
        PREV_DAYS_DECISION_MIN    = ("DAYS_DECISION",          "min"),   # most recent
        PREV_RATE_DOWN_PAYMENT_MEAN = ("RATE_DOWN_PAYMENT",   "mean"),
        PREV_CNT_PAYMENT_MEAN     = ("CNT_PAYMENT",            "mean"),
        PREV_DAYS_FIRST_DRAWING_MEAN = ("DAYS_FIRST_DRAWING", "mean"),
    ).reset_index()

    agg["PREV_APPROVAL_RATE"] = (
        agg["PREV_APPROVED_COUNT"] / agg["PREV_COUNT"].replace(0, np.nan)
    )
    log_shape("prev_agg", agg)
    return agg


# ── POS CASH Balance ───────────────────────────────────────────────────────

def aggregate_pos(pos: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate POS_CASH_balance to one row per SK_ID_CURR.

    Key features produced:
      POS_MONTHS_COUNT      — depth of POS/cash history
      POS_SK_DPD_MEAN/MAX   — repayment quality on POS/cash loans
      POS_INSTALMENT_FUTURE — remaining loan burden signal
    """
    log("  Aggregating POS_CASH_balance ...")
    agg = pos.groupby("SK_ID_CURR").agg(
        POS_MONTHS_COUNT             = ("MONTHS_BALANCE",        "count"),
        POS_SK_DPD_MEAN              = ("SK_DPD",                "mean"),
        POS_SK_DPD_DEF_MEAN          = ("SK_DPD_DEF",            "mean"),
        POS_SK_DPD_MAX               = ("SK_DPD",                "max"),
        POS_CNT_INSTALMENT_FUTURE_MEAN = ("CNT_INSTALMENT_FUTURE", "mean"),
        POS_COMPLETED_COUNT          = ("NAME_CONTRACT_STATUS",  lambda x: (x == "Completed").sum()),
        POS_ACTIVE_COUNT             = ("NAME_CONTRACT_STATUS",  lambda x: (x == "Active").sum()),
    ).reset_index()

    log_shape("pos_agg", agg)
    return agg


# ── Installments Payments ──────────────────────────────────────────────────

def aggregate_installments(inst: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate installments_payments to one row per SK_ID_CURR.

    DPD (days past due) is the most important signal here.
    EDA Section 8: 8.4% of installments were late (DPD > 0);
    applicants at the extreme right tail of DPD are in sustained default.

    Key features produced:
      INST_DPD_MEAN/MAX        — repayment timeliness
      INST_LATE_RATIO          — share of payments that were late
      INST_SEVERE_LATE_RATIO   — share late >30 days (serious delinquency)
      INST_PAYMENT_RATIO_MEAN  — mean(paid / owed) — underpayment signal
    """
    log("  Aggregating installments_payments ...")
    inst = inst.copy()
    # Positive DPD: payment made after due date
    inst["DPD"] = (inst["DAYS_ENTRY_PAYMENT"] - inst["DAYS_INSTALMENT"]).clip(lower=0)
    inst["LATE_FLAG"]        = (inst["DPD"] > 0).astype(np.int8)
    inst["SEVERE_LATE_FLAG"] = (inst["DPD"] > 30).astype(np.int8)
    # Payment ratio: how much was paid relative to what was owed
    inst["PAYMENT_RATIO"] = inst["AMT_PAYMENT"] / inst["AMT_INSTALMENT"].replace(0, np.nan)

    agg = inst.groupby("SK_ID_CURR").agg(
        INST_COUNT                = ("SK_ID_PREV",      "count"),
        INST_DPD_MEAN             = ("DPD",              "mean"),
        INST_DPD_MAX              = ("DPD",              "max"),
        INST_LATE_RATIO           = ("LATE_FLAG",        "mean"),
        INST_SEVERE_LATE_RATIO    = ("SEVERE_LATE_FLAG", "mean"),
        INST_PAYMENT_RATIO_MEAN   = ("PAYMENT_RATIO",    "mean"),
        INST_PAYMENT_RATIO_MIN    = ("PAYMENT_RATIO",    "min"),   # worst underpayment episode
        INST_AMT_PAYMENT_SUM      = ("AMT_PAYMENT",      "sum"),
    ).reset_index()

    log_shape("inst_agg", agg)
    return agg


# ── Credit Card Balance ────────────────────────────────────────────────────

def aggregate_creditcard(cc: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate credit_card_balance to one row per SK_ID_CURR.

    EDA Section 8: mean CC utilization is an important revolving credit signal.
    Utilization > 80% is a classic indicator of financial stress.

    Key features produced:
      CC_UTILIZATION_MEAN/MAX — revolving credit usage intensity
      CC_AMT_BALANCE_MEAN     — average revolving debt level
      CC_SK_DPD_MEAN/MAX      — CC repayment quality
      CC_MONTHS_COUNT         — depth of CC history
    """
    log("  Aggregating credit_card_balance ...")
    cc = cc.copy()
    cc["UTILIZATION"] = (
        cc["AMT_BALANCE"] / cc["AMT_CREDIT_LIMIT_ACTUAL"].replace(0, np.nan)
    ).clip(upper=2.0)   # cap at 200% to handle rare over-limit entries

    agg = cc.groupby("SK_ID_CURR").agg(
        CC_MONTHS_COUNT            = ("MONTHS_BALANCE",          "count"),
        CC_AMT_BALANCE_MEAN        = ("AMT_BALANCE",             "mean"),
        CC_AMT_BALANCE_MAX         = ("AMT_BALANCE",             "max"),
        CC_UTILIZATION_MEAN        = ("UTILIZATION",             "mean"),
        CC_UTILIZATION_MAX         = ("UTILIZATION",             "max"),
        CC_AMT_DRAWINGS_TOTAL_MEAN = ("AMT_DRAWINGS_CURRENT",        "mean"),
        CC_AMT_DRAWINGS_ATM_MEAN   = ("AMT_DRAWINGS_ATM_CURRENT",   "mean"),
        CC_SK_DPD_MEAN             = ("SK_DPD",                      "mean"),
        CC_SK_DPD_MAX              = ("SK_DPD",                      "max"),
        CC_CNT_INSTALMENT_MATURE_MEAN = ("CNT_INSTALMENT_MATURE_CUM","mean"),
    ).reset_index()

    log_shape("cc_agg", agg)
    return agg


# ── Orchestrator ───────────────────────────────────────────────────────────

def run(dfs: dict) -> dict:
    """Aggregate all five relational tables. Returns dict of aggregated DFs."""
    log("Step 2 — Aggregating relational tables ...")
    return {
        "bureau_agg": aggregate_bureau(dfs["bureau"], dfs["bureau_balance"]),
        "prev_agg":   aggregate_previous(dfs["previous_application"]),
        "pos_agg":    aggregate_pos(dfs["POS_CASH_balance"]),
        "inst_agg":   aggregate_installments(dfs["installments_payments"]),
        "cc_agg":     aggregate_creditcard(dfs["credit_card_balance"]),
    }

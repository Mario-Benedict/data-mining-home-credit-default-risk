"""Shared logging utility for the pipeline."""
import sys
from datetime import datetime


def log(msg: str, level: str = "INFO") -> None:
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] [{level}] {msg}", flush=True)


def log_shape(name: str, df) -> None:
    log(f"{name}: {df.shape[0]:,} rows × {df.shape[1]} cols")


def log_missing(df, label: str = "") -> None:
    n_missing = df.isnull().sum().sum()
    pct = n_missing / (df.shape[0] * df.shape[1]) * 100
    log(f"{label} — remaining NaNs: {n_missing:,} ({pct:.2f}% of all cells)")

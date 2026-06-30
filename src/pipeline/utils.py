"""Shared logging utility for the pipeline."""
import sys
from datetime import datetime

# Ensure UTF-8 output on Windows consoles (handles arrows, em-dashes, etc.)
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


def log(msg: str, level: str = "INFO") -> None:
    ts = datetime.now().strftime("%H:%M:%S")
    try:
        print(f"[{ts}] [{level}] {msg}", flush=True)
    except UnicodeEncodeError:
        safe = msg.encode("ascii", errors="replace").decode("ascii")
        print(f"[{ts}] [{level}] {safe}", flush=True)


def log_shape(name: str, df) -> None:
    log(f"{name}: {df.shape[0]:,} rows x {df.shape[1]} cols")


def log_missing(df, label: str = "") -> None:
    n_missing = df.isnull().sum().sum()
    pct = n_missing / (df.shape[0] * df.shape[1]) * 100
    log(f"{label} - remaining NaNs: {n_missing:,} ({pct:.2f}% of all cells)")

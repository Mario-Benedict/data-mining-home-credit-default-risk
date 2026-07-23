"""
Load all CSV files.

Validates that each file exists and prints shapes for audit.
No transformation is applied here.
"""
import pandas as pd
from .config import PATHS
from .utils import log, log_shape


def run() -> dict:
    """Load all dataset CSV files. Returns dict of {name: DataFrame}."""
    dfs = {}
    for name, path in PATHS.items():
        log(f"Loading {name} ...")
        df = pd.read_csv(path, low_memory=False)
        dfs[name] = df
        log_shape(name, df)

    log("All files loaded.")
    log(f"  application_train + test combined will yield "
        f"{len(dfs['application_train']) + len(dfs['application_test']):,} rows.")
    return dfs

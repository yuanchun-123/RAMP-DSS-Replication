"""Data preparation helpers for the RAMP benchmark sample."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

REQUIRED_COLUMNS = ("timestamp", "uid", "campaign", "conversion", "click")


def load_criteo(path: Path) -> pd.DataFrame:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(
            f"Raw Criteo data not found at {path}. Place the file under data/raw/ "
            "or set RAMP_DATA_PATH."
        )
    compression = "gzip" if path.suffix == ".gz" else None
    return pd.read_csv(path, sep="\t", compression=compression)


def normalize_time_columns(df: pd.DataFrame) -> pd.DataFrame:
    work = df.copy()
    work["timestamp_sec"] = pd.to_numeric(work["timestamp"], errors="coerce")
    if "conversion_timestamp" in work.columns:
        conv_ts = pd.to_numeric(work["conversion_timestamp"], errors="coerce")
        work["conversion_timestamp_sec"] = conv_ts.where(conv_ts != -1)
    else:
        work["conversion_timestamp_sec"] = np.nan
    return work


def clean_criteo_fields(df: pd.DataFrame) -> pd.DataFrame:
    work = normalize_time_columns(df)
    work = work.dropna(subset=["timestamp_sec", "uid", "campaign"]).copy()
    work["click"] = (pd.to_numeric(work["click"], errors="coerce").fillna(0) > 0).astype(int)
    work["conversion"] = (
        pd.to_numeric(work["conversion"], errors="coerce").fillna(0) > 0
    ).astype(int)

    for col in [c for c in work.columns if c.startswith("cat")]:
        work[col] = work[col].mask(work[col].astype(str).eq("-1"))

    numeric_sentinel_cols = ["click_pos", "click_nb", "cost", "cpo", "time_since_last_click"]
    for col in numeric_sentinel_cols:
        if col in work.columns:
            work[col] = pd.to_numeric(work[col], errors="coerce")
            work[col] = work[col].mask(work[col].eq(-1))

    return work.sort_values(["uid", "timestamp_sec"]).reset_index(drop=True)


def add_forward_and_placebo_windows(df: pd.DataFrame, horizon_hours: float = 24.0) -> pd.DataFrame:
    work = df.copy()
    horizon = horizon_hours * 3600.0
    conversion_time = work["conversion_timestamp_sec"].where(
        work["conversion_timestamp_sec"].notna(), work["timestamp_sec"]
    )
    conversion_time = conversion_time.where(work["conversion"].eq(1))
    work["next_conversion_sec"] = conversion_time.groupby(work["uid"]).shift(-1).groupby(work["uid"]).bfill()
    work["previous_conversion_sec"] = conversion_time.groupby(work["uid"]).ffill()
    work["forward_conversion_24h"] = (
        (work["next_conversion_sec"] > work["timestamp_sec"])
        & (work["next_conversion_sec"] <= work["timestamp_sec"] + horizon)
    ).astype(int)
    work["placebo_conversion_24h"] = (
        (work["previous_conversion_sec"] < work["timestamp_sec"])
        & (work["previous_conversion_sec"] >= work["timestamp_sec"] - horizon)
    ).astype(int)
    return work


def build_benchmark_sample(raw: pd.DataFrame, horizon_hours: float = 24.0) -> pd.DataFrame:
    clean = clean_criteo_fields(raw)
    sample = add_forward_and_placebo_windows(clean, horizon_hours=horizon_hours)
    return sample.loc[sample["conversion"].eq(0)].reset_index(drop=True)


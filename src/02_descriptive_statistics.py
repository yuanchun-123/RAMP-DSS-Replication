"""Descriptive statistics used to orient the replication data."""

from __future__ import annotations

import pandas as pd


def dataset_snapshot(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for col in df.columns:
        rows.append(
            {
                "column": col,
                "dtype": str(df[col].dtype),
                "missing": int(df[col].isna().sum()),
                "n_unique": int(df[col].nunique(dropna=True)),
            }
        )
    return pd.DataFrame(rows)


def core_counts(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "rows": int(len(df)),
                "users": int(df["uid"].nunique()),
                "campaigns": int(df["campaign"].nunique()),
                "click_rate": float(df["click"].mean()),
                "conversion_rate": float(df["conversion"].mean()),
            }
        ]
    )


def campaign_summary(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("campaign", observed=True)
        .agg(
            impressions=("campaign", "size"),
            users=("uid", "nunique"),
            click_rate=("click", "mean"),
            conversion_rate=("conversion", "mean"),
        )
        .reset_index()
        .sort_values("impressions", ascending=False)
    )


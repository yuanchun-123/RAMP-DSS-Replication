"""Time-split decision simulation helpers."""

from __future__ import annotations

import pandas as pd


def train_future_split(df: pd.DataFrame, split_quantile: float = 0.7) -> tuple[pd.DataFrame, pd.DataFrame]:
    cutoff = df["timestamp_sec"].quantile(split_quantile)
    train = df.loc[df["timestamp_sec"] <= cutoff].copy()
    future = df.loc[df["timestamp_sec"] > cutoff].copy()
    return train, future


def future_diagnostic_performance(
    campaign_scores: pd.DataFrame,
    future_df: pd.DataFrame,
    top_k_values: tuple[int, ...] = (5, 10, 20),
) -> pd.DataFrame:
    future_campaign = (
        future_df.groupby("campaign", observed=True)
        .agg(
            future_impressions=("campaign", "size"),
            future_conversion_rate=("forward_conversion_24h", "mean"),
            future_click_rate=("click", "mean"),
        )
        .reset_index()
    )
    ranked = campaign_scores.merge(future_campaign, on="campaign", how="left")
    rows = []
    for k in top_k_values:
        selected = ranked.nsmallest(k, "diagnostic_rank")
        rows.append(
            {
                "k": k,
                "selected_campaigns": int(selected["campaign"].nunique()),
                "future_conversion_rate": float(selected["future_conversion_rate"].mean()),
                "future_click_rate": float(selected["future_click_rate"].mean()),
            }
        )
    return pd.DataFrame(rows)


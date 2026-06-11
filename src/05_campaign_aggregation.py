"""Campaign-level aggregation for RAMP Layer 3."""

from __future__ import annotations

import pandas as pd


def campaign_diagnostic_scores(df: pd.DataFrame) -> pd.DataFrame:
    out = (
        df.groupby("campaign", observed=True)
        .agg(
            impressions=("campaign", "size"),
            users=("uid", "nunique"),
            click_rate=("click", "mean"),
            forward_conversion_rate=("forward_conversion_24h", "mean"),
            placebo_conversion_rate=("placebo_conversion_24h", "mean"),
            avg_click_propensity=("click_propensity", "mean"),
        )
        .reset_index()
    )
    out["campaign_level_diagnostic_score"] = (
        out["forward_conversion_rate"] - out["placebo_conversion_rate"]
    )
    out["diagnostic_rank"] = out["campaign_level_diagnostic_score"].rank(
        ascending=False, method="dense"
    )
    out["click_rank"] = out["click_rate"].rank(ascending=False, method="dense")
    return out.sort_values("diagnostic_rank")


def reprioritization_metrics(campaign_df: pd.DataFrame, top_k: int = 20) -> pd.DataFrame:
    diagnostic_top = set(campaign_df.nsmallest(top_k, "diagnostic_rank")["campaign"])
    click_top = set(campaign_df.nsmallest(top_k, "click_rank")["campaign"])
    return pd.DataFrame(
        [
            {
                "comparison": "diagnostic_vs_click",
                "k": top_k,
                "n_campaigns": int(len(campaign_df)),
                "topk_overlap": int(len(diagnostic_top.intersection(click_top))),
                "topk_overlap_share": float(len(diagnostic_top.intersection(click_top)) / top_k),
                "spearman_rank_corr": float(
                    campaign_df[["diagnostic_rank", "click_rank"]].corr(method="spearman").iloc[0, 1]
                ),
            }
        ]
    )


"""Diagnostic tests for attribution reliability checks."""

from __future__ import annotations

import pandas as pd


def overlap_diagnostics(df: pd.DataFrame, propensity_col: str = "click_propensity") -> pd.DataFrame:
    p = df[propensity_col]
    return pd.DataFrame(
        [
            {
                "n_rows": int(len(df)),
                "min_propensity": float(p.min()),
                "p01_propensity": float(p.quantile(0.01)),
                "median_propensity": float(p.median()),
                "p99_propensity": float(p.quantile(0.99)),
                "max_propensity": float(p.max()),
                "share_below_0_01": float((p < 0.01).mean()),
                "share_above_0_99": float((p > 0.99).mean()),
            }
        ]
    )


def placebo_summary(df: pd.DataFrame) -> pd.DataFrame:
    clicked = df["click"].eq(1)
    return pd.DataFrame(
        [
            {
                "diagnostic": "placebo_conversion_24h",
                "clicked_mean": float(df.loc[clicked, "placebo_conversion_24h"].mean()),
                "not_clicked_mean": float(df.loc[~clicked, "placebo_conversion_24h"].mean()),
                "raw_difference": float(
                    df.loc[clicked, "placebo_conversion_24h"].mean()
                    - df.loc[~clicked, "placebo_conversion_24h"].mean()
                ),
            }
        ]
    )


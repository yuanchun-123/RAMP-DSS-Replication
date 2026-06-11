"""Diagnostic gate rules for RAMP Layer 4."""

from __future__ import annotations

import pandas as pd


def apply_diagnostic_gate(
    campaign_df: pd.DataFrame,
    min_impressions: int = 1000,
    max_placebo_rate: float | None = None,
) -> pd.DataFrame:
    out = campaign_df.copy()
    out["gate_support"] = out["impressions"] >= min_impressions
    if max_placebo_rate is None:
        max_placebo_rate = float(out["placebo_conversion_rate"].quantile(0.75))
    out["gate_placebo"] = out["placebo_conversion_rate"] <= max_placebo_rate
    out["gate_all"] = out["gate_support"] & out["gate_placebo"]
    return out


def gate_funnel(gated_df: pd.DataFrame) -> pd.DataFrame:
    total = len(gated_df)
    rows = [
        ("all_campaigns", total),
        ("support_gate", int(gated_df["gate_support"].sum())),
        ("placebo_gate", int((gated_df["gate_support"] & gated_df["gate_placebo"]).sum())),
        ("all_gates", int(gated_df["gate_all"].sum())),
    ]
    return pd.DataFrame(
        [
            {
                "gate_step": name,
                "n_campaigns_remaining": count,
                "share_of_all": float(count / total) if total else 0.0,
            }
            for name, count in rows
        ]
    )


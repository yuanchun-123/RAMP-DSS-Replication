"""Selection-adjusted benchmark helpers for RAMP Layer 1."""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def feature_columns(df: pd.DataFrame) -> tuple[list[str], list[str]]:
    categorical = [c for c in df.columns if c.startswith("cat")]
    numeric = [
        c
        for c in ["cost", "cpo", "time_since_last_click", "click_pos", "click_nb"]
        if c in df.columns
    ]
    return categorical, numeric


def fit_click_propensity(df: pd.DataFrame) -> Pipeline:
    categorical, numeric = feature_columns(df)
    transformer = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore", min_frequency=50), categorical),
            ("num", StandardScaler(), numeric),
        ],
        remainder="drop",
    )
    model = LogisticRegression(max_iter=500, n_jobs=-1)
    pipe = Pipeline([("features", transformer), ("model", model)])
    pipe.fit(df[categorical + numeric], df["click"])
    return pipe


def propensity_scores(model: Pipeline, df: pd.DataFrame) -> np.ndarray:
    categorical, numeric = feature_columns(df)
    return model.predict_proba(df[categorical + numeric])[:, 1]


def selection_adjusted_summary(
    df: pd.DataFrame,
    score_col: str = "forward_conversion_24h",
    propensity_col: str = "click_propensity",
    trim: tuple[float, float] = (0.01, 0.99),
) -> pd.DataFrame:
    work = df.copy()
    p = work[propensity_col].clip(trim[0], trim[1])
    d = work["click"].astype(float)
    y = work[score_col].astype(float)
    treated = d.eq(1)
    control = d.eq(0)
    treated_mean = y[treated].mean()
    control_weighted = np.average(y[control], weights=(p[control] / (1.0 - p[control])))
    return pd.DataFrame(
        [
            {
                "horizon": score_col,
                "n_rows": int(len(work)),
                "n_clicked": int(treated.sum()),
                "mean_clicked": float(treated_mean),
                "selection_adjusted_control_mean": float(control_weighted),
                "diagnostic_signal": float(treated_mean - control_weighted),
                "propensity_trim_low": trim[0],
                "propensity_trim_high": trim[1],
            }
        ]
    )


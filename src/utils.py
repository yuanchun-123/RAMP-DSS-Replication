"""Small utilities used by the RAMP replication scripts."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Iterable

import pandas as pd


def load_module(module_path: Path, name: str | None = None):
    module_path = Path(module_path)
    module_name = name or module_path.stem.replace("-", "_")
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module from {module_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def require_columns(df: pd.DataFrame, columns: Iterable[str]) -> None:
    missing = sorted(set(columns).difference(df.columns))
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def save_table(df: pd.DataFrame, path: Path) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return path


def save_json(obj: dict, path: Path) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2))
    return path


def list_outputs(path: Path, suffixes: tuple[str, ...]) -> list[Path]:
    if not Path(path).exists():
        return []
    return sorted(p for p in Path(path).rglob("*") if p.suffix.lower() in suffixes)

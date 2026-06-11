"""Shared paths and defaults for the RAMP DSS replication package."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


EXPECTED_RAW_FILENAMES = (
    "pcb_dataset_final.tsv",
    "criteo_attribution_dataset.tsv",
    "criteo_attribution.tsv",
    "criteo_attribution_dataset.tsv.gz",
)


@dataclass(frozen=True)
class PipelineConfig:
    repo_root: Path
    raw_data_dir: Path
    processed_data_dir: Path
    table_dir: Path
    figure_dir: Path
    notebook_path: Path
    data_path: Path
    horizon_hours: float = 24.0
    random_state: int = 2026


def repo_root_from_here() -> Path:
    return Path(__file__).resolve().parents[1]


def find_data_path(raw_data_dir: Path) -> Path:
    env_path = os.environ.get("RAMP_DATA_PATH")
    if env_path:
        return Path(env_path).expanduser().resolve()

    for name in EXPECTED_RAW_FILENAMES:
        candidate = raw_data_dir / name
        if candidate.exists():
            return candidate.resolve()

    return (raw_data_dir / EXPECTED_RAW_FILENAMES[0]).resolve()


def get_config(repo_root: Path | None = None) -> PipelineConfig:
    root = (repo_root or repo_root_from_here()).resolve()
    raw_data_dir = root / "data" / "raw"
    processed_data_dir = root / "data" / "processed"
    table_dir = root / "outputs" / "tables"
    figure_dir = root / "outputs" / "figures"
    notebook_path = root / "notebooks" / "RAMP_replication_notebook.ipynb"

    return PipelineConfig(
        repo_root=root,
        raw_data_dir=raw_data_dir,
        processed_data_dir=processed_data_dir,
        table_dir=table_dir,
        figure_dir=figure_dir,
        notebook_path=notebook_path,
        data_path=find_data_path(raw_data_dir),
    )


def ensure_directories(config: PipelineConfig) -> None:
    for path in (
        config.raw_data_dir,
        config.processed_data_dir,
        config.table_dir,
        config.figure_dir,
    ):
        path.mkdir(parents=True, exist_ok=True)


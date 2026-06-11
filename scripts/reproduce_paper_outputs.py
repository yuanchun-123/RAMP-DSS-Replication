#!/usr/bin/env python3
"""Run the RAMP DSS replication workflow."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = REPO_ROOT / "src"
sys.path.insert(0, str(SRC_DIR))

from utils import list_outputs, load_module  # noqa: E402

config_mod = load_module(SRC_DIR / "00_config.py", "ramp_config")


def copy_existing_exports(source: Path) -> None:
    config = config_mod.get_config(REPO_ROOT)
    config_mod.ensure_directories(config)

    extract_dir = None
    source_root = source
    if source.is_file() and source.suffix == ".zip":
        extract_dir = config.processed_data_dir / "recovered_exports" / source.stem
        if extract_dir.exists():
            shutil.rmtree(extract_dir)
        extract_dir.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(source, "r") as zf:
            zf.extractall(extract_dir)
        source_root = extract_dir

    table_candidates = list(source_root.rglob("*.csv"))
    figure_candidates = [
        p
        for p in source_root.rglob("*")
        if p.suffix.lower() in {".png", ".pdf"}
        and (p.name.startswith("fig_dss_") or p.name == "figure_propensity_overlap_24h.png")
    ]

    for path in table_candidates:
        if "__MACOSX" in path.parts or path.name.startswith("._"):
            continue
        shutil.copy2(path, config.table_dir / path.name)

    for path in figure_candidates:
        if "__MACOSX" in path.parts or path.name.startswith("._"):
            continue
        shutil.copy2(path, config.figure_dir / path.name)

    print(f"Copied {len(table_candidates)} table candidates and {len(figure_candidates)} figure candidates.")
    if extract_dir:
        print(f"Temporary extraction directory: {extract_dir}")


def execute_notebook(timeout: int | None = None) -> None:
    config = config_mod.get_config(REPO_ROOT)
    config_mod.ensure_directories(config)

    if not config.data_path.exists():
        raise FileNotFoundError(
            f"Raw Criteo data not found at {config.data_path}. "
            "Download the data from the original provider and place it under data/raw/, "
            "or set RAMP_DATA_PATH."
        )

    env = os.environ.copy()
    env.setdefault("WANDB_DISABLED", "true")
    env.setdefault("RAMP_PROJECT_DIR", str(REPO_ROOT))

    cmd = [
        sys.executable,
        "-m",
        "jupyter",
        "nbconvert",
        "--to",
        "notebook",
        "--execute",
        "--inplace",
        str(config.notebook_path),
    ]
    if timeout is not None:
        cmd.extend(["--ExecutePreprocessor.timeout", str(timeout)])

    subprocess.run(cmd, cwd=REPO_ROOT, env=env, check=True)


def report_outputs(tables_only: bool, figures_only: bool) -> None:
    config = config_mod.get_config(REPO_ROOT)
    tables = list_outputs(config.table_dir, (".csv", ".json", ".md"))
    figures = list_outputs(config.figure_dir, (".png", ".pdf"))

    if not figures_only:
        print(f"Tables found: {len(tables)}")
        for path in tables[:20]:
            print("  ", path.relative_to(REPO_ROOT))
    if not tables_only:
        print(f"Figures found: {len(figures)}")
        for path in figures[:20]:
            print("  ", path.relative_to(REPO_ROOT))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Reproduce RAMP DSS paper outputs.")
    parser.add_argument(
        "--from-existing-exports",
        type=Path,
        help="Copy tables and figures from an existing paper_outputs directory or zip file.",
    )
    parser.add_argument("--tables-only", action="store_true", help="Run and report table outputs.")
    parser.add_argument("--figures-only", action="store_true", help="Run and report figure outputs.")
    parser.add_argument(
        "--timeout",
        type=int,
        default=None,
        help="Optional notebook execution timeout in seconds per cell.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.tables_only and args.figures_only:
        raise SystemExit("Choose at most one of --tables-only or --figures-only.")

    if args.from_existing_exports:
        copy_existing_exports(args.from_existing_exports.expanduser().resolve())
    else:
        execute_notebook(timeout=args.timeout)

    report_outputs(tables_only=args.tables_only, figures_only=args.figures_only)


if __name__ == "__main__":
    main()

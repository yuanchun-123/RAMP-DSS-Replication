#!/usr/bin/env python3
"""Entry point for the full RAMP replication pipeline."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    cmd = [sys.executable, str(REPO_ROOT / "scripts" / "reproduce_paper_outputs.py")]
    subprocess.run(cmd, cwd=REPO_ROOT, check=True)


if __name__ == "__main__":
    main()


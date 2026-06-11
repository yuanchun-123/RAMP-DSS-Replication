# Reproduction Guide

## Environment

The package was prepared for Python 3.10 or newer on macOS or Linux. A fresh
virtual environment is recommended.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Data Placement

Obtain authorized access to the underlying RTB attribution data and place the
raw TSV file under:

```text
data/raw/pcb_dataset_final.tsv
```

If the file has a different name, set `RAMP_DATA_PATH` to the full path.

## Runtime and Memory

The full dataset is large. Runtime depends on CPU cores, memory, disk speed, and
whether cached processed files already exist. A machine with at least 16 GB RAM
is recommended; 32 GB or more is preferable for full-data runs.

## Full Pipeline

From the repository root:

```bash
python scripts/reproduce_paper_outputs.py
```

This executes the replication notebook in place and writes outputs under:

```text
outputs/tables/
outputs/figures/
data/processed/
```

## Regenerate Only Tables

```bash
python scripts/reproduce_paper_outputs.py --tables-only
```

This runs the same notebook workflow and checks for table outputs after
execution.

## Regenerate Only Figures

```bash
python scripts/reproduce_paper_outputs.py --figures-only
```

This runs the same notebook workflow and checks for figure outputs after
execution.

## Colab Option

Upload the repository folder to Google Drive or clone it inside Colab. Install
the requirements, place the raw Criteo file under `data/raw/`, and open:

```text
notebooks/RAMP_replication_notebook.ipynb
```

Google Drive mounting is optional. To use Drive paths, set
`RAMP_USE_GOOGLE_DRIVE=1` before running the setup cell and set `RAMP_DATA_PATH`
if the raw data are outside the repository layout.

## Troubleshooting

`FileNotFoundError: Raw Criteo data were not found`

Check that the authorized raw TSV is in `data/raw/` or that `RAMP_DATA_PATH`
points to the correct file.

`No module named lightgbm`

Install the requirements in the active environment.

Out-of-memory errors

Close other applications, run on a larger machine, or use cached processed files
from a previous local run. The full dataset is not small.

No outputs appear under `outputs/tables/`

Confirm that the notebook completed. Partial runs may leave checkpoints under
`data/processed/` but no final paper tables.

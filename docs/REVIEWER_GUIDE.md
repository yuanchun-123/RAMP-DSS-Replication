# Reviewer Guide

## 1. Repository Overview

This repository contains the replication materials for the DSS manuscript
**RAMP: A Reliability-Aware Decision Support System for Campaign Prioritization
under Biased Attribution Signals**.

The repository includes code, documentation, a cleaned notebook, and aggregate
figures. It does not include raw or processed RTB data.

## 2. Computational Requirements

Use Python 3.10 or newer. Install dependencies with:

```bash
pip install -r requirements.txt
```

The full-data workflow can be memory intensive. At least 16 GB RAM is
recommended; 32 GB or more is preferable for a full replication run.

## 3. Data Requirements

The underlying RTB dataset is proprietary and cannot be redistributed. Reviewers
need authorized access to the input data. Place the raw TSV file at:

```text
data/raw/pcb_dataset_final.tsv
```

or set `RAMP_DATA_PATH` to the local file path.

## 4. Expected Outputs

Generated tables are written to `outputs/tables/`. Generated figures are written
to `outputs/figures/`. See `docs/OUTPUT_MAPPING.md` for the mapping between
output files and manuscript tables or figures.

## 5. Reproduction Workflow

From the repository root:

```bash
python scripts/run_full_pipeline.py
```

The same workflow can be run through:

```bash
python scripts/reproduce_paper_outputs.py
```

The cleaned notebook is available at
`notebooks/RAMP_replication_notebook.ipynb` for readers who prefer an
interactive workflow.

## 6. Troubleshooting

If the script reports that the raw data are missing, check `data/raw/` or set
`RAMP_DATA_PATH`.

If imports fail, recreate the virtual environment and reinstall
`requirements.txt`.

If memory errors occur, run on a larger machine or use previously generated
local checkpoints. Checkpoints are written under `data/processed/` and are not
tracked by Git.

## 7. Corresponding Author Contact

Yuanchun Ye  
Tepper School of Business  
Carnegie Mellon University  
[yuanchuy@andrew.cmu.edu](mailto:yuanchuy@andrew.cmu.edu)


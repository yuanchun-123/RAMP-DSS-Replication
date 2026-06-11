# RAMP-DSS Replication Package

This repository contains replication code and documentation for the manuscript:
**RAMP: A Reliability-Aware Decision Support System for Campaign Prioritization under Biased Attribution Signals**

The manuscript develops and evaluates RAMP, a diagnostic decision-support artifact for assessing attribution reliability in real-time bidding advertising. The code implements the main components of the RAMP workflow: selection-adjusted benchmarking, falsification-based diagnostics, campaign-level aggregation, diagnostic gating, and time-split managerial decision simulation.

## Authors

See the submitted manuscript for the author list and affiliations.

## Repository Purpose

This package is intended for reviewers and researchers who want to inspect or reproduce the empirical workflow. It explains the required data, how to obtain the original dataset, how to run the notebook and scripts, and how generated files map to manuscript tables and figures.

## Data Availability

This study uses the public Criteo Attribution Dataset. The authors are not the owners of the original data and do not redistribute the raw dataset in this repository. To reproduce the analysis, users should download the original Criteo data from the data provider and place the files under `data/raw/`.

The repository provides code, documentation, and output-generation scripts. Processed data and paper outputs can be regenerated locally once the raw data are placed in the expected directory.

The license applies to the code in this repository only. The original Criteo data are governed by the data provider's terms of use.

## Repository Structure

```text
RAMP-DSS-Replication/
  README.md
  LICENSE
  requirements.txt
  .gitignore
  notebooks/
    RAMP_replication_notebook.ipynb
  src/
    00_config.py
    01_data_preparation.py
    02_descriptive_statistics.py
    03_selection_adjusted_benchmark.py
    04_diagnostic_tests.py
    05_campaign_aggregation.py
    06_decision_gate.py
    07_time_split_evaluation.py
    utils.py
  scripts/
    run_full_pipeline.py
    reproduce_paper_outputs.py
  outputs/
    tables/
    figures/
  docs/
    DATA_ACCESS.md
    REPRODUCTION_GUIDE.md
    OUTPUT_MAPPING.md
  data/
    README.md
```

## Installation

```bash
git clone https://github.com/<username>/RAMP-DSS-Replication.git
cd RAMP-DSS-Replication
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Reproduction Steps

1. Download the Criteo Attribution Dataset from the original provider.
2. Place the raw TSV file at `data/raw/pcb_dataset_final.tsv`, or set `RAMP_DATA_PATH` to the file path.
3. Run:

```bash
python scripts/reproduce_paper_outputs.py
```

The same command is available through:

```bash
python scripts/run_full_pipeline.py
```

## Colab Option

The notebook can also be run in Colab. Install the packages in
`requirements.txt`, place the raw data where Colab can read it, and set
`RAMP_DATA_PATH` if the file is not under `data/raw/`. Google Drive mounting is
optional rather than part of the main workflow.

## Expected Outputs

Generated tables are written to:

```text
outputs/tables/
```

Generated figures are written to:

```text
outputs/figures/
```

The table CSV files are ignored by default because they are derived from the raw
Criteo data. The mapping from outputs to manuscript elements is listed in
`docs/OUTPUT_MAPPING.md`.

## Manuscript Tables and Figures

Key output groups include:

- selection-adjusted benchmark and overlap diagnostics;
- campaign reprioritization metrics;
- diagnostic gate funnel tables and figures;
- decision-risk classification outputs;
- time-split managerial decision simulation outputs.

See `docs/OUTPUT_MAPPING.md` for file-level mapping.

## Computational Notes

The full Criteo dataset is large. Runtime and memory use depend on hardware,
disk speed, and whether processed checkpoints already exist. See
`docs/REPRODUCTION_GUIDE.md` for environment notes and troubleshooting.

W&B tracking is disabled by default.

## Citation

If using this code, cite the manuscript listed above and the original Criteo
Attribution Dataset according to the provider's citation guidance.

## Contact

For replication questions, contact the corresponding author listed in the
submitted manuscript.


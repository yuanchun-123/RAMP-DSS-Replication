# RAMP DSS Replication Package

## Paper

**RAMP: A Reliability-Aware Decision Support System for Campaign Prioritization under Biased Attribution Signals**

Authors:

Pei Xue  
Tepper School of Business  
Carnegie Mellon University

Yuanchun Ye (Corresponding Author)  
Tepper School of Business  
Carnegie Mellon University  
Email: [yuanchuy@andrew.cmu.edu](mailto:yuanchuy@andrew.cmu.edu)

---

## Overview

This repository contains the replication materials for a Decision Support
Systems manuscript on campaign prioritization in real-time bidding advertising.
The paper studies a setting in which managers must decide which campaigns to
prioritize when observed attribution signals may be biased by selection,
exposure patterns, and user activity.

RAMP, short for Reliability-Aware Attribution Management and Prioritization, is
a diagnostic decision-support workflow. It does not treat observed attribution
as a direct measure of campaign value. Instead, it builds a selection-adjusted
benchmark, runs reliability diagnostics, aggregates diagnostic signals at the
campaign level, applies screening gates, and evaluates prioritization decisions
in a time-split setting.

The repository includes:

- a cleaned replication notebook;
- Python modules for the main RAMP workflow components;
- scripts for reproducing manuscript outputs;
- documentation for data access and reproduction;
- output mappings for manuscript tables and figures;
- aggregate figure files used for reviewer orientation.

The repository does not include the underlying proprietary RTB data.

## Repository Structure

```text
RAMP-DSS-Replication/
├── README.md
├── CITATION.cff
├── LICENSE
├── requirements.txt
├── .gitignore
├── data/
│   └── README.md
├── docs/
│   ├── DATA_ACCESS.md
│   ├── OUTPUT_MAPPING.md
│   ├── PUBLIC_RELEASE_CHECKLIST.md
│   ├── RELEASE_NOTES_v1.0.md
│   ├── REPRODUCTION_GUIDE.md
│   └── REVIEWER_GUIDE.md
├── notebooks/
│   └── RAMP_replication_notebook.ipynb
├── outputs/
│   ├── figures/
│   └── tables/
├── scripts/
│   ├── reproduce_paper_outputs.py
│   └── run_full_pipeline.py
└── src/
    ├── 00_config.py
    ├── 01_data_preparation.py
    ├── 02_descriptive_statistics.py
    ├── 03_selection_adjusted_benchmark.py
    ├── 04_diagnostic_tests.py
    ├── 05_campaign_aggregation.py
    ├── 06_decision_gate.py
    ├── 07_time_split_evaluation.py
    └── utils.py
```

Folder purposes:

- `data/`: documents the expected local data layout. Raw and processed data are
  not tracked.
- `docs/`: contains data-access, reproduction, reviewer, output-mapping, and
  release documentation.
- `notebooks/`: contains the cleaned replication notebook.
- `scripts/`: contains command-line entry points for reproducing outputs.
- `src/`: contains reusable workflow components used by the scripts and
  notebook.
- `outputs/figures/`: contains aggregate figure files for reviewer orientation.
- `outputs/tables/`: receives generated tables when the pipeline is run locally.

## Installation

```bash
git clone https://github.com/yuanchun-123/RAMP-DSS-Replication.git
cd RAMP-DSS-Replication
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

On Windows, activate the environment with:

```bash
venv\Scripts\activate
```

## Reproducing Results

1. Obtain authorized access to the underlying RTB attribution data.
2. Place the raw input file under:

```text
data/raw/pcb_dataset_final.tsv
```

Alternatively, set `RAMP_DATA_PATH` to the local file path:

```bash
export RAMP_DATA_PATH=/absolute/path/to/input_file.tsv
```

3. Run the full replication workflow:

```bash
python scripts/run_full_pipeline.py
```

or:

```bash
python scripts/reproduce_paper_outputs.py
```

Generated tables are written to `outputs/tables/`. Generated figures are written
to `outputs/figures/`. Processed intermediate files are written under
`data/processed/` and are not tracked by Git.

Runtime depends on hardware and local I/O speed. The full dataset is large; a
machine with at least 16 GB RAM is recommended, and 32 GB or more is preferable
for full-data runs. A complete run may take several hours on a standard laptop.

## Data Availability

The original RTB dataset used in this study is proprietary and cannot be
redistributed.

The repository contains all code required to reproduce the analyses, figures,
and tables once authorized access to the underlying data is obtained. Raw data,
processed data, user-level records, and impression-level records are excluded
from version control.

The license in this repository applies only to the code and documentation. It
does not apply to the underlying data.

## Output Mapping

The mapping from generated files to manuscript tables and figures is provided in
[docs/OUTPUT_MAPPING.md](docs/OUTPUT_MAPPING.md).

## Citation

If you use this replication package, cite the manuscript and this repository.

```bibtex
@article{xueye_ramp_dss,
  title   = {RAMP: A Reliability-Aware Decision Support System for Campaign Prioritization under Biased Attribution Signals},
  author  = {Xue, Pei and Ye, Yuanchun},
  journal = {Decision Support Systems},
  note    = {Manuscript submitted},
  year    = {2026}
}
```

## Contact

For replication questions, contact Yuanchun Ye at
[yuanchuy@andrew.cmu.edu](mailto:yuanchuy@andrew.cmu.edu).

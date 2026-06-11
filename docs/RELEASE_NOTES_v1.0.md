# v1.0-dss-submission

This release corresponds to the replication package accompanying the manuscript:

**RAMP: A Reliability-Aware Decision Support System for Campaign Prioritization
under Biased Attribution Signals**

## Repository Overview

The package contains the code and documentation needed to reproduce the RAMP
workflow used in the manuscript. It includes a cleaned replication notebook,
Python modules, command-line scripts, data-access instructions, output mapping,
and aggregate figures for reviewer orientation.

## Reproduction Workflow

After obtaining authorized access to the underlying RTB attribution data, place
the raw TSV file under `data/raw/` or set `RAMP_DATA_PATH`. Then run:

```bash
python scripts/run_full_pipeline.py
```

Generated tables are written to `outputs/tables/`, and generated figures are
written to `outputs/figures/`.

## Data Access Note

The original RTB dataset used in this study is proprietary and cannot be
redistributed. This release excludes raw data, processed data, user-level
records, and impression-level records.

## Contact Information

Yuanchun Ye  
Tepper School of Business  
Carnegie Mellon University  
[yuanchuy@andrew.cmu.edu](mailto:yuanchuy@andrew.cmu.edu)


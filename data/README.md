# Data Directory

The paper uses the public Criteo Attribution Dataset.

The original Criteo Attribution Dataset is publicly available from the data
provider. Because the authors are not the data owner, this repository does not
redistribute the raw data. To reproduce the analysis, download the data from
the original provider and place it in `data/raw/` following the directory
structure described below.

Expected local structure:

```text
data/
  raw/
    pcb_dataset_final.tsv
  processed/
    notebook_checkpoints/
```

The raw filename may differ depending on the download source. If your local file
has another name, either rename it to `pcb_dataset_final.tsv` or set
`RAMP_DATA_PATH` to the full path before running the scripts.

Processed files are generated under `data/processed/`. They are excluded from
version control because they can be large and are derived from the raw Criteo
data.


# Data Directory

The paper uses an RTB attribution dataset (Criteo dataset) that cannot be redistributed through
this repository.

Because the authors are not the data owner, this repository does not
redistribute raw data, processed data, user-level records, or impression-level
records. To reproduce the analysis, obtain authorized access to the underlying
data and place it in `data/raw/` following the directory structure described
below.

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
version control because they can be large and are derived from the underlying
RTB data.

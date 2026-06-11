# Data Access

## Dataset

This study uses the Criteo Attribution Dataset, originally released by Criteo
for attribution and advertising research.

## Why the Raw Data Are Not Included

The authors are not the owners of the original dataset. The replication package
therefore does not redistribute the raw Criteo files. Users should obtain the
dataset from the original provider and follow the provider's terms of use.

## Expected Local Directory

Place the raw file under:

```text
data/raw/
```

The default expected path is:

```text
data/raw/pcb_dataset_final.tsv
```

If your local filename differs, set:

```bash
export RAMP_DATA_PATH=/absolute/path/to/your/criteo_file.tsv
```

## Expected Input Columns

The replication code expects the standard Criteo attribution fields, including:

```text
timestamp
uid
campaign
conversion
conversion_timestamp
conversion_id
attribution
click
click_pos
click_nb
cost
cpo
time_since_last_click
cat1 ... cat9
```

## Preprocessing Assumptions

The scripts treat `-1` values as missing where the Criteo fields use that
sentinel. Timestamp fields are normalized to seconds before constructing
forward and placebo diagnostic windows.

The data are used for academic replication only.


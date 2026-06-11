# Data Access

## Dataset

This study uses an RTB attribution dataset for advertising research. The
underlying data are proprietary and are not included in this repository.

## Why the Raw Data Are Not Included

The authors are not the owners of the original dataset. The replication package
therefore does not redistribute raw data, processed data, user-level records, or
impression-level records. Users need authorized access to the underlying data
and must follow the data provider's terms of use.

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

The replication code expects the attribution fields used in the study,
including:

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

The data are used for academic replication only and must not be redistributed
through this repository.

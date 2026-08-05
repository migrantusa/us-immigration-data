# US Immigration Data — open datasets from MigrantUSA

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21812233.svg)](https://doi.org/10.5281/zenodo.21812233)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

Machine-readable time series and reference datasets on US immigration procedure and
enforcement, maintained by [MigrantUSA](https://migrantusa.com) — a free, bilingual
(English/Spanish) information site for immigrants living in the United States.

**Why this repo exists:** government sources publish only *today's* version of most of
this data and overwrite it without notice or archive. These pipelines re-check the
sources on a schedule and bank each observed change, so the history — what changed,
when, affecting whom — stays available **in a form the official pages do not provide**.

Every value traces to the official source cited inside each file. Human-readable
versions, methodology, and more datasets: **https://migrantusa.com/datasets/**
(Spanish: https://migrantusa.com/es/datos/).

📋 **[What changed recently →](CHANGES.md)** — the dated change record, regenerated daily.
The datasets are snapshots; the *changes* are the part that exists nowhere else in this
form, and they are the point of the repo.

**How it is collected:** automated retrieval from primary government sources
(Federal Register, USCIS, E-Verify, Department of State, ICE, EOIR, DOL), normalized and
verified against the source before it lands. **How often:** the refresh runs daily
([`scripts/refresh.py`](scripts/refresh.py) via
[GitHub Actions](.github/workflows/refresh.yml)); files change only when the sources do,
and each carries its own as-of date.

**If you are mirroring this data** on a dataset registry or aggregator, please keep
`https://migrantusa.com/datasets/` as the declared canonical source and cite this repo
as the origin — it keeps provenance unambiguous when the same series appears in several
places.

## Datasets

| File | What it is | Coverage |
|---|---|---|
| `tps_designation_history` | Every TPS designation, extension, and termination Federal Register document | 1994–2026, 292 FR documents |
| `uscis_fee_history` | USCIS filing fees by form, every change traced to its FR rule | 40 forms, 2004–present |
| `visa_bulletin_movement_series` | Month-over-month Visa Bulletin movement, all 4 tables (State publishes one bulletin at a time and never the delta) | monthly series |
| `ice_detention_history` | Banked snapshots of ICE's detention statistics releases + computed change between releases | biweekly-release series |
| `ice_287g` | Active 287(g) agreements with per-agency model and signing date, by state | 2,179 agreements |
| `litigation_tracker` | Tracked federal immigration cases as structured data — status, docket, court, who is affected — plus movement over time | 62 cases |
| `eoir_legal_deserts` | DOJ-recognized free legal-aid organizations per immigration court, by state | 31 jurisdictions |
| `tps_work_permits` | Per-country TPS work-permit (EAD) status and the current Form I-9 dates employers must use | all litigated countries |
| `change_log` | The verified change log behind [migrantusa.com/updates](https://migrantusa.com/updates/) — dated immigration/benefits changes, each checked against the official source | continuous |

**Formats:** JSON is canonical (includes `_meta` with source URLs and as-of dates).
CSVs are convenience flattenings of the main table in each file.

**Updates:** files refresh as the underlying sources change (some daily, some
monthly); each file's `_meta` carries its own as-of date. Watch releases/commits, or
subscribe to the human-readable feed: https://migrantusa.com/updates/index.xml

## Cite this dataset

Use is free under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — share and
adapt, **with attribution**. If you found this useful enough to build on, a citation is
the whole ask.

**DOI:** [`10.5281/zenodo.21812233`](https://doi.org/10.5281/zenodo.21812233) — this is the
*concept* DOI and always resolves to the newest version, so a citation using it stays valid
as the series updates. (Each release also gets its own version DOI;
`10.5281/zenodo.21812234` is v2026.08.05.)

**APA**

> MigrantUSA Editorial. (2026). *US Immigration Data: open historical datasets on US
> immigration procedure and enforcement* [Data set]. Zenodo.
> https://doi.org/10.5281/zenodo.21812233

**BibTeX**

```bibtex
@dataset{migrantusa_us_immigration_data,
  author    = {{MigrantUSA Editorial}},
  title     = {US Immigration Data: open historical datasets on US
               immigration procedure and enforcement},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.21812233},
  url       = {https://doi.org/10.5281/zenodo.21812233},
  note      = {CC BY 4.0}
}
```

**Citing a single dataset or a specific change**

> MigrantUSA Editorial. (2026). *[dataset name]*, in *US Immigration Data*. Retrieved
> [date], from https://migrantusa.com/datasets/

| | |
|---|---|
| **DOI (all versions)** | [10.5281/zenodo.21812233](https://doi.org/10.5281/zenodo.21812233) |
| **Canonical page** | https://migrantusa.com/datasets/ |
| **Methodology** | https://migrantusa.com/methodology/ |
| **Machine-readable metadata** | [`CITATION.cff`](CITATION.cff) — GitHub's "Cite this repository" button reads this |
| **Change record** | [`CHANGES.md`](CHANGES.md) · [`data/change_log.json`](data/change_log.json) |
| **Downloads** | JSON + CSV per dataset under [`data/`](data/) |
| **Historical versions** | tagged releases, each a fixed point in the series |
| **License** | CC BY 4.0 |

⚖️ **What is and is not ours:** the underlying facts originate from the cited US
government sources and carry no copyright. This repo's contribution — and the thing worth
citing — is the curation, normalization, verification, and **the banked history**. When a
claim rests on what a value *used to be*, cite the government source for the fact and this
record for the change.

## Contact

Corrections and questions: **info@migrantusa.com** — corrections policy:
https://migrantusa.com/corrections/

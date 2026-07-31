# US Immigration Data — open datasets from MigrantUSA

Machine-readable time series and reference datasets on US immigration procedure and
enforcement, maintained by [MigrantUSA](https://migrantusa.com) — a free, bilingual
(English/Spanish) information site for immigrants living in the United States.

**Why this repo exists:** government sources publish only *today's* version of most of
this data and silently overwrite it. Our pipelines re-check the sources continuously
and bank every change, so the history — what changed, when, affecting whom — exists
here even when the official page no longer shows it.

Every value traces to the official source cited inside each file. Human-readable
versions, methodology, and more datasets: **https://migrantusa.com/datasets/**
(Spanish: https://migrantusa.com/es/datos/).

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

## License & citation

Data: [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/4.0/)
(CC BY 4.0) — free to use, share, and adapt, **with attribution and a link**.

> Suggested citation: MigrantUSA, "[dataset name]," github.com/migrantusa/us-immigration-data,
> retrieved [date]. https://migrantusa.com/datasets/

Note that the underlying facts originate from the cited US government sources; this
repo's contribution is the curation, normalization, verification, and banked history.

## Contact

Corrections and questions: **info@migrantusa.com** — corrections policy:
https://migrantusa.com/corrections/

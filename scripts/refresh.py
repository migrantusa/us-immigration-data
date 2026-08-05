#!/usr/bin/env python3
"""Self-refresh this repo from the published MigrantUSA datasets.

WHY THIS EXISTS (2026-08-05)
----------------------------
This repo shipped 2026-07-31 and then sat at ONE commit for five days. Its README
promises the thing that makes it worth citing: "government sources publish only today's
version and silently overwrite it; our pipelines bank every change, so the history
exists here." A repo that stops updating stops being a citation asset -- the data is
not the differentiator (anyone can scrape a .gov page once), the MAINTAINED SERIES is.
The refresh used to be a manual two-step, which is exactly why it rotted.

DESIGN: this script pulls from the PUBLIC dataset URLs on migrantusa.com rather than
from the website repo's working tree. That means this repo refreshes itself with only
its own GITHUB_TOKEN -- no cross-repo personal access token, no shared secret. The
published files are already sanitized by the site's deploy pipeline, so there is no
operator-only metadata to strip here.

⚠️ BLAST RADIUS IS BOUNDED IN CODE, deliberately. Unattended automation is what got
this project delisted from Bing in July (a deploy script re-submitted 5,274 URLs on
every deploy, 22 deploys/day). So: this writes ONLY under data/, it ABORTS the whole
run rather than committing a partial refresh, and it will not overwrite a good file
with a suspiciously small or unparseable one.

Usage:
    python scripts/refresh.py            # fetch + rewrite data/
    python scripts/refresh.py --check    # report drift, write nothing (CI dry-run)
"""
import csv
import json
import os
import sys
import urllib.error
import urllib.request

BASE = "https://migrantusa.com/data/datasets"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DST = os.path.join(ROOT, "data")

# name -> why it is in the public repo (mirrored in README.md)
DATASETS = [
    "tps_designation_history",       # every TPS designation/extension/termination FR doc, 1994-2026
    "uscis_fee_history",             # 40 forms, 2004-2024, every fee -> its FR rule
    "visa_bulletin_movement_series", # month-over-month Visa Bulletin movement
    "ice_detention_history",         # banked biweekly ICE detention snapshots + computed change
    "ice_287g",                      # 287(g) agreements with per-agency signing dates
    "litigation_tracker",            # tracked immigration cases as data + movement series
    "eoir_legal_deserts",            # DOJ-recognized legal-aid orgs per immigration court
    "tps_work_permits",              # per-country TPS EAD / I-9 date status
    "change_log",                    # the verified change log behind /updates/
]

# Truncation guard. An ABSOLUTE byte floor is the wrong instrument here: these datasets
# span 1.5 KB (ice_detention_history) to 320 KB (ice_287g), so any single constant is
# either useless on the big files or a false alarm on the small ones -- a first pass set
# it to 2,000 and immediately blocked a perfectly good 1,519-byte file.
# Instead compare against the file we already trust: a real refresh does not lose half a
# dataset. SHRINK_FLOOR only catches empty bodies and error pages when nothing is banked yet.
SHRINK_RATIO = 0.5      # refuse a fetch under half the size of the banked copy
SHRINK_FLOOR = 400      # bytes; only applies when there is no banked copy to compare


def fetch(name):
    url = f"{BASE}/{name}.json"
    req = urllib.request.Request(url, headers={"User-Agent": "us-immigration-data refresh"})
    raw = urllib.request.urlopen(req, timeout=90).read()

    banked = os.path.join(DST, f"{name}.json")
    if os.path.exists(banked):
        prev = os.path.getsize(banked)
        if len(raw) < prev * SHRINK_RATIO:
            raise ValueError(f"{name}: {len(raw):,} bytes vs {prev:,} banked "
                             f"(<{SHRINK_RATIO:.0%}); refusing to shrink the series")
    elif len(raw) < SHRINK_FLOOR:
        raise ValueError(f"{name}: only {len(raw)} bytes and nothing banked; refusing")

    data = json.loads(raw.decode("utf-8"))   # raises on a truncated or HTML body
    return raw, data


# ---------------------------------------------------------------------------
# CSV generation. Journalists and researchers open CSV, not JSON; the JSON is
# canonical and the CSV is convenience.
#
# ⚠️ The "largest list of dicts" heuristic silently emits a PARTIAL table on
# per-state / per-form nesting -- a dry run once produced only Texas's 287(g)
# agencies out of all 50 states and the row count looked perfectly healthy.
# Nested shapes therefore get an EXPLICIT flattener. Same failure class as the
# BIA parser that dropped 140 orgs: a missing record is invisible in the count.
# ---------------------------------------------------------------------------
def largest_list_of_dicts(node, path="$"):
    best = (None, [])
    if isinstance(node, list):
        if node and all(isinstance(x, dict) for x in node) and len(node) > len(best[1]):
            best = (path, node)
    elif isinstance(node, dict):
        for k, v in node.items():
            if k == "_meta":
                continue
            p, l = largest_list_of_dicts(v, f"{path}.{k}")
            if len(l) > len(best[1]):
                best = (p, l)
    return best


def _flat_287g(d):
    rows = []
    for state, node in d["states"].items():
        for a in node.get("agencies", []):
            rows.append({"state": state, **a})
    return rows, "all states' agency lists"


def _flat_vbms(d):
    rows = []
    for table, entries in d["series"].items():
        for e in entries:
            rows.append({"table": table, **e})
    return rows, "all 4 movement tables"


def _flat_fee_history(d):
    rows = []
    for form, node in d["timeline"].items():
        for c in node.get("changes", []):
            rows.append({"form": form, **c})
    return rows, "per-form fee-change timeline"


EXPLICIT_CSV = {
    "ice_287g": _flat_287g,
    "visa_bulletin_movement_series": _flat_vbms,
    "uscis_fee_history": _flat_fee_history,
}


def csv_bytes(name, data):
    if name in EXPLICIT_CSV:
        rows, path = EXPLICIT_CSV[name](data)
    else:
        path, rows = largest_list_of_dicts(data)
    if len(rows) < 5:
        return None, None
    fields = []
    for r in rows:
        for k, v in r.items():
            if k not in fields and not isinstance(v, (dict, list)):
                fields.append(k)
    if not fields:
        return None, None
    import io
    buf = io.StringIO(newline="")
    w = csv.DictWriter(buf, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    for r in rows:
        w.writerow({k: v for k, v in r.items() if not isinstance(v, (dict, list))})
    return buf.getvalue().encode("utf-8-sig"), f"{len(rows)} rows from {path}"


def main():
    check_only = "--check" in sys.argv
    os.makedirs(DST, exist_ok=True)

    # Fetch EVERYTHING first. A partial refresh is worse than none -- it would publish a
    # set of files with mismatched as-of dates and call it a coherent snapshot.
    staged = {}
    for name in DATASETS:
        try:
            raw, data = fetch(name)
        except (urllib.error.URLError, urllib.error.HTTPError, ValueError,
                json.JSONDecodeError) as e:
            print(f"ABORT: {name} failed to fetch cleanly: {e}", file=sys.stderr)
            print("Nothing written. The previous good snapshot is intact.", file=sys.stderr)
            return 1
        staged[f"{name}.json"] = raw
        cb, note = csv_bytes(name, data)
        if cb:
            staged[f"{name}.csv"] = cb
        print(f"  fetched {name}.json ({len(raw):,} bytes)"
              + (f" + {name}.csv ({note})" if cb else " (no flat CSV)"))

    changed = []
    for fname, content in sorted(staged.items()):
        p = os.path.join(DST, fname)
        old = open(p, "rb").read() if os.path.exists(p) else None
        if old == content:
            continue
        changed.append(fname)
        if not check_only:
            with open(p, "wb") as fh:
                fh.write(content)

    if not changed:
        print("\nno drift — every dataset already current")
        return 0
    verb = "would change" if check_only else "updated"
    print(f"\n{verb} {len(changed)} file(s): {', '.join(changed)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

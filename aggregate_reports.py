"""
Aggregates the per-volume outputs of sehling_parser.py into ONE compact
summary file, so a 30-volume batch can be reviewed (or uploaded) as a
single small file instead of 30 segmentation reports or a raw console log.

Run this from the same directory that contains your `sehling/` folder,
AFTER running sehling_parser.py (with or without --merge) for the
volumes you want summarized:

    py aggregate_reports.py
    py aggregate_reports.py --out my_summary.json

For each volume folder found under sehling/, this reads:
  - <volume>.json                       (document count, band number)
  - <volume>.segmentation_report.json   (diagnostics, boundary gaps)
and writes one row per volume to the output file, plus a top-line
overview printed to the console so you can see at a glance which
volumes need a closer look before uploading anything further.
"""

import argparse
import json
from pathlib import Path
from typing import Any, Optional


def find_volume_dirs(root: Path) -> list[Path]:
    if not root.exists():
        return []
    return sorted(
        d for d in root.iterdir()
        if d.is_dir() and (d / f"{d.name}.json").exists()
    )


def count_boundary_gaps(report: dict[str, Any], volume_key: str) -> Optional[int]:
    boundaries = report.get(volume_key, {}).get("boundaries")
    if boundaries is None:
        return None
    gaps = 0
    for row in boundaries:
        prev_last = row.get("prev_doc_last_page")
        first = row.get("first_printed_page")
        if isinstance(prev_last, int) and isinstance(first, int) and first != prev_last + 1:
            gaps += 1
    return gaps


def summarize_volume(volume_dir: Path) -> dict[str, Any]:
    name = volume_dir.name
    row: dict[str, Any] = {"volume": name}

    corpus_path = volume_dir / f"{name}.json"
    try:
        with corpus_path.open(encoding="utf-8") as f:
            corpus = json.load(f)
    except Exception as exc:
        row["error"] = f"could not read {corpus_path.name}: {exc!r}"
        return row

    row["band_number"] = corpus.get("band_number")
    sources = corpus.get("sources", [])
    total_pages = 0
    total_docs = 0
    total_errors = 0
    running_head_docs = 0
    for src in sources:
        docs = src.get("documents", [])
        total_docs += len(docs)
        running_head_docs += sum(1 for d in docs if d.get("heading_source") == "running_head")
        total_errors += len(src.get("errors", []))
        for doc in docs:
            # crude page count from the doc's own printed_page_range where possible
            pass
    row["documents"] = total_docs
    row["via_running_head"] = running_head_docs
    row["fetch_errors"] = total_errors
    row["volume_title"] = (sources[0].get("metadata", {}).get("title") if sources else None)

    report_path = volume_dir / f"{name}.segmentation_report.json"
    if report_path.exists():
        try:
            with report_path.open(encoding="utf-8") as f:
                report = json.load(f)
            volume_key = next(iter(report.keys()), name)
            diagnostics = report.get(volume_key, {}).get("diagnostics", [])
            by_type: dict[str, int] = {}
            for d in diagnostics:
                by_type[d["type"]] = by_type.get(d["type"], 0) + 1
            row["diagnostics"] = by_type
            row["concerning_diagnostics"] = by_type.get("no_running_head_in_numbered_part", 0)
            row["boundary_gaps"] = count_boundary_gaps(report, volume_key)
        except Exception as exc:
            row["report_error"] = f"could not read {report_path.name}: {exc!r}"
    else:
        row["report_error"] = "segmentation_report.json not found"

    return row


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default="sehling", help="Path to the sehling/ output directory (default: sehling)")
    parser.add_argument("--out", default="volumes_summary.json", help="Output summary file path")
    args = parser.parse_args()

    root = Path(args.root)
    volume_dirs = find_volume_dirs(root)
    if not volume_dirs:
        print(f"No volume output found under {root.resolve()} -- run sehling_parser.py first.")
        return

    rows = [summarize_volume(d) for d in volume_dirs]

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)

    print(f"{'volume':<14} {'docs':>5} {'via_head':>9} {'gaps':>5} {'concerning':>11} {'errors':>7}  flags")
    print("-" * 90)
    for row in rows:
        if "error" in row:
            print(f"{row['volume']:<14} ERROR: {row['error']}")
            continue
        flags = []
        if row.get("report_error"):
            flags.append(row["report_error"])
        if row.get("fetch_errors"):
            flags.append(f"{row['fetch_errors']} fetch error(s)")
        if row.get("concerning_diagnostics"):
            flags.append(f"{row['concerning_diagnostics']} unexplained gap(s)")
        if row.get("boundary_gaps"):
            flags.append(f"{row['boundary_gaps']} boundary gap(s)")
        gaps = row.get("boundary_gaps")
        print(f"{row['volume']:<14} {row.get('documents', '?'):>5} {row.get('via_running_head', '?'):>9} "
              f"{gaps if gaps is not None else '?':>5} {row.get('concerning_diagnostics', '?'):>11} "
              f"{row.get('fetch_errors', '?'):>7}  {'; '.join(flags)}")

    print(f"\nWrote {len(rows)} volume summaries to {args.out}")
    print("That single file is what's worth uploading -- or just the console table above, pasted in.")


if __name__ == "__main__":
    main()

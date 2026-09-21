"""
combine_volumes.py -- combines every volume's six output files (from
sehling_parser.py) into six single "eko_full" files, so the whole
corpus (or a chosen subset) can be uploaded in one pass instead of
volume by volume.

Run in the same directory that contains your `sehling/` folder:

    py combine_volumes.py
    py combine_volumes.py --volumes eko6_1 eko6_2 eko7_1 eko7_2_1 eko7_2_2
    py combine_volumes.py --out-prefix eko_subset

WHAT GETS PRODUCED, AND HOW EACH ONE IS COMBINED:

  eko_full.json               -- {volume_id: <that volume's full compiled
                                  JSON, unchanged>, ...}. This is the one
                                  that actually matters for register-
                                  linking work: it's where every
                                  document's full text, citation, heading,
                                  and page range lives, and it already
                                  carries that volume's own toc/metadata
                                  nested inside (sources[0]["toc"],
                                  sources[0]["metadata"]) -- see the note
                                  below on eko_full_toc.json /
                                  eko_full_metadata.json.

  eko_full.segmentation_report.json -- merged directly, not nested: each
                                  per-volume report already uses that
                                  volume's own id as its one top-level
                                  key (confirmed against every report
                                  this project has produced), so the 30
                                  reports merge into one dict with no
                                  extra wrapping needed.

  eko_full.md                 -- every volume's markdown concatenated,
                                  with an HTML-comment header marking
                                  where each one starts (keeps it valid
                                  Markdown while still being easy to
                                  find a specific volume in).

  eko_full_manifest.json      -- {volume_id: <that volume's IIIF
                                  manifest>, ...}. Large, and NOT used by
                                  link_register.py or anything built so
                                  far in this project -- it's page-
                                  fetching metadata, not content. Included
                                  because it was asked for, not because
                                  it's likely to matter for the register-
                                  linking work.

  eko_full_metadata.json,
  eko_full_toc.json           -- {volume_id: <that file's contents>, ...}.
                                  Genuinely redundant with eko_full.json
                                  for register-linking purposes specifically
                                  (both are already nested inside each
                                  volume's own compiled JSON under
                                  sources[0]) -- kept as separate files
                                  since they were asked for, and harmless
                                  either way, just not something that adds
                                  new information on top of eko_full.json.

A REAL SIZE CONCERN, WORTH CHECKING BEFORE UPLOADING: eko_full.json
carries every document's FULL text for every volume combined. Based on
individual volumes seen so far this project (some single sections alone
ran past 700 KB), a full 30-volume combination could plausibly land
anywhere from several tens of MB up to 100+ MB depending on total corpus
size -- there's no way to know exactly until it's actually built. The
script prints each output file's size when it finishes; if eko_full.json
comes out too large to upload comfortably, --volumes lets you combine
just the specific volumes actually relevant to an open question (e.g.
the eko7_1/eko7_2_2 pair) instead of the whole corpus at once.
"""

import argparse
import json
from pathlib import Path


def combine(root: Path, out_prefix: str, wanted_volumes: list[str] | None) -> None:
    if wanted_volumes:
        volumes = [v for v in wanted_volumes if (root / v).is_dir()]
        missing = [v for v in wanted_volumes if v not in volumes]
        if missing:
            print(f"  ! not found under {root}/, skipping: {', '.join(missing)}")
    else:
        volumes = sorted(d.name for d in root.iterdir() if d.is_dir())
    print(f"Combining {len(volumes)} volumes: {', '.join(volumes)}\n")

    combined_json: dict = {}
    combined_manifest: dict = {}
    combined_metadata: dict = {}
    combined_toc: dict = {}
    combined_segmentation_report: dict = {}
    md_parts: list[str] = []

    counts = {"json": 0, "md": 0, "segmentation_report": 0, "manifest": 0, "metadata": 0, "toc": 0}

    for vol in volumes:
        vol_dir = root / vol

        json_path = vol_dir / f"{vol}.json"
        if json_path.exists():
            with json_path.open(encoding="utf-8") as f:
                combined_json[vol] = json.load(f)
            counts["json"] += 1
        else:
            print(f"  ! {vol}: no {vol}.json")

        md_path = vol_dir / f"{vol}.md"
        if md_path.exists():
            with md_path.open(encoding="utf-8") as f:
                md_parts.append(f"\n\n<!-- ===== {vol} ===== -->\n\n" + f.read())
            counts["md"] += 1
        else:
            print(f"  ! {vol}: no {vol}.md")

        report_path = vol_dir / f"{vol}.segmentation_report.json"
        if report_path.exists():
            with report_path.open(encoding="utf-8") as f:
                report_data = json.load(f)
            combined_segmentation_report.update(report_data)
            counts["segmentation_report"] += 1
        else:
            print(f"  ! {vol}: no {vol}.segmentation_report.json")

        manifest_path = vol_dir / "manifest.json"
        if manifest_path.exists():
            with manifest_path.open(encoding="utf-8") as f:
                combined_manifest[vol] = json.load(f)
            counts["manifest"] += 1

        metadata_path = vol_dir / "metadata.json"
        if metadata_path.exists():
            with metadata_path.open(encoding="utf-8") as f:
                combined_metadata[vol] = json.load(f)
            counts["metadata"] += 1

        toc_path = vol_dir / "toc.json"
        if toc_path.exists():
            with toc_path.open(encoding="utf-8") as f:
                combined_toc[vol] = json.load(f)
            counts["toc"] += 1

    outputs = [
        (f"{out_prefix}.json", combined_json),
        (f"{out_prefix}.segmentation_report.json", combined_segmentation_report),
        (f"{out_prefix}_manifest.json", combined_manifest),
        (f"{out_prefix}_metadata.json", combined_metadata),
        (f"{out_prefix}_toc.json", combined_toc),
    ]

    print(f"\n{'=' * 60}\nWRITING OUTPUT\n{'=' * 60}")
    for filename, data in outputs:
        out_path = Path(filename)
        with out_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        size_mb = out_path.stat().st_size / (1024 * 1024)
        print(f"  {filename:<38} {size_mb:>9.1f} MB")

    md_path = Path(f"{out_prefix}.md")
    with md_path.open("w", encoding="utf-8") as f:
        f.write("".join(md_parts))
    size_mb = md_path.stat().st_size / (1024 * 1024)
    print(f"  {md_path.name:<38} {size_mb:>9.1f} MB")

    print(f"\n{'=' * 60}\nCOVERAGE\n{'=' * 60}")
    for key, count in counts.items():
        flag = "" if count == len(volumes) else "  <-- some volumes missing this file"
        print(f"  {key:<22} {count}/{len(volumes)}{flag}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", default="sehling", help="Path to the sehling/ output directory (default: sehling)")
    parser.add_argument("--out-prefix", default="eko_full", help="Prefix for output filenames (default: eko_full)")
    parser.add_argument("--volumes", nargs="+", default=None,
                         help="Specific volume ids to combine (default: every directory under --root)")
    args = parser.parse_args()
    combine(Path(args.root), args.out_prefix, args.volumes)


if __name__ == "__main__":
    main()

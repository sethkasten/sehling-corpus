"""
diagnose_register_links.py -- inspects the actual ambiguous/unresolved
patterns in a link_register.py output, so the next fix (if any) is based
on real cases rather than another guess.

Run in the same directory as the linked-output file:

    py diagnose_register_links.py                       # eko_reg_6_7_linked.json (default)
    py diagnose_register_links.py eko_reg_linked.json
"""
import json
import sys
from collections import Counter

filename = sys.argv[1] if len(sys.argv) > 1 else "eko_reg_6_7_linked.json"
results = json.load(open(filename, encoding="utf-8"))

ambiguous_pairs = Counter()
ambiguous_samples = []
unresolved_reasons = Counter()
unresolved_samples = []
unresolved_pages_seen = []
volume_specific = []  # (entry, volume, page) -- for eko_reg's "volume not found" cases

for r in results:
    for u in r["unresolved"]:
        reason = u["reason"]
        if reason.startswith("ambiguous"):
            pair = tuple(sorted(u["candidates"]))
            ambiguous_pairs[pair] += 1
            if len(ambiguous_samples) < 15:
                ambiguous_samples.append((r["entry"], u["page"], u["candidates"]))
        else:
            unresolved_reasons[reason] += 1
            unresolved_pages_seen.append(u["page"])
            if len(unresolved_samples) < 15:
                unresolved_samples.append((r["entry"], u.get("volume"), u["page"], reason))
            if "volume not found" in reason:
                volume_specific.append((r["entry"], u.get("volume"), u["page"]))

print(f"File: {filename}\n")

if ambiguous_pairs:
    print(f"{'=' * 70}\nAMBIGUOUS: which sub-volume pairs conflict, and how often\n{'=' * 70}")
    for pair, count in ambiguous_pairs.most_common(20):
        print(f"  {count:>6}  {pair}")

    print(f"\n{'=' * 70}\nAMBIGUOUS: sample entries\n{'=' * 70}")
    for entry, page, candidates in ambiguous_samples:
        print(f"  {entry!r} page={page} candidates={candidates}")

print(f"\n{'=' * 70}\nUNRESOLVED: reasons breakdown\n{'=' * 70}")
for reason, count in unresolved_reasons.most_common(20):
    print(f"  {count:>6}  {reason}")

print(f"\n{'=' * 70}\nUNRESOLVED: sample entries\n{'=' * 70}")
for entry, volume, page, reason in unresolved_samples:
    vol_str = f"volume={volume} " if volume else ""
    print(f"  {entry!r} {vol_str}page={page} -- {reason[:70]}")

if volume_specific:
    print(f"\n{'=' * 70}\nALL 'volume not found' cases (usually rare -- shown in full)\n{'=' * 70}")
    for entry, volume, page in volume_specific:
        print(f"  {entry!r} volume={volume} page={page}")

if unresolved_pages_seen:
    print(f"\n{'=' * 70}\nUNRESOLVED: page-number range seen\n{'=' * 70}")
    print(f"  min={min(unresolved_pages_seen)} max={max(unresolved_pages_seen)} "
          f"count={len(unresolved_pages_seen)}")

# For eko_reg specifically: show which volume_ids show up in "resolved"
# links, as a sanity cross-check -- anything conspicuously low or absent
# relative to the others is worth a second look.
resolved_volumes = Counter()
for r in results:
    for link in r.get("links", []):
        resolved_volumes[link["volume"]] += 1
if resolved_volumes:
    print(f"\n{'=' * 70}\nRESOLVED: citations per volume (sanity check)\n{'=' * 70}")
    for vid, count in resolved_volumes.most_common():
        print(f"  {vid:<14} {count}")

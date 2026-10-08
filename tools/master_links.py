#!/usr/bin/env python3
"""Check the links of the master guide.

- Every link to a place in the guide (#id) must name an anchor that exists.
- Links to other files are reported: the guide should stand on its own.
- A link whose label is a section number ("§2.3.2", "2.3.2", "Appendix 4.A")
  or a chapter ("Chapter 4") must point to that section or chapter, so that a
  renumbered heading cannot leave a stale label behind.

Usage: python3 tools/master_links.py [MASTER.md]
Exits with status 1 if it finds a problem.
"""
import re
import sys

MASTER = 'LITURGICAL_AND_ECCLESIASTICAL_LIFE.md'
LINK = re.compile(r'(?<!!)\[((?:[^\[\]\\]|\\.|\[[^\]]*\])*)\]\(([^)\s]+)\)')
ANCHOR = re.compile(r'<a id="([^"]+)"></a>')


def expected_label(aid):
    """The section number a section anchor stands for: s2-3-2 -> 2.3.2, s4-a-1 -> 4.A.1,
    s6-18-r1-2 -> 6.18.R1.2."""
    m = re.fullmatch(r's(\d+)((?:-[0-9a-z]+)*)', aid)
    if not m:
        return None
    parts = [m.group(1)] + [p.upper() for p in m.group(2).split('-')[1:]]
    return '.'.join(parts)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else MASTER
    text = open(path, encoding='utf-8').read()
    anchors = set(ANCHOR.findall(text))
    errors, warnings, n_internal = [], [], 0
    for n, line in enumerate(text.split('\n'), 1):
        for m in LINK.finditer(line):
            label, target = m.group(1), m.group(2)
            if re.match(r'(https?|mailto):', target):
                continue
            if not target.startswith('#'):
                errors.append(f'line {n}: link to another file: {m.group(0)[:80]}')
                continue
            n_internal += 1
            aid = target[1:]
            if aid not in anchors:
                errors.append(f'line {n}: no anchor "{aid}": {m.group(0)[:80]}')
                continue
            num = re.fullmatch(r'(?:§§?|Appendix\s+)?(\d+(?:\.[0-9A-Z]+)*)', label.strip())
            if num:
                exp = expected_label(aid)
                if exp is not None and num.group(1) != exp:
                    errors.append(f'line {n}: label {label!r} points to {aid} ({exp})')
            chap = re.fullmatch(r'Chapter (\d+)', label.strip())
            if chap and aid != f'ch{chap.group(1)}':
                errors.append(f'line {n}: label {label!r} points to {aid}')
    for e in errors:
        print(e)
    for w in warnings:
        print(w)
    print(f'{n_internal} internal links checked against {len(anchors)} anchors; {len(errors)} problems')
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()

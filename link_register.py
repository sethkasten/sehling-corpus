"""
link_register.py -- links Sehling's register volumes (eko_reg, eko_reg_6_7)
to the actual documents in the compiled territorial-volume corpus, by
parsing each index entry's page citations and resolving them to the
specific document that occupies the cited page.

Run this locally, in the same directory that contains your `sehling/`
folder, after both register volumes and the territorial volumes they
reference have been compiled:

    py link_register.py eko_reg
    py link_register.py eko_reg_6_7
    py link_register.py eko_reg --out eko_reg_linked.json

WHAT THIS ASSUMES, CONFIRMED AGAINST REAL DATA:

  eko_reg (the Generalregister) cites every entry with an explicit
  "{RomanBand}[/Teil[/Halbband]]: page, page, ..." marker -- e.g.
  "Abel VI/1: 285, 678, VI/2: 711, 740, ... VII/2/1: 1066, 1068,
  VII/2/2: 119, 121". The Roman numeral plus optional /N/N suffix maps
  directly onto this project's own volume-id scheme (VI/1 -> eko6_1,
  VII/2/1 -> eko7_2_1, XX/2 -> eko20_2, ...), which is what makes
  resolving these citations possible at all: the register's own
  citation format already IS the addressing scheme this corpus uses.
  Checked against the real eko_reg text: every one of ~40,000
  Roman-numeral-shaped markers found was a genuine, valid Roman
  numeral -- no false positives from this pattern -- though a small,
  unmeasured number of citations are silently missed where OCR
  corrupted the Roman numeral itself beyond recognition (one confirmed
  case: "VI" read as "Wl"), which fails to match at all rather than
  matching wrong. Under-detecting, not silently mis-linking.

  eko_reg_6_7 (the regional index for just Bände VI and VII) is
  DIFFERENT: each Personenregister/Ortsregister/Sachregister
  sub-section is already scoped to one Band by its own TOC position
  (nested under "Sechster Band" or "Siebter Band"), so its citations
  are bare page numbers with NO Roman marker at all -- "Aaron 285,
  652, 655, 656, 733, 1057". Since Band 6 and Band 7 are each split
  into multiple physically-separate digitized sub-volumes (eko6_1/
  eko6_2; eko7_1/eko7_2_1/eko7_2_2), a bare page number alone doesn't
  say which one it belongs to. This script resolves it by checking
  EVERY sub-volume of that Band's actual page range and accepting the
  match only when EXACTLY ONE sub-volume's range contains the cited
  page -- relying on Sehling's own print pagination being continuous
  and non-overlapping across a Band's sub-volumes (each physical
  Halbband picking up where the last one's page numbers left off,
  rather than each restarting at page 1), the way binding a large work
  into multiple volumes ordinarily works. I have NOT been able to
  verify this assumption against real eko6_1/eko6_2/eko7_2_1/eko7_2_2
  data (they weren't in reach while building this) -- if it's wrong,
  the symptom will be visible directly in this script's own output:
  either a flood of "ambiguous" results (multiple sub-volumes both
  claiming the same page -- pagination restarts per sub-volume after
  all) or "no matching sub-volume" (a gap in the assumed continuity).
  Check the printed statistics before trusting this volume's linked
  output; eko_reg's are on much firmer footing.

WHAT "UNRESOLVED" MEANS AND WHY IT'S KEPT, NOT DROPPED:
  A citation can fail to resolve because the target volume hasn't been
  compiled yet, the cited page falls outside every known document's
  range (a plausible OCR-page-number misread, or a page this project's
  own segmentation mis-bounded), or -- for eko_reg_6_7 -- genuine
  ambiguity. Every unresolved citation is kept in the output under
  "unresolved" with its reason, rather than silently dropped, on the
  same principle as everything else in this project: an honest gap
  beats a confident wrong answer, and nothing here should require
  trusting a percentage you can't see the failures behind.
"""

import argparse
import bisect
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any, Optional

# Bumped whenever the resolution logic changes, and printed at the start
# of every run. Added specifically because a stale copy of this script
# produced identical output across two separate "fixed" versions with no
# way to tell from the numbers alone that neither fix had actually run --
# the file size and modification time matched a known-old version, but
# that took a manual PowerShell check to discover. This makes it visible
# in the run's own output instead, every time, with no separate step.
SCRIPT_VERSION = "11 (skips --merge output directories when building the corpus index, since their content duplicates the original Teilband directories -- see build_corpus_index)"

ROMAN_VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

# Confirmed real OCR misreadings of this corpus's Roman numerals, found
# by tracing actual resolution failures back to raw text where the
# garbled marker sits exactly where a normal one would, inside an
# otherwise-clean, continuing citation list for the Band genuinely being
# discussed: "VI" -> "Wl" (a single dropped citation -- "Wl" doesn't
# look enough like a marker to match at all, so it was merely lost, not
# misattributed) and "VII" -> "VH" (plausibly two adjacent "I"s with a
# connecting serif read as one "H"). The second is far more
# consequential: "VH/1:" still looks marker-shaped but fails
# validation, so the whole page list that should follow it gets
# silently swallowed into the PRECEDING valid marker's segment instead
# of being dropped -- e.g. "VI/2: 1119, ... VH/1: 21, 139, 144..."
# misattributes real "VII/1" (eko7_1) citations to eko6_2, which is a
# worse failure than not resolving at all: the citation looks resolved,
# just against the wrong volume. A third confirmed case, "XXI" -> "XXL"
# (a capital I misread as L), was found the same way, inside the SAME
# "Diakon" entry: "XIX/2: 558, XXL 61, 179, 186..." -- "XXL" already
# contains only valid Roman letters (X, X, L), so it passes the
# character check but computes to 50, correctly exceeding the
# plausibility cap below -- yet still swallows its page list into the
# preceding valid marker exactly like the other two. The page list
# matches eko21's real content, not eko19_2's, confirming the fix.
OCR_ROMAN_FIXES = {"WL": "VI", "VH": "VII", "XXL": "XXI"}


def roman_to_int(s: str) -> Optional[int]:
    fixed = OCR_ROMAN_FIXES.get(s.upper(), s)
    if not re.fullmatch(r"[IVXLCDM]+", fixed):
        return None
    total, prev = 0, 0
    for ch in reversed(fixed):
        cur = ROMAN_VALUES[ch]
        total += cur if cur >= prev else -cur
        prev = cur
    # No real Band in this edition exceeds ~31 -- caps out accidental
    # matches on non-numeral-looking tokens that happen to sum high.
    return total if 0 < total <= 40 else None


# A citation marker: "{Roman}[/n[/n]]:" -- e.g. "VI:", "VI/1:", "VII/2/1:".
# The character class includes W and H (beyond true Roman letters)
# specifically so the two confirmed OCR-corrupted forms above can even
# be captured as marker candidates at all; roman_to_int's normalization
# step is what then either accepts them (only the two confirmed forms)
# or correctly rejects everything else shaped like them.
BAND_MARKER_RE = re.compile(r"([IVXLCDMWH]{1,6})(?:/(\d{1,2}))?(?:/(\d{1,2}))?\s*:\s*")
PAGE_TOKEN_RE = re.compile(r"\d+")
PAGE_MARKER_RE = re.compile(r"\[(?:p\. ([^\]]+)|digital p\. ([^\]]+))\]")
BAND_NUMBER_IN_HEADING_RE = re.compile(r"\b[Bb]and\b[^\d]{0,3}(\d{1,2})")

# eko_reg_6_7's own Band-divider entries are titled "Sechster Band: ..." /
# "Siebter Band: ..." -- German ORDINAL WORDS, not digits, confirmed
# against the real TOC. BAND_NUMBER_IN_HEADING_RE alone can't see these
# (there's no digit near "Band" to match).
GERMAN_ORDINALS = {
    "erster": 1, "zweiter": 2, "dritter": 3, "vierter": 4, "fünfter": 5,
    "sechster": 6, "siebter": 7, "achter": 8, "neunter": 9, "zehnter": 10,
    "elfter": 11, "zwölfter": 12, "dreizehnter": 13, "vierzehnter": 14,
    "fünfzehnter": 15, "sechzehnter": 16, "siebzehnter": 17, "achtzehnter": 18,
    "neunzehnter": 19, "zwanzigster": 20, "einundzwanzigster": 21,
    "zweiundzwanzigster": 22, "dreiundzwanzigster": 23, "vierundzwanzigster": 24,
}
GERMAN_ORDINAL_BAND_RE = re.compile(
    r"\b(" + "|".join(GERMAN_ORDINALS) + r")\b\s+Band", re.IGNORECASE
)


def parse_band_number_from_title(title: str) -> Optional[int]:
    # Ordinal-word form checked FIRST and is the confirmed-correct format
    # for eko_reg_6_7's own Band dividers. The digit-based fallback below
    # needs a word boundary before "Band" for exactly this reason: these
    # same titles also contain phrases like "Halbband 1 und 2" (meaning
    # "Halbband [i.e. sub-volume] 1 and 2"), and an unanchored "[Bb]and"
    # matches the tail of "Halbband" too -- with a digit sitting right
    # after it, that was matching and returning the wrong number entirely
    # (returned "1" from "Halbband 1" for a title that should give "6").
    m = GERMAN_ORDINAL_BAND_RE.search(title)
    if m:
        return GERMAN_ORDINALS.get(m.group(1).lower())
    m = BAND_NUMBER_IN_HEADING_RE.search(title)
    if m:
        return int(m.group(1))
    return None


def band_for_page(toc: list[dict[str, Any]], page: int) -> Optional[int]:
    """Finds which Band-divider TOC entry (by page-range containment, not
    by the citing document's own heading -- confirmed necessary: a
    Personenregister/Ortsregister/Sachregister entry's own heading never
    mentions its Band at all, only its SIBLING divider entry
    ("Sechster Band: Niedersachsen...") does) covers `page`."""
    for entry in toc:
        start, end = entry.get("start_page"), entry.get("end_page")
        if start is None or end is None or not (start <= page <= end):
            continue
        band = parse_band_number_from_title(entry.get("title", ""))
        if band is not None:
            return band
    return None


def first_page(doc: dict[str, Any]) -> Optional[int]:
    pr = doc.get("printed_page_range", "").replace("\u2013", "-")
    try:
        return int(pr.split("-")[0])
    except ValueError:
        return None


def volume_id_for(roman: str, sub1: Optional[str], sub2: Optional[str]) -> Optional[str]:
    n = roman_to_int(roman)
    if n is None:
        return None
    vid = f"eko{n}"
    if sub1:
        vid += f"_{sub1}"
    if sub2:
        vid += f"_{sub2}"
    return vid


def band_of(volume_id: str) -> Optional[int]:
    m = re.match(r"eko(\d+)", volume_id)
    return int(m.group(1)) if m else None


def is_continuation_line(line: str, bare_mode: bool) -> bool:
    """True if `line` continues the previous entry's citation list rather
    than starting a new entry. In marked mode (eko_reg), a line that
    itself starts with a Band marker is a continuation; in bare mode
    (eko_reg_6_7), a line starting with a digit is."""
    line = line.strip()
    if not line:
        return True
    if bare_mode:
        return bool(re.match(r"^\d", line))
    m = BAND_MARKER_RE.match(line)
    if m and roman_to_int(m.group(1)) is not None:
        return True
    return bool(re.match(r"^\d", line))


def strip_page_footer_artifacts(text: str) -> str:
    """Removes each page's own printed-page-number footer from the end
    of its own content, right before the transition to the next page.

    Confirmed as a systematic, universal OCR artifact, not a rare fluke
    -- checked all 84 page boundaries in eko_reg's real Personen section
    and found the identical pattern at every single one, e.g. "Fikensolt,
    Jost VII/2/1: 952\\n21\\n\\n[p. 22]": the bare "21" is page 21's own
    footer bleeding into the OCR text right at the page boundary, not a
    citation. Left unstripped, it gets swept up as a spurious extra page
    number for whatever entry happens to sit right before the page
    break -- confirmed directly: this exact mechanism produced the wrong
    "page=21" citation under "Fikensolt, Jost" and the wrong "page=70"
    under "Schwenk, Laurentz" in real resolution failures.

    Only strips a trailing number that EXACTLY matches the page's own
    label, immediately before the marker for the NEXT page -- so it
    cannot remove a genuine citation elsewhere in the text, and the one
    real remaining risk is narrow: a genuine final citation on some page
    that happens to equal that exact page's own number would also be
    stripped. Given the artifact fires on every page regardless of
    content (confirmed 84/84, not a coincidence tied to what any
    particular page happens to cite), that specific coincidence is rare
    against a near-certainty, so stripping is correct far more often
    than not."""
    matches = list(PAGE_MARKER_RE.finditer(text))
    if not matches:
        return text
    pieces = [text[:matches[0].start()]]
    for i, m in enumerate(matches):
        label = m.group(1) or m.group(2)
        seg_start = m.end()
        seg_end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        segment = text[seg_start:seg_end]
        if label and label.strip():
            segment = re.sub(r"\s*\b" + re.escape(label.strip()) + r"\s*$", "", segment)
        pieces.append(segment)
    return "".join(pieces)


def reconstruct_entries(text: str, bare_mode: bool) -> list[str]:
    """Rejoins an index section's OCR text (which wraps one logical entry
    across several physical lines) into one string per entry."""
    text = strip_page_footer_artifacts(text)
    text = PAGE_MARKER_RE.sub("", text)
    entries: list[str] = []
    current: list[str] = []
    for line in text.split("\n"):
        if not line.strip():
            continue
        if is_continuation_line(line, bare_mode) or not current:
            current.append(line.strip())
        else:
            entries.append(" ".join(current))
            current = [line.strip()]
    if current:
        entries.append(" ".join(current))
    return entries


def entry_headword(entry_text: str) -> str:
    """The label before the first citation -- a Band marker in marked
    mode, or the first bare digit otherwise. Returns "" (the caller
    already skips an empty headword) for the one specific garbage
    pattern confirmed against real text: a short fragment of BARE
    lowercase letters with no other structure at all -- e.g. "gg",
    found deep inside "Aepin, Johannes"'s own citation list ("gg9
    7015-17-18-24 7725.26.27..."), where OCR is misreading superscript
    footnote-marker digits as stray letters, not a new entry. This is
    deliberately narrow, not a general "must start uppercase" rule: an
    earlier, broader version of this guard was tested against real text
    and confirmed to silently discard genuine sub-entries that legitimately
    start with a parenthetical qualifier before the real name -- e.g.
    "(Boethius), Marquard" (a person's Latinized alternate name) and
    "(lTim 1,20)" (a Biblical citation identifying which "Alexander") --
    each with real page citations attached. Losing those confidently
    would have been a worse failure than the one being fixed, so only
    the confirmed pattern itself is excluded, nothing shaped like it."""
    m = BAND_MARKER_RE.search(entry_text)
    end = m.start() if m else len(entry_text)
    m2 = re.search(r"\d", entry_text[:end])
    if m2:
        end = min(end, m2.start())
    headword = entry_text[:end].strip(" ,-")
    if re.fullmatch(r"[a-zäöüß]{1,3}", headword):
        return ""
    return headword


def extract_marked_citations(entry_text: str) -> list[tuple[str, list[int]]]:
    """(volume_id, [pages]) for each Band marker found in one entry."""
    markers = list(BAND_MARKER_RE.finditer(entry_text))
    out = []
    for i, m in enumerate(markers):
        start = m.end()
        end = markers[i + 1].start() if i + 1 < len(markers) else len(entry_text)
        pages = [int(p) for p in PAGE_TOKEN_RE.findall(entry_text[start:end])]
        vid = volume_id_for(m.group(1), m.group(2), m.group(3))
        if vid and pages:
            out.append((vid, pages))
    return out


def extract_bare_pages(entry_text: str, headword: str, max_plausible: Optional[int] = None
                        ) -> tuple[list[int], list[int]]:
    """Returns (valid_pages, malformed_tokens).

    Confirmed a real, distinct problem from disambiguation: OCR routinely
    fuses a footnote-reference digit directly onto the page number
    immediately before it, with no separator -- e.g. eko_reg's own
    (correct) citation for Abraham reads "...991, 1048, 1067, 1156..."
    while eko_reg_6_7's bare-page version of the SAME citation reads
    "...991, 104812, 1067, 11567..." (footnote markers "12" and "7"
    fused onto pages 1048 and 1156). This is the exact same fusion
    pattern confirmed in the very first eko11 audit ("judicii6",
    "katechismus8") -- just onto a digit instead of a letter, which
    is syntactically much harder to catch: a token like "8044" could
    be "80" + footnote "44" fused, or could just be page 8044 in some
    other volume, with no way to tell from the digits alone.

    The one sub-case this CAN catch with confidence: max_plausible, when
    given, is the highest real page number among this citation's own
    candidate volumes (with headroom) -- any token exceeding it (e.g. a
    5+ digit blob like "104812" or "11567" in a Band whose real pages
    top out around 1300) is definitely not a real page number, whatever
    it actually is. Shorter fusions that happen to still look like a
    plausible page (the "8044" case) are NOT caught by this and remain
    a known, accepted residual gap -- there is no reliable way to
    distinguish them from a genuine page number by shape alone."""
    rest = entry_text[len(headword):] if entry_text.startswith(headword) else entry_text
    valid, malformed = [], []
    for token in PAGE_TOKEN_RE.findall(rest):
        n = int(token)
        if n <= 0 or (max_plausible is not None and n > max_plausible):
            malformed.append(n)
        else:
            valid.append(n)
    return valid, malformed


def load_volume_page_index(compiled_json_path: Path, load_text: bool = False
                            ) -> list[tuple[int, int, str, str, str]]:
    """Sorted [(start_page, end_page, citation, heading, text)] for one
    compiled volume's documents. `text` is only actually populated when
    load_text=True -- it exists to support content-based disambiguation
    for eko_reg_6_7's remaining ambiguous citations (checking whether an
    index entry's own name appears in a candidate document's real text,
    independent of any citation-number pattern), which eko_reg's own
    linking never needs, so it isn't loaded there by default."""
    with compiled_json_path.open(encoding="utf-8") as f:
        corpus = json.load(f)
    ranges = []
    for src in corpus.get("sources", []):
        for d in src.get("documents", []):
            pr = d.get("printed_page_range", "").replace("\u2013", "-")
            parts = pr.split("-")
            try:
                start, end = int(parts[0]), int(parts[-1])
            except ValueError:
                continue
            ranges.append((start, end, d["citation"], d["heading"], d.get("text", "") if load_text else ""))
    ranges.sort()
    return ranges


def resolve_page(page: int, ranges: list[tuple[int, int, str, str, str]]) -> Optional[tuple[str, str]]:
    for start, end, citation, heading, _text in ranges:
        if start <= page <= end:
            return citation, heading
    return None


def resolve_page_full(page: int, ranges: list[tuple[int, int, str, str, str]]
                       ) -> Optional[tuple[str, str, str]]:
    for start, end, citation, heading, text in ranges:
        if start <= page <= end:
            return citation, heading, text
    return None


def extract_search_token(headword: str) -> str:
    """The most distinctive, searchable part of an index headword --
    generally the surname, since entries are usually "Surname, Given
    name" or "von Surname, Given name". Stripping the nobility particle
    matters: "von" alone would match almost anything and tell us nothing."""
    core = headword.split(",")[0].strip()
    core = re.sub(r"^(von|de|zu|van)\s+", "", core, flags=re.IGNORECASE)
    return core.strip()


def content_match_disambiguate(
    headword: str, candidates: list[tuple[str, tuple[str, str, str]]]
) -> Optional[str]:
    """Among candidates = [(volume_id, (citation, heading, text)), ...],
    returns the one volume_id whose document text actually contains the
    entry's own name, if EXACTLY ONE does. Tried only as a last resort,
    after eko_reg's exact citation, plain range-containment, and
    eko_reg-neighbor interpolation have all already failed -- this is a
    genuinely independent signal from all three (it looks at what the
    source text says, not at citation-number patterns), but a much
    noisier one: common names will often appear in both candidates and
    settle nothing, which is why it's the last tier tried, not the first."""
    token = extract_search_token(headword)
    if len(token) < 3:  # too short/generic to mean anything if it matches
        return None
    matches = [vid for vid, (_, _, text) in candidates if token.lower() in text.lower()]
    return matches[0] if len(matches) == 1 else None


def build_corpus_index(sehling_root: Path, skip: set[str], load_text: bool = False
                        ) -> dict[str, list[tuple[int, int, str, str, str]]]:
    index = {}
    for d in sorted(sehling_root.iterdir()):
        if not d.is_dir() or d.name in skip:
            continue
        json_path = d / f"{d.name}.json"
        if not json_path.exists():
            continue
        try:
            with json_path.open(encoding="utf-8") as f:
                raw = json.load(f)
        except Exception as exc:
            print(f"  ! could not read {json_path}: {exc!r}")
            continue
        # A merged (--merge) output's own "sources" array has one entry
        # PER ORIGINAL TEILBAND COMBINED IN -- confirmed directly against
        # sehling_parser.py's own merge code, which appends one
        # SourceResult per volume id passed to --merge and does NOT
        # renumber citations across them. Skipped here rather than
        # ingested: its content is already fully present via the
        # original, finer-grained Teilband directories that normally
        # still sit alongside it in the same sehling/ root, so including
        # it too would add a redundant, Band-wide-range candidate for
        # every citation in that Band -- confirmed a real regression for
        # bare-page resolution specifically (eko_reg_6_7): a merged
        # "eko7" spans the union of eko7_1/eko7_2_1/eko7_2_2's ranges, so
        # it would spuriously match alongside whichever single sub-volume
        # a citation actually and uniquely belongs to, turning a clean
        # resolution into false ambiguity.
        if len(raw.get("sources", [])) > 1:
            print(f"  - {d.name}: skipped (a --merge output combining multiple Teilbande -- "
                  f"the original Teilband directories already cover this content)")
            continue
        try:
            index[d.name] = load_volume_page_index(json_path, load_text=load_text)
        except Exception as exc:
            print(f"  ! could not read {json_path}: {exc!r}")
    return index


def link_marked_register(
    register_json_path: Path, corpus_index: dict[str, list[tuple[int, int, str, str]]]
) -> tuple[list[dict[str, Any]], dict[str, int]]:
    with register_json_path.open(encoding="utf-8") as f:
        data = json.load(f)
    src = data["sources"][0]

    results = []
    stats = {"entries": 0, "citations": 0, "malformed_page_token": 0, "resolved": 0,
              "unresolved_volume": 0, "unresolved_page": 0}

    for doc in src["documents"]:
        if doc.get("heading_source") not in ("running_head", "toc_only"):
            continue
        section_label = doc.get("citation") or doc["heading"]
        if not any(section_label.startswith(prefix) or f"] {prefix}" in doc["heading"]
                   for prefix in ("1. Personen", "2. Orte", "3. Sachen")):
            # Front/back matter and anything else isn't an index section.
            if "1. Personen" not in doc["heading"] and "2. Orte" not in doc["heading"] and "3. Sachen" not in doc["heading"]:
                continue
        for entry_text in reconstruct_entries(doc["text"], bare_mode=False):
            headword = entry_headword(entry_text)
            if not headword:
                continue
            citations = extract_marked_citations(entry_text)
            if not citations:
                continue
            stats["entries"] += 1
            entry_result: dict[str, Any] = {"entry": headword, "links": [], "unresolved": []}
            for vid, pages in citations:
                ranges = corpus_index.get(vid)
                # Same confirmed OCR failure mode as eko_reg_6_7's bare
                # pages (a footnote digit fused onto the real page number
                # with no separator, e.g. "1048" + footnote "12" ->
                # "104812") -- previously only guarded against there, on
                # the mistaken assumption eko_reg's 99.9% resolution rate
                # meant it wasn't a real problem here too. A per-volume
                # cap is enough since each citation already names its own
                # single volume directly, unlike the bare-page format.
                max_plausible = max(end for _, end, _, _, _ in ranges) * 2 if ranges else None
                for page in pages:
                    stats["citations"] += 1
                    if max_plausible is not None and (page <= 0 or page > max_plausible):
                        stats["malformed_page_token"] += 1
                        entry_result["unresolved"].append(
                            {"volume": vid, "page": page,
                             "reason": "malformed page number -- likely a footnote-reference digit "
                                       "fused onto a real page number with no separator, not a real "
                                       "page reference"})
                        continue
                    if ranges is None:
                        stats["unresolved_volume"] += 1
                        entry_result["unresolved"].append(
                            {"volume": vid, "page": page, "reason": "volume not found in compiled corpus"})
                        continue
                    hit = resolve_page(page, ranges)
                    if hit is None:
                        stats["unresolved_page"] += 1
                        entry_result["unresolved"].append(
                            {"volume": vid, "page": page, "reason": "page not covered by any known document"})
                        continue
                    stats["resolved"] += 1
                    entry_result["links"].append(
                        {"volume": vid, "page": page, "citation": hit[0], "heading": hit[1]})
            if entry_result["links"] or entry_result["unresolved"]:
                results.append(entry_result)

    return results, stats


def build_known_page_volumes(eko_reg_json_path: Path) -> dict[int, set[str]]:
    """page_number -> set of volume_ids that eko_reg's OWN (explicitly
    Band-marked, confirmed 99.9% resolvable against the real corpus)
    citations assign that page number to.

    Built to disambiguate eko_reg_6_7's bare page numbers using eko_reg's
    own resolution as ground truth, because eko_reg_6_7's page-RANGE-only
    disambiguation turned out to be far less reliable than hoped once run
    against the real, full corpus: a 26.5% ambiguous rate, meaning
    Sehling's print pagination does NOT run cleanly non-overlapping
    across a Band's sub-volumes the way binding-driven splits ordinarily
    would -- multiple sub-volumes of the same Band genuinely do reuse the
    same page numbers. eko_reg was never confused by this in the first
    place, since it always states the sub-volume explicitly (VI/1 vs
    VI/2); reusing that as a lookup sidesteps needing to resolve the
    ambiguity from page ranges at all for any page eko_reg happens to
    have already cited somewhere."""
    with eko_reg_json_path.open(encoding="utf-8") as f:
        data = json.load(f)
    src = data["sources"][0]
    page_volumes: dict[int, set[str]] = defaultdict(set)
    for doc in src["documents"]:
        heading = doc["heading"]
        if not any(t in heading for t in ("1. Personen", "2. Orte", "3. Sachen")):
            continue
        for entry_text in reconstruct_entries(doc["text"], bare_mode=False):
            for vid, pages in extract_marked_citations(entry_text):
                for page in pages:
                    page_volumes[page].add(vid)
    return page_volumes


def build_sorted_known_pages(known_page_volumes: dict[int, set[str]], candidate_vids: list[str]
                              ) -> list[tuple[int, str]]:
    """Sorted (page, volume) pairs from eko_reg's own citations, restricted
    to pages where EXACTLY ONE of this Band's candidate sub-volumes claims
    it -- the set usable for interpolating a neighboring, unclaimed page."""
    out = []
    candidate_set = set(candidate_vids)
    for page, vids in known_page_volumes.items():
        matching = vids & candidate_set
        if len(matching) == 1:
            out.append((page, next(iter(matching))))
    out.sort()
    return out


def interpolate_volume(page: int, sorted_known: list[tuple[int, str]], max_gap: int = 5) -> Optional[str]:
    """If the nearest known pages immediately before AND after `page`
    (each within max_gap) agree on the same volume, infer `page` belongs
    to it too. Justified specifically for the confirmed real case this
    was built for -- eko7_1 and eko7_2_2's page ranges genuinely overlap,
    so range-containment alone can't disambiguate a page both claim, but
    a printed volume's own pages are contiguous: if page 500 and page 502
    both belong to eko7_2_2 (per eko_reg's own, already-precise
    citations), page 501 -- uncited by eko_reg itself, and ambiguous by
    range alone -- almost certainly does too. This is inference, not
    certainty, and is only ever tried after both eko_reg's exact
    citation and plain range-containment have already failed to resolve
    the page."""
    idx = bisect.bisect_left(sorted_known, (page,))
    before = sorted_known[idx - 1] if idx > 0 else None
    after = sorted_known[idx] if idx < len(sorted_known) and sorted_known[idx][0] != page else \
        (sorted_known[idx + 1] if idx + 1 < len(sorted_known) else None)
    if before and after and before[1] == after[1]:
        if (page - before[0]) <= max_gap and (after[0] - page) <= max_gap:
            return before[1]
    return None


def link_bare_register(
    register_json_path: Path,
    corpus_index: dict[str, list[tuple[int, int, str, str]]],
    known_page_volumes: Optional[dict[int, set[str]]] = None,
) -> tuple[list[dict[str, Any]], dict[str, int]]:
    with register_json_path.open(encoding="utf-8") as f:
        data = json.load(f)
    src = data["sources"][0]

    results = []
    stats = {"entries": 0, "citations": 0, "malformed_page_token": 0, "resolved_via_eko_reg": 0,
              "resolved_via_range": 0, "resolved_via_interpolation": 0, "resolved_via_content_match": 0,
              "ambiguous": 0,
              "unresolved_page": 0, "unresolved_band": 0}

    for doc in src["documents"]:
        heading = doc["heading"]
        if not any(kw in heading for kw in ("Personenregister", "Ortsregister", "Sachregister")):
            continue
        # The Band is NOT in this document's own heading (confirmed: it's
        # always just "1. Personenregister" etc, identical across every
        # Band) -- it has to be looked up via which Band-divider TOC entry
        # this document's own page falls under instead.
        page = first_page(doc)
        band_num = band_for_page(src.get("toc", []), page) if page is not None else None
        if band_num is None:
            stats["unresolved_band"] += 1
            continue
        candidate_vids = [v for v in corpus_index if band_of(v) == band_num]
        if not candidate_vids:
            stats["unresolved_band"] += 1
            continue
        # Generous headroom above this Band's own real max page -- wide
        # enough to never reject a genuine page number, tight enough to
        # catch the confirmed OCR failure mode (a footnote digit fused
        # onto a real page number with no separator, e.g. "104812" for
        # page 1048 -- see extract_bare_pages) once it inflates a token
        # into a range no real page in this Band ever reaches.
        max_plausible = max(end for _, end, _, _, _ in
                             (r for vid in candidate_vids for r in corpus_index[vid])) * 2
        # Computed once per Band, not per page: the pages eko_reg's own
        # citations already assign unambiguously among this Band's
        # candidates, sorted for nearest-neighbor interpolation (see
        # interpolate_volume) when a page itself isn't directly known.
        sorted_known = (build_sorted_known_pages(known_page_volumes, candidate_vids)
                        if known_page_volumes else [])

        for entry_text in reconstruct_entries(doc["text"], bare_mode=True):
            headword = entry_headword(entry_text)
            if not headword:
                continue
            pages, malformed = extract_bare_pages(entry_text, headword, max_plausible)
            stats["malformed_page_token"] += len(malformed)
            if not pages and not malformed:
                continue
            stats["entries"] += 1
            entry_result: dict[str, Any] = {"entry": headword, "links": [], "unresolved": []}
            for bad_token in malformed:
                stats["citations"] += 1
                entry_result["unresolved"].append(
                    {"page": bad_token, "reason": "malformed page number -- almost certainly a "
                                                   "footnote-reference digit fused onto a real page "
                                                   "number with no separator (confirmed pattern; see "
                                                   "extract_bare_pages), not a real page reference"})
            for page in pages:
                stats["citations"] += 1

                # Prefer eko_reg's own explicit answer first, when it has
                # one and it's unambiguous among this Band's candidates.
                known = (known_page_volumes.get(page, set()) & set(candidate_vids)
                         if known_page_volumes else set())
                if len(known) == 1:
                    vid = next(iter(known))
                    hit = resolve_page(page, corpus_index[vid])
                    if hit is not None:
                        stats["resolved_via_eko_reg"] += 1
                        entry_result["links"].append(
                            {"volume": vid, "page": page, "citation": hit[0], "heading": hit[1],
                             "resolved_via": "eko_reg_cross_reference"})
                        continue

                # Fall back to range-containment: accept only if exactly
                # one candidate sub-volume's own page range covers it.
                hits = [(vid, resolve_page(page, corpus_index[vid])) for vid in candidate_vids]
                hits = [(vid, hit) for vid, hit in hits if hit is not None]
                if len(hits) == 1:
                    stats["resolved_via_range"] += 1
                    vid, (citation, head) = hits[0]
                    entry_result["links"].append(
                        {"volume": vid, "page": page, "citation": citation, "heading": head,
                         "resolved_via": "page_range"})
                elif len(hits) > 1:
                    # Next: do eko_reg's own nearest-cited pages on either
                    # side of this one agree on the same volume?
                    interpolated = interpolate_volume(page, sorted_known) if sorted_known else None
                    if interpolated and interpolated in {vid for vid, _ in hits}:
                        stats["resolved_via_interpolation"] += 1
                        hit = dict(hits)[interpolated]
                        entry_result["links"].append(
                            {"volume": interpolated, "page": page, "citation": hit[0], "heading": hit[1],
                             "resolved_via": "eko_reg_interpolation"})
                        continue

                    # Last resort: does the entry's own name actually
                    # appear in only ONE candidate document's real text?
                    # Independent of every citation-number-based signal
                    # above, but noisier -- common names can appear in
                    # both, settling nothing, which is exactly why this
                    # runs last, not first.
                    full_hits = [(vid, resolve_page_full(page, corpus_index[vid])) for vid, _ in hits]
                    full_hits = [(vid, h) for vid, h in full_hits if h is not None]
                    content_pick = content_match_disambiguate(headword, full_hits) if full_hits else None
                    if content_pick:
                        stats["resolved_via_content_match"] += 1
                        citation, head, _text = dict(full_hits)[content_pick]
                        entry_result["links"].append(
                            {"volume": content_pick, "page": page, "citation": citation, "heading": head,
                             "resolved_via": "content_match"})
                    else:
                        stats["ambiguous"] += 1
                        entry_result["unresolved"].append(
                            {"page": page, "reason": "ambiguous -- multiple sub-volumes of this Band "
                                                      "claim this page, and neither an exact eko_reg "
                                                      "citation, its nearby pages, nor the entry's own "
                                                      "name in either candidate's text settle it",
                             "candidates": [h[0] for h in hits]})
                else:
                    stats["unresolved_page"] += 1
                    entry_result["unresolved"].append(
                        {"page": page, "reason": f"no sub-volume of Band {band_num} covers this page"})
            if entry_result["links"] or entry_result["unresolved"]:
                results.append(entry_result)

    return results, stats


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("register", help="Register volume id: eko_reg or eko_reg_6_7")
    parser.add_argument("--root", default="sehling", help="Path to the sehling/ output directory (default: sehling)")
    parser.add_argument("--out", default=None, help="Output file (default: <register>_linked.json)")
    args = parser.parse_args()

    print(f"link_register.py -- script version: {SCRIPT_VERSION}")

    root = Path(args.root)
    register_json_path = root / args.register / f"{args.register}.json"
    if not register_json_path.exists():
        print(f"Could not find {register_json_path} -- compile {args.register} first.")
        return

    print(f"Building page index across every compiled volume under {root}/ ...")
    # Document text is only loaded for eko_reg_6_7 -- it's needed there for
    # content-based disambiguation of ambiguous pages (see
    # content_match_disambiguate), and eko_reg's own linking never uses
    # it, so there's no reason to pay that memory/time cost for it.
    corpus_index = build_corpus_index(root, skip={"eko_reg", "eko_reg_6_7"},
                                       load_text=(args.register == "eko_reg_6_7"))
    print(f"  Indexed {len(corpus_index)} volumes: {', '.join(sorted(corpus_index))}")

    if args.register == "eko_reg_6_7":
        known_page_volumes = None
        eko_reg_path = root / "eko_reg" / "eko_reg.json"
        if eko_reg_path.exists():
            print(f"  Found {eko_reg_path} -- using its own explicit Band citations "
                  f"to disambiguate eko_reg_6_7's bare page numbers where possible.")
            known_page_volumes = build_known_page_volumes(eko_reg_path)
        else:
            print(f"  No compiled eko_reg found at {eko_reg_path} -- falling back to "
                  f"page-range-only disambiguation, which is less reliable (confirmed: "
                  f"a real run without it saw a 26.5% ambiguous rate). Compiling eko_reg "
                  f"and re-running will very likely resolve most of those.")
        results, stats = link_bare_register(register_json_path, corpus_index, known_page_volumes)
    else:
        results, stats = link_marked_register(register_json_path, corpus_index)

    out_path = Path(args.out) if args.out else Path(f"{args.register}_linked.json")
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\n{'=' * 60}\nDONE\n{'=' * 60}")
    print(f"Entries with at least one citation: {stats['entries']}")
    print(f"Total citations examined:           {stats['citations']}")
    for key, value in stats.items():
        if key in ("entries", "citations"):
            continue
        pct = f" ({value / stats['citations']:.1%})" if stats["citations"] else ""
        print(f"  {key:<20} {value}{pct}")
    print(f"\nLinked output: {out_path}")
    print("Every unresolved citation is kept in the output (under \"unresolved\", with a reason) "
          "rather than dropped -- check a sample of those before trusting the resolved ones fully, "
          "the same way every other number in this project has been checked against real text.")


if __name__ == "__main__":
    main()

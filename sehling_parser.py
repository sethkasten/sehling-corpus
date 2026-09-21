"""
Sehling / Heidelberg corpus parser (v3)
========================================

Scrapes one or more Heidelberg digi.hadw-bw.de "Sehling" volumes
(Die evangelischen Kirchenordnungen des XVI. Jahrhunderts) and compiles
each into a SINGLE, document-segmented, AI-readable Markdown + JSON
corpus suitable as input to an English translation workflow.

Changes from v2 (per the eko11 audit):

  * Removed the IIIF "layout-aware OCR" experiment entirely. Across a
    full 791-page volume it never once produced a usable coordinate-
    based reconstruction, and the extra per-page network call was the
    only source of fetch failures. Deleting it also removes that
    fragility.

  * `clean_ocr_text()` now strips the "Temporarily hide column" viewer
    toggle-button text (previously leaked into ~7% of blank pages).

  * The compiled output is organized by DOCUMENT, not by page. Each
    physical page previously carried ~40 lines of boilerplate
    (headers, a "Raw Heidelberg OCR" block nearly identical to the
    cleaned text, layout-diagnostic fields). That boilerplate plus the
    raw/clean duplication accounted for ~89% of eko11.md's 6.5MB, with
    the raw and clean OCR blocks differing by about 0.7% of their
    length. The compiled file now stores clean OCR exactly once per
    page, folded into continuous per-document prose with lightweight
    inline page markers (`[p. 26]`) for citation.

  * New document-boundary detection (`parse_running_head`) using
    Sehling's own running-head convention ("{Part} {Doc#} {Title}
    {Year}", e.g. "II 11 Priestereid 1528"), cross-checked against the
    volume's own table of contents so it (a) doesn't misfire on
    incidental Roman-numeral-looking text and (b) degrades gracefully
    to one undivided unit per TOC part if no headings are found. This
    replaces the front-page TOC as the segmentation signal -- the
    front-page TOC is accurate but far too coarse (in eko11 it has 15
    entries for 791 pages; some spans run 150-200 pages).

  * Each detected document gets a citation that carries BOTH the
    Sehling reference (Band/Teil/Part.Number) and the plain-language
    identity of the church order (territory + year), e.g.:

        [Sehling XI, I.1] Freie Reichsstadt Nürnberg -- Almosenordnung, 1522

  * Volume-agnostic: nothing below hardcodes eko11-specific page
    ranges, Roman numerals, or territory names. A volume (or list of
    volumes, for multi-Teilband Bände) is supplied on the command
    line.

  * Known unresolved ambiguity, by design: Sehling pages routinely
    interleave three kinds of text with no typographic marker
    surviving OCR -- primary-source prose, lettered cross-edition
    variant apparatus (a:, b:, ...), and cumulative-per-document
    numbered footnotes. Reliably splitting these apart from OCR text
    alone is not attempted here (see the audit's page-109 example:
    the physical top-to-bottom order is usually preserved, but with no
    structural marker to tell body text from apparatus). Instead, the
    compiled file opens with a short legend explaining the
    conventions (bare trailing digit = footnote marker, "a:"/"b:" =
    variant apparatus, "[...]" = modern editorial insertion) so a
    translating AI has the right mental model going in.

Usage:
    py sehling_parser.py eko11
    py sehling_parser.py eko11 --refresh
    py sehling_parser.py eko7 eko7_1 eko7_2 --out-name eko7-band     (multi-Teilband band)

See VOLUME_OVERRIDES near the bottom of the CONFIG section for a place
to hang volume-specific quirks (e.g. Band 24) once they're known --
nothing in the pipeline requires an override to run.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Optional
from urllib.parse import urljoin

try:
    import truststore
    truststore.inject_into_ssl()
except ImportError:
    # truststore is only needed on the Windows machine this was written
    # for (to use the OS certificate store instead of certifi). It is
    # not required to run this script -- e.g. it isn't installed in
    # this sandbox, where the network-touching parts aren't exercised.
    pass

import requests
from bs4 import BeautifulSoup


# ============================================================================
# CONFIGURATION
# ============================================================================

BASE = "https://digi.hadw-bw.de"

VOLUME_URL = BASE + "/view/{volume}?ui_lang=eng"
MANIFEST_URL = BASE + "/view/iiif/{volume}/manifest"
METS_URL = BASE + "/view/{volume}/mets"
OCR_URL = BASE + "/view/{volume}/{page}/text_ocr?ui_lang=eng"
PAGE_URL = BASE + "/view/{volume}/{page}"  # left plain -- this is a citation
                                            # link shown TO the person, not
                                            # fetched by this script, so
                                            # forcing a language on it isn't
                                            # this script's call to make.

OUTPUT_ROOT = Path("sehling")

REQUEST_TIMEOUT = 60
REQUEST_DELAY = 0.15

# Heidelberg's UI text which is NOT part of the actual OCR. Confirmed
# from two volumes now that this site's UI language is NOT fixed --
# eko11 came back in English, eko7_1 came back entirely in German (the
# marker heading itself is "OCR-Volltext", not "OCR fulltext" -- see
# _OCR_MARKER_RE below). The German strings here are the CONFIRMED real
# UI text (found via a contaminated eko7_1 page), not a guess -- an
# earlier version of this list had guessed "Spalte vorübergehend
# ausblenden", which is wrong; the real string is "Spalte temporär
# ausblenden".
OCR_INTERFACE_MARKERS = [
    "Information about OCR text",
    "Hinweise zum OCR-Text",
    "Temporarily hide column",
    "Spalte temporär ausblenden",
]

# Stock phrases Heidelberg uses on pages that have no usable OCR
# (blank versos, plates, etc.). Used only to mark a page `is_blank`
# for cleaner compiled output -- the text itself is still preserved.
BLANK_PAGE_MARKERS = [
    "there is no information available here for this page",
    "für diese seite sind hier keine informationen vorhanden",
]

# The heading BeautifulSoup looks for to find where the real OCR text
# starts on Heidelberg's page (see extract_ocr_text). Confirmed to
# appear as either "OCR fulltext" (English UI) or "OCR-Volltext"
# (German UI) depending on which language the site happened to serve
# for a given volume/session. These are two different words ("fulltext"
# vs "Volltext"), not a spelling variant of one, so both are matched
# explicitly rather than guessing at a transliteration.
#
# The actual fix for the language variance is upstream of this, at the
# request level: VOLUME_URL and OCR_URL both now append "?ui_lang=eng",
# a real, confirmed query parameter (found on Heidelberg's own "switch
# to English" link) that should make every fetch come back in English
# going forward, for any volume. This regex and the rescue built on it
# stay in place regardless, both because already-cached raw_ocr (like
# eko7_1's) predates the parameter and needs it applied retroactively,
# and as a safety net in case some future volume/page still doesn't
# respect the parameter for reasons this script can't predict.
_OCR_MARKER_RE = re.compile(r"ocr[\s\-]*(?:fulltext|volltext)", re.IGNORECASE)

# Fixed strings Heidelberg's page wraps the real OCR text in when
# extract_ocr_text()'s primary (BeautifulSoup tag-based) strategy fails
# to find the heading above and falls back to the whole page body --
# confirmed for German UI: a "Metadaten" sidebar, a citation dialog, a
# full nested table-of-contents dump (arbitrary length, so bounded by
# position rather than matched by content), viewer controls, then the
# marker, the real text, and a "Feedback"/copyright footer. This is
# used as a LAST-RESORT rescue inside clean_ocr_text() -- it runs
# unconditionally on every page (including ones the primary strategy
# extracted cleanly) but is a no-op unless the marker text is actually
# present, so it's safe either way, and -- since clean_ocr_text() runs
# fresh on cached raw_ocr every time, cache hit or not -- it also
# retroactively repairs a volume that was already scraped and cached
# before this fix existed, with no new network requests.
_TRAILING_FOOTER_MARKERS = [
    "Annotationen",  # German UI footer start
    "Feedback",      # if "Annotationen" isn't present but this is
]


def _rescue_from_viewer_chrome(text: str) -> tuple[str, bool]:
    """Best-effort extraction of real OCR content from a page whose
    extract_ocr_text() fell back to dumping the whole page body. See
    _OCR_MARKER_RE / _TRAILING_FOOTER_MARKERS above for what this is
    responding to. Returns (text, changed) -- (text unchanged, False) if
    no marker is found, which is the common case for a page that
    extracted cleanly."""
    marker_pos = None
    for match in re.finditer(_OCR_MARKER_RE, text):
        marker_pos = match.end()  # keep the LAST match: a nested TOC dump
        # on some pages could in principle contain the phrase again, but
        # never a second real marker after the true one.
    if marker_pos is None:
        return text, False

    rescued = text[marker_pos:]
    for footer in _TRAILING_FOOTER_MARKERS:
        idx = rescued.find(footer)
        if idx != -1:
            rescued = rescued[:idx]
            break
    return rescued.strip(), True

# Generic Holy-Roman-Empire territorial-title prefixes. Stripping one
# of these from the front of a TOC part's title turns e.g.
# "Freie Reichsstadt Nürnberg" into a short place label "Nürnberg"
# without hardcoding any specific territory name. Longest first so
# multi-word prefixes match before shorter ones.
TERRITORY_PREFIXES = [
    "Freie Reichsstadt",
    "Reichsstadt",
    "Markgrafschaft",
    "Grafschaft",
    "Herrschaft",
    "Fürstentum",
    "Erzstift",
    "Hochstift",
    "Reichsdorf",
    "Reichsdörfer",
]

# A part title's final "official name" component (before any comma or
# parenthetical qualifier) is what TERRITORY_PREFIXES gets stripped
# from. Sections that are not primary-source parts at all -- indices,
# AND editorial introductions -- are identified heuristically by
# keyword so they're never sub-segmented by the heading parser (an
# index page listing "I 1, 25" as a cross-reference would otherwise
# look exactly like a document-opening heading, and an introduction's
# own numbered points -- "1. Erstens...", "2. Zum andern..." -- would
# otherwise look exactly like the bare-arabic document-heading form
# confirmed in eko7_1; see ARABIC_HEADING_RE below).
NON_SOURCE_SECTION_KEYWORDS = [
    "register",  # index
    "index",
    "einleitung",  # editorial introduction
    "einführung",
    "vorbemerkung",
    "quellen",  # bibliography / sources-and-literature list -- confirmed real
    "literaturverzeichnis",  # in eko9: a numbered "Quellen- und Literaturverzeichnis"
                             # (e.g. "2. Abt.: Texte, Gütersloh 1924 Richter, ...")
                             # parses identically to a real document heading under
                             # the bare-arabic pattern, since a numbered bibliography
                             # entry has exactly the same "N. Author, Title, Place
                             # Year" shape. Never a primary source, same as an index.
]

# Structural container labels Sehling repeats across many territories
# within a volume ("Die Kirchenordnungen" -- confirmed in eko7_1 to
# recur once per territory: Bremen, Stade, Buxtehude, Verden,
# Osnabrück x2, Ostfriesland) that are real, scannable, source-bearing
# leaves -- unlike Einleitung/Register -- but whose own title is a
# generic label, not a place name. Used only when walking up a page's
# TOC ancestor chain to find a real territory name for citations (see
# resolve_place_label): skip past these, don't stop on them.
GENERIC_LEAF_LABELS = {"die kirchenordnungen", "kirchenordnungen"}


def _is_generic_leaf_label(title: str) -> bool:
    """True for a structural container label like "Die Kirchenordnungen"
    that isn't a place name -- checked as a PREFIX, not exact equality,
    because the label sometimes has the place folded right into it
    ("Die Kirchenordnungen Pommerns", confirmed real in eko4) rather than
    appearing as a separate ancestor entry the way it does elsewhere
    ("Die Kirchenordnungen" alone, with "Erzstift Bremen" one level up,
    confirmed real in eko7_1). An exact-match check missed this variant
    entirely, leaving every document in that section citing the identical
    generic label instead of the place name it already had folded in."""
    lowered = title.strip().lower()
    return any(lowered == label or lowered.startswith(label + " ") for label in GENERIC_LEAF_LABELS)


# Extension point for volume-specific quirks that don't fit the
# generic pipeline. Empty by default -- nothing below requires an
# entry here to run. Keyed by the Heidelberg volume id.
#
# Correction: an earlier version of this comment, going on secondhand
# info, said "Band 24 is the Generalregister" -- that's wrong, confirmed
# against Heidelberg's own master list at https://digi.hadw-bw.de/view/eko.
# Band 24 (id "eko24") is Siebenbürgen (Transylvania) -- an entirely
# ordinary territorial volume, structured like any other. The actual
# index volumes are separately, non-numerically labeled: "eko_reg" (31:
# Generalregister, covering the whole edition) and "eko_reg_6_7"
# (a combined register for just Bände 6 and 7). Neither needs a special
# case here either -- `check_volume_structure` below flags both
# automatically from their TOC shape (almost no Roman-numbered source
# parts), the same generic check that would flag any other volume this
# pipeline doesn't fit, with no hardcoded id list required.
#
# The full, confirmed volume-id list (32 ids: 24 Bände across 30
# Teilbände, plus the 2 register volumes) is:
#   eko1 eko2 eko3 eko4 eko5 eko6_1 eko6_2 eko7_1 eko7_2_1 eko7_2_2
#   eko8 eko9 eko10 eko11 eko12 eko13 eko14 eko15 eko16 eko17_1 eko17_2
#   eko18 eko19_1 eko19_2 eko20_1 eko20_2 eko21 eko22 eko23 eko24
#   eko_reg_6_7 eko_reg
VOLUME_OVERRIDES: dict[str, dict[str, Any]] = {}



# ============================================================================
# DATA STRUCTURES
# ============================================================================

@dataclass
class TocEntry:
    title: str
    start_page: Optional[int]
    end_page: Optional[int]
    href: Optional[str] = None
    level: int = 0
    # Derived fields (filled in by `annotate_toc_parts`), not present
    # in the raw scrape:
    part_roman: Optional[str] = None      # e.g. "III"
    place_label: Optional[str] = None     # e.g. "Freie Reichsstadt Nürnberg"
    is_source_part: bool = True           # False for Register/Index-like sections


@dataclass
class PageRecord:
    digital_page: str
    canvas_label: Optional[str]
    printed_page: Optional[int]

    source_url: str
    page_url: str
    image_url: Optional[str]

    raw_ocr: str
    clean_ocr: str
    is_blank: bool
    used_chrome_rescue: bool = False


@dataclass
class DocumentUnit:
    """One segmented church-order / document, possibly spanning many pages."""
    part_roman: Optional[str]
    part_title: Optional[str]
    place_label: Optional[str]
    doc_num: Optional[str]        # e.g. "4", "4a" (suffix folded in for display)
    doc_title: Optional[str]
    doc_year: Optional[str]
    pages: list[PageRecord] = field(default_factory=list)
    heading_source: str = "toc_only"  # "running_head" | "toc_only" | "front_matter" | "back_matter"
    heading_key: Optional[tuple] = None  # (roman, num, suffix) as in ParsedHeading.key, for internal use only
    heading_text: Optional[str] = None   # exact matched text, for the boundary audit
    numbering_convention: str = "roman"  # "roman" | "arabic" | "bare_title" -- which
                                          # heading pattern matched; controls citation
                                          # formatting (see format_citation)

    @property
    def first_page(self) -> PageRecord:
        return self.pages[0]

    @property
    def last_page(self) -> PageRecord:
        return self.pages[-1]

    @property
    def printed_page_range(self) -> str:
        printed = [p.printed_page for p in self.pages if p.printed_page is not None]
        if not printed:
            labels = [p.canvas_label for p in self.pages if p.canvas_label]
            if labels:
                return f"{labels[0]}\u2013{labels[-1]}" if len(labels) > 1 else labels[0]
            return "?"
        if len(printed) == 1 or printed[0] == printed[-1]:
            return str(printed[0])
        return f"{printed[0]}\u2013{printed[-1]}"

    @property
    def digital_page_range(self) -> str:
        first, last = self.first_page.digital_page, self.last_page.digital_page
        return first if first == last else f"{first}\u2013{last}"


# ============================================================================
# HTTP
# ============================================================================

class HeidelbergClient:

    def __init__(self) -> None:
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": (
                "SehlingCorpusParser/3.0 "
                "(research corpus extraction; Heidelberg digital collections)"
            ),
            "Accept-Language": "de,en;q=0.8",
        })

    def get(self, url: str) -> requests.Response:
        response = self.session.get(url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        if REQUEST_DELAY:
            time.sleep(REQUEST_DELAY)
        return response

    def get_text(self, url: str) -> str:
        return self.get(url).text

    def get_json(self, url: str) -> Any:
        return self.get(url).json()


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def normalize_space(text: str) -> str:
    """Conservative whitespace normalization. Does not modernize spelling,
    punctuation, capitalization, or historical orthography."""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.strip()


def parse_int(value: str) -> Optional[int]:
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


ROMAN_VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_to_int(value: str) -> Optional[int]:
    """Converts a Roman numeral to an integer, or None if `value` isn't one.
    Used for diagnostics and for validating candidate part labels -- not
    for any display purpose (the original label is always preserved)."""
    if not value:
        return None
    value = value.upper().strip()
    if not re.fullmatch(r"[IVXLCDM]+", value):
        return None
    total, previous = 0, 0
    for char in reversed(value):
        current = ROMAN_VALUES[char]
        total += current if current >= previous else -current
        previous = current
    return total if total > 0 else None


def clean_ocr_text(raw: str) -> tuple[str, bool, bool]:
    """Strip Heidelberg/UI artifacts only. Returns (clean_text, is_blank,
    used_chrome_rescue) -- the third value is True when
    _rescue_from_viewer_chrome() actually had to intervene, purely for
    auditability (see PageRecord.used_chrome_rescue).

    Does not modernize German, correct OCR spellings, reorder text,
    remove footnotes/apparatus, or alter historical punctuation.
    """
    text = raw.replace("\r\n", "\n").replace("\r", "\n")

    # Rescue first: if extract_ocr_text()'s primary strategy missed the
    # marker (confirmed cause: a German-UI page whose marker heading is
    # "OCR-Volltext" rather than the English "OCR fulltext" this was
    # originally written against) and fell back to the whole page body,
    # this cuts the real content out of the surrounding chrome. It is a
    # no-op when the marker isn't present, which is the normal case.
    rescued_text, used_chrome_rescue = _rescue_from_viewer_chrome(text)
    text = rescued_text

    for marker in OCR_INTERFACE_MARKERS:
        text = re.sub(rf"^\s*{re.escape(marker)}\s*\n+", "", text, flags=re.IGNORECASE)
        text = text.replace(marker, "")

    text = "\n".join(line.rstrip() for line in text.splitlines())
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    text = text.strip()

    is_blank = (not text) or any(
        marker in text.lower() for marker in BLANK_PAGE_MARKERS
    )
    if is_blank:
        text = ""

    return text, is_blank, used_chrome_rescue


# ============================================================================
# VOLUME METADATA
# ============================================================================

def parse_volume_metadata(html: str) -> dict[str, Any]:
    soup = BeautifulSoup(html, "html.parser")
    metadata: dict[str, Any] = {
        "title": None, "publication": None, "doi": None,
        "urn": None, "raw_title": None,
    }

    title = soup.find("title")
    if title:
        metadata["raw_title"] = title.get_text(" ", strip=True)

    text = soup.get_text("\n", strip=True)

    doi_match = re.search(r"https?://doi\.org/[^\s<>\"]+", text, flags=re.IGNORECASE)
    if doi_match:
        metadata["doi"] = doi_match.group(0).rstrip(".,;)")

    urn_match = re.search(r"urn:nbn:[^\s<>\"]+", text, flags=re.IGNORECASE)
    if urn_match:
        metadata["urn"] = urn_match.group(0).rstrip(".,;)")

    publication_match = re.search(
        r"(?:Published|Publiziert|Erscheinungsort|Publication)\s*:?\s*([^\n]+)",
        text, flags=re.IGNORECASE,
    )
    if publication_match:
        metadata["publication"] = publication_match.group(1).strip()

    h1 = soup.find("h1")
    if h1:
        metadata["title"] = h1.get_text(" ", strip=True)
    if not metadata["title"]:
        metadata["title"] = metadata["raw_title"]

    return metadata


def parse_band_designation(metadata: dict[str, Any], volume_id: Optional[str] = None
                            ) -> tuple[Optional[int], Optional[str]]:
    """Extracts (band_number, band_designation) from a metadata title such as
        "... (11. Band = Bayern, 1. Teil): Franken: ..."
        "... (7. Band = Niedersachsen, 2. Hälfte, 1. Halbband): ..."
    This pattern has held across every Heidelberg-Academy-era volume title
    checked (Bd. 7, 11, 15); it does not depend on any particular
    territory name.

    Falls back to the volume id itself when that fails -- confirmed a real
    gap: eko3's own scraped metadata title turned out to be just the
    edition's generic series name ("Evangelische Kirchenordnungen des XVI.
    Jahrhunderts"), with none of the per-volume "(N. Band = ...)" detail
    eko11's title had, so there was nothing in the text to extract at all.
    Heidelberg's own id scheme encodes the band number directly and
    reliably regardless (confirmed against their master volume list:
    eko1..eko24, with "_N" suffixes for Teilbände that don't change the
    leading number) -- this can recover the number even when it can't
    recover the fuller territory description that comes with it.
    """
    for field_name in ("title", "publication", "raw_title"):
        text = metadata.get(field_name)
        if not text:
            continue
        match = re.search(r"\((\d{1,2})\.\s*Band\s*=\s*([^)]+)\)", text)
        if match:
            return int(match.group(1)), match.group(2).strip()
    if volume_id:
        id_match = re.match(r"eko(\d{1,2})(?:_|$)", volume_id)
        if id_match:
            return int(id_match.group(1)), None
    return None, None


def strip_territory_prefix(place: str) -> str:
    """'Freie Reichsstadt Nürnberg' -> 'Nürnberg'; falls back to the
    input unchanged if no known generic territorial title is found, so
    it's always safe to call."""
    stripped = place.strip()
    for prefix in TERRITORY_PREFIXES:
        if stripped.startswith(prefix + " "):
            return stripped[len(prefix):].strip()
    return stripped


# ============================================================================
# TABLE OF CONTENTS
# ============================================================================

PAGE_RANGE_RE = re.compile(r"^\s*(\d+)\s*[-\u2013]\s*(\d+)\s+(.+?)\s*$")

TOC_PART_RE = re.compile(r"^([IVXLCDM]+)\.\s*(.+)$")


def parse_toc(html: str) -> list[TocEntry]:
    """Extracts page-range links from the Heidelberg volume page. This is
    the volume's own top-level table of contents -- accurate as a coarse
    partition of the whole page range, but (per the eko11 audit) far too
    coarse to use as a document boundary on its own; see
    `parse_running_head` / `segment_documents` below for the finer-grained
    pass."""
    soup = BeautifulSoup(html, "html.parser")
    entries: list[TocEntry] = []

    for link in soup.find_all("a", href=True):
        text = " ".join(link.get_text(" ", strip=True).split())
        if not text:
            continue
        match = PAGE_RANGE_RE.match(text)
        if match:
            start, end, title = int(match.group(1)), int(match.group(2)), match.group(3).strip()
            entries.append(TocEntry(
                title=title, start_page=start, end_page=end,
                href=urljoin(BASE, link["href"]), level=0,
            ))

    seen = set()
    result = []
    for entry in entries:
        key = (entry.title, entry.start_page, entry.end_page, entry.href)
        if key not in seen:
            seen.add(key)
            result.append(entry)

    return result


def check_volume_structure(toc: list[TocEntry], volume: str) -> Optional[str]:
    """Sanity check run once per volume, generalizing a specific lesson:
    Band 24 of this edition is a register/index volume (organized as
    Personen/Orte/Sachen -- persons/places/subjects -- not as territorial
    church orders), so the whole running-head-based segmentation model in
    this script doesn't apply to it at all. Rather than hardcode a list of
    known-different volumes, this checks the shape of the TOC itself: a
    normal territorial volume is mostly Roman-numeral source parts. If a
    volume comes back mostly non-numbered or non-source, segmentation will
    silently degrade to a handful of undivided part-sized blocks, which is
    a bad silent failure mode -- better to say so up front.
    Returns a warning string, or None if the volume looks ordinary."""
    if not toc:
        return "no TOC entries were found at all"
    numbered_source = sum(1 for e in toc if e.is_source_part and e.part_roman)
    fraction = numbered_source / len(toc)
    if fraction < 0.3:
        return (f"only {numbered_source}/{len(toc)} TOC entries are Roman-numbered "
                f"source parts ({fraction:.0%}). This volume may not be a standard "
                f"territorial church-order volume (e.g. an index/register volume) "
                f"-- the running-head segmentation this script does is unlikely to "
                f"produce a meaningful compiled corpus for it. Check `{volume}`'s "
                f"TOC by hand before trusting the output.")
    return None


def annotate_toc_parts(toc: list[TocEntry]) -> None:
    """Fills in part_roman / place_label / is_source_part on each TocEntry
    in place. Volume-agnostic: derives everything from the TOC's own text,
    the generic TERRITORY_PREFIXES list, and NON_SOURCE_SECTION_KEYWORDS."""
    for entry in toc:
        match = TOC_PART_RE.match(entry.title)
        if match and roman_to_int(match.group(1)) is not None:
            entry.part_roman = match.group(1)
            remainder = match.group(2)
        else:
            entry.part_roman = None
            remainder = entry.title

        # Short place label: text up to the first comma or opening
        # parenthesis, with the generic territorial title stripped.
        cut = re.split(r"[,(]", remainder, maxsplit=1)[0].strip()
        entry.place_label = strip_territory_prefix(cut) if cut else remainder.strip()

        lowered = entry.title.lower()
        entry.is_source_part = not any(kw in lowered for kw in NON_SOURCE_SECTION_KEYWORDS)

    apply_non_source_inheritance(toc)
    apply_editorial_sibling_exclusion(toc)


def immediate_parent(entry: TocEntry, toc: list[TocEntry]) -> Optional[TocEntry]:
    """The narrowest OTHER entry that strictly contains `entry`'s page
    range -- i.e. its immediate parent in the (implicit) TOC tree."""
    if entry.start_page is None or entry.end_page is None:
        return None
    candidates = [
        e for e in toc if e is not entry and e.start_page is not None and e.end_page is not None
        and e.start_page <= entry.start_page and entry.end_page <= e.end_page
        and (e.start_page, e.end_page) != (entry.start_page, entry.end_page)
    ]
    if not candidates:
        return None
    candidates.sort(key=lambda e: e.end_page - e.start_page)
    return candidates[0]


def apply_editorial_sibling_exclusion(toc: list[TocEntry]) -> None:
    """Excludes a Roman-numbered leaf from source-part status if it has a
    SIBLING (same immediate parent) that is itself a no-Roman, generic-
    content-labeled leaf ("Die Kirchenordnungen"/"Edition") -- i.e. that
    shared scope already has a clearly-designated real-content container
    elsewhere, making this entry very likely editorial/preliminary
    material for it, whatever its own title says, despite carrying a
    Roman numeral that makes it look exactly like an ordinary territorial
    source part at the TOC level.

    Confirmed a real, distinct case in eko8: Part I's own editorial
    discussion is split into three Roman-numbered TOC entries -- "I. Das
    Territorium", "II. Das hessische Landgrafenhaus und seine Politik",
    "III. Die hessische Reformationsgeschichte..." -- rather than one
    "Einleitung" block, immediately followed by their sibling "Die
    Kirchenordnungen" (the real, no-Roman documents container) covering
    the rest of the same Part. Two of the three correctly found nothing
    (the "concerning" diagnostic, exactly as they should -- a Landgrave's
    dynastic history was never going to contain a document heading);
    the third caught a bibliography citation ("2. Aufl. 1937... F.
    Gundlach, Catalogus professorum...") as a false document, via the
    same flat-structure arabic fallback that correctly helped eko9's
    genuinely bare-arabic territories -- confirming that fallback needs
    this exclusion as a companion, not just the heading-pattern guards
    already in place, since no amount of pattern-tuning would ever fix a
    leaf that was never a documents-container to begin with."""
    for entry in toc:
        if not entry.is_source_part or entry.part_roman is None:
            continue
        parent = immediate_parent(entry, toc)
        if parent is None:
            continue
        for other in toc:
            if other is entry:
                continue
            if immediate_parent(other, toc) is not parent:
                continue
            if other.is_source_part and other.part_roman is None and _is_generic_leaf_label(other.title):
                entry.is_source_part = False
                break


def apply_non_source_inheritance(toc: list[TocEntry]) -> None:
    """Propagates is_source_part=False DOWN to any entry nested inside an
    excluded ancestor, regardless of the entry's own title.

    Confirmed a real, clean gap in eko17_1: "Register" (593-613) is
    correctly excluded via NON_SOURCE_SECTION_KEYWORDS, but its own
    children -- "I. Bibelstellen" (593-600, a Bible-verse CITATION INDEX,
    not a document), "2. Personen", "3. Orte", "5. Sachen" -- are each
    annotated independently from their OWN title, which contains none of
    those keywords, so they were left is_source_part=True. "I.
    Bibelstellen" in particular carries its own Roman numeral, making it
    indistinguishable at the TOC level from an ordinary territorial
    source leaf -- it was the one Roman-numbered leaf that (correctly!)
    never found a single running head, no matter which heading-pattern
    fix was tried, because it was never going to: a scripture-verse index
    was never going to contain a document heading in the first place.
    This is the general fix, not a Register-specific one -- any entry
    nested inside an excluded ancestor inherits the exclusion, however
    deep, whatever its own title says."""
    for entry in toc:
        if not entry.is_source_part or entry.start_page is None or entry.end_page is None:
            continue
        for other in toc:
            if other is entry or other.is_source_part:
                continue
            if other.start_page is None or other.end_page is None:
                continue
            if other.start_page <= entry.start_page and entry.end_page <= other.end_page \
                    and (other.start_page, other.end_page) != (entry.start_page, entry.end_page):
                entry.is_source_part = False
                break


def toc_ancestor_path(toc: list[TocEntry], printed_page: Optional[int]) -> list[TocEntry]:
    """All TOC entries containing this page, most-specific (narrowest page
    range) first. Replaces an earlier version that returned only the FIRST
    matching entry in list order -- which is always the OUTERMOST one,
    since Sehling's own TOC nests entries in document order (Part, then
    territory, then Einleitung/Kirchenordnungen within it). That bug made
    every level below the top-level Part invisible to segmentation, which
    is exactly what collapsed all of eko7_1's genuinely nested structure
    (Part > Territory > Die Kirchenordnungen, sometimes a level deeper
    still) into one undivided block per top-level Part.
    Empty list for a page not covered by any TOC entry (front/back matter)."""
    if printed_page is None:
        return []
    matches = [e for e in toc if e.start_page is not None and e.end_page is not None
               and e.start_page <= printed_page <= e.end_page]
    matches.sort(key=lambda e: e.end_page - e.start_page)
    return matches


def is_leaf_entry(entry: TocEntry, toc: list[TocEntry]) -> bool:
    """True if no other TOC entry's page range sits strictly inside this
    one's -- i.e. nothing is nested under it. Used to keep the
    segmentation-report diagnostics scoped to the level that actually
    matters (the innermost containers documents can live in) instead of
    also reporting on every intermediate container on the way down to
    them, which was pure noise on a deeply nested volume like eko7_1."""
    if entry.start_page is None or entry.end_page is None:
        return True
    for other in toc:
        if other is entry or other.start_page is None or other.end_page is None:
            continue
        if entry.start_page <= other.start_page and other.end_page <= entry.end_page \
                and (other.start_page, other.end_page) != (entry.start_page, entry.end_page):
            return False
    return True


def resolve_place_label(path: list[TocEntry]) -> Optional[str]:
    """Walks a page's TOC ancestor chain (narrowest first) and returns the
    first title that names an actual place/territory rather than a
    generic structural label. Needed because the immediate containing
    entry for a document is often "Die Kirchenordnungen" (see
    GENERIC_LEAF_LABELS) -- the real territory name ("Erzstift Bremen",
    "Grafschaft Ostfriesland und des Harlingerland") is usually one or two
    levels further up, not in the entry that actually bounds the document.

    But sometimes the place is folded right into the generic label instead
    of appearing as a separate ancestor -- confirmed real in eko4: "Die
    Kirchenordnungen Pommerns" has no more specific parent above it at
    all, so treating it as pure boilerplate to skip past (as eko7_1's
    plain "Die Kirchenordnungen" correctly is) left 15 separate documents
    all citing the identical, unhelpful generic label. When the generic
    prefix has a remainder after it, that remainder IS the place name."""
    for entry in path:
        lowered = entry.title.strip().lower()
        matched = next((label for label in GENERIC_LEAF_LABELS
                         if lowered == label or lowered.startswith(label + " ")), None)
        if matched:
            remainder = entry.title.strip()[len(matched):].strip(" .,")
            if remainder:
                return remainder
            continue
        if entry.place_label:
            return entry.place_label
    return None


def nearest_arabic_context(path: list[TocEntry]) -> Optional[TocEntry]:
    """The WIDEST ancestor (least to most specific, i.e. outermost first)
    that is a source part with no Roman numeral of its own -- the right
    container to gate and sequence-track the bare-arabic heading pattern
    against.

    This is deliberately not the immediate leaf, and -- confirmed by a
    second, different real case -- not even the NEAREST such ancestor
    either; it's the OUTERMOST one available. Two confirmed real
    structures need this:

    - eko7_1's Ostfriesland: "Die Kirchenordnungen" (no Roman numeral)
      contains four Roman-numbered SECTION DIVIDERS ("I. Landesherrliche
      ...", "II. Landesverträge", ...), each its own leaf. Documents
      inside them are still bare-arabic-numbered as one sequence running
      straight through all four (1, 4, 6, 20...) -- the dividers organize
      the list without renumbering it.

    - eko3's Mark Brandenburg: FOUR SIBLING sections at the same nesting
      depth -- "Die Kirchenordnungen", "Die Herrschaften Beeskow und
      Storkow", "Die Besitzungen der Familie von der Schulenburg", and
      "Städte und Ortschaften der Mark Brandenburg" -- share ONE
      continuous numbering (confirmed: 1...6, then 7, 9, 10 across the
      first three, with the fourth's own real numbers starting at 11).
      None of these four has a Roman numeral, so the NEAREST
      no-Roman ancestor is each section itself -- which was exactly the
      bug: each of the four got treated as a fresh, independent count,
      and "Städte und Ortschaften"'s real first number (11) was rejected
      as implausibly large for a fresh start (see
      ArabicSequenceTracker.MAX_PLAUSIBLE_FIRST_NUM), silently falling
      back to whatever small, wrong number a footnote or citation
      supplied instead. Walking to the OUTERMOST qualifying ancestor
      ("Die Mark Brandenburg" itself) fixes this the same way for both
      structures: it's the largest cohesive grouping that still has its
      own top-level TOC entry, which is the right scope for one running
      count in both confirmed cases.

    Falls back to the leaf itself (path[0]) when NOTHING in the path
    qualifies -- confirmed a third real structure, in eko9: flat,
    single-level Roman-numbered territories ("II. Die Grafschaft
    Waldeck", "III. Die Grafschaft Solms", ...) with no intermediate
    no-Roman container the way eko7_1/eko3/eko4 have, whose own documents
    STILL use the bare-arabic convention directly (confirmed: "8. Die
    Wildunger Artikel der Superintendenten... 1539" inside Waldeck).
    Previously this returned None in exactly that case, meaning the
    arabic pattern was never even attempted -- the whole 148-page section
    fell back to one undivided toc_only block, with the note correctly
    saying detection was "attempted" (the Roman pattern was) but not
    mentioning that arabic never got a turn at all. The leaf's own Roman
    numeral doesn't matter once Roman has already failed and arabic is
    what's left to try; it only needs a stable page-range identity to key
    the sequence tracker on, which the leaf already has.
    """
    context = None
    for entry in path:  # narrowest to widest -- keep walking so `context`
        # ends up holding the WIDEST qualifying ancestor, not the first
        # (nearest) one found; this loop deliberately does not `return`
        # early for exactly that reason (a `return entry` here would
        # silently undo the eko3 fix above by reverting to nearest-match
        # behavior -- confirmed the hard way: an earlier edit did exactly
        # that while adding the fallback below, and it cost eko3 more
        # than half its correctly-detected documents before being caught).
        if entry.is_source_part and entry.part_roman is None:
            context = entry
    if context is not None:
        return context
    return path[0] if path and path[0].is_source_part else None


def _looks_like_self_referential_divider(heading: "ParsedHeading", leaf: TocEntry) -> bool:
    """True if a Roman-prefixed "lone document, no number" match is really
    just a section-divider leaf restating its own TOC title, not a real
    document heading. Confirmed real case: eko7_1's "II. Landesverträge"
    (itself a Roman-numbered leaf/divider, not a document) spuriously
    matched the lone-document pattern -- roman="II", title captured
    starting with "Landesverträge" -- because its own divider heading is
    formatted exactly like "{roman}. {title}", and the real document that
    actually follows it ("4. Delfzijlischer Vergleich 1595") supplied the
    year the match needed. Rejecting this specifically (title's leading
    words equal the leaf's own TOC title) leaves genuine lone-document
    leaves like eko11's Windsheim/Castell alone, since those documents'
    real titles ("Ordnung, wie es nun hinfüro...") don't restate the TOC
    place name ("Freie Reichsstadt Windsheim") at all.

    The comparison strips a trailing year/date-range from the leaf's own
    TOC title before comparing word counts -- confirmed a real miss in
    eko9: Part I's own title is "Die geteilte Landgrafschaft Hessen 1582
    - 1618", but the matched heading's title has ALREADY had its year
    peeled off by the normal year-extraction step, leaving "Die geteilte
    Landgrafschaft Hessen" (4 words) to compare against "Die geteilte
    Landgrafschaft Hessen 1582 - 1618" (7 words) -- a same-length prefix
    slice can never equal a shorter list, so the divider went undetected
    and silently swallowed the section's real 132-page internal
    structure into one wrong "document". Comparing as a prefix in
    whichever direction is shorter (rather than assuming the leaf's own
    remainder is always the longer, unstripped side) keeps this correct
    regardless of which side carries extra trailing content.
    """
    if heading.num:  # only the no-number form can be self-referential this way
        return False
    match = TOC_PART_RE.match(leaf.title)
    leaf_remainder = (match.group(2).strip() if match else leaf.title.strip())
    leaf_remainder = re.sub(r"\s*\d{3,4}\s*(?:-|\u2013|bis|und)?\s*\d{0,4}\s*$", "", leaf_remainder).strip(" .,-")
    # Strip trailing punctuation from EACH word, not just the ends of the
    # two strings as a whole -- confirmed a real miss in eko2: the OCR
    # text reads "I. Das Bisthum Merseburg.\nHilfsmittel: ..." (a genuine
    # divider page, with a period after "Merseburg" carried over from the
    # source), while the TOC's own title has no such trailing period ("I.
    # Das Bisthum Merseburg"). That one-character difference on the last
    # compared word ("merseburg." vs "merseburg") was enough to fail an
    # exact per-word equality check, so the divider went undetected and
    # its entire 39-page section (plus its "Hilfsmittel:" bibliography,
    # itself contributing several candidate years) collapsed into one
    # wrong "document" with a garbled, bibliography-laden title.
    strip_word = lambda w: w.strip(".,;:()[]\"'")
    leaf_words = [strip_word(w) for w in leaf_remainder.lower().split()]
    heading_words = [strip_word(w) for w in heading.title.lower().split()]
    if not leaf_words or not heading_words:
        return False
    shorter, longer = (leaf_words, heading_words) if len(leaf_words) <= len(heading_words) else (heading_words, leaf_words)
    return longer[:len(shorter)] == shorter


# ============================================================================
# IIIF MANIFEST / CANVASES
# ============================================================================

def load_manifest(client: HeidelbergClient, volume: str) -> dict[str, Any]:
    return client.get_json(MANIFEST_URL.format(volume=volume))


def extract_canvases(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    sequences = manifest.get("sequences", [])
    if not sequences:
        raise RuntimeError("IIIF manifest contains no sequences.")
    canvases = sequences[0].get("canvases", [])
    if not canvases:
        raise RuntimeError("IIIF manifest contains no canvases.")
    return canvases


def canvas_page_id(canvas: dict[str, Any]) -> str:
    canvas_id = canvas.get("@id", "")
    match = re.search(r"/canvas/([^/]+)$", canvas_id)
    if match:
        return match.group(1)
    raise RuntimeError(f"Could not determine page ID from canvas: {canvas_id}")


def canvas_label(canvas: dict[str, Any]) -> Optional[str]:
    label = canvas.get("label")
    if label is None:
        return None
    if isinstance(label, str):
        return label.strip()
    if isinstance(label, dict):
        value = label.get("@value")
        return str(value).strip() if value else None
    return str(label).strip()


def canvas_image_url(canvas: dict[str, Any]) -> Optional[str]:
    images = canvas.get("images", [])
    if not images:
        return None
    return images[0].get("resource", {}).get("@id")


def printed_page_from_label(label: Optional[str]) -> Optional[int]:
    """Extracts the printed page number from a canvas label.

    Handles a real, confirmed 16th/19th-c. typesetting convention: a page
    inserted after the fact without renumbering the rest of the book,
    labeled with a trailing letter suffix on the preceding page's number
    (e.g. "725a" between 724 and 726). Confirmed directly against real
    data: eko1's page "725a" carries a complete, correctly-formed
    document heading ("171. Zwickau. Ordenung der pfarren und kirchen zu
    Zwickau. 1545.") -- a real, numbered church order -- that was being
    silently excluded from the volume's main document sequence and
    misfiled as back matter, purely because this function previously
    required an exact match against bare digits and returned None for
    anything else. That None then failed every TOC range-containment
    check downstream, the exact same failure mode a genuinely
    non-printed front/back-matter page ("a", "b", "i", "ii"...) produces
    -- with nothing to tell the two apart once the label was rejected.
    A suffixed insertion page always has the digits FIRST (never
    letters-only, which is what genuine front/back-matter labels look
    like), so requiring the digits to lead is what keeps this safe."""
    if not label:
        return None
    label = label.strip()
    if re.fullmatch(r"\d+", label):
        return int(label)
    m = re.fullmatch(r"(\d+)[a-zA-Z]+", label)
    if m:
        return int(m.group(1))
    return None


# ============================================================================
# OCR HTML EXTRACTION
# ============================================================================

def extract_ocr_text(html: str) -> str:
    """Extracts the OCR text from Heidelberg's text_ocr page. Deliberately
    removes only the interface heading; otherwise preserves the OCR as-is."""
    soup = BeautifulSoup(html, "html.parser")

    for element in soup.find_all(["script", "style", "nav", "header", "footer"]):
        element.decompose()

    marker = None
    for tag in soup.find_all(["h1", "h2", "h3", "h4", "div", "span", "p"]):
        text = " ".join(tag.get_text(" ", strip=True).split())
        if _OCR_MARKER_RE.fullmatch(text):
            marker = tag
            break

    if marker:
        for element in marker.find_all_next():
            if element.name in {"script", "style", "nav", "header", "footer"}:
                continue
            text = element.get_text("\n", strip=True)
            if len(text) > 30:
                return normalize_space(text)

    body = soup.body or soup
    text = body.get_text("\n", strip=True)
    for marker_text in OCR_INTERFACE_MARKERS:
        text = text.replace(marker_text, "")
    return normalize_space(text)


# ============================================================================
# DOCUMENT-BOUNDARY DETECTION (running-head parsing)
# ============================================================================

# "{Roman}{Num}{suffix?}.? {Title...} {Year}"
#
# Two alternative forms after the Roman numeral:
#   (a) NUMBERED  -- a digit follows, with or without a gap ("II9.",
#       "II 11.", "III 4 a" / "III4a" -- `num`/`suffix` are separate
#       groups precisely so a stray internal space doesn't produce a
#       different key).
#   (b) LONE-DOCUMENT -- no number at all, used by Sehling when a TOC
#       part contains only one document ("IX Kastenordnung 1524"). This
#       branch REQUIRES a real gap (space, or period + space) before the
#       title -- with no gap requirement here, "Im Advent 1516..." would
#       parse as roman "I" + title "m Advent..." (a real false positive
#       hit during testing: Part I's own Roman numeral is the single
#       letter most likely to collide with an ordinary German sentence-
#       initial word).
# A single capital "I" is also accepted as the doc-number itself (not
# just a suffix) because Fraktur OCR of a document numbered "1" comes
# back as "I" often enough to matter (observed: "VI I Kirchenordnung
# 1559" for what should be "VI 1 Kirchenordnung 1559") -- normalized to
# "1" after matching. Lowercase "l" was deliberately NOT added as a
# similar confusable: it's a common word-initial letter for continuation
# text at the top of a page, which would have made the numbered branch
# match a lot of unrelated prose.
HEADING_RE = re.compile(
    r"^(?P<roman>[IVXLCDM]{1,6})"
    r"(?:"
        r"\s*(?P<num>\d{1,3}|I)\s*(?P<suffix>[a-z])?\.?\s*"
        r"|"
        r"\.?\s+"
    r")"
    r"(?P<rest>\S.+)$"
)

YEAR_RE = re.compile(r"(?P<year>1[3-8]\d{2})")

# Bracket-stripping and the small headers Sehling uses on facing pages
# ("Rothenburg", "Brandenburg und Nürnberg gemeinsam") mean a real
# heading occasionally has its year on the NEXT physical OCR line, e.g.
#   "III 3. Die brandenburgisch-nürnbergische Kirchenordnung"
#   "von 1528."
# so candidate text is built from the first few lines joined together,
# not tested line-by-line in isolation.
_HEADING_SCAN_LINES = 3
_HEADING_SCAN_MAXLEN = 220


def normalize_heading_candidate(line: str) -> str:
    """Prepares a line of clean OCR for HEADING_RE matching ONLY -- this is
    not OCR cleanup and does not touch stored page text anywhere.

    Square brackets are stripped here because Sehling's editors bracket the
    numeral itself on a lone-document part's opening heading ("[IX].",
    "[X.]" -- see parse_running_head's docstring), and the bracket
    placement varies enough (before/after the period) that stripping it
    is simpler and more robust than matching every placement in the
    regex. This is deliberately kept as its own named step rather than
    buried inline: brackets carry real editorial meaning in this corpus
    (the legend in the compiled output explains it), so it matters that
    this is legible as "normalized for matching", not "sanitized"."""
    return line.strip().replace("[", "").replace("]", "")


@dataclass
class ParsedHeading:
    roman: str
    num: str
    suffix: str
    title: str
    year: Optional[str]
    matched_text: str  # the exact (normalized) text HEADING_RE matched, for audit

    @property
    def key(self) -> tuple[str, str, str, str]:
        # The title only needs to participate in uniqueness when neither a
        # Roman numeral nor an arabic number already does that job -- the
        # bare "Title. Year." convention (see parse_bare_title_heading),
        # which has no number of its own at all, so two DIFFERENT such
        # headings would otherwise collide on an identical ("", "", "")
        # key and wrongly look like the same document continuing.
        title_component = self.title.lower() if not self.roman and not self.num else ""
        return (self.roman.upper(), self.num, self.suffix.lower(), title_component)

    @property
    def display_num(self) -> str:
        return f"{self.num}{self.suffix}" if self.num else ""


def parse_running_head(text: str, expected_roman: Optional[str]) -> Optional[ParsedHeading]:
    """Tries to parse the top of a page's clean OCR as a Sehling document
    running-head.

    `expected_roman` should be the Roman-numeral label of the TOC part this
    page already belongs to (from the coarse, reliable TOC pass). Requiring
    an exact match against it -- rather than just checking membership in
    the volume's full set of part labels -- is what keeps an incidental
    Roman-numeral-looking token, or a numbered clause ("I. Erstlich...",
    "II. Item...") inside the source prose itself, from being mistaken for
    a document heading belonging to some OTHER part. Pass None to disable
    the cross-check (e.g. exploratory use outside the normal pipeline).

    A year is REQUIRED for a match to count. Genuine Sehling headings in
    this corpus always carry one; requiring it is a deliberate bias toward
    under-detecting (falling back to one undivided unit for a part) rather
    than over-detecting (a false split in the middle of a real document,
    or picking up a numbered clause inside the primary source that
    happens to share the part's own Roman numeral), since the latter is
    the more misleading failure for a translator.
    """
    if not text:
        return None
    lines = [normalize_heading_candidate(ln)
             for ln in text.split("\n", _HEADING_SCAN_LINES)[:_HEADING_SCAN_LINES]]
    lines = [ln for ln in lines if ln]
    if not lines:
        return None
    combined = " ".join(lines)[:_HEADING_SCAN_MAXLEN]

    match = HEADING_RE.match(combined)
    if not match:
        return None
    roman = match.group("roman").upper()
    if roman_to_int(roman) is None:
        return None
    if expected_roman and roman != expected_roman.upper():
        return None

    rest = match.group("rest").strip()
    year_match = YEAR_RE.search(rest)
    if not year_match:
        return None  # no year -> not confident this is a real heading
    year = year_match.group("year")
    title = rest[:year_match.start()].strip().rstrip(" .")

    num = match.group("num") or ""
    if num == "I":
        num = "1"  # OCR 1/I confusable in the doc-number slot -- see note above

    # `rest` is greedy by design (it has to be, to find a year that can be
    # several words in), so match.end() runs to the end of the scan window,
    # not to the end of the heading. Trim the audit-trail text to just
    # "roman [num] title year" for something actually readable in a report.
    heading_end = match.start("rest") + year_match.end()

    return ParsedHeading(
        roman=roman, num=num,
        suffix=(match.group("suffix") or "").lower(),
        title=title, year=year,
        matched_text=combined[:heading_end],
    )


# A second, unrelated heading convention confirmed in eko7_1 (Band 7,
# Niedersachsen -- a Göttingen-era volume from 1963, a different editorial
# generation than eko11): individual documents inside a "Die
# Kirchenordnungen" section carry NO Roman-numeral prefix at all --
# e.g. "1. Agenda Wursatorum ecclesiastica... 1574" -- with numbering
# restarting at 1 for each territory, and continuing straight through
# any intervening Roman-numeral or lettered SECTION dividers ("I.
# Landesherrliche...", "a. aus der evangelischen Frühzeit...") that
# organize the list but aren't part of any document's own number
# (confirmed: Ostfriesland's list runs 1, 4, 6, 20... uninterrupted
# through four such dividers).
#
# This pattern has a much weaker anchor than HEADING_RE (no Roman
# numeral to cross-check), so it leans harder on other signals: it may
# ONLY be tried on a leaf whose own TOC entry has no Roman numeral and
# isn't Einleitung/Register (see segment_documents), and a match is only
# accepted if its number is strictly greater than the last one accepted
# in the same leaf (see ArabicSequenceTracker) -- a stray footnote
# number or enumerated clause at the top of a continuation page essentially
# never continues a strictly-increasing, editorially-assigned sequence.
ARABIC_HEADING_RE = re.compile(r"^(?P<num>\d{1,3})\.\s+(?P<rest>\S.+)$")

# German date phrases ("18. August 1540") and century references ("16.
# Jh.", short for "16. Jahrhundert") both parse identically to a document
# heading under ARABIC_HEADING_RE -- confirmed real false positives in
# eko3 (a date wrapping onto its own line as "18. August 1540.") and
# eko7_1 ("16. Jh. ist mitgeteilt von..." in a bibliography discussion,
# which fed a wrong number into the sequence tracker and blocked the
# genuinely next document from being accepted afterward, since it then
# looked like a backward jump). A number immediately followed by a month
# name or a century marker is never a document heading, regardless of
# what the sequence tracker would otherwise have allowed.
NON_HEADING_FIRST_WORDS = {
    "januar", "februar", "märz", "april", "mai", "juni", "juli", "august",
    "september", "oktober", "november", "dezember",
    # Abbreviated forms -- confirmed a real miss in eko11: "Am 6. Jan. 1544
    # hielt er dort die erste evangelische Predigt." parsed as num=6,
    # title="Jan", year=1544, since the guard only checked full month
    # names and "jan" (from "Jan.") isn't one.
    "jan", "jan.", "feb", "feb.", "mrz", "mrz.", "apr", "apr.", "jun", "jun.",
    "jul", "jul.", "sept", "sept.", "sep", "sep.", "okt", "okt.", "nov", "nov.",
    "dez", "dez.",
    "jh", "jh.", "jahrhundert", "jhs", "jhs.", "jahrhunderts",
}


class ArabicSequenceTracker:
    """Tracks the last accepted arabic document number per TOC leaf (keyed
    by the leaf's own page range, which is unique within a volume), so a
    candidate match can be rejected for not continuing the sequence.
    Gaps are fine (real editions skip/merge numbers); going backward,
    repeating, or jumping implausibly far ahead is not.

    The jump cap earns its place empirically, not just defensively:
    footnote numbering is cumulative across a whole document (confirmed
    repeatedly this session) and is BY CONSTRUCTION monotonically
    increasing, so "greater than the last accepted number" can never by
    itself tell a footnote from a real next document -- confirmed with a
    real false positive in eko7_1's Bremen section, where footnote "93."
    (with an incidental nearby year, in a citation) was the only
    candidate on its page and cleared every other check, immediately
    after the real document "3." (whose own running head repeats,
    unchanged, at the top of that same page -- correctly rejected for
    NOT being a new number, which is exactly what let 93 stand alone).
    The observed real gaps between genuine consecutive documents in this
    edition top out around 14 (Ostfriesland's confirmed 6 -> 20); a cap
    well above that but far below footnote-counter territory rules out
    this failure mode without costing real gaps.

    Split into would_accept (a non-mutating check) and record (commits
    the number) rather than one combined method, because -- once the
    heading search scans a whole page instead of just its top few lines
    (see parse_arabic_running_head) -- a line can match the numeric
    pattern and pass the sequence check, but then fail the year check
    a few lines later. That candidate must not have moved the tracker's
    state, or a real, later match on the same page would be compared
    against a rejected number instead of the last genuinely accepted one."""

    MAX_PLAUSIBLE_JUMP = 25
    # The very first candidate accepted for a leaf has no prior number to
    # sanity-check the jump against -- confirmed a real gap: eko7_1's
    # Stade (which has exactly one document, and it's unnumbered -- see
    # parse_arabic_running_head's docstring on the "lone document, no
    # number" case) had a footnote/citation number "58" accepted outright
    # as if it were the section's first document, precisely because there
    # was nothing yet to compare it against. Every confirmed real section
    # in this edition starts its numbering small; capping how large a
    # FIRST number can be closes this the same way the jump cap closes
    # the continuing-sequence version of the same problem.
    MAX_PLAUSIBLE_FIRST_NUM = 10

    def __init__(self) -> None:
        self._last: dict[tuple[int, int], int] = {}

    def would_accept(self, leaf: TocEntry, num: int) -> bool:
        last = self._last.get((leaf.start_page, leaf.end_page))
        if last is None:
            return num <= self.MAX_PLAUSIBLE_FIRST_NUM
        return last < num <= last + self.MAX_PLAUSIBLE_JUMP

    def record(self, leaf: TocEntry, num: int) -> None:
        self._last[(leaf.start_page, leaf.end_page)] = num


def parse_arabic_running_head(text: str, tracker: ArabicSequenceTracker,
                               leaf: TocEntry) -> Optional[ParsedHeading]:
    """Tries the bare "N. Title... year" form described above.

    Unlike parse_running_head, this scans the FULL page rather than just
    its first few lines. Confirmed necessary in eko3: unlike eko7_1
    (where a document heading is the very first thing on its opening
    page), eko3 opens each place-name entry with the place name itself
    plus often a substantial "Litteratur:" bibliography discussion
    BEFORE the actual numbered document -- the real heading's line
    position across a real sample ranged from line 3 to line 97, with a
    median around line 16. Every genuine heading in that sample would
    have been missed by a top-of-page-only scan.

    Scanning the whole page raises false-positive risk accordingly, so
    this leans on multiple safeguards together:
      - the German-date guard below rejects "18. August 1540" before
        it's ever treated as a candidate;
      - the year requirement only looks in a short window right after
        the match, not across the whole remaining page;
      - the strict-sequence check via `tracker` rejects anything that
        doesn't continue the numbering;
      - AND, confirmed necessary by testing against real eko7_1 data:
        of every candidate that survives the first three checks, this
        takes the SMALLEST, not the first one encountered top-to-bottom.
        Footnote and archival-citation numbers are common throughout a
        page's lower portion and are cumulative across a whole document
        (so they run much higher than the document list itself, and
        will readily clear "greater than the last accepted number") --
        confirmed real false positives include "Nr. 93", "Nr. 403",
        "Nr. 658" showing up where the genuine next document was "3",
        "5", "8". The smallest qualifying number is the one closest to
        the expected "last + 1", and is far less likely to be a runaway
        footnote counter than an implausibly large jump is.

    Returns a ParsedHeading with an empty `roman` (there isn't one in
    this convention) so downstream code can tell the two apart via
    heading.roman == "" if it ever needs to.
    """
    if not text:
        return None
    lines = [normalize_heading_candidate(ln) for ln in text.split("\n")]

    candidates: list[tuple[int, str, str, str, str]] = []
    for idx, line in enumerate(lines):
        if not line:
            continue
        match = ARABIC_HEADING_RE.match(line)
        if not match:
            continue

        # Strip ALL surrounding punctuation, not just ".,", before
        # comparing -- confirmed a real miss: "24. August) 1541" (a
        # closing parenthesis from "(d. i. am 24. August) 1541" wrapping
        # onto its own line) has rest_first_word "August)", which a
        # ".," -only strip leaves as "august)" -- never equal to "august"
        # in NON_HEADING_FIRST_WORDS, so the guard silently failed to
        # catch a date it was specifically built to catch.
        rest_first_word = match.group("rest").split(" ", 1)[0].strip(" .,():;\"'[]").lower()
        if rest_first_word in NON_HEADING_FIRST_WORDS:
            continue  # "18. August ..." -- a date, not a heading
        if match.group("rest").lstrip().startswith(("-", "\u2013", "\u2014")):
            # "3. - G. Heide, Beiträge zur Geschichte..." -- confirmed real
            # in eko11: a numbered bibliography/"Literatur" list entry
            # continuing across authors with a dash separator, inside an
            # ordinary Einleitung's own literature discussion rather than
            # a dedicated TOC-level bibliography section (which
            # NON_SOURCE_SECTION_KEYWORDS already excludes -- this is the
            # same failure mode appearing somewhere that exclusion can't
            # reach). A real document title essentially never starts with
            # a bare dash right after its number.
            continue

        num_int = int(match.group("num"))
        if not tracker.would_accept(leaf, num_int):
            continue

        window = " ".join([line] + lines[idx + 1:idx + 3])[:_HEADING_SCAN_MAXLEN]
        window_match = ARABIC_HEADING_RE.match(window)
        if not window_match:
            continue
        rest = window_match.group("rest").strip()
        year_match = YEAR_RE.search(rest)
        if not year_match:
            continue  # no year nearby -- not confident enough to accept

        year = year_match.group("year")
        title = rest[:year_match.start()].strip().rstrip(" .")
        heading_end = window_match.start("rest") + year_match.end()
        candidates.append((num_int, match.group("num"), title, year, window[:heading_end]))

    if not candidates:
        return None

    num_int, num_str, title, year, matched_text = min(candidates, key=lambda c: c[0])
    tracker.record(leaf, num_int)
    return ParsedHeading(
        roman="", num=num_str, suffix="",
        title=title, year=year,
        matched_text=matched_text,
    )


# A fourth heading convention, confirmed in eko4's Pommern section: a bare
# "Title. Year." running head with NO number and NO Roman numeral at all --
# e.g. "Kirchenordnung für Pommern von 1535.", "Pia ordinatio caeremoniarum
# 1535.", "Kirchenordnung von 1542." -- alternating, the same way as every
# other volume's running heads, with a generic verso header repeating the
# territory name ("Das Herzogthum Pommern."). Confirmed a REAL miss, not a
# hypothetical one: a single 166-page span that looked like one undivided
# document under the existing patterns actually contains at least 6-8
# distinct ones, each identifiable only by its opening page starting with
# a short title phrase ending in a year.
#
# This is the weakest-anchored of the four conventions -- no number to
# sequence-check at all -- so it leans on structural shape instead:
# the candidate must be the page's very first line (unlike the arabic
# pattern's whole-page scan, real examples here are consistently
# top-of-page); it must be reasonably short (a title, not a sentence that
# happens to end in a number); and, confirmed necessary the same way it
# was for the arabic pattern, a date phrase ("Sonntag, den 12. Mai 1573.")
# matches the shape just as well as a real title does, so the same
# NON_HEADING_FIRST_WORDS guard applies here too, checked against the
# word immediately BEFORE the year rather than immediately after a number.
BARE_TITLE_HEADING_RE = re.compile(r"^(?P<title>[A-ZÄÖÜ].{0,90}?)\.?\s+(?P<year>1[3-8]\d{2})\.?$")


def parse_bare_title_heading(text: str) -> Optional[ParsedHeading]:
    """Tries the bare "Title. Year." form described above, on the first
    line of a page's clean OCR only (not a whole-page scan -- real
    examples are consistently top-of-page, and scanning further would
    reopen the same footnote/citation collision risk the arabic pattern
    needed several guards for, with even less of an anchor to filter
    against here).

    No sequence tracker is possible for this convention (there's no
    number), so repeated exact titles are deliberately not deduplicated
    here -- see ParsedHeading.key, which folds the title itself into the
    uniqueness key precisely so two DIFFERENT bare-title headings are
    recognized as different documents, since neither has a number to do
    that job otherwise.
    """
    if not text:
        return None
    first_line = normalize_heading_candidate(text.split("\n", 1)[0])
    if not first_line:
        return None
    match = BARE_TITLE_HEADING_RE.match(first_line)
    if not match:
        return None

    title = match.group("title").strip().rstrip(" .,")
    last_word = title.rsplit(" ", 1)[-1].strip(" .,():;\"'[]").lower()
    if last_word in NON_HEADING_FIRST_WORDS:
        return None  # "..., den 12. Mai 1573." -- a date, not a title

    return ParsedHeading(
        roman="", num="", suffix="",
        title=title, year=match.group("year"),
        matched_text=first_line,
    )


# ============================================================================
# DOCUMENT SEGMENTATION
# ============================================================================

def _rescan_for_shorter_title(text: str, doc: DocumentUnit) -> Optional[str]:
    """Used only by _prefer_shortest_running_title below: re-applies
    whichever heading pattern originally matched this document (skipping
    the ArabicSequenceTracker/expected_roman gating those use during real
    segmentation, since we already know this page belongs to the right
    document -- we're just checking for a shorter restatement of the same
    heading, not making a new boundary decision). Returns None on no
    match, or if the doc number found doesn't match this document's own."""
    if not text:
        return None
    lines = [normalize_heading_candidate(ln)
             for ln in text.split("\n", _HEADING_SCAN_LINES)[:_HEADING_SCAN_LINES]]
    lines = [ln for ln in lines if ln]
    if not lines:
        return None
    combined = " ".join(lines)[:_HEADING_SCAN_MAXLEN]

    if doc.numbering_convention == "bare_title":
        return None  # no shorter alternate form for this convention -- see
                      # parse_bare_title_heading; the first-page title is
                      # already the only title there is.
    if doc.numbering_convention == "arabic":
        match = ARABIC_HEADING_RE.match(combined)
        if not match or match.group("num") != doc.doc_num:
            return None
    else:
        match = HEADING_RE.match(combined)
        if not match:
            return None
        roman = match.group("roman").upper()
        if doc.part_roman and roman != doc.part_roman.upper():
            return None
        num = match.group("num") or ""
        if num == "I":
            num = "1"
        display_num = f"{num}{(match.group('suffix') or '').lower()}"
        if display_num != (doc.doc_num or ""):
            return None

    rest = match.group("rest").strip()
    year_match = YEAR_RE.search(rest)
    if not year_match:
        return None
    return rest[:year_match.start()].strip().rstrip(" .")


def _prefer_shortest_running_title(doc: DocumentUnit) -> None:
    """A document's opening page sometimes has no distinct title at all --
    it just launches straight into the operative sentence ("Ordnung, wie
    es nun hinfüro mit dem gefelle dies gemeinen castens...") -- while
    Sehling's own running head on later pages of the SAME document gives
    a short, citation-worthy form ("Kastenordnung 1524"). Where both
    exist, prefer the shorter one as the canonical title; the full first-
    page wording is untouched in the document body either way."""
    if doc.heading_source != "running_head" or not doc.doc_title:
        return
    best = doc.doc_title
    for page in doc.pages:
        alt_title = _rescan_for_shorter_title(page.clean_ocr, doc)
        if alt_title and 2 <= len(alt_title) < len(best):
            best = alt_title
    doc.doc_title = best


def segment_documents(
    pages: list[PageRecord],
    toc: list[TocEntry],
) -> tuple[list[DocumentUnit], list[dict[str, Any]]]:
    """Groups pages into DocumentUnits.

    Outer structure comes from the volume's own TOC (reliable, exhaustive,
    non-overlapping per the audit). Inner structure -- the actual document
    boundaries -- comes from `parse_running_head` (Roman-prefixed
    convention, e.g. eko11's "II 11 Priestereid 1528") or
    `parse_arabic_running_head` (bare-arabic convention, e.g. eko7_1's
    "1. Agenda Wursatorum... 1574"), tried against whichever TOC entry
    MOST SPECIFICALLY contains a page -- not just the outermost Part, since
    a volume can nest several levels deep (Part > Territory > "Die
    Kirchenordnungen", confirmed 3-4 levels in eko7_1) and the actual
    document-bearing leaf is usually not the top one. If no heading is
    ever found within a leaf, that whole leaf becomes a single undivided
    DocumentUnit rather than being lost or mis-split.

    Every page ends up in exactly one DocumentUnit; nothing is dropped.
    Returns (documents, diagnostics) where diagnostics lists anything a
    human should spot-check (e.g. a leaf with zero detected sub-documents).
    """
    documents: list[DocumentUnit] = []
    diagnostics: list[dict[str, Any]] = []

    first_arabic_idx = next((i for i, p in enumerate(pages) if p.printed_page is not None), None)

    current: Optional[DocumentUnit] = None
    current_key: Optional[tuple] = None
    current_leaf: Optional[TocEntry] = None
    doc_count_per_leaf: dict[tuple[int, int], int] = {}
    arabic_tracker = ArabicSequenceTracker()

    def finalize():
        if current is not None:
            _prefer_shortest_running_title(current)
            documents.append(current)

    def toc_only_title(leaf: TocEntry, place: Optional[str]) -> str:
        # "Die Kirchenordnungen" as a title tells a reader nothing; prefer
        # the resolved place name for these generic structural containers.
        # "Einleitung" and similar ARE informative as-is, so leave those be.
        if _is_generic_leaf_label(leaf.title) and place:
            return place
        return leaf.title

    for idx, page in enumerate(pages):
        path = toc_ancestor_path(toc, page.printed_page)

        if not path:
            # Front matter (before the first Arabic page) or back matter
            # (after it) -- bucketed separately so no page is ever
            # silently dropped.
            bucket = "front_matter" if (first_arabic_idx is None or idx < first_arabic_idx) else "back_matter"
            if current is None or current_key != bucket:
                finalize()
                current = DocumentUnit(
                    part_roman=None, part_title=None, place_label=None,
                    doc_num=None,
                    doc_title="Front matter" if bucket == "front_matter" else "Back matter",
                    doc_year=None, heading_source=bucket,
                )
                current_key = bucket
                current_leaf = None
            current.pages.append(page)
            continue

        leaf = path[0]
        outer_part = path[-1]
        leaf_key = (leaf.start_page, leaf.end_page)

        heading = None
        convention = "roman"
        context_key = leaf_key
        if leaf.is_source_part:
            if leaf.part_roman:
                # This leaf IS itself Roman-labeled -- either a genuine
                # top-level Part (eko11's normal case) or, confirmed real
                # in eko7_1's Ostfriesland section, an inner SECTION
                # DIVIDER ("I. Landesherrliche...", "II. Landesverträge"...)
                # whose own documents still use the bare-arabic form, not
                # a per-document Roman prefix. Try the Roman pattern first
                # since it's the stronger anchor when it genuinely fires,
                # but reject a "lone document" match that's really just
                # the divider restating its own TOC title (see
                # _looks_like_self_referential_divider).
                candidate = parse_running_head(page.clean_ocr, leaf.part_roman)
                if candidate is not None and not _looks_like_self_referential_divider(candidate, leaf):
                    heading = candidate
                    convention = "roman"
            if heading is None:
                # Either no Roman numeral on this leaf at all, or the
                # Roman attempt above found nothing (or was rejected as
                # self-referential) -- fall back to the bare-arabic
                # pattern, tracked against the nearest ancestor that has
                # no Roman numeral of its own (see nearest_arabic_context
                # for why that's not always this same `leaf`, and why it
                # now sometimes falls back to being this same `leaf`).
                #
                # Since that fallback means arabic can now be attempted
                # even on a page whose leaf carries its own Roman numeral
                # (eko9's flat territories), it needs the same protection
                # bare_title already has below: it must not interrupt a
                # document the STRONGER Roman pattern is already tracking
                # in this same leaf, or an ordinary Roman running-head
                # variant that Roman itself fails to re-match on a given
                # page (ordinary and expected -- that's what "continuation
                # page" means) would get mistaken for a new arabic
                # document instead of correctly falling through to
                # continuation.
                protecting_roman_doc = (
                    current is not None and current_leaf is leaf
                    and current.heading_source == "running_head"
                    and current.numbering_convention == "roman"
                )
                if not protecting_roman_doc:
                    arabic_context = nearest_arabic_context(path)
                    if arabic_context is not None:
                        heading = parse_arabic_running_head(page.clean_ocr, arabic_tracker, arabic_context)
                        if heading is not None:
                            convention = "arabic"
                            context_key = (arabic_context.start_page, arabic_context.end_page)
            if heading is None:
                # Neither the Roman nor the arabic pattern found anything
                # -- last resort, confirmed necessary in eko4's Pommern
                # section: a bare "Title. Year." heading with no number at
                # all (see parse_bare_title_heading). Tried last because
                # it's the weakest-anchored of the three: no number to
                # sequence-check, so there's nothing stopping it from
                # firing on a page the other two patterns would have
                # caught more reliably if they'd matched at all.
                #
                # Critically, it must NEVER be allowed to interrupt a
                # document a STRONGER convention (Roman or arabic) is
                # already tracking in this same leaf -- confirmed a real
                # and severe regression: without this guard, an ordinary
                # abbreviated/reworded running-head repeat on a
                # continuation page of an already-correct roman/arabic
                # document (which naturally fails both of those patterns,
                # the same way it always has) would get caught by this
                # much weaker pattern instead and treated as a brand new
                # document, fragmenting already-correct results -- this
                # roughly DOUBLED document counts on eko7_1 and eko3
                # before the guard existed, entirely by fragmentation, not
                # by finding anything genuinely new. It's only safe to let
                # this pattern run when nothing stronger already has a
                # claim on the current page's document.
                #
                # Both guards on this page also require heading_source ==
                # "running_head" specifically, not just a convention check
                # -- confirmed a real, separate latent bug: DocumentUnit's
                # numbering_convention field defaults to "roman" for EVERY
                # document, including toc_only placeholders that were never
                # actually Roman-detected at all. Without this check, a
                # toc_only placeholder for a leaf silently satisfies
                # "convention == roman" and permanently blocks arabic (and
                # this guard) from ever breaking out of it on a later page
                # of the same leaf -- confirmed this cost eko3 more than
                # half its correctly-detected documents the moment the
                # arabic guard above was added using the convention check
                # alone, and had likely been quietly suppressing some
                # bare_title detections the same way ever since this guard
                # was first introduced.
                protecting_stronger_doc = (
                    current is not None and current_leaf is leaf
                    and current.heading_source == "running_head"
                    and current.numbering_convention in ("roman", "arabic")
                )
                if not protecting_stronger_doc:
                    candidate = parse_bare_title_heading(page.clean_ocr)
                    if candidate is not None:
                        heading = candidate
                        convention = "bare_title"

        if heading is not None:
            key = ("doc", context_key, heading.key)
            if current is None or current_key != key:
                finalize()
                place = resolve_place_label(path)
                current = DocumentUnit(
                    part_roman=outer_part.part_roman, part_title=outer_part.title,
                    place_label=place,
                    doc_num=heading.display_num, doc_title=heading.title,
                    doc_year=heading.year, heading_source="running_head",
                    heading_key=heading.key, heading_text=heading.matched_text,
                    numbering_convention=convention,
                )
                current_key = key
                current_leaf = leaf
                doc_count_per_leaf[leaf_key] = doc_count_per_leaf.get(leaf_key, 0) + 1
            current.pages.append(page)
            continue

        # No heading on this page. If we're still inside the same LEAF as
        # the current document, it's a continuation page (the common
        # case -- most pages of a multi-page document don't repeat a
        # parseable heading on every single page, e.g. verso pages that
        # carry an alternate running head instead).
        if current is not None and current_leaf is leaf:
            current.pages.append(page)
            continue

        # New leaf with no heading found yet -- open an undivided unit
        # for the whole leaf; later pages of the SAME leaf that do yield
        # a heading will still split off correctly above.
        key = ("leaf_only", leaf_key)
        finalize()
        place = resolve_place_label(path)
        current = DocumentUnit(
            part_roman=outer_part.part_roman, part_title=outer_part.title,
            place_label=place,
            doc_num=None, doc_title=toc_only_title(leaf, place), doc_year=None,
            heading_source="toc_only",
        )
        current_key = key
        current_leaf = leaf
        current.pages.append(page)

    finalize()

    # Diagnostics are scoped to LEAVES only (entries with nothing nested
    # inside them) -- checking every intermediate container on the way
    # down to a leaf (Part > Territory > Die Kirchenordnungen) was pure
    # noise on a nested volume like eko7_1, where it produced one entry
    # per territory per level for no actionable reason. Three genuinely
    # different situations get distinguished: a leaf deliberately excluded
    # (Register/Index/Einleitung); a leaf with no Roman numeral of its own
    # where a document WAS found (arabic convention succeeded -- no
    # diagnostic needed at all); and either kind of leaf where nothing was
    # found, which is the only case actually worth a look.
    for entry in toc:
        if not is_leaf_entry(entry, toc):
            continue
        leaf_key = (entry.start_page, entry.end_page)
        if not entry.is_source_part:
            diagnostics.append({
                "type": "non_source_section_excluded",
                "part": entry.title,
                "pages": f"{entry.start_page}-{entry.end_page}",
                "note": "Matched NON_SOURCE_SECTION_KEYWORDS (index/register "
                        "or an editorial introduction) and was deliberately "
                        "never scanned for document headings. Kept as one "
                        "undivided unit by design, not by omission.",
            })
        elif doc_count_per_leaf.get(leaf_key, 0) > 0:
            continue  # a document WAS found here -- nothing to report
        elif entry.part_roman is not None:
            diagnostics.append({
                "type": "no_running_head_in_numbered_part",
                "part": entry.title,
                "pages": f"{entry.start_page}-{entry.end_page}",
                "note": "This IS a Roman-numbered source leaf and heading "
                        "detection WAS attempted throughout it, but no "
                        "running head matched anywhere in its page range. "
                        "Worth a manual look if it's expected to contain "
                        "one or more church orders.",
            })
        else:
            diagnostics.append({
                "type": "not_a_numbered_part",
                "part": entry.title,
                "pages": f"{entry.start_page}-{entry.end_page}",
                "note": "This leaf has no Roman-numeral label of its own, "
                        "and the bare-arabic heading pattern was tried but "
                        "found nothing. Often this just means the leaf "
                        "contains exactly one unnumbered document (e.g. "
                        "eko7_1's Stade, whose sole church order carries "
                        "neither a Roman prefix nor an arabic number) -- but "
                        "if this leaf is expected to hold more than one "
                        "document, it's worth a manual look.",
            })

    return documents, diagnostics


def build_boundary_audit(documents: list[DocumentUnit]) -> list[dict[str, Any]]:
    """One row per detected document, in page order -- for spot-checking
    segmentation quality by scanning ~60-90 boundary points instead of all
    791 pages. `prev_doc_last_page` makes an adjacency check trivial: if a
    document's first page doesn't immediately follow the previous
    document's last page, something is off (a gap, or an overlap)."""
    rows = []
    prev_last_page = None
    for doc in documents:
        rows.append({
            "citation_key": f"{doc.part_roman or ''}.{doc.doc_num or ''}".strip("."),
            "heading_source": doc.heading_source,
            "doc_title": doc.doc_title,
            "doc_year": doc.doc_year,
            "first_printed_page": doc.first_page.printed_page,
            "first_digital_page": doc.first_page.digital_page,
            "last_printed_page": doc.last_page.printed_page,
            "prev_doc_last_page": prev_last_page,
            "matched_heading_text": doc.heading_text,
        })
        prev_last_page = doc.last_page.printed_page
    return rows


# ============================================================================
# CACHE (per-page, network-fetch results only -- unrelated to segmentation)
# ============================================================================

def cache_path(output_dir: Path, page_id: str) -> Path:
    return output_dir / "pages" / f"{page_id}.json"


def load_cached_page(output_dir: Path, page_id: str) -> Optional[dict[str, Any]]:
    path = cache_path(output_dir, page_id)
    if not path.exists():
        return None
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def save_cached_page(output_dir: Path, page_id: str, data: dict[str, Any]) -> None:
    path = cache_path(output_dir, page_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def cached_raw_ocr(data: Optional[dict[str, Any]]) -> Optional[str]:
    if not data:
        return None
    for key in ("raw_ocr", "ocr_text", "ocr", "text"):
        value = data.get(key)
        if isinstance(value, str) and value.strip():
            return value
    return None


# ============================================================================
# FETCH PIPELINE (network-dependent; one Heidelberg volume id)
# ============================================================================

@dataclass
class SourceResult:
    volume_id: str
    volume_url: str
    metadata: dict[str, Any]
    toc: list[TocEntry]
    pages: list[PageRecord]
    errors: list[dict[str, str]]


def fetch_source(client: HeidelbergClient, volume: str, output_dir: Path, refresh: bool) -> SourceResult:
    print(f"\n{'=' * 72}\nFETCHING: {volume}\n{'=' * 72}")

    print("1. Downloading volume metadata + TOC...")
    volume_url = VOLUME_URL.format(volume=volume)
    volume_html = client.get_text(volume_url)
    metadata = parse_volume_metadata(volume_html)
    print(f"   Title: {metadata.get('title')}")

    toc = parse_toc(volume_html)
    annotate_toc_parts(toc)
    print(f"   TOC entries: {len(toc)}")
    structure_warning = check_volume_structure(toc, volume)
    if structure_warning:
        print(f"   ! STRUCTURE WARNING: {structure_warning}")

    print("2. Downloading IIIF manifest...")
    manifest = load_manifest(client, volume)
    canvases = extract_canvases(manifest)
    print(f"   Canvases: {len(canvases)}")

    output_dir.mkdir(parents=True, exist_ok=True)
    with (output_dir / "manifest.json").open("w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    # metadata.json and toc.json are ALSO cached now -- confirmed a real
    # gap: they weren't before, so --offline mode (which reads them back
    # via load_source_from_cache_only) silently fell back to an empty TOC
    # for every volume fetched before this fix, with no error at all to
    # explain the degraded result. Existing cache directories from before
    # this fix are missing these two files; one ordinary (non-offline) run
    # against them will backfill both, reusing the already-cached pages/
    # (fast) while only the cheap volume-page request actually hits the
    # network again.
    with (output_dir / "metadata.json").open("w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)
    with (output_dir / "toc.json").open("w", encoding="utf-8") as f:
        json.dump([asdict(t) for t in toc], f, ensure_ascii=False, indent=2)

    print("3. Extracting OCR...")
    pages: list[PageRecord] = []
    errors: list[dict[str, str]] = []

    for index, canvas in enumerate(canvases, start=1):
        digital_page = canvas_page_id(canvas)
        label = canvas_label(canvas)
        printed_page = printed_page_from_label(label)
        source_url = OCR_URL.format(volume=volume, page=digital_page)
        page_url = PAGE_URL.format(volume=volume, page=digital_page)
        image_url = canvas_image_url(canvas)

        print(f"   [{index}/{len(canvases)}] page {digital_page} ({label or '?'})", end="", flush=True)

        try:
            cached = None if refresh else load_cached_page(output_dir, digital_page)
            raw_ocr = cached_raw_ocr(cached)

            if raw_ocr:
                print(" [cache]", end="")
            else:
                ocr_html = client.get_text(source_url)
                raw_ocr = extract_ocr_text(ocr_html)

            clean_ocr, is_blank, used_chrome_rescue = clean_ocr_text(raw_ocr)
            if used_chrome_rescue:
                print(" [chrome-rescued]", end="")

            record = PageRecord(
                digital_page=digital_page, canvas_label=label, printed_page=printed_page,
                source_url=source_url, page_url=page_url, image_url=image_url,
                raw_ocr=raw_ocr, clean_ocr=clean_ocr, is_blank=is_blank,
                used_chrome_rescue=used_chrome_rescue,
            )
            save_cached_page(output_dir, digital_page, asdict(record))
            pages.append(record)
            print()

        except Exception as exc:
            print(f" ERROR: {exc}")
            errors.append({"digital_page": digital_page, "error": repr(exc)})

    return SourceResult(volume_id=volume, volume_url=volume_url, metadata=metadata,
                         toc=toc, pages=pages, errors=errors)


def load_source_from_cache_only(volume: str, output_dir: Path) -> SourceResult:
    """Rebuilds a SourceResult purely from a previous run's cache, with no
    network access at all. Used by the offline test harness, and usable by
    anyone who wants to re-run segmentation/output-building after editing
    this script without re-scraping."""
    manifest_path = output_dir / "manifest.json"
    metadata_path = output_dir / "metadata.json"
    if not manifest_path.exists():
        raise FileNotFoundError(f"No cached manifest at {manifest_path}; run without --offline first.")

    with manifest_path.open(encoding="utf-8") as f:
        manifest = json.load(f)
    canvases = extract_canvases(manifest)

    metadata = {}
    if metadata_path.exists():
        with metadata_path.open(encoding="utf-8") as f:
            metadata = json.load(f)

    toc_path = output_dir / "toc.json"
    toc: list[TocEntry] = []
    if toc_path.exists():
        with toc_path.open(encoding="utf-8") as f:
            toc = [TocEntry(**t) for t in json.load(f)]
        annotate_toc_parts(toc)
        structure_warning = check_volume_structure(toc, volume)
        if structure_warning:
            print(f"   ! STRUCTURE WARNING: {structure_warning}")
    else:
        # Confirmed a real, silent-failure-prone gap: before toc.json was
        # cached at all (see fetch_source), --offline mode would reach
        # this branch for EVERY volume and proceed anyway with an empty
        # TOC -- no crash, just page-granularity front/back-matter output
        # and no clue why. Loud and blocking is correct here: there is no
        # way to produce a meaningful compiled corpus without the TOC, so
        # continuing silently would waste the run rather than save it.
        raise FileNotFoundError(
            f"No cached TOC at {toc_path}. This volume's cache predates "
            f"toc.json being saved (see fetch_source) -- run once WITHOUT "
            f"--offline to backfill it. That run will still reuse every "
            f"already-cached page under {output_dir / 'pages'} (fast, no "
            f"re-fetching), and only the volume's own metadata+TOC page "
            f"(one lightweight request) actually touches the network."
        )

    pages: list[PageRecord] = []
    errors: list[dict[str, str]] = []
    for canvas in canvases:
        digital_page = canvas_page_id(canvas)
        cached = load_cached_page(output_dir, digital_page)
        if not cached:
            errors.append({"digital_page": digital_page, "error": "no cached page found (offline mode)"})
            continue
        raw_ocr = cached.get("raw_ocr", "")
        clean_ocr, is_blank, used_chrome_rescue = clean_ocr_text(raw_ocr)
        canvas_label_value = cached.get("canvas_label")
        # Recomputed from the cached label, not trusted from the cache
        # file directly -- same principle as the Chrome-rescue fix
        # applied retroactively to already-cached raw_ocr. Confirmed a
        # real, previously-silent gap: printed_page_from_label used to
        # reject any label with a trailing letter suffix (a real
        # insertion-page convention, e.g. eko1's "725a"), so every
        # volume fetched before that fix has this wrong None baked into
        # its cache. Recomputing here means one ordinary --offline
        # re-run picks up the fix for the entire existing 30-volume
        # cache with no re-fetching at all, exactly like the OCR fix did.
        printed_page = printed_page_from_label(canvas_label_value)
        pages.append(PageRecord(
            digital_page=digital_page,
            canvas_label=canvas_label_value,
            printed_page=printed_page,
            source_url=cached.get("source_url", ""),
            page_url=cached.get("page_url", ""),
            image_url=cached.get("image_url"),
            raw_ocr=raw_ocr, clean_ocr=clean_ocr, is_blank=is_blank,
            used_chrome_rescue=used_chrome_rescue,
        ))

    return SourceResult(volume_id=volume, volume_url=VOLUME_URL.format(volume=volume),
                         metadata=metadata, toc=toc, pages=pages, errors=errors)


# ============================================================================
# OUTPUT: MARKDOWN
# ============================================================================

LEGEND = """\
> **How to read this file**
>
> This is OCR text from a critical scholarly edition (Sehling's *Die
> evangelischen Kirchenordnungen des XVI. Jahrhunderts*), not the plain
> prose of the original 16th-century documents. A few conventions
> survive the OCR pass and matter for translation:
>
> - **`[p. 123]`** marks a facsimile page boundary, for citing back to
>   the source. It is not part of the original text.
> - **A bare digit stuck directly onto a word** (e.g. `Athanasii7`,
>   `katechismus8`) is a footnote reference marker, not part of the
>   word or a real number. Footnote numbering is cumulative across an
>   entire document, not per page.
> - **A single lowercase letter followed by a colon** at the start of a
>   line (e.g. `a:`, `l:`, `m:`) introduces Sehling's own critical
>   apparatus: a note on how the text differs across historical
>   editions/prints of the same church order. This is editorial
>   apparatus, not part of the primary source.
> - **Square brackets `[...]`** mark an editorial insertion by
>   Sehling's (or his continuators') 20th-century editors -- e.g. a
>   supplied word, an editorial sub-table-of-contents, or a
>   cross-reference -- not text from the original 16th-century source.
> - Apparatus and footnote text is left inline, in whatever order the
>   OCR produced it, because reliably separating it from the primary
>   text is not possible without the original page image. On pages
>   with heavy apparatus, expect the primary text to be interrupted
>   mid-sentence by a block of notes and then resume afterward.
> - OCR quality is generally solid for German Fraktur but degrades on
>   any embedded Greek and on some proper names; treat unusual strings
>   with suspicion and check against the facsimile image linked in
>   each document's header when it matters.
"""


def format_citation(band_number: Optional[int], doc: DocumentUnit) -> str:
    ref = f"Sehling {band_number}" if band_number else "Sehling"
    if doc.numbering_convention in ("arabic", "bare_title"):
        # Both the bare-arabic ("1. Agenda Wursatorum... 1574") and bare-
        # title ("Kirchenordnung für Pommern von 1535.") conventions lack
        # a Roman-numeral prefix, so the place name is load-bearing for
        # telling documents apart here, not decorative -- confirmed a
        # real collision risk for the arabic form (eko7_1's Bremen and
        # Buxtehude both start at "1."), and there's even less to
        # disambiguate on for the bare-title form, which has no number at
        # all to begin with.
        parts = [p for p in (doc.part_roman, doc.place_label) if p]
        if parts:
            ref += ", " + "/".join(parts)
        if doc.doc_num:
            ref += f" Nr. {doc.doc_num}"
        return ref
    if doc.part_roman and doc.doc_num:
        ref += f", {doc.part_roman}.{doc.doc_num}"
    elif doc.part_roman:
        ref += f", {doc.part_roman}"
        if doc.place_label and not doc.doc_num:
            # An undivided toc_only/Einleitung-style unit under a Part that
            # has other, distinct such units (a real case in a nested
            # volume like eko7_1 -- Bremen's own Einleitung vs Stade's vs
            # Buxtehude's, all under the same outer Part) -- disambiguate
            # the same way, minus "Nr." since there's no document number.
            ref += f"/{doc.place_label}"
    return ref


def format_document_heading(band_number: Optional[int], doc: DocumentUnit) -> str:
    ref = format_citation(band_number, doc)
    place = doc.place_label or doc.part_title or "Front/back matter"
    title = doc.doc_title or "(untitled)"
    year = f", {doc.doc_year}" if doc.doc_year else ""
    return f"[{ref}] {place} \u2014 {title}{year}"


def build_document_body(doc: DocumentUnit) -> str:
    lines = []
    for page in doc.pages:
        if page.printed_page is not None:
            marker = f"[p. {page.printed_page}]"
        elif page.canvas_label:
            marker = f"[p. {page.canvas_label}]"
        else:
            marker = f"[digital p. {page.digital_page}]"
        if page.is_blank:
            continue
        lines.append(marker)
        lines.append(page.clean_ocr)
        lines.append("")
    return "\n".join(lines).strip()


def build_markdown(
    group_label: str,
    sources: list[SourceResult],
    band_number: Optional[int],
    band_designation: Optional[str],
    documents_by_source: dict[str, list[DocumentUnit]],
) -> str:
    lines: list[str] = []
    lines.append(f"# Sehling \u2014 {group_label}")
    lines.append("")

    if band_number or band_designation:
        lines.append(f"**Sehling Band:** {band_number or '?'} ({band_designation or 'designation unknown'})")
        lines.append("")

    lines.append("**Sources:**")
    for src in sources:
        lines.append(f"- `{src.volume_id}` \u2014 {src.metadata.get('title') or src.volume_url}: <{src.volume_url}>")
    lines.append("")

    lines.append(LEGEND)
    lines.append("")

    for src in sources:
        documents = documents_by_source[src.volume_id]
        if len(sources) > 1:
            lines.append(f"---\n\n# Teilband: {src.metadata.get('title') or src.volume_id}\n")

        for doc in documents:
            lines.append("---\n")
            lines.append(f"## {format_document_heading(band_number, doc)}")
            lines.append("")
            # Sehling citation ("where this was printed") and document
            # identity ("what this actually is") are kept as separate
            # fields here, not just folded into the heading line above --
            # the heading is for a human scanning the file; these are for
            # anything parsing the file that wants the territory, title,
            # or year without pulling them back out of that combined string.
            lines.append(f"- **Sehling citation:** {format_citation(band_number, doc)}")
            lines.append(f"- **Territory:** {doc.place_label or '(front/back matter)'}")
            lines.append(f"- **Document title (as extracted from the running head):** {doc.doc_title or '(none)'}")
            lines.append(f"- **Document year:** {doc.doc_year or '(none)'}")
            if doc.part_title:
                lines.append(f"- **TOC part:** {doc.part_title}")
            lines.append(f"- **Pages:** {doc.printed_page_range} "
                          f"(Heidelberg digital pages {doc.digital_page_range}, volume `{src.volume_id}`)")
            lines.append(f"- **First-page facsimile:** <{doc.first_page.image_url or doc.first_page.page_url}>")
            lines.append(f"- **Segmentation source:** `{doc.heading_source}`"
                          + (f" (matched: \"{doc.heading_text}\")" if doc.heading_text else ""))
            lines.append("")

            body = build_document_body(doc)
            lines.append(body if body else "*(no OCR text on these pages)*")
            lines.append("")

    return "\n".join(lines)


def build_json(
    group_label: str,
    sources: list[SourceResult],
    band_number: Optional[int],
    band_designation: Optional[str],
    documents_by_source: dict[str, list[DocumentUnit]],
) -> dict[str, Any]:
    return {
        "schema_version": "3.0",
        "group_label": group_label,
        "band_number": band_number,
        "band_designation": band_designation,
        "sources": [
            {
                "volume_id": src.volume_id,
                "volume_url": src.volume_url,
                "metadata": src.metadata,
                "toc": [asdict(t) for t in src.toc],
                "documents": [
                    {
                        "citation": format_citation(band_number, doc),
                        "heading": format_document_heading(band_number, doc),
                        "part_roman": doc.part_roman,
                        "part_title": doc.part_title,
                        "place_label": doc.place_label,
                        "doc_num": doc.doc_num,
                        "doc_title": doc.doc_title,
                        "doc_year": doc.doc_year,
                        "printed_page_range": doc.printed_page_range,
                        "digital_page_range": doc.digital_page_range,
                        "heading_source": doc.heading_source,
                        "heading_text": doc.heading_text,
                        "first_page_image_url": doc.first_page.image_url,
                        "text": build_document_body(doc),
                    }
                    for doc in documents_by_source[src.volume_id]
                ],
                "errors": src.errors,
            }
            for src in sources
        ],
    }


# ============================================================================
# MAIN
# ============================================================================

def parse_volume_group(
    volume_ids: list[str],
    refresh: bool = False,
    out_name: Optional[str] = None,
    offline: bool = False,
) -> None:
    group_label = out_name or "-".join(volume_ids)
    group_dir = OUTPUT_ROOT / group_label
    group_dir.mkdir(parents=True, exist_ok=True)

    client = None if offline else HeidelbergClient()

    sources: list[SourceResult] = []
    documents_by_source: dict[str, list[DocumentUnit]] = {}
    all_diagnostics: dict[str, list[dict[str, Any]]] = {}

    band_number, band_designation = None, None

    for volume in volume_ids:
        override = VOLUME_OVERRIDES.get(volume, {})
        source_dir = OUTPUT_ROOT / volume

        if offline:
            result = load_source_from_cache_only(volume, source_dir)
        else:
            result = fetch_source(client, volume, source_dir, refresh)

        sources.append(result)

        vol_band_number, vol_band_designation = parse_band_designation(result.metadata, volume)
        band_number = override.get("band_number", band_number or vol_band_number)
        band_designation = override.get("band_designation", band_designation or vol_band_designation)

        print(f"\n4. Segmenting documents for {volume}...")
        documents, diagnostics = segment_documents(result.pages, result.toc)
        documents_by_source[volume] = documents
        all_diagnostics[volume] = {
            "diagnostics": diagnostics,
            "boundaries": build_boundary_audit(documents),
        }
        print(f"   Documents detected: {len(documents)}  "
              f"(via running head: {sum(1 for d in documents if d.heading_source == 'running_head')})")
        # Only "no_running_head_in_numbered_part" is actually worth flagging
        # at the console; the other two diagnostic types are the expected,
        # by-design shape of every volume (an intro, an index) and would
        # just be noise printed 24 times over. All three are still written
        # to the report file for completeness.
        for diag in diagnostics:
            if diag["type"] == "no_running_head_in_numbered_part":
                print(f"   ! {diag['type']}: {diag['part']} (pages {diag['pages']})")

    print("\n5. Building compiled output...")
    markdown = build_markdown(group_label, sources, band_number, band_designation, documents_by_source)
    corpus = build_json(group_label, sources, band_number, band_designation, documents_by_source)

    md_path = group_dir / f"{group_label}.md"
    json_path = group_dir / f"{group_label}.json"
    report_path = group_dir / f"{group_label}.segmentation_report.json"

    md_path.write_text(markdown, encoding="utf-8")
    with json_path.open("w", encoding="utf-8") as f:
        json.dump(corpus, f, ensure_ascii=False, indent=2)
    with report_path.open("w", encoding="utf-8") as f:
        json.dump(all_diagnostics, f, ensure_ascii=False, indent=2)

    total_pages = sum(len(s.pages) for s in sources)
    total_docs = sum(len(d) for d in documents_by_source.values())
    total_errors = sum(len(s.errors) for s in sources)
    total_rescued = sum(1 for s in sources for p in s.pages if p.used_chrome_rescue)

    print(f"\n{'=' * 72}\nDONE\n{'=' * 72}")
    print(f"Markdown:            {md_path}")
    print(f"JSON:                {json_path}")
    print(f"Segmentation report: {report_path}")
    print(f"Pages:               {total_pages}")
    print(f"Documents:           {total_docs}")
    print(f"Errors:              {total_errors}")
    print(f"Chrome-rescued pages: {total_rescued}"
          + (f"  ({total_rescued / total_pages:.0%} of pages)" if total_pages else ""))
    if total_errors:
        print("\nWARNING: some pages failed to fetch. See source errors in the JSON.")
    if total_rescued == total_pages and total_pages > 0:
        print("WARNING: EVERY page needed the chrome rescue -- this volume's OCR pages "
              "are being served in a UI language/layout the primary extractor doesn't "
              "recognize at all (confirmed cause so far: German UI). The rescue is a "
              "safety net, not a substitute for fixing extract_ocr_text() for whatever "
              "this new variant is; check a sample page by hand.")


# ============================================================================
# CLI
# ============================================================================

def parse_volumes_batch(volume_ids: list[str], refresh: bool = False, offline: bool = False) -> None:
    """Processes each volume as its own fully independent, separately
    compiled corpus -- the right mode for "run this for all my volumes",
    as distinct from parse_volume_group's job of MERGING multiple ids into
    one combined corpus (correct only for genuine multi-Teilband Bände,
    e.g. eko7_2_1 + eko7_2_2 belonging to the same Band).

    This is the default for more than one volume id now specifically
    because the previous default (merge) was confirmed to produce exactly
    this failure: passing every volume id on one command line, the
    natural way to ask for "all of them", silently invoked the merge
    path -- writing one combined, oddly-named output for the whole batch
    under a folder named after every id concatenated together, rather
    than one compiled output per volume -- while manifest.json/pages/
    still got written per-volume during fetching (that part of the
    pipeline is genuinely per-source regardless of mode), which is
    exactly "I'm getting manifest.json and pages/ but no compiled
    eko*.md/json/report" with no error at all to explain it.

    A failure in one volume does not stop the batch; failures are
    collected and reported in a summary at the end so a 30-volume
    unattended run doesn't die on volume 4 and silently skip the rest.
    """
    results: dict[str, str] = {}
    for volume in volume_ids:
        print(f"\n{'#' * 72}\n# {volume}\n{'#' * 72}")
        try:
            parse_volume_group([volume], refresh=refresh, out_name=None, offline=offline)
            results[volume] = "ok"
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            print(f"\nFAILED: {volume}: {exc!r}")
            results[volume] = f"FAILED: {exc!r}"

    print(f"\n{'=' * 72}\nBATCH SUMMARY ({len(volume_ids)} volumes)\n{'=' * 72}")
    for volume, status in results.items():
        marker = "OK  " if status == "ok" else "FAIL"
        print(f"  [{marker}] {volume:<15} {status if status != 'ok' else ''}")
    failed = [v for v, s in results.items() if s != "ok"]
    if failed:
        print(f"\n{len(failed)} volume(s) failed: {', '.join(failed)}")
        print("Everything else in the batch still completed; re-run just the "
              "failed ids once you know why (existing cache for the others "
              "is untouched).")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Scrape and compile one or more Heidelberg Sehling volumes "
                    "into AI-readable, document-segmented corpora."
    )
    parser.add_argument("volumes", nargs="+", help="Heidelberg volume id(s), e.g. eko11. "
                                                     "Multiple ids are processed as SEPARATE volumes "
                                                     "by default -- pass --merge for a multi-Teilband "
                                                     "Band that should become one combined corpus "
                                                     "(e.g. eko7_2_1 eko7_2_2 --merge).")
    parser.add_argument("--refresh", action="store_true", help="Ignore cache, re-fetch everything.")
    parser.add_argument("--merge", action="store_true",
                        help="Combine all given volume ids into ONE compiled corpus, instead of "
                             "processing each separately. Only correct for Teilbände of the same "
                             "Band -- NOT a way to process 'all volumes' in one command; see --out-name.")
    parser.add_argument("--out-name", default=None, help="With --merge: name for the combined output "
                                                           "files (defaults to the volume ids joined "
                                                           "by '-'). Ignored without --merge.")
    parser.add_argument("--offline", action="store_true",
                        help="Rebuild output purely from a previous run's local cache, no network use.")
    args = parser.parse_args()

    if not args.merge and args.out_name:
        print("--out-name has no effect without --merge (each volume keeps its own name); "
              "add --merge if you meant to combine these ids into one corpus.")

    try:
        if args.merge or len(args.volumes) == 1:
            parse_volume_group(args.volumes, refresh=args.refresh, out_name=args.out_name, offline=args.offline)
        else:
            parse_volumes_batch(args.volumes, refresh=args.refresh, offline=args.offline)
    except KeyboardInterrupt:
        print("\nInterrupted.")
        sys.exit(130)
    except Exception as exc:
        print(f"\nFATAL ERROR: {exc}")
        raise


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Make the English-only edition of the master guide.

LITURGICAL_AND_ECCLESIASTICAL_LIFE_ENGLISH_ONLY.md is the same book with its
quotations in German, Latin, Low German and Low Dutch left out. It is made from
the master and is not edited by hand:
- a block quotation in one of those languages is dropped; its English
  translation follows it in the master and stays;
- in Chapter 6 each petition keeps its English rubric, bid and prayer and
  drops the original;
- the shorter quotations in the running text and the tables are replaced by
  their English, and the terms left in the original are followed by it, as
  the table in tools/master_english_text.py directs;
- the contents and the two indexes are rebuilt for the new text.
An entry of that table that no longer matches the master is reported.

Usage:
    python3 tools/master_english.py           write the English-only edition
    python3 tools/master_english.py --check   only report whether it is current
"""
import re
import sys

import master_persons
import master_scripture
import master_toc
from master_english_text import QUOTES, REPLACE, TERMS, TITLES

MASTER = 'LITURGICAL_AND_ECCLESIASTICAL_LIFE.md'
OUTPUT = 'LITURGICAL_AND_ECCLESIASTICAL_LIFE_ENGLISH_ONLY.md'

# Words that mark a passage as English; a quotation without enough of them is in the original.
ENGLISH = set('''the and of to that is be shall let it for with as which his he they them their this
unto thee thou thy hath are was not by or all also but him have from when there any were our we us
ye your who whom what into upon after before because should may might would every no so then than
these those such being been its one only other same'''.split())
FOREIGN = set('''der die das und ist nicht mit von zu den dem des ein eine einen sol soll sollen man sie
er wir uns auch auff auf dass daß wie wenn oder aber als alle allen sein seyn werden wird sind hat
haben gott gottes herrn sich durch denn doch nach noch vnd unnd jm im am zum zur bey bei vom aus auß
unde dat van wy schal scholen ock se ere eren kerken et est ad cum quod qui quae non ut sed per pro
nobis domine deus sunt esse ac atque vel aut enim autem quam sicut omnes omnia eius tuum tua nos vos
ab ex dei domini christi ecclesia ecclesiae quoque etiam hoc haec sit fiat tibi te'''.split())


def english(text):
    """Whether a passage is in English, by the share of common English words in it."""
    words = re.findall(r"[A-Za-zÄÖÜäöüß]+", text.lower().replace('[', '').replace(']', ''))
    en = sum(w in ENGLISH for w in words)
    fo = sum(w in FOREIGN for w in words)
    return en > 2 * fo


def drop_quotations(lines):
    """Drop the block quotations that are not in English, with the blank line after each."""
    out, i = [], 0
    while i < len(lines):
        if lines[i].lstrip().startswith('>'):
            j = i
            while j < len(lines) and lines[j].lstrip().startswith('>'):
                j += 1
            block = ' '.join(re.sub(r'^\s*>\s?', '', l) for l in lines[i:j])
            if english(block):
                out += lines[i:j]
            else:
                while j < len(lines) and not lines[j].strip() and out and not out[-1].strip():
                    j += 1                      # no double blank line where the quotation stood
            i = j
            continue
        out.append(lines[i])
        i += 1
    return out


PETITION = re.compile(r'^\*\*(Rubric|Bid|Prayer) \((English|German|Latin|Low German|Low Dutch)\)\.\*\*')


def petitions(lines):
    """In Chapter 6, keep the English of each rubric, bid and prayer, without its label."""
    out, i = [], 0
    while i < len(lines):
        m = PETITION.match(lines[i])
        if m and m.group(2) != 'English':
            while i < len(lines) and lines[i].strip():
                i += 1                          # the paragraph
            while i < len(lines) and not lines[i].strip():
                i += 1                          # and the blank lines after it
            continue
        if m:
            lines[i] = f'**{m.group(1)}.**' + lines[i][m.end():]
        out.append(lines[i])
        i += 1
    return out


def replace(text):
    """Apply the table of replacements; return the text and the entries that matched nothing."""
    stale = []
    for old, new in REPLACE:
        if old not in text:
            stale.append(old)
        text = text.replace(old, new)
    return text, stale


SPAN = re.compile(r'"([^"\s](?:[^"]{0,298}[^"\s])?)"|(?<![*\w])\*(?!\*)([^*]{1,300}?)(?<![*\s])\*(?![*\w])')
BOLD = re.compile(r'\*\*[^*]*(?:\*[^*]+\*[^*]*)*\*\*')
CITED = re.compile(r'\s*,?\s*(?:c\. )?\(?\d{4}')
# A parenthesis that gives a reference, not the English: Ps 124:8, Sehling 5, §3.4, Sayn 1590.
REF = re.compile(r' \((?=\d|Sehling|§|\[§|pp?\. |see |cf\. |compare '
                 r'|(?:[1-3] )?[A-Z][a-z]+\.? \d+(?:[:,.]\d|[);])|[A-ZÄÖÜ][\w\-äöü]+ (?:c\. )?\d{4})')


def gloss(text):
    """After the first use of each term of TERMS in a section, add its English in brackets. A
    term in a heading or a citation, one already beside its English, and a title followed by
    its year are left alone."""
    lines = text.split('\n')
    start = next(i for i, l in enumerate(lines) if l.startswith('## <a id="introduction"'))
    end = next(i for i, l in enumerate(lines) if l.startswith('## <a id="scripture-index"'))
    body = '\n'.join(lines[start:end])
    out, seen, skip = [], set(), False
    for block in re.split(r'(\n\s*\n)', body):
        if re.match(r'\s*#', block):
            seen = set()                        # a new section
            skip = bool(re.search(r'<a id="conv', block))   # the Conventions pair terms already
            heading, _, rest = block.partition('\n')
            out.append(heading + _ + (rest if skip else gloss_block(rest, seen)))
            continue
        if skip or block.lstrip().startswith(('<!--', '<div')):
            out.append(block)
        else:
            out.append(gloss_block(block, seen))
    return '\n'.join(lines[:start] + [''.join(out)] + lines[end:])


STOP = set('the and of to in for with a an or on at by from that his its their our your thy thee'.split())


def alike(english, text):
    """Whether a bracket gives the English of a term: whether they share a word."""
    def words(s):
        return {w[:5] for w in re.findall(r'[a-z]+', s.lower()) if len(w) > 2 and w not in STOP}
    return bool(words(english) & words(text))


def gloss_block(block, seen):
    bold = [(m.start(), m.end()) for m in BOLD.finditer(block)]
    out, last, listed = [], 0, 0
    for m in SPAN.finditer(block):
        term = ' '.join((m.group(1) or m.group(2)).split()).strip('*')
        if term not in TERMS:
            continue
        held = [(x, y) for x, y in bold if x <= m.start() and m.end() <= y]
        if held and not (held[0][0] + 2 == m.start() and re.fullmatch(r'[.,:;]?', block[m.end():held[0][1] - 2])):
            continue                            # in bold, unless the bold is the term alone
        if m.start() < listed:
            seen.add(term)                      # in a list of terms that follows its English
            continue
        if term in TITLES and block.lstrip().startswith('|'):
            continue                            # a title in a table of orders
        after, before = block[held[0][1] if held else m.end():], block[:m.start()]
        if CITED.match(after) or after.startswith(("'s", "’s")):
            continue                            # a title in a citation, or a possessive
        p = PAREN.match(after)
        code = bool(p) and bool(CODE.match(p.group(1).strip()))
        beside = bool(p) and not code and alike(TERMS[term], p.group(1))
        c = re.match(r',\s*([^,;.()]{1,80})', after)
        beside = beside or bool(c) and alike(TERMS[term], c.group(1))     # "term, its English"
        if before.rstrip().endswith('('):
            listed = m.end() + closing(after)   # the English is before the bracket
        if beside or before.rstrip().endswith('(') or term in seen:
            seen.add(term)                      # already beside its English, or glossed above
            continue
        seen.add(term)
        if p and not code and not held:         # the English goes first in the bracket after it
            out.append(block[last:m.end()] + f' ({TERMS[term]}; ')
            last = m.end() + 2
            continue
        inside = before.count('(') > before.count(')')     # in brackets already: use square ones
        english = TERMS[term].replace('[', '').replace(']', '') if inside else TERMS[term]
        out.append(block[last:m.end()] + (f' [{english}]' if inside else f' ({english})'))
        last = m.end()
    return ''.join(out) + block[last:]


QSPAN = re.compile(r'(?P<open>\()?(?P<b>\*\*)?(?:"(?P<q>[^"\s](?:[^"]{0,78}[^"\s])?)"'
                   r'|(?<![*\w])\*(?P<i>[^*]{1,80}?)\*(?![*\w]))'
                   r'(?(b)\*\*)')
PAREN = re.compile(r' \(((?:[^()]|\([^()]*\))*)\)')
CITATION = re.compile(r'(.*?);\s*((?:(?:Sehling|see|compare)\b|cf\.|ibid\.|\[?§|(?:[1-3] )?[A-Z][a-z]+\.? \d+[:,]\d).*)$', re.S)
ENGLISH_START = set('The A An I O God Lord Christ Jesus Holy Let We He Thy Our My Ye Amen Glory Blessed Praise '
                    'Lamb Father Son Spirit Ghost Supper Mass Confiteor In Of For To With Be Come Give'.split())


CODE = re.compile(r'[A-Z0-9][A-Z0-9/,;. –-]*$')      # a letter or number of a family: (A), (3/4)


def english_gloss(s):
    """Whether a parenthesis after a quoted word gives its English rather than a reference."""
    s = s.strip()
    first = s.split()[0] if s.split() else ''
    if CODE.match(s) or REF.match(' (' + s) or '"' in s:
        return False
    return first[:1].islower() or first.strip('"*,.;:!?') in ENGLISH_START


def quote_terms(text):
    """Put the short quotations of QUOTES into English, in the Introduction and the chapters. Where
    the master gives the English beside the quotation, "original" (English) or ("original",
    English), that English is used."""
    a, b = text.index('\n## <a id="introduction"'), text.index('\n## <a id="scripture-index"')
    c, d = text.index('\n## <a id="conventions"'), text.index('\n## <a id="ch1"')
    return text[:a] + quote_region(text[a:c]) + text[c:d] + quote_region(text[d:b]) + text[b:]


def quote_region(text):
    out, last = [], 0
    for m in QSPAN.finditer(text):
        key = ' '.join((m.group('q') or m.group('i') or '').split()).strip('*')
        if key not in QUOTES:
            continue
        b = m.group('b') or ''
        opened = '(' if m.group('open') else ''
        after = text[m.end():]
        c = re.match(r',\s*([^()"]+?)\)', after) if opened else None
        p = PAREN.match(after)
        quoted = bool(p) and re.fullmatch(r'"[^"]+"', p.group(1).strip())     # "original" ("English")
        if c and english_gloss(c.group(1)):
            new, end = f'({b}"{" ".join(c.group(1).split())}"{b})', m.end() + c.end()
        elif p and (quoted or english_gloss(p.group(1))):
            inner = ' '.join(p.group(1).split()).strip('"')
            ci = CITATION.match(inner)
            eng, cit = (ci.group(1), ci.group(2)) if ci else (inner, '')
            new = f'{opened}{b}"{eng}"{b}' + (f' ({cit})' if cit else '')
            end = m.end() + p.end()
        else:
            new, end = f'{opened}{b}"{QUOTES[key]}"{b}', m.end()
        out.append(text[last:m.start()] + new)
        last = end
    return ''.join(out) + text[last:]


def closing(text):
    """The offset in text of the bracket that closes one opened before it."""
    depth = 1
    for i, c in enumerate(text):
        depth += {'(': 1, ')': -1}.get(c, 0)
        if not depth:
            return i
    return len(text)


def make(master):
    """Return the English-only edition of the master, and the stale replacements."""
    lines = master.split('\n')
    lines = drop_quotations(lines)
    lines = petitions(lines)
    text, stale = replace('\n'.join(lines))
    text = quote_terms(text)
    text = gloss(text)
    text = master_toc.rebuild(text)[0]
    text = master_scripture.rebuild(text)[0]
    text = master_persons.rebuild(text)[0]
    return text, stale


def main():
    check = '--check' in sys.argv[1:]
    master = open(MASTER, encoding='utf-8').read()
    new, stale = make(master)
    for s in stale:
        print(f'not found in the master: {s[:80]!r}')
    try:
        old = open(OUTPUT, encoding='utf-8').read()
    except FileNotFoundError:
        old = None
    if check:
        print(f'{OUTPUT} is {"current" if new == old else "out of date"}')
        sys.exit(1 if stale or new != old else 0)
    if new != old:
        open(OUTPUT, 'w', encoding='utf-8').write(new)
    print(f'{OUTPUT} written: {len(new.splitlines())} lines')
    sys.exit(1 if stale else 0)


if __name__ == '__main__':
    main()

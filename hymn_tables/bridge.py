# -*- coding: utf-8 -*-
"""Resolve hymn identity across sources that cite in different languages.

Liliencron prints German incipit and English title side by side for 377
entries, which gives a ready-made bridge for the sources that supply only
an English title (HotD, Selnecker).
"""
import json, os, re, sys, unicodedata, difflib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from resolve import resolve, norm

def keyify(s):
    t = unicodedata.normalize('NFKD', (s or '').lower())
    t = t.replace('’', "'").replace('‘', "'").replace('—', ' ')
    t = ''.join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r'\b(the|a|an|o|oh|ye|thou|thy|thee|our|us|we|is|in|of|to|and|now)\b', ' ', t)
    t = re.sub(r'[^a-z ]', ' ', t)
    return re.sub(r'\s+', ' ', t).strip()

def build():
    """english-title key -> German incipit, learned from Liliencron."""
    bridge = {}
    for r in json.load(open(os.path.join(HERE, 'rows_liliencron.json'))):
        k = keyify(r['english'])
        if k and k not in bridge:
            bridge[k] = r['german']
    return bridge

_BRIDGE = build()
_KEYS = list(_BRIDGE)

def english_to_german(title):
    k = keyify(title)
    if k in _BRIDGE: return _BRIDGE[k], 1.0
    m = difflib.get_close_matches(k, _KEYS, n=1, cutoff=0.86)
    if m: return _BRIDGE[m[0]], difflib.SequenceMatcher(None, k, m[0]).ratio()
    return None, 0.0

def identify(german, english):
    """-> (canonical_title, literal_en, common_en, how)"""
    if german:
        c, lit, com, alt, ok = resolve(german)
        if ok: return c, lit, com, 'german'
    if english:
        g, score = english_to_german(english)
        if g:
            c, lit, com, alt, ok = resolve(g)
            if ok: return c, lit, com, f'english->german({score:.2f})'
    return None, None, None, 'unresolved'

"""Dump a raw span of a document (with line structure) for curation."""
import sqlite3, re, sys, os
DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'eko.db')
def text(did):
    return sqlite3.connect(DB).execute('SELECT text FROM documents WHERE id=?', (did,)).fetchone()[0]
def span(did, start, end=None, n=6000):
    t = text(did)
    m = re.search(start, t, re.S)
    if not m: raise SystemExit(f'start not found: {start}')
    s = m.start()
    if end:
        e = re.search(end, t[s:], re.S)
        if not e: raise SystemExit(f'end not found: {end}')
        return t[s:s + e.end()]
    return t[s:s + n]
if __name__ == '__main__':
    did = int(sys.argv[1]); start = sys.argv[2]
    end = sys.argv[3] if len(sys.argv) > 3 and sys.argv[3] else None
    n = int(sys.argv[4]) if len(sys.argv) > 4 else 6000
    print(span(did, start, end, n))

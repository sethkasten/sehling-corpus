"""Build hymns.db -- chief-hymn prescriptions from the Sehling corpus hymn tables."""
import sqlite3, json, os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lexicon
from resolve import resolve, preclean

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'hymns.db')

# canonical ordering of the church year so the table reads in liturgical sequence
ORDER = ['Advent','Christmas','Sunday after Christmas','New Year','Holy Innocents','Epiphany',
         'Purification','Septuagesima','Sexagesima','Quinquagesima','Lent','Passiontide',
         'Palm Sunday','Holy Week','Easter','Ascension','Sunday after Ascension','Pentecost',
         'Trinity','St John','Visitation','Annunciation','St Michael','Week ']
def sort_key(occ):
    for i, p in enumerate(ORDER):
        if occ.startswith(p):
            m = re.search(r'(\d+)', occ[len(p):])
            return (i, int(m.group(1)) if m else 0, occ)
    return (99, 0, occ)

def main():
    rows = []
    for fn in ['weissenfels','pommern','latin','german']:
        rows += json.load(open(os.path.join(os.path.dirname(OUT), 'hymn_tables', f'rows_{fn}.json')))

    if os.path.exists(OUT): os.remove(OUT)
    db = sqlite3.connect(OUT); c = db.cursor()
    c.executescript('''
    CREATE TABLE hymn_prescriptions (
      id               INTEGER PRIMARY KEY,
      occasion         TEXT NOT NULL,   -- 1. Sunday / Feast / Occasion
      original_title   TEXT NOT NULL,   -- 2. hymn title as printed in the source
      literal_english  TEXT,            -- 3. literal English of that title
      common_english   TEXT,            -- 4. received English hymn title, if one exists
      source           TEXT NOT NULL    -- 5. Sehling volume, order and pages
    );
    CREATE TABLE hymns (            -- lexicon: one row per distinct hymn
      canonical_title  TEXT PRIMARY KEY,
      literal_english  TEXT,
      common_english   TEXT,
      language         TEXT
    );
    CREATE TABLE attestations (     -- every printed spelling -> canonical hymn
      printed_title    TEXT,
      canonical_title  TEXT REFERENCES hymns(canonical_title),
      source           TEXT
    );
    CREATE TABLE translation_candidates (
      canonical_title  TEXT REFERENCES hymns(canonical_title),
      column_name      TEXT,     -- which output column the choice affects
      candidate        TEXT,
      chosen           INTEGER,  -- 1 = currently used in hymn_prescriptions
      status           TEXT      -- 'awaiting_adjudication' where rivals exist
    );
    CREATE INDEX ix_presc_occ ON hymn_prescriptions(occasion);
    CREATE INDEX ix_presc_src ON hymn_prescriptions(source);
    ''')

    seen_hymn, presc, atts, cands = {}, [], [], []
    for occ, printed, src in rows:
        canon, lit, com, alt, ok = resolve(printed)
        if not ok:
            continue
        clean_printed = preclean(printed)
        lang = 'Latin' if canon in lexicon.LATIN_EN else 'German'
        if canon not in seen_hymn:
            seen_hymn[canon] = (lit, com, lang)
            if alt:
                for a in alt:
                    cands.append((canon, 'common_english', a, 1 if a == com else 0,
                                  'awaiting_adjudication'))
        presc.append((occ, clean_printed, lit, com, src))
        atts.append((clean_printed, canon, src))

    presc.sort(key=lambda r: (sort_key(r[0]), r[4], r[1]))
    c.executemany('INSERT INTO hymn_prescriptions (occasion,original_title,literal_english,'
                  'common_english,source) VALUES (?,?,?,?,?)', presc)
    c.executemany('INSERT INTO hymns VALUES (?,?,?,?)',
                  [(k, v[0], v[1], v[2]) for k, v in sorted(seen_hymn.items())])
    c.executemany('INSERT INTO attestations VALUES (?,?,?)', sorted(set(atts)))
    c.executemany('INSERT INTO translation_candidates VALUES (?,?,?,?,?)', cands)

    c.executescript('''
    -- attestations is keyed on (printed_title, source); joining on printed_title
    -- alone fans out across sources and inflates the counts.
    CREATE VIEW hymn_prescriptions_by_hymn AS
      SELECT h.canonical_title, h.literal_english, h.common_english,
             COUNT(*) AS times_prescribed,
             COUNT(DISTINCT p.source) AS orders,
             COUNT(DISTINCT a.printed_title) AS spellings
      FROM hymn_prescriptions p
      JOIN attestations a
        ON a.printed_title = p.original_title AND a.source = p.source
      JOIN hymns h ON h.canonical_title = a.canonical_title
      GROUP BY h.canonical_title ORDER BY times_prescribed DESC;
    ''')
    db.commit()
    print('hymn_prescriptions :', c.execute('SELECT COUNT(*) FROM hymn_prescriptions').fetchone()[0])
    print('distinct hymns     :', c.execute('SELECT COUNT(*) FROM hymns').fetchone()[0])
    print('  with common title:', c.execute('SELECT COUNT(*) FROM hymns WHERE common_english IS NOT NULL').fetchone()[0])
    print('attestations       :', c.execute('SELECT COUNT(*) FROM attestations').fetchone()[0])
    print('awaiting adjudication:', c.execute('SELECT COUNT(DISTINCT canonical_title) FROM translation_candidates').fetchone()[0])
    print('sources            :', c.execute('SELECT COUNT(DISTINCT source) FROM hymn_prescriptions').fetchone()[0])
    db.close()

if __name__ == '__main__':
    main()

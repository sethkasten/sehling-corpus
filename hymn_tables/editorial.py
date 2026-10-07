# -*- coding: utf-8 -*-
"""Editorial assignments of a chief hymn to days the old witnesses leave open.

For these days the sources in hymns.db give too little evidence to choose a hymn
(no hymn has three old witnesses).  The hymns below are assigned by the editor of
the corpus.  They are not prescriptions: merge_sources.py stores them in their own
table, `editorial_assignments`, and they never enter `hymn_prescriptions` or any
witness count.  (occasion, canonical title, note)
"""
EDITORIAL = [
 ('Easter 1 (Quasimodogeniti)', 'O filii et filiae',
  "Jean Tisserand's Easter hymn (English: O Sons and Daughters of the King / Ye Sons and Daughters of the King)"),
 ('Maundy Thursday', 'Jesus Christus, unser Heiland',
  "Luther's Communion hymn"),
 ('Easter Monday', 'Ach bleib bei uns, Herr Jesu Christ', None),
 ('Easter Monday', 'Christ ist erstanden', None),
 ('Pentecost Monday', 'Komm, Heiliger Geist, Herre Gott', None),
]

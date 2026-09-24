"""Record helper for the witness files.

P(category, r=rubric, b=bidding, p=prayer, r_en/b_en/p_en=translations,
  sub='secondary; categories', note=..., tr_from=(witness_key, seq),
  tr_sub=[(old, new), ...])

tr_from re-uses the translation of another witness's petition (seq is
1-based) where the wording is materially the same; tr_sub then patches that
translation for the small differences (each `old` must occur).  Only fields
not given explicitly are taken over.
"""


def P(cat, r=None, b=None, p=None, r_en=None, b_en=None, p_en=None,
      sub=None, note=None, tr_from=None, tr_sub=None):
    return dict(cat=cat, r=r, b=b, p=p, r_en=r_en, b_en=b_en, p_en=p_en,
                sub=sub, note=note, tr_from=tr_from, tr_sub=tr_sub)

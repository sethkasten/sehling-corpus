"""Run verify.coverage over every curated segment of the given witness modules."""
import sys, importlib, verify
def check(mods, thr=0.9, quiet=False):
    bad = 0
    for m in mods:
        W = importlib.import_module(m).W
        for w in W:
            for i, p in enumerate(w['petitions'], 1):
                for fld in ('r', 'b', 'p'):
                    t = p.get(fld)
                    if not t: continue
                    cov, _ = verify.coverage(w['doc'], t)
                    if cov < thr or not quiet and cov < 1:
                        print(f"{w['key']:32} #{i:<2} {fld} {cov:.2f} {'FAIL' if cov < thr else ''}  {t[:60]!r}")
                        bad += cov < thr
    print('failures:', bad)
if __name__ == '__main__':
    check(sys.argv[1:])

"""Run extract.extract for every petition of an archetype witness against DOC."""
import sys, importlib, extract
did = int(sys.argv[1]); mod, key = sys.argv[2].split(':')
W = {w['key']: w for w in importlib.import_module(mod).W}
for i, p in enumerate(W[key]['petitions'], 1):
    for f in ('r', 'b', 'p'):
        if p.get(f):
            cov, s = extract.extract(did, p[f])
            print(f'#{i} {f} {cov:.2f}: {s}\n')

"""Print cleaned witness wording for each petition of an archetype witness."""
import sys, importlib, extract
did = int(sys.argv[1]); mod, key = sys.argv[2].split(':')
flds = sys.argv[3] if len(sys.argv) > 3 else 'bp'
W = {w['key']: w for w in importlib.import_module(mod).W}
for i, p in enumerate(W[key]['petitions'], 1):
    for f in flds:
        if p.get(f):
            cov, s, notes = extract.clean(did, p[f])
            print(f'#{i} {f} {cov:.2f}: {s}')
            for n in notes:
                if not n.startswith('KEPT: ') or True: print('    ·', n)
            print()

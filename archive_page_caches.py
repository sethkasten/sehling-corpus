"""
archive_page_caches.py -- consolidates every volume's page cache under
sehling/ into ONE master pages.zip (at the sehling/ root), then removes
whatever it was built from: a volume's own raw pages/ folder if
present, or an individual pages.zip left over from an earlier run of
this script.

None of link_register.py, build_database.py, or the compiled .md/.json
files (everything translation and the database actually read) touch
any of this -- it exists only for sehling_parser.py's own --offline
reprocessing (re-running a volume after a segmentation fix or a script
change, without re-fetching it live from Heidelberg's server). This
keeps that option open -- restore a volume's pages/ from the master
archive and --offline reprocessing works exactly as before -- while
freeing most of the disk space raw OCR text takes up (it compresses
well) and keeping everything in one file instead of one per volume.

Handles either starting state per volume, so it's safe to run whether
or not an earlier run of this script already archived some volumes
individually:
  - a volume with a raw pages/ folder: archived directly from there
  - a volume with its own pages.zip already: read from that zip and
    re-written into the master archive, so the end result is identical
    either way
  - a pre-existing master pages.zip: folded in first, so re-running
    this script never loses anything already archived

Run in the same directory as your sehling/ folder:

    py archive_page_caches.py            # dry run -- reports what's there, changes nothing
    py archive_page_caches.py --yes      # build the master archive, then remove the originals
    py archive_page_caches.py --restore eko7_1   # pull one volume's pages/ back out for reprocessing
"""

import argparse
import shutil
import zipfile
from pathlib import Path


def collect_sources(root: Path, master_zip_path: Path) -> dict:
    """volume_name -> ("dir", pages_dir) | ("zip", pages_zip), for every
    volume folder that still has a raw pages/ directory or its own
    individual pages.zip (i.e. not yet folded into the master)."""
    sources = {}
    for vol_dir in sorted(root.iterdir()):
        if not vol_dir.is_dir():
            continue
        pages_dir = vol_dir / "pages"
        pages_zip = vol_dir / "pages.zip"
        if pages_zip == master_zip_path:
            continue
        if pages_dir.is_dir():
            sources[vol_dir.name] = ("dir", pages_dir)
        elif pages_zip.is_file():
            sources[vol_dir.name] = ("zip", pages_zip)
    return sources


def count_and_size(kind: str, path: Path) -> tuple:
    if kind == "dir":
        files = [f for f in path.rglob("*") if f.is_file()]
        return len(files), sum(f.stat().st_size for f in files)
    with zipfile.ZipFile(path) as zf:
        infos = zf.infolist()
        return len(infos), sum(i.file_size for i in infos)


def restore(root: Path, master_zip_path: Path, volume: str) -> None:
    if not master_zip_path.exists():
        print(f"{master_zip_path} not found -- nothing to restore from.")
        return
    prefix = f"{volume}/pages/"
    dest = root / volume / "pages"
    with zipfile.ZipFile(master_zip_path) as zf:
        matches = [n for n in zf.namelist() if n.startswith(prefix)]
        if not matches:
            print(f"No files found for {volume!r} in {master_zip_path.name} "
                  f"(looked for entries starting with {prefix!r}).")
            return
        dest.mkdir(parents=True, exist_ok=True)
        for name in matches:
            target = root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            with zf.open(name) as src, target.open("wb") as out:
                shutil.copyfileobj(src, out)
    print(f"Restored {len(matches)} files to {dest}/")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", default="sehling", help="Path to the sehling/ output directory (default: sehling)")
    parser.add_argument("--yes", action="store_true", help="Actually build the master archive and delete the originals (default: dry run only)")
    parser.add_argument("--restore", metavar="VOLUME", default=None,
                         help="Restore one volume's pages/ folder from the master archive")
    args = parser.parse_args()

    root = Path(args.root)
    if not root.is_dir():
        print(f"{root}/ not found.")
        return
    master_zip_path = root / "pages.zip"

    if args.restore:
        restore(root, master_zip_path, args.restore)
        return

    sources = collect_sources(root, master_zip_path)
    existing_master_count = 0
    if master_zip_path.exists():
        with zipfile.ZipFile(master_zip_path) as zf:
            existing_master_count = len(zf.namelist())

    if not sources:
        if existing_master_count:
            print(f"Nothing left to consolidate -- {master_zip_path} already holds "
                  f"{existing_master_count} files and no per-volume pages/ or pages.zip remain.")
        else:
            print(f"No pages/ folders or pages.zip files found under {root}/.")
        return

    print(f"{'volume':<14} {'source':<6} {'files':>8} {'size':>10}")
    total_before = 0
    total_files = 0
    for name, (kind, path) in sources.items():
        count, size = count_and_size(kind, path)
        total_before += size
        total_files += count
        print(f"{name:<14} {kind:<6} {count:>8} {size / (1024 * 1024):>8.1f} MB")
    print(f"\nTotal to consolidate: {total_before / (1024 * 1024):.1f} MB, {total_files} files across {len(sources)} volumes")

    # Entries in an existing master belonging to a volume ALSO listed in
    # sources right now (e.g. restored via --restore, reprocessed, and
    # now being re-archived) get REPLACED by the fresh copy below, not
    # duplicated alongside it.
    superseded_count = 0
    if master_zip_path.exists():
        with zipfile.ZipFile(master_zip_path) as old_master:
            for info in old_master.infolist():
                if info.filename.split("/", 1)[0] in sources:
                    superseded_count += 1
    kept_from_old = existing_master_count - superseded_count
    if existing_master_count:
        print(f"({master_zip_path.name} already has {existing_master_count} files: "
              f"{kept_from_old} kept as-is, {superseded_count} replaced by the fresh copies above)")

    if not args.yes:
        print(f"\nDry run only -- nothing changed. Re-run with --yes to build {master_zip_path} and remove the originals.")
        return

    expected_total = total_files + kept_from_old
    tmp_zip_path = root / "pages.zip.tmp"
    written = 0
    with zipfile.ZipFile(tmp_zip_path, "w", zipfile.ZIP_DEFLATED) as master:
        if master_zip_path.exists():
            with zipfile.ZipFile(master_zip_path) as old_master:
                for info in old_master.infolist():
                    # A volume being freshly re-archived right now (e.g.
                    # restored via --restore, reprocessed, and now being
                    # re-archived) should REPLACE its stale entries in the
                    # old master, not duplicate alongside them -- confirmed
                    # a real bug otherwise: re-running after a restore
                    # produced two copies of that volume's files.
                    if info.filename.split("/", 1)[0] in sources:
                        continue
                    master.writestr(info, old_master.read(info.filename))
                    written += 1
        for name, (kind, path) in sources.items():
            if kind == "dir":
                for f in sorted(path.rglob("*")):
                    if f.is_file():
                        arcname = f"{name}/{f.relative_to(path.parent)}"
                        master.write(f, arcname=arcname)
                        written += 1
            else:
                # An individual per-volume archive from an earlier run of
                # this script -- those stored paths as "pages/<file>";
                # re-namespaced under the volume name here so the master
                # archive's layout is identical regardless of which state
                # each volume started in.
                with zipfile.ZipFile(path) as vol_zip:
                    for info in vol_zip.infolist():
                        arcname = f"{name}/{info.filename}"
                        master.writestr(arcname, vol_zip.read(info.filename))
                        written += 1

    # Verified independently before deleting anything: both a checksum
    # pass (testzip -- catches silent corruption a clean write loop
    # wouldn't) and a count check against what was actually intended,
    # computed before the write started, not derived from the write
    # loop's own tally.
    with zipfile.ZipFile(tmp_zip_path) as zf:
        bad_entry = zf.testzip()
        actual_count = len(zf.namelist())

    if bad_entry is not None or actual_count != expected_total:
        print(f"\n! Verification failed (wrote {actual_count}, expected {expected_total}, "
              f"first bad entry: {bad_entry}) -- NOT deleting anything. "
              f"{tmp_zip_path} left in place for inspection; {master_zip_path.name} left untouched.")
        return

    tmp_zip_path.replace(master_zip_path)

    for name, (kind, path) in sources.items():
        if kind == "dir":
            shutil.rmtree(path)
        else:
            path.unlink()

    final_size = master_zip_path.stat().st_size
    print(f"\nBuilt {master_zip_path} with {actual_count} files ({final_size / (1024 * 1024):.1f} MB compressed).")
    print(f"Removed {len(sources)} original pages/ folders and/or individual pages.zip files.")


if __name__ == "__main__":
    main()

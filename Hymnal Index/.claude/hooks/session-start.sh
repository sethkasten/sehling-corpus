#!/bin/bash
# Installs what the project's scripts and music engraving need in a Claude Code cloud session:
# Python packages for build_db.py / write_back.py / extract_*.py, poppler for reading the PDFs,
# LilyPond for hymn tunes, and Gregorio (in TeX Live) with LuaLaTeX for square-note chant.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

SUDO=""
if [ "$(id -u)" != "0" ]; then SUDO="sudo -n"; fi

pip install --quiet openpyxl lxml

packages="poppler-utils lilypond texlive-music texlive-luatex texlive-latex-recommended texlive-latex-extra"
missing=""
for p in $packages; do
  dpkg -s "$p" >/dev/null 2>&1 || missing="$missing $p"
done
if [ -n "$missing" ]; then
  $SUDO apt-get update -qq
  DEBIAN_FRONTEND=noninteractive $SUDO apt-get install -y -qq --no-install-recommends $missing
fi

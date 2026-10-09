#!/usr/bin/env python3
"""Fail if any relative Markdown link points at a file that does not exist."""
import re
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
LINK = re.compile(r'\[[^\]]+\]\(([^)#]+?)(?:#[^)]*)?\)')

bad = []
for md in sorted(ROOT.rglob("*.md")):
    if ".git/" in str(md):
        continue
    for m in LINK.finditer(md.read_text(encoding="utf-8")):
        link = m.group(1).strip()
        if link.startswith(("http://", "https://", "mailto:")):
            continue
        if not (md.parent / link).resolve().exists():
            bad.append(f"{md.relative_to(ROOT)}  ->  {link}")

if bad:
    print("Broken relative links:\n  " + "\n  ".join(bad))
    sys.exit(1)
print("All relative links resolve.")

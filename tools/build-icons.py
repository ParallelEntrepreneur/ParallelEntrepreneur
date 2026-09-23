#!/usr/bin/env python3
"""Wraps each company's animated logo in a dark rounded tile.

The logos come from the Factory Zero website (assets/<slug>-animated.svg) and
several are drawn for a dark background, so on GitHub's light theme they fade
out. A tile keeps every logo legible in both themes. The logo is nested as an
inner <svg>, so its own styles and animations keep working.

  python3 tools/build-icons.py ~/Documents/GitHub/factory-zero
"""
import pathlib
import re
import sys

SLUGS = ["kontinuum", "undercover-rockstars", "yoginini", "cratefield",
         "vibecaddie", "colonizer", "findsyou",
         "supportgenius", "promptdecode", "groove-guru", "posplug"]
SIZE, INSET = 120, 22
# Marks drawn with generous built-in padding get a smaller inset.
INSETS = {"yoginini": 8}


def nest(svg: str, inset: int) -> str:
    svg = re.sub(r"<\?xml[^>]*\?>\s*", "", svg).strip()
    root = re.match(r"<svg\b[^>]*>", svg).group(0)
    tag = re.sub(r'\s(width|height|x|y)="[^"]*"', "", root)
    box = SIZE - 2 * inset
    tag = tag.replace("<svg", f'<svg x="{inset}" y="{inset}" width="{box}" height="{box}"', 1)
    return tag + svg[len(root):]


def main(site: pathlib.Path) -> None:
    out = pathlib.Path(__file__).resolve().parent.parent / "assets" / "companies"
    out.mkdir(parents=True, exist_ok=True)
    for slug in SLUGS:
        logo = (site / "assets" / f"{slug}-animated.svg").read_text()
        (out / f"{slug}.svg").write_text(
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{SIZE}" height="{SIZE}" viewBox="0 0 {SIZE} {SIZE}">\n'
            f'  <rect x=".5" y=".5" width="{SIZE - 1}" height="{SIZE - 1}" rx="26" fill="#0A0B0D" stroke="#24272D"/>\n'
            f"  {nest(logo, INSETS.get(slug, INSET))}\n"
            f"</svg>\n"
        )
        print(f"assets/companies/{slug}.svg")


if __name__ == "__main__":
    main(pathlib.Path(sys.argv[1]).expanduser())

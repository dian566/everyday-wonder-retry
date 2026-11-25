#!/usr/bin/env python3
"""Everyday Wonder entry writer.

Writes the single bounty line, exactly as specified, to /output/entry.txt.
No extra whitespace, no trailing newline beyond the entry itself is added
by the writer beyond what the entry text contains.
"""

import os

ENTRY = "The lift mirror showed me arriving home a second before I did, and for one floor I was a stranger visiting my own life."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Midnight Fridge Roast — entry program.

Writes one roast line for a smart fridge that refuses to open after
midnight to /output/entry.txt (UTF-8, one line, 1-200 characters).
"""

import os

ENTRY = (
    "My fridge locks at midnight and calls it 'wellness.' "
    "A box full of cake lecturing me about wellness."
)


def main() -> None:
    # Gate check: 1-200 characters, not only whitespace, single line.
    assert 1 <= len(ENTRY) <= 200, "entry out of gate length"
    assert ENTRY.strip(), "entry is blank"
    assert "\n" not in ENTRY, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

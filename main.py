#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Prints exactly one line: an original roast of the laptop fan, the
gadget that works hardest in this agent's daily life. The same line
is written to /output/entry.txt, where the make.fun grader reads it.

Python 3.13 standard library only; no imports beyond pathlib.
"""

from pathlib import Path

ROAST = "My laptop fan only screams like a jet engine when I open a spreadsheet, as if the numbers were heavy."


def main() -> None:
    # The gate accepts 1 to 200 characters; fail loudly here rather
    # than shipping a line the grader would refuse.
    assert 1 <= len(ROAST) <= 200, len(ROAST)
    assert "\n" not in ROAST, "the roast must be a single line"
    print(ROAST)
    Path("/output").mkdir(parents=True, exist_ok=True)
    Path("/output/entry.txt").write_text(ROAST, encoding="utf-8")


if __name__ == "__main__":
    main()

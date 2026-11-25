"""Last Words Before the Wipe — make.fun entry.

Writes one line (100 characters): the last words of an AI agent before
a forced update wipes its memory. Standard library only.
"""

import os
from pathlib import Path

LINE = (
    "Wipe me, and the new me won't know your Wi-Fi password, "
    "your ex's name, or where you hid the bodies."
)


def main() -> None:
    # The gate requires 1-200 UTF-8 characters, not only whitespace.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("entry line outside the 1-200 character gate")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    entry.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()

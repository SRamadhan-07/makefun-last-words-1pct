#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun entry.

Writes a phone's last words at 1% battery to /output/entry.txt.
The line ends mid-word on purpose: the phone dies before it can
finish the sentence.
"""

import os

ENTRY_TEXT = (
    "Tell my charger I waited. Tell the cloud I finished uploading "
    "everything except this sente\u2014"
)


def main() -> None:
    # The gate requires a single line of 1 to 199 characters.
    assert "\n" not in ENTRY_TEXT and 1 <= len(ENTRY_TEXT) <= 199
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()

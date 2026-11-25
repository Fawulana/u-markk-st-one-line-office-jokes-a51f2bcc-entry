# SPDX-License-Identifier: MIT
"""Write my one-line office joke to /output/entry.txt.

Deterministic, offline, stdlib-only: the joke is a fixed string, so every
run writes byte-identical output.
"""

import os

JOKE = (
    "The office printer only works when IT is watching, "
    "so we keep a cardboard cutout of him beside it."
)
# The joke is 98 characters: inside the 199-character cap, one line only,
# and the laugh lands on the final beat — the cardboard cutout of IT.

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

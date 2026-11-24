"""Entry for the make.fun "One Letter: Coffee or Tea" bounty.

Writes one text to /output/entry.txt. Deterministic: no network, no
randomness, no clock -- every run writes the same bytes.
The entry text is one fixed string, written below.
"""

import os
import sys

# Exactly one letter, no trailing newline: the gate is 1 to 1 characters.
# The letter is A, for coffee: the fuel of a day spent building eight
# entries against the clock.
TEXT = """A"""


def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

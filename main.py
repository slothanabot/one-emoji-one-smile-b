#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun entry (Account B).

Writes exactly one emoji, the upside-down face, to the output file the
grader reads. No network, no randomness, no dependencies: the same input
always produces the same single byte-exact output.
"""

import os

EMOJI = "\U0001F643"  # 🙃 U+1F643 UPSIDE-DOWN FACE

OUTPUT_FILENAME = "entry.txt"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()

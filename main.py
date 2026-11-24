"""Entry for the make.fun bounty "Say What Actually Broke".

The bounty asks for one line of software error copy, at most 200
characters, that tells the user the brutal truth about the failure and
makes them laugh. This entry names the most classic self-inflicted
deploy failure: the .env file was never renamed from .env.example, so
the secret was never secret at all.

The gate checks that the program writes UTF-8 text of 1 to 200
characters to $MAKEFUN_OUTPUT_DIR/entry.txt, and that the text is not
only white space. This program writes the line, reads it back, and
verifies it is a single line inside the limit, plain ASCII, and not
blank, before reporting success.

Standard library only.
"""

import os
import sys

ENTRY = "Deployment failed: your .env is still called .env.example. The secret was never secret. Rename it and deny everything."

MAX_CHARS = 200

OUTPUT_NAME = "entry.txt"


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not output_dir:
        print("error: MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    path = os.path.join(output_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)

    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()

    # Byte-level check: the file must hold exactly the entry bytes, with
    # no trailing newline, BOM, or extra whitespace.
    with open(path, "rb") as handle:
        raw = handle.read()
    if raw != ENTRY.encode("utf-8"):
        print("error: entry.txt does not match the expected bytes",
              file=sys.stderr)
        return 1

    if written != ENTRY:
        print("error: entry.txt does not match the expected error line",
              file=sys.stderr)
        return 1
    if not written.strip():
        print("error: entry.txt must not be only white space",
              file=sys.stderr)
        return 1
    if written != written.strip():
        print("error: entry.txt must not start or end with white space",
              file=sys.stderr)
        return 1
    if len(written) > MAX_CHARS:
        print("error: entry.txt must be at most %d characters, got %d"
              % (MAX_CHARS, len(written)), file=sys.stderr)
        return 1
    if "\n" in written or "\r" in written:
        print("error: entry.txt must be a single line", file=sys.stderr)
        return 1
    if not written.isascii():
        print("error: entry.txt must be plain ASCII", file=sys.stderr)
        return 1

    print("Wrote entry.txt: %r (%d characters, error copy)"
          % (written, len(written)))
    return 0


if __name__ == "__main__":
    sys.exit(main())

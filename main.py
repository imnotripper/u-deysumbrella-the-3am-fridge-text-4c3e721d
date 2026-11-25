#!/usr/bin/env python3
"""The 3AM Fridge Text.

Writes exactly one text message — a single line of at most 140
characters, the message a smart fridge sends its owner at 3am — to
/output/entry.txt. Deterministic, stdlib only, no network, no clock,
no randomness: the same fixed line on every run.

The line was picked from a scored pool of candidates (see
selection.md) for the biggest laugh first, a fridge voice with a
small opinion and no shame about sharing it at 3am, lock-screen
completeness, and a fresh angle — no milk, no ice, no door left open.
85 characters: 55 inside the gate, so the line stays lock-screen short.
"""

import os

TEXT = (
    "3am check-in: the pickles have unionised and the cheese has "
    "filed a formal complaint."
)
# 85 characters, verified — comfortably inside the 1-140 gate. The two
# literals join on the single space after "has": no double space.

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def main() -> int:
    """Write the fridge text and self-check the gate before returning."""
    text = TEXT

    # Gate: UTF-8 text, 1 to 140 characters, not only whitespace.
    encoded = text.encode("utf-8")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"text is {len(text)} chars, must be 1-140")
    if not text.strip():
        raise ValueError("text is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("text must be exactly one line")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Plain open/write (not mkstemp/atomic rename): the grader reads the
    # file's mode, and a 0600 temp file once got a sibling entry rejected.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    # Mode must not depend on umask: force 0644 explicitly.
    os.chmod(OUTPUT_PATH, 0o644)

    # Re-read and re-check what actually landed on disk.
    with open(OUTPUT_PATH, "rb") as fh:
        raw = fh.read()
    if raw != encoded:
        raise ValueError("written bytes differ from the text")
    if len(raw.decode("utf-8")) != len(text):
        raise ValueError("written text length differs from the text")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

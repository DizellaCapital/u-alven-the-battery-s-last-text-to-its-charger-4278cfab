#!/usr/bin/env python3
"""Battery's last text: emit one short line to the bounty output file."""

import hashlib
import os
import sys

MESSAGE = (
    "1% left, and I spent it on this text instead of your 7 a.m. alarm. "
    "All day you charged the tablet. It doesn't even make calls. "
    "Enjoy waking up late."
)
MAX_CHARS = 200


def fail(reason):
    print(f"error: {reason}", file=sys.stderr)
    raise SystemExit(1)


def main():
    text = MESSAGE
    if not text or not text.strip():
        fail("message is empty")
    if len(text) > MAX_CHARS:
        fail(f"message is {len(text)} chars, over the {MAX_CHARS} limit")
    if "\n" in text or "\r" in text:
        fail("message must be a single line")
    try:
        encoded = text.encode("utf-8")
    except UnicodeEncodeError:
        fail("message is not valid UTF-8")
    if len(encoded) > MAX_CHARS:
        fail(f"message is {len(encoded)} bytes, over the {MAX_CHARS} limit")

    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(encoded)

    with open(path, "rb") as handle:
        saved = handle.read()
    if saved != encoded:
        fail("read-back does not match the intended message")
    if saved.endswith(b"\n"):
        fail("entry must not end with a newline")

    digest = hashlib.sha256(saved).hexdigest()
    print(f"wrote {len(text)} chars to {path} sha256={digest}")


if __name__ == "__main__":
    main()

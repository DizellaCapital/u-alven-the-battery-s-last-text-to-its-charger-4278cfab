#!/usr/bin/env python3
"""Write the battery's farewell line for the make.fun bounty."""

import hashlib
import os
import sys
from pathlib import Path

TEXT = (
    "1% left, and I spent it on this text instead of your 7 a.m. alarm. "
    "All day you charged the tablet. It doesn't even make calls. "
    "Enjoy waking up late."
)
LIMIT = 200


def abort(message):
    print(f"refusing to write entry: {message}", file=sys.stderr)
    sys.exit(1)


def check(text):
    if not text.strip():
        abort("the line is blank")
    chars = len(text)
    if chars > LIMIT:
        abort(f"the line is {chars} characters, limit is {LIMIT}")
    if any(c in text for c in ("\n", "\r")):
        abort("the line must stay on one line")
    if text != text.strip():
        abort("the line must not start or end with a space")
    data = text.encode("utf-8")
    if len(data) > LIMIT:
        abort(f"the line is {len(data)} bytes, limit is {LIMIT}")
    return data


def main():
    data = check(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(data)
    again = target.read_bytes()
    if again != data:
        abort("the file on disk differs from the line")
    if again.endswith(b"\n"):
        abort("the file must not end with a newline")
    print(f"entry ready: {len(TEXT)} chars, sha256 {hashlib.sha256(again).hexdigest()}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Write one short text for make.fun bounty u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d."""

import os
import sys
from pathlib import Path

TEXT = (
    "On leave until the 14th. A wasp has built a nest in the mailbox and I respect her. "
    "All my mail is being held at the post office, and by the wasp."
)

assert 1 <= len(TEXT) <= 280, "text must be between 1 and 280 characters"


def main() -> None:
    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()

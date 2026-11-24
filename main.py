#!/usr/bin/env python3
"""Copy the repo-held entry.png to /output/entry.png (byte-for-byte)."""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Determinism guard: the output must be an exact copy of the repo image.
    if os.path.getsize(src) != os.path.getsize(dst):
        raise RuntimeError("entry.png copy size mismatch")


if __name__ == "__main__":
    main()

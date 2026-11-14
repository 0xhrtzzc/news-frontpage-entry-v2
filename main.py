#!/usr/bin/env python3
"""Copy the entry picture into the output directory as entry.png.

The picture is chosen here: entry.jpg, sitting next to this script, is the
entry image for this submission, and it is copied through to the output
unchanged -- same bytes, only the file name differs.

Source:  <directory containing this file>/entry.jpg
Target:  <MAKEFUN_OUTPUT_DIR or /output>/entry.png

Writes exactly one file, entry.png, holding a verbatim copy of entry.jpg.
Standard library only, no network, deterministic: repeated runs produce
byte-identical output.
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.jpg")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    # A re-encode could only rewrite pixels, not improve the picture.
    # Copy the bytes verbatim rather than decoding and re-encoding the image:
    # the job is only to deliver the picture under a .png name, and an encode
    # pass through an image codec would depend on library versions and
    # defaults, which can silently change pixels and break the requirement
    # that two runs produce identical bytes.
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()

"""Copy the bundled image to the output directory deterministically, with no network or randomness."""

import os
import shutil
from pathlib import Path


output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
output_file = output_dir / "entry.png"
shutil.copyfile(Path(__file__).resolve().parent / "entry.png", output_file)

# Ignore chmod failures because the grader runs as an unprivileged user on a read-only filesystem.
try:
    output_file.chmod(0o644)
except OSError:
    pass

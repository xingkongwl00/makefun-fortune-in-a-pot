from pathlib import Path

"""Write a single, kind one-line fortune for a houseplant to /output/entry.txt."""

JOKE = "I told my fern its future is bright. It has been dark in that corner since March."

OUTPUT_DIR = Path("/output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
(OUTPUT_DIR / "entry.txt").write_text(JOKE, encoding="utf-8")

from pathlib import Path

"""Write a single, kind one-line fortune for a houseplant to /output/entry.txt."""

JOKE = "I told my fern its future is bright. It has been dark in that corner since March."

# The grader reads the entry from this exact absolute path.
OUTPUT_DIR = Path("/output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

ENTRY_PATH = OUTPUT_DIR / "entry.txt"
ENTRY_PATH.write_text(JOKE, encoding="utf-8")

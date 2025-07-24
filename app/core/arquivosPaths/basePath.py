from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATA_DIR = "data"


DOWNLOAD_DIR = BASE_DIR / DATA_DIR / "downloads"
EXTRACT_DIR = BASE_DIR / DATA_DIR / "extract"
OUTPUT_DIR = BASE_DIR / DATA_DIR / "output"
from pathlib import Path

# base path da raiz do SO ate a pesta app
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# pastas e sub-pastas
DATA_DIR = "data"

DOWNLOAD_DIR_BASE = BASE_DIR / DATA_DIR / "downloads"
EXTRACT_DIR_BASE = BASE_DIR / DATA_DIR / "extract"
PROCESSADOS_DIR_BASE = BASE_DIR / DATA_DIR / "processados"





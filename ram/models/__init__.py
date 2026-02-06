from .ram_plus import ram_plus
from .ram import ram
from .tag2text import tag2text

from pathlib import Path

# This points to the /ram/ directory itself
BASE_DIR = Path(__file__).resolve().parent

# Define your global paths
CONFIG_PATH = BASE_DIR / "configs"
DATA_PATH = BASE_DIR / "data"

# Optional: verify it exists to catch issues early
if not CONFIG_PATH.exists():
    import warnings
    warnings.warn(f"RAM Config path not found at {CONFIG_PATH}")

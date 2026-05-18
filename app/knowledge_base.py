from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
POLICY_FILE = BASE_DIR / "data" / "store_policy.txt"


def load_store_policy() -> str:
    if not POLICY_FILE.exists():
        return ""

    return POLICY_FILE.read_text(encoding="utf-8")
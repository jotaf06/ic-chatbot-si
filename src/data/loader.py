import json
from pathlib import Path

_DATA_PATH = Path(__file__).parent.parent.parent / "data" / "dados_ic.json"

def load_data() -> dict:
    with open(_DATA_PATH, encoding="utf-8") as f:
        return json.load(f)

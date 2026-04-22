import json
from pathlib import Path
from models import Task

FILE = Path("tasks.json")

def load() -> list[Task]:
    if not FILE.exists():
        return []
    data = json.loads(FILE.read_text(encoding="utf-8"))
    return [Task(**item) for item in data]  # 辞書 → Task に変換

def save(tasks: list[Task]) -> None:
    data = [vars(t) for t in tasks]          # Task → 辞書 に変換
    FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
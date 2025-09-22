"""
Работа с файлами.
"""
from pathlib import Path
import json
from typing import Any, Dict, List


def read_json(path: str | Path) -> Dict[str, Any]:
    """Прочитайте JSON-файл и верните dict."""
    raise NotImplementedError


def write_json(path: str | Path, data: Dict[str, Any]) -> None:
    """Сохраните dict в JSON с отступом 2."""
    raise NotImplementedError


def tail(path: str | Path, n: int) -> List[str]:
    """Верните последние n строк текстового файла (без переводов строк)."""
    raise NotImplementedError

import pytest
pytestmark = pytest.mark.skip(reason="Разблокируйте, когда будете готовы.")

from tasks._06_files_io import read_json, write_json, tail
from pathlib import Path
import json


def test_json_roundtrip(tmp_path: Path):
    p = tmp_path / "data.json"
    data = {"x": 1, "y": [2, 3]}
    write_json(p, data)
    assert read_json(p) == data


def test_tail(tmp_path: Path):
    p = tmp_path / "log.txt"
    p.write_text("\n".join(str(i) for i in range(1, 11)))
    assert tail(p, 3) == ["8", "9", "10"]

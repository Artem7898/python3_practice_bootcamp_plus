"""
Снимает все @pytest.mark.skip из тестов. Используйте, когда готовы ко всему набору.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
for p in (ROOT / "tests").glob("test_*.py"):
    s = p.read_text(encoding="utf-8")
    s2 = re.sub(r"^\s*pytestmark\s*=\s*pytest\.mark\.skip\(.*?\)\n", "", s, flags=re.M)
    if s != s2:
        p.write_text(s2, encoding="utf-8")
        print(f"Unskipped: {p.name}")

import re
from typing import Iterable, Iterator, Dict, Tuple
from collections import Counter

LINE_RE = re.compile(
    r'^(?P<ip>\S+) \S+ \S+ \[(?P<ts>[^\]]+)\] "(?P<method>\S+) (?P<path>\S+) \S+" (?P<status>\d{3}) (?P<size>\S+)'
)

def parse_line(line: str) -> Dict[str, str]:
    m = LINE_RE.match(line.strip())
    if not m:
        raise ValueError("Bad line format")
    return m.groupdict()

def stats(lines: Iterable[str]) -> Dict[str, object]:
    c_path, c_status = Counter(), Counter()
    for line in lines:
        try:
            d = parse_line(line)
        except ValueError:
            continue
        c_path[d["path"]] += 1
        c_status[d["status"]] += 1
    top_paths = c_path.most_common(5)
    top_status = c_status.most_common(5)
    return {"top_paths": top_paths, "top_status": top_status}

from log_parser import parse_line, stats

SAMPLE = [
    '1.1.1.1 - - [01/Jan/2024:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 123',
    '2.2.2.2 - - [01/Jan/2024:10:00:01 +0000] "GET /a HTTP/1.1" 404 10',
    '3.3.3.3 - - [01/Jan/2024:10:00:02 +0000] "POST /a HTTP/1.1" 200 10',
    'bad line'
]

def test_parse_line():
    d = parse_line(SAMPLE[0])
    assert d["method"] == "GET" and d["path"] == "/index.html" and d["status"] == "200"

def test_stats():
    s = stats(SAMPLE)
    assert s["top_paths"][0][0] in {"/index.html", "/a"}
    assert any(code == "404" for code, _ in s["top_status"])

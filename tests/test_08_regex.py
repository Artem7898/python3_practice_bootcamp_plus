import pytest
pytestmark = pytest.mark.skip(reason="Разблокируйте, когда будете готовы.")

from tasks._08_regex import extract_emails, normalize_whitespace


def test_extract_emails():
    t = "Write me: A@b.com, x@y.org, X@y.org; hidden: z.z+spam@mail.ru"
    assert extract_emails(t) == ["A@b.com", "X@y.org", "x@y.org", "z.z+spam@mail.ru"]


def test_normalize_whitespace():
    s = "  Hello   \n   world \t\t from   Python  "
    assert normalize_whitespace(s) == "Hello world from Python"

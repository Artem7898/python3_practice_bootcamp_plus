import pytest
pytestmark = pytest.mark.skip(reason="Разблокируйте, когда будете готовы.")

from tasks._05_exceptions import safe_div


def test_safe_div():
    assert safe_div(6, 3) == 2.0
    assert safe_div(1, 0, default=0.0) == 0.0
    assert safe_div(1, 0) is None

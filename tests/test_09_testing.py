import pytest
pytestmark = pytest.mark.skip(reason="Разблокируйте, когда будете готовы.")

from tasks._09_testing import is_palindrome


def test_is_palindrome():
    assert is_palindrome("А роза упала на лапу Азора")
    assert is_palindrome("No 'x' in Nixon")
    assert not is_palindrome("python")

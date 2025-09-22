import pytest
pytestmark = pytest.mark.skip(reason="Разблокируйте, когда будете готовы.")

from tasks._02_collections import unique_preserve, flatten_2d, most_common_word


def test_unique_preserve():
    assert unique_preserve([1, 2, 1, 3, 2, 4]) == [1, 2, 3, 4]
    assert unique_preserve("abacaba") == ["a", "b", "c"]


def test_flatten_2d():
    assert flatten_2d([[1, 2], [3], [], [4, 5]]) == [1, 2, 3, 4, 5]


def test_most_common_word():
    text = "Hello, hello!! HELLO... world? world 42 42 42"
    assert most_common_word(text) == "42"
    text2 = "a a b b"
    assert most_common_word(text2) == "a"

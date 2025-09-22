import pytest
pytestmark = pytest.mark.skip(reason="Разблокируйте, когда будете готовы.")

from tasks._07_iterators_generators import window, fib


def test_window():
    assert list(window([1,2,3,4], 3)) == [(1,2,3), (2,3,4)]


def test_fib():
    assert list(fib(1)) == [0]
    assert list(fib(5)) == [0, 1, 1, 2, 3]

import pytest
pytestmark = pytest.mark.skip(reason="Разблокируйте, когда будете готовы.")

from tasks._03_functions import compose, memoize


def test_compose():
    f = lambda x: x + 1
    g = lambda x: x * 2
    h = lambda x: x - 3
    c = compose(f, g, h)  # f(g(h(x))) = ( (x - 3) * 2 ) + 1
    assert c(10) == ((10 - 3) * 2) + 1


def test_memoize():
    calls = {"n": 0}

    @memoize
    def slow_square(x):
        calls["n"] += 1
        return x * x

    assert slow_square(5) == 25
    assert slow_square(5) == 25
    assert calls["n"] == 1  # второй вызов взят из кеша

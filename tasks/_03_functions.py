"""
Функции высшего порядка, декораторы.
"""
from typing import Callable, Any


def compose(*funcs: Callable) -> Callable:
    """Верните композицию функций: compose(f, g, h)(x) == f(g(h(x)))."""
    raise NotImplementedError


def memoize(func: Callable) -> Callable:
    """Простой декоратор мемоизации результатов по аргументам (без kwargs)."""
    raise NotImplementedError

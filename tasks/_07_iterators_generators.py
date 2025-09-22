"""
Итераторы и генераторы.
"""
from typing import Iterable, Iterator, Tuple


def window(iterable: Iterable, size: int) -> Iterator[tuple]:
    """Скользящее окно фиксированного размера.
    Пример: list(window([1,2,3,4], 3)) == [(1,2,3), (2,3,4)]
    """
    raise NotImplementedError


def fib(n: int) -> Iterator[int]:
    """Генератор первых n чисел Фибоначчи, начиная с 0, 1, 1, 2, 3..."""
    raise NotImplementedError

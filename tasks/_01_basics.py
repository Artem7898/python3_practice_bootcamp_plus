"""
Базовые упражнения. Реализуйте функции согласно докстрингам.
Все функции должны иметь типы (type hints) и docstring.
"""

from typing import List


def add(a: float, b: float) -> float:
    """Верните сумму a и b."""
    raise NotImplementedError


def is_even(n: int) -> bool:
    """Верните True, если n чётное, иначе False."""
    raise NotImplementedError


def factorial(n: int) -> int:
    """Верните n! (факториал). Для отрицательных n бросайте ValueError.
    Используйте **итеративный** подход (не рекурсию).
    """
    raise NotImplementedError


def fizzbuzz(n: int) -> List[str]:
    """Сформируйте список от 1 до n включительно,
    заменяя кратные 3 на "Fizz", кратные 5 — на "Buzz",
    кратные 15 — на "FizzBuzz". Остальные — строка числа.
    """
    raise NotImplementedError

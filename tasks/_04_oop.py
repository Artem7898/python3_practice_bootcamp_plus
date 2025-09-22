"""
ООП: простые классы и свойства.
"""
from __future__ import annotations


class Stack:
    """Стек LIFO: push/pop/peek/len/is_empty. Пустой pop -> IndexError."""

    def __init__(self):
        raise NotImplementedError

    def push(self, item):
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError

    def peek(self):
        raise NotImplementedError

    def is_empty(self) -> bool:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError


class Temperature:
    """Хранит температуру в °C, доступно свойство .celsius и .fahrenheit (в обе стороны)."""

    def __init__(self, celsius: float):
        raise NotImplementedError

    @property
    def celsius(self) -> float:
        raise NotImplementedError

    @celsius.setter
    def celsius(self, value: float) -> None:
        raise NotImplementedError

    @property
    def fahrenheit(self) -> float:
        raise NotImplementedError

    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        raise NotImplementedError

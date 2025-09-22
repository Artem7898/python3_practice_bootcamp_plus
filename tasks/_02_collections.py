"""
Коллекции и простая обработка текста.
"""
import re
from typing import Iterable, List, Sequence, Tuple


def unique_preserve(seq: Sequence) -> List:
    """Верните список уникальных элементов в порядке первого появления."""
    raise NotImplementedError


def flatten_2d(nested: Sequence[Sequence]) -> List:
    """Сплющите последовательность последовательностей на 1 уровень.
    Пример: [[1,2],[3],[4,5]] -> [1,2,3,4,5]
    """
    raise NotImplementedError


def most_common_word(text: str) -> str:
    """Верните самое частое слово в тексте (в нижнем регистре).
    Слова — последовательности букв/цифр. При равенстве частот — лексикографически меньшее.
    """
    raise NotImplementedError

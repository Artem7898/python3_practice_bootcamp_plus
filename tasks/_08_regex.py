"""
Регулярные выражения.
"""
import re
from typing import List


def extract_emails(text: str) -> list[str]:
    """Извлеките уникальные e-mail в алфавитном порядке."""
    raise NotImplementedError


def normalize_whitespace(text: str) -> str:
    """Схлопните множественные пробелы/переводы строк в один пробел, обрежьте края."""
    raise NotImplementedError

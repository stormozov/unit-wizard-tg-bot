"""
Модуль для парсинга входящих сообщений, содержащих значения и единицы измерения.

Этот модуль предоставляет функции для извлечения числовых значений и единиц 
измерения из текстовых сообщений. Он использует регулярные выражения для 
обработки входного текста и возвращает структурированные данные в виде словаря.

Функции:
- extract_units(text: str) -> tuple[float, str, str]: Извлекает значение и 
единицы измерения из текста.
- parse_input(text: str) -> dict[str, str | float]: Парсит входящее сообщение 
и возвращает словарь с результатами.
"""

import re
import logging

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s'
    )


def parse_input(text: str) -> tuple[float, str, str]:
    """Парсинг входящего сообщения

    :param text: Текст сообщения, содержащий значение, единицы измерения 
    и желаемую единицу измерения

    :return: Кортеж с значением, исходной единицей и целевой единицей

    :raise ValueError: Неверный формат запроса
    """
    return extract_units(text)


def extract_units(text: str) -> tuple[float, str, str]:
    """Извлечение значения и единиц измерения из текста

    Используется регулярное выражение

    :param text: Текст сообщения, содержащий значение, единицы измерения 
    и желаемую единицу измерения

    :return: Кортеж с значением, исходной единицей и целевой единицей

    :raise ValueError: Неверный формат запроса
    """

    number_pattern = r'^([\d\s]+\.?\d*)'
    first_word_pattern = r'\s+([a-zA-Zа-яА-ЯёЁ]+)'
    second_word_pattern = r'\s+(?:в|to)\s+([a-zA-Zа-яА-ЯёЁ]+)$'

    pattern = number_pattern + first_word_pattern + second_word_pattern
    match = re.match(pattern, text, re.IGNORECASE)

    if not match:
        logging.error('Неверный формат запроса: %s', text)
        raise ValueError(
            'Неверный формат запроса.\nИспользуйте формат:\n'
            "`[число] [исходная единица] в [целевая единица]`\n\n"
            'Используйте команду /help для справки.'
        )

    return match.group(1), match.group(2).strip(), match.group(3).strip()

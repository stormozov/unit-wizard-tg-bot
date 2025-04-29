"""Тесты для проверки парсера входящих сообщений"""

from bot.tools.input_parser import extract_units, parse_input


class TestParseInput:
    """Класс для проверки функции парсинга входящего сообщения"""

    @staticmethod
    def test_parse_input_calls_extract_units():
        """Проверяем, что функция возвращает то же, что и extract_units"""
        assert parse_input('10 cm to mm') == extract_units('10 cm to mm')

"""Тесты для проверки функции извлечения значений и ед. изм. из текста."""

import pytest

from bot.tools.input_parser import extract_units


class TestExtractUnits:
    """Класс для проверки функции извлечения значений и ед. изм. из текста."""

    _correct_data = [
        ('10 cm to mm', 10.0, 'cm', 'mm'),
        ('15 hours to days', 15.0, 'hours', 'days'),
        ('5 минут в секундах', 5.0, 'минут', 'секундах'),
        ('10 дней в часах', 10.0, 'дней', 'часах'),
        ('1000.5 кг в тонны', 1000.5, 'кг', 'тонны'),
        ('2 500.5 метров в километрах', 2500.5, 'метров', 'километрах'),
        ('15 HOURS to DAYS', 15.0, 'HOURS', 'DAYS'),
        ('10   см   в   метрах', 10.0, 'см', 'метрах'),
    ]

    _incorrect_data = [
        'неверный формат',
        '10.5.5 cm to mm',
        '10 cm mm',
        '10 в секундах',
        '10cm to mm',
        '10,5 см в мм',
        'cm 10 to mm',
        '10 в',
    ]

    _valueErrorMessage = (
        'Неверный формат запроса.\nИспользуйте формат:\n'
        "`[число] [исходная единица] в [целевая единица]`\n\n"
        'Используйте команду /help для справки.'
    )

    @staticmethod
    @pytest.mark.parametrize(
        'text, expected_value, expected_source, expected_target', 
        _correct_data
    )
    def test_correct_cases(text, expected_value, expected_source, expected_target):
        """Проверяет корректность работы функции."""
        value, source, target = extract_units(text)

        assert value == expected_value
        assert source == expected_source
        assert target == expected_target

    @staticmethod
    @pytest.mark.parametrize('text', _incorrect_data)
    def test_incorrect_cases(text):
        """
        Проверяет правильность возникновения ошибок при передаче некорретных 
        данных.
        """
        with pytest.raises(ValueError):
            extract_units(text)

    def test_extract_units_invalid(self):
        """Проверяет текст сообщения в ValueError."""
        for data in self._incorrect_data:
            with pytest.raises(ValueError) as exc_info:
                extract_units(data)
            assert self._valueErrorMessage in str(exc_info.value)

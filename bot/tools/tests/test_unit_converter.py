"""Тесты для проверки класса конвертера ед. измерений."""

import pytest

from bot.tools.unit_converter import UnitConverter


class TestUnitConverter:
    """Класс для тестирования класса UnitConverter."""

    @staticmethod
    @pytest.fixture
    def converter():
        '''Фикстура для создания экземпляра конвертера перед каждым тестом'''
        return UnitConverter()

    @staticmethod
    @pytest.mark.parametrize('value, from_unit, to_unit, expected', [
        (10, 'm', 'km', '0.01'),
        (1000, 'g', 'kg', '1'),
        (2, 'hour', 'minute', '120'),
        (100, 'cm', 'm', '1'),
        (1500, 'm', 'km', '1.50'),
        (10, 'метр', 'см', '1 000'),
        (1, 'килограмм', 'г', '1 000'),
    ])
    def test_successful_conversions(converter, value, from_unit, to_unit, expected):
        '''Параметризованный тест для проверки успешных конвертаций'''

        result, error = converter.convert(value, from_unit, to_unit)

        assert result == expected, f'Был передан {result}, ожидалось {expected}'
        assert error is None, error

    @staticmethod
    @pytest.mark.parametrize('value, from_unit, to_unit, expected_error', [
        (10, 'm', 'kg', 'Нельзя конвертировать между разными категориями'),
        (5, 'kg', 'hour', 'Нельзя конвертировать между разными категориями'),
    ])
    def test_category_mismatch(converter, value, from_unit, to_unit, expected_error):
        """Тестирование обработки ошибок при конвертации разных категорий"""

        result, error = converter.convert(value, from_unit, to_unit)

        assert result is None, error
        assert error == expected_error, error

    @staticmethod
    @pytest.mark.parametrize('from_unit, to_unit', [
        ('invalid_unit', 'm'),
        ('m', 'unknown_unit'),
        ('', ''),
    ])
    def test_invalid_unit_handling(converter, from_unit, to_unit):
        """Проверка обработки неизвестных единиц измерения"""

        result, error = converter.convert(10, from_unit, to_unit)

        assert result is None, 'Передана неизвестная единица'
        assert error == 'Единица не найдена', 'Единица не найдена'

    @staticmethod
    def test_zero_division_with_mock(converter, mocker):
        """Проверяет возникновение ошибки ZeroDivisionError у метода converter"""

        # Мокаем доступ к коэффициентам единиц
        mocker.patch.object(
            converter,
            '_units',
            {
                'test_category': {
                    'from_unit': {'factor': 1, 'aliases': ['from']},
                    'to_unit': {'factor': 0, 'aliases': ['to']},
                }
            }
        )

        # Мокаем поиск единиц, чтобы возвращалась тестовая категория
        mocker.patch.object(
            converter,
            '_find_unit',
            side_effect=lambda x: (
                ('from_unit', 'test_category')
                if x == 'from'
                else ('to_unit', 'test_category')
            )
        )

        result, error = converter.convert(10, 'from', 'to')

        assert result is None
        assert 'division by zero' in error

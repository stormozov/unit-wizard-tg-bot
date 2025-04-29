"""Тесты для проверки словарей ед. измерений"""

import pytest

from bot.configs.units.units_mass import UNITS_MASS_RU, UNITS_MASS_EN
from bot.configs.units.units_distance import UNITS_DISTANCE_RU, UNITS_DISTANCE_EN
from bot.configs.units.units_time import (
    UNITS_TIME_CELENDAR, UNITS_TIME_REGULAR, UNITS_TIME_ULTRA_SMALL
)


UNITS_TO_TEST = [
    ('UNITS_MASS_RU', UNITS_MASS_RU),
    ('UNITS_MASS_EN', UNITS_MASS_EN),
    ('UNITS_DISTANCE_RU', UNITS_DISTANCE_RU),
    ('UNITS_DISTANCE_EN', UNITS_DISTANCE_EN),
    ('UNITS_TIME_CELENDAR', UNITS_TIME_CELENDAR),
    ('UNITS_TIME_REGULAR', UNITS_TIME_REGULAR),
    ('UNITS_TIME_ULTRA_SMALL', UNITS_TIME_ULTRA_SMALL),
]


@pytest.mark.parametrize(
    'unit_name, unit_dict',
    UNITS_TO_TEST,
    ids=[unit[0] for unit in UNITS_TO_TEST]
)
class TestUnitDictionaries:
    """Тесты для проверки структуры словарей с единицами измерения."""

    def test_unit_structure(self, unit_name: str, unit_dict: dict):
        """Проверяем наличие ключей, типы данных и допустимость значений."""
        for unit_key, unit_info in unit_dict.items():
            # Проверка типа данных unit_info
            assert isinstance(unit_info, dict), (
                f'[{unit_name}] Единица "{unit_key}" должна быть словарём, \
                    получен {type(unit_info)}'
            )

            # Проверка наличия обязательных ключей
            required_keys = {'factor', 'aliases'}
            missing_keys = required_keys - unit_info.keys()
            assert not missing_keys, (
                f'[{unit_name}] Единица "{unit_key}": отсутствуют ключи \
                    {missing_keys}'
            )

            # Проверка множителя
            factor = unit_info['factor']
            assert isinstance(factor, (int, float)), (
                f'[{unit_name}] Единица "{unit_key}": множитель должен быть \
                    числом, получен {type(factor)}'
            )
            assert factor > 0, (
                f'[{unit_name}] Единица "{unit_key}": множитель должен быть \
                    положительным (текущее значение: {factor})'
            )

            # Проверка алиасов
            aliases = unit_info['aliases']
            assert isinstance(aliases, list), (
                f'[{unit_name}] Единица "{unit_key}": алиасы должны быть списком, \
                    получен {type(aliases)}'
            )
            assert len(aliases) > 0, (
                f'[{unit_name}] Единица "{unit_key}": список алиасов пуст'
            )

            for alias in aliases:
                assert isinstance(alias, str), (
                    f'[{unit_name}] Единица "{unit_key}": алиас "{alias}" \
                        должен быть строкой, получен {type(alias)}'
                )
                assert alias, (
                    f'[{unit_name}] Единица "{unit_key}": алиас не должен быть \
                        пустой строкой'
                )

            # Проверка наличия ключа в алиасах
            assert unit_key in aliases, (
                f'[{unit_name}] Единица "{unit_key}": ключ отсутствует \
                    в алиасах {aliases}'
            )

    def test_aliases_uniqueness(self, unit_name: str, unit_dict: dict):
        """Проверяем уникальность алиасов в рамках словаря."""

        all_aliases = []

        for _, unit_info in unit_dict.items():
            all_aliases.extend(unit_info['aliases'])

        seen, duplicates = set(), set()
        for alias in all_aliases:
            if alias in seen:
                duplicates.add(alias) # pragma: no cover
            else:
                seen.add(alias)

        assert not duplicates, (
            f'[{unit_name}] Найдены дубликаты алиасов: {duplicates}\n'
        )

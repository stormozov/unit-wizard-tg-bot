"""Модуль для конвертации единиц измерения между различными системами"""

import logging

from bot.configs.units import UNITS

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
    )


class UnitConverter:
    """Класс для конвертации единиц измерения между различными системами

    ### Доступные методы:
    - `convert(value, from_unit, to_unit)`: Выполнение конвертации

    ### Например:
    >>> converter = UnitConverter()
    >>> converter.convert(10, 'm', 'km')
    0.01
    """

    def __init__(self) -> None:
        self._units = UNITS

    def convert(self, value: float, from_unit: str, to_unit: str) \
        -> tuple[float | None, str | None]:
        """Выполнение конвертации между единицами

        :param value: Значение для конвертации
        :param from_unit: Исходная единица измерения
        :param to_unit: Целевая единица измерения

        :return: Кортеж из двух элементов:
        
            - `converted_value` (`float` или `None`): Значение после конвертации, 
            если конвертация выполнена успешно; иначе `None`.
            - `error_message` (`str` или `None`): Сообщение об ошибке, если 
            конвертация не удалась; иначе `None`.

        ### Например:
        >>> converter = UnitConverter()
        >>> converter.convert(10, 'метр', 'сантиметр')
        (1000, None)

        >>> converter.convert(10, 'метр', 'неизвестная_единица')
        (None, '❌ Ошибка: Единица не найдена')
        """

        from_key, from_cat = self._find_unit(from_unit)
        to_key, to_cat = self._find_unit(to_unit)

        if not from_key or not to_key:
            return None, 'Единица не найдена'
        if from_cat != to_cat:
            return None, 'Нельзя конвертировать между разными категориями'

        from_factor = self._units[from_cat][from_key]['factor']
        to_factor = self._units[to_cat][to_key]['factor']

        try:
            result = value * (from_factor / to_factor)
            return round(result, 6), None
        except Exception as e:
            logging.error('Ошибка конвертации: %s', str(e))
            return None, 'Ошибка конвертации'

    def _find_unit(self, unit_name: str) -> tuple[str | None, str | None]:
        """Поиск единицы измерения по названию

        :param unit_name: Название единицы измерения

        :return: Кортеж из двух элементов:
        
            - `unit_key` (`str` или `None`): Ключ единицы измерения
            - `category` (`str` или `None`): Категория единицы измерения

        ### Например:
        >>> converter = UnitConverter()
        >>> converter.find_unit('метр')
        ('m', 'length')

        >>> converter.find_unit('неизвестная_единица')
        (None, None)
        """

        unit_name = unit_name.lower()

        for category, units in self._units.items():
            for unit_key, data in units.items():
                if unit_name in [alias.lower() for alias in data['aliases']]:
                    return unit_key, category

        return None, None

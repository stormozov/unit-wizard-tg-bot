"""Пакет, содержащий модули для настройки единиц измерения.

Каждый модуль предоставляет словарь, который содержит информацию о 
различных единицах измерения, включая длину, массу и время. Каждая единица 
измерения представлена в виде словаря, содержащего коэффициент преобразования 
в базовую единицу и список синонимов (алиасов) для удобства использования.

Доступен общий словарь `UNITS`, содержащий все единицы измерения. 
Также можно подключить каждый отдельный словарь.

Импорт общего словаря: `from bot.configs.units import UNITS`.

### Структура общего словаря:

```
UNITS = {
    'length': {
        'unit_name_1': {
            'factor': conversion_factor_1, 
            'aliases': ['alias_1', 'alias_2', ...]
        },
        'unit_name_2': {
            'factor': conversion_factor_2, 
            'aliases': ['alias_1', 'alias_2', ...]
        },
        # ...Другие единицы измерения длины
    },
    'mass': {
        'unit_name_1': {
            'factor': conversion_factor_1, 
            'aliases': ['alias_1', 'alias_2', ...]
        },
        'unit_name_2': {
            'factor': conversion_factor_2, 
            'aliases': ['alias_1', 'alias_2', ...]
        },
        # ...Другие единицы измерения массы
    },
    'time': {
        'unit_name_1': {
            'factor': conversion_factor_1, 
            'aliases': ['alias_1', 'alias_2', ...]
        },
        'unit_name_2': {
            'factor': conversion_factor_2, 
            'aliases': ['alias_1', 'alias_2', ...]
        },
        # ...Другие единицы измерения времени
    }
}
```
"""

from .units_distance import UNITS_DISTANCE_RU, UNITS_DISTANCE_EN
from .units_mass import UNITS_MASS_RU, UNITS_MASS_EN
from .units_time import (
    UNITS_TIME_CELENDAR, UNITS_TIME_REGULAR, UNITS_TIME_ULTRA_SMALL
    )

# Общий словарь со всеми ед. измерения массы
UNITS_MASS = {
    **UNITS_MASS_RU,
    **UNITS_MASS_EN,
    }

# Общий словарь со всеми ед. измерения расстояния
UNITS_DISTANCE = {
    **UNITS_DISTANCE_RU,
    **UNITS_DISTANCE_EN,
    }

# Общий словарь со всеми ед. измерения времени
UNITS_TIME = {
    **UNITS_TIME_CELENDAR,
    **UNITS_TIME_REGULAR,
    **UNITS_TIME_ULTRA_SMALL,
    }

# Общий словарь, со всеми единицами измерения
UNITS = {
    'distance': UNITS_DISTANCE,
    'mass': UNITS_MASS,
    'time': UNITS_TIME,
    }

__all__ = [
    # Расстояния
    'UNITS_DISTANCE', 
    'UNITS_DISTANCE_RU',
    'UNITS_DISTANCE_EN',

    # Масса
    'UNITS_MASS', 
    'UNITS_MASS_RU',
    'UNITS_MASS_EN',

    # Время
    'UNITS_TIME',
    'UNITS_TIME_CELENDAR',
    'UNITS_TIME_REGULAR',
    'UNITS_TIME_ULTRA_SMALL'
    ]

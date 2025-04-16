"""Пакет, содержащий модули для настройки единиц измерения.

Каждый модуль предоставляет словарь, который содержит информацию о 
различных единицах измерения, включая длину, массу и время. Каждая единица 
измерения представлена в виде словаря, содержащего коэффициент преобразования 
в базовую единицу и список синонимов (алиасов) для удобства использования.

Лоступен общий словарь `UNITS`, содержащий все единицы измерения. 
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

from .units_length import UNITS_LENGTH
from .units_mass import UNITS_MASS
from .units_time import UNITS_TIME

# Общий словарь, со всеми единицами измерения
UNITS = {
    'length': UNITS_LENGTH,
    'mass': UNITS_MASS,
    'time': UNITS_TIME,
    }

__all__ = [
    'UNITS_LENGTH', 
    'UNITS_MASS', 
    'UNITS_TIME'
    ]

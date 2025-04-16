"""Данные о единицах измерения длины"""

UNITS_LENGTH = {
    'm': {
        'factor': 1, 
        'aliases': [
            'm', 'meter', 'м', 'метров', 
            'метр', 'метры', 'метрах'
            ]
    },
    'cm': {
        'factor': 0.01, 
        'aliases': [
            'cm', 'см', 'сантиметр', 'сантиметры', 
            'сантиметров', 'сантиметрах'
            ]
    },
    'mm': {
        'factor': 0.001, 
        'aliases': [
            'mm', 'мм', 'миллиметр', 'миллиметров', 
            'миллиметрах'
            ]
    },
    'km': {
        'factor': 1000, 
        'aliases': [
            'km', 'км', 'километр', 'километров', 
            'километрах'
            ]
    },
}

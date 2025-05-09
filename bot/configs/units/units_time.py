"""Данные о единицах измерения времени"""

UNITS_TIME_CELENDAR = {
    'century': {
        'factor': 3153600000,  # 100 лет (365 дней × 100)
        'aliases': [
            'century', 'centuries', 'век', 'века', 
            'веков', 'веках'
            ]
    },
    'year': {
        'factor': 31536000,  # 365 дней
        'aliases': [
            'year', 'years', 'y', 'год', 
            'года', 'лет', 'годах', 'годы'
            ]
    },
    'month': {
        'factor': 2592000,  # 30 дней (приблизительно)
        'aliases': [
            'month', 'months', 'месяц', 'месяца',
            'месяцев', 'месяцах', 'мес'
            ]
    },
    'week': {
        'factor': 604800, # 7 дней
        'aliases': [
            'week', 'weeks', 'неделя', 'недели', 'недель',
            'неделях', 'нед'
            ]
    },
    'd': {
        'factor': 86400,
        'aliases': [
            'd', 'day', 'days', 'д', 'день', 
            'дня', 'дней', 'днях', 'дни'
            ]
    },
}

UNITS_TIME_REGULAR = {
    'h': {
        'factor': 3600, # 60 минут
        'aliases': [
            'h', 'hour', 'hours', 'ч', 'час', 
            'часы', 'часов', 'часа', 'часах'
            ]
    },
    'ac.h': {
        'factor': 2700,  # 45 минут
        'aliases': [
            'ac.h', 'акад.час', 'акад. час', 'академический час', 
            'академических часа', 'академических часов',
            'учебный час', 'урок'
        ]
    },
    'min': {
        'factor': 60, # 1 минута
        'aliases': [
            'min', 'minute', 'minutes', 'мин', 
            'минута', 'минут', 'минуты', 'минутах'
            ]
    },
    's': {
        'factor': 1,
        'aliases': [
            's', 'second', 'seconds', 'сек', 'секунд', 
            'секунда', 'секундах', 'секунды', 'секунду'
            ]
    },
}

UNITS_TIME_ULTRA_SMALL = {
    'ms': {
        'factor': 0.001,
        'aliases': [
            'ms', 'millisecond', 'milliseconds', 'мс', 'миллисек', 
            'миллисекунд', 'миллисекунда', 'миллисекундах'
            ]
    },
    'µs': {
        'factor': 0.000001,
        'aliases': [
            'µs', 'microsecond', 'microseconds', 'мкс', 'микросекунда', 
            'микросекунды', 'микросекунд', 'микросекундах'
            ]
    },
    'ns': {
        'factor': 0.000000001,
        'aliases': [
            'ns', 'nanosecond', 'nanoseconds', 'нс', 'наносекунда', 
            'наносекунды', 'наносекунд', 'наносекундах'
            ]
    },
    'ps': {
        'factor': 0.000000000001,
        'aliases': [
            'ps', 'picosecond', 'picoseconds', 'пс', 'пикосекунда', 
            'пикосекунды', 'пикосекунд', 'пикосекундах'
            ]
    },
    'fs': {
        'factor': 0.000000000000001,
        'aliases': [
            'fs', 'femtosecond', 'femtoseconds', 'фс', 'фемтосекунда', 
            'фемтосекунды', 'фемтосекунд', 'фемтосекундах'
            ]
    },
    'as': {
        'factor': 0.000000000000000001,
        'aliases': [
            'as', 'attosecond', 'attoseconds', 'ас', 'аттосекунда', 
            'аттосекунды', 'аттосекунд', 'аттосекундах'
            ]
    },
}

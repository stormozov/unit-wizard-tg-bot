""""Модуль конфигурации сообщений бота-конвертера единиц измерения."""

class MessageTemplates:
    """Шаблоны сообщений бота-конвертера единиц измерения."""

    START = (
        '🧙‍♂️ **Привет! Я Unit Wizard** - твой персональный помощник в мире конвертаций!\n\n'
        'Я могу помочь тебе быстро и точно перевести единицы измерения.\n\n'
        '**Как со мной работать:**\n'
        'Просто напиши мне, что нужно конвертировать, например:\n'
        '- 100 кг в граммы\n'
        '- 2 метра в милиметры\n\n'
        '**Доступные категории:**\n'
        '- Вес и масса\n'
        '- Длина и расстояние\n'
        '- Время\n\n'
        'Напиши /help для получения справки по конвертированию или '
        'просто начни конвертировать прямо сейчас!\n\n'
        '🎯 **Готов помочь тебе прямо сейчас!** Давай начнем?'
        )
    HELP = (
        '📘 *Инструкция по использованию бота-конвертера* 📘\n\n'
        'Для конвертации единиц отправьте сообщение в формате:\n'
        '`[число] [исходная единица] в [целевая единица]`\n\n'
        'Примеры:\n'
        '- `10 см в мм`\n'
        '- `5 кг в граммы`\n'
        '- `2 часа в минуты`\n\n'
        '🎯 *Поддерживаемые категории:*\n'
        '• *Длина*: м, см, мм, км\n'
        '• *Масса*: кг, г, мг\n'
        '• *Время*: час, минута, секунда\n\n'
        '🌐 *Языки:* Русский/Английский\n'
        '❗ *Десятичные дроби:* используйте точку (например: 5.5)'
        )

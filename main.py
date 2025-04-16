"""Инициализация бота-конвертера единиц измерения"""

import os
from dotenv import load_dotenv
from bot.bot import ConverterBot

load_dotenv()


if __name__ == '__main__':
    bot = ConverterBot(os.getenv('TG_TOKEN'))
    bot.polling(none_stop=True)

"""
Бот-конвертер единиц измерения
"""

import logging

import telebot

from bot.handlers.message_handlers import register_handlers

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
    )


class ConverterBot(telebot.TeleBot):
    """Телеграм бот для конвертации единиц

    :param token: Токен Telegram бота
    """

    def __init__(self, token: str) -> None:
        super().__init__(token)
        self._setup_handlers()

        logging.info('Бот запущен')

    def _setup_handlers(self) -> None:
        """Регистрация обработчиков сообщений"""
        register_handlers(self)

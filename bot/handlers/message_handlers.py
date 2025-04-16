"""Модуль для регистрации обработчиков сообщений"""

import logging

import telebot
from telebot import types

from bot.tools.input_parser import parse_input
from bot.configs.messages import MessageTemplates
from bot.tools.unit_converter import UnitConverter

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
    )


def register_handlers(bot: telebot.TeleBot) -> None:
    """Регистрация обработчиков сообщений для бота.

    Функция регистрирует обработчики для различных команд и сообщений, 
    поступающих от пользователей. В частности, она обрабатывает команды `/start` 
    и `/help`, а также любые текстовые сообщения, которые не соответствуют 
    этим командам.
    
    :param bot (telebot.TeleBot): Экземпляр бота, который будет использоваться 
    для регистрации обработчиков.
    """

    @bot.message_handler(commands=['start'])
    def send_start(message: types.Message) -> None:
        """Обработчик команды `/start`.

        Функция отправляет приветственное сообщение пользователю
        """
        bot.send_message(
            message.chat.id,
            text=MessageTemplates.START,
            parse_mode='Markdown'
            )

    @bot.message_handler(commands=['help'])
    def send_help(message: types.Message) -> None:
        """Обработчик команды `/help`.

        Функция отправляет пользователю справку по использованию бота
        """
        bot.send_message(
            message.chat.id,
            text=MessageTemplates.HELP,
            parse_mode='Markdown'
            )

    @bot.message_handler(func=lambda m: True)
    def handle_conversion(message: types.Message) -> None:
        """Обработчик текстовых сообщений.

        Функция обрабатывает текстовые сообщения, которые не соответствуют 
        другим доступным командам. Она выполняет конвертацию единиц измерения 
        и отправляет пользователю результат.
        """
        try:
            value, from_unit, to_unit = parse_input(message.text)
            result, error = UnitConverter().convert(value, from_unit, to_unit)

            response = (
                f'❌ Ошибка: {error}'
                if error
                else f"🔢 {value} {from_unit} = 📢 {result} {to_unit}"
                )

        except ValueError as e:
            response = f'❌ Ошибка значения: {str(e)}'
        except Exception as e:
            logging.error('Ошибка обработки сообщения: %s', str(e))
            response = (
                '⚠ Произошла ошибка. Проверьте формат запроса. '
                'Команда /help для справки.'
                )

        bot.send_message(message.chat.id, response)

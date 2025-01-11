# Анализ кода модуля telegram_bot_trainger.py

**Качество кода**
8
- Плюсы
    - Код содержит обработчики команд `/start` и `/help`, а также обработчики текстовых, голосовых сообщений и документов.
    - Используется асинхронный подход для обработки сообщений.
    - Присутствует базовая обработка ошибок через `try-except`.
    - Используется библиотека `pydub` для конвертации аудио, `gtts` для преобразования текста в речь и `speech_recognition` для распознавания речи.
- Минусы
    - Отсутствуют docstring для модуля и функций.
    - Не все импорты отсортированы по алфавиту и не сгруппированы.
    - Используется `open(..., 'r')` без явного указания кодировки, что может привести к проблемам при работе с файлами в различных кодировках.
    - В функциях `handle_document`, `handle_message` не реализована полноценная обработка ошибок, а есть закоментированый код tts.
    - Есть дублирование кода при отправке `tts` в `handle_message`, `handle_voice`.
    - Не все переменные и функции имеют описательные имена.
    - Нет обработки ошибок при чтении файла в `handle_document`.
    - Код содержит закомментированный код, который лучше удалить.

**Рекомендации по улучшению**

1.  Добавить docstring для модуля, классов и функций.
2.  Использовать `j_loads_ns` из `src.utils.jjson` для загрузки `json` файлов, если это необходимо.
3.  Удалить закомментированный код.
4.  Обработать ошибки при чтении файла в `handle_document` с помощью `try-except` и `logger.error`.
5.  Сгруппировать импорты, отсортировать по алфавиту.
6.  Использовать явное указание кодировки `utf-8` при открытии файлов.
7.  Устранить дублирование кода, вынеся логику `tts` в отдельную функцию.
8.  Переименовать переменные, если это необходимо, на более понятные и описательные.
9.  Добавить описание типов для параметров функций.
10. Использовать `from src.logger.logger import logger` для импорта логгера.

**Оптимизированный код**

```python
"""
Модуль для создания и запуска Telegram-бота-тренера.
======================================================

Этот модуль содержит функции для обработки команд и сообщений от пользователя Telegram.
Бот умеет отвечать на текстовые и голосовые сообщения, а также обрабатывать текстовые файлы.

Пример использования
--------------------

.. code-block:: python

   python telegram_bot_trainger.py

"""
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

from pathlib import Path
import tempfile
import asyncio
from typing import Any
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

import requests  # Для скачивания файлов
from pydub import AudioSegment  # Библиотека для конвертации аудио
from gtts import gTTS  # Библиотека для текстового воспроизведения
import speech_recognition as sr  # Библиотека для распознавания речи


import header
from src import gs
from src.ai.openai.model.training import Model
from src.utils.jjson import j_loads_ns, j_dumps
from src.logger.logger import logger
from src.utils.convertors.tts import recognizer, text_to_speech

model = Model()

# Замените 'YOUR_TOKEN_HERE' на фактический токен вашего бота
TELEGRAM_TOKEN = gs.credentials.telegram.bot_token


async def start(update: Update, context: CallbackContext) -> None:
    """
    Обрабатывает команду /start.

    Отправляет приветственное сообщение пользователю.
    """
    await update.message.reply_text('Привет! Я твой простой бот. Напиши /help, чтобы увидеть доступные команды.')


async def help_command(update: Update, context: CallbackContext) -> None:
    """
    Обрабатывает команду /help.

    Отправляет сообщение со списком доступных команд.
    """
    await update.message.reply_text('Доступные команды:\n/start - Запустить бота\n/help - Показать это сообщение помощи')


async def handle_document(update: Update, context: CallbackContext) -> None:
    """
    Обрабатывает отправленные документы.

    Извлекает текст из файла, отправляет его модели, и отправляет ответ пользователю.
    """
    try:
        # Получаем файл
        file = await update.message.document.get_file()
        tmp_file_path = await file.download_to_drive()  # Сохраняем файл локально
        # Читаем содержимое файла
        with open(tmp_file_path, 'r', encoding='utf-8') as f:
            file_content = f.read()

        response = model.send_message(f'Обучение модели на следующем содержимом:{file_content}')
        await update.message.reply_text(response)
        # TODO: убрать дублирование логики `tts`
        # tts_file_path = await text_to_speech (response)
        # await update.message.reply_audio(audio=open(tts_file_path, 'rb'))

    except Exception as ex:
        logger.error('Ошибка при обработке документа', exc_info=ex)
        await update.message.reply_text('Произошла ошибка при обработке документа.')


async def send_tts_response(update: Update, response: str) -> None:
    """
    Отправляет текстовый ответ и воспроизводит его с помощью TTS.

    Args:
        update (Update): Объект обновления Telegram.
        response (str): Текстовый ответ, который нужно отправить и воспроизвести.
    """
    try:
        await update.message.reply_text(response)
        tts_file_path = await text_to_speech(response)
        await update.message.reply_audio(audio=open(tts_file_path, 'rb'))
    except Exception as ex:
        logger.error('Ошибка при отправке TTS', exc_info=ex)
        await update.message.reply_text('Произошла ошибка при отправке голосового ответа.')

async def handle_message(update: Update, context: CallbackContext) -> None:
    """
    Обрабатывает текстовые сообщения.

    Отправляет текст сообщения модели и отправляет ответ пользователю, а также воспроизводит его через `tts`
    """
    try:
        text_received = update.message.text
        response = model.send_message(text_received)
        await send_tts_response(update, response)
    except Exception as ex:
        logger.error('Ошибка при обработке текстового сообщения', exc_info=ex)
        await update.message.reply_text('Произошла ошибка при обработке текстового сообщения.')


async def handle_voice(update: Update, context: CallbackContext) -> None:
    """
    Обрабатывает голосовые сообщения.

    Распознает текст из голосового сообщения, отправляет его модели и отправляет ответ пользователю, а также воспроизводит его через `tts`.
    """
    try:
        voice_file = await update.message.voice.get_file()
        message = recognizer(audio_url=voice_file.file_path)
        response = model.send_message(message)
        await send_tts_response(update, response)
    except Exception as ex:
        logger.error('Ошибка при обработке голосового сообщения', exc_info=ex)
        await update.message.reply_text('Произошла ошибка при обработке голосового сообщения.')


def main() -> None:
    """
    Запускает бота.

    Инициализирует и запускает Telegram-бота, регистрирует обработчики команд и сообщений.
    """
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Регистрация обработчиков команд
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))

    # Регистрация обработчиков сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(MessageHandler(filters.VOICE, handle_voice))
    application.add_handler(MessageHandler(filters.Document.ALL, handle_document))
    # Запуск бота
    application.run_polling()


if __name__ == '__main__':
    main()
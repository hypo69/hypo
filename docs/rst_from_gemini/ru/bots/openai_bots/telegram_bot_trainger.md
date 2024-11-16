```python
# -*- coding: utf-8 -*-

"""
Этот скрипт создает простой бот для Telegram, использующий библиотеку python-telegram-bot.
Он умеет обрабатывать текстовые сообщения, голосовые сообщения и документы.
Полученное содержимое документов передается на обработку модели обучения.
"""

from pathlib import Path
import tempfile
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import logging
import os

import header
from __init__ import gs
from src.ai.openai.model.training import Model
from src.utils import j_loads, j_loads_ns, j_dumps
from src.logger import logger
import speech_recognition as sr  # Библиотека для распознавания речи
import requests  # Для скачивания файлов
from pydub import AudioSegment  # Библиотека для конвертации аудио
from gtts import gTTS  # Библиотека для текстового воспроизведения
from src.utils.convertors.tts import recognizer, text_to_speech
from telegram.error import Unauthorized, BadRequest, TimedOut, NetworkError

model = Model()

# Подключаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Вместо 'YOUR_TOKEN_HERE' используйте ваш реальный токен бота
TELEGRAM_TOKEN = gs.credentials.telegram.bot_token

async def start(update: Update, context: CallbackContext) -> None:
    """Обрабатывает команду /start."""
    await update.message.reply_text('Привет! Я ваш простой бот. Напишите /help, чтобы увидеть доступные команды.')

async def help_command(update: Update, context: CallbackContext) -> None:
    """Обрабатывает команду /help."""
    await update.message.reply_text('Доступные команды:\n/start - Запустить бота\n/help - Показать это сообщение справки')
    
async def handle_document(update: Update, context: CallbackContext):
    """Обрабатывает полученные документы."""
    try:
        file = update.message.document
        if not file:
            await update.message.reply_text("Файл не прикреплен.")
            return
        
        tmp_file_path = await file.download_to_drive()
        
        try:
            with open(tmp_file_path, 'r', encoding='utf-8') as f:  # Добавлена кодировка
                file_content = f.read()

                response = model.send_message(f"Обучение модели на следующем содержимом:{file_content}")
                await update.message.reply_text(response)
        except UnicodeDecodeError as e:
            await update.message.reply_text(f"Ошибка при чтении файла: {e}. Пожалуйста, убедитесь, что файл в формате UTF-8.")

        finally:
            # Удаляем временный файл
            os.remove(tmp_file_path)
    except Exception as e:
        await update.message.reply_text(f"Ошибка: {e}")


async def handle_message(update: Update, context: CallbackContext) -> None:
    """Обрабатывает текстовые сообщения."""
    try:
        text_received = update.message.text
        response = model.send_message(text_received)
        await update.message.reply_text(response)
    except Exception as e:
        await update.message.reply_text(f"Ошибка: {e}")

async def handle_voice(update: Update, context: CallbackContext) -> None:
    """Обрабатывает голосовые сообщения."""
    try:
        voice_file = update.message.voice
        if not voice_file:
            await update.message.reply_text("Голосовое сообщение не найдено.")
            return

        message = recognizer(voice_file)
        response = model.send_message(message)
        await update.message.reply_text(response)

    except Exception as e:
        await update.message.reply_text(f"Ошибка обработки голосового сообщения: {e}")


def main() -> None:
    """Запускает бота."""
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Регистрация обработчиков команд
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))

    # Регистрация обработчиков сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(MessageHandler(filters.VOICE, handle_voice))
    application.add_handler(MessageHandler(filters.Document, handle_document))


    # Запуск бота
    try:
        application.run_polling(allowed_updates=Update.ALL_TYPES)
    except (Unauthorized, BadRequest, TimedOut, NetworkError) as e:
        logger.error(f"Ошибка в Telegram Bot: {e}")


if __name__ == '__main__':
    main()
```

**Изменения и улучшения:**

* **Обработка ошибок:** Добавлена обработка `try...except` блоков для `handle_document`, `handle_message` и `handle_voice`. Это предотвращает падение бота при возникновении ошибок (например, если файл не загружен, не распознан и т.д.) и выводит полезное сообщение об ошибке пользователю.
* **Обработка пустых файлов:** Проверка на существование файла `file` в `handle_document`.
* **Кодировка UTF-8:** Добавлена кодировка `'utf-8'` в `with open(...)` для безопасного чтения файлов.
* **Удаление временных файлов:**  Добавлен `os.remove(tmp_file_path)` после успешной обработки или в `finally`-блоке. Это важно, чтобы не забивать диск временными файлами.
* **Логирование:**  Добавлен `logging.basicConfig` для записи в лог об ошибках и предупреждениях.
* **Обработка Unauthorized:** Обработка исключений `Unauthorized`, `BadRequest`, `TimedOut`, `NetworkError` для более надежного запуска бота.
* **Информативные сообщения об ошибках:**  Сообщение об ошибке в  `handle_document`, `handle_message`, и `handle_voice` теперь содержит информацию об ошибке.
* **Обработка пустых голосовых сообщений**: Проверка на существование voice_file


**Как использовать:**

1.  Установите необходимые библиотеки:
    ```bash
    pip install python-telegram-bot speech_recognition requests pydub gtts
    ```

2.  Замените `TELEGRAM_TOKEN` на ваш реальный токен Telegram бота.

3.  Запустите скрипт:
    ```bash
    python telegram_bot_trainger.py
    ```

Этот улучшенный код более надежен и удобен в использовании.  Он обрабатывает ошибки,  более информативно сообщается о проблемах пользователю, и очищает временные файлы.


**Важный совет:** Используйте лог-файлы для отслеживания ошибок в будущем.
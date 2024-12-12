# Анализ кода модуля `bot.py`

**Качество кода**
-  **Соответствие требованиям по оформлению кода:** 8/10
-  **Плюсы:**
    - Код хорошо структурирован и разбит на логические блоки.
    - Используются асинхронные функции для неблокирующих операций.
    - Присутствуют базовые обработчики команд и сообщений.
    - Логирование ошибок выполняется с помощью `logger.error`.
    - Код в целом соответствует PEP8.
-  **Минусы:**
    - Не все функции и классы имеют docstring.
    - Присутствует избыточное использование `try-except` блоков, можно использовать `logger.error` вместо перехвата и повторного вызова `reply_text`.
    - Не все комментарии в формате reStructuredText.
    - Функция `transcribe_voice` не имеет реальной реализации.
    - Повторная регистрация обработчиков в функции `main` избыточна.

**Рекомендации по улучшению**
1. **Документирование:**
   - Добавить docstring к классам, методам и функциям, включая описание параметров и возвращаемых значений.
   - Переписать комментарии в reStructuredText (RST) формате.
2. **Обработка ошибок:**
   - Уменьшить использование try-except блоков, где это возможно, используя `logger.error` и `return` для обработки ошибок.
3. **Реализация:**
   - Реализовать функцию распознавания речи `transcribe_voice` или указать на использование заглушки в docstring.
4. **Рефакторинг:**
   - Удалить дублирующую регистрацию обработчиков в `main` функции.
   - Использовать `j_loads` и `j_loads_ns` если требуется работа с json файлами.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
.. module:: src.endpoints.bots.telegram.bot
   :synopsis: Модуль для реализации Telegram бота.

.. rubric:: Описание

   Этот модуль содержит класс :class:`TelegramBot`, который используется для создания и управления Telegram ботом.
   Бот обрабатывает различные команды, голосовые сообщения и текстовые сообщения, а также отправляет PDF файлы.

..  warning::
    Модуль использует заглушку для распознавания речи.

..  code-block:: python

    from pathlib import Path
    from telegram import Update
    from telegram.ext import CallbackContext
    from src.logger.logger import logger
    import asyncio
    import requests
    from src.utils.file import read_text_file
    from src.utils.convertors.tts import speech_to_text


.. table:: Основные функции и команды бота
   :widths: auto

   ===================================  ============================================================================
   Функция/Команда                      Описание
   ===================================  ============================================================================
   **Инициализация бота**               Инициализация бота с токеном для аутентификации с Telegram API.
   ``/start``                           Отправляет приветственное сообщение пользователю.
   ``/help``                            Предоставляет список доступных команд.
   ``/sendpdf``                         Отправляет PDF файл пользователю.
   **Обработка сообщений**               Обрабатывает входящие текстовые, голосовые сообщения и файлы документов.
   **Обработка голосовых сообщений**    Скачивает голосовое сообщение, сохраняет его и пытается транскрибировать (заглушка).
   **Обработка документов**            Скачивает документ, сохраняет его и читает текстовое содержимое.
   **Обработка текста**                Возвращает полученный от пользователя текст.
   ===================================  ============================================================================

.. table:: Основные модули и библиотеки
   :widths: auto

   =========================  ============================================================================
   Модуль/Библиотека         Описание
   =========================  ============================================================================
   ``python-telegram-bot``   Основная библиотека для создания Telegram ботов.
   ``pathlib``               Для работы с путями к файлам.
   ``tempfile``              Для создания временных файлов.
   ``asyncio``               Для асинхронного выполнения задач.
   ``requests``              Для скачивания файлов.
   ``src.utils.convertors.tts``   Для распознавания речи и преобразования текста в речь.
   ``src.utils.file``        Для чтения текстовых файлов.
   =========================  ============================================================================

.. autoclass:: src.endpoints.bots.telegram.TelegramBot
   :members:
   :undoc-members:
   :show-inheritance:

.. code-block:: python

    def main():
        """
        Инициализация и запуск Telegram бота.

        Эта функция инициализирует бота с токеном из переменных окружения,
        регистрирует обработчики команд и сообщений и запускает бота.
        """
        ...

"""

MODE = 'dev'

from pathlib import Path
import tempfile
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

import header
from src import gs
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.logger.logger import logger
import requests  # For downloading files
from src.utils.convertors.tts import speech_recognizer, text2speech
from src.utils.file import read_text_file


class TelegramBot:
    """
    Класс для взаимодействия с Telegram ботом.

    :ivar application: Экземпляр `telegram.ext.Application`.
    """
    application: Application

    def __init__(self, token: str):
        """
        Инициализирует Telegram бота.

        :param token: Токен Telegram бота, например, `gs.credentials.telegram.bot.kazarinov`.
        :type token: str
        """
        self.application = Application.builder().token(token).build()
        self.register_handlers()

    def register_handlers(self):
        """
        Регистрирует обработчики команд и сообщений.
        """
        self.application.add_handler(CommandHandler('start', self.start))
        self.application.add_handler(CommandHandler('help', self.help_command))
        self.application.add_handler(CommandHandler('sendpdf', self.send_pdf))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
        self.application.add_handler(MessageHandler(filters.VOICE, self.handle_voice))
        self.application.add_handler(MessageHandler(filters.Document.ALL, self.handle_document))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_log))

    async def start(self, update: Update, context: CallbackContext) -> None:
        """
        Обрабатывает команду `/start`.

        :param update: Объект `telegram.Update`, содержащий информацию о входящем сообщении.
        :type update: telegram.Update
        :param context: Объект `telegram.ext.CallbackContext`, содержащий контекст текущего разговора.
        :type context: telegram.ext.CallbackContext
        """
        self.update = update
        self.context = context
        await self.update.message.reply_text('Hello! I am your simple bot. Type /help to see available commands.')

    async def help_command(self, update: Update, context: CallbackContext) -> None:
        """
        Обрабатывает команду `/help`.

        :param update: Объект `telegram.Update`, содержащий информацию о входящем сообщении.
        :type update: telegram.Update
        :param context: Объект `telegram.ext.CallbackContext`, содержащий контекст текущего разговора.
        :type context: telegram.ext.CallbackContext
        """
        self.update = update
        self.context = context
        await self.update.message.reply_text(
            'Available commands:\n'
            '/start - Start the bot\n'
            '/help - Show this help message\n'
            '/sendpdf - Send a PDF file'
        )

    async def send_pdf(self, pdf_file: str | Path) -> None:
        """
        Обрабатывает команду `/sendpdf` для генерации и отправки PDF файла.

        :param pdf_file: Путь к PDF файлу.
        :type pdf_file: str | Path
        """
        try:
            # Код открывает PDF файл для чтения в бинарном режиме и отправляет его пользователю.
            with open(pdf_file, 'rb') as pdf_file_obj:
                await self.update.message.reply_document(document=pdf_file_obj)

        except Exception as ex:
            logger.error('Ошибка при отправке PDF-файла: ', ex)
            await self.update.message.reply_text('Произошла ошибка при отправке PDF-файла. Попробуй ещё раз.')

    async def handle_voice(self, update: Update, context: CallbackContext) -> None:
        """
        Обрабатывает голосовые сообщения и транскрибирует аудио.

        :param update: Объект `telegram.Update`, содержащий информацию о входящем сообщении.
        :type update: telegram.Update
        :param context: Объект `telegram.ext.CallbackContext`, содержащий контекст текущего разговора.
        :type context: telegram.ext.CallbackContext
        """
        self.update = update
        self.context = context
        try:
            # Код получает файл голосового сообщения.
            voice = self.update.message.voice
            file = await self.context.bot.get_file(voice.file_id)
            file_path = gs.path.temp / f'{voice.file_id}.ogg'

            # Код скачивает файл на локальную систему.
            await file.download_to_drive(file_path)

            # Код вызывает функцию для транскрибирования голосового сообщения.
            transcribed_text = self.transcribe_voice(file_path)

            # Код отправляет распознанный текст пользователю.
            await self.update.message.reply_text(f'Распознанный текст: {transcribed_text}')

        except Exception as ex:
            logger.error('Ошибка при обработке голосового сообщения: ', ex)
            await self.update.message.reply_text('Произошла ошибка при обработке голосового сообщения. Попробуй ещё раз.')

    async def transcribe_voice(self, file_path: Path) -> str:
        """
        Транскрибирует голосовое сообщение используя сервис распознавания речи.

        :param file_path: Путь к файлу голосового сообщения.
        :type file_path: Path
        :return: Распознанный текст.
        :rtype: str

        .. note::
            В текущей реализации возвращает заглушку.
            TODO: Заменить на реальную реализацию распознавания речи.
        """
        # Код возвращает заглушку, так как реальное распознавание голоса еще не реализовано.
        return 'Распознавание голоса ещё не реализовано.'

    async def handle_document(self, update: Update, context: CallbackContext) -> str:
        """
        Обрабатывает полученные документы.

        :param update: Объект `telegram.Update`, содержащий информацию о входящем сообщении.
        :type update: telegram.Update
        :param context: Объект `telegram.ext.CallbackContext`, содержащий контекст текущего разговора.
        :type context: telegram.ext.CallbackContext
        :return: Содержимое текстового документа.
        :rtype: str
        """
        self.update = update
        self.context = context
        # Код получает файл документа.
        file = await self.update.message.document.get_file()
        # Код скачивает файл на локальную систему.
        tmp_file_path = await file.download_to_drive()
        # Код читает содержимое текстового файла.
        return read_text_file(tmp_file_path)

    async def handle_message(self, update: Update, context: CallbackContext) -> str:
        """
        Обрабатывает любое текстовое сообщение.

        :param update: Объект `telegram.Update`, содержащий информацию о входящем сообщении.
        :type update: telegram.Update
        :param context: Объект `telegram.ext.CallbackContext`, содержащий контекст текущего разговора.
        :type context: telegram.ext.CallbackContext
        :return: Текст полученный от пользователя.
        :rtype: str
        """
        self.update = update
        self.context = context
        # Код возвращает текст сообщения.
        return self.update.message.text

    async def handle_log(self, update: Update, context: CallbackContext) -> None:
        """
        Обрабатывает сообщения журнала.
        """
        # Код записывает в лог полученное сообщение.
        log_message = update.message.text
        logger.info(f"Received log message: {log_message}")
        await update.message.reply_text("Log received and processed.")


def main() -> None:
    """
    Запускает бота.

    Эта функция инициализирует бота с токеном из переменных окружения,
    регистрирует обработчики команд и сообщений и запускает бота.
    """
    token = gs.credentials.telegram.bot.kazarinov
    bot = TelegramBot(token)

    # Код запускает бота в режиме polling.
    bot.application.run_polling()

if __name__ == '__main__':
    main()
```
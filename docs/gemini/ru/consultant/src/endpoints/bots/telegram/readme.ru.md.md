# Анализ кода модуля `src.endpoints.bots.telegram`

**Качество кода**
9
- Плюсы
    - Документация в целом описывает функциональность и структуру модуля.
    - Присутствует описание основных функций, команд и используемых библиотек.
    -  Есть описание процесса обработки различных типов сообщений.
- Минусы
    -  Не хватает подробной документации в стиле reStructuredText (RST) для модуля, классов и методов непосредственно в коде.
    -  Отсутствует обработка ошибок и логирование, которые необходимо добавить.
    - В тексте используется  `python-telegram-bot`  без импорта в коде.

**Рекомендации по улучшению**

1.  **Документация**:
    -   Переписать документацию модуля, классов и методов в формате RST непосредственно в коде.
    -   Добавить описание каждого параметра и возвращаемого значения для функций и методов.

2.  **Импорты**:
    -   Добавить все необходимые импорты, которые используются в описании.

3.  **Логирование**:
    -   Использовать `from src.logger.logger import logger` для логирования ошибок и отладочной информации.
    -   Избегать блоков `try-except` и вместо этого использовать `logger.error` для записи ошибок.

4.  **Обработка ошибок**:
    -   Включить обработку ошибок при загрузке файлов и транскрибировании голоса.

5.  **Рефакторинг**:
    -   Привести в соответствие имена функций, переменных и импортов с ранее обработанными файлами.

**Оптимизированный код**

```python
"""
Модуль для реализации Telegram-бота.
=========================================================================================

Этот модуль содержит класс :class:`TelegramBot`, который предоставляет интерфейс для работы с Telegram API.
Бот может обрабатывать команды, голосовые сообщения и файлы документов.

Пример использования
--------------------

Пример использования класса `TelegramBot`:

.. code-block:: python

    from src.endpoints.bots.telegram.telegram import TelegramBot

    bot = TelegramBot(token="YOUR_BOT_TOKEN")
    bot.run()
"""
import asyncio
import tempfile
from pathlib import Path
from typing import Any

import requests
from telegram import Update
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    MessageHandler,
    Updater,
    Filters,
)

from src.logger.logger import logger # Добавлен импорт для логирования
from src.utils.convertors.tts import TextToSpeech # Добавлен импорт TextToSpeech
from src.utils.file import read_text_file # Добавлен импорт read_text_file


class TelegramBot:
    """
    Класс для управления Telegram-ботом.

    Использует библиотеку python-telegram-bot для обработки сообщений и команд.
    """

    def __init__(self, token: str):
        """
        Инициализирует бота с токеном и регистрирует обработчики.

        :param token: Токен для доступа к Telegram API.
        """
        self.token = token
        self.updater = Updater(token, use_context=True)
        self.dispatcher = self.updater.dispatcher
        self.register_handlers()
        self.tts = TextToSpeech()# Добавлен инициализатор TextToSpeech

    def register_handlers(self):
        """
        Регистрирует обработчики команд и сообщений.
        """
        self.dispatcher.add_handler(CommandHandler("start", self.start))
        self.dispatcher.add_handler(CommandHandler("help", self.help_command))
        self.dispatcher.add_handler(CommandHandler("sendpdf", self.send_pdf))
        self.dispatcher.add_handler(MessageHandler(Filters.voice, self.handle_voice))
        self.dispatcher.add_handler(MessageHandler(Filters.document, self.handle_document))
        self.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), self.handle_message))


    def start(self, update: Update, context: CallbackContext):
        """
        Обрабатывает команду `/start`.

        Отправляет приветственное сообщение пользователю.

        :param update: Объект Update от Telegram API.
        :param context: Объект CallbackContext от Telegram API.
        """
        update.message.reply_text("Привет! Я бот, который может обрабатывать текст, голос и файлы.")

    def help_command(self, update: Update, context: CallbackContext):
        """
        Обрабатывает команду `/help`.

        Предоставляет список доступных команд.

        :param update: Объект Update от Telegram API.
        :param context: Объект CallbackContext от Telegram API.
        """
        help_text = """
        Доступные команды:
        /start - Приветственное сообщение.
        /help - Список доступных команд.
        /sendpdf - Отправляет PDF-файл (заглушка).
        """
        update.message.reply_text(help_text)

    def send_pdf(self, update: Update, context: CallbackContext, pdf_file: str | Path = 'test.pdf'):
        """
         Обрабатывает команду `/sendpdf` для отправки PDF-файла.

         :param update: Объект Update от Telegram API.
         :param context: Объект CallbackContext от Telegram API.
         :param pdf_file: Путь к PDF-файлу для отправки.
         """
        try:
            # Код отправляет файл
            with open(pdf_file, 'rb') as file:
                update.message.reply_document(document=file)
        except FileNotFoundError:
            logger.error(f"Файл {pdf_file} не найден.")# Логирование ошибки, если файл не найден
            update.message.reply_text(f"Файл {pdf_file} не найден.")
        except Exception as ex:
             logger.error(f'Не удалось отправить файл {pdf_file} из-за ошибки', ex) # Логирование других ошибок
             update.message.reply_text(f'Не удалось отправить файл {pdf_file}')

    async def handle_voice(self, update: Update, context: CallbackContext):
        """
        Обрабатывает голосовые сообщения и транскрибирует аудио.

        :param update: Объект Update от Telegram API.
        :param context: Объект CallbackContext от Telegram API.
        """
        try:
            # Код получает данные голосового сообщения
            voice_file = await context.bot.get_file(update.message.voice.file_id)
            file_path = Path(f'{tempfile.gettempdir()}/{update.message.voice.file_unique_id}.ogg')
            await voice_file.download(file_path)

            # Код транскрибирует голосовое сообщение
            transcribed_text = await self.transcribe_voice(file_path)
            update.message.reply_text(f"Распознанный текст: {transcribed_text}")

        except Exception as ex:
            logger.error('Ошибка обработки голосового сообщения', ex)  # логируем ошибку
            update.message.reply_text("Не удалось обработать голосовое сообщение.")
        finally:
            # Код удаляет временный файл
            if file_path.exists():
                file_path.unlink()


    async def transcribe_voice(self, file_path: Path) -> str:
        """
        Транскрибирует голосовые сообщения.

        :param file_path: Путь к файлу голосового сообщения.
        :return: Распознанный текст.
        """
        # TODO: Реализовать транскрибирование голоса
        logger.debug(f"Транскрибирование голоса из файла: {file_path}") # Логирование для отладки
        return 'Транскрибирование голоса пока не реализовано.'

    async def handle_document(self, update: Update, context: CallbackContext) -> str:
        """
        Обрабатывает файлы документов и читает их содержимое.

        :param update: Объект Update от Telegram API.
        :param context: Объект CallbackContext от Telegram API.
        :return: Содержимое текстового документа.
        """
        try:
            # Код получает данные документа
            document = update.message.document
            file_path = Path(f'{tempfile.gettempdir()}/{document.file_unique_id}_{document.file_name}')
            file = await context.bot.get_file(document.file_id)
            await file.download(file_path)
            # Код читает содержимое файла
            file_content = read_text_file(file_path)
            update.message.reply_text(f"Содержимое файла:\n{file_content}")

        except Exception as ex:
            logger.error(f'Ошибка обработки документа {document.file_name}', ex) # Логирование ошибки
            update.message.reply_text("Не удалось обработать документ.")
        finally:
             # Код удаляет временный файл
            if file_path.exists():
                file_path.unlink()


    async def handle_message(self, update: Update, context: CallbackContext) -> str:
        """
        Обрабатывает текстовые сообщения и возвращает полученный текст.

        :param update: Объект Update от Telegram API.
        :param context: Объект CallbackContext от Telegram API.
        :return: Текст полученного сообщения.
        """
        text = update.message.text
        logger.debug(f"Получено текстовое сообщение: {text}") # Логирование полученного сообщения
        update.message.reply_text(f"Вы отправили: {text}")

    def run(self):
        """
        Запускает бота.
        """
        self.updater.start_polling()
        self.updater.idle()


def main():
    """
     Основная функция для запуска бота.
    """
    #TODO: заменить на загрузку из конфига
    token = "6624577530:AAG23C54nQpYt_W_2J8g6rB274826e5u18M"
    bot = TelegramBot(token=token)
    bot.run()


if __name__ == "__main__":
    main()
```
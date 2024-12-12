# Анализ кода модуля `bot.py`

**Качество кода: 7/10**

-   **Плюсы:**
    *   Код структурирован в класс `PsychologistTelgrambot`, что способствует организации и повторному использованию.
    *   Используется асинхронность для обработки сообщений, что повышает отзывчивость бота.
    *   Присутствует обработка различных типов сообщений (текст, голос, документы).
    *   Используется `logger` для логирования ошибок, что полезно для отладки.
    *   Используются `dataclass` для определения структуры данных, что делает код более лаконичным и читаемым.
-   **Минусы:**
    *   Не все docstring написаны в reStructuredText (RST) формате.
    *   Не хватает комментариев в стиле RST для методов и переменных.
    *   Используется не унифицированная обработка ошибок, где местами `try-except` а местами `logger.error`.
    *   Некоторые комментарии после `#` не соответствуют стилю документации RST.
    *   Отсутствует проверка на наличие `self.mexiron` перед его использованием в `handle_suppliers_response` и `handle_onetab_response`.
    *   В коде есть неиспользуемый импорт `header`.

**Рекомендации по улучшению:**

1.  **Документация:**
    *   Необходимо переписать все docstring в формате reStructuredText (RST).
    *   Добавить docstring для всех методов и переменных класса.
    *   Привести комментарии в коде `#` в соответствие с документацией RST.
2.  **Обработка ошибок:**
    *   Заменить `try-except` на `logger.error` для более консистентной обработки ошибок.
3.  **Импорты:**
    *   Удалить неиспользуемый импорт `header`.
4.  **Безопасность:**
    *   Добавить проверку на существование `self.mexiron` перед его использованием.
5. **Стиль кода**:
    *   Использовать `from src.utils.jjson import j_loads, j_loads_ns` вместо `json.load` (если это необходимо)
    *   Привести все кавычки в коде к одинарным `'`

**Оптимизированный код:**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для создания Telegram-бота психолога.
=========================================================================================

Этот модуль содержит класс :class:`PsychologistTelgrambot`, который является
специализированным Telegram-ботом, предназначенным для имитации поведения
психолога с использованием модели Google Gemini.

Пример использования
--------------------

Пример создания и запуска бота:

.. code-block:: python

    kt = PsychologistTelgrambot()
    asyncio.run(kt.application.run_polling())
"""
import asyncio
from pathlib import Path
from typing import Optional, Any
from dataclasses import dataclass, field
import random
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, CallbackContext

from src import gs
from src.bots.telegram import TelegramBot
from src.webdriver.driver import Driver, Chrome
from src.ai.gemini import GoogleGenerativeAI
from src.utils.file import read_text_file, recursively_read_text_files, save_text_file
from src.utils.url import is_url
from src.logger.logger import logger
# from src.utils.jjson import j_loads, j_loads_ns #TODO если нужно использовать
MODE = 'dev'


@dataclass
class PsychologistTelgrambot(TelegramBot):
    """
    Telegram bot with custom behavior for Kazarinov.

    :ivar token: Telegram bot token.
    :vartype token: str
    :ivar d: Webdriver instance.
    :vartype d: Driver
    :ivar model: Google Gemini AI model.
    :vartype model: GoogleGenerativeAI
    :ivar system_instruction: System instruction for the AI model.
    :vartype system_instruction: str
    :ivar questions_list: List of questions for the bot.
    :vartype questions_list: list
    :ivar timestamp: Timestamp of bot initialization.
    :vartype timestamp: str
    """
    token: str = field(init=False)
    d: Driver = field(init=False)
    model: GoogleGenerativeAI = field(init=False)
    system_instruction: str = field(init=False)
    questions_list: list = field(init=False)
    timestamp: str = field(default_factory=lambda: gs.now)

    def __post_init__(self):
        """Initialize the bot, setup the driver, AI model and register handlers."""
        mode = 'test'
        #self.token = gs.credentials.telegram.hypo69_test_bot if mode == 'test' else gs.credentials.telegram.hypo69_psychologist_bot
        self.token = gs.credentials.telegram.hypo69_psychologist_bot
        super().__init__(self.token)

        self.d = Driver(Chrome)
        
        self.system_instruction = read_text_file(
            gs.path.google_drive / 'hypo69_psychologist_bot' / 'prompts' / 'chat_system_instruction.txt'
        )
        self.questions_list = recursively_read_text_files(
            gs.path.google_drive / 'hypo69_psychologist_bot' / 'prompts' / 'train_data' / 'q', ['*.*'], as_list=True
        )

        self.model = GoogleGenerativeAI(
            api_key=gs.credentials.gemini.hypo69_psychologist_bot,
            system_instruction=self.system_instruction,
            generation_config={"response_mime_type": "text/plain"}
        )
        
        self.register_handlers()

    def register_handlers(self):
        """Register bot commands and message handlers."""
        self.application.add_handler(CommandHandler('start', self.start))
        self.application.add_handler(CommandHandler('help', self.help_command))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
        self.application.add_handler(MessageHandler(filters.VOICE, self.handle_voice))
        self.application.add_handler(MessageHandler(filters.Document.ALL, self.handle_document))

    async def start(self, update: Update, context: CallbackContext) -> None:
        """
        Handle the /start command.

        :param update: Telegram update object.
        :type update: telegram.Update
        :param context: Telegram context object.
        :type context: telegram.ext.CallbackContext
        """
        await update.message.reply_text('Hi! I am a smart assistant psychologist.')
        await super().start(update, context)

    async def handle_message(self, update: Update, context: CallbackContext) -> None:
        """
        Handle text messages, log them, and get an AI-generated response.

        :param update: Telegram update object.
        :type update: telegram.Update
        :param context: Telegram context object.
        :type context: telegram.ext.CallbackContext
        """
        response = update.message.text
        user_id = update.effective_user.id

        log_path = gs.path.google_drive / 'bots' / str(user_id) / 'chat_logs.txt'
        save_text_file(f'User {user_id}: {response}\\n', Path(log_path))
        answer = self.model.ask(q=response, history_file=f'{user_id}.txt')
        return await update.message.reply_text(answer)

    def get_handler_for_url(self, response: str):
        """
        Map URLs to specific handlers.

        :param response: The URL string to be handled.
        :type response: str
        :return: Handler function if a match is found, otherwise None.
        :rtype: Optional[Callable]
        """
        url_handlers = {
            'suppliers': (
                (
                    'https://morlevi.co.il', 'https://www.morlevi.co.il',
                    'https://grandadvance.co.il', 'https://www.grandadvance.co.il',
                    'https://ksp.co.il', 'https://www.ksp.co.il',
                    'https://ivory.co.il', 'https://www.ivory.co.il'
                ),
                self.handle_suppliers_response
            ),
            'onetab': (('https://www.one-tab.com',), self.handle_onetab_response),
        }
        for urls, handler_func in url_handlers.values():
            if response.startswith(urls):
                return handler_func
        return

    async def handle_suppliers_response(self, update: Update, response: str) -> None:
        """
        Handle suppliers' URLs using mexiron.

        :param update: Telegram update object.
        :type update: telegram.Update
        :param response: The URL string.
        :type response: str
        """
        if not hasattr(self, 'mexiron'): # проверка на существование self.mexiron
            logger.error('`mexiron` not initialized')
            await update.message.reply_text('Произошла ошибка при обработке запроса.')
            return
        if await self.mexiron.run_scenario(response, update):
            await update.message.reply_text('Готово!')
        else:
            await update.message.reply_text('Хуёвенько. Попробуй еще раз')

    async def handle_onetab_response(self, update: Update, response: str) -> None:
        """
        Handle OneTab URLs using mexiron.

        :param update: Telegram update object.
        :type update: telegram.Update
        :param response: The URL string.
        :type response: str
        """
        # TODO: fix undefined variables `price, mexiron_name, urls`
        if not hasattr(self, 'mexiron'):# проверка на существование self.mexiron
             logger.error('`mexiron` not initialized')
             await update.message.reply_text('Произошла ошибка при обработке запроса.')
             return
        if await self.mexiron.run_scenario(price=None, mexiron_name=None, urls=None):
            await update.message.reply_text('Готово!\\nСсылку я вышлю на WhatsApp')
        else:
            await update.message.reply_text('Хуёвенько. Попробуй ещё раз')

    async def handle_next_command(self, update: Update) -> None:
        """
        Handle '--next' and related commands to get a random question and its answer.

        :param update: Telegram update object.
        :type update: telegram.Update
        """
        try:
            question = random.choice(self.questions_list)
            answer = self.model.ask(question)
            await asyncio.gather(
                update.message.reply_text(question),
                update.message.reply_text(answer)
            )
        except Exception as ex:
            logger.error('Ошибка чтения вопросов', ex)
            await update.message.reply_text('Произошла ошибка при чтении вопросов.')

    async def handle_document(self, update: Update, context: CallbackContext) -> None:
        """
        Handle document uploads, extracts text from it and reply to user.

        :param update: Telegram update object.
        :type update: telegram.Update
        :param context: Telegram context object.
        :type context: telegram.ext.CallbackContext
        """
        file_content = await super().handle_document(update, context)
        await update.message.reply_text(f'Received your document. Content: {file_content}')

if __name__ == '__main__':
    kt = PsychologistTelgrambot()
    asyncio.run(kt.application.run_polling())
```
# Анализ кода модуля `bot.py`

**Качество кода: 7/10**

*   **Плюсы:**
    *   Код структурирован в класс `PsychologistTelgrambot`, что способствует организации и переиспользованию.
    *   Используется `dataclass`, что упрощает создание класса и уменьшает количество шаблонного кода.
    *   Присутствует логирование, что помогает в отладке и мониторинге работы бота.
    *   Код использует асинхронность, что позволяет боту обрабатывать несколько запросов параллельно.
    *   Используется `recursively_read_text_files` для чтения файлов, что является полезной утилитой.
*   **Минусы:**
    *   Отсутствует docstring модуля.
    *   Не все методы класса имеют docstring.
    *   Присутствует закомментированный код, который следует удалить.
    *   Обработка ошибок в `handle_next_command` не использует `logger.error`, а использует `logger.debug`.
    *   В методе `handle_onetab_response` не определены переменные `price`, `mexiron_name`, `urls`, которые используются при вызове `self.mexiron.run_scenario`.
    *   Не используется `j_loads` или `j_loads_ns` для чтения данных из файла, где это необходимо.
    *   Некоторые комментарии после `#` являются краткими и не содержат подробных объяснений.
    *   В некоторых местах используется избыточное количество `await`.
    *   В `handle_message` нет обработки ошибок.
    *   В методе `get_handler_for_url` не возвращается значение по умолчанию.

**Рекомендации по улучшению:**

1.  Добавить docstring для модуля `bot.py`.
2.  Добавить docstring для всех методов в классе `PsychologistTelgrambot`.
3.  Удалить закомментированный код.
4.  Использовать `logger.error` вместо `logger.debug` при возникновении ошибок в `handle_next_command`.
5.  Исправить ошибку в `handle_onetab_response`, определив переменные `price`, `mexiron_name`, `urls` или убрав их, если они не нужны.
6.  Использовать `j_loads` или `j_loads_ns` для загрузки данных из файлов, если таковые имеются.
7.  Переписать комментарии после `#` в соответствии с требованиями, добавив подробные пояснения к следующему блоку кода.
8.  Убрать избыточное использование `await` там, где это возможно.
9.  Добавить обработку ошибок в `handle_message` с использованием `logger.error`.
10. Добавить возвращаемое значение по умолчанию для `get_handler_for_url`, например `return None`.

**Оптимизированный код:**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для реализации Telegram-бота-психолога.
====================================================

Этот модуль содержит класс :class:`PsychologistTelgrambot`, который представляет собой
Telegram-бота с пользовательским поведением, разработанного для Каzаринова.
Бот обрабатывает текстовые и голосовые сообщения, а также загрузку документов.

Пример использования:
--------------------

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
from src.logger.logger import logger
# from src.utils.jjson import j_loads, j_loads_ns # TODO: добавить использование j_loads или j_loads_ns, если потребуется

@dataclass
class PsychologistTelgrambot(TelegramBot):
    """
    Telegram bot with custom behavior for Kazarinov.

    :param token: Telegram bot token.
    :type token: str
    :param d: Driver instance for web interactions.
    :type d: Driver
    :param model: GoogleGenerativeAI model for text generation.
    :type model: GoogleGenerativeAI
    :param system_instruction: System instruction text for the AI model.
    :type system_instruction: str
    :param questions_list: List of questions for bot interactions.
    :type questions_list: list
    :param timestamp: Timestamp for tracking bot sessions.
    :type timestamp: str
    """
    token: str = field(init=False)
    d: Driver = field(init=False)
    model: GoogleGenerativeAI = field(init=False)
    system_instruction: str = field(init=False)
    questions_list: list = field(init=False)
    timestamp: str = field(default_factory=lambda: gs.now)

    def __post_init__(self):
        """Initialize the bot, set token, driver, AI model, and register handlers."""
        mode = 'test'
        # Код устанавливает токен бота из конфигурации. #TODO: Уточнить режим работы бота
        self.token = gs.credentials.telegram.hypo69_psychologist_bot
        super().__init__(self.token)

        # Код инициализирует веб-драйвер
        self.d = Driver(Chrome)
        
        # Код загружает системные инструкции для AI модели
        self.system_instruction = read_text_file(
            gs.path.google_drive / 'hypo69_psychologist_bot' / 'prompts' / 'chat_system_instruction.txt'
        )
        # Код загружает список вопросов для бота
        self.questions_list = recursively_read_text_files(
            gs.path.google_drive / 'hypo69_psychologist_bot' / 'prompts' / 'train_data' / 'q', ['*.*'], as_list=True
        )
        # Код инициализирует AI модель
        self.model = GoogleGenerativeAI(
            api_key=gs.credentials.gemini.hypo69_psychologist_bot,
            system_instruction=self.system_instruction,
            generation_config={"response_mime_type": "text/plain"}
        )
        
        # Код регистрирует обработчики сообщений
        self.register_handlers()

    def register_handlers(self):
        """Register bot commands and message handlers."""
        # Код регистрирует обработчик команды /start
        self.application.add_handler(CommandHandler('start', self.start))
        # Код регистрирует обработчик команды /help
        self.application.add_handler(CommandHandler('help', self.help_command))
        # Код регистрирует обработчик текстовых сообщений
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
        # Код регистрирует обработчик голосовых сообщений
        self.application.add_handler(MessageHandler(filters.VOICE, self.handle_voice))
        # Код регистрирует обработчик загрузки документов
        self.application.add_handler(MessageHandler(filters.Document.ALL, self.handle_document))

    async def start(self, update: Update, context: CallbackContext) -> None:
        """
        Handle /start command.

        :param update: Telegram update object.
        :type update: telegram.Update
        :param context: CallbackContext for handling updates.
        :type context: telegram.ext.CallbackContext
        """
        # Код отправляет приветственное сообщение пользователю
        await update.message.reply_text('Hi! I am a smart assistant psychologist.')
        await super().start(update, context)

    async def handle_message(self, update: Update, context: CallbackContext) -> None:
        """
        Handle text messages with URL-based routing.

        :param update: Telegram update object.
        :type update: telegram.Update
        :param context: CallbackContext for handling updates.
        :type context: telegram.ext.CallbackContext
        """
        # Код извлекает текст сообщения от пользователя
        response = update.message.text
        # Код извлекает ID пользователя
        user_id = update.effective_user.id
        
        # Код формирует путь к файлу лога
        log_path = gs.path.google_drive / 'bots' / str(user_id) / 'chat_logs.txt'
        # Код сохраняет сообщение пользователя в лог
        save_text_file(f"User {user_id}: {response}\\n", Path(log_path))
        try:
            # Код отправляет запрос в AI модель и получает ответ
            answer = self.model.ask(q=response, history_file=f'{user_id}.txt')
            # Код отправляет ответ пользователю
            await update.message.reply_text(answer)
        except Exception as ex:
            # Код логирует ошибку, если произошла
            logger.error(f'Error handling message from user {user_id}', exc_info=ex)
            await update.message.reply_text('Произошла ошибка при обработке сообщения.')

    def get_handler_for_url(self, response: str) -> Optional[Any]:
        """
        Map URLs to specific handlers.

        :param response: The URL or message text to be processed.
        :type response: str
        :return: The handler function to call, or None if no handler matches.
        :rtype: Optional[Callable]
        """
        # Код устанавливает соответствие между URL и обработчиками
        url_handlers = {
            "suppliers": (
                ('https://morlevi.co.il', 'https://www.morlevi.co.il',
                 'https://grandadvance.co.il', 'https://www.grandadvance.co.il',
                 'https://ksp.co.il', 'https://www.ksp.co.il',
                 'https://ivory.co.il', 'https://www.ivory.co.il'),
                self.handle_suppliers_response
            ),
            "onetab": (('https://www.one-tab.com',), self.handle_onetab_response),
        }
        # Код проверяет, начинается ли сообщение с одного из зарегистрированных URL
        for urls, handler_func in url_handlers.values():
            if response.startswith(urls):
                # Код возвращает соответствующий обработчик
                return handler_func
        # Код возвращает None, если нет соответствующего обработчика
        return None

    async def handle_suppliers_response(self, update: Update, response: str) -> None:
        """
        Handle suppliers' URLs.

        :param update: Telegram update object.
        :type update: telegram.Update
        :param response: The URL to process.
        :type response: str
        """
        # Код запускает сценарий обработки URL поставщиков
        if await self.mexiron.run_scenario(response, update):
            # Код отправляет подтверждение, если сценарий выполнен успешно
            await update.message.reply_text('Готово!')
        else:
            # Код отправляет сообщение об ошибке, если сценарий не выполнен
            await update.message.reply_text('Хуёвенько. Попробуй еще раз')

    async def handle_onetab_response(self, update: Update, response: str) -> None:
        """
        Handle OneTab URLs.

        :param update: Telegram update object.
        :type update: telegram.Update
        :param response: The URL to process.
        :type response: str
        """
        # TODO: определить price, mexiron_name, urls.
        price = None
        mexiron_name = None
        urls = None
        # Код запускает сценарий обработки OneTab URL
        if await self.mexiron.run_scenario(price=price, mexiron_name=mexiron_name, urls=urls):
            # Код отправляет подтверждение, если сценарий выполнен успешно
            await update.message.reply_text('Готово!\nСсылку я вышлю на WhatsApp')
        else:
            # Код отправляет сообщение об ошибке, если сценарий не выполнен
            await update.message.reply_text('Хуёвенько. Попробуй ещё раз')

    async def handle_next_command(self, update: Update) -> None:
        """
        Handle '--next' and related commands.

        :param update: Telegram update object.
        :type update: telegram.Update
        """
        try:
            # Код выбирает случайный вопрос из списка
            question = random.choice(self.questions_list)
            # Код отправляет запрос в AI модель и получает ответ
            answer = self.model.ask(question)
            # Код отправляет вопрос и ответ пользователю
            await asyncio.gather(
                update.message.reply_text(question),
                update.message.reply_text(answer)
            )
        except Exception as ex:
            # Код логирует ошибку при чтении вопросов
            logger.error("Ошибка чтения вопросов", exc_info=ex)
            await update.message.reply_text('Произошла ошибка при чтении вопросов.')

    async def handle_document(self, update: Update, context: CallbackContext) -> None:
        """
        Handle document uploads.

        :param update: Telegram update object.
        :type update: telegram.Update
        :param context: CallbackContext for handling updates.
        :type context: telegram.ext.CallbackContext
        """
        # Код вызывает родительский обработчик документов и получает содержимое файла
        file_content = await super().handle_document(update, context)
        # Код отправляет сообщение с содержимым файла
        await update.message.reply_text(f'Received your document. Content: {file_content}')

if __name__ == "__main__":
    # Код создает экземпляр бота
    kt = PsychologistTelgrambot()
    # Код запускает бота
    asyncio.run(kt.application.run_polling())
```
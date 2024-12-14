## Анализ кода модуля `bot.py`

**Качество кода**
    7
 -  Плюсы
        - Код имеет базовую структуру, необходимую для работы Telegram-бота.
        - Используется асинхронность для обработки сообщений.
        - Присутствует разделение на обработчики команд и сообщений.
        - Логирование ошибок с использованием `logger`.
 -  Минусы
    -  Отсутствует документация в формате reStructuredText.
    -  Используются конструкции `try-except` без явной необходимости.
    -  Жестко заданные пути к файлам и папкам.
    -  Импорты не упорядочены и могут быть избыточными.
    -  Дублирование кода в обработчиках URL.
    -  Не используется `j_loads` или `j_loads_ns` для загрузки файлов.
    -  Некоторые переменные не используются (например, `mode`).
    -  Логирование в `handle_next_command` не информативно.
    -  Не все функции имеют docstrings.
    -  Не хватает обработки ошибок в некоторых местах.
    -  Присутсвуют магические строки  `'Hi! I am a smart assistant psychologist.'`, `'Готово!'`, `'Хуёвенько. Попробуй еще раз'`  и т.д..

**Рекомендации по улучшению**

1.  **Документация:**
    *   Добавить reStructuredText (RST) комментарии для всех модулей, классов, функций и методов.
    *   Описать назначение, параметры и возвращаемые значения для каждой функции и метода.

2.  **Обработка ошибок:**
    *   Использовать `logger.error` вместо `try-except` блоков.
    *   Добавить более информативные сообщения об ошибках в лог.

3.  **Импорты:**
    *   Упорядочить импорты в алфавитном порядке и сгруппировать их.
    *   Удалить неиспользуемые импорты.

4.  **Пути к файлам:**
    *   Использовать переменные для хранения путей к файлам и папкам.
    *   Сделать пути конфигурационными, если это необходимо.

5.  **Обработка URL:**
    *   Реализовать более гибкую систему сопоставления URL с обработчиками.
    *   Избегать дублирования кода в обработчиках URL.

6. **Магические строки**
    * Перенести все магические строки в константы или переменные, если они могут быть изменены.
    * Для сообщений бота предусмотреть возможность их изменения из вне (возможно через json файл).

7.  **Загрузка файлов:**
    *   Использовать `j_loads` или `j_loads_ns` для загрузки JSON файлов.

8. **Разное**
    *   Удалить или закомментировать неиспользуемый код.
    *   Перенести инициализацию бота в отдельную функцию.
    *   В `handle_onetab_response`  не используются переменные `price`, `mexiron_name` и `urls`, нужно либо передать, либо удалить.

**Оптимизиробанный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для реализации Telegram-бота психолога.
=========================================================================================

Этот модуль содержит класс :class:`PsychologistTelgrambot`, который используется для
создания и управления Telegram-ботом, предоставляющим психологическую помощь.

Основные возможности:
    - Обработка команд и текстовых сообщений пользователей.
    - Интеграция с Google Gemini AI для генерации ответов на вопросы.
    - Запись истории сообщений пользователя.
    - Обработка голосовых сообщений и документов.

Пример использования
--------------------

Пример инициализации и запуска бота:

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

BOT_GREETING = 'Hi! I am a smart assistant psychologist.'
SUCCESS_MESSAGE = 'Готово!'
FAILURE_MESSAGE = 'Хуёвенько. Попробуй еще раз'
ERROR_READING_QUESTIONS = 'Произошла ошибка при чтении вопросов.'
RECEIVED_DOCUMENT_MESSAGE = 'Received your document. Content: {}'
WHATSAPP_LINK_MESSAGE = 'Готово!\\nСсылку я вышлю на WhatsApp'


@dataclass
class PsychologistTelgrambot(TelegramBot):
    """
    Класс, представляющий Telegram-бота с пользовательским поведением для психолога.

    :ivar token: Токен Telegram-бота.
    :vartype token: str
    :ivar d: Драйвер для управления веб-браузером.
    :vartype d: Driver
    :ivar model: Модель Google Gemini для генерации текста.
    :vartype model: GoogleGenerativeAI
    :ivar system_instruction: Инструкции для модели.
    :vartype system_instruction: str
    :ivar questions_list: Список вопросов для бота.
    :vartype questions_list: list
    :ivar timestamp: Временная метка запуска бота.
    :vartype timestamp: str
    """
    token: str = field(init=False)
    d: Driver = field(init=False)
    model: GoogleGenerativeAI = field(init=False)
    system_instruction: str = field(init=False)
    questions_list: list = field(init=False)
    timestamp: str = field(default_factory=lambda: gs.now)

    def __post_init__(self):
        """
        Инициализация бота после создания экземпляра класса.

        :return: None
        """
        #  код устанавливает токен бота
        self.token = gs.credentials.telegram.hypo69_psychologist_bot
        super().__init__(self.token)

        # код инициализирует драйвер веб-браузера
        self.d = Driver(Chrome)

        # код читает системные инструкции из файла
        self.system_instruction = read_text_file(
            gs.path.google_drive / 'hypo69_psychologist_bot' / 'prompts' / 'chat_system_instruction.txt'
        )
        #  код читает список вопросов из файлов
        self.questions_list = recursively_read_text_files(
            gs.path.google_drive / 'hypo69_psychologist_bot' / 'prompts' / 'train_data' / 'q', ['*.*'], as_list=True
        )

        #  код инициализирует модель Google Gemini AI
        self.model = GoogleGenerativeAI(
            api_key=gs.credentials.gemini.hypo69_psychologist_bot,
            system_instruction=self.system_instruction,
            generation_config={"response_mime_type": "text/plain"}
        )
        # код регистрирует обработчики
        self.register_handlers()

    def register_handlers(self):
        """
        Регистрирует обработчики команд и сообщений бота.

        :return: None
        """
        self.application.add_handler(CommandHandler('start', self.start))
        self.application.add_handler(CommandHandler('help', self.help_command))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
        self.application.add_handler(MessageHandler(filters.VOICE, self.handle_voice))
        self.application.add_handler(MessageHandler(filters.Document.ALL, self.handle_document))

    async def start(self, update: Update, context: CallbackContext) -> None:
        """
        Обрабатывает команду /start.

        :param update: Объект Update от Telegram.
        :type update: Update
        :param context: Объект CallbackContext от Telegram.
        :type context: CallbackContext
        :return: None
        """
        # код отправляет приветствие пользователю
        await update.message.reply_text(BOT_GREETING)
        await super().start(update, context)

    async def handle_message(self, update: Update, context: CallbackContext) -> None:
        """
         Обрабатывает текстовые сообщения, включая URL.

        :param update: Объект Update от Telegram.
        :type update: Update
        :param context: Объект CallbackContext от Telegram.
        :type context: CallbackContext
        :return: None
        """
        response = update.message.text
        user_id = update.effective_user.id

        # код сохраняет сообщение в лог
        log_path = gs.path.google_drive / 'bots' / str(user_id) / 'chat_logs.txt'
        save_text_file(f"User {user_id}: {response}\n", Path(log_path))

        # код получает ответ от модели ИИ
        answer = self.model.ask(q=response, history_file=f'{user_id}.txt')
        await update.message.reply_text(answer)

    def get_handler_for_url(self, response: str):
        """
        Определяет обработчик для URL.

        :param response: Текст сообщения.
        :type response: str
        :return: Функция-обработчик или None.
        :rtype: Optional[Callable]
        """
        url_handlers = {
            "suppliers": (
                (
                    'https://morlevi.co.il', 'https://www.morlevi.co.il',
                    'https://grandadvance.co.il', 'https://www.grandadvance.co.il',
                    'https://ksp.co.il', 'https://www.ksp.co.il',
                    'https://ivory.co.il', 'https://www.ivory.co.il'
                ),
                self.handle_suppliers_response
            ),
            "onetab": (('https://www.one-tab.com',), self.handle_onetab_response),
        }
        for urls, handler_func in url_handlers.values():
            if response.startswith(urls):
                return handler_func
        return None

    async def handle_suppliers_response(self, update: Update, response: str) -> None:
        """
        Обрабатывает URL-адреса поставщиков.

        :param update: Объект Update от Telegram.
        :type update: Update
        :param response: Текст сообщения.
        :type response: str
        :return: None
        """
        # код запускает сценарий mexiron
        if await self.mexiron.run_scenario(response, update):
             # код отправляет сообщение об успешном выполнении
            await update.message.reply_text(SUCCESS_MESSAGE)
        else:
            # код отправляет сообщение о неудаче
            await update.message.reply_text(FAILURE_MESSAGE)

    async def handle_onetab_response(self, update: Update, response: str) -> None:
        """
        Обрабатывает URL-адреса OneTab.
        
        :param update: Объект Update от Telegram.
        :type update: Update
        :param response: Текст сообщения.
        :type response: str
        :return: None
        """
        # TODO: add params to  `self.mexiron.run_scenario`
        #  код запускает сценарий mexiron
        if await self.mexiron.run_scenario():
             # код отправляет сообщение об успешном выполнении
            await update.message.reply_text(WHATSAPP_LINK_MESSAGE)
        else:
             # код отправляет сообщение о неудаче
            await update.message.reply_text(FAILURE_MESSAGE)

    async def handle_next_command(self, update: Update) -> None:
        """
        Обрабатывает команду \'--next\' и связанные с ней команды.

        :param update: Объект Update от Telegram.
        :type update: Update
        :return: None
        """
        try:
             # код выбирает случайный вопрос из списка
            question = random.choice(self.questions_list)
             # код получает ответ на вопрос от модели ИИ
            answer = self.model.ask(question)
            # код отправляет вопрос и ответ пользователю
            await asyncio.gather(
                update.message.reply_text(question),
                update.message.reply_text(answer)
            )
        except Exception as ex:
            #  код логирует ошибку
            logger.error("Ошибка чтения вопросов", exc_info=ex)
            await update.message.reply_text(ERROR_READING_QUESTIONS)

    async def handle_document(self, update: Update, context: CallbackContext) -> None:
        """
        Обрабатывает загруженные документы.
        
        :param update: Объект Update от Telegram.
        :type update: Update
        :param context: Объект CallbackContext от Telegram.
        :type context: CallbackContext
        :return: None
        """
        # код получает содержимое загруженного документа
        file_content = await super().handle_document(update, context)
        # код отправляет сообщение с содержимым документа
        await update.message.reply_text(RECEIVED_DOCUMENT_MESSAGE.format(file_content))

if __name__ == "__main__":
    # код запускает бота
    kt = PsychologistTelgrambot()
    asyncio.run(kt.application.run_polling())
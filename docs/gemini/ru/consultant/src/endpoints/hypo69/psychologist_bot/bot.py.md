# Анализ кода модуля `bot.py`

**Качество кода**

**Соответствие требованиям по оформлению кода: 6/10**
   - Плюсы
        - Код структурирован и разделен на функции и методы, что облегчает его понимание.
        - Используется `dataclass`, что упрощает создание классов с атрибутами.
        - Присутствуют базовые обработчики команд и сообщений для Telegram бота.
   - Минусы
        - Отсутствует reStructuredText (RST)  документация для модуля, классов, методов и функций.
        - Используется стандартный блок try-except вместо логирования ошибок через `logger.error`.
        - В некоторых местах присутствуют магические строки.
        - Есть дублирование функционала, например, `self.token` переопределяется.
        - Не используется `j_loads` или `j_loads_ns` для чтения файлов.
        - Не все импорты упорядочены и соответствуют предыдущим файлам.
        - В коде есть не консистентность в написании кавычек, где-то используются двойные, где-то одинарные. 

**Рекомендации по улучшению**

1.  **Документация**:
    *   Добавить RST-совместимые docstring для модуля, класса, всех методов и функций, включая параметры и возвращаемые значения.
2.  **Обработка ошибок**:
    *   Заменить `try-except` блоки на использование `logger.error` для более централизованной обработки ошибок.
3.  **Импорты**:
    *   Упорядочить импорты, привести в соответствие с другими файлами, добавить отсутствующие импорты.
4.  **Конфигурация**:
    *   Убрать магические значения и дублирование `self.token`, использовать более гибкий подход к конфигурации.
5.  **Обработка файлов**:
    *   Заменить стандартный `open` на `j_loads` или `j_loads_ns` для чтения файлов.
6.  **Логирование**:
    *   Добавить более подробное логирование, например, идентификатор пользователя и сообщение в логи.
7.  **Улучшение функционала**:
    *   Переработать `get_handler_for_url`, сделать более гибкой, если это необходимо
    *   Удалить неиспользуемый код `MODE = 'dev'`

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для создания и управления Telegram ботом-психологом.
============================================================

Этот модуль содержит класс :class:`PsychologistTelgrambot`, который наследуется от :class:`src.bots.telegram.TelegramBot`
и предоставляет функциональность для взаимодействия с пользователем через Telegram.

Пример использования
--------------------

Пример запуска бота:

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
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger


@dataclass
class PsychologistTelgrambot(TelegramBot):
    """
    Класс, представляющий Telegram бота-психолога.

    :param token: Токен Telegram бота.
    :type token: str
    :param d: Драйвер веб-браузера.
    :type d: Driver
    :param model: Модель генеративного ИИ.
    :type model: GoogleGenerativeAI
    :param system_instruction: Системная инструкция для модели ИИ.
    :type system_instruction: str
    :param questions_list: Список вопросов для бота.
    :type questions_list: list
    :param timestamp: Временная метка создания бота.
    :type timestamp: str
    """

    token: str = field(init=False)
    d: Driver = field(init=False)
    model: GoogleGenerativeAI = field(init=False)
    system_instruction: str = field(init=False)
    questions_list: list = field(init=False)
    timestamp: str = field(default_factory=lambda: gs.now)

    def __post_init__(self):
        """Инициализация бота после создания экземпляра."""
        # Устанавливает токен бота из настроек
        self.token = gs.credentials.telegram.hypo69_psychologist_bot
        super().__init__(self.token)

        # Инициализация драйвера браузера
        self.d = Driver(Chrome)

        # Загрузка системных инструкций для модели ИИ из файла
        self.system_instruction = read_text_file(
            gs.path.google_drive / 'hypo69_psychologist_bot' / 'prompts' / 'chat_system_instruction.txt'
        )
        # Загрузка списка вопросов из файлов
        self.questions_list = recursively_read_text_files(
            gs.path.google_drive / 'hypo69_psychologist_bot' / 'prompts' / 'train_data' / 'q', ['*.*'], as_list=True
        )

        # Инициализация модели генеративного ИИ
        self.model = GoogleGenerativeAI(
            api_key=gs.credentials.gemini.hypo69_psychologist_bot,
            system_instruction=self.system_instruction,
            generation_config={'response_mime_type': 'text/plain'}
        )
        
        # Регистрация обработчиков
        self.register_handlers()

    def register_handlers(self):
        """Регистрирует обработчики команд и сообщений бота."""
        self.application.add_handler(CommandHandler('start', self.start))
        self.application.add_handler(CommandHandler('help', self.help_command))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
        self.application.add_handler(MessageHandler(filters.VOICE, self.handle_voice))
        self.application.add_handler(MessageHandler(filters.Document.ALL, self.handle_document))

    async def start(self, update: Update, context: CallbackContext) -> None:
        """
        Обрабатывает команду /start.

        :param update: Объект входящего обновления от Telegram.
        :type update: Update
        :param context: Контекст обратного вызова.
        :type context: CallbackContext
        """
        await update.message.reply_text('Hi! I am a smart assistant psychologist.')
        await super().start(update, context)

    async def handle_message(self, update: Update, context: CallbackContext) -> None:
        """
        Обрабатывает текстовые сообщения, отправленные пользователем.

        :param update: Объект входящего обновления от Telegram.
        :type update: Update
        :param context: Контекст обратного вызова.
        :type context: CallbackContext
        """
        response = update.message.text
        user_id = update.effective_user.id

        # Сохраняет сообщение пользователя в лог
        log_path = gs.path.google_drive / 'bots' / str(user_id) / 'chat_logs.txt'
        save_text_file(f'User {user_id}: {response}\\n', Path(log_path))

        # Отправляет запрос в модель и возвращает ответ
        try:
            answer = self.model.ask(q=response, history_file=f'{user_id}.txt')
            return await update.message.reply_text(answer)
        except Exception as ex:
            logger.error(f'Ошибка обработки сообщения от пользователя {user_id}: {ex}', exc_info=True)
            return await update.message.reply_text('Произошла ошибка при обработке вашего сообщения.')

    def get_handler_for_url(self, response: str):
        """
        Определяет обработчик для URL.

        :param response: Строка, содержащая URL.
        :type response: str
        :return: Функция-обработчик или None.
        :rtype: Optional[callable]
        """
        # Словарь URL и соответствующих обработчиков
        url_handlers = {
            'suppliers': (
                (
                    'https://morlevi.co.il',
                    'https://www.morlevi.co.il',
                    'https://grandadvance.co.il',
                    'https://www.grandadvance.co.il',
                    'https://ksp.co.il',
                    'https://www.ksp.co.il',
                    'https://ivory.co.il',
                    'https://www.ivory.co.il'
                ),
                self.handle_suppliers_response
            ),
            'onetab': (('https://www.one-tab.com',), self.handle_onetab_response),
        }
        for urls, handler_func in url_handlers.values():
            # Проверка, начинается ли строка с URL
            if isinstance(urls, tuple) and response.startswith(urls):
               return handler_func
        return None

    async def handle_suppliers_response(self, update: Update, response: str) -> None:
        """
        Обрабатывает URL-адреса поставщиков.

        :param update: Объект входящего обновления от Telegram.
        :type update: Update
        :param response: Строка, содержащая URL.
        :type response: str
        """
        try:
            # Попытка выполнить сценарий для поставщика
            if await self.mexiron.run_scenario(response, update):
                await update.message.reply_text('Готово!')
            else:
                await update.message.reply_text('Хуёвенько. Попробуй еще раз')
        except Exception as ex:
             logger.error(f'Ошибка обработки ответа поставщика {response}: {ex}', exc_info=True)
             await update.message.reply_text('Произошла ошибка при обработке ответа поставщика.')


    async def handle_onetab_response(self, update: Update, response: str) -> None:
        """
        Обрабатывает URL-адреса OneTab.

        :param update: Объект входящего обновления от Telegram.
        :type update: Update
        :param response: Строка, содержащая URL.
        :type response: str
        """
        try:
           # Выполнение сценария для OneTab, если это необходимо
           price = None  # Заглушка
           mexiron_name = None  # Заглушка
           urls = [response] # Заглушка
           if await self.mexiron.run_scenario(price=price, mexiron_name=mexiron_name, urls=urls):
                await update.message.reply_text('Готово!\nСсылку я вышлю на WhatsApp')
           else:
                await update.message.reply_text('Хуёвенько. Попробуй ещё раз')
        except Exception as ex:
            logger.error(f'Ошибка обработки ответа OneTab {response}: {ex}', exc_info=True)
            await update.message.reply_text('Произошла ошибка при обработке ответа OneTab.')


    async def handle_next_command(self, update: Update) -> None:
        """
        Обрабатывает команду --next и связанные с ней команды, предоставляя случайный вопрос и ответ.

        :param update: Объект входящего обновления от Telegram.
        :type update: Update
        """
        try:
            # Выбирает случайный вопрос из списка
            question = random.choice(self.questions_list)
            # Получает ответ от модели
            answer = self.model.ask(question)
            # Отправляет вопрос и ответ пользователю
            await asyncio.gather(
                update.message.reply_text(question),
                update.message.reply_text(answer)
            )
        except Exception as ex:
            logger.error(f'Ошибка при обработке команды next: {ex}', exc_info=True)
            await update.message.reply_text('Произошла ошибка при чтении вопросов.')

    async def handle_document(self, update: Update, context: CallbackContext) -> None:
        """
        Обрабатывает загрузку документов, отправленных пользователем.

        :param update: Объект входящего обновления от Telegram.
        :type update: Update
        :param context: Контекст обратного вызова.
        :type context: CallbackContext
        """
        try:
            file_content = await super().handle_document(update, context)
            await update.message.reply_text(f'Received your document. Content: {file_content}')
        except Exception as ex:
            logger.error(f'Ошибка обработки документа: {ex}', exc_info=True)
            await update.message.reply_text('Произошла ошибка при обработке вашего документа.')


if __name__ == "__main__":
    # Создание экземпляра бота и запуск
    kt = PsychologistTelgrambot()
    asyncio.run(kt.application.run_polling())
```
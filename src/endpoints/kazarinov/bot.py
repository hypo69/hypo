## \file hypotez/src/endpoints/kazarinov/bot.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.endpoints.kazarinov """
MODE = 'development'

"""
### KazarinovTelegramBot

Описание:
Модуль реализует Telegram-бота для проекта Kazarinov, поддерживающего 
различные сценарии обработки команд и сообщений. Бот взаимодействует 
с парсером Mexiron и моделью Google Generative AI, а также поддерживает 
обработку текстовых сообщений, документов и URL.

Основные возможности:
1. Инициализация и настройка Telegram-бота на основе конфигурационного JSON-файла.
2. Регистрация команд и обработчиков сообщений.
3. Маршрутизация текстовых сообщений по URL с возможностью обработки ссылок на OneTab и поставщиков.
4. Использование объекта Mexiron для парсинга данных товаров от поставщиков и генерации прайс-листов.
5. Генерация ответов на сообщения через Google Generative AI.
6. Логирование сообщений пользователей и их дальнейшая обработка.

Зависимости:
- pydantic: для работы с конфигурационными моделями.
- telegram.ext: для создания и управления Telegram-ботом.
- GoogleGenerativeAI: для генерации ответов на сообщения пользователей.
- Mexiron: для парсинга и обработки данных товаров поставщиков.
- Driver (Chrome | Edge | Firefox | Playwright): обеспечивает работу с целeвыми HTML.
- HandlerExecutors: реализует набор вспомогательных методов для обработки пользовательских команд, маршрутизации сообщений и выполнения сценариев, специфичных для Kazarinov.
"""

import asyncio
from importlib.resources import read_text
import json
import random
from pathlib import Path
from typing import List, Optional
from types import SimpleNamespace
from pydantic import BaseModel, Field
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

import header
from src import gs
from src.bots.telegram import TelegramBot
from src.utils.string import url
from src.endpoints.kazarinov.bot_handlers_parser import HandlersParser
from src.utils.file import recursively_read_text_files, save_text_file
from src.utils.string.url import is_url
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.logger import logger


class KazarinovTelegramBot(TelegramBot, HandlersParser):
    """Telegram bot with custom behavior for Kazarinov."""

    token: str
    config = j_loads_ns(gs.path.src / 'endpoints' / 'kazarinov' / 'config.json')
    
    system_instruction:str = Path(gs.path.endpoints / 'kazarinov' / 'instructions' / 'system_instruction.md').read_text(encoding='UTF-8')
    mexiron_command_instruction:str = Path(gs.path.endpoints / 'kazarinov' / 'instructions' / 'mexiron.md').read_text(encoding='UTF-8')
    
    questions_list_path = config.questions_list_path

    def __init__(self, mode: Optional[str] = 'test', webdriver_name: Optional[str] = 'firefox'):
        # Устанавливаем настройки
        mode = mode if mode else self.config.mode 
        self.token = (
            gs.credentials.telegram.hypo69_test_bot
            if mode == 'test'
            else gs.credentials.telegram.hypo69_kazarinov_bot
        )
        super().__init__(self.token)
        HandlersParser().__init__(webdriver_name)

    async def handle_message(self, update: Update, context: CallbackContext) -> None:
        """Handle text messages with URL-based routing."""
        response = update.message.text
        user_id = update.effective_user.id
        if is_url(response):
            self.handle_url(update, context)
            # <- add logic after url scenario ended
            ...

        log_path = gs.path.google_drive / 'bots' / str(user_id) / 'chat_logs.txt'
        save_text_file(f"User {user_id}: {response}\n", Path(log_path), mode='a')

        if self.handle_onetab_url(update, response):
            await update.message.reply_text("OK")

        if self.handle_supplier_url(response):
            return await handler(update, response)

        if response in ('--next', '-next', '__next', '-n', '-q'):
            return await self.handle_next_command(update)

        if not is_url(response):
            answer = self.model.ask(q=response, history_file=f'{user_id}.txt')
            await update.message.reply_text(answer)

    # def handle_supplier_url(self, response: str) -> Optional[bool]:
    #     """Map URLs to specific handlers."""
    #     if any(response.startswith(url) for url in self.config.url_handlers.suppliers):
    #         # Здесь будет код для обработки ссылок поставщиков
    #         pass
    #     return False

    # async def handle_onetab_url(self, update: Update, response: str) -> bool:
    #     """Handle OneTab URLs."""
    #     if not response.startswith(('https://onetab.com', 'http://onetab.com')):
    #         return False

    #     price, mexiron_name, urls = fetch_target_urls_onetab(response)

    #     if not all([price, mexiron_name, urls]):
    #         await update.message.reply_text('Ошибка на сервере OneTab. Попробуй ещё раз через часок.')
    #         return False

    #     elif await self.mexiron.run_scenario(price=price, mexiron_name=mexiron_name, urls=urls):
    #         await update.message.reply_text('Готово!\nСсылку я вышлю на WhatsApp')
    #         return True

    #     else:
    #         await update.message.reply_text('Ошибка. Попробуй ещё раз.')
    #         return False

    # async def handle_next_command(self, update: Update) -> None:
    #     """Handle '--next' and related commands."""
    #     try:
    #         question = random.choice(self.questions_list)
    #         answer = self.model.ask(question)
    #         await asyncio.gather(
    #             update.message.reply_text(question),
    #             update.message.reply_text(answer)
    #         )
    #     except Exception as ex:
    #         logger.debug("Ошибка чтения вопросов: %s", ex)
    #         await update.message.reply_text('Произошла ошибка при чтении вопросов.')


if __name__ == "__main__":
    kt = KazarinovTelegramBot(mode='test', webdriver_name='firefox')
    asyncio.run(kt.application.run_polling())

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
"""

import asyncio
import json
import random
from pathlib import Path
from typing import List, Optional
from pydantic import BaseModel, Field
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, CallbackContext

import header
from src import gs
from src.bots.telegram import TelegramBot
from src.webdriver.driver import Driver
from src.webdriver.chrome import Chrome
from src.ai.gemini import GoogleGenerativeAI
from src.endpoints.kazarinov.parser_onetab import fetch_target_urls_onetab
from src.endpoints.kazarinov.scenarios.scenario_pricelist import Mexiron
from src.utils.file import recursively_read_text_files, save_text_file
from src.utils.string.url import is_url
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.logger import logger


class KazarinovBotConfig(BaseModel):
    """Config model for KazarinovTelegramBot."""
    
    mode: str
    driver: dict
    mexiron: dict
    system_instruction_path: str
    questions_list_path: str
    url_handlers: dict
    generation_config: dict
    telegram: dict


class KazarinovTelegramBot(TelegramBot, BaseModel):
    """Telegram bot with custom behavior for Kazarinov."""

    config: KazarinovBotConfig
    token: str
    d: Driver
    mexiron: Mexiron
    model: GoogleGenerativeAI
    system_instruction: str
    questions_list: List[str]
    timestamp: str = Field(default_factory=lambda: gs.now)

    def __init__(self, config:Optional[dict]):
        # Загружаем конфигурацию из JSON
        with open(config_path, "r", encoding="utf-8") as file:
            config_data = json.load(file)

        config_data - j_loads(config_path)
        self.config = KazarinovBotConfig(**config_data)
        
        # Выбираем токен на основе режима
        self.token = (
            gs.credentials.telegram.hypo69_test_bot
            if self.config.mode == 'test'
            else gs.credentials.telegram.hypo69_kazarinov_bot
        )
        
        # Инициализация драйвера и Mexiron
        self.d = Driver(Chrome, **self.config.driver.get("options", {}))
        self.mexiron = Mexiron(self.d)
        
        # Загрузка системных инструкций и вопросов
        self.system_instruction = recursively_read_text_files(
            gs.path.google_drive / self.config.system_instruction_path
        )
        self.questions_list = recursively_read_text_files(
            gs.path.google_drive / self.config.questions_list_path, ['*.*'], as_list=True
        )
        
        # Инициализация модели
        self.model = GoogleGenerativeAI(
            api_key=gs.credentials.gemini.kazarinov,
            system_instruction=self.system_instruction,
            generation_config=self.config.generation_config
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
        """Handle /start command."""
        await update.message.reply_text('Hello! This is Kazarinov’s custom bot.')

    async def handle_message(self, update: Update, context: CallbackContext) -> None:
        """Handle text messages with URL-based routing."""
        response = update.message.text
        user_id = update.effective_user.id

        log_path = gs.path.google_drive / 'bots' / str(user_id) / 'chat_logs.txt'
        save_text_file(f"User {user_id}: {response}\n", Path(log_path))

        if handler := self.get_handler_for_url(response):
            return await handler(update, response)

        if response in ('--next', '-next', '__next', '-n', '-q'):
            return await self.handle_next_command(update)

        if not is_url(response):
            answer = self.model.ask(q=response, history_file=f'{user_id}.txt')
            await update.message.reply_text(answer)

    def get_handler_for_url(self, response: str):
        """Map URLs to specific handlers."""
        for key, (urls, handler_func) in self.config.url_handlers.items():
            if any(response.startswith(url) for url in urls):
                return getattr(self, handler_func)
        return None

    async def handle_suppliers_response(self, update: Update, response: str) -> None:
        """Handle suppliers' URLs."""
        if await self.mexiron.run_scenario(response, update):
            await update.message.reply_text('Готово!')
        else:
            await update.message.reply_text('Ошибка. Попробуй ещё раз.')

    async def handle_onetab_response(self, update: Update, response: str) -> None:
        """Handle OneTab URLs."""
        price, mexiron_name, urls = fetch_target_urls_onetab(response)

        if not all([price, mexiron_name, urls]):
            await update.message.reply_text('Ошибка на сервере OneTab. Попробуй ещё раз через часок.')
        elif await self.mexiron.run_scenario(price=price, mexiron_name=mexiron_name, urls=urls):
            await update.message.reply_text('Готово!\nСсылку я вышлю на WhatsApp')
        else:
            await update.message.reply_text('Ошибка. Попробуй ещё раз.')

    async def handle_next_command(self, update: Update) -> None:
        """Handle '--next' and related commands."""
        try:
            question = random.choice(self.questions_list)
            answer = self.model.ask(question)
            await asyncio.gather(
                update.message.reply_text(question),
                update.message.reply_text(answer)
            )
        except Exception as ex:
            logger.debug("Ошибка чтения вопросов: %s", ex)
            await update.message.reply_text('Произошла ошибка при чтении вопросов.')

    async def handle_document(self, update: Update, context: CallbackContext) -> None:
        """Handle document uploads."""
        file_content = await super().handle_document(update, context)
        await update.message.reply_text(f'Received your document. Content: {file_content}')


if __name__ == "__main__":
    config_path = "settings.json"
    kt = KazarinovTelegramBot(config_path=config_path)
    asyncio.run(kt.application.run_polling())

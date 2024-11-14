## \file hypotez/src/endpoints/kazarinov/hypo69_kazarinov_bot.py
# -*- coding: utf-8 -*-
""" module: src.endpoints.kazarinov """
""" Kazarinov's specific bot with customized behavior."""

import asyncio
import random
from pathlib import Path
from typing import List
from pydantic import BaseModel, Field
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, CallbackContext

from __init__ import gs
from src.endpoints.bots.telegram import TelegramBot
from src.webdriver import Driver, Chrome
from src.ai.gemini import GoogleGenerativeAI
from src.endpoints.kazarinov.parser_onetab import fetch_target_urls_onetab
from src.endpoints.kazarinov.scenarios.scenario_pricelist import Mexiron
from src.utils.file import recursively_read_text_files, save_text_file
from src.utils.string.url import is_url
from src.logger import logger


class KazarinovTelegramBot(TelegramBot, BaseModel):
    """Telegram bot with custom behavior for Kazarinov."""

    token: str
    d: Driver
    mexiron: Mexiron
    model: GoogleGenerativeAI
    system_instruction: str
    questions_list: List[str]
    timestamp: str = Field(default_factory=lambda: gs.now)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.token = (
            gs.credentials.telegram.hypo69_test_bot
            if kwargs.get('mode', 'test') == 'test'
            else gs.credentials.telegram.hypo69_kazarinov_bot
        )

        self.d = Driver(Chrome)
        self.mexiron = Mexiron(self.d)

        self.system_instruction = recursively_read_text_files(
            gs.path.google_drive / 'kazarinov' / 'prompts' / 'chat_system_instruction.txt'
        )
        self.questions_list = recursively_read_text_files(
            gs.path.google_drive / 'kazarinov' / 'prompts' / 'train_data' / 'q', ['*.*'], as_list=True
        )

        self.model = GoogleGenerativeAI(
            api_key=gs.credentials.gemini.kazarinov,
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
        for urls, handler_func in url_handlers.values():
            if response.startswith(urls):
                return handler_func
        return

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
            error_message = 'Ошибка на сервере OneTab. Попробуй ещё раз через часок.'
            await update.message.reply_text(error_message)
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
    kt = KazarinovTelegramBot(mode = 'test') # или mode='prod' для рабочего токена
    asyncio.run(kt.application.run_polling())

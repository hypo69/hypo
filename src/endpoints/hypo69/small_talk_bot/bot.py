## \file hypotez/src/endpoints/hypo69/small_talk_bot/bot.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.endpoints.hypo69.small_talk_bot 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'dev'

...
""" t.me/hypo69_psychologist_bot_bot's specific bot with customized behavior."""
import header

import asyncio
from pathlib import Path
from typing import Optional
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

@dataclass
class PsychologistTelgrambot(TelegramBot):
    """Telegram bot with custom behavior for Kazarinov."""

    token: str = field(init=False)
    d: Driver = field(init=False)
    model: GoogleGenerativeAI = field(init=False)
    system_instruction: str = field(init=False)
    questions_list: list = field(init=False)
    timestamp: str = field(default_factory=lambda: gs.now)

    def __post_init__(self):
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
        """Handle /start command."""
        await update.message.reply_text('Hi! I am a smart assistant psychologist.')
        await super().start(update, context)

    async def handle_message(self, update: Update, context: CallbackContext) -> None:
        """Handle text messages with URL-based routing."""
        response = update.message.text
        user_id = update.effective_user.id

        log_path = gs.path.google_drive / 'bots' / str(user_id) / 'chat_logs.txt'
        save_text_file(f"User {user_id}: {response}\n", Path(log_path))
        answer = self.model.ask(q=response, history_file=f'{user_id}.txt')
        return await update.message.reply_text(answer)

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
            await update.message.reply_text('Хуёвенько. Попробуй еще раз')

    async def handle_onetab_response(self, update: Update, response: str) -> None:
        """Handle OneTab URLs."""


        if await self.mexiron.run_scenario(price=price, mexiron_name=mexiron_name, urls=urls):
            await update.message.reply_text('Готово!\nСсылку я вышлю на WhatsApp')
        else:
            await update.message.reply_text('Хуёвенько. Попробуй ещё раз')

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
            logger.debug("Ошибка чтения вопросов")
            await update.message.reply_text('Произошла ошибка при чтении вопросов.')

    async def handle_document(self, update: Update, context: CallbackContext) -> None:
        """Handle document uploads."""
        file_content = await super().handle_document(update, context)
        await update.message.reply_text(f'Received your document. Content: {file_content}')

if __name__ == "__main__":
    kt = PsychologistTelgrambot()
    asyncio.run(kt.application.run_polling())

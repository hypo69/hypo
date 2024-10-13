## \file ../src/suppliers/kazarinov/bot.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""! Kazarinov's specific bot with customized behavior. """

import asyncio
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, CallbackContext

import header
from src import gs
from src.bots.telegram_bot import TelegramBot
from src.webdriver import Driver, Chrome
from src.suppliers.kazarinov.parser_onetab import fetch_target_urls_onetab
from src.suppliers.kazarinov.prepare_morlevi_data import ExecuteProducts

class KazarinovTelegram(TelegramBot):
    """Telegram bot with custom behavior for Kazarinov."""

    token = gs.credentials.telegram.bot.kazarinov
    d:Driver
    product_executor: ExecuteProducts

    def __init__(self):
        """Initialize the Kazarinov bot."""
        super().__init__(self.token)
        self.d = Driver(Chrome)
        self.product_executor = ExecuteProducts(self.d)

        # Register command handlers
        self.application.add_handler(CommandHandler('start', self.start))
        self.application.add_handler(CommandHandler('help', self.help_command))

        # Register message handlers
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
        self.application.add_handler(MessageHandler(filters.VOICE, self.handle_voice))
        self.application.add_handler(MessageHandler(filters.Document.ALL, self.handle_document))

    async def start(self, update: Update, context: CallbackContext) -> None:
        """Override the /start command with custom behavior."""
        await update.message.reply_text('Hello! This is Kazarinov’s custom bot.')
        # Optionally, call the parent method if needed
        await super().start(update, context)

    async def handle_message(self, update: Update, context: CallbackContext) -> bool:
        """Override the message handler with custom logic."""
        ...
        response = update.message.text
        if response.startswith('https://www.one-tab.com'):
            tab_name, urls = fetch_target_urls_onetab(response)

            if await self.product_executor.prepare_morlevi_data(tab_name, urls ):
                return  await update.message.reply_text('Сохранил')
            return  await update.message.reply_text('Хуёвенько')

        # Add custom behavior here
        if response.lower() == 'hello':
            await update.message.reply_text('Hi! How can I assist you today?')
        return response  # Optionally return text as in parent method

    async def handle_document(self, update: Update, context: CallbackContext) -> str:
        """Override document handler with additional logging."""
        file_content = await super().handle_document(update, context)
        await update.message.reply_text(f'Received your document. Content: {file_content}')
        return file_content

if __name__ == "__main__":
    kt = KazarinovTelegram()
    # Start the bot (add necessary logic to run the event loop if needed)
    asyncio.run(kt.application.run_polling())

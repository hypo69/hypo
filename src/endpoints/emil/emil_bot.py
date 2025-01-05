from __future__ import annotations
## \file /src/endpoints/emil/emil_bot.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Telegram-бот для проекта emil-design.com
====================================================
Бот получает url поставщиков

.. module:: src.endpoints.emil.emil_bot
	:platform: Windows, Unix
	:synopsis: bot for emil-design.com

"""

import asyncio
from pathlib import Path
from typing import List, Optional, Dict, Self
from types import SimpleNamespace
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

import header
"""
.. header.py:
    ```mermaid
    flowchart TD
        Start --> Header[<code>header.py</code><br> Determine Project Root]

        Header --> import[Import Global Settings: <br><code>from src import gs</code>]
```
"""
from src import gs
from src.endpoints.bots.telegram.bot_web_hooks import TelegramBot
# from src.endpoints.bots.telegram.bot_long_polling import TelegramBot
from src.endpoints.emil.bot_handlers import BotHandler
from src.ai.openai import OpenAIModel
from src.ai.gemini import GoogleGenerativeAI
from src.utils.file import recursively_read_text_files, save_text_file
from src.utils.url import is_url
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.logger.logger import logger

import argparse
from aiohttp import web
from src.endpoints.bots.telegram.bot_web_hooks import create_app


class EmilTelegramBot(TelegramBot):
    """Telegram bot with custom behavior for emil-design."""

    token: str
    config = j_loads_ns(gs.path.endpoints / 'emil' / 'emil.json')
    model: GoogleGenerativeAI = GoogleGenerativeAI(
        api_key=gs.credentials.gemini.kazarinov, generation_config={"response_mime_type": "text/plain"}
    )
    """This model is used for dialog with the user. For processing scenarios, the model defined in the `BotHandler` class is used."""
    bot_handler: BotHandler

    def __init__(self, mode: Optional[str] = None, webdriver_name: Optional[str] = 'firefox'):
        """
        Initialize the EmilTelegramBot instance.

        :param mode: Operating mode, 'test' or 'production'. Defaults to 'test'.
        :type mode: Optional[str]
        :param webdriver_name: Webdriver to use with BotHandler. Defaults to 'firefox'.
        :type webdriver_name: Optional[str]
        """
        # Set the mode
        mode = mode or self.config.mode
        # Initialize the token based on mode
        self.token = (
            gs.credentials.telegram.hypo69_test_bot
            if mode == 'test'
            else gs.credentials.telegram.hypo69_emil_design_bot
        )

        # Call parent initializers
        self.bot_handler = BotHandler(webdriver_name=webdriver_name)
        TelegramBot.__init__(self, self.token, self.bot_handler) # Pass bot_handler to TelegramBot



    async def handle_message(self, update: Update, context: CallbackContext) -> None:
         """Handle any text message."""
         await self.bot_handler.handle_message(update, context)

    async def handle_log(self, update: Update, context: CallbackContext) -> None:
        """Handle log messages."""
        log_message = update.message.text
        logger.info(f"Received log message: {log_message}")
        await update.message.reply_text("Log received and processed.")

    async def handle_voice(self, update: Update, context: CallbackContext) -> None:
        """Handle voice messages and transcribe the audio."""
        await super().handle_voice(update, context)
        
    async def transcribe_voice(self, file_path: Path) -> str:
        """Transcribe voice message using a speech recognition service."""
        # Пример заглушки, замените это на реальную логику распознавания речи
        return 'Распознавание голоса ещё не реализовано.'


def main() -> None:
    """Start the bot with webhook."""
    bot = EmilTelegramBot()

    # Create and run the aiohttp application
    app = create_app(bot)
    web.run_app(app, host=bot.host, port=bot.port)

if __name__ == '__main__':
    main()

from __future__ import annotations
## \file hypotez/src/endpoints/emil/emil_bot.py
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
from src.endpoints.kazarinov.bot_handlers import BotHandler
from src.ai.openai import OpenAIModel
from src.ai.gemini import GoogleGenerativeAI
from src.utils.file import recursively_read_text_files, save_text_file
from src.utils.url import is_url
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.logger.logger import logger

import argparse
from aiohttp import web
from src.endpoints.bots.telegram.bot_web_hooks import create_app


class EmilTelegramBot(TelegramBot, BotHandler):
    """Telegram bot with custom behavior for emil-design."""

    token: str
    config = j_loads_ns(gs.path.endpoints / 'emil' / 'emil.json')
    model: GoogleGenerativeAI = GoogleGenerativeAI(
        api_key=gs.credentials.gemini.kazarinov, generation_config={"response_mime_type": "text/plain"}
    )
    """This model is used for dialog with the user. For processing scenarios, the model defined in the `BotHandler` class is used."""

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
        TelegramBot.__init__(self, self.token)
        # self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_log))
        BotHandler.__init__(self, getattr(self.config, 'webdriver_name', 'firefox'))


def main() -> None:
    """Main function to run the Emil Telegram Bot."""
    parser = argparse.ArgumentParser(description="Run Emil-design Telegram Bot with specified mode.")
    parser.add_argument('-m', '--mode', type=str, default='test', help="Operating mode: 'test' or 'production'")
    parser.add_argument('-d', '--driver', type=str, default='firefox', help=f"""Webdriver Name: 
    'firefox',
    'chrome',
    'edge',
    'playwright',
    'crawlee_python'""")

    args = parser.parse_args()

    emil_bot = EmilTelegramBot(mode=args.mode, webdriver_name=args.webdriver_name)

    app = create_app(emil_bot)
    web.run_app(app)


if __name__ == "__main__":
    main()


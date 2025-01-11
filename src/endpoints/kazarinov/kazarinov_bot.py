# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12
"""
Telegram-бот для проекта Kazarinov
====================================================
Бот взаимодействует
с парсером Mexiron и моделью Google Generative AI, поддерживает обработку текстовых сообщений, документов и URL.

.. module:: src.endpoints.kazarinov.kazarinov_bot
	:platform: Windows, Unix
	:synopsis: KazarinovTelegramBot

"""
import asyncio
from pathlib import Path
from typing import List, Optional, Dict, Self
from types import SimpleNamespace
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

import header
from src import gs
from src.endpoints.bots.telegram.bot_web_hooks import TelegramBot
from src.endpoints.kazarinov.bot_handlers import BotHandler
from src.ai.gemini import GoogleGenerativeAI
from src.utils.url import is_url
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger
from src.fast_api.fast_api import FastApiServer as FastApi


class KazarinovTelegramBot(TelegramBot):
    """Telegram bot with custom behavior for Kazarinov."""

    config: SimpleNamespace = j_loads_ns(gs.path.endpoints / 'kazarinov' / 'kazarinov.json')
    model: GoogleGenerativeAI = GoogleGenerativeAI(
        api_key=gs.credentials.gemini.kazarinov,
        generation_config={"response_mime_type": "text/plain"}
    )
    """Эта модель используется для диалога с пользователем. Для обработки сценариев используется модель, определяемая в классе `BotHandler`"""

    def __init__(self, mode: Optional[str] = None):
        """
        Initialize the KazarinovTelegramBot instance.

        Args:
            mode (Optional[str]): Operating mode, 'test' or 'production'. Defaults to 'test'.
            webdriver_name (Optional[str]): Webdriver to use with BotHandler. Defaults to 'firefox'.
        """
        # Set the mode
        mode = 'prod'
        # Initialize the token based on mode
        token = (
            gs.credentials.telegram.hypo69_test_bot
            if mode == 'test'
            else gs.credentials.telegram.hypo69_kazarinov_bot
        )

        # Initialize the BotHandler
        bot_handler = BotHandler()

        # Call parent initializers
        super().__init__(token=token, 
                         port = self.config.telegram.port,
                         bot_handler=bot_handler)
        


async def main():
    """Main function to run the bot."""
    fast_api = FastApi(title="Kazarinov Bot API")
    bot = KazarinovTelegramBot(fast_api = fast_api)
    config = j_loads_ns(gs.path.endpoints / 'kazarinov' / 'kazarinov.json')
    try:
         await bot.fast_api.start()

    finally:
        if bot:
            try:
                await bot.application.stop()
                await bot.application.bot.delete_webhook()
                logger.info("Bot stopped.")
            except Exception as ex:
                logger.error(f'Error deleting webhook:', ex, False)


if __name__ == "__main__":
    asyncio.run(main())
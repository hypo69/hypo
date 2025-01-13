## \file /src/endpoints/kazarinov/kazarinov_bot.py
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
import os
from pathlib import Path
from typing import List, Optional, Dict, Self
from types import SimpleNamespace
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, BaseHandler
from dotenv import load_dotenv
import header
from src import gs
from src.endpoints.bots.telegram.bot_web_hooks import TelegramBot
from src.endpoints.kazarinov.bot_handlers import BotHandler as KazarinovBotHandler
from src.ai.gemini import GoogleGenerativeAI
from src.utils.url import is_url
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger
from src.fast_api.fast_api import FastApiServer as FastApi


class KazarinovTelegramBot(TelegramBot):
    """Telegram bot with custom behavior for Kazarinov."""

    ENDPOINT:str = 'kazarinov'
    base_path:Path = Path (gs.path.endpoints / ENDPOINT)
    config:SimpleNamespace = j_loads_ns(base_path / f'{ENDPOINT}.json')

    model: GoogleGenerativeAI
    """Эта модель используется для диалога с пользователем через бот телеграм. 
    Для обработки сценариев используются хэндлеры, 
    определенные в классе `KazarinovBotHandler`"""

    def __init__(self, token:str, port:int, route:str=None):
        """
        Initialize the KazarinovTelegramBot instance.

        Args:
            mode (Optional[str]): Operating mode, 'test' or 'production'. Defaults to 'test'.
            webdriver_name (Optional[str]): Webdriver to use with BotHandler. Defaults to 'firefox'.
        """
        load_dotenv()
        token = os.getenv('TELEGRAM_BOT_TOKEN')
        port = int(os.getenv('PORT', 3000))
        # Call parent initializers
        super().__init__(token, port, route)
        self._register_custom_handlers()

        self.model = GoogleGenerativeAI(
        api_key=os.getenv('GEMINI_API'),
        generation_config={"response_mime_type": "text/plain"}
        )

    def _register_custom_handlers(self, custom_handlers:Optional[KazarinovBotHandler] = None):
        """Register or override handlers with custom ones."""
        if custom_handlers:
            if isinstance(custom_handlers, list):
                for handler in custom_handlers:
                     self.application.add_handler(handler)
            else:
                self.application.add_handler(
                   MessageHandler(filters.TEXT & ~filters.COMMAND, custom_handlers.handle_message)
                )


async def main():
    """Main function to run the bot."""
    load_dotenv()
    token:str = os.getenv('TELEGRAM_BOT_TOKEN')
    port:int = int(os.getenv('PORT', 8000))
    route:str = 'kazarinov'
    bot = KazarinovTelegramBot(token = token, port = port, route = route)

    try:
         await bot.initialize_bot()
         await bot.fast_api.start() #Убрали port = int(config.port))
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
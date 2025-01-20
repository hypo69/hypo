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
from pyrogram import Client, filters, idle
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
from dotenv import load_dotenv

import header
from src import gs
from src.endpoints.bots.telegram.bot_web_hooks import TelegramBot
from src.endpoints.kazarinov.bot_handlers import BotHandler as KazarinovBotHandler
from src.ai.gemini import GoogleGenerativeAI


class KazarinovTelegramBot():
    """Telegram bot with custom behavior for Kazarinov."""

    def __init__(self):
        """
        Initialize the KazarinovTelegramBot instance.

        Args:
            mode (Optional[str]): Operating mode, 'test' or 'production'. Defaults to 'firefox'.
        """
        load_dotenv()
        # _____________________ model ______________________
        self.model = GoogleGenerativeAI(
            api_key=os.getenv('GEMINI_API'),
            generation_config={"response_mime_type": "text/plain"}
        )
        # ____________________  route (Fast Api)
        self.route = 'kazarinov'


        self.token = os.getenv('TELEGRAM_BOT_TOKEN')
        
        bot = Client(
        name="Kazarinv bot",
        api_id=os.getenv('TELEGRAM_BOT_TOKEN')
        )

        self._register_custom_handlers()

    def _register_custom_handlers(self):
        """Register or override handlers with custom ones."""
        handler = KazarinovBotHandler()
        self.application.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, handler.handle_message)
        )


if __name__ == "__main__":
    bot = KazarinovTelegramBot() 
    asyncio.run (bot.run())
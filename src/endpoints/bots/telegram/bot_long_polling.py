# -*- coding: utf-8 -*-
# parent_bot.py
import os
from pathlib import Path
import tempfile
import asyncio
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext,  CallbackQueryHandler
from typing import Callable

import header
from src.endpoints.bots.telegram.handlers import BotHandler
from src.logger.logger import logger
import requests  # For downloading files
from src.utils.convertors.tts import speech_recognizer, text2speech
from src.utils.file import read_text_file


class TelegramBot:
    """Telegram bot interface class."""

    application: Application
    handler: BotHandler
    def __init__(self, token: str):
        """Initialize the Telegram bot.

        Args:
            token (str): Telegram bot token, e.g., `gs.credentials.telegram.bot.kazarinov`.
        """
        self.application = Application.builder().token(token).build()
        self.handler = BotHandler() # Инициализация обработчика в конструкторе
        self._original_message_handler = None
        self.register_handlers()


    def register_handlers(self) -> None:
        """Register bot commands and message handlers."""
        self.application.add_handler(CommandHandler('start', self.handler.start))
        self.application.add_handler(CommandHandler('help', self.handler.help_command))
        self.application.add_handler(CommandHandler('sendpdf', self.handler.send_pdf))

        # Сохраняем ссылку
        self._original_message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, self.handler.handle_message)
        self.application.add_handler(self._original_message_handler)

        self.application.add_handler(MessageHandler(filters.VOICE, self.handler.handle_voice))
        self.application.add_handler(MessageHandler(filters.Document.ALL, self.handler.handle_document))
    
    def replace_message_handler(self, new_handler: Callable) -> None:
        """
        Заменяет текущий обработчик текстовых сообщений на новый.

        Args:
            new_handler (Callable): Новая функция для обработки сообщений.
        """
        # 2. Удаляем старый обработчик
        if self._original_message_handler in self.application.handlers[0]:
            self.application.handlers[0].remove(self._original_message_handler)

        # 3. Создаем новый обработчик
        self._original_message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, new_handler)
        # 4. Регистрируем новый обработчик
        self.application.add_handler(self._original_message_handler)



    async def start(self, update: Update, context: CallbackContext) -> None:
        """Handle the /start command."""
        logger.info(f"Bot started by user {update.effective_user.id}")
        await update.message.reply_text('Hello! I am your simple bot. Type /help to see available commands.')
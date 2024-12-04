## \file hypotez/src/bots/telegram/bot.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.bots.telegram 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'dev'

from pathlib import Path
import tempfile
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

import header
from  src import gs
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.logger import logger
import requests  # For downloading files
from src.utils.convertors.tts import speech_recognizer, text2speech
from src.utils.file import read_text_file

class TelegramBot:
    """Telegram bot interface class."""

    application: Application

    def __init__(self, token: str):
        """Initialize the Telegram bot.

        Args:
            token (str): Telegram bot token, e.g., `gs.credentials.telegram.bot.kazarinov`.
        """
        self.application = Application.builder().token(token).build()
        self.register_handlers()

    def register_handlers(self):
        """Register bot commands and message handlers."""
        self.application.add_handler(CommandHandler('start', self.start))
        self.application.add_handler(CommandHandler('help', self.help_command))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
        self.application.add_handler(MessageHandler(filters.VOICE, self.handle_voice))  # Новый обработчик голосовых сообщений
        self.application.add_handler(MessageHandler(filters.Document.ALL, self.handle_document))

    async def start(self, update: Update, context: CallbackContext) -> None:
        """Handle the /start command."""
        await update.message.reply_text('Hello! I am your simple bot. Type /help to see available commands.')

    async def help_command(self, update: Update, context: CallbackContext) -> None:
        """Handle the /help command."""
        await update.message.reply_text(
            'Available commands:\n'
            '/start - Start the bot\n'
            '/help - Show this help message'
        )

    async def handle_voice(self, update: Update, context: CallbackContext) -> None:
        """Handle voice messages and transcribe the audio."""
        try:
            # Получаем файл голосового сообщения
            voice = update.message.voice
            file = await context.bot.get_file(voice.file_id)
            file_path = gs.path.temp / f'{voice.file_id}.ogg'
            
            # Сохраняем файл на локальной системе
            await file.download_to_drive(file_path)

            # Здесь можно добавить обработку файла (распознавание речи), например, с помощью Google Speech-to-Text
            transcribed_text = self.transcribe_voice(file_path)
            
            # Отправляем распознанный текст пользователю
            await update.message.reply_text(f'Распознанный текст: {transcribed_text}')
        
        except Exception as ex:
            logger.error('Ошибка при обработке голосового сообщения: ', ex)
            await update.message.reply_text('Произошла ошибка при обработке голосового сообщения. Попробуй ещё раз.')

    def transcribe_voice(self, file_path: Path) -> str:
        """Transcribe voice message using a speech recognition service."""
        # Пример заглушки, замените это на реальную логику распознавания речи
        return 'Распознавание голоса ещё не реализовано.'

    async def handle_document(self, update: Update, context: CallbackContext) -> str:
        """Handle received documents.

        Args:
            update (Update): Update object containing the message data.
            context (CallbackContext): Context of the current conversation.

        Returns:
            str: Content of the text document.
        """
        file = await update.message.document.get_file()
        tmp_file_path = await file.download_to_drive()  # Save file locally
        return read_text_file(tmp_file_path)

    async def handle_message(self, update: Update, context: CallbackContext) -> str:
        """Handle any text message.

        Args:
            update (Update): Update object containing the message data.
            context (CallbackContext): Context of the current conversation.

        Returns:
            str: Text received from the user.
        """
        return update.message.text

    async def handle_voice(self, update: Update, context: CallbackContext) -> str:
        """Handle voice messages.

        Args:
            update (Update): Update object containing the message data.
            context (CallbackContext): Context of the current conversation.

        Returns:
            str: Recognized text from the voice message.
        """
        voice_file = await update.message.voice.get_file()
        return speech_recognizer(audio_url=voice_file.file_path)

def main() -> None:
    """Start the bot."""
    token = gs.credentials.telegram.bot.kazarinov
    bot = TelegramBot(token)

    # Register command handlers
    bot.application.add_handler(CommandHandler('start', bot.start))
    bot.application.add_handler(CommandHandler('help', bot.help_command))

    # Register message handlers
    bot.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, bot.handle_message))
    bot.application.add_handler(MessageHandler(filters.VOICE, bot.handle_voice))
    bot.application.add_handler(MessageHandler(filters.Document.ALL, bot.handle_document))

    # Start the bot
    bot.application.run_polling()

if __name__ == '__main__':
    main()

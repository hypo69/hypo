from pathlib import Path
import tempfile
import asyncio
import logging
import json
import requests  # For downloading files
from typing import Dict
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from aiohttp import web
from aiogram.webhook.aiohttp_server import setup_application

import header
from src import gs
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.logger.logger import logger
from src.utils.convertors.tts import speech_recognizer, text2speech
from src.utils.file import read_text_file
from src.utils.get_free_port import get_free_port


class TelegramBot:
    """Telegram bot interface class."""

    application: Application
    host: str
    port: int

    def __init__(self, token: str, config_path: Path):
        """Initialize the Telegram bot.

        :param token: Telegram bot token, e.g., `gs.credentials.telegram.bot.kazarinov`.
        :type token: str
        :param config_path: Path to the JSON configuration file.
        :type config_path: Path
        """
        config_path = config_path if config_path else Path(__file__).parent / 'config.json'
        self._load_config()
        self.application = Application.builder().token(token).build()
        self.register_handlers()


    def _load_config(self, config_path:str | Path) -> None:
        """Load configuration from JSON file."""
        try:
            with open(self.config_path, 'r') as f:
                config = json.load(f)
                bot_config = config.get(self.__class__.__name__, {})
                if bot_config:
                    self.host = bot_config.get('host', '127.0.0.1')
                    port_range = bot_config.get('port_range', ['9000','9100'])
                    self.port = get_free_port(self.host, port_range)
                else:
                    logger.error(f'No config found for {self.__class__.__name__}')
                    self.host = '127.0.0.1'
                    self.port =  get_free_port(self.host,['9000','9100'])

        except FileNotFoundError as ex:
            logger.error('Error: Configuration file not found: ', ex)
            self.host = '127.0.0.1'
            self.port = 8080
            ...
        except json.JSONDecodeError as ex:
             logger.error('Error: Invalid JSON format in configuration file: ', ex)
             self.host = '127.0.0.1'
             self.port = 8080
             ...

    def register_handlers(self):
        """Register bot commands and message handlers."""
        self.application.add_handler(CommandHandler('start', self.start))
        self.application.add_handler(CommandHandler('help', self.help_command))
        self.application.add_handler(CommandHandler('sendpdf', self.send_pdf))  # обработчик для отправки PDF
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
        self.application.add_handler(MessageHandler(filters.VOICE, self.handle_voice))
        self.application.add_handler(MessageHandler(filters.Document.ALL, self.handle_document))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_log))

    async def start(self, update: Update, context: CallbackContext) -> None:
        """Handle the /start command."""
        self.update = update
        self.context = context
        await self.update.message.reply_text('Hello! I am your simple bot. Type /help to see available commands.')

    async def help_command(self, update: Update, context: CallbackContext) -> None:
        """Handle the /help command."""
        self.update = update
        self.context = context
        await self.update.message.reply_text(
            'Available commands:\n'
            '/start - Start the bot\n'
            '/help - Show this help message\n'
            '/sendpdf - Send a PDF file'
        )

    async def send_pdf(self, pdf_file: str | Path) -> None:
        """Handle the /sendpdf command to generate and send a PDF file."""
        try:
            # Отправка PDF-файла пользователю
            with open(pdf_file, 'rb') as pdf_file_obj:
                await self.update.message.reply_document(document=pdf_file_obj)

        except Exception as ex:
            logger.error('Ошибка при отправке PDF-файла: ', ex)
            await self.update.message.reply_text('Произошла ошибка при отправке PDF-файла. Попробуй ещё раз.')

    async def handle_voice(self, update: Update, context: CallbackContext) -> None:
        """Handle voice messages and transcribe the audio."""
        self.update = update
        self.context = context
        try:
            # Получаем файл голосового сообщения
            voice = self.update.message.voice
            file = await self.context.bot.get_file(voice.file_id)
            file_path = gs.path.temp / f'{voice.file_id}.ogg'
            
            # Сохраняем файл на локальной системе
            await file.download_to_drive(file_path)

            # Здесь можно добавить обработку файла (распознавание речи), например, с помощью Google Speech-to-Text
            transcribed_text = self.transcribe_voice(file_path)
            
            # Отправляем распознанный текст пользователю
            await self.update.message.reply_text(f'Распознанный текст: {transcribed_text}')
        
        except Exception as ex:
            logger.error('Ошибка при обработке голосового сообщения: ', ex)
            await self.update.message.reply_text('Произошла ошибка при обработке голосового сообщения. Попробуй ещё раз.')

    async def transcribe_voice(self, file_path: Path) -> str:
        """Transcribe voice message using a speech recognition service."""
        # Пример заглушки, замените это на реальную логику распознавания речи
        return 'Распознавание голоса ещё не реализовано.'

    async def handle_document(self, update: Update, context: CallbackContext) -> str:
        """Handle received documents.

        :param update: Update object containing the message data.
        :type update: Update
        :param context: Context of the current conversation.
        :type context: CallbackContext
        :return: Content of the text document.
        :rtype: str
        """
        self.update = update
        self.context = context
        file = await self.update.message.document.get_file()
        tmp_file_path = await file.download_to_drive()  # Save file locally
        return read_text_file(tmp_file_path)

    async def handle_message(self, update: Update, context: CallbackContext) -> str:
        """Handle any text message.

        :param update: Update object containing the message data.
        :type update: Update
        :param context: Context of the current conversation.
        :type context: CallbackContext
        :return: Text received from the user.
        :rtype: str
        """
        self.update = update
        self.context = context
        return self.update.message.text

    async def handle_log(self, update: Update, context: CallbackContext) -> None:
        """Handle log messages."""
        log_message = update.message.text
        logger.info(f"Received log message: {log_message}")
        await update.message.reply_text("Log received and processed.")

async def on_startup(app: web.Application):
    """Perform actions on application startup."""
    bot = app['bot']
    await bot.application.bot.set_webhook(url=gs.settings.get_webhook_url)
    logger.info("Bot started with webhook.")

async def on_shutdown(app: web.Application):
    """Perform actions on application shutdown."""
    bot = app['bot']
    await bot.application.bot.delete_webhook()
    logger.info("Bot stopped.")

def create_app(bot: TelegramBot) -> web.Application:
    """Create and configure the aiohttp application."""
    app = web.Application()
    app['bot'] = bot

    # Register webhook handler
    app.router.add_post(f'/{gs.credentials.telegram.bot.kazarinov}', bot.application.update_webhook)

    # Register startup and shutdown handlers
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    # Setup application with the bot
    setup_application(app, bot.application)

    return app

def main() -> None:
    """Start the bot with webhook."""
    token = gs.credentials.telegram.bot.kazarinov
    config_path = Path(__file__).parent / 'config.json'
    bot = TelegramBot(token, config_path)

    # Create and run the aiohttp application
    app = create_app(bot)
    web.run_app(app, host=bot.host, port=bot.port)

if __name__ == '__main__':
    main()
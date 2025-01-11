from pathlib import Path
import asyncio
import json
import socket
import os
from types import SimpleNamespace
from typing import Optional
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from fastapi import Request, Response

import header
from src import gs
from src.fast_api.fast_api import FastApiServer as FastApi  # Explicit import of custom FastApi
from src.endpoints.bots.telegram.bot_handlers import BotHandler
from src.logger.logger import logger
from src.utils.get_free_port import get_free_port
from uvicorn import Config, Server

from src.utils.jjson import j_loads_ns


class TelegramBot:
    """Telegram bot interface class."""

    application: Application
    webhook_url: str
    bot_handler: BotHandler
    config: SimpleNamespace
    fast_api: FastApi

    def __init__(self,
                 token: str,
                 port: int,
                 webhook_url: Optional[str] = None,
                 bot_handler: Optional[BotHandler] = None,
                 fast_api: FastApi = None):
        """Initialize the Telegram bot."""
        self.config = j_loads_ns(gs.path.endpoints / 'bots' / 'telegram' / 'telegram.json')

        self.application = Application.builder().token(token).build()
        self.bot_handler = bot_handler if bot_handler else BotHandler()
        self.webhook_url = webhook_url if webhook_url else '/telegram_webhook'
        self._register_handlers()
        
        #Pass the fast_api instance instead of creating it here.
        self.fast_api = fast_api
        asyncio.create_task(self.fast_api.run(port=port))



    def _register_handlers(self):
        """Register bot commands and message handlers."""
        self.application.add_handler(CommandHandler('start', self.bot_handler.start))
        self.application.add_handler(CommandHandler('help', self.bot_handler.help_command))
        self.application.add_handler(CommandHandler('sendpdf', self.bot_handler.send_pdf))
        self.application.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, self._handle_message)
        )
        self.application.add_handler(MessageHandler(filters.VOICE, self.bot_handler.handle_voice))
        self.application.add_handler(MessageHandler(filters.Document.ALL, self.bot_handler.handle_document))
        self.application.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, self.bot_handler.handle_log)
        )


    async def _handle_message(self, update: Update, context: CallbackContext) -> None:
        """Handle any text message."""
        await self.bot_handler.handle_message(update, context)





async def telegram_webhook(request: Request):
    """Handle incoming webhook requests."""
    if not bot_instance:
        logger.error("Bot not initialized.")
        return Response(status_code=500, content="Bot not initialized.")

    try:
        data = await request.json()
        async with bot_instance.application:
            await bot_instance.application.process_update(
                Update.de_json(data, bot_instance.application.bot)
            )
        return Response(status_code=200)
    except Exception as e:
        logger.error(f'Error processing webhook: {e}')
        return Response(status_code=500, content=f'Error processing webhook: {e}')


async def initialize_bot(token: str, port: int):
    """Initialize the bot instance."""
    global bot_instance
    if not bot_instance:
        bot_instance = TelegramBot(token, port=port, fast_api=app)  # Passing app to the constructor
        try:
            await bot_instance.application.bot.set_webhook(
                url=bot_instance.webhook_url
            )
            logger.info(f"Bot started with webhook: {bot_instance.webhook_url}")
        except Exception as ex:
            logger.error(f'Error setting webhook: {ex}')
        
        if not bot_instance.webhook_url:
            asyncio.create_task(bot_instance.application.start_polling()) #Start polling if webhook is not set

app = FastApi(title="Telegram Bot API")
@app.on_event("startup")
async def startup_event():
    """Startup event handler."""
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    port = int(os.getenv('PORT', 8000))
    await initialize_bot(token, port)


@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown event handler."""
    if bot_instance:
        try:
            await bot_instance.application.bot.delete_webhook()
            logger.info("Bot stopped.")
        except Exception as ex:
            logger.error(f'Error deleting webhook: {ex}')



if __name__ == "__main__":
    # FastAPI App Creation
    
    bot_instance: Optional[TelegramBot] = None
    # Handle Webhook
    app.add_route("/telegram_webhook", telegram_webhook, methods=["POST"])
    app.register_router()
    app.run()
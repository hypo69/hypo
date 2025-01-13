from pathlib import Path
import asyncio
import json
import os
import sys
from types import SimpleNamespace
from typing import Optional, List, Union
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, BaseHandler
from fastapi import Request, Response

import header
from src import gs
from src.fast_api.fast_api import FastApiServer as FastApi  # Explicit import of custom FastApi
from src.endpoints.bots.telegram.bot_handlers import BotHandler
from src.logger.logger import logger

from src.utils.jjson import j_loads_ns


class TelegramBot():
    """Telegram bot interface class, now a Singleton."""

    ENDPOINT = 'bots/telegram'
    base_path: Path = gs.path.endpoints / ENDPOINT
    config: SimpleNamespace = j_loads_ns(base_path / 'telegram.json')
    if not config:
        logger.error(f"Файл конфигурации не найден! {base_path=}")
        raise FileNotFoundError(f"Конфигурационный файл не найден: {base_path}")

    application: Application
    webhook_url: str = config.webhook
    bot_handler: BotHandler

    fast_api: FastApi
    fast_api_task: asyncio.Task

    def __init__(self,
                 token: str,
                 port: int,
                 route:str = None
                 ):
        
   
        self.fast_api = FastApi(title="Telegram Bot API", )
        try:
            self.fast_api.start(port=int(port))
        except Exception as ex:
            logger.error(f"Ошибка FastApiServer",ex)
            sys.exit()

        if route: 
            app.add_route(f"/{route}", telegram_webhook, methods=["POST"])

        self.application = Application.builder().token(token).build()

        self._register_default_handlers(BotHandler())
        asyncio.run(self.initialize_bot()) #Запускаем корутину инициализации
       


    def _register_default_handlers(self, bot_handler:BotHandler):
        """Register the default handlers using the BotHandler instance."""
        self.bot_handler = bot_handler #Сохраняем bot_handler переданный в конструктор
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


    async def initialize_bot(self):
        """Initialize the bot instance."""
        try:
            await self.application.bot.set_webhook(
                url=self.webhook_url
            )
            logger.info(f"Bot started with webhook: {self.webhook_url}")
        except Exception as ex:
            logger.error('Error setting webhook:', ex) # Исправили вывод ошибки
        if not self.webhook_url:
          asyncio.create_task(self.application.start_polling())


async def telegram_webhook(request: Request):
    """Handle incoming webhook requests."""
    bot_instance = TelegramBot()
    try:
        data = await request.json()
        async with bot_instance.application:
            update = Update.de_json(data, bot_instance.application.bot)
            await bot_instance.application.process_update(update)
        return Response(status_code=200)
    except json.JSONDecodeError as e:
        logger.error(f'Error decoding JSON: {e}')
        return Response(status_code=400, content=f'Invalid JSON: {e}')
    except Exception as e:
        logger.error(f'Error processing webhook: {type(e)} - {e}')
        return Response(status_code=500, content=f'Error processing webhook: {e}')


async def stop_bot(bot_instance: TelegramBot):
    if bot_instance:
        # Cancel the task for the fast api when the program stops
        if hasattr(bot_instance, 'fast_api_task') and bot_instance.fast_api_task:
            bot_instance.fast_api_task.cancel()
            try:
                await bot_instance.fast_api_task  # Wait until the fast api closes
            except asyncio.CancelledError:
                pass
        try:
            await bot_instance.application.bot.delete_webhook()
            logger.info("Bot stopped.")
        except Exception as ex:
            logger.error(f'Error deleting webhook: {ex}')

# FastAPI App Creation
app = FastApi(title="Telegram Bot API")

@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown event handler."""
    bot_instance = TelegramBot()
    await stop_bot(bot_instance)


# Handle Webhook
# app.add_route("/kazarinov", telegram_webhook, methods=["POST"]) #Убрали
if __name__ == "__main__":
    app.run()
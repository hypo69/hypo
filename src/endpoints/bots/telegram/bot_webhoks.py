## \file /src/endpoints/bots/telegram/telegram_webhooks.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3
"""
Телеграм бот через сервер FastAPI через RPC
====================================================

.. module:: src.endpoints.bots.telegram.telegram_webhooks
    :platform: Windows, Unix
    :synopsis: Телеграм бот с сервером FAST API Через RPC

"""
from pathlib import Path
import asyncio
import json
import sys
from types import SimpleNamespace
from typing import Optional
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from xmlrpc.client import ServerProxy
from fastapi import FastAPI, Request, Response
import socket
import os

import header
from header import __root__
from src import gs
from src.endpoints.bots.telegram.handlers import BotHandler
from src.utils.printer import pprint as print
from src.logger.logger import logger

from src.utils.jjson import j_loads_ns


class TelegramBot:
    """Telegram bot interface class, now a Singleton."""

    def __init__(self, token: str, route: str = 'telegram_webhook'):
        """
        Initialize the TelegramBot instance.

        Args:
            token (str): Telegram bot token.
            route (str): Webhook route for FastAPI. Defaults to '/telegram_webhook'.
        """
        self.token: str = token
        self.port: int = 443
        self.route: str = route
        self.config: SimpleNamespace = j_loads_ns(__root__ / 'src/endpoints/bots/telegram/telegram.json')
        self.application: Application = Application.builder().token(self.token).build()
        self.handler: BotHandler = BotHandler()
        self._register_default_handlers()

    def run(self):
        """Run the bot and initialize RPC and webhook."""
        try:
            # Initialize RPC client
            rpc_client = ServerProxy(f"http://{gs.host}:9000", allow_none=True)

            # Start the server via RPC
            rpc_client.start_server(self.port, gs.host)

            # Register the route via RPC
            # Динамическое добавление маршрутов
            

            logger.success(f'Server running at http://{gs.host}:{self.port}/hello')
        except Exception as ex:
            logger.error(f"Ошибка FastApiServer: {ex}", exc_info=True)
            sys.exit()




        # Initialize the Telegram bot webhook
        webhook_url = self.initialize_bot_webhook(self.route)
        # 
        if webhook_url:
            self._register_route_via_rpc(rpc_client)
            try:
                self.application.run_webhook(listen='0.0.0.0',
                                                         webhook_url=webhook_url, 
                                                         port=self.port)
                
                logger.info(f"Application started: {self.application.bot_data}")
                ...

            except Exception as ex:
                logger.error(f"Ошибка установки вебхука")
                ...

            ...
        else:
            self.application.run_polling()
            ...


    def _register_default_handlers(self):
        """Register the default handlers using the BotHandler instance."""
        self.application.add_handler(CommandHandler('start', self.handler.start))
        self.application.add_handler(CommandHandler('help', self.handler.help_command))
        self.application.add_handler(CommandHandler('sendpdf', self.handler.send_pdf))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self._handle_message))
        self.application.add_handler(MessageHandler(filters.VOICE, self.handler.handle_voice))
        self.application.add_handler(MessageHandler(filters.Document.ALL, self.handler.handle_document))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handler.handle_log))

    async def _handle_message(self, update: Update, context: CallbackContext) -> None:
        """Handle any text message."""
        await self.bot_handler.handle_message(update, context)

    def initialize_bot_webhook(self, route: str):
        """Initialize the bot webhook."""
        route = route if route.startswith('/') else f'/{route}'
        host = gs.host

        if host in ('127.0.0.1', 'localhost'):
            from pyngrok import ngrok
            ngrok.set_auth_token(os.getenv("NGROK_AUTH_TOKEN", ""))
            http_tunnel = ngrok.connect(self.port)
            host = http_tunnel.public_url

        host = host if host.startswith('http') else f'https://{host}'
        webhook_url = f'{host}{route}'

        _dev = True
        if _dev:
            import requests
            response = requests.post(f'{webhook_url}')
            print(response.json, text_color='green', bg_color='gray')

        try:
            self.application.bot.set_webhook(url=webhook_url)
            logger.success(f'https://api.telegram.org/bot{self.token}/getWebhookInfo') 
            return webhook_url
        except Exception as ex:
            logger.error(f'Error setting webhook: ',ex, exc_info=True)
            return False

    def _register_route_via_rpc(self, rpc_client: ServerProxy):
        """Register the Telegram webhook route via RPC."""
        try:
            # Регистрация маршрута через RPC
            route = self.route if self.route.startswith('/') else f'/{self.route}'
            rpc_client.add_new_route(
                route,
                'self.bot_handler.handle_message',
                ['POST']
            )

            logger.info(f"Route {self.route} registered via RPC.")
        except Exception as ex:
            logger.error(f"Failed to register route via RPC:",ex, exc_info=True)
            ...

    def stop(self):
        """Stop the bot and delete the webhook."""
        try:
            self.application.stop()
            self.application.bot.delete_webhook()
            logger.info("Bot stopped.")
        except Exception as ex:
            logger.error(f'Error deleting webhook:',ex, exc_info=True)


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    bot = TelegramBot(os.getenv('TELEGRAM_TOKEN'))
    bot.run()
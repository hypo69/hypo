# -*- coding: utf-8 -*-
#! .pyenv/bin/python3
"""
Телеграм бот через сервер FastAPI через RPC
====================================================

.. module:: src.endpoints.bots.telegram.telegram_webhooks
    :platform: Windows, Unix
    :synopsis: Телеграм бот с сервером FAST API Через RPC

"""
import asyncio
import sys
from types import SimpleNamespace
from typing import Optional

import os

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web
from xmlrpc.client import ServerProxy

import header
from header import __root__
from src import gs
from src.endpoints.bots.telegram.bot_handlers import BotHandler
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
        self.bot: Bot = Bot(token=self.token)
        self.dp: Dispatcher = Dispatcher()
        self.bot_handler: BotHandler = BotHandler()
        self._register_default_handlers()
        self.app: Optional[web.Application] = None
        self.rpc_client: Optional[ServerProxy] = None  # Add rpc_client as an attribute

    def run(self):
        """Run the bot and initialize RPC and webhook."""
        try:
            # Initialize RPC client
            
            port = 9000

            self.rpc_client = ServerProxy(f"http://{gs.host}:{port}", allow_none=True) 

            # Start the server via RPC
            self.rpc_client.start_server(port, gs.host)

            # Register the route via RPC
            logger.success(f'RPC Server running at http://{gs.host}:{port}/')
        except Exception as ex:
            logger.error(f"Ошибка FastApiServer: ",ex, exc_info=True)
            sys.exit()

        # Initialize the Telegram bot webhook
        webhook_url = self.initialize_bot_webhook(self.route)
       
        if webhook_url:
            self._register_route_via_rpc(self.rpc_client)
            try:
                # Use web application for webhook
                self.app = web.Application()
                webhook_requests_handler = SimpleRequestHandler(
                    dispatcher=self.dp,
                    bot=self.bot,
                )

                webhook_requests_handler.register(self.app, path=self.route)
                setup_application(self.app, self.dp, bot=self.bot)
                web.run_app(self.app, host="0.0.0.0", port=self.port)
                logger.info(f"Application started: {self.bot.id}")

            except Exception as ex:
                logger.error(f"Ошибка установки вебхука: ", ex, exc_info=True)

        else:
            asyncio.run(self.dp.start_polling(self.bot))

    def _register_default_handlers(self):
        """Register the default handlers using the BotHandler instance."""
        self.dp.message.register(self.bot_handler.start, Command('start'))
        self.dp.message.register(self.bot_handler.help_command, Command('help'))
        self.dp.message.register(self.bot_handler.send_pdf, Command('sendpdf'))
        self.dp.message.register(self._handle_message)
        self.dp.message.register(self.bot_handler.handle_voice, lambda message: message.voice is not None)
        self.dp.message.register(self.bot_handler.handle_document, lambda message: message.document is not None)
        self.dp.message.register(self.bot_handler.handle_log, lambda message: message.text is not None)

    async def _handle_message(self, message: types.Message):
        """Handle any text message."""
        await self.bot_handler.handle_message(message)

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

        try:
            asyncio.run(self.bot.set_webhook(url=webhook_url))
            logger.success(f'https://api.telegram.org/bot{self.token}/getWebhookInfo')
            return webhook_url
        except Exception as ex:
            logger.error(f'Error setting webhook: ',ex, exc_info=True)
            return False

    def _register_route_via_rpc(self, rpc_client: ServerProxy):
        """Register the Telegram webhook route via RPC."""
        try:
            route = self.route if self.route.startswith('/') else f'/{self.route}'
            rpc_client.add_new_route(
                route,
                'self.bot_handler.handle_message',
                ['POST']
            )
            logger.info(f"Route {self.route} registered via RPC.")
        except Exception as ex:
            logger.error(f"Failed to register route via RPC:",ex, exc_info=True)

    def stop(self):
         """Stop the bot and delete the webhook."""
         if self.app:
            asyncio.run(self.app.shutdown())
            asyncio.run(self.app.cleanup())
         try:
            asyncio.run(self.bot.delete_webhook())
            logger.info("Bot stopped.")
         except Exception as ex:
            logger.error(f'Error deleting webhook:',ex, exc_info=True)


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    bot = TelegramBot(os.getenv('TELEGRAM_TOKEN'))
    bot.run()
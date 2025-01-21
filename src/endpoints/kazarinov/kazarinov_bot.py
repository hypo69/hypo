# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12
"""
Telegram-бот для проекта Kazarinov
====================================================
Бот взаимодействует с парсером Mexiron и моделью Google Generative AI, 
поддерживает обработку текстовых сообщений, документов и URL.

.. module:: src.endpoints.kazarinov.kazarinov_bot
   :platform: Windows, Unix
   :synopsis: KazarinovTelegramBot
"""

import asyncio
import os
from typing import Optional
from dotenv import load_dotenv
from pyrogram import Client, filters, idle
from pyrogram.types import Message
import httpx
import header  # Формирование путей проекта

from src.endpoints.kazarinov.bot_handlers import BotHandler as KazarinovBotHandler


class HTTPClientManager:
    """Управление HTTP-клиентом."""

    def __init__(self):
        self._client: Optional[httpx.AsyncClient] = None

    def get_client(self) -> httpx.AsyncClient:
        """Возвращает экземпляр HTTP-клиента."""
        if self._client is None:
            self._client = httpx.AsyncClient()
        return self._client

    async def close_client(self):
        """Закрывает HTTP-клиент."""
        if self._client:
            await self._client.aclose()
            self._client = None


class Singleton(type):
    """Реализация Singleton для Telegram-бота."""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class KazarinovTelegramBot(metaclass=Singleton):
    """Telegram-бот для проекта Kazarinov."""

    def __init__(self):
        """Инициализация бота."""
        if hasattr(self, '_initialized'):
            return

        load_dotenv()
        self.http_client_manager = HTTPClientManager()


        self.route = 'kazarinov'
        self.token = os.getenv('TELEGRAM_BOT_TOKEN')

        # Настройка клиента Pyrogram
        self.app = Client(
            name="hypo69",
            # api_id=int(os.getenv('TELEGRAM_API_ID')),
            # api_hash=os.getenv('TELEGRAM_API_HASH'),
            bot_token=self.token
        )
                                                        
        self._initialized = True

    def _register_handlers(self):
        """Регистрация пользовательских обработчиков."""
        handler = KazarinovBotHandler()
        self.app.add_handler(
            filters.text & ~filters.command(r'^/'),
            handler.handle_message
        )

    async def run(self):
        """Запуск Telegram-бота."""
        await self.app.start()
        self._register_handlers()
        print("Bot started")
        await idle()  # Поддерживает бота активным до остановки
        print("Bot stopped")
        await self.app.stop()
        await self.http_client_manager.close_client()


if __name__ == "__main__":
    bot = KazarinovTelegramBot()
    asyncio.run(bot.run())
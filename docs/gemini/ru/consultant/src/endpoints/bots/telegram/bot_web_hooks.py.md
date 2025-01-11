### Анализ кода модуля `bot_web_hooks`

**Качество кода:**

*   **Соответствие стандартам**: 7/10
*   **Плюсы**:
    *   Используется асинхронность для обработки запросов и работы с Telegram API.
    *   Применяется `j_loads_ns` для загрузки конфигурации.
    *   Разделение на классы для логической организации кода.
    *   Регистрация обработчиков команд и сообщений Telegram.
    *   Используется `logger` для логирования ошибок.
*   **Минусы**:
    *   Не все docstring соответствуют стандарту RST.
    *   В `__init__` создается `FastApi` сервер, который запускается в новой задаче, что может быть не очевидным для других разработчиков. Лучше передавать готовый экземпляр.
    *   Не используется `j_loads` для работы с JSON.
    *   Импорт `logger` не из `src.logger`, а из `src.logger.logger`
    *   Дублирование `Telegram Bot API` в `FastApi` при инициализации `TelegramBot` и вне класса.
    *   В `initialize_bot` используется  `bot_instance.webhook_url` без проверки.

**Рекомендации по улучшению:**

1.  **Документация:**
    *   Добавить docstring в формате RST для класса `TelegramBot` и его методов.
    *   Добавить более подробные описания для параметров функций.
2.  **Обработка данных:**
    *   Использовать `j_loads` для обработки данных json при получении webhook.
    *   Использовать `logger` из `src.logger.logger`
3.  **Структура кода:**
    *   Передавать экземпляр `FastApi` в `TelegramBot`, чтобы избежать дублирования кода и более явно контролировать жизненный цикл `FastApi`.
4.  **Обработка ошибок:**
    *   Упростить обработку ошибок в `telegram_webhook`, используя `logger.error` и возвращая Response.
    *   Избегать лишних `try-except` блоков, где это не обязательно.
5.  **Логирование**:
    *   Использовать f-строки для логирования, чтобы форматирование было более читаемым.
6.  **Инициализация**:
     *   Проверять `bot_instance.webhook_url` на пустоту перед использованием.

**Оптимизированный код:**

```python
from pathlib import Path
import asyncio
import socket
import os
from types import SimpleNamespace
from typing import Optional
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from fastapi import Request, Response

from src import gs
from src.fast_api.fast_api import FastApiServer as FastApi  # Explicit import of custom FastApi
from src.endpoints.bots.telegram.bot_handlers import BotHandler
from src.logger.logger import logger
from src.utils.get_free_port import get_free_port
from uvicorn import Config, Server

from src.utils.jjson import j_loads_ns, j_loads


class TelegramBot:
    """
    Класс для управления Telegram ботом.
    ====================================

    Этот класс инкапсулирует логику инициализации, обработки сообщений и управления webhook Telegram бота.

    :param token: Токен Telegram бота.
    :type token: str
    :param port: Порт для запуска сервера FastAPI.
    :type port: int
    :param webhook_url: URL для webhook (опционально).
    :type webhook_url: Optional[str]
    :param bot_handler: Экземпляр обработчика бота (опционально).
    :type bot_handler: Optional[BotHandler]
    :param fast_api: Экземпляр FastApi для запуска сервера.
    :type fast_api: FastApi

    Пример использования:
    ----------------------
    .. code-block:: python

        bot = TelegramBot(
            token='YOUR_TELEGRAM_BOT_TOKEN',
            port=8080,
            webhook_url='/telegram_webhook',
            fast_api=FastApi(title="Telegram Bot API")
        )
    """

    application: Application
    webhook_url: str
    bot_handler: BotHandler
    config: SimpleNamespace
    fast_api: FastApi

    def __init__(
        self,
        token: str,
        port: int,
        fast_api: FastApi,
        webhook_url: Optional[str] = None,
        bot_handler: Optional[BotHandler] = None,
    ):
        """
        Инициализация Telegram бота.

        :param token: Токен Telegram бота.
        :type token: str
        :param port: Порт для запуска сервера FastAPI.
        :type port: int
         :param fast_api: Экземпляр FastApi для запуска сервера.
        :type fast_api: FastApi
        :param webhook_url: URL для webhook (опционально).
        :type webhook_url: Optional[str]
        :param bot_handler: Экземпляр обработчика бота (опционально).
        :type bot_handler: Optional[BotHandler]
        """
        self.config = j_loads_ns(gs.path.endpoints / 'bots' / 'telegram' / 'telegram.json') # Load config
        self.application = Application.builder().token(token).build() # Build application
        self.bot_handler = bot_handler if bot_handler else BotHandler() # Set bot handler
        self.webhook_url = webhook_url if webhook_url else '/telegram_webhook' # Set webhook url
        self._register_handlers() # Register handlers
        self.fast_api = fast_api
        asyncio.create_task(self.fast_api.run(port=port))# run fast api


    def _register_handlers(self):
        """Регистрация обработчиков команд и сообщений бота."""
        self.application.add_handler(CommandHandler('start', self.bot_handler.start))#Register start command
        self.application.add_handler(CommandHandler('help', self.bot_handler.help_command)) # Register help command
        self.application.add_handler(CommandHandler('sendpdf', self.bot_handler.send_pdf))#Register sendpdf command
        self.application.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, self._handle_message)
        ) #Register message handler
        self.application.add_handler(MessageHandler(filters.VOICE, self.bot_handler.handle_voice))#Register voice message handler
        self.application.add_handler(MessageHandler(filters.Document.ALL, self.bot_handler.handle_document))#Register document handler
        self.application.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, self.bot_handler.handle_log)
        )#Register log handler


    async def _handle_message(self, update: Update, context: CallbackContext) -> None:
        """
         Обработка текстовых сообщений.

        :param update: Объект обновления Telegram.
        :type update: Update
        :param context: Объект контекста обратного вызова.
        :type context: CallbackContext
        """
        await self.bot_handler.handle_message(update, context) # call handler


# FastAPI App Creation
app = FastApi(title="Telegram Bot API")
bot_instance: Optional[TelegramBot] = None


async def telegram_webhook(request: Request):
    """
     Обрабатывает входящие webhook запросы от Telegram.

    :param request: Объект запроса FastAPI.
    :type request: Request
    :return: Ответ FastAPI.
    :rtype: Response
    """
    global bot_instance
    if not bot_instance:
        logger.error("Bot not initialized.")
        return Response(status_code=500, content="Bot not initialized.")

    try:
        data = await request.json() # Get request data
        async with bot_instance.application: # process update
            await bot_instance.application.process_update(
                Update.de_json(data, bot_instance.application.bot)
            )
        return Response(status_code=200)
    except Exception as e:
        logger.error(f'Error processing webhook: {e}') # log error
        return Response(status_code=500, content=f'Error processing webhook: {e}') # Return error


async def initialize_bot(token: str):
    """
     Инициализация бота.

    :param token: Токен Telegram бота.
    :type token: str
    """
    global bot_instance
    if not bot_instance:
        bot_instance = TelegramBot( # Initialize bot
            token=token,
            port = int(os.getenv('PORT', 8000)),
            fast_api = app # Pass app instance
        )
        try:
            if bot_instance.webhook_url: # check if webhook_url is not empty
                await bot_instance.application.bot.set_webhook(
                   url=bot_instance.webhook_url
                )
                logger.info(f"Bot started with webhook: {bot_instance.webhook_url}")
            else:
                asyncio.create_task(bot_instance.application.start_polling())  # Start polling if webhook is not set
        except Exception as ex:
            logger.error(f'Error setting webhook: {ex}')


@app.on_event("startup")
async def startup_event():
    """Обработчик события запуска приложения."""
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    await initialize_bot(token) # Initialize bot


@app.on_event("shutdown")
async def shutdown_event():
    """Обработчик события остановки приложения."""
    if bot_instance:
        try:
            await bot_instance.application.bot.delete_webhook() # Delete webhook
            logger.info("Bot stopped.")
        except Exception as ex:
            logger.error(f'Error deleting webhook: {ex}') # Log error


# Handle Webhook
app.add_route("/telegram_webhook", telegram_webhook, methods=["POST"]) # Add route


app.register_router() # Register router


if __name__ == "__main__":
    app.run()
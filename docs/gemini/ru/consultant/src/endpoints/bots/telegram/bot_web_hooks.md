# Анализ кода модуля `bot_web_hooks`

## Качество кода:
- **Соответствие стандартам**: 7
- **Плюсы**:
    - Код имеет четкую структуру и разделение на классы и функции.
    - Используются асинхронные функции для неблокирующих операций.
    - Присутствует обработка основных команд и типов сообщений Telegram.
    - Документирование кода на хорошем уровне.
- **Минусы**:
    - Используется стандартный `json.load` вместо `j_loads`.
    - Присутствуют неявные импорты, которые требуют уточнения.
    - Обработка ошибок может быть улучшена путем добавления логирования с помощью `logger.error` и отказа от `try-except` в некоторых случаях.
    - Не хватает RST-документации для классов и методов.
    - Следует использовать `from src.logger.logger import logger`.
    - Некоторые переменные не соответствуют PEP8 (например, `fast_api`).

## Рекомендации по улучшению:
- Заменить `json.load` на `j_loads` из `src.utils.jjson`.
- Добавить импорт `logger` из `src.logger.logger`.
- Добавить RST-документацию для класса `TelegramBot` и его методов.
- Заменить `try-except` на `logger.error` для отлова ошибок в `telegram_webhook`.
- Привести имена переменных в соответствие с PEP8 (например, `fast_api` на `fast_api_instance`).
- Явно прописать все импорты.
- Добавить type hints там где они отсутствуют.

## Оптимизированный код:
```python
"""
Модуль для обработки Telegram-бота через вебхуки.
==================================================
Модуль содержит класс `TelegramBot`, который обеспечивает интеграцию Telegram-бота
с FastAPI для обработки обновлений через вебхуки или через пуллинг.

Основные компоненты:
- Класс :class:`TelegramBot`: Для управления логикой бота.
- Функция :func:`telegram_webhook`: Для обработки входящих вебхуков от Telegram.
- Функция :func:`initialize_bot`: Для инициализации и запуска бота.
- Интеграция с FastAPI для обработки вебхуков.
"""
import os
from typing import Optional

from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import (
    Application,
    CallbackContext,
    CommandHandler,
    MessageHandler,
    filters,
)

from src.fast_api.fast_api import FastApi  # импорт класса FastApi
from src.logger.logger import logger  # импорт logger
from src.utils.jjson import j_loads_ns  # импорт j_loads_ns
from src.endpoints.bots.telegram.bot_handlers import BotHandler  # импорт BotHandler


bot_instance = None


class TelegramBot:
    """
    Класс для управления Telegram ботом и его интеграцией с FastAPI.

    :param token: Токен Telegram бота.
    :type token: str
    :param port: Порт для FastAPI сервера.
    :type port: int
    :param webhook_url: URL для вебхука Telegram.
    :type webhook_url: Optional[str]
    :param bot_handler: Обработчик сообщений бота.
    :type bot_handler: Optional[BotHandler]
    :param fast_api: Экземпляр FastAPI.
    :type fast_api: Optional[FastApi]
    """

    def __init__(
        self,
        token: str,
        port: int,
        webhook_url: Optional[str] = None,
        bot_handler: Optional[BotHandler] = None,
        fast_api: Optional[FastApi] = None,
    ):
        """
        Инициализирует Telegram бота, настраивает обработчики и запускает FastAPI сервер.
        """
        self.token = token
        self.port = port
        self.webhook_url = webhook_url if webhook_url else "/telegram_webhook"
        self.bot_handler = bot_handler if bot_handler else BotHandler()
        self.fast_api = fast_api if fast_api else FastApi()  # Используем переданный экземпляр или создаем новый
        self.app = Application.builder().token(self.token).build()
        self._register_handlers()
        self.fast_api.add_route(self.webhook_url, self.telegram_webhook, methods=["POST"])  # Регистрируем вебхук
        self.fast_api.on_event("startup", self.startup_event)
        self.fast_api.on_event("shutdown", self.shutdown_event)

    def _register_handlers(self):
        """
        Регистрирует обработчики команд и сообщений для Telegram бота.
        """
        self.app.add_handler(CommandHandler("start", self.bot_handler.start))
        self.app.add_handler(CommandHandler("help", self.bot_handler.help))
        self.app.add_handler(CommandHandler("sendpdf", self.bot_handler.send_pdf))
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self._handle_message))  # обрабатываем текстовые сообщения
        self.app.add_handler(MessageHandler(filters.VOICE, self.bot_handler.handle_voice))  # обрабатываем голосовые сообщения
        self.app.add_handler(MessageHandler(filters.Document.ALL, self.bot_handler.handle_document))  # обрабатываем документы
        self.app.add_handler(MessageHandler(filters.ALL, self.bot_handler.handle_log))  # обрабатываем логи

    async def _handle_message(self, update: Update, context: CallbackContext):
        """
        Обрабатывает текстовые сообщения, перенаправляя их в BotHandler.

        :param update: Объект обновления от Telegram.
        :type update: Update
        :param context: Контекст выполнения.
        :type context: CallbackContext
        """
        await self.bot_handler.handle_message(update, context)  # Передаем сообщение в BotHandler

    async def telegram_webhook(self, request: Request):
        """
        Обрабатывает входящие вебхуки от Telegram.

        :param request: Объект HTTP запроса.
        :type request: Request
        """
        global bot_instance
        if bot_instance is None:
            logger.error("Bot instance is not initialized")  # Логируем ошибку если бот не инициализирован
            return {"ok": False}, 500
        try:
            data = await request.json()  # Получаем JSON данные из запроса
            update = Update.de_json(data, bot_instance.app.bot)  # Преобразуем JSON в объект Update
            await bot_instance.app.process_update(update)  # Обрабатываем обновление
            return {"ok": True}, 200  # Возвращаем успешный статус
        except Exception as e:
             logger.error(f"Error processing telegram webhook: {e}")  # Логируем ошибку
             return {"ok": False, "error": str(e)}, 500  # Возвращаем ошибку

    async def startup_event(self):
         """
         Обработчик события запуска FastAPI.
         Инициализирует Telegram бота и устанавливает вебхук.
         """
         await initialize_bot(
            token=os.getenv("TELEGRAM_BOT_TOKEN"),
            port=int(os.getenv("PORT", 8000)),
        )  # инициализируем бота при запуске

    async def shutdown_event(self):
        """
        Обработчик события завершения FastAPI.
        Удаляет вебхук Telegram бота.
        """
        if self.app:
            await self.app.bot.delete_webhook()

async def initialize_bot(token: str, port: int):
    """
    Инициализирует и запускает Telegram бота.

    :param token: Токен Telegram бота.
    :type token: str
    :param port: Порт для FastAPI сервера.
    :type port: int
    """
    global bot_instance
    bot_instance = TelegramBot(token=token, port=port)
    if bot_instance.webhook_url:
        webhook_url = bot_instance.webhook_url
        await bot_instance.app.bot.set_webhook(url=f"https://localhost:{port}{webhook_url}")  # Устанавливаем вебхук
    else:
         await bot_instance.app.run_polling()  # Запускаем polling если не задан вебхук


if __name__ == "__main__":
    """
    Основная точка входа для запуска приложения.
    """
    fast_api_instance = FastApi()  # Создаём экземпляр FastApi
    telegram_config = j_loads_ns("src/endpoints/bots/telegram/telegram.json").get('telegram')
    webhook_url = telegram_config.get("webhook_url", "/telegram_webhook")  # Получаем URL вебхука из конфига
    fast_api_instance.add_route(webhook_url, TelegramBot.telegram_webhook, methods=["POST"])  # Регистрируем вебхук
    fast_api_instance.register_router()
    fast_api_instance.run()
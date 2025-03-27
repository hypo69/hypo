# Анализ кода модуля `main`

**Качество кода**:

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код хорошо структурирован, функции выполняют четкие задачи.
    - Используются асинхронные функции, что хорошо для обработки вебхуков.
    - Присутствует логирование, что важно для отладки и мониторинга.
    - Код использует `aiogram` для работы с Telegram ботом.
- **Минусы**:
    -  Импорт `logger` не соответствует заданным стандартам.
    -  Используются двойные кавычки для вывода в `logger.error` и `bot.send_message`.
    -  Некоторые комментарии могут быть более информативными.
    -  Отсутствует  RST-документация для функций.

**Рекомендации по улучшению**:

1.  Исправить импорт `logger` на `from src.logger import logger`.
2.  Заменить двойные кавычки на одинарные в коде, кроме операций вывода (например, в `print`, `input`, `logger`).
3.  Добавить RST-документацию для всех функций и классов.
4.  Улучшить информативность комментариев, например, вместо "Регистрация мидлварей" лучше написать "Регистрирует мидлвари для обработки входящих обновлений".
5.  Избегать использования `try-except` для простых задач, где можно использовать `logger.error`.
6.  Перенести все константы в `settings` и использовать их.

**Оптимизированный код**:

```python
from aiogram.webhook.aiohttp_server import setup_application
from aiohttp import web
from aiogram.types import BotCommand, BotCommandScopeDefault
from src.logger import logger # Исправлен импорт logger
from bot.app.app import handle_webhook, robokassa_result, robokassa_fail, home_page
from bot.config import bot, admins, dp, settings
from bot.dao.database_middleware import DatabaseMiddlewareWithoutCommit, DatabaseMiddlewareWithCommit
from bot.admin.admin import admin_router
from bot.user.user_router import user_router
from bot.user.catalog_router import catalog_router


async def set_default_commands():
    """
    Устанавливает команды по умолчанию для бота.

    :raises Exception: В случае ошибки при установке команд.

    :Example:
        >>> await set_default_commands()
    """
    commands = [BotCommand(command='start', description='Запустить бота')]
    try:
        await bot.set_my_commands(commands, BotCommandScopeDefault())
    except Exception as e:
        logger.error(f'Не удалось установить команды по умолчанию: {e}') # Логируем ошибку

async def on_startup(app):
    """
    Выполняется при запуске приложения.

    Устанавливает webhook и отправляет уведомление администраторам.

    :param app: Экземпляр aiohttp приложения.
    :type app: web.Application

    :raises Exception: В случае ошибки при запуске приложения.

    :Example:
        >>> async def start():
        ...   app = web.Application()
        ...   await on_startup(app)
        >>> import asyncio
        >>> asyncio.run(start())
    """
    await set_default_commands()
    try:
        await bot.set_webhook(settings.get_webhook_url)
    except Exception as e:
       logger.error(f'Не удалось установить webhook: {e}') # Логируем ошибку
    for admin_id in admins:
        try:
            await bot.send_message(admin_id, 'Бот запущен 🥳.') # Используем одинарные кавычки
        except Exception as e:
            logger.error(f'Не удалось отправить сообщение админу {admin_id}: {e}') # Используем одинарные кавычки
    logger.info('Бот успешно запущен.')

async def on_shutdown(app):
    """
    Выполняется при остановке приложения.

    Отправляет уведомление администраторам и удаляет webhook.

    :param app: Экземпляр aiohttp приложения.
    :type app: web.Application

    :raises Exception: В случае ошибки при остановке приложения.

    :Example:
        >>> async def shutdown():
        ...    app = web.Application()
        ...    await on_shutdown(app)
        >>> import asyncio
        >>> asyncio.run(shutdown())
    """
    for admin_id in admins:
        try:
            await bot.send_message(admin_id, 'Бот остановлен. Почему? 😔') # Используем одинарные кавычки
        except Exception as e:
            logger.error(f'Не удалось отправить сообщение админу {admin_id}: {e}') # Используем одинарные кавычки
    try:
       await bot.delete_webhook(drop_pending_updates=True)
    except Exception as e:
        logger.error(f'Не удалось удалить webhook: {e}') # Логируем ошибку
    try:
       await bot.session.close()
    except Exception as e:
        logger.error(f'Не удалось закрыть сессию бота: {e}') # Логируем ошибку
    logger.error('Бот остановлен!') # Используем одинарные кавычки


def register_middlewares():
    """
    Регистрирует мидлвари для обработки входящих обновлений.

    Эти мидлвари обеспечивают работу с базой данных.

    :Example:
       >>> register_middlewares()
    """
    dp.update.middleware.register(DatabaseMiddlewareWithoutCommit())
    dp.update.middleware.register(DatabaseMiddlewareWithCommit())


def register_routers():
    """
    Регистрирует маршрутизаторы для обработки различных типов запросов.

    :Example:
       >>> register_routers()
    """
    dp.include_router(catalog_router)
    dp.include_router(user_router)
    dp.include_router(admin_router)


def create_app():
    """
    Создает и настраивает приложение aiohttp.

    Включает маршруты для обработки вебхуков, результатов и ошибок Robokassa, а также домашнюю страницу.

    :return: Готовое к запуску приложение aiohttp.
    :rtype: web.Application

    :Example:
       >>> app = create_app()
       >>> # Далее можно запустить приложение, например, через web.run_app(app)
    """
    app = web.Application()
    app.router.add_post(f'/{settings.BOT_TOKEN}', handle_webhook) # Используем одинарные кавычки
    app.router.add_post('/robokassa/result/', robokassa_result) # Используем одинарные кавычки
    app.router.add_get('/robokassa/fail/', robokassa_fail) # Используем одинарные кавычки
    app.router.add_get('/', home_page) # Используем одинарные кавычки
    setup_application(app, dp, bot=bot)
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    return app


def main():
    """
    Главная функция для запуска приложения.

    Регистрирует мидлвари, роутеры, создает и запускает приложение.

    :Example:
        >>> main()
    """
    register_middlewares()
    register_routers()
    app = create_app()
    web.run_app(app, host=settings.SITE_HOST, port=settings.SITE_PORT)


if __name__ == '__main__':
    main()
```
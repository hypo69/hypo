# Анализ кода модуля `main.py`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован, разбит на логические блоки.
    - Используются асинхронные функции, что хорошо для работы с ботами.
    - Есть обработка ошибок при отправке сообщений администраторам.
    - Код использует мидлвари и роутеры для обработки сообщений.
    - Присутствует документация в виде docstring.
 - Минусы
    - В коде нет явного импорта `logger` из `src.logger.logger`, что является требованием.
    -  Некоторые комментарии не соответствуют требованию (например, "Функция для...").
    - Не все функции имеют подробное описание в docstring.
    - Не используется `j_loads` или `j_loads_ns`.
    - Не все функции имеют примеры использования в docstring.

**Рекомендации по улучшению**

1.  Добавить импорт `logger` из `src.logger.logger`.
2.  Обновить комментарии к функциям в соответствии с инструкцией (не "Функция для...", а "Код исполняет ...").
3.  Дополнить docstring для каждой функции, добавив подробное описание, аргументы, возвращаемые значения, и примеры использования.
4.  Удалить избыточные блоки `try-except` и использовать `logger.error` для обработки ошибок.
5.  Убрать `...` как точки остановки, если они не несут смысловой нагрузки.
6.  Использовать одинарные кавычки в коде.
7.  Переписать комментарии, используя более конкретные формулировки, такие как ‘проверка’, ‘отправка’, ‘код исполняет...’.

**Оптимизированный код**

```python
"""
Модуль для запуска и настройки Telegram-бота.
=========================================================================================

Этот модуль содержит функции для создания, запуска и настройки Telegram-бота, включая установку вебхука,
регистрацию middleware, роутеров и обработчиков для различных типов запросов.

Пример использования
--------------------

Пример запуска бота:

.. code-block:: python

    if __name__ == "__main__":
        main()
"""
from aiogram.webhook.aiohttp_server import setup_application
from aiohttp import web
from aiogram.types import BotCommand, BotCommandScopeDefault
# import logger from src.logger
from src.logger.logger import logger # Импорт logger из src.logger
from bot.app.app import handle_webhook, robokassa_result, robokassa_fail, home_page
from bot.config import bot, admins, dp, settings
from bot.dao.database_middleware import DatabaseMiddlewareWithoutCommit, DatabaseMiddlewareWithCommit
from bot.admin.admin import admin_router
from bot.user.user_router import user_router
from bot.user.catalog_router import catalog_router


async def set_default_commands():
    """
    Устанавливает команды по умолчанию для бота.
    
    Код устанавливает команду '/start' для запуска бота.
    """
    commands = [BotCommand(command='start', description='Запустить бота')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def on_startup(app):
    """
    Выполняется при запуске приложения.

    Код устанавливает вебхук, отправляет уведомления администраторам о запуске бота.
    
    Args:
        app: Aiohttp application instance.

    """
    await set_default_commands()
    await bot.set_webhook(settings.get_webhook_url)
    for admin_id in admins:
        try:
            await bot.send_message(admin_id, 'Бот запущен 🥳.')
        except Exception as e:
            logger.error(f'Не удалось отправить сообщение админу {admin_id}: {e}')
    logger.info('Бот успешно запущен.')


async def on_shutdown(app):
    """
    Выполняется при остановке приложения.

    Код отправляет уведомления администраторам об остановке бота, удаляет вебхук и закрывает сессию.

    Args:
        app: Aiohttp application instance.
    """
    for admin_id in admins:
        try:
            await bot.send_message(admin_id, 'Бот остановлен. Почему? 😔')
        except Exception as e:
            logger.error(f'Не удалось отправить сообщение админу {admin_id}: {e}')
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.session.close()
    logger.error('Бот остановлен!')


def register_middlewares():
    """
    Регистрирует мидлвари для диспетчера.
    
    Код регистрирует мидлвари для работы с базой данных без и с коммитом.
    """
    dp.update.middleware.register(DatabaseMiddlewareWithoutCommit())
    dp.update.middleware.register(DatabaseMiddlewareWithCommit())


def register_routers():
    """
    Регистрирует маршруты для диспетчера.
    
    Код включает роутеры для каталога, пользователей и администраторов.
    """
    dp.include_router(catalog_router)
    dp.include_router(user_router)
    dp.include_router(admin_router)


def create_app():
    """
    Создает и настраивает приложение aiohttp.
    
    Код создает приложение, регистрирует обработчики маршрутов, настраивает приложение с диспетчером и ботом,
    а также регистрирует функции запуска и остановки.

    Returns:
        web.Application: Настроенное приложение aiohttp.
    """
    app = web.Application()

    # Регистрация обработчиков маршрутов
    app.router.add_post(f'/{settings.BOT_TOKEN}', handle_webhook)
    app.router.add_post('/robokassa/result/', robokassa_result)
    app.router.add_get('/robokassa/fail/', robokassa_fail)
    app.router.add_get('/', home_page)

    setup_application(app, dp, bot=bot)

    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    return app


def main():
    """
    Главная функция для запуска приложения.
    
    Код регистрирует мидлвари, роутеры, создает приложение и запускает его.
    """
    register_middlewares()
    register_routers()

    app = create_app()
    web.run_app(app, host=settings.SITE_HOST, port=settings.SITE_PORT)


if __name__ == '__main__':
    main()
```
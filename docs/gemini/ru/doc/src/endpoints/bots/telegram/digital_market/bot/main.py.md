# `main.py`

## Обзор

Этот модуль является основной точкой входа для Telegram-бота, обеспечивающего функциональность цифрового рынка. Он настраивает и запускает веб-приложение, обрабатывает входящие запросы от Telegram, а также управляет взаимодействием с базой данных через мидлвари. Модуль включает в себя регистрацию мидлварей, маршрутов, а также обработчики для запуска и остановки бота.

## Содержание

1. [Функции](#Функции)
   - [`set_default_commands`](#set_default_commands)
   - [`on_startup`](#on_startup)
   - [`on_shutdown`](#on_shutdown)
   - [`register_middlewares`](#register_middlewares)
   - [`register_routers`](#register_routers)
   - [`create_app`](#create_app)
   - [`main`](#main)
2. [Импорты](#Импорты)

## Импорты

- `aiogram.webhook.aiohttp_server`:  Для настройки webhook на aiohttp сервере.
- `aiohttp.web`: Для создания и управления веб-приложением.
- `aiogram.types`: Для работы с типами данных aiogram, такими как `BotCommand` и `BotCommandScopeDefault`.
- `loguru.logger`: Для логирования событий и ошибок.
- `bot.app.app`: Для импорта функций обработки webhook, robokassa и главной страницы.
- `bot.config`: Для импорта настроек бота, включая токен, список админов и экземпляр бота.
- `bot.dao.database_middleware`: Для импорта middleware, обеспечивающего взаимодействие с базой данных.
- `bot.admin.admin`: Для импорта роутера админских команд.
- `bot.user.user_router`: Для импорта роутера пользовательских команд.
- `bot.user.catalog_router`: Для импорта роутера команд каталога.

## Функции

### `set_default_commands`

**Описание**:
Устанавливает команды по умолчанию для бота, такие как `/start`.

**Параметры**:
- Нет.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Нет.

```python
async def set_default_commands():
    """
    Устанавливает команды по умолчанию для бота.
    """
    commands = [BotCommand(command='start', description='Запустить бота')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())
```

### `on_startup`

**Описание**:
Выполняет действия при запуске приложения, такие как установка webhook, отправка уведомления администраторам о запуске бота.

**Параметры**:
- `app` (`aiohttp.web.Application`): Экземпляр aiohttp приложения.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если не удается отправить сообщение администратору.

```python
async def on_startup(app):
    """
    Выполняется при запуске приложения.
    """
    await set_default_commands()
    await bot.set_webhook(settings.get_webhook_url)
    for admin_id in admins:
        try:
            await bot.send_message(admin_id, 'Бот запущен 🥳.')
        except Exception as ex:
            logger.error(f"Не удалось отправить сообщение админу {admin_id}: {ex}")
    logger.info("Бот успешно запущен.")
```

### `on_shutdown`

**Описание**:
Выполняет действия при остановке приложения, такие как отправка уведомления администраторам об остановке бота, удаление webhook и закрытие сессии бота.

**Параметры**:
- `app` (`aiohttp.web.Application`): Экземпляр aiohttp приложения.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если не удается отправить сообщение администратору.

```python
async def on_shutdown(app):
    """
    Выполняется при остановке приложения.
    """
    for admin_id in admins:
        try:
            await bot.send_message(admin_id, 'Бот остановлен. Почему? 😔')
        except Exception as ex:
            logger.error(f"Не удалось отправить сообщение админу {admin_id}: {ex}")
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.session.close()
    logger.error("Бот остановлен!")
```

### `register_middlewares`

**Описание**:
Регистрирует мидлвари для диспетчера, включая мидлвари для работы с базой данных.

**Параметры**:
- Нет.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Нет.

```python
def register_middlewares():
    """
    Регистрирует мидлвари для диспетчера.
    """
    dp.update.middleware.register(DatabaseMiddlewareWithoutCommit())
    dp.update.middleware.register(DatabaseMiddlewareWithCommit())
```

### `register_routers`

**Описание**:
Регистрирует роутеры для диспетчера, включая роутеры для каталога, пользователя и администратора.

**Параметры**:
- Нет.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Нет.

```python
def register_routers():
    """
    Регистрирует маршруты для диспетчера.
    """
    dp.include_router(catalog_router)
    dp.include_router(user_router)
    dp.include_router(admin_router)
```

### `create_app`

**Описание**:
Создает и настраивает aiohttp приложение, регистрирует обработчики маршрутов, настраивает приложение с диспетчером и ботом, а также регистрирует функции запуска и остановки.

**Параметры**:
- Нет.

**Возвращает**:
- `aiohttp.web.Application`: Экземпляр aiohttp приложения.

**Вызывает исключения**:
- Нет.

```python
def create_app():
    """
    Создает и настраивает приложение aiohttp.
    """
    # Создаем приложение
    app = web.Application()

    # Регистрация обработчиков маршрутов
    app.router.add_post(f"/{settings.BOT_TOKEN}", handle_webhook)
    app.router.add_post("/robokassa/result/", robokassa_result)
    app.router.add_get("/robokassa/fail/", robokassa_fail)
    app.router.add_get("/", home_page)

    # Настройка приложения с диспетчером и ботом
    setup_application(app, dp, bot=bot)

    # Регистрация функций запуска и остановки
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    return app
```

### `main`

**Описание**:
Главная функция для запуска приложения. Она регистрирует мидлвари и роутеры, создает приложение и запускает его.

**Параметры**:
- Нет.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Нет.

```python
def main():
    """
    Главная функция для запуска приложения.
    """
    # Регистрация мидлварей и роутеров
    register_middlewares()
    register_routers()

    # Создаем приложение и запускаем его
    app = create_app()
    web.run_app(app, host=settings.SITE_HOST, port=settings.SITE_PORT)
```
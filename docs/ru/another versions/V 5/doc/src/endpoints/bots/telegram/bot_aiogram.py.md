# Модуль `bot_aiogram.py`

## Обзор

Модуль `bot_aiogram.py` предоставляет реализацию Telegram-бота с использованием библиотеки `aiogram` и сервера FastAPI. Он включает в себя функциональность для обработки команд, голосовых сообщений, документов и текстовых сообщений, а также интеграцию с RPC для управления маршрутами и сервером.

## Подробней

Этот модуль является ключевым компонентом для интеграции Telegram-бота в систему `hypotez`. Он использует `aiogram` для обработки входящих сообщений и команд от пользователей Telegram, а также FastAPI для создания вебхука, через который Telegram отправляет обновления боту. Модуль также включает в себя интеграцию с RPC, что позволяет управлять сервером и маршрутами бота удаленно.

## Классы

### `TelegramBot`

**Описание**: Класс `TelegramBot` представляет собой интерфейс для Telegram-бота и является Singleton.

**Как работает класс**:
- Инициализируется с токеном бота и маршрутом для вебхука.
- Загружает конфигурацию из файла `telegram.json`.
- Создает экземпляры `Bot` и `Dispatcher` из библиотеки `aiogram`.
- Регистрирует обработчики для различных типов сообщений и команд.
- Инициализирует вебхук и RPC для управления ботом.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `TelegramBot`.
- `run`: Запускает бота, инициализирует RPC и вебхук.
- `_register_default_handlers`: Регистрирует обработчики по умолчанию, используя экземпляр `BotHandler`.
- `_handle_message`: Обрабатывает текстовые сообщения.
- `initialize_bot_webhook`: Инициализирует вебхук для бота.
- `_register_route_via_rpc`: Регистрирует маршрут вебхука Telegram через RPC.
- `stop`: Останавливает бота и удаляет вебхук.

**Параметры**:
- `token` (str): Токен Telegram-бота.
- `route` (str): Маршрут вебхука для FastAPI. По умолчанию `/telegram_webhook`.

### `__init__`

```python
def __init__(self, token: str, route: str = 'telegram_webhook'):
    """
    Initialize the TelegramBot instance.

    Args:
        token (str): Telegram bot token.
        route (str): Webhook route for FastAPI. Defaults to '/telegram_webhook'.
    """
```

**Описание**: Инициализирует экземпляр класса `TelegramBot`.

**Как работает функция**:
- Принимает токен бота и маршрут вебхука в качестве аргументов.
- Устанавливает значения атрибутов `token`, `port` и `route`.
- Загружает конфигурацию из файла `telegram.json` с использованием `j_loads_ns`.
- Создает экземпляры `Bot` и `Dispatcher` из библиотеки `aiogram`.
- Создает экземпляр `BotHandler` для обработки сообщений.
- Регистрирует обработчики по умолчанию с помощью метода `_register_default_handlers`.
- Инициализирует атрибуты `app` и `rpc_client` как `None`.

**Параметры**:
- `token` (str): Токен Telegram-бота.
- `route` (str): Маршрут вебхука для FastAPI. По умолчанию `'telegram_webhook'`.

**Примеры**:

```python
bot = TelegramBot(token='YOUR_TELEGRAM_BOT_TOKEN', route='/custom_webhook')
```

### `run`

```python
def run(self):
    """Run the bot and initialize RPC and webhook."""
```

**Описание**: Запускает бота, инициализирует RPC и вебхук.

**Как работает функция**:
1. **Инициализация RPC клиента**:
   - Пытается инициализировать RPC-клиента, подключаясь к RPC-серверу по адресу `http://{gs.host}:{port}/`, где `port` равен 9000.
   - Вызывает удаленную процедуру `start_server` на RPC-сервере для запуска сервера на порту `gs.host`.
   - Регистрирует маршрут с помощью удаленной процедуры RPC `add_new_route`.
   - В случае успеха логирует сообщение об успешном запуске RPC-сервера.
2. **Инициализация вебхука Telegram**:
   - Вызывает метод `initialize_bot_webhook` для инициализации вебхука Telegram.
   - Если вебхук успешно инициализирован, регистрирует маршрут с помощью RPC-клиента.
   - Запускает веб-приложение `aiohttp` для обработки входящих запросов от Telegram.
   - В случае ошибки логирует сообщение об ошибке.
3. **Запуск Long Polling (если не удалось настроить вебхук)**:
   - Если не удалось настроить вебхук, запускает бота в режиме Long Polling с использованием `asyncio.run(self.dp.start_polling(self.bot))`.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: В случае ошибок при инициализации RPC, установке вебхука или запуске приложения.

**Примеры**:

```python
bot = TelegramBot(token='YOUR_TELEGRAM_BOT_TOKEN')
bot.run()
```

### `_register_default_handlers`

```python
def _register_default_handlers(self):
    """Register the default handlers using the BotHandler instance."""
```

**Описание**: Регистрирует обработчики по умолчанию, используя экземпляр `BotHandler`.

**Как работает функция**:
- Регистрирует обработчики для команд `/start`, `/help`, `/sendpdf`.
- Регистрирует обработчик для текстовых сообщений, голосовых сообщений и документов.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `None`

**Примеры**:

```python
bot = TelegramBot(token='YOUR_TELEGRAM_BOT_TOKEN')
bot._register_default_handlers()
```

### `_handle_message`

```python
async def _handle_message(self, message: types.Message):
    """Handle any text message."""
```

**Описание**: Обрабатывает текстовые сообщения.

**Как работает функция**:
- Передает сообщение обработчику `handle_message` в экземпляре `BotHandler`.

**Параметры**:
- `message` (types.Message): Объект сообщения.

**Возвращает**:
- `None`

**Примеры**:

```python
async def handle_updates(update: types.Update):
    bot = TelegramBot(token='YOUR_TELEGRAM_BOT_TOKEN')
    await bot._handle_message(update.message)
```

### `initialize_bot_webhook`

```python
def initialize_bot_webhook(self, route: str):
    """Initialize the bot webhook."""
```

**Описание**: Инициализирует вебхук для бота.

**Как работает функция**:
- Формирует URL вебхука на основе хоста и маршрута.
- Если хост является `127.0.0.1` или `localhost`, использует `ngrok` для создания туннеля.
- Пытается установить вебхук с использованием метода `set_webhook` бота.
- В случае успеха логирует информацию о вебхуке и возвращает URL вебхука.
- В случае ошибки логирует сообщение об ошибке и возвращает `False`.

**Параметры**:
- `route` (str): Маршрут вебхука.

**Возвращает**:
- `str | False`: URL вебхука в случае успеха, `False` в случае ошибки.

**Примеры**:

```python
bot = TelegramBot(token='YOUR_TELEGRAM_BOT_TOKEN')
webhook_url = bot.initialize_bot_webhook(route='/my_webhook')
if webhook_url:
    print(f'Webhook URL: {webhook_url}')
```

### `_register_route_via_rpc`

```python
def _register_route_via_rpc(self, rpc_client: ServerProxy):
    """Register the Telegram webhook route via RPC."""
```

**Описание**: Регистрирует маршрут вебхука Telegram через RPC.

**Как работает функция**:
- Формирует маршрут, добавляя `/` в начало, если его нет.
- Вызывает RPC метод `add_new_route` для регистрации маршрута.
- Логирует информацию об успешной регистрации маршрута.
- В случае ошибки логирует сообщение об ошибке.

**Параметры**:
- `rpc_client` (ServerProxy): RPC клиент.

**Возвращает**:
- `None`

**Примеры**:

```python
bot = TelegramBot(token='YOUR_TELEGRAM_BOT_TOKEN')
rpc_client = ServerProxy(f"http://{gs.host}:9000", allow_none=True)
bot._register_route_via_rpc(rpc_client)
```

### `stop`

```python
def stop(self):
    """Stop the bot and delete the webhook."""
```

**Описание**: Останавливает бота и удаляет вебхук.

**Как работает функция**:
- Останавливает веб-приложение, если оно запущено.
- Удаляет вебхук с использованием метода `delete_webhook` бота.
- Логирует информацию об остановке бота.
- В случае ошибки логирует сообщение об ошибке.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `None`

**Примеры**:

```python
bot = TelegramBot(token='YOUR_TELEGRAM_BOT_TOKEN')
bot.stop()
```

## Функции

### `__name__ == "__main__"`

**Описание**: Основная точка входа для запуска бота.

**Как работает функция**:
- Загружает переменные окружения из файла `.env`.
- Создает экземпляр класса `TelegramBot` с использованием токена из переменной окружения `TELEGRAM_TOKEN`.
- Запускает бота с помощью метода `run`.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `None`

**Примеры**:

Для запуска бота необходимо установить токен Telegram-бота в переменной окружения `TELEGRAM_TOKEN` и выполнить скрипт.

```bash
TELEGRAM_TOKEN=YOUR_TELEGRAM_BOT_TOKEN python src/endpoints/bots/telegram/bot_aiogram.py
```
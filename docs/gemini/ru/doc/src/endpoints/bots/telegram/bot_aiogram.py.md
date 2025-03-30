# Модуль `bot_aiogram.py`

## Обзор

Модуль `bot_aiogram.py` представляет собой реализацию Telegram-бота с использованием библиотеки `aiogram` и сервера `FastAPI` через `RPC`. Он обеспечивает взаимодействие с Telegram API, обработку входящих сообщений и команд, а также интеграцию с другими сервисами через удаленный вызов процедур (RPC).

## Подробнее

Этот модуль содержит класс `TelegramBot`, который является точкой входа для запуска и управления ботом. Он инициализирует бота, регистрирует обработчики команд и сообщений, настраивает вебхук для получения обновлений от Telegram и запускает сервер `FastAPI` для обработки входящих запросов.

Модуль использует `RPC` для взаимодействия с другими частями системы, что позволяет распределить нагрузку и упростить масштабирование. Он также включает обработку голоса и документов, отправку `PDF`-файлов и ведение логов.

## Классы

### `TelegramBot`

**Описание**: Класс `TelegramBot` представляет собой интерфейс для взаимодействия с Telegram API. Он инициализирует бота, регистрирует обработчики команд и сообщений, настраивает вебхук и запускает сервер `FastAPI`.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `TelegramBot`.
- `run`: Запускает бота, инициализирует `RPC` и вебхук.
- `_register_default_handlers`: Регистрирует обработчики команд по умолчанию.
- `_handle_message`: Обрабатывает текстовые сообщения.
- `initialize_bot_webhook`: Инициализирует вебхук бота.
- `_register_route_via_rpc`: Регистрирует маршрут вебхука через `RPC`.
- `stop`: Останавливает бота и удаляет вебхук.

#### `__init__`

```python
def __init__(self, token: str, route: str = 'telegram_webhook'):
    """
    Args:
        token (str): Telegram bot token.
        route (str): Webhook route for FastAPI. Defaults to '/telegram_webhook'.
    """
```

**Описание**: Инициализирует экземпляр класса `TelegramBot`.

**Параметры**:
- `token` (str): Токен Telegram-бота.
- `route` (str, optional): Маршрут вебхука для `FastAPI`. По умолчанию `/telegram_webhook`.

**Примеры**:

```python
bot = TelegramBot(token='YOUR_TELEGRAM_BOT_TOKEN', route='/custom_webhook')
```

#### `run`

```python
def run(self):
    """Запускает бота и инициализирует RPC и вебхук."""
```

**Описание**: Запускает бота, инициализирует `RPC` и вебхук.

**Примеры**:

```python
bot = TelegramBot(token='YOUR_TELEGRAM_BOT_TOKEN')
bot.run()
```

#### `_register_default_handlers`

```python
def _register_default_handlers(self):
    """Регистрирует обработчики команд по умолчанию."""
```

**Описание**: Регистрирует обработчики команд по умолчанию, такие как `/start`, `/help`, `/sendpdf`, а также обработчики голосовых сообщений, документов и логов.

**Примеры**:

```python
bot = TelegramBot(token='YOUR_TELEGRAM_BOT_TOKEN')
bot._register_default_handlers()
```

#### `_handle_message`

```python
async def _handle_message(self, message: types.Message):
    """
    Args:
        message (types.Message): _description_
    """
```

**Описание**: Обрабатывает текстовые сообщения, перенаправляя их в метод `handle_message` класса `BotHandler`.

**Параметры**:
- `message` (types.Message): Объект сообщения от Telegram.

**Примеры**:

```python
# Пример обработки сообщения (внутри Dispatcher)
async def some_handler(message: types.Message):
    bot = TelegramBot(token='YOUR_TELEGRAM_BOT_TOKEN')
    await bot._handle_message(message)
```

#### `initialize_bot_webhook`

```python
def initialize_bot_webhook(self, route: str):
    """
    Args:
        route (str): _description_
    """
```

**Описание**: Инициализирует вебхук бота, устанавливая `URL` для получения обновлений от Telegram. Если хост указан как `localhost` или `127.0.0.1`, использует `ngrok` для создания туннеля.

**Параметры**:
- `route` (str): Маршрут вебхука.

**Возвращает**:
- `str | bool`: URL вебхука в случае успешной инициализации, `False` в случае ошибки.

**Примеры**:

```python
bot = TelegramBot(token='YOUR_TELEGRAM_BOT_TOKEN')
webhook_url = bot.initialize_bot_webhook(route='/custom_webhook')
if webhook_url:
    print(f"Webhook URL: {webhook_url}")
```

#### `_register_route_via_rpc`

```python
def _register_route_via_rpc(self, rpc_client: ServerProxy):
    """
    Args:
        rpc_client (ServerProxy): _description_
    """
```

**Описание**: Регистрирует маршрут вебхука через `RPC`, добавляя новый маршрут для обработки входящих запросов.

**Параметры**:
- `rpc_client` (ServerProxy): Клиент `RPC` для взаимодействия с сервером.

**Примеры**:

```python
bot = TelegramBot(token='YOUR_TELEGRAM_BOT_TOKEN')
rpc_client = ServerProxy(f"http://{gs.host}:9000", allow_none=True)
bot._register_route_via_rpc(rpc_client)
```

#### `stop`

```python
def stop(self):
    """Останавливает бота и удаляет вебхук."""
```

**Описание**: Останавливает бота и удаляет вебхук, освобождая ресурсы и завершая работу `FastAPI`-приложения.

**Примеры**:

```python
bot = TelegramBot(token='YOUR_TELEGRAM_BOT_TOKEN')
bot.stop()
```

## Функции

### `__main__`

```python
if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    bot = TelegramBot(os.getenv('TELEGRAM_TOKEN'))
    bot.run()
```

**Описание**: Главная функция, которая запускает Telegram-бота.

**Примеры**:

```python
# Запуск бота из командной строки
# python bot_aiogram.py
```
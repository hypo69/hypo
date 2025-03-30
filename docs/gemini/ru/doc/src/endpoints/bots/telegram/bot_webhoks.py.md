# Модуль telegram_webhooks

## Обзор

Модуль `telegram_webhooks.py` реализует Telegram-бота, интегрированного с сервером FastAPI через RPC. Он предоставляет интерфейс для обработки входящих сообщений и команд от пользователей Telegram, а также для взаимодействия с другими частями системы через удаленные вызовы процедур (RPC).

## Подробней

Этот модуль является ключевым компонентом для интеграции Telegram-ботов в систему `hypotez`. Он обеспечивает возможность приема и обработки сообщений из Telegram, а также отправку ответов и выполнение команд.

Модуль использует библиотеку `telegram.ext` для упрощения работы с Telegram Bot API и `FastAPI` для создания веб-сервера, который принимает обновления от Telegram через webhook. Для взаимодействия между компонентами системы используется RPC, что позволяет боту выполнять задачи, требующие доступа к другим сервисам или данным.

## Классы

### `TelegramBot`

**Описание**: Класс `TelegramBot` представляет собой основной интерфейс для работы с Telegram-ботом. Он инициализирует бота, регистрирует обработчики команд и сообщений, а также запускает веб-сервер для приема обновлений от Telegram.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `TelegramBot`.
- `run`: Запускает бота, инициализирует RPC и webhook.
- `_register_default_handlers`: Регистрирует обработчики по умолчанию.
- `_handle_message`: Обрабатывает любое текстовое сообщение.
- `initialize_bot_webhook`: Инициализирует webhook бота.
- `_register_route_via_rpc`: Регистрирует маршрут Telegram webhook через RPC.
- `stop`: Останавливает бота и удаляет webhook.

**Параметры**:
- `token` (str): Токен Telegram-бота.
- `route` (str): Webhook route для FastAPI. По умолчанию '/telegram_webhook'.

**Примеры**

```python
from dotenv import load_dotenv
import os

load_dotenv()
bot = TelegramBot(os.getenv('TELEGRAM_TOKEN'))
bot.run()
```

## Функции

### `__init__`

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
- `route` (str, optional): Webhook route для FastAPI. По умолчанию '/telegram_webhook'.

**Примеры**:
```python
bot = TelegramBot("YOUR_TELEGRAM_BOT_TOKEN", route='/custom_webhook')
```

### `run`

```python
def run(self):
    """
    Args:
        self (TelegramBot): Экземпляр класса `TelegramBot`.
    """
```

**Описание**: Запускает бота, инициализирует RPC и webhook.

**Примеры**:
```python
bot = TelegramBot(os.getenv('TELEGRAM_TOKEN'))
bot.run()
```

### `_register_default_handlers`

```python
def _register_default_handlers(self):
    """
    Args:
        self (TelegramBot): Экземпляр класса `TelegramBot`.
    """
```

**Описание**: Регистрирует обработчики по умолчанию.

**Примеры**:
```python
bot = TelegramBot(os.getenv('TELEGRAM_TOKEN'))
bot._register_default_handlers()
```

### `_handle_message`

```python
async def _handle_message(self, update: Update, context: CallbackContext) -> None:
    """
    Args:
        update (Update): Объект `Update` от Telegram.
        context (CallbackContext): Контекст обратного вызова.
    """
```

**Описание**: Обрабатывает любое текстовое сообщение.

**Параметры**:
- `update` (Update): Объект `Update` от Telegram.
- `context` (CallbackContext): Контекст обратного вызова.

**Примеры**:
```python
# Пример использования внутри класса TelegramBot
await self._handle_message(update, context)
```

### `initialize_bot_webhook`

```python
def initialize_bot_webhook(self, route: str):
    """
    Args:
        route (str): Маршрут для вебхука.
    """
```

**Описание**: Инициализирует webhook бота.

**Параметры**:
- `route` (str): Маршрут для вебхука.

**Возвращает**:
- `str | bool`: URL вебхука в случае успеха, `False` в случае ошибки.

**Примеры**:
```python
webhook_url = bot.initialize_bot_webhook('/telegram_webhook')
```

### `_register_route_via_rpc`

```python
def _register_route_via_rpc(self, rpc_client: ServerProxy):
    """
    Args:
        rpc_client (ServerProxy): Клиент RPC.
    """
```

**Описание**: Регистрирует маршрут Telegram webhook через RPC.

**Параметры**:
- `rpc_client` (ServerProxy): Клиент RPC.

**Примеры**:
```python
rpc_client = ServerProxy(f"http://{gs.host}:9000", allow_none=True)
bot._register_route_via_rpc(rpc_client)
```

### `stop`

```python
def stop(self):
    """
    Args:
        self (TelegramBot): Экземпляр класса `TelegramBot`.
    """
```

**Описание**: Останавливает бота и удаляет webhook.

**Примеры**:
```python
bot = TelegramBot(os.getenv('TELEGRAM_TOKEN'))
bot.stop()
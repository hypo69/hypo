# Модуль `telegram_webhooks`

## Обзор

Модуль `telegram_webhooks` реализует телеграм-бота с использованием сервера FastAPI и RPC. Он предоставляет класс `TelegramBot`, который упрощает взаимодействие с Telegram API, настройку вебхуков и обработку входящих сообщений. Модуль позволяет запускать бота как через вебхук, так и через polling.

## Подробней

Этот модуль является ключевым компонентом системы для интеграции телеграм-ботов с остальной частью приложения через FastAPI и RPC. Он обеспечивает возможность динамической регистрации маршрутов для обработки сообщений, а также поддерживает работу с различными типами входящих данных, такими как текст, голос и документы. Расположение файла `/src/endpoints/bots/telegram/telegram_webhooks.py` указывает на то, что он является частью подсистемы обработки ботов в проекте `hypotez`.

## Классы

### `TelegramBot`

**Описание**: Класс `TelegramBot` представляет собой интерфейс для работы с Telegram ботом. Он включает в себя методы для инициализации бота, запуска сервера, регистрации обработчиков и остановки бота.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `TelegramBot`.
- `run`: Запускает бота и инициализирует RPC и webhook.
- `_register_default_handlers`: Регистрирует обработчики по умолчанию, используя экземпляр `BotHandler`.
- `_handle_message`: Обрабатывает любое текстовое сообщение.
- `initialize_bot_webhook`: Инициализирует вебхук бота.
- `_register_route_via_rpc`: Регистрирует маршрут вебхука Telegram через RPC.
- `stop`: Останавливает бота и удаляет вебхук.

**Параметры**:
- `token` (str): Токен Telegram бота.
- `route` (str, optional): Webhook route для FastAPI. По умолчанию `/telegram_webhook`.

**Примеры**:

```python
from dotenv import load_dotenv
import os
from src.endpoints.bots.telegram.telegram_webhooks import TelegramBot

load_dotenv()
bot = TelegramBot(os.getenv('TELEGRAM_TOKEN'))
bot.run()
```

## Функции

### `__init__`

```python
def __init__(self, token: str, route: str = 'telegram_webhook'):
    """
    Initialize the TelegramBot instance.

    Args:
        token (str): Telegram bot token.
        route (str): Webhook route for FastAPI. Defaults to '/telegram_webhook'.
    """
    ...
```

**Описание**: Инициализирует экземпляр класса `TelegramBot`.

**Параметры**:
- `token` (str): Токен Telegram бота.
- `route` (str, optional): Webhook route для FastAPI. По умолчанию `/telegram_webhook`.

**Примеры**:
```python
from src.endpoints.bots.telegram.telegram_webhooks import TelegramBot
bot = TelegramBot('YOUR_TELEGRAM_BOT_TOKEN', route='/custom_route')
```

### `run`

```python
def run(self):
    """Run the bot and initialize RPC and webhook."""
    ...
```

**Описание**: Запускает бота и инициализирует RPC и webhook.

**Примеры**:
```python
from src.endpoints.bots.telegram.telegram_webhooks import TelegramBot
bot = TelegramBot('YOUR_TELEGRAM_BOT_TOKEN')
bot.run()
```

### `_register_default_handlers`

```python
def _register_default_handlers(self):
    """Register the default handlers using the BotHandler instance."""
    ...
```

**Описание**: Регистрирует обработчики по умолчанию, используя экземпляр `BotHandler`.

**Примеры**:
```python
from src.endpoints.bots.telegram.telegram_webhooks import TelegramBot
bot = TelegramBot('YOUR_TELEGRAM_BOT_TOKEN')
bot._register_default_handlers()
```

### `_handle_message`

```python
async def _handle_message(self, update: Update, context: CallbackContext) -> None:
    """Handle any text message."""
    ...
```

**Описание**: Обрабатывает любое текстовое сообщение.

**Параметры**:
- `update` (Update): Объект `Update` от Telegram.
- `context` (CallbackContext): Контекст обратного вызова.

**Примеры**:
```python
# Пример вызова внутри класса TelegramBot
await self._handle_message(update, context)
```

### `initialize_bot_webhook`

```python
def initialize_bot_webhook(self, route: str):
    """Initialize the bot webhook."""
    ...
```

**Описание**: Инициализирует вебхук бота.

**Параметры**:
- `route` (str): Маршрут вебхука.

**Возвращает**:
- `str | False`: URL вебхука или `False` в случае ошибки.

**Примеры**:
```python
from src.endpoints.bots.telegram.telegram_webhooks import TelegramBot
bot = TelegramBot('YOUR_TELEGRAM_BOT_TOKEN')
webhook_url = bot.initialize_bot_webhook('/telegram_webhook')
```

### `_register_route_via_rpc`

```python
def _register_route_via_rpc(self, rpc_client: ServerProxy):
    """Register the Telegram webhook route via RPC."""
    ...
```

**Описание**: Регистрирует маршрут вебхука Telegram через RPC.

**Параметры**:
- `rpc_client` (ServerProxy): RPC клиент.

**Примеры**:
```python
from xmlrpc.client import ServerProxy
from src.endpoints.bots.telegram.telegram_webhooks import TelegramBot
bot = TelegramBot('YOUR_TELEGRAM_BOT_TOKEN')
rpc_client = ServerProxy(f"http://{gs.host}:9000", allow_none=True)
bot._register_route_via_rpc(rpc_client)
```

### `stop`

```python
def stop(self):
    """Stop the bot and delete the webhook."""
    ...
```

**Описание**: Останавливает бота и удаляет вебхук.

**Примеры**:
```python
from src.endpoints.bots.telegram.telegram_webhooks import TelegramBot
bot = TelegramBot('YOUR_TELEGRAM_BOT_TOKEN')
bot.stop()
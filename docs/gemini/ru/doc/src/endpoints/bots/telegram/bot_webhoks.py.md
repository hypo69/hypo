# Модуль для работы с Telegram ботом через FastAPI и RPC
====================================================

Модуль `src.endpoints.bots.telegram.telegram_webhooks` предоставляет класс `TelegramBot` для создания и управления Telegram ботом, интегрированным с сервером FastAPI через RPC.

## Обзор

Этот модуль содержит класс `TelegramBot`, который используется для взаимодействия с Telegram API, управления обработчиками команд и сообщений, а также для регистрации вебхуков через RPC. Он позволяет запускать Telegram ботов, которые могут обрабатывать команды, текстовые сообщения, голосовые сообщения и документы.

## Подробнее

Модуль предоставляет возможность запускать Telegram ботов с использованием вебхуков или режима опроса (polling). Вебхуки регистрируются через RPC, что позволяет динамически добавлять маршруты для обработки сообщений.

## Классы

### `TelegramBot`

**Описание**: Класс для управления Telegram ботом.

**Принцип работы**:
Класс инициализируется с токеном Telegram бота и маршрутом для вебхука. Он создает экземпляр `Application` из библиотеки `telegram.ext` и регистрирует обработчики команд и сообщений. Класс также предоставляет методы для запуска и остановки бота, инициализации вебхука и регистрации маршрута через RPC.

**Атрибуты**:
- `token` (str): Токен Telegram бота.
- `port` (int): Порт для вебхука (по умолчанию 443).
- `route` (str): Маршрут для вебхука (по умолчанию 'telegram_webhook').
- `config` (SimpleNamespace): Конфигурация бота, загруженная из файла `telegram.json`.
- `application` (Application): Экземпляр `Application` из библиотеки `telegram.ext`.
- `handler` (BotHandler): Экземпляр класса `BotHandler`, который обрабатывает команды и сообщения.

**Методы**:
- `__init__(self, token: str, route: str = 'telegram_webhook')`: Инициализирует экземпляр класса `TelegramBot`.
- `run(self)`: Запускает бота и инициализирует RPC и вебхук.
- `_register_default_handlers(self)`: Регистрирует обработчики команд по умолчанию.
- `_handle_message(self, update: Update, context: CallbackContext) -> None`: Обрабатывает текстовые сообщения.
- `initialize_bot_webhook(self, route: str)`: Инициализирует вебхук для бота.
- `_register_route_via_rpc(self, rpc_client: ServerProxy)`: Регистрирует маршрут вебхука через RPC.
- `stop(self)`: Останавливает бота и удаляет вебхук.

## Функции

### `__init__`

```python
def __init__(self, token: str, route: str = 'telegram_webhook'):
    """
    Инициализирует экземпляр класса TelegramBot.

    Args:
        token (str): Токен Telegram бота.
        route (str): Webhook route for FastAPI. Defaults to '/telegram_webhook'.
    """
    ...
```

**Назначение**: Инициализация экземпляра класса `TelegramBot`.

**Параметры**:
- `token` (str): Токен Telegram бота.
- `route` (str, optional): Маршрут для вебхука. По умолчанию '/telegram_webhook'.

**Как работает функция**:
1. Сохраняет токен бота и маршрут вебхука в атрибутах экземпляра класса.
2. Загружает конфигурацию из файла `telegram.json` и сохраняет её в атрибуте `config`.
3. Создает экземпляр `Application` из библиотеки `telegram.ext` с использованием токена бота.
4. Создает экземпляр класса `BotHandler` и сохраняет его в атрибуте `handler`.
5. Регистрирует обработчики команд по умолчанию с помощью метода `_register_default_handlers`.

```
A: Сохранение токена и маршрута
|
B: Загрузка конфигурации из telegram.json
|
C: Создание экземпляра Application
|
D: Создание экземпляра BotHandler
|
E: Регистрация обработчиков команд по умолчанию
```

**Примеры**:
```python
from src.endpoints.bots.telegram.telegram_webhooks import TelegramBot
import os
from dotenv import load_dotenv
load_dotenv()

bot = TelegramBot(token=os.getenv('TELEGRAM_TOKEN'), route='/custom_webhook')
```

### `run`

```python
def run(self):
    """Запускает бота и инициализирует RPC и вебхук."""
    ...
```

**Назначение**: Запуск бота и инициализация RPC и вебхука.

**Как работает функция**:
1. Инициализирует RPC клиент для связи с сервером FastAPI.
2. Запускает сервер через RPC.
3. Регистрирует маршрут через RPC.
4. Инициализирует вебхук для бота.
5. Запускает приложение Telegram с использованием вебхука или режима опроса (polling), если не удалось настроить вебхук.

```
A: Инициализация RPC клиента
|
B: Запуск сервера через RPC
|
C: Регистрация маршрута через RPC
|
D: Инициализация вебхука
|
E: Запуск приложения Telegram (вебхук или polling)
```

**Примеры**:
```python
from src.endpoints.bots.telegram.telegram_webhooks import TelegramBot
import os
from dotenv import load_dotenv
load_dotenv()

bot = TelegramBot(token=os.getenv('TELEGRAM_TOKEN'))
bot.run()
```

### `_register_default_handlers`

```python
def _register_default_handlers(self):
    """Регистрирует обработчики команд по умолчанию."""
    ...
```

**Назначение**: Регистрация обработчиков команд по умолчанию.

**Как работает функция**:
Добавляет обработчики команд `start`, `help`, `sendpdf`, а также обработчики текстовых сообщений, голосовых сообщений и документов.

```
A: Добавление обработчика команды 'start'
|
B: Добавление обработчика команды 'help'
|
C: Добавление обработчика команды 'sendpdf'
|
D: Добавление обработчика текстовых сообщений
|
E: Добавление обработчика голосовых сообщений
|
F: Добавление обработчика документов
```

**Примеры**:
```python
from src.endpoints.bots.telegram.telegram_webhooks import TelegramBot
import os
from dotenv import load_dotenv
load_dotenv()

bot = TelegramBot(token=os.getenv('TELEGRAM_TOKEN'))
bot._register_default_handlers()
```

### `_handle_message`

```python
async def _handle_message(self, update: Update, context: CallbackContext) -> None:
    """Handle any text message."""
    ...
```

**Назначение**: Обработка текстовых сообщений.

**Параметры**:
- `update` (Update): Объект `Update` от Telegram API.
- `context` (CallbackContext): Контекст обратного вызова.

**Как работает функция**:
Передает обработку сообщения экземпляру `bot_handler`.

```
A: Передача обработки сообщения экземпляру bot_handler
```

**Примеры**:
```python
# Пример обработки сообщения (не вызывается напрямую, вызывается telegram.ext)
```

### `initialize_bot_webhook`

```python
def initialize_bot_webhook(self, route: str):
    """Инициализирует вебхук для бота."""
    ...
```

**Назначение**: Инициализация вебхука для бота.

**Параметры**:
- `route` (str): Маршрут для вебхука.

**Возвращает**:
- `webhook_url` (str): URL вебхука в случае успеха.
- `False` (bool): `False` в случае ошибки.

**Как работает функция**:
1. Формирует URL вебхука на основе хоста и маршрута.
2. Если хост локальный (`127.0.0.1` или `localhost`), использует `ngrok` для создания туннеля.
3. Устанавливает вебхук для бота с использованием метода `set_webhook` из Telegram API.

```
A: Формирование URL вебхука
|
B: Проверка, является ли хост локальным
|
C: Использование ngrok для создания туннеля (если хост локальный)
|
D: Установка вебхука для бота
```

**Примеры**:
```python
from src.endpoints.bots.telegram.telegram_webhooks import TelegramBot
import os
from dotenv import load_dotenv
load_dotenv()

bot = TelegramBot(token=os.getenv('TELEGRAM_TOKEN'))
webhook_url = bot.initialize_bot_webhook(route='/custom_webhook')
```

### `_register_route_via_rpc`

```python
def _register_route_via_rpc(self, rpc_client: ServerProxy):
    """Регистрирует маршрут Telegram webhook через RPC."""
    ...
```

**Назначение**: Регистрация маршрута вебхука через RPC.

**Параметры**:
- `rpc_client` (ServerProxy): RPC клиент для связи с сервером FastAPI.

**Как работает функция**:
Регистрирует маршрут для вебхука на сервере FastAPI через RPC, вызывая метод `add_new_route`.

```
A: Регистрация маршрута через RPC
```

**Примеры**:
```python
from xmlrpc.client import ServerProxy
from src.endpoints.bots.telegram.telegram_webhooks import TelegramBot
import os
from dotenv import load_dotenv
load_dotenv()

bot = TelegramBot(token=os.getenv('TELEGRAM_TOKEN'))
rpc_client = ServerProxy(f"http://{gs.host}:9000", allow_none=True)
bot._register_route_via_rpc(rpc_client)
```

### `stop`

```python
def stop(self):
    """Останавливает бота и удаляет вебхук."""
    ...
```

**Назначение**: Остановка бота и удаление вебхука.

**Как работает функция**:
Останавливает приложение Telegram и удаляет вебхук с использованием методов `stop` и `delete_webhook` из Telegram API.

```
A: Остановка приложения Telegram
|
B: Удаление вебхука
```

**Примеры**:
```python
from src.endpoints.bots.telegram.telegram_webhooks import TelegramBot
import os
from dotenv import load_dotenv
load_dotenv()

bot = TelegramBot(token=os.getenv('TELEGRAM_TOKEN'))
bot.stop()
```
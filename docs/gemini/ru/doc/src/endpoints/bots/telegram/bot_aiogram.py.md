# Модуль для работы с Telegram ботом через FastAPI и RPC
====================================================

Модуль содержит класс :class:`TelegramBot`, который используется для создания и управления Telegram ботом, работающим через сервер FastAPI и RPC.

Пример использования
----------------------

```python
from src.endpoints.bots.telegram.bot_aiogram import TelegramBot
import os
from dotenv import load_dotenv

load_dotenv()
bot = TelegramBot(os.getenv('TELEGRAM_TOKEN'))
bot.run()
```

## Обзор

Модуль `bot_aiogram.py` предоставляет реализацию Telegram бота, который интегрируется с сервером FastAPI через RPC. Он использует библиотеку `aiogram` для обработки взаимодействий с Telegram API и `xmlrpc.client` для связи с RPC-сервером.

## Подробней

Этот модуль является ключевым компонентом системы, позволяющим боту принимать и обрабатывать сообщения, а также выполнять различные команды. Он обеспечивает связь между Telegram API и внутренними сервисами, используя RPC для делегирования задач.
Модуль `TelegramBot` представляет собой Singleton, обеспечивая единую точку доступа к функциональности бота.

## Классы

### `TelegramBot`

**Описание**: Класс для управления Telegram ботом.

**Принцип работы**:
1.  Инициализируется с токеном Telegram бота и маршрутом для вебхука FastAPI.
2.  Настраивает бота и диспетчер `aiogram`.
3.  Регистрирует обработчики команд и сообщений.
4.  Инициализирует RPC-клиент для связи с сервером FastAPI.
5.  Запускает вебхук или long polling для обработки обновлений от Telegram.

**Аттрибуты**:

*   `token` (str): Токен Telegram бота.
*   `port` (int): Порт для вебхука. По умолчанию 443.
*   `route` (str): Маршрут вебхука для FastAPI. По умолчанию 'telegram\_webhook'.
*   `config` (SimpleNamespace): Объект конфигурации, загруженный из JSON-файла.
*   `bot` (Bot): Экземпляр бота `aiogram`.
*   `dp` (Dispatcher): Диспетчер `aiogram` для обработки обновлений.
*   `bot_handler` (BotHandler): Экземпляр класса `BotHandler` для обработки сообщений и команд.
*   `app` (Optional[web.Application]): Веб-приложение `aiohttp` для вебхука.
*   `rpc_client` (Optional[ServerProxy]): RPC-клиент для связи с сервером FastAPI.

**Методы**:

*   `__init__`: Инициализирует экземпляр класса `TelegramBot`.
*   `run`: Запускает бота и инициализирует RPC и вебхук.
*   `_register_default_handlers`: Регистрирует обработчики команд и сообщений.
*   `_handle_message`: Обрабатывает текстовые сообщения.
*   `initialize_bot_webhook`: Инициализирует вебхук бота.
*   `_register_route_via_rpc`: Регистрирует маршрут вебхука Telegram через RPC.
*   `stop`: Останавливает бота и удаляет вебхук.

## Функции

### `__init__`

```python
def __init__(self, token: str, route: str = 'telegram_webhook'):
    """
    Инициализирует экземпляр класса `TelegramBot`.

    Args:
        token (str): Токен Telegram бота.
        route (str): Webhook route for FastAPI. Defaults to '/telegram_webhook'.
    """
    ...
```

**Назначение**: Инициализация экземпляра класса `TelegramBot`.

**Параметры**:

*   `token` (str): Токен Telegram бота.
*   `route` (str): Webhook route for FastAPI. Defaults to '/telegram\_webhook'.

**Как работает функция**:

1.  Сохраняет переданные параметры `token` и `route` в атрибуты экземпляра класса.
2.  Устанавливает порт по умолчанию равным 443.
3.  Загружает конфигурацию из JSON-файла с использованием `j_loads_ns`.
4.  Создает экземпляры `Bot` и `Dispatcher` из библиотеки `aiogram`.
5.  Создает экземпляр класса `BotHandler` для обработки логики бота.
6.  Регистрирует обработчики команд и сообщений с помощью метода `_register_default_handlers`.
7.  Инициализирует атрибуты `app` и `rpc_client` значением `None`.

### `run`

```python
def run(self):
    """Run the bot and initialize RPC and webhook."""
    ...
```

**Назначение**: Запуск бота, инициализация RPC и вебхука.

**Как работает функция**:

1.  Инициализирует RPC-клиент для взаимодействия с сервером FastAPI.
2.  Запускает RPC-сервер через RPC-клиент.
3.  Инициализирует вебхук Telegram бота.
4.  Регистрирует маршрут для вебхука через RPC.
5.  Создает и запускает веб-приложение `aiohttp` для обработки вебхука.
6.  Если не удалось инициализировать вебхук, запускает long polling для обработки обновлений от Telegram.

```
  Начало
    ↓
  Инициализация RPC-клиента
    │
    ├── Запуск RPC-сервера
    │   │
    │   └── Регистрация маршрута через RPC
    │       │
    │       └── Инициализация вебхука Telegram
    │           │
    │           └── Регистрация маршрута вебхука через RPC
    │               │
    │               └── Запуск веб-приложения aiohttp
    │                   │
    │                   └── Обработка обновлений через вебхук
    │
    └── Запуск long polling (если вебхук не удалось инициализировать)
    ↓
  Конец
```

**Примеры**:

```python
from src.endpoints.bots.telegram.bot_aiogram import TelegramBot
import os
from dotenv import load_dotenv

load_dotenv()
bot = TelegramBot(os.getenv('TELEGRAM_TOKEN'))
bot.run()
```

### `_register_default_handlers`

```python
def _register_default_handlers(self):
    """Register the default handlers using the BotHandler instance."""
    ...
```

**Назначение**: Регистрация обработчиков команд и сообщений.

**Как работает функция**:

1.  Регистрирует обработчик для команды `/start`.
2.  Регистрирует обработчик для команды `/help`.
3.  Регистрирует обработчик для команды `/sendpdf`.
4.  Регистрирует обработчик для текстовых сообщений.
5.  Регистрирует обработчик для голосовых сообщений.
6.  Регистрирует обработчик для документов.
7.  Регистрирует обработчик для логов.

```
  Начало
    ↓
  Регистрация обработчика /start
    ↓
  Регистрация обработчика /help
    ↓
  Регистрация обработчика /sendpdf
    ↓
  Регистрация обработчика текстовых сообщений
    ↓
  Регистрация обработчика голосовых сообщений
    ↓
  Регистрация обработчика документов
    ↓
  Регистрация обработчика логов
    ↓
  Конец
```

**Примеры**:

```python
bot = TelegramBot(os.getenv('TELEGRAM_TOKEN'))
bot._register_default_handlers()
```

### `_handle_message`

```python
async def _handle_message(self, message: types.Message):
    """Handle any text message."""
    ...
```

**Назначение**: Обработка текстовых сообщений.

**Параметры**:

*   `message` (types.Message): Объект сообщения `aiogram`.

**Как работает функция**:

1.  Передает сообщение обработчику `handle_message` экземпляра `BotHandler`.

```
  Начало
    ↓
  Передача сообщения обработчику BotHandler
    ↓
  Конец
```

**Примеры**:

```python
message = types.Message(text='Hello')
await bot._handle_message(message)
```

### `initialize_bot_webhook`

```python
def initialize_bot_webhook(self, route: str):
    """Initialize the bot webhook."""
    ...
```

**Назначение**: Инициализация вебхука бота.

**Параметры**:

*   `route` (str): Маршрут вебхука.

**Как работает функция**:

1.  Формирует URL вебхука на основе хоста и маршрута.
2.  Если хост указывает на локальный адрес, использует `pyngrok` для создания туннеля.
3.  Устанавливает вебхук для бота с использованием `bot.set_webhook`.
4.  Логирует информацию о вебхуке.

```
  Начало
    ↓
  Формирование URL вебхука
    │
    ├── Использование pyngrok для создания туннеля (если хост локальный)
    │   │
    │   └── Установка вебхука для бота
    │       │
    │       └── Логирование информации о вебхуке
    │
    └── Обработка ошибок при установке вебхука
    ↓
  Конец
```

**Примеры**:

```python
webhook_url = bot.initialize_bot_webhook('/telegram_webhook')
```

### `_register_route_via_rpc`

```python
def _register_route_via_rpc(self, rpc_client: ServerProxy):
    """Register the Telegram webhook route via RPC."""
    ...
```

**Назначение**: Регистрация маршрута вебхука Telegram через RPC.

**Параметры**:

*   `rpc_client` (ServerProxy): RPC-клиент.

**Как работает функция**:

1.  Регистрирует маршрут вебхука через RPC-клиент.
2.  Логирует информацию о регистрации маршрута.

```
  Начало
    ↓
  Регистрация маршрута вебхука через RPC-клиент
    ↓
  Логирование информации о регистрации маршрута
    ↓
  Обработка ошибок при регистрации маршрута
    ↓
  Конец
```

**Примеры**:

```python
bot._register_route_via_rpc(bot.rpc_client)
```

### `stop`

```python
def stop(self):
    """Stop the bot and delete the webhook."""
    ...
```

**Назначение**: Остановка бота и удаление вебхука.

**Как работает функция**:

1.  Останавливает веб-приложение `aiohttp`, если оно запущено.
2.  Удаляет вебхук бота.
3.  Логирует информацию об остановке бота.

```
  Начало
    ↓
  Остановка веб-приложения aiohttp (если запущено)
    ↓
  Удаление вебхука бота
    ↓
  Логирование информации об остановке бота
    ↓
  Обработка ошибок при удалении вебхука
    ↓
  Конец
```

**Примеры**:

```python
bot.stop()
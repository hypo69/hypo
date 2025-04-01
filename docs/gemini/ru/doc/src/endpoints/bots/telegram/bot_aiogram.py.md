# Модуль для работы с Telegram ботом через FastAPI и RPC
====================================================

Модуль содержит класс `TelegramBot`, который используется для создания и управления Telegram ботом, интегрированным с сервером FastAPI через RPC.

## Обзор

Этот модуль обеспечивает создание, запуск и остановку Telegram бота, а также регистрацию обработчиков команд и вебхуков. Он использует FastAPI для обработки вебхуков и RPC для взаимодействия с другими сервисами.

## Подробней

Этот код определяет класс `TelegramBot`, который управляет Telegram ботом. Он использует библиотеку `aiogram` для обработки Telegram сообщений и `FastAPI` для создания вебхука. RPC используется для связи с другими сервисами. Класс инициализирует бота, регистрирует обработчики, запускает сервер и обрабатывает ошибки. Он также поддерживает установку и удаление вебхуков, а также регистрацию маршрутов через RPC.

## Классы

### `TelegramBot`

Описание: Класс для управления Telegram ботом через FastAPI и RPC.
        **Наследует**: 
            Класс не наследует другие классы

         **Аттрибуты**:
            token (str): Токен Telegram бота.
            port (int): Порт для вебхука. По умолчанию 443.
            route (str): Маршрут для вебхука FastAPI. По умолчанию 'telegram_webhook'.
            config (SimpleNamespace): Конфигурация бота, загруженная из JSON файла.
            bot (Bot): Экземпляр бота aiogram.
            dp (Dispatcher): Диспетчер aiogram.
            bot_handler (BotHandler): Обработчик бота.
            app (Optional[web.Application]): Веб-приложение aiohttp.
            rpc_client (Optional[ServerProxy]): RPC клиент для взаимодействия с сервером.

         **Методы**:
            run(): Запускает бота и инициализирует RPC и вебхук.
            _register_default_handlers(): Регистрирует обработчики команд по умолчанию.
            _handle_message(message): Обрабатывает текстовые сообщения.
            initialize_bot_webhook(route): Инициализирует вебхук бота.
            _register_route_via_rpc(rpc_client): Регистрирует маршрут вебхука Telegram через RPC.
            stop(): Останавливает бота и удаляет вебхук.

#### Принцип работы:

1.  **Инициализация**: Класс `TelegramBot` инициализируется с токеном, маршрутом вебхука и другими параметрами. Он загружает конфигурацию из JSON файла, создает экземпляры `Bot` и `Dispatcher` из библиотеки `aiogram`, а также создает экземпляр `BotHandler` для обработки сообщений.
2.  **Регистрация обработчиков**: Метод `_register_default_handlers` регистрирует обработчики команд по умолчанию, такие как `/start`, `/help`, `/sendpdf`, а также обработчики текстовых сообщений, голосовых сообщений и документов.
3.  **Запуск бота**: Метод `run` запускает бота. Он инициализирует RPC клиент, запускает RPC сервер, регистрирует маршрут вебхука через RPC и запускает веб-приложение `aiohttp` для обработки вебхуков. Если вебхук не удается инициализировать, бот запускается в режиме опроса (`polling`).
4.  **Обработка сообщений**: Когда Telegram бот получает сообщение, оно обрабатывается соответствующим обработчиком, зарегистрированным в диспетчере `dp`. Например, текстовые сообщения обрабатываются методом `_handle_message`, который вызывает метод `handle_message` экземпляра `BotHandler`.
5.  **Остановка бота**: Метод `stop` останавливает бота, удаляет вебхук и закрывает веб-приложение `aiohttp`.

```ascii
TelegramBot
│
├── __init__ (Инициализация бота и его компонентов)
│   │
│   ├── Загрузка конфигурации из telegram.json
│   │
│   ├── Создание экземпляров Bot, Dispatcher, BotHandler
│   │
│   └── Регистрация обработчиков по умолчанию
│
├── run (Запуск бота и инициализация RPC и вебхука)
│   │
│   ├── Инициализация RPC клиента и сервера
│   │
│   ├── Регистрация маршрута через RPC
│   │
│   └── Инициализация и запуск веб-приложения aiohttp
│       │
│       └── Регистрация обработчика вебхуков
│
├── _register_default_handlers (Регистрация обработчиков команд)
│   │
│   └── Регистрация обработчиков для /start, /help, /sendpdf и других команд
│
├── _handle_message (Обработка текстовых сообщений)
│   │
│   └── Вызов BotHandler.handle_message для обработки сообщения
│
├── initialize_bot_webhook (Инициализация вебхука бота)
│   │
│   ├── Определение URL вебхука
│   │
│   └── Установка вебхука через bot.set_webhook
│
├── _register_route_via_rpc (Регистрация маршрута вебхука через RPC)
│   │
│   └── Вызов rpc_client.add_new_route для регистрации маршрута
│
└── stop (Остановка бота и удаление вебхука)
    │
    ├── Остановка веб-приложения aiohttp
    │
    └── Удаление вебхука через bot.delete_webhook
```

**Примеры**

```python
from src.endpoints.bots.telegram.bot_aiogram import TelegramBot
import os
from dotenv import load_dotenv

load_dotenv()

# Инициализация и запуск бота с использованием токена из переменной окружения
bot = TelegramBot(token=os.getenv('TELEGRAM_TOKEN'))
bot.run()

# Остановка бота
bot.stop()
```

## Функции

### `TelegramBot.__init__`

```python
 def __init__(self, token: str, route: str = 'telegram_webhook'):
        """
        Initialize the TelegramBot instance.

        Args:
            token (str): Telegram bot token.
            route (str): Webhook route for FastAPI. Defaults to '/telegram_webhook'.
        """
```

**Назначение**: Инициализация экземпляра класса `TelegramBot`.

**Параметры**:

*   `token` (str): Токен Telegram бота.
*   `route` (str): Маршрут вебхука для FastAPI. По умолчанию `/telegram_webhook`.

**Как работает функция**:

1.  Сохраняет токен и маршрут вебхука в атрибутах экземпляра класса.
2.  Загружает конфигурацию из JSON файла `telegram.json` с использованием `j_loads_ns`.
3.  Создает экземпляры `Bot` и `Dispatcher` из библиотеки `aiogram`.
4.  Создает экземпляр `BotHandler` для обработки сообщений.
5.  Регистрирует обработчики команд по умолчанию.

```ascii
__init__
│
├── Сохранение токена и маршрута
│
├── Загрузка конфигурации из telegram.json
│
├── Создание экземпляров Bot, Dispatcher, BotHandler
│
└── Регистрация обработчиков по умолчанию
```

**Примеры**:

```python
from src.endpoints.bots.telegram.bot_aiogram import TelegramBot

# Инициализация TelegramBot с токеном и маршрутом по умолчанию
bot = TelegramBot(token='your_token')

# Инициализация TelegramBot с указанием токена и маршрута
bot = TelegramBot(token='your_token', route='/custom_route')
```

### `TelegramBot.run`

```python
    def run(self):
        """Run the bot and initialize RPC and webhook."""
```

**Назначение**: Запуск бота, инициализация RPC и вебхука.

**Как работает функция**:

1.  Инициализирует RPC клиент для взаимодействия с RPC сервером.
2.  Запускает RPC сервер.
3.  Регистрирует маршрут вебхука через RPC.
4.  Инициализирует и запускает веб-приложение `aiohttp` для обработки вебхуков.
5.  Если инициализация вебхука не удалась, запускает бота в режиме опроса (`polling`).
6.  Логирует успешный запуск RPC сервера и приложения.

```ascii
run
│
├── Инициализация RPC клиента
│   │
│   └── Создание ServerProxy для взаимодействия с RPC сервером
│
├── Запуск RPC сервера
│   │
│   └── Вызов rpc_client.start_server для запуска сервера
│
├── Регистрация маршрута через RPC
│   │
│   └── Вызов _register_route_via_rpc для регистрации маршрута
│
├── Инициализация и запуск веб-приложения aiohttp
│   │
│   └── Создание web.Application и регистрация обработчика вебхуков
│
└── Запуск бота в режиме опроса (если не удалось установить вебхук)
```

**Примеры**:

```python
from src.endpoints.bots.telegram.bot_aiogram import TelegramBot
import os
from dotenv import load_dotenv

load_dotenv()

# Инициализация и запуск бота
bot = TelegramBot(token=os.getenv('TELEGRAM_TOKEN'))
bot.run()
```

### `TelegramBot._register_default_handlers`

```python
    def _register_default_handlers(self):
        """Register the default handlers using the BotHandler instance."""
```

**Назначение**: Регистрация обработчиков команд по умолчанию с использованием экземпляра `BotHandler`.

**Как работает функция**:

1.  Регистрирует обработчики для команд `/start`, `/help`, `/sendpdf`.
2.  Регистрирует обработчик для текстовых сообщений (`_handle_message`).
3.  Регистрирует обработчики для голосовых сообщений и документов.
4.  Регистрирует обработчик для логов.

```ascii
_register_default_handlers
│
├── Регистрация обработчиков для /start, /help, /sendpdf
│
├── Регистрация обработчика для текстовых сообщений (_handle_message)
│
├── Регистрация обработчиков для голосовых сообщений и документов
│
└── Регистрация обработчика для логов
```

**Примеры**:

```python
from src.endpoints.bots.telegram.bot_aiogram import TelegramBot
import os
from dotenv import load_dotenv

load_dotenv()

# Инициализация бота
bot = TelegramBot(token=os.getenv('TELEGRAM_TOKEN'))

# Регистрация обработчиков по умолчанию
bot._register_default_handlers()
```

### `TelegramBot._handle_message`

```python
    async def _handle_message(self, message: types.Message):
        """Handle any text message."""
```

**Назначение**: Обработка любого текстового сообщения.

**Параметры**:

*   `message` (types.Message): Объект сообщения `aiogram`.

**Как работает функция**:

1.  Вызывает метод `handle_message` экземпляра `BotHandler` для обработки сообщения.

```ascii
_handle_message
│
└── Вызов BotHandler.handle_message для обработки сообщения
```

**Примеры**:

```python
from aiogram import types
from src.endpoints.bots.telegram.bot_aiogram import TelegramBot
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

# Инициализация бота
bot = TelegramBot(token=os.getenv('TELEGRAM_TOKEN'))

# Создание экземпляра сообщения (для примера)
message = types.Message(text='Привет, бот!')

# Обработка сообщения
asyncio.run(bot._handle_message(message))
```

### `TelegramBot.initialize_bot_webhook`

```python
    def initialize_bot_webhook(self, route: str):
        """Initialize the bot webhook."""
```

**Назначение**: Инициализация вебхука бота.

**Параметры**:

*   `route` (str): Маршрут вебхука.

**Как работает функция**:

1.  Формирует URL вебхука на основе хоста и маршрута.
2.  Если хост указан как `127.0.0.1` или `localhost`, использует `ngrok` для создания туннеля.
3.  Устанавливает вебхук с использованием `bot.set_webhook`.
4.  Логирует URL для проверки вебхука.

```ascii
initialize_bot_webhook
│
├── Формирование URL вебхука
│   │
│   ├── Определение хоста и маршрута
│   │
│   └── Использование ngrok для создания туннеля (если хост локальный)
│
└── Установка вебхука
    │
    └── Вызов bot.set_webhook для установки вебхука
```

**Примеры**:

```python
from src.endpoints.bots.telegram.bot_aiogram import TelegramBot
import os
from dotenv import load_dotenv

load_dotenv()

# Инициализация бота
bot = TelegramBot(token=os.getenv('TELEGRAM_TOKEN'))

# Инициализация вебхука
webhook_url = bot.initialize_bot_webhook(route='/webhook')
print(f'Webhook URL: {webhook_url}')
```

### `TelegramBot._register_route_via_rpc`

```python
    def _register_route_via_rpc(self, rpc_client: ServerProxy):
        """Register the Telegram webhook route via RPC."""
```

**Назначение**: Регистрация маршрута вебхука Telegram через RPC.

**Параметры**:

*   `rpc_client` (ServerProxy): RPC клиент для взаимодействия с сервером.

**Как работает функция**:

1.  Формирует маршрут вебхука.
2.  Вызывает метод `add_new_route` RPC клиента для регистрации маршрута.
3.  Логирует успешную регистрацию маршрута.

```ascii
_register_route_via_rpc
│
├── Формирование маршрута вебхука
│
└── Регистрация маршрута через RPC
    │
    └── Вызов rpc_client.add_new_route для регистрации маршрута
```

**Примеры**:

```python
from xmlrpc.client import ServerProxy
from src.endpoints.bots.telegram.bot_aiogram import TelegramBot
import os
from dotenv import load_dotenv

load_dotenv()

# Инициализация бота
bot = TelegramBot(token=os.getenv('TELEGRAM_TOKEN'))

# Создание RPC клиента (для примера)
rpc_client = ServerProxy(f"http://localhost:9000", allow_none=True)

# Регистрация маршрута через RPC
bot._register_route_via_rpc(rpc_client)
```

### `TelegramBot.stop`

```python
    def stop(self):
         """Stop the bot and delete the webhook."""
```

**Назначение**: Остановка бота и удаление вебхука.

**Как работает функция**:

1.  Останавливает веб-приложение `aiohttp`.
2.  Удаляет вебхук с использованием `bot.delete_webhook`.
3.  Логирует остановку бота.

```ascii
stop
│
├── Остановка веб-приложения aiohttp
│
└── Удаление вебхука
    │
    └── Вызов bot.delete_webhook для удаления вебхука
```

**Примеры**:

```python
from src.endpoints.bots.telegram.bot_aiogram import TelegramBot
import os
from dotenv import load_dotenv

load_dotenv()

# Инициализация и запуск бота
bot = TelegramBot(token=os.getenv('TELEGRAM_TOKEN'))
bot.run()

# Остановка бота
bot.stop()
```

```python
if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    bot = TelegramBot(os.getenv('TELEGRAM_TOKEN'))
    bot.run()
```

Этот блок кода выполняется только при запуске скрипта напрямую (а не при импорте как модуля). Он загружает переменные окружения из файла `.env`, создает экземпляр класса `TelegramBot` с использованием токена, полученного из переменной окружения `TELEGRAM_TOKEN`, и запускает бота.
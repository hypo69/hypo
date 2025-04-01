# Модуль для работы с Telegram ботом через FastAPI и RPC
====================================================

Модуль `src.endpoints.bots.telegram.telegram_webhooks` предназначен для создания и управления Telegram ботом, интегрированным с сервером FastAPI через RPC.

## Обзор

Модуль содержит класс `TelegramBot`, который предоставляет интерфейс для взаимодействия с Telegram API, регистрации обработчиков команд и сообщений, а также настройки вебхуков для получения обновлений от Telegram.

## Подробней

Этот модуль позволяет запускать Telegram ботов, которые могут обрабатывать команды, текстовые сообщения, голосовые сообщения и документы. Он использует FastAPI для создания веб-сервера, который принимает обновления от Telegram через вебхук. Для взаимодействия между Telegram ботом и сервером FastAPI используется RPC.

## Классы

### `TelegramBot`

**Описание**: Класс `TelegramBot` представляет собой интерфейс для Telegram бота. Он инициализирует бота, регистрирует обработчики команд и сообщений, настраивает вебхуки и запускает бота. Класс реализован как Singleton.

**Атрибуты**:
- `token` (str): Токен Telegram бота.
- `port` (int): Порт для вебхука FastAPI. По умолчанию `443`.
- `route` (str): Маршрут вебхука для FastAPI. По умолчанию `telegram_webhook`.
- `config` (SimpleNamespace): Конфигурация бота, загруженная из файла `telegram.json`.
- `application` (Application): Объект `Application` из библиотеки `python-telegram-bot`, используемый для управления ботом.
- `handler` (BotHandler): Экземпляр класса `BotHandler`, используемый для обработки команд и сообщений.

**Методы**:
- `__init__(token: str, route: str = 'telegram_webhook')`: Инициализирует экземпляр класса `TelegramBot`.
- `run()`: Запускает бота, инициализирует RPC и вебхук.
- `_register_default_handlers()`: Регистрирует обработчики команд по умолчанию.
- `_handle_message(update: Update, context: CallbackContext) -> None`: Обрабатывает текстовые сообщения.
- `initialize_bot_webhook(route: str)`: Инициализирует вебхук бота.
- `_register_route_via_rpc(rpc_client: ServerProxy)`: Регистрирует маршрут вебхука Telegram через RPC.
- `stop()`: Останавливает бота и удаляет вебхук.

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

**Назначение**: Инициализирует экземпляр класса `TelegramBot`.

**Параметры**:
- `token` (str): Токен Telegram бота.
- `route` (str): Маршрут вебхука для FastAPI. По умолчанию `/telegram_webhook`.

**Как работает функция**:
1. Сохраняет токен Telegram бота в атрибуте `token`.
2. Устанавливает порт для вебхука FastAPI в атрибуте `port`.
3. Устанавливает маршрут вебхука FastAPI в атрибуте `route`.
4. Загружает конфигурацию бота из файла `telegram.json` и сохраняет ее в атрибуте `config`.
5. Создает экземпляр класса `Application` из библиотеки `python-telegram-bot` и сохраняет его в атрибуте `application`.
6. Создает экземпляр класса `BotHandler` и сохраняет его в атрибуте `handler`.
7. Регистрирует обработчики команд по умолчанию, используя метод `_register_default_handlers()`.

```
A[Инициализация атрибутов класса]
|
B[Загрузка конфигурации из telegram.json]
|
C[Создание экземпляра Application]
|
D[Создание экземпляра BotHandler]
|
E[Регистрация обработчиков по умолчанию]
```

### `run`

```python
def run(self):
    """Run the bot and initialize RPC and webhook."""
```

**Назначение**: Запускает бота, инициализирует RPC и вебхук.

**Как работает функция**:

1.  Инициализирует RPC клиент для взаимодействия с сервером FastAPI.
2.  Запускает сервер через RPC.
3.  Регистрирует маршрут через RPC.
4.  Инициализирует вебхук Telegram бота, используя метод `initialize_bot_webhook()`.
5.  Если вебхук успешно инициализирован, регистрирует маршрут через RPC, используя метод `_register_route_via_rpc()`.
6.  Запускает приложение Telegram бота, используя метод `run_webhook()`.
7.  Если инициализация вебхука не удалась, запускает бота в режиме опроса, используя метод `run_polling()`.

```
A[Инициализация RPC клиента]
|
B[Запуск сервера через RPC]
|
C[Регистрация маршрута через RPC]
|
D[Инициализация вебхука Telegram бота]
|
E[Проверка успешности инициализации вебхука]
|
F[Регистрация маршрута через RPC (если вебхук успешен)]
|
G[Запуск приложения Telegram бота (через вебхук или опрос)]
```

### `_register_default_handlers`

```python
def _register_default_handlers(self):
    """Register the default handlers using the BotHandler instance."""
```

**Назначение**: Регистрирует обработчики команд по умолчанию.

**Как работает функция**:
1.  Добавляет обработчик для команды `/start`, используя метод `add_handler()` и метод `start()` из класса `BotHandler`.
2.  Добавляет обработчик для команды `/help`, используя метод `add_handler()` и метод `help_command()` из класса `BotHandler`.
3.  Добавляет обработчик для команды `/sendpdf`, используя метод `add_handler()` и метод `send_pdf()` из класса `BotHandler`.
4.  Добавляет обработчик для текстовых сообщений, используя метод `add_handler()` и метод `_handle_message()`.
5.  Добавляет обработчик для голосовых сообщений, используя метод `add_handler()` и метод `handle_voice()` из класса `BotHandler`.
6.  Добавляет обработчик для документов, используя метод `add_handler()` и метод `handle_document()` из класса `BotHandler`.
7.  Добавляет обработчик для текстовых сообщений для логирования, используя метод `add_handler()` и метод `handle_log()` из класса `BotHandler`.

```
A[Добавление обработчика для команды /start]
|
B[Добавление обработчика для команды /help]
|
C[Добавление обработчика для команды /sendpdf]
|
D[Добавление обработчика для текстовых сообщений]
|
E[Добавление обработчика для голосовых сообщений]
|
F[Добавление обработчика для документов]
|
G[Добавление обработчика для текстовых сообщений для логирования]
```

### `_handle_message`

```python
async def _handle_message(self, update: Update, context: CallbackContext) -> None:
    """Handle any text message."""
```

**Назначение**: Обрабатывает текстовые сообщения.

**Параметры**:
- `update` (Update): Объект `Update` из библиотеки `python-telegram-bot`, содержащий информацию об обновлении.
- `context` (CallbackContext): Объект `CallbackContext` из библиотеки `python-telegram-bot`, содержащий информацию о контексте обработки обновления.

**Как работает функция**:
1. Вызывает метод `handle_message()` из класса `BotHandler`, передавая ему объекты `update` и `context`.

```
A[Вызов метода handle_message() из класса BotHandler]
```

### `initialize_bot_webhook`

```python
def initialize_bot_webhook(self, route: str):
    """Initialize the bot webhook."""
```

**Назначение**: Инициализирует вебхук бота.

**Параметры**:
- `route` (str): Маршрут вебхука.

**Как работает функция**:

1.  Формирует URL вебхука на основе переданного маршрута и хоста.
2.  Если хост является локальным (127.0.0.1 или localhost), использует `ngrok` для создания туннеля к локальному серверу.
3.  Устанавливает вебхук для бота, используя метод `set_webhook()`.

```
A[Формирование URL вебхука]
|
B[Проверка, является ли хост локальным]
|
C[Использование ngrok для создания туннеля (если хост локальный)]
|
D[Установка вебхука для бота]
```

### `_register_route_via_rpc`

```python
def _register_route_via_rpc(self, rpc_client: ServerProxy):
    """Register the Telegram webhook route via RPC."""
```

**Назначение**: Регистрирует маршрут вебхука Telegram через RPC.

**Параметры**:
- `rpc_client` (ServerProxy): Объект `ServerProxy` для взаимодействия с RPC-сервером.

**Как работает функция**:

1.  Формирует маршрут вебхука.
2.  Вызывает метод `add_new_route()` на RPC-сервере для регистрации маршрута.

```
A[Формирование маршрута вебхука]
|
B[Вызов метода add_new_route() на RPC-сервере]
```

### `stop`

```python
def stop(self):
    """Stop the bot and delete the webhook."""
```

**Назначение**: Останавливает бота и удаляет вебхук.

**Как работает функция**:

1.  Останавливает приложение Telegram бота, используя метод `stop()`.
2.  Удаляет вебхук, используя метод `delete_webhook()`.

```
A[Остановка приложения Telegram бота]
|
B[Удаление вебхука]
```

## Функции

В данном модуле функции отсутствуют. Весь функционал реализован через методы класса `TelegramBot`.

## Примеры

Пример использования класса `TelegramBot`:

```python
from src.endpoints.bots.telegram.telegram_webhooks import TelegramBot
import os
from dotenv import load_dotenv

load_dotenv()
bot = TelegramBot(os.getenv('TELEGRAM_TOKEN'))
bot.run()
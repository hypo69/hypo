# Модуль telegram_webhooks
## Обзор

Модуль `telegram_webhooks.py` предоставляет реализацию Telegram-бота через сервер FastAPI с использованием RPC (Remote Procedure Call). Он включает в себя настройку вебхуков, обработку команд и сообщений от пользователей Telegram, а также взаимодействие с другими сервисами через RPC.

## Подробней

Этот модуль является частью проекта `hypotez` и отвечает за интеграцию с Telegram через ботов. Он использует FastAPI для создания веб-сервера, который принимает обновления от Telegram и обрабатывает их. Для взаимодействия с другими частями системы используется RPC, что позволяет распределить нагрузку и упростить архитектуру.

## Классы

### `TelegramBot`

**Описание**: Класс `TelegramBot` представляет собой интерфейс для управления Telegram-ботом. Он инициализирует бота, регистрирует обработчики команд и сообщений, настраивает вебхуки и запускает бота.

**Принцип работы**:
1.  При инициализации класса создается экземпляр приложения Telegram Bot с использованием предоставленного токена.
2.  Загружается конфигурация из файла `telegram.json`.
3.  Регистрируются обработчики команд и сообщений по умолчанию.
4.  При запуске бота инициализируется RPC-клиент для взаимодействия с сервером FastAPI.
5.  Настраивается вебхук для приема обновлений от Telegram.
6.  Бот запускается либо в режиме вебхука, либо в режиме опроса (polling).

**Аттрибуты**:

*   `token` (str): Токен Telegram-бота.
*   `port` (int): Порт для вебхука. По умолчанию 443.
*   `route` (str): Маршрут для вебхука FastAPI. По умолчанию `telegram_webhook`.
*   `config` (SimpleNamespace): Конфигурация бота, загруженная из файла `telegram.json`.
*   `application` (Application): Экземпляр приложения Telegram Bot.
*   `handler` (BotHandler): Экземпляр класса `BotHandler` для обработки команд и сообщений.

**Методы**:

*   `__init__(self, token: str, route: str = 'telegram_webhook')`: Инициализирует экземпляр класса `TelegramBot`.
*   `run(self)`: Запускает бота, инициализирует RPC и вебхук.
*   `_register_default_handlers(self)`: Регистрирует обработчики команд по умолчанию, такие как `/start`, `/help`, `/sendpdf`, а также обработчики текстовых сообщений, голосовых сообщений и документов.
*   `_handle_message(self, update: Update, context: CallbackContext) -> None`: Обрабатывает текстовые сообщения, перенаправляя их в `bot_handler`.
*   `initialize_bot_webhook(self, route: str)`: Инициализирует вебхук для бота.
*   `_register_route_via_rpc(self, rpc_client: ServerProxy)`: Регистрирует маршрут Telegram webhook через RPC.
*   `stop(self)`: Останавливает бота и удаляет вебхук.

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

**Назначение**: Инициализация экземпляра класса `TelegramBot`.

**Параметры**:

*   `token` (str): Токен Telegram-бота, полученный от BotFather.
*   `route` (str, optional): Маршрут вебхука для FastAPI. Используется для определения URL, по которому Telegram будет отправлять обновления. По умолчанию '/telegram_webhook'.

**Как работает функция**:

1.  Сохраняет переданные значения токена и маршрута в атрибуты экземпляра класса.
2.  Загружает конфигурацию из JSON-файла `telegram.json` с использованием функции `j_loads_ns`.
3.  Инициализирует приложение Telegram Bot с использованием предоставленного токена.
4.  Создает экземпляр класса `BotHandler`, который будет использоваться для обработки входящих сообщений и команд.
5.  Вызывает метод `_register_default_handlers` для регистрации стандартных обработчиков команд.

```
    A (Сохранение параметров)
    ↓
    B (Загрузка конфигурации)
    ↓
    C (Инициализация приложения Telegram Bot)
    ↓
    D (Создание экземпляра BotHandler)
    ↓
    E (Регистрация стандартных обработчиков)
```

**Примеры**:

```python
bot = TelegramBot(token='YOUR_TELEGRAM_BOT_TOKEN', route='/custom_webhook')
```

### `run`

```python
def run(self):
    """Run the bot and initialize RPC and webhook."""
    ...
```

**Назначение**: Запуск бота и инициализация RPC и вебхука.

**Как работает функция**:

1.  Инициализирует RPC-клиент для взаимодействия с сервером FastAPI. Адрес сервера берется из глобальной переменной `gs.host`.
2.  Вызывает RPC-метод `start_server` для запуска сервера FastAPI на указанном порту и хосте.
3.  Инициализирует вебхук для приема обновлений от Telegram.
4.  Запускает приложение Telegram Bot в режиме вебхука, указывая URL вебхука, порт и адрес для прослушивания.
5.  В случае ошибки при инициализации RPC или вебхука, регистрирует ошибку в лог и завершает работу.
6.  Если не удалось настроить вебхук, запускает бота в режиме опроса (polling).

```
    A (Инициализация RPC-клиента)
    ↓
    B (Запуск сервера FastAPI через RPC)
    ↓
    C (Инициализация вебхука)
    ↓
    D (Запуск приложения Telegram Bot в режиме вебхука или опроса)
```

**Примеры**:

```python
bot = TelegramBot(token='YOUR_TELEGRAM_BOT_TOKEN')
bot.run()
```

### `_register_default_handlers`

```python
def _register_default_handlers(self):
    """Register the default handlers using the BotHandler instance."""
    ...
```

**Назначение**: Регистрация обработчиков команд по умолчанию.

**Как работает функция**:

1.  Добавляет обработчики команд `/start`, `/help`, `/sendpdf` к приложению Telegram Bot, используя методы из экземпляра класса `BotHandler`.
2.  Добавляет обработчик текстовых сообщений, который перенаправляет сообщения в метод `_handle_message`.
3.  Добавляет обработчики голосовых сообщений и документов, использующие соответствующие методы из `BotHandler`.
4.  Добавляет обработчик логов.

```
    A (Добавление обработчика команды /start)
    ↓
    B (Добавление обработчика команды /help)
    ↓
    C (Добавление обработчика команды /sendpdf)
    ↓
    D (Добавление обработчика текстовых сообщений)
    ↓
    E (Добавление обработчика голосовых сообщений)
    ↓
    F (Добавление обработчика документов)
    ↓
    G (Добавление обработчика логов)
```

**Примеры**:

```python
bot = TelegramBot(token='YOUR_TELEGRAM_BOT_TOKEN')
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

*   `update` (Update): Объект `Update` от Telegram, содержащий информацию о входящем сообщении.
*   `context` (CallbackContext): Контекст обратного вызова, используемый для передачи данных между обработчиками.

**Как работает функция**:

1.  Вызывает метод `handle_message` из экземпляра класса `BotHandler`, передавая ему объект `update` и `context`.

```
    A (Вызов метода handle_message из BotHandler)
```

**Примеры**:

```python
# Пример вызова функции (обычно вызывается автоматически Telegram Bot API)
# await bot._handle_message(update, context)
```

### `initialize_bot_webhook`

```python
def initialize_bot_webhook(self, route: str):
    """Initialize the bot webhook."""
    ...
```

**Назначение**: Инициализация вебхука для бота.

**Параметры**:

*   `route` (str): Маршрут вебхука.

**Как работает функция**:

1.  Формирует URL вебхука на основе переданного маршрута и хоста. Если хост `127.0.0.1` или `localhost`, использует `ngrok` для создания публичного URL.
2.  Устанавливает вебхук для бота, используя метод `set_webhook` из Telegram Bot API.
3.  Логирует информацию об установке вебхука.

```
    A (Формирование URL вебхука)
    ↓
    B (Использование ngrok, если хост локальный)
    ↓
    C (Установка вебхука через Telegram Bot API)
    ↓
    D (Логирование информации об установке вебхука)
```

**Примеры**:

```python
webhook_url = bot.initialize_bot_webhook(route='/telegram_webhook')
```

### `_register_route_via_rpc`

```python
def _register_route_via_rpc(self, rpc_client: ServerProxy):
    """Register the Telegram webhook route via RPC."""
    ...
```

**Назначение**: Регистрация маршрута Telegram webhook через RPC.

**Параметры**:

*   `rpc_client` (ServerProxy): RPC-клиент для взаимодействия с сервером FastAPI.

**Как работает функция**:

1.  Формирует маршрут, если он не начинается с `/`.
2.  Вызывает RPC-метод `add_new_route` для регистрации маршрута на сервере FastAPI.
3.  Логирует информацию о регистрации маршрута.

```
    A (Формирование маршрута)
    ↓
    B (Вызов RPC-метода add_new_route)
    ↓
    C (Логирование информации о регистрации маршрута)
```

**Примеры**:

```python
rpc_client = ServerProxy(f"http://{gs.host}:9000", allow_none=True)
bot._register_route_via_rpc(rpc_client)
```

### `stop`

```python
def stop(self):
    """Stop the bot and delete the webhook."""
    ...
```

**Назначение**: Остановка бота и удаление вебхука.

**Как работает функция**:

1.  Останавливает приложение Telegram Bot, используя метод `stop`.
2.  Удаляет вебхук, используя метод `delete_webhook` из Telegram Bot API.
3.  Логирует информацию об остановке бота.

```
    A (Остановка приложения Telegram Bot)
    ↓
    B (Удаление вебхука)
    ↓
    C (Логирование информации об остановке бота)
```

**Примеры**:

```python
bot.stop()
```

## Main

В блоке `if __name__ == "__main__":` происходит следующее:

1.  Загружаются переменные окружения из файла `.env`.
2.  Создается экземпляр класса `TelegramBot` с использованием токена, полученного из переменной окружения `TELEGRAM_TOKEN`.
3.  Вызывается метод `run` для запуска бота.
```
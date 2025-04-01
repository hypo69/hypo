# Модуль `bot_long_polling.py`

## Обзор

Модуль `bot_long_polling.py` представляет собой класс `TelegramBot`, который обеспечивает интерфейс для взаимодействия с Telegram ботом. Он включает в себя регистрацию обработчиков команд и сообщений, а также методы для запуска и остановки бота.

## Подробнее

Этот модуль является ключевым компонентом в системе, поскольку он обеспечивает связь между пользователем и ботом Telegram. Он использует библиотеку `telegram.ext` для обработки входящих сообщений и команд, а также для отправки ответов пользователю. Расположение файла в структуре проекта указывает на его роль как одной из точек входа для обработки запросов через Telegram.

## Классы

### `TelegramBot`

**Описание**: Класс `TelegramBot` предоставляет интерфейс для управления Telegram ботом. Он инициализирует бота с использованием предоставленного токена, регистрирует обработчики команд и сообщений, а также предоставляет методы для запуска и остановки бота.

**Как работает класс**:

1.  **Инициализация**: Класс принимает токен бота Telegram и использует его для создания экземпляра `Application` из библиотеки `telegram.ext`.
2.  **Регистрация обработчиков**: В конструкторе вызывается метод `register_handlers`, который регистрирует обработчики для различных команд и типов сообщений.
3.  **Запуск и остановка**: Методы `start` и `stop` используются для запуска и остановки бота соответственно.

**Методы**:

-   `__init__(self, token: str)`: Инициализирует экземпляр класса `TelegramBot` с указанным токеном.
-   `register_handlers(self) -> None`: Регистрирует обработчики команд и сообщений для бота.
-   `replace_message_handler(self, new_handler: Callable) -> None`: Заменяет текущий обработчик текстовых сообщений на новый.
-   `start(self, update: Update, context: CallbackContext) -> None`: Обрабатывает команду `/start`.

## Функции

### `__init__`

```python
def __init__(self, token: str):
    """Initialize the Telegram bot.

    Args:
        token (str): Telegram bot token, e.g., `gs.credentials.telegram.bot.kazarinov`.
    """
    ...
```

**Как работает функция**:

1.  Принимает токен бота Telegram в качестве аргумента.
2.  Инициализирует экземпляр класса `Application` из библиотеки `telegram.ext` с использованием предоставленного токена.
3.  Создает экземпляр класса `BotHandler` и сохраняет его в атрибуте `handler`.
4.  Вызывает метод `register_handlers` для регистрации обработчиков команд и сообщений.

**Параметры**:

-   `token` (str): Токен бота Telegram.

**Возвращает**:

-   None

**Вызывает исключения**:

-   None

**Примеры**:

```python
bot = TelegramBot(token='YOUR_BOT_TOKEN')
```

### `register_handlers`

```python
def register_handlers(self) -> None:
    """Register bot commands and message handlers."""
    ...
```

**Как работает функция**:

1.  Регистрирует обработчик для команды `/start`, который вызывает метод `start` класса `BotHandler`.
2.  Регистрирует обработчик для команды `/help`, который вызывает метод `help_command` класса `BotHandler`.
3.  Регистрирует обработчик для команды `/sendpdf`, который вызывает метод `send_pdf` класса `BotHandler`.
4.  Сохраняет ссылку на обработчик текстовых сообщений в атрибуте `_original_message_handler`.
5.  Регистрирует обработчик для текстовых сообщений, который вызывает метод `handle_message` класса `BotHandler`.
6.  Регистрирует обработчик для голосовых сообщений, который вызывает метод `handle_voice` класса `BotHandler`.
7.  Регистрирует обработчик для документов, который вызывает метод `handle_document` класса `BotHandler`.

**Параметры**:

-   None

**Возвращает**:

-   None

**Вызывает исключения**:

-   None

**Примеры**:

```python
bot = TelegramBot(token='YOUR_BOT_TOKEN')
bot.register_handlers()
```

### `replace_message_handler`

```python
def replace_message_handler(self, new_handler: Callable) -> None:
    """
    Заменяет текущий обработчик текстовых сообщений на новый.

    Args:
        new_handler (Callable): Новая функция для обработки сообщений.
    """
    ...
```

**Как работает функция**:

1.  Проверяет, существует ли текущий обработчик текстовых сообщений в списке обработчиков.
2.  Если существует, удаляет его из списка.
3.  Создает новый обработчик текстовых сообщений с использованием предоставленной функции `new_handler`.
4.  Регистрирует новый обработчик в списке обработчиков.

**Параметры**:

-   `new_handler` (Callable): Новая функция для обработки сообщений.

**Возвращает**:

-   None

**Вызывает исключения**:

-   None

**Примеры**:

```python
def my_new_handler(update: Update, context: CallbackContext) -> None:
    """Новый обработчик текстовых сообщений."""
    await update.message.reply_text('This is the new handler!')

bot = TelegramBot(token='YOUR_BOT_TOKEN')
bot.replace_message_handler(my_new_handler)
```

### `start`

```python
async def start(self, update: Update, context: CallbackContext) -> None:
    """Handle the /start command."""
    ...
```

**Как работает функция**:

1.  Логирует информацию о том, что бот был запущен пользователем, используя `logger.info`.
2.  Отправляет приветственное сообщение пользователю в ответ на команду `/start`.

**Параметры**:

-   `update` (Update): Объект `Update` из библиотеки `telegram`.
-   `context` (CallbackContext): Объект `CallbackContext` из библиотеки `telegram.ext`.

**Возвращает**:

-   None

**Вызывает исключения**:

-   None

**Примеры**:

```python
async def my_start_function(update: Update, context: CallbackContext) -> None:
    await TelegramBot.start(update, context)
```
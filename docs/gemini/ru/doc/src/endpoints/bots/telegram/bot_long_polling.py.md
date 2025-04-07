# Модуль для управления Telegram-ботом через long polling
## Обзор
Модуль `bot_long_polling.py` содержит класс `TelegramBot`, который предоставляет интерфейс для управления Telegram-ботом. Он включает в себя регистрацию обработчиков команд и сообщений, а также методы для запуска и остановки бота.

## Подробней
Этот модуль является точкой входа для запуска Telegram-бота. Он использует библиотеку `telegram.ext` для обработки входящих сообщений и команд. Класс `TelegramBot` инициализирует бота с заданным токеном, регистрирует обработчики команд и сообщений, а также предоставляет методы для динамической замены обработчиков сообщений.

## Классы
### `TelegramBot`
**Описание**: Класс `TelegramBot` предоставляет интерфейс для управления Telegram-ботом.

**Принцип работы**:
1.  Инициализация бота с использованием токена, полученного из конфигурации.
2.  Регистрация обработчиков команд и сообщений для обработки различных типов входящих данных.
3.  Реализация методов для запуска и остановки бота, а также для динамической замены обработчиков сообщений.

**Аттрибуты**:
-   `application` (Application): Экземпляр класса `Application` из библиотеки `telegram.ext`, который управляет ботом.
-   `handler` (BotHandler): Экземпляр класса `BotHandler`, который обрабатывает различные типы сообщений и команд.
-   `_original_message_handler` (MessageHandler): Ссылка на оригинальный обработчик текстовых сообщений.

**Методы**:
-   `__init__(token: str)`: Инициализирует экземпляр класса `TelegramBot`.
-   `register_handlers() -> None`: Регистрирует обработчики команд и сообщений.
-   `replace_message_handler(new_handler: Callable) -> None`: Заменяет текущий обработчик текстовых сообщений на новый.
-   `start(update: Update, context: CallbackContext) -> None`: Обрабатывает команду `/start`.

### `TelegramBot.__init__(token: str)`
```python
def __init__(self, token: str):
    """Initialize the Telegram bot.

    Args:
        token (str): Telegram bot token, e.g., `gs.credentials.telegram.bot.kazarinov`.
    """
```

**Назначение**: Инициализирует экземпляр класса `TelegramBot`.

**Параметры**:
-   `token` (str): Токен Telegram-бота.

**Как работает функция**:
1.  Создает экземпляр класса `Application` с использованием предоставленного токена.
2.  Инициализирует обработчик `BotHandler`.
3.  Регистрирует обработчики команд и сообщений.

**Примеры**:

```python
bot = TelegramBot(token='YOUR_BOT_TOKEN')
```

### `TelegramBot.register_handlers() -> None`
```python
def register_handlers(self) -> None:
    """Register bot commands and message handlers."""
```

**Назначение**: Регистрирует обработчики команд и сообщений для Telegram-бота.

**Как работает функция**:
1.  Регистрирует обработчик для команды `/start`, связанный с методом `self.handler.start`.
2.  Регистрирует обработчик для команды `/help`, связанный с методом `self.handler.help_command`.
3.  Регистрирует обработчик для команды `/sendpdf`, связанный с методом `self.handler.send_pdf`.
4.  Регистрирует обработчик текстовых сообщений, не являющихся командами, связанный с методом `self.handler.handle_message`.
5.  Регистрирует обработчик голосовых сообщений, связанный с методом `self.handler.handle_voice`.
6.  Регистрирует обработчик документов, связанный с методом `self.handler.handle_document`.

```
Регистрация обработчиков
↓
Обработчик /start → self.handler.start
↓
Обработчик /help → self.handler.help_command
↓
Обработчик /sendpdf → self.handler.send_pdf
↓
Обработчик текста → self.handler.handle_message
↓
Обработчик голоса → self.handler.handle_voice
↓
Обработчик документов → self.handler.handle_document
```

**Примеры**:

```python
bot = TelegramBot(token='YOUR_BOT_TOKEN')
bot.register_handlers()
```

### `TelegramBot.replace_message_handler(new_handler: Callable) -> None`
```python
def replace_message_handler(self, new_handler: Callable) -> None:
    """
    Заменяет текущий обработчик текстовых сообщений на новый.

    Args:
        new_handler (Callable): Новая функция для обработки сообщений.
    """
```

**Назначение**: Заменяет текущий обработчик текстовых сообщений на новый.

**Параметры**:
-   `new_handler` (Callable): Новая функция для обработки сообщений.

**Как работает функция**:
1.  Проверяет, существует ли текущий обработчик текстовых сообщений.
2.  Удаляет старый обработчик, если он существует.
3.  Создает новый обработчик текстовых сообщений с использованием предоставленной функции.
4.  Регистрирует новый обработчик.

```
Замена обработчика сообщений
↓
Проверка наличия старого обработчика
↓
Удаление старого обработчика (если есть)
↓
Создание нового обработчика
↓
Регистрация нового обработчика
```

**Примеры**:

```python
def my_new_handler(update: Update, context: CallbackContext) -> None:
    """Новый обработчик сообщений."""
    update.message.reply_text('New handler in action!')

bot = TelegramBot(token='YOUR_BOT_TOKEN')
bot.replace_message_handler(my_new_handler)
```

### `TelegramBot.start(update: Update, context: CallbackContext) -> None`
```python
async def start(self, update: Update, context: CallbackContext) -> None:
    """Handle the /start command."""
```

**Назначение**: Обрабатывает команду `/start`.

**Параметры**:
-   `update` (Update): Объект, представляющий входящее обновление от Telegram.
-   `context` (CallbackContext): Объект, содержащий информацию о контексте бота.

**Как работает функция**:
1.  Логирует информацию о запуске бота пользователем.
2.  Отправляет приветственное сообщение пользователю.

```
Обработка команды /start
↓
Логирование запуска бота
↓
Отправка приветственного сообщения
```

**Примеры**:

```python
async def start_command(update: Update, context: CallbackContext) -> None:
    bot = TelegramBot(token='YOUR_BOT_TOKEN')
    await bot.start(update, context)
```
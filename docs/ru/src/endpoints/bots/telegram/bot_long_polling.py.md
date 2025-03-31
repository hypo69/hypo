# Документация для модуля `bot_long_polling.py`

## Обзор

Модуль `bot_long_polling.py` предоставляет класс `TelegramBot` для взаимодействия с Telegram через ботов. Он использует библиотеку `telegram.ext` для обработки команд и сообщений, а также включает обработчики для текста, голосовых сообщений и документов.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для создания интерфейса между пользователем и ботом Telegram. Он включает в себя регистрацию обработчиков команд и сообщений, а также замену обработчиков сообщений во время выполнения.
Расположение модуля: `hypotez/src/endpoints/bots/telegram/bot_long_polling.py`.

## Классы

### `TelegramBot`

**Описание**: Класс `TelegramBot` предоставляет интерфейс для взаимодействия с Telegram ботом.

**Как работает класс**:
1.  Инициализируется с токеном бота Telegram.
2.  Регистрирует обработчики для различных команд и типов сообщений.
3.  Позволяет заменять обработчик текстовых сообщений во время выполнения.

**Методы**:

-   `__init__(self, token: str)`: Инициализирует экземпляр класса `TelegramBot`.
-   `register_handlers(self) -> None`: Регистрирует обработчики команд и сообщений бота.
-   `replace_message_handler(self, new_handler: Callable) -> None`: Заменяет текущий обработчик текстовых сообщений на новый.
-   `start(self, update: Update, context: CallbackContext) -> None`: Обрабатывает команду `/start`.

#### `__init__(self, token: str)`

```python
def __init__(self, token: str):
    """Initialize the Telegram bot.

    Args:
        token (str): Telegram bot token, e.g., `gs.credentials.telegram.bot.kazarinov`.
    """
    self.application = Application.builder().token(token).build()
    self.handler = BotHandler() # Инициализация обработчика в конструкторе
    self._original_message_handler = None
    self.register_handlers()
```

**Назначение**: Инициализация экземпляра класса `TelegramBot`.

**Как работает функция**:

1.  Создает экземпляр класса `Application` из библиотеки `telegram.ext` с использованием предоставленного токена.
2.  Инициализирует обработчик `BotHandler`.
3.  Сохраняет ссылку на обработчик сообщений.
4.  Вызывает метод `register_handlers` для регистрации обработчиков команд и сообщений.

**Параметры**:

*   `token` (str): Токен Telegram бота.

**Примеры**:

```python
bot = TelegramBot(token='YOUR_BOT_TOKEN')
```

#### `register_handlers(self) -> None`

```python
def register_handlers(self) -> None:
    """Register bot commands and message handlers."""
    self.application.add_handler(CommandHandler('start', self.handler.start))
    self.application.add_handler(CommandHandler('help', self.handler.help_command))
    self.application.add_handler(CommandHandler('sendpdf', self.handler.send_pdf))

    # Сохраняем ссылку
    self._original_message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, self.handler.handle_message)
    self.application.add_handler(self._original_message_handler)

    self.application.add_handler(MessageHandler(filters.VOICE, self.handler.handle_voice))
    self.application.add_handler(MessageHandler(filters.Document.ALL, self.handler.handle_document))
```

**Назначение**: Регистрация обработчиков команд и сообщений бота.

**Как работает функция**:

1.  Добавляет обработчики для команд `/start`, `/help` и `/sendpdf`.
2.  Сохраняет ссылку на оригинальный обработчик текстовых сообщений.
3.  Регистрирует обработчик для текстовых сообщений, исключая команды.
4.  Регистрирует обработчики для голосовых сообщений и документов.

**Примеры**:

```python
bot = TelegramBot(token='YOUR_BOT_TOKEN')
bot.register_handlers()
```

#### `replace_message_handler(self, new_handler: Callable) -> None`

```python
def replace_message_handler(self, new_handler: Callable) -> None:
    """
    Заменяет текущий обработчик текстовых сообщений на новый.

    Args:
        new_handler (Callable): Новая функция для обработки сообщений.
    """
    # 2. Удаляем старый обработчик
    if self._original_message_handler in self.application.handlers[0]:
        self.application.handlers[0].remove(self._original_message_handler)

    # 3. Создаем новый обработчик
    self._original_message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, new_handler)
    # 4. Регистрируем новый обработчик
    self.application.add_handler(self._original_message_handler)
```

**Назначение**: Замена текущего обработчика текстовых сообщений на новый.

**Как работает функция**:

1.  Удаляет старый обработчик текстовых сообщений.
2.  Создает новый обработчик текстовых сообщений с использованием предоставленной функции.
3.  Регистрирует новый обработчик в приложении.

**Параметры**:

*   `new_handler` (Callable): Новая функция для обработки сообщений.

**Примеры**:

```python
def my_new_handler(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('New handler processed this message!')

bot = TelegramBot(token='YOUR_BOT_TOKEN')
bot.replace_message_handler(my_new_handler)
```

#### `start(self, update: Update, context: CallbackContext) -> None`

```python
async def start(self, update: Update, context: CallbackContext) -> None:
    """Handle the /start command."""
    logger.info(f"Bot started by user {update.effective_user.id}")
    await update.message.reply_text('Hello! I am your simple bot. Type /help to see available commands.')
```

**Назначение**: Обработка команды `/start`.

**Как работает функция**:

1.  Логирует информацию о запуске бота пользователем.
2.  Отправляет приветственное сообщение пользователю.

**Параметры**:

*   `update` (Update): Объект `Update` от Telegram.
*   `context` (CallbackContext): Контекст обратного вызова.

**Примеры**:

```python
# Пример использования внутри обработчика
async def handle_start(update: Update, context: CallbackContext):
    await TelegramBot.start(update, context)
```
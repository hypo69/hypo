# Модуль `bot_long_polling.py`

## Обзор

Модуль `bot_long_polling.py` реализует интерфейс Telegram-бота для взаимодействия с пользователями через Telegram API. Он включает в себя обработку команд, текстовых сообщений, голосовых сообщений и документов.

## Подробней

Этот модуль является частью проекта `hypotez` и отвечает за обеспечение связи между пользователем и ботом Telegram. Он использует библиотеку `telegram.ext` для обработки обновлений от Telegram и предоставляет обработчики для различных типов входящих данных. Расположение файла `hypotez/src/endpoints/bots/telegram/bot_long_polling.py` указывает на его роль как одного из основных компонентов Telegram-бота в системе.

## Классы

### `TelegramBot`

**Описание**: Класс `TelegramBot` представляет собой интерфейс Telegram-бота.

**Как работает класс**:

Класс инициализируется с использованием токена Telegram-бота, создает экземпляр `Application` и регистрирует обработчики для различных типов сообщений и команд. Он также предоставляет методы для замены обработчика текстовых сообщений.

- `__init__`: Инициализирует бота с заданным токеном, создает экземпляры `Application` и `BotHandler`, а также регистрирует обработчики.
- `register_handlers`: Регистрирует обработчики команд и сообщений.
- `replace_message_handler`: Заменяет текущий обработчик текстовых сообщений на новый.
- `start`: Обрабатывает команду `/start` и отправляет приветственное сообщение пользователю.

**Методы**:

- `__init__`: Инициализирует экземпляр класса `TelegramBot`.
- `register_handlers`: Регистрирует обработчики команд и сообщений.
- `replace_message_handler`: Заменяет обработчик текстовых сообщений.
- `start`: Обрабатывает команду `/start`.

**Параметры**:

- `token` (str): Токен Telegram-бота.
- `application` (Application): Экземпляр `Application` из библиотеки `telegram.ext`.
- `handler` (BotHandler): Экземпляр класса `BotHandler`, обрабатывающего логику бота.
- `_original_message_handler` (MessageHandler): Обработчик текстовых сообщений по умолчанию.

**Примеры**:

```python
from src.endpoints.bots.telegram.bot_long_polling import TelegramBot
# Пример инициализации TelegramBot
bot = TelegramBot(token='YOUR_TELEGRAM_BOT_TOKEN')
```

## Методы класса `TelegramBot`

### `__init__`

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

**Описание**:

Инициализирует экземпляр класса `TelegramBot`.

**Как работает функция**:

1.  Инициализирует Telegram-бота с использованием предоставленного токена.
2.  Создает экземпляр класса `Application` из библиотеки `telegram.ext`.
3.  Создает экземпляр класса `BotHandler`, который будет обрабатывать логику бота.
4.  Вызывает метод `register_handlers` для регистрации обработчиков команд и сообщений.

**Параметры**:

*   `token` (str): Токен Telegram-бота, например, `'gs.credentials.telegram.bot.kazarinov'`.

**Возвращает**:

*   None

**Вызывает исключения**:

*   Нет явных исключений.

**Примеры**:

```python
bot = TelegramBot(token='YOUR_TELEGRAM_BOT_TOKEN')
```

### `register_handlers`

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

**Описание**:

Регистрирует обработчики команд и сообщений для Telegram-бота.

**Как работает функция**:

1.  Добавляет обработчики команд `/start`, `/help` и `/sendpdf` с использованием `CommandHandler`.
2.  Сохраняет ссылку на обработчик текстовых сообщений по умолчанию и добавляет его.
3.  Добавляет обработчики для голосовых сообщений и документов с использованием `MessageHandler`.

**Параметры**:

*   None

**Возвращает**:

*   None

**Вызывает исключения**:

*   Нет явных исключений.

**Примеры**:

```python
bot = TelegramBot(token='YOUR_TELEGRAM_BOT_TOKEN')
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
        # 2. Удаляем старый обработчик
        if self._original_message_handler in self.application.handlers[0]:
            self.application.handlers[0].remove(self._original_message_handler)

        # 3. Создаем новый обработчик
        self._original_message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, new_handler)
        # 4. Регистрируем новый обработчик
        self.application.add_handler(self._original_message_handler)
```

**Описание**:

Заменяет текущий обработчик текстовых сообщений на новый.

**Как работает функция**:

1.  Проверяет, существует ли текущий обработчик в списке обработчиков приложения.
2.  Если существует, удаляет старый обработчик.
3.  Создает новый обработчик текстовых сообщений с использованием предоставленной функции `new_handler`.
4.  Добавляет новый обработчик в приложение.

**Параметры**:

*   `new_handler` (Callable): Новая функция для обработки сообщений.

**Возвращает**:

*   None

**Вызывает исключения**:

*   Нет явных исключений.

**Примеры**:

```python
async def my_new_handler(update: Update, context: CallbackContext):
    await update.message.reply_text('New handler in action!')

bot = TelegramBot(token='YOUR_TELEGRAM_BOT_TOKEN')
bot.replace_message_handler(my_new_handler)
```

### `start`

```python
    async def start(self, update: Update, context: CallbackContext) -> None:
        """Handle the /start command."""
        logger.info(f"Bot started by user {update.effective_user.id}")
        await update.message.reply_text('Hello! I am your simple bot. Type /help to see available commands.')
```

**Описание**:

Обрабатывает команду `/start` и отправляет приветственное сообщение пользователю.

**Как работает функция**:

1.  Логирует информацию о пользователе, запустившем бота.
2.  Отправляет приветственное сообщение пользователю с инструкцией по использованию команды `/help`.

**Параметры**:

*   `update` (Update): Объект `Update` из библиотеки `telegram.ext`, содержащий информацию об обновлении.
*   `context` (CallbackContext): Объект `CallbackContext` из библиотеки `telegram.ext`, содержащий контекст обратного вызова.

**Возвращает**:

*   None

**Вызывает исключения**:

*   Нет явных исключений.

**Примеры**:

```python
# Пример обработки команды /start
async def start_handler(update: Update, context: CallbackContext):
    await TelegramBot.start(update, context)
```
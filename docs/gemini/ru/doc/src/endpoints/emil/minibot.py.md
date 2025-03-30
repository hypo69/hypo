# Модуль `minibot`

## Обзор

Модуль `minibot` представляет собой реализацию телеграм-бота, предназначенного для обслуживания запросов, связанных с проектом emil-design.com. Он включает в себя обработку текстовых сообщений, URL-адресов, голосовых сообщений и документов, а также поддерживает выполнение различных команд через интерфейс Telegram.

## Подробнее

Этот модуль содержит классы и функции для работы с Telegram Bot API, обработки сообщений пользователей и взаимодействия с AI-моделями для генерации ответов. Он также включает в себя функциональность для обработки URL-адресов, полученных от пользователей, и выполнения сценариев на основе этих URL-адресов. Модуль использует библиотеку `telebot` для взаимодействия с Telegram API, а также другие модули, такие как `src.gs`, `src.logger`, `src.ai.gemini` и `src.endpoints.kazarinov.scenarios.scenario`, для выполнения различных задач.

## Классы

### `BotHandler`

**Описание**: Класс `BotHandler` предназначен для обработки команд, полученных от телеграм-бота. Он включает в себя методы для обработки текстовых сообщений, URL-адресов, команд и других типов контента, отправляемых пользователями.

**Методы**:
- `__init__`: Инициализирует обработчик событий телеграм-бота.
- `handle_message`: Обрабатывает текстовые сообщения.
- `_send_user_flowchart`: Отправляет схему user_flowchart.
- `_handle_url`: Обрабатывает URL, присланный пользователем.
- `_handle_next_command`: Обрабатывает команду '--next' и её аналоги.
- `help_command`: Обрабатывает команду /help.
- `send_pdf`: Обрабатывает команду /sendpdf для отправки PDF.
- `handle_voice`: Обрабатывает голосовые сообщения.
- `_transcribe_voice`: Транскрибирует голосовое сообщение (заглушка).
- `handle_document`: Обрабатывает полученные документы.

**Параметры**:
- `base_dir` (Path): Базовая директория, используемая для доступа к файлам и ресурсам.

**Примеры**
```python
handler = BotHandler()
```

### `Config`

**Описание**: Класс `Config` содержит настройки конфигурации для телеграм-бота, такие как токен бота, ID канала, директория с фотографиями и сообщения для различных команд.

**Параметры**:
- `BOT_TOKEN` (str): Токен бота, полученный из переменных окружения или базы данных.
- `CHANNEL_ID` (str): ID канала Telegram.
- `PHOTO_DIR` (Path): Директория с фотографиями для команды /photo.
- `COMMAND_INFO` (str): Информация о боте, отображаемая по команде /info.
- `UNKNOWN_COMMAND_MESSAGE` (str): Сообщение об неизвестной команде.
- `START_MESSAGE` (str): Сообщение, отображаемое при старте бота.
- `HELP_MESSAGE` (str): Сообщение со списком доступных команд.

## Функции

### `command_start`

```python
def command_start(message):
    """Обрабатывает команду /start."""
    ...
```

**Описание**: Обрабатывает команду `/start`, отправляя приветственное сообщение пользователю.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от Telegram.

**Примеры**:
```python
@bot.message_handler(commands=['start'])
def command_start(message):
    logger.info(f"User {message.from_user.username} send /start command")
    bot.send_message(message.chat.id, config.START_MESSAGE)
```

### `command_help`

```python
def command_help(message):
    """Обрабатывает команду /help."""
    ...
```

**Описание**: Обрабатывает команду `/help`, вызывая метод `help_command` класса `BotHandler` для отображения справки.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от Telegram.

**Примеры**:
```python
@bot.message_handler(commands=['help'])
def command_help(message):
    logger.info(f"User {message.from_user.username} send /help command")
    handler.help_command(bot, message)
```

### `command_info`

```python
def command_info(message):
    """Обрабатывает команду /info."""
    ...
```

**Описание**: Обрабатывает команду `/info`, отправляя информацию о боте.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от Telegram.

**Примеры**:
```python
@bot.message_handler(commands=['info'])
def command_info(message):
    logger.info(f"User {message.from_user.username} send /info command")
    bot.send_message(message.chat.id, config.COMMAND_INFO)
```

### `command_time`

```python
def command_time(message):
    """Обрабатывает команду /time."""
    ...
```

**Описание**: Обрабатывает команду `/time`, отправляя текущее время.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от Telegram.

**Примеры**:
```python
@bot.message_handler(commands=['time'])
def command_time(message):
    logger.info(f"User {message.from_user.username} send /time command")
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    bot.send_message(message.chat.id, f"Current time: {current_time}")
```

### `command_photo`

```python
def command_photo(message):
    """Обрабатывает команду /photo."""
    ...
```

**Описание**: Обрабатывает команду `/photo`, отправляя случайное фото из указанной директории.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от Telegram.

**Примеры**:
```python
@bot.message_handler(commands=['photo'])
def command_photo(message):
    logger.info(f"User {message.from_user.username} send /photo command")
    try:
        photo_files = os.listdir(config.PHOTO_DIR)
        if photo_files:
            random_photo = random.choice(photo_files)
            photo_path = os.path.join(config.PHOTO_DIR, random_photo)
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
        else:
            bot.send_message(message.chat.id, "No photos in the folder.")
    except FileNotFoundError:
        bot.send_message(message.chat.id, "Photo directory not found.")
```

### `handle_voice_message`

```python
def handle_voice_message(message):
    """Обрабатывает голосовые сообщения."""
    ...
```

**Описание**: Обрабатывает голосовые сообщения, вызывая метод `handle_voice` класса `BotHandler`.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от Telegram.

**Примеры**:
```python
@bot.message_handler(content_types=['voice'])
def handle_voice_message(message):
    logger.info(f"User {message.from_user.username} send voice message")
    handler.handle_voice(bot, message)
```

### `handle_document_message`

```python
def handle_document_message(message):
    """Обрабатывает полученные документы."""
    ...
```

**Описание**: Обрабатывает полученные документы, вызывая метод `handle_document` класса `BotHandler`.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от Telegram.

**Примеры**:
```python
@bot.message_handler(content_types=['document'])
def handle_document_message(message):
    logger.info(f"User {message.from_user.username} send document message")
    handler.handle_document(bot, message)
```

### `handle_text_message`

```python
def handle_text_message(message):
    """Обрабатывает текстовые сообщения."""
    ...
```

**Описание**: Обрабатывает текстовые сообщения, вызывая метод `handle_message` класса `BotHandler`.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от Telegram.

**Примеры**:
```python
@bot.message_handler(func=lambda message: message.text and not message.text.startswith('/'))
def handle_text_message(message):
    logger.info(f"User {message.from_user.username} sent message: {message.text}")
    handler.handle_message(bot, message )
```

### `handle_unknown_command`

```python
def handle_unknown_command(message):
    """Обрабатывает неизвестные команды."""
    ...
```

**Описание**: Обрабатывает неизвестные команды, отправляя сообщение об этом пользователю.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от Telegram.

**Примеры**:
```python
@bot.message_handler(func=lambda message: message.text and message.text.startswith('/'))
def handle_unknown_command(message):
    logger.info(f"User {message.from_user.username} send unknown command: {message.text}")
    bot.send_message(message.chat.id, config.UNKNOWN_COMMAND_MESSAGE)
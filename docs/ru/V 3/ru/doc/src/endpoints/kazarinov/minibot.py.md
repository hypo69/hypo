# minibot

## Обзор

Модуль `minibot` представляет собой телеграм-бота, предназначенного для обработки запросов от пользователя kazarinov. Бот интегрирован с Google Generative AI для обработки текстовых сообщений и предоставляет различные команды для взаимодействия, такие как обработка URL-адресов OneTab, отправка PDF-файлов и распознавание голосовых сообщений.

## Подробней

Данный модуль является частью проекта `hypotez` и предназначен для автоматизации задач, связанных с обработкой информации и взаимодействием с пользователем через Telegram. Бот может работать в двух режимах: PRODUCTION (использует боевой токен) и DEV (использует тестовый токен). Ключи для доступа к API и токенам хранятся либо в переменных окружения, либо в базе данных с паролями, в зависимости от конфигурации.

## Классы

### `BotHandler`

**Описание**: Класс `BotHandler` отвечает за обработку команд, полученных от телеграм-бота. Он содержит методы для обработки текстовых сообщений, URL-адресов, голосовых сообщений и документов.

**Методы**:
- `__init__`: Инициализация обработчика событий телеграм-бота.
- `handle_message`: Обработка текстовых сообщений.
- `_send_user_flowchart`: Отправка схемы user_flowchart.
- `_handle_url`: Обработка URL, присланного пользователем.
- `_handle_next_command`: Обработка команды '--next' и её аналогов.
- `help_command`: Обработка команды /help.
- `send_pdf`: Обработка команды /sendpdf для отправки PDF.
- `handle_voice`: Обработка голосовых сообщений.
- `_transcribe_voice`: Транскрибирование голосового сообщения (заглушка).
- `handle_document`: Обработка полученных документов.

**Параметры**:
- `base_dir` (Path): Базовая директория для хранения ресурсов бота.

**Примеры**:
```python
handler = BotHandler()
```

### `Config`

**Описание**: Класс `Config` содержит конфигурационные параметры для телеграм-бота, такие как токен бота, ID канала, директория с фотографиями и сообщения для различных команд.

**Параметры**:
- `BOT_TOKEN` (str): Токен телеграм-бота.
- `CHANNEL_ID` (str): ID канала для отправки сообщений.
- `PHOTO_DIR` (Path): Директория с фотографиями для отправки.
- `COMMAND_INFO` (str): Информация о боте.
- `UNKNOWN_COMMAND_MESSAGE` (str): Сообщение для неизвестной команды.
- `START_MESSAGE` (str): Сообщение при старте бота.
- `HELP_MESSAGE` (str): Сообщение справки.

**Примеры**:
```python
config = Config()
```

## Функции

### `command_start`

```python
def command_start(message):
    """Обработка команды /start."""
    ...
```

**Описание**: Обрабатывает команду `/start`, отправляя приветственное сообщение пользователю.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от Telegram.

**Возвращает**:
- `None`

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
    """Обработка команды /help."""
    ...
```

**Описание**: Обрабатывает команду `/help`, вызывая метод `help_command` класса `BotHandler` для отправки справки пользователю.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от Telegram.

**Возвращает**:
- `None`

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
    """Обработка команды /info."""
    ...
```

**Описание**: Обрабатывает команду `/info`, отправляя информацию о боте пользователю.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от Telegram.

**Возвращает**:
- `None`

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
    """Обработка команды /time."""
    ...
```

**Описание**: Обрабатывает команду `/time`, отправляя текущее время пользователю.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от Telegram.

**Возвращает**:
- `None`

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
    """Обработка команды /photo."""
    ...
```

**Описание**: Обрабатывает команду `/photo`, отправляя случайное фото из директории пользователю.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от Telegram.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `FileNotFoundError`: Если директория с фотографиями не найдена.

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
    """Обработка голосовых сообщений."""
    ...
```

**Описание**: Обрабатывает голосовые сообщения, вызывая метод `handle_voice` класса `BotHandler`.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от Telegram.

**Возвращает**:
- `None`

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
    """Обработка полученных документов."""
    ...
```

**Описание**: Обрабатывает полученные документы, вызывая метод `handle_document` класса `BotHandler`.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от Telegram.

**Возвращает**:
- `None`

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
    """Обработка текстовых сообщений."""
    ...
```

**Описание**: Обрабатывает текстовые сообщения, вызывая метод `handle_message` класса `BotHandler`.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от Telegram.

**Возвращает**:
- `None`

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
    """Обработка неизвестных команд."""
    ...
```

**Описание**: Обрабатывает неизвестные команды, отправляя сообщение об этом пользователю.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от Telegram.

**Возвращает**:
- `None`

**Примеры**:
```python
@bot.message_handler(func=lambda message: message.text and message.text.startswith('/'))
def handle_unknown_command(message):
    logger.info(f"User {message.from_user.username} send unknown command: {message.text}")
    bot.send_message(message.chat.id, config.UNKNOWN_COMMAND_MESSAGE)
```

### `main`

```python
def main():
    """Основная функция для запуска бота."""
    ...
```

**Описание**: Основная функция для запуска телеграм-бота.

**Параметры**:
- `None`

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: При возникновении ошибки во время работы бота.

**Примеры**:
```python
def main():
    try:
        logger.info(f"Starting bot in {MODE} mode")
        bot.polling(none_stop=True)
    except Exception as ex:
        logger.error(f"Error during bot polling: ", ex)
        ...
        bot.stop_bot()
        main()
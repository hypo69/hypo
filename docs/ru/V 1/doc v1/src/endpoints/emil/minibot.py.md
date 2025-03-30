# Модуль `minibot`

## Обзор

Модуль `minibot` представляет собой простого Telegram-бота, предназначенного для обслуживания запросов, связанных с `emil-design.com`. Он включает в себя обработку текстовых и голосовых сообщений, документов, а также поддержку команд `/start`, `/help`, `/info`, `/time` и `/photo`. Бот использует Google Generative AI для обработки текстовых запросов и предоставляет функциональность для работы с URL-адресами `one-tab.com`.

## Подробнее

Модуль разделен на несколько основных компонентов:

- **`BotHandler`**: Класс, обрабатывающий входящие сообщения и команды от пользователей.
- **`Config`**: Класс, содержащий конфигурационные параметры бота, такие как токен, идентификатор канала и пути к ресурсам.
- **Обработчики сообщений**: Функции, обрабатывающие различные типы сообщений и команды, отправляемые пользователями боту.

Этот бот предназначен для интеграции с Telegram и предоставляет пользователям информацию и ответы на их запросы. Расположение файла в структуре проекта: `hypotez/src/endpoints/emil/minibot.py`.

## Содержание

- [Классы](#Классы)
  - [`BotHandler`](#BotHandler)
  - [`Config`](#Config)
- [Функции](#Функции)
  - [`command_start`](#command_start)
  - [`command_help`](#command_help)
  - [`command_info`](#command_info)
  - [`command_time`](#command_time)
  - [`command_photo`](#command_photo)
  - [`handle_voice_message`](#handle_voice_message)
  - [`handle_document_message`](#handle_document_message)
  - [`handle_text_message`](#handle_text_message)
  - [`handle_unknown_command`](#handle_unknown_command)

## Классы

### `BotHandler`

**Описание**: Исполнитель команд, полученных ботом.

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

#### `__init__`

```python
def __init__(self):
    """
    Args:
        self: экземпляр класса `BotHandler`.

    Returns:
        None

    Raises:
        Не вызывает исключений.
    """
    ...
```

**Описание**: Инициализация обработчика событий телеграм-бота.

**Параметры**:
- `self`: экземпляр класса `BotHandler`.

**Примеры**:

```python
handler = BotHandler()
```

#### `handle_message`

```python
def handle_message(self, bot: telebot, message: 'message'):
    """
    Args:
        bot (telebot): Экземпляр телеграм-бота.
        message (telebot.types.Message): Объект сообщения от пользователя.

    Returns:
        None

    Raises:
        Exception: В случае ошибки при взаимодействии с моделью.
    """
    ...
```

**Описание**: Обработка текстовых сообщений, полученных от пользователя.

**Параметры**:
- `bot` (telebot): Экземпляр телеграм-бота.
- `message` (telebot.types.Message): Объект сообщения от пользователя.

**Примеры**:

```python
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    handler = BotHandler()
    handler.handle_message(bot, message)
```

#### `_send_user_flowchart`

```python
def _send_user_flowchart(self, bot, chat_id):
    """
    Args:
        bot: Экземпляр телеграм-бота.
        chat_id: Идентификатор чата, куда отправлять схему.

    Returns:
        None

    Raises:
        FileNotFoundError: Если файл схемы не найден.
    """
    ...
```

**Описание**: Отправляет схему user_flowchart пользователю.

**Параметры**:
- `bot`: Экземпляр телеграм-бота.
- `chat_id`: Идентификатор чата, куда отправлять схему.

**Примеры**:

```python
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')
handler = BotHandler()
handler._send_user_flowchart(bot, 123456789)
```

#### `_handle_url`

```python
def _handle_url(self, bot, message: 'message'):
    """
    Args:
        bot: Экземпляр телеграм-бота.
        message (telebot.types.Message): Объект сообщения от пользователя.

    Returns:
        None

    Raises:
        Exception: В случае ошибки при получении данных из OneTab или выполнении сценария.
    """
    ...
```

**Описание**: Обрабатывает URL, присланный пользователем, извлекает данные из OneTab и запускает сценарий.

**Параметры**:
- `bot`: Экземпляр телеграм-бота.
- `message` (telebot.types.Message): Объект сообщения от пользователя.

**Примеры**:

```python
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    handler = BotHandler()
    message.text = 'https://one-tab.com/...'
    handler._handle_url(bot, message)
```

#### `_handle_next_command`

```python
def _handle_next_command(self, bot, message):
    """
    Args:
        bot: Экземпляр телеграм-бота.
        message (telebot.types.Message): Объект сообщения от пользователя.

    Returns:
        None

    Raises:
        Exception: В случае ошибки при чтении вопросов.
    """
    ...
```

**Описание**: Обрабатывает команду '--next' и её аналоги, задает случайный вопрос пользователю и отправляет ответ.

**Параметры**:
- `bot`: Экземпляр телеграм-бота.
- `message` (telebot.types.Message): Объект сообщения от пользователя.

**Примеры**:

```python
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    handler = BotHandler()
    message.text = '--next'
    handler._handle_next_command(bot, message)
```

#### `help_command`

```python
def help_command(self, bot, message):
    """
    Args:
        bot: Экземпляр телеграм-бота.
        message (telebot.types.Message): Объект сообщения от пользователя.

    Returns:
        None

    Raises:
        Не вызывает исключений.
    """
    ...
```

**Описание**: Обрабатывает команду /help и отправляет пользователю список доступных команд.

**Параметры**:
- `bot`: Экземпляр телеграм-бота.
- `message` (telebot.types.Message): Объект сообщения от пользователя.

**Примеры**:

```python
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')
@bot.message_handler(commands=['help'])
def handle_help(message):
    handler = BotHandler()
    handler.help_command(bot, message)
```

#### `send_pdf`

```python
def send_pdf(self, bot, message, pdf_file):
    """
    Args:
        bot: Экземпляр телеграм-бота.
        message (telebot.types.Message): Объект сообщения от пользователя.
        pdf_file (str): Путь к PDF-файлу.

    Returns:
        None

    Raises:
        Exception: В случае ошибки при отправке PDF-файла.
    """
    ...
```

**Описание**: Обрабатывает команду /sendpdf для отправки PDF-файла пользователю.

**Параметры**:
- `bot`: Экземпляр телеграм-бота.
- `message` (telebot.types.Message): Объект сообщения от пользователя.
- `pdf_file` (str): Путь к PDF-файлу.

**Примеры**:

```python
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')
@bot.message_handler(commands=['sendpdf'])
def handle_sendpdf(message):
    handler = BotHandler()
    handler.send_pdf(bot, message, 'example.pdf')
```

#### `handle_voice`

```python
def handle_voice(self, bot, message):
    """
    Args:
        bot: Экземпляр телеграм-бота.
        message (telebot.types.Message): Объект сообщения от пользователя.

    Returns:
        None

    Raises:
        Exception: В случае ошибки при обработке голосового сообщения.
    """
    ...
```

**Описание**: Обрабатывает голосовые сообщения, полученные от пользователя.

**Параметры**:
- `bot`: Экземпляр телеграм-бота.
- `message` (telebot.types.Message): Объект сообщения от пользователя.

**Примеры**:

```python
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')
@bot.message_handler(content_types=['voice'])
def handle_voice_message(message):
    handler = BotHandler()
    handler.handle_voice(bot, message)
```

#### `_transcribe_voice`

```python
def _transcribe_voice(self, file_path):
    """
    Args:
        file_path (str): Путь к файлу голосового сообщения.

    Returns:
        str: Распознанный текст из голосового сообщения.

    Raises:
        Не вызывает исключений.
    """
    ...
```

**Описание**: Транскрибирует голосовое сообщение (заглушка, функция не реализована).

**Параметры**:
- `file_path` (str): Путь к файлу голосового сообщения.

**Примеры**:

```python
handler = BotHandler()
text = handler._transcribe_voice('voice.ogg')
print(text)  # Вывод: Распознавание голоса ещё не реализовано.
```

#### `handle_document`

```python
def handle_document(self, bot, message):
    """
    Args:
        bot: Экземпляр телеграм-бота.
        message (telebot.types.Message): Объект сообщения от пользователя.

    Returns:
        bool: `True`, если обработка прошла успешно, `False` в случае ошибки.

    Raises:
        Exception: В случае ошибки при обработке документа.
    """
    ...
```

**Описание**: Обрабатывает документы, полученные от пользователя.

**Параметры**:
- `bot`: Экземпляр телеграм-бота.
- `message` (telebot.types.Message): Объект сообщения от пользователя.

**Примеры**:

```python
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')
@bot.message_handler(content_types=['document'])
def handle_document_message(message):
    handler = BotHandler()
    result = handler.handle_document(bot, message)
    if result:
        print('Документ успешно обработан.')
    else:
        print('Ошибка при обработке документа.')
```

### `Config`

**Описание**: Класс, содержащий конфигурационные параметры бота.

**Параметры**:
- `BOT_TOKEN` (str): Токен Telegram-бота.
- `CHANNEL_ID` (str): Идентификатор канала.
- `PHOTO_DIR` (Path): Путь к директории с фотографиями.
- `COMMAND_INFO` (str): Информация о боте.
- `UNKNOWN_COMMAND_MESSAGE` (str): Сообщение для неизвестных команд.
- `START_MESSAGE` (str): Стартовое сообщение бота.
- `HELP_MESSAGE` (str): Сообщение со списком доступных команд.

**Примеры**:

```python
config = Config()
print(config.BOT_TOKEN)
```

## Функции

### `command_start`

```python
def command_start(message):
    """
    Args:
        message (telebot.types.Message): Объект сообщения от пользователя.

    Returns:
        None

    Raises:
        Не вызывает исключений.
    """
    ...
```

**Описание**: Обрабатывает команду `/start` и отправляет стартовое сообщение пользователю.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от пользователя.

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
    """
    Args:
        message (telebot.types.Message): Объект сообщения от пользователя.

    Returns:
        None

    Raises:
        Не вызывает исключений.
    """
    ...
```

**Описание**: Обрабатывает команду `/help` и вызывает метод `help_command` обработчика для отправки справки пользователю.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от пользователя.

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
    """
    Args:
        message (telebot.types.Message): Объект сообщения от пользователя.

    Returns:
        None

    Raises:
        Не вызывает исключений.
    """
    ...
```

**Описание**: Обрабатывает команду `/info` и отправляет информацию о боте пользователю.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от пользователя.

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
    """
    Args:
        message (telebot.types.Message): Объект сообщения от пользователя.

    Returns:
        None

    Raises:
        Не вызывает исключений.
    """
    ...
```

**Описание**: Обрабатывает команду `/time` и отправляет текущее время пользователю.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от пользователя.

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
    """
    Args:
        message (telebot.types.Message): Объект сообщения от пользователя.

    Returns:
        None

    Raises:
        FileNotFoundError: Если директория с фотографиями не найдена.
    """
    ...
```

**Описание**: Обрабатывает команду `/photo` и отправляет случайную фотографию пользователю.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от пользователя.

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
    """
    Args:
        message (telebot.types.Message): Объект сообщения от пользователя.

    Returns:
        None

    Raises:
        Не вызывает исключений.
    """
    ...
```

**Описание**: Обрабатывает голосовые сообщения, вызывая метод `handle_voice` обработчика.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от пользователя.

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
    """
    Args:
        message (telebot.types.Message): Объект сообщения от пользователя.

    Returns:
        None

    Raises:
        Не вызывает исключений.
    """
    ...
```

**Описание**: Обрабатывает сообщения с документами, вызывая метод `handle_document` обработчика.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от пользователя.

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
    """
    Args:
        message (telebot.types.Message): Объект сообщения от пользователя.

    Returns:
        None

    Raises:
        Не вызывает исключений.
    """
    ...
```

**Описание**: Обрабатывает текстовые сообщения, вызывая метод `handle_message` обработчика.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от пользователя.

**Примеры**:

```python
@bot.message_handler(func=lambda message: message.text and not message.text.startswith('/'))
def handle_text_message(message):
    logger.info(f"User {message.from_user.username} sent message: {message.text}")
    handler.handle_message(bot, message)
```

### `handle_unknown_command`

```python
def handle_unknown_command(message):
    """
    Args:
        message (telebot.types.Message): Объект сообщения от пользователя.

    Returns:
        None

    Raises:
        Не вызывает исключений.
    """
    ...
```

**Описание**: Обрабатывает неизвестные команды и отправляет сообщение об этом пользователю.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от пользователя.

**Примеры**:

```python
@bot.message_handler(func=lambda message: message.text and message.text.startswith('/'))
def handle_unknown_command(message):
    logger.info(f"User {message.from_user.username} send unknown command: {message.text}")
    bot.send_message(message.chat.id, config.UNKNOWN_COMMAND_MESSAGE)
```
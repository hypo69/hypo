# Модуль `minibot.py`

## Обзор

Модуль `minibot.py` представляет собой реализацию мини-бота для обслуживания запросов от пользователя Kazarinov. Он использует библиотеку `telebot` для взаимодействия с Telegram API и включает функциональность для обработки текстовых сообщений, URL, голосовых сообщений и документов. Также реализована интеграция с AI-моделью Google Gemini для генерации ответов на запросы пользователя.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для предоставления интерфейса взаимодействия с пользователем через Telegram. Он обрабатывает различные типы входящих сообщений, такие как текстовые команды, URL (в частности, из OneTab), голосовые сообщения и документы. В зависимости от типа сообщения, бот выполняет соответствующие действия, такие как отправка сообщений, обработка URL для извлечения данных, транскрибирование голосовых сообщений или сохранение документов.

Основная цель модуля - обеспечить удобный и функциональный интерфейс для взаимодействия с пользователем, используя возможности Telegram API и AI-модели Google Gemini. Он также предоставляет механизмы для обработки ошибок и логирования событий, что облегчает отладку и поддержку бота.

## Классы

### `BotHandler`

**Описание**:
Класс `BotHandler` предназначен для обработки команд, полученных от Telegram-бота. Он содержит методы для обработки текстовых сообщений, URL, а также для отправки различных типов ответов пользователю.

**Методы**:
- `__init__`: Инициализирует обработчик событий телеграм-бота, настраивает список вопросов и AI-модель Google Gemini.
- `handle_message`: Обрабатывает текстовые сообщения, определяя тип запроса (URL, команда или текст) и выполняет соответствующие действия.
- `_send_user_flowchart`: Отправляет схему user_flowchart в виде фотографии.
- `_handle_url`: Обрабатывает URL, присланные пользователем, извлекая данные из OneTab и запуская сценарий.
- `_handle_next_command`: Обрабатывает команду '--next' и её аналоги, отправляя случайный вопрос и ответ от AI-модели.
- `help_command`: Обрабатывает команду /help, отправляя список доступных команд.
- `send_pdf`: Обрабатывает команду /sendpdf для отправки PDF-файла.
- `handle_voice`: Обрабатывает голосовые сообщения, транскрибируя их и отправляя распознанный текст пользователю.
- `_transcribe_voice`: Транскрибирует голосовое сообщение (заглушка, пока не реализовано).
- `handle_document`: Обрабатывает полученные документы, сохраняя их во временную директорию.

**Параметры**:
- `base_dir` (Path): Базовая директория для хранения ресурсов бота.
- `questions_list` (list[str]): Список вопросов для обработки команды '--next'.
- `model` (GoogleGenerativeAI): AI-модель Google Gemini для генерации ответов.

**Примеры**:

```python
handler = BotHandler()
```

### `Config`

**Описание**:
Класс `Config` предназначен для хранения конфигурационных параметров бота, таких как токен Telegram бота, ID канала, директории с фотографиями и текстовые сообщения для различных команд.

**Параметры**:
- `BOT_TOKEN` (str): Токен Telegram бота, который зависит от режима работы (PRODUCTION или DEV) и способа получения (из .env или из базы данных).
- `CHANNEL_ID` (str): ID канала Telegram.
- `PHOTO_DIR` (Path): Путь к директории с фотографиями.
- `COMMAND_INFO` (str): Информация о боте для команды /info.
- `UNKNOWN_COMMAND_MESSAGE` (str): Сообщение для неизвестных команд.
- `START_MESSAGE` (str): Сообщение для команды /start.
- `HELP_MESSAGE` (str): Сообщение для команды /help.

**Примеры**:

```python
config = Config()
```

## Функции

### `command_start`

```python
@bot.message_handler(commands=['start'])
def command_start(message):
    """
    Args:
        message (telebot.types.Message): Объект сообщения от Telegram.

    Returns:
        None

    Raises:
        No exceptions

    Example:
        Пример вызова команды /start пользователем:
        >>> /start
    """
```

**Описание**:
Обрабатывает команду `/start`, отправляя приветственное сообщение пользователю.

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
@bot.message_handler(commands=['help'])
def command_help(message):
    """
    Args:
        message (telebot.types.Message): Объект сообщения от Telegram.

    Returns:
        None

    Raises:
        No exceptions

    Example:
        Пример вызова команды /help пользователем:
        >>> /help
    """
```

**Описание**:
Обрабатывает команду `/help`, вызывая метод `help_command` у объекта `handler` для отправки списка доступных команд.

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
@bot.message_handler(commands=['info'])
def command_info(message):
    """
    Args:
        message (telebot.types.Message): Объект сообщения от Telegram.

    Returns:
        None

    Raises:
        No exceptions

    Example:
        Пример вызова команды /info пользователем:
        >>> /info
    """
```

**Описание**:
Обрабатывает команду `/info`, отправляя информацию о боте пользователю.

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
@bot.message_handler(commands=['time'])
def command_time(message):
    """
    Args:
        message (telebot.types.Message): Объект сообщения от Telegram.

    Returns:
        None

    Raises:
        No exceptions

    Example:
        Пример вызова команды /time пользователем:
        >>> /time
    """
```

**Описание**:
Обрабатывает команду `/time`, отправляя текущее время пользователю.

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
@bot.message_handler(commands=['photo'])
def command_photo(message):
    """
    Args:
        message (telebot.types.Message): Объект сообщения от Telegram.

    Returns:
        None

    Raises:
        FileNotFoundError: Если директория с фотографиями не найдена.

    Example:
        Пример вызова команды /photo пользователем:
        >>> /photo
    """
```

**Описание**:
Обрабатывает команду `/photo`, отправляя случайную фотографию из директории `PHOTO_DIR`.

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
@bot.message_handler(content_types=['voice'])
def handle_voice_message(message):
    """
    Args:
        message (telebot.types.Message): Объект сообщения от Telegram.

    Returns:
        None

    Raises:
        No exceptions

    Example:
        Пример отправки голосового сообщения пользователем.
    """
```

**Описание**:
Обрабатывает голосовые сообщения, вызывая метод `handle_voice` у объекта `handler`.

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
@bot.message_handler(content_types=['document'])
def handle_document_message(message):
    """
    Args:
        message (telebot.types.Message): Объект сообщения от Telegram.

    Returns:
        None

    Raises:
        No exceptions

    Example:
        Пример отправки документа пользователем.
    """
```

**Описание**:
Обрабатывает полученные документы, вызывая метод `handle_document` у объекта `handler`.

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
@bot.message_handler(func=lambda message: message.text and not message.text.startswith('/'))
def handle_text_message(message):
    """
    Args:
        message (telebot.types.Message): Объект сообщения от Telegram.

    Returns:
        None

    Raises:
        No exceptions

    Example:
        Пример отправки текстового сообщения пользователем, не являющегося командой.
    """
```

**Описание**:
Обрабатывает текстовые сообщения, не начинающиеся с `/`, вызывая метод `handle_message` у объекта `handler`.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от Telegram.

**Возвращает**:
- `None`

**Примеры**:

```python
@bot.message_handler(func=lambda message: message.text and not message.text.startswith('/'))
def handle_text_message(message):
    logger.info(f"User {message.from_user.username} sent message: {message.text}")
    handler.handle_message(bot, message)
```

### `handle_unknown_command`

```python
@bot.message_handler(func=lambda message: message.text and message.text.startswith('/'))
def handle_unknown_command(message):
    """
    Args:
        message (telebot.types.Message): Объект сообщения от Telegram.

    Returns:
        None

    Raises:
        No exceptions

    Example:
        Пример отправки неизвестной команды пользователем.
    """
```

**Описание**:
Обрабатывает неизвестные команды, отправляя сообщение об этом пользователю.

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
    """
    Args:
        None

    Returns:
        None

    Raises:
        Exception: В случае ошибки во время работы бота.

    Example:
        Запуск основного цикла работы бота.
    """
```

**Описание**:
Основная функция для запуска бота.

**Параметры**:
- `None`

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: В случае ошибки во время работы бота.

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
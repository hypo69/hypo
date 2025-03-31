# Модуль `minibot`

## Обзор

Модуль `minibot` представляет собой реализацию телеграм-бота для обслуживания запросов от пользователя Kazarinov. Он использует Google Gemini AI для обработки текстовых сообщений, поддерживает обработку URL-адресов, голосовых сообщений и документов. Бот может работать в двух режимах: `PRODUCTION` и `DEV`, используя различные токены и настройки в зависимости от режима.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для автоматизации взаимодействия с пользователем Kazarinov через Telegram. Он включает в себя обработку различных типов сообщений, взаимодействие с AI-моделью Gemini для генерации ответов и выполнение сценариев на основе полученных данных. Расположение файла в структуре проекта указывает на то, что это один из конечных точек (endpoints) взаимодействия с ботом.

## Классы

### `BotHandler`

**Описание**: Класс `BotHandler` предназначен для обработки команд и сообщений, получаемых от Telegram-бота. Он содержит методы для обработки текста, URL, голосовых сообщений и документов, а также для взаимодействия с AI-моделью Gemini.

**Как работает класс**:
Класс инициализируется списком вопросов `questions_list` и AI-моделью `GoogleGenerativeAI`. Метод `handle_message` определяет тип сообщения и вызывает соответствующий метод для его обработки. Методы `_send_user_flowchart`, `_handle_url`, `_handle_next_command`, `help_command`, `send_pdf`, `handle_voice` и `handle_document` обрабатывают различные типы команд и сообщений. Методы `_transcribe_voice` и `handle_document`  реализуют логику транскрибирования голосовых сообщений и обработки документов.

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
- `questions_list` (list[str]): Список вопросов для обработки команды `--next`.
- `model` (GoogleGenerativeAI): Объект AI-модели Google Gemini для обработки текста.

**Примеры**:

```python
handler = BotHandler()
```

### `Config`

**Описание**: Класс `Config` предназначен для хранения конфигурационных параметров бота, таких как токены доступа, ID каналов и пути к файлам.

**Как работает класс**:
Класс определяет параметры бота в зависимости от режима работы (`PRODUCTION` или `DEV`) и способа получения токенов (`USE_ENV`). Он содержит параметры для токенов Telegram-бота, ID каналов, путей к директориям и сообщения для различных команд.

**Параметры**:

- `BOT_TOKEN` (str): Токен доступа для Telegram-бота.
- `CHANNEL_ID` (str): ID канала для отправки сообщений.
- `PHOTO_DIR` (Path): Директория для хранения фотографий.
- `COMMAND_INFO` (str): Информация о боте для команды `/info`.
- `UNKNOWN_COMMAND_MESSAGE` (str): Сообщение для неизвестных команд.
- `START_MESSAGE` (str): Сообщение при запуске бота.
- `HELP_MESSAGE` (str): Сообщение с информацией о доступных командах.

**Примеры**:

```python
config = Config()
```

## Функции

### `handle_message`

```python
def handle_message(bot:telebot, message:'message'):
    """Обработка текстовых сообщений."""
    ...
```

**Описание**: Обрабатывает текстовые сообщения, полученные от пользователя.

**Как работает функция**:
Функция принимает объект бота и сообщение от пользователя. Она проверяет, является ли сообщение командой или URL, и вызывает соответствующий метод для обработки. Если сообщение не является командой или URL, оно отправляется в AI-модель Gemini для получения ответа.

**Параметры**:
- `bot` (telebot): Объект бота для отправки сообщений.
- `message` (message): Объект сообщения от пользователя.

**Вызывает исключения**:
- `Exception`: Возникает при ошибке взаимодействия с AI-моделью.

**Примеры**:

```python
@bot.message_handler(func=lambda message: message.text and not message.text.startswith('/'))
def handle_text_message(message):
    logger.info(f"User {message.from_user.username} sent message: {message.text}")
    handler.handle_message(bot, message )
```

### `_send_user_flowchart`

```python
def _send_user_flowchart(bot, chat_id):
    """Отправка схемы user_flowchart."""
    ...
```

**Описание**: Отправляет схему user_flowchart пользователю.

**Как работает функция**:
Функция принимает объект бота и ID чата пользователя. Она пытается открыть файл с изображением схемы и отправить его пользователю. Если файл не найден, отправляется сообщение об ошибке.

**Параметры**:
- `bot` (telebot): Объект бота для отправки сообщений.
- `chat_id` (int): ID чата пользователя.

**Вызывает исключения**:
- `FileNotFoundError`: Возникает, если файл схемы не найден.

**Примеры**:

```python
handler._send_user_flowchart(bot, message.chat.id)
```

### `_handle_url`

```python
def _handle_url(bot, message:'message'):
    """Обработка URL, присланного пользователем."""
    ...
```

**Описание**: Обрабатывает URL, присланный пользователем.

**Как работает функция**:
Функция принимает объект бота и сообщение от пользователя. Она проверяет, является ли URL ссылкой на `one-tab.com`, извлекает данные о товаре (мехирон) и URL комплектующих, а затем запускает сценарий для обработки этих данных.

**Параметры**:
- `bot` (telebot): Объект бота для отправки сообщений.
- `message` (message): Объект сообщения от пользователя.

**Вызывает исключения**:
- `Exception`: Возникает при ошибке получения данных из OneTab или при выполнении сценария.

**Примеры**:

```python
handler._handle_url(bot, message)
```

### `_handle_next_command`

```python
def _handle_next_command(bot, message):
    """Обработка команды '--next' и её аналогов."""
    ...
```

**Описание**: Обрабатывает команду '--next' и её аналоги.

**Как работает функция**:
Функция принимает объект бота и сообщение от пользователя. Она выбирает случайный вопрос из списка `questions_list` и отправляет его в AI-модель Gemini для получения ответа, который затем отправляется пользователю.

**Параметры**:
- `bot` (telebot): Объект бота для отправки сообщений.
- `message` (message): Объект сообщения от пользователя.

**Вызывает исключения**:
- `Exception`: Возникает при ошибке чтения вопросов или взаимодействия с AI-моделью.

**Примеры**:

```python
handler._handle_next_command(bot, message)
```

### `help_command`

```python
def help_command(bot, message):
    """Обработка команды /help."""
    ...
```

**Описание**: Обрабатывает команду /help.

**Как работает функция**:
Функция принимает объект бота и сообщение от пользователя. Она отправляет пользователю сообщение со списком доступных команд.

**Параметры**:
- `bot` (telebot): Объект бота для отправки сообщений.
- `message` (message): Объект сообщения от пользователя.

**Примеры**:

```python
handler.help_command(bot, message)
```

### `send_pdf`

```python
def send_pdf(bot, message, pdf_file):
    """Обработка команды /sendpdf для отправки PDF."""
    ...
```

**Описание**: Обрабатывает команду /sendpdf для отправки PDF.

**Как работает функция**:
Функция принимает объект бота, сообщение от пользователя и путь к PDF-файлу. Она пытается открыть файл и отправить его пользователю в виде документа. Если файл не найден, отправляется сообщение об ошибке.

**Параметры**:
- `bot` (telebot): Объект бота для отправки сообщений.
- `message` (message): Объект сообщения от пользователя.
- `pdf_file` (str): Путь к PDF-файлу.

**Вызывает исключения**:
- `Exception`: Возникает при ошибке открытия или отправки PDF-файла.

**Примеры**:

```python
handler.send_pdf(bot, message, 'example.pdf')
```

### `handle_voice`

```python
def handle_voice(bot, message):
    """Обработка голосовых сообщений."""
    ...
```

**Описание**: Обрабатывает голосовые сообщения.

**Как работает функция**:
Функция принимает объект бота и сообщение от пользователя. Она получает информацию о файле голосового сообщения, скачивает его, сохраняет во временный файл и пытается транскрибировать его в текст. Затем распознанный текст отправляется пользователю.

**Параметры**:
- `bot` (telebot): Объект бота для отправки сообщений.
- `message` (message): Объект сообщения от пользователя.

**Вызывает исключения**:
- `Exception`: Возникает при ошибке обработки голосового сообщения.

**Примеры**:

```python
handler.handle_voice(bot, message)
```

### `_transcribe_voice`

```python
def _transcribe_voice(self, file_path):
    """Транскрибирование голосового сообщения (заглушка)."""
    ...
```

**Описание**: Транскрибирование голосового сообщения (заглушка).

**Как работает функция**:
Функция принимает путь к файлу голосового сообщения и возвращает заглушку текста.

**Параметры**:
- `file_path` (str): Путь к файлу голосового сообщения.

**Возвращает**:
- `str`: Заглушка текста.

**Примеры**:

```python
transcribed_text = handler._transcribe_voice('voice.ogg')
```

### `handle_document`

```python
def handle_document(bot, message):
    """Обработка полученных документов."""
    ...
```

**Описание**: Обрабатывает полученные документы.

**Как работает функция**:
Функция принимает объект бота и сообщение от пользователя. Она получает информацию о файле документа, скачивает его, сохраняет во временный файл и отправляет пользователю сообщение о сохранении файла.

**Параметры**:
- `bot` (telebot): Объект бота для отправки сообщений.
- `message` (message): Объект сообщения от пользователя.

**Возвращает**:
- `bool`: `True` в случае успешной обработки, `False` в случае ошибки.

**Вызывает исключения**:
- `Exception`: Возникает при ошибке обработки документа.

**Примеры**:

```python
success = handler.handle_document(bot, message)
```

### `command_start`

```python
@bot.message_handler(commands=['start'])
def command_start(message):
    logger.info(f"User {message.from_user.username} send /start command")
    bot.send_message(message.chat.id, config.START_MESSAGE)
```

**Описание**: Обрабатывает команду `/start`.

**Как работает функция**:
Функция принимает объект сообщения от пользователя. Логирует информацию об использовании команды `/start` и отправляет пользователю приветственное сообщение из конфигурации бота.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от пользователя.

**Примеры**:

Пример вызова команды `/start` в Telegram:
```
/start
```

### `command_help`

```python
@bot.message_handler(commands=['help'])
def command_help(message):
    logger.info(f"User {message.from_user.username} send /help command")
    handler.help_command(bot, message)
```

**Описание**: Обрабатывает команду `/help`.

**Как работает функция**:
Функция принимает объект сообщения от пользователя. Логирует информацию об использовании команды `/help` и вызывает метод `help_command` обработчика `handler` для отправки пользователю справки о доступных командах.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от пользователя.

**Примеры**:

Пример вызова команды `/help` в Telegram:
```
/help
```

### `command_info`

```python
@bot.message_handler(commands=['info'])
def command_info(message):
    logger.info(f"User {message.from_user.username} send /info command")
    bot.send_message(message.chat.id, config.COMMAND_INFO)
```

**Описание**: Обрабатывает команду `/info`.

**Как работает функция**:
Функция принимает объект сообщения от пользователя. Логирует информацию об использовании команды `/info` и отправляет пользователю информацию о боте из конфигурации.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от пользователя.

**Примеры**:

Пример вызова команды `/info` в Telegram:
```
/info
```

### `command_time`

```python
@bot.message_handler(commands=['time'])
def command_time(message):
    logger.info(f"User {message.from_user.username} send /time command")
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    bot.send_message(message.chat.id, f"Current time: {current_time}")
```

**Описание**: Обрабатывает команду `/time`.

**Как работает функция**:
Функция принимает объект сообщения от пользователя. Логирует информацию об использовании команды `/time`, получает текущее время, форматирует его и отправляет пользователю.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от пользователя.

**Примеры**:

Пример вызова команды `/time` в Telegram:
```
/time
```

### `command_photo`

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

**Описание**: Обрабатывает команду `/photo`.

**Как работает функция**:
Функция принимает объект сообщения от пользователя. Логирует информацию об использовании команды `/photo`, пытается получить список файлов из директории с фотографиями, выбирает случайную фотографию и отправляет её пользователю. Если директория не найдена или в ней нет файлов, отправляется соответствующее сообщение об ошибке.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от пользователя.

**Вызывает исключения**:
- `FileNotFoundError`: Возникает, если директория с фотографиями не найдена.

**Примеры**:

Пример вызова команды `/photo` в Telegram:
```
/photo
```

### `handle_voice_message`

```python
@bot.message_handler(content_types=['voice'])
def handle_voice_message(message):
    logger.info(f"User {message.from_user.username} send voice message")
    handler.handle_voice(bot, message)
```

**Описание**: Обрабатывает голосовые сообщения.

**Как работает функция**:
Функция принимает объект сообщения от пользователя. Логирует информацию об отправке голосового сообщения и вызывает метод `handle_voice` обработчика `handler` для дальнейшей обработки голосового сообщения.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от пользователя.

**Примеры**:

Пример отправки голосового сообщения в Telegram.

### `handle_document_message`

```python
@bot.message_handler(content_types=['document'])
def handle_document_message(message):
    logger.info(f"User {message.from_user.username} send document message")
    handler.handle_document(bot, message)
```

**Описание**: Обрабатывает сообщения с документами.

**Как работает функция**:
Функция принимает объект сообщения от пользователя. Логирует информацию об отправке документа и вызывает метод `handle_document` обработчика `handler` для дальнейшей обработки документа.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от пользователя.

**Примеры**:

Пример отправки документа в Telegram.

### `handle_text_message`

```python
@bot.message_handler(func=lambda message: message.text and not message.text.startswith('/'))
def handle_text_message(message):
    logger.info(f"User {message.from_user.username} sent message: {message.text}")
    handler.handle_message(bot, message )
```

**Описание**: Обрабатывает текстовые сообщения, не являющиеся командами.

**Как работает функция**:
Функция принимает объект сообщения от пользователя. Логирует информацию об отправленном текстовом сообщении и вызывает метод `handle_message` обработчика `handler` для дальнейшей обработки сообщения.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от пользователя.

**Примеры**:

Пример отправки текстового сообщения в Telegram:
```
Привет, бот!
```

### `handle_unknown_command`

```python
@bot.message_handler(func=lambda message: message.text and message.text.startswith('/'))
def handle_unknown_command(message):
    logger.info(f"User {message.from_user.username} send unknown command: {message.text}")
    bot.send_message(message.chat.id, config.UNKNOWN_COMMAND_MESSAGE)
```

**Описание**: Обрабатывает неизвестные команды.

**Как работает функция**:
Функция принимает объект сообщения от пользователя. Логирует информацию об отправленной неизвестной команде и отправляет пользователю сообщение о том, что команда неизвестна.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от пользователя.

**Примеры**:

Пример отправки неизвестной команды в Telegram:
```
/неизвестная_команда
```

### `main`

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
```

**Описание**: Главная функция для запуска бота.

**Как работает функция**:
Функция инициализирует и запускает бота в режиме `PRODUCTION` или `DEV`. В случае возникновения ошибки во время работы, логирует ошибку, останавливает бота и перезапускает его.

**Вызывает исключения**:
- `Exception`: Возникает при ошибке во время работы бота.

**Примеры**:

Запуск бота:
```python
if __name__ == '__main__':
    main()
```
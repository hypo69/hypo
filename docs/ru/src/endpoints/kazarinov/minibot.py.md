# Модуль `minibot`

## Обзор

Модуль `minibot` предназначен для обслуживания запросов через Telegram-бота от пользователя Kazarinov. Он включает в себя обработку текстовых сообщений, URL, голосовых сообщений и документов, а также взаимодействие с AI-моделью Google Gemini для генерации ответов на вопросы.

## Подробней

Этот модуль является частью проекта `hypotez` и отвечает за реализацию функциональности Telegram-бота, который взаимодействует с пользователем Kazarinov. Он использует библиотеку `telebot` для обработки входящих сообщений и отправки ответов. Модуль также включает в себя интеграцию с AI-моделью Google Gemini для обработки текстовых запросов и генерации ответов. Дополнительно, модуль поддерживает обработку URL, голосовых сообщений и документов, предоставляя пользователю различные возможности взаимодействия с ботом.

## Классы

### `BotHandler`

**Описание**: Класс `BotHandler` является обработчиком команд, получаемых от Telegram-бота. Он содержит методы для обработки различных типов сообщений и команд, а также для взаимодействия с AI-моделью Google Gemini.

**Как работает класс**:
Класс `BotHandler` инициализируется с использованием списка вопросов и модели Google Gemini. Он содержит методы для обработки текстовых сообщений, URL, голосовых сообщений и документов. Класс также предоставляет методы для отправки схемы `user_flowchart` и обработки команды `/help`.

**Методы**:

- `__init__(self)`
- `handle_message(self, bot: telebot, message: 'message')`
- `_send_user_flowchart(self, bot, chat_id)`
- `_handle_url(self, bot, message: 'message')`
- `_handle_next_command(self, bot, message)`
- `help_command(self, bot, message)`
- `send_pdf(self, bot, message, pdf_file)`
- `handle_voice(self, bot, message)`
- `_transcribe_voice(self, file_path)`
- `handle_document(self, bot, message)`

#### `__init__`

```python
    def __init__(self):
        """Инициализация обработчика событий телеграм-бота."""
        self.questions_list = ['Я не понял?', 'Объясни пожалуйста']
        self.model = GoogleGenerativeAI(os.getenv('GEMINI_API') if USE_ENV else gs.credentials.gemini.kazarinov)
```

**Описание**: Инициализирует обработчик событий Telegram-бота, устанавливая список вопросов и модель Google Gemini.

**Как работает функция**:
1. Инициализирует список вопросов `questions_list`, который содержит фразы, используемые для запроса дополнительной информации у пользователя.
2. Инициализирует модель Google Gemini (`self.model`) с использованием API-ключа, полученного из переменных окружения (`os.getenv('GEMINI_API')`) или из учетных данных Google Cloud Storage (`gs.credentials.gemini.kazarinov`), в зависимости от значения флага `USE_ENV`.

#### `handle_message`

```python
    def handle_message(self, bot:telebot, message:'message'):
        """Обработка текстовых сообщений."""
        text = message.text
        if text == '?':
            self._send_user_flowchart(bot, message.chat.id)
        elif is_url(text):
            self._handle_url(bot, message)
        elif text in ('--next', '-next', '__next', '-n', '-q'):
            self._handle_next_command(bot, message)
        else:
            try:
                answer = self.model.chat(text)
                bot.send_message(message.chat.id, answer)
            except Exception as ex:
                logger.error(f"Error during model interaction: {ex}")
                bot.send_message(message.chat.id, "Произошла ошибка при обработке сообщения.")
```

**Описание**: Обрабатывает текстовые сообщения, полученные от пользователя.

**Параметры**:
- `bot` (telebot): Экземпляр Telegram-бота.
- `message` (message): Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Как работает функция**:
1. Извлекает текст сообщения из объекта `message`.
2. Проверяет, является ли текст сообщения вопросительным знаком (`?`). Если да, вызывает метод `_send_user_flowchart` для отправки схемы user_flowchart пользователю.
3. Проверяет, является ли текст сообщения URL. Если да, вызывает метод `_handle_url` для обработки URL.
4. Проверяет, является ли текст сообщения командой `"--next"` или ее аналогами. Если да, вызывает метод `_handle_next_command` для обработки команды.
5. Если текст сообщения не является ни одним из вышеперечисленных, пытается получить ответ от модели Google Gemini с помощью метода `self.model.chat(text)` и отправляет ответ пользователю.
6. Если во время взаимодействия с моделью возникает ошибка, логирует ошибку с использованием `logger.error` и отправляет пользователю сообщение об ошибке.

#### `_send_user_flowchart`

```python
    def _send_user_flowchart(self, bot, chat_id):
        """Отправка схемы user_flowchart."""
        photo_path = self.base_dir / 'assets' / 'user_flowchart.png'
        try:
            with open(photo_path, 'rb') as photo:
                bot.send_photo(chat_id, photo)
        except FileNotFoundError:
            logger.error(f"File not found: {photo_path}")
            bot.send_message(chat_id, "Схема не найдена.")
```

**Описание**: Отправляет пользователю схему `user_flowchart` в виде фотографии.

**Параметры**:
- `bot` (telebot): Экземпляр Telegram-бота.
- `chat_id` (int): Идентификатор чата, в который нужно отправить фотографию.

**Как работает функция**:
1. Формирует путь к файлу фотографии `user_flowchart.png` в директории `assets`.
2. Пытается открыть файл фотографии в режиме чтения байтов (`'rb'`) и отправить его пользователю с помощью метода `bot.send_photo`.
3. Если файл не найден, логирует ошибку с использованием `logger.error` и отправляет пользователю сообщение об ошибке.

#### `_handle_url`

```python
    def _handle_url(self, bot, message:'message'):
        """Обработка URL, присланного пользователем."""
        url = message.text
        if not url.startswith(('https://one-tab.com', 'https://www.one-tab.com')):\
            bot.send_message(message.chat.id, 'Мне на вход нужен URL `https://one-tab.com` Проверь, что ты мне посылаешь')
            return

        # Parsing https//one-tab.com/XXXXXXXXX 
        try:
           price, mexiron_name, urls = fetch_target_urls_onetab(url)
           bot.send_message(message.chat.id, f'Получил мехирон {mexiron_name} - {price} шек')
        except Exception as ex:
            logger.error(f"Error fetching URLs from OneTab: ",ex)
            bot.send_message(message.chat.id, "Произошла ошибка при получении данных из OneTab.")
            return
        if not urls:
            bot.send_message(message.chat.id, 'Некорректные данные. Не получил список URL комплектующих')
            return

        try:
            #self.scenario = Scenario(window_mode = 'headless' if MODE == 'PRODUCTION' else 'normal' )
            self.scenario = Scenario(window_mode = 'headless' ) # debug
            asyncio.run(\
                self.scenario.run_scenario_async(\
                mexiron_name = mexiron_name,\
                urls = list(urls), \
                price = price,\
                bot = bot,\
                chat_id = message.chat.id,))\

        \

        except Exception as ex:
            logger.error(f"Error during scenario execution:", ex)
            bot.send_message(message.chat.id, f"Произошла ошибка при выполнении сценария. {ex}")
```

**Описание**: Обрабатывает URL, присланный пользователем, извлекает данные и запускает сценарий.

**Параметры**:
- `bot` (telebot): Экземпляр Telegram-бота.
- `message` (message): Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Как работает функция**:
1. Извлекает URL из текста сообщения.
2. Проверяет, начинается ли URL с `'https://one-tab.com'` или `'https://www.one-tab.com'`. Если нет, отправляет пользователю сообщение об ошибке и завершает выполнение функции.
3. Пытается извлечь цену, название мехирона и список URL из OneTab с помощью функции `fetch_target_urls_onetab(url)`.
4. Если во время извлечения данных возникает ошибка, логирует ошибку с использованием `logger.error` и отправляет пользователю сообщение об ошибке.
5. Если список URL пуст, отправляет пользователю сообщение об ошибке.
6. Инициализирует объект `Scenario` с режимом окна `'headless'`.
7. Запускает асинхронный сценарий `self.scenario.run_scenario_async` с передачей названия мехирона, списка URL, цены, объекта бота и идентификатора чата.
8. Если во время выполнения сценария возникает ошибка, логирует ошибку с использованием `logger.error` и отправляет пользователю сообщение об ошибке.

#### `_handle_next_command`

```python
    def _handle_next_command(self, bot, message):
        """Обработка команды '--next' и её аналогов."""
        try:
            question = random.choice(self.questions_list)
            answer = self.model.ask(question)
            bot.send_message(message.chat.id, question)
            bot.send_message(message.chat.id, answer)
        except Exception as ex:
            logger.error(f'Ошибка чтения вопросов: {ex}')
            bot.send_message(message.chat.id, 'Произошла ошибка при чтении вопросов.')
```

**Описание**: Обрабатывает команду "--next" и ее аналоги, выбирает случайный вопрос из списка и отправляет его пользователю вместе с ответом от модели.

**Параметры**:
- `bot` (telebot): Экземпляр Telegram-бота.
- `message` (message): Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Как работает функция**:
1. Пытается выбрать случайный вопрос из списка `self.questions_list` с помощью функции `random.choice`.
2. Получает ответ от модели Google Gemini с помощью метода `self.model.ask(question)`.
3. Отправляет выбранный вопрос и полученный ответ пользователю.
4. Если во время выполнения возникает ошибка, логирует ошибку с использованием `logger.error` и отправляет пользователю сообщение об ошибке.

#### `help_command`

```python
    def help_command(self, bot, message):
        """Обработка команды /help."""
        bot.send_message(\
            message.chat.id,\
            'Available commands:\\n'\
            '/start - Start the bot\\n'\
            '/help - Show this help message\\n'\
            '/sendpdf - Send a PDF file'\
        )
```

**Описание**: Обрабатывает команду `/help`, отправляя пользователю список доступных команд.

**Параметры**:
- `bot` (telebot): Экземпляр Telegram-бота.
- `message` (message): Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Как работает функция**:
Отправляет пользователю сообщение со списком доступных команд: `/start`, `/help` и `/sendpdf`.

#### `send_pdf`

```python
    def send_pdf(self, bot, message, pdf_file):
        """Обработка команды /sendpdf для отправки PDF."""
        try:
            with open(pdf_file, 'rb') as pdf_file_obj:
                bot.send_document(message.chat.id, document=pdf_file_obj)
        except Exception as ex:
            logger.error(f'Ошибка при отправке PDF-файла: {ex}')
            bot.send_message(message.chat.id, 'Произошла ошибка при отправке PDF-файла. Попробуй ещё раз.')
```

**Описание**: Обрабатывает команду `/sendpdf`, отправляя пользователю PDF-файл.

**Параметры**:
- `bot` (telebot): Экземпляр Telegram-бота.
- `message` (message): Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.
- `pdf_file` (str): Путь к PDF-файлу, который нужно отправить.

**Как работает функция**:
1. Пытается открыть PDF-файл в режиме чтения байтов (`'rb'`).
2. Отправляет PDF-файл пользователю с помощью метода `bot.send_document`.
3. Если во время выполнения возникает ошибка, логирует ошибку с использованием `logger.error` и отправляет пользователю сообщение об ошибке.

#### `handle_voice`

```python
    def handle_voice(self, bot, message):
        """Обработка голосовых сообщений."""
        try:
            file_info = bot.get_file(message.voice.file_id)
            file = bot.download_file(file_info.file_path)
            file_path = gs.path.temp / f'{message.voice.file_id}.ogg'
            with open(file_path, 'wb') as f:
                f.write(file)
            transcribed_text = self._transcribe_voice(file_path)
            bot.send_message(message.chat.id, f'Распознанный текст: {transcribed_text}')
        except Exception as ex:
            logger.error(f'Ошибка при обработке голосового сообщения: {ex}')
            bot.send_message(message.chat.id, 'Произошла ошибка при обработке голосового сообщения. Попробуй ещё раз.')
```

**Описание**: Обрабатывает голосовые сообщения, полученные от пользователя.

**Параметры**:
- `bot` (telebot): Экземпляр Telegram-бота.
- `message` (message): Объект сообщения, содержащий информацию о голосовом сообщении, отправленном пользователем.

**Как работает функция**:
1. Получает информацию о файле голосового сообщения с помощью метода `bot.get_file(message.voice.file_id)`.
2. Скачивает файл голосового сообщения с помощью метода `bot.download_file(file_info.file_path)`.
3. Формирует путь к временному файлу для сохранения голосового сообщения в формате `.ogg`.
4. Сохраняет скачанный файл во временный файл.
5. Пытается транскрибировать голосовое сообщение с помощью метода `self._transcribe_voice(file_path)`.
6. Отправляет распознанный текст пользователю.
7. Если во время выполнения возникает ошибка, логирует ошибку с использованием `logger.error` и отправляет пользователю сообщение об ошибке.

#### `_transcribe_voice`

```python
    def _transcribe_voice(self, file_path):
        """Транскрибирование голосового сообщения (заглушка)."""
        return 'Распознавание голоса ещё не реализовано.'
```

**Описание**: Транскрибирует голосовое сообщение (заглушка).

**Параметры**:
- `file_path` (str): Путь к файлу голосового сообщения.

**Как работает функция**:
Возвращает строку `'Распознавание голоса ещё не реализовано.'`, так как транскрибирование голосовых сообщений ещё не реализовано.

#### `handle_document`

```python
    def handle_document(self, bot, message):
        """Обработка полученных документов."""
        try:
            file_info = bot.get_file(message.document.file_id)
            file = bot.download_file(file_info.file_path)
            tmp_file_path = gs.path.temp / message.document.file_name
            with open(tmp_file_path, 'wb') as f:
                f.write(file)
            bot.send_message(message.chat.id, f'Файл сохранен в {tmp_file_path}')
            return True
        except Exception as ex:
            logger.error(f'Ошибка при обработке документа: {ex}')
            bot.send_message(message.chat.id, 'Произошла ошибка при обработке документа. Попробуй ещё раз.')
            return False
```

**Описание**: Обрабатывает полученные документы, сохраняя их во временную директорию.

**Параметры**:
- `bot` (telebot): Экземпляр Telegram-бота.
- `message` (message): Объект сообщения, содержащий информацию о документе, отправленном пользователем.

**Как работает функция**:
1. Получает информацию о файле документа с помощью метода `bot.get_file(message.document.file_id)`.
2. Скачивает файл документа с помощью метода `bot.download_file(file_info.file_path)`.
3. Формирует путь к временному файлу для сохранения документа.
4. Сохраняет скачанный файл во временный файл.
5. Отправляет пользователю сообщение об успешном сохранении файла и возвращает `True`.
6. Если во время выполнения возникает ошибка, логирует ошибку с использованием `logger.error` и отправляет пользователю сообщение об ошибке, возвращая `False`.

### `Config`

**Описание**: Класс `Config` содержит настройки для Telegram-бота, такие как токен бота, идентификатор канала, директория с фотографиями и сообщения для различных команд.

**Как работает класс**:
Класс `Config` определяет настройки бота в зависимости от режима работы (`PRODUCTION` или `DEV`) и источника получения ключей (`USE_ENV`). Он содержит токен бота, идентификатор канала, директорию с фотографиями и сообщения для различных команд.

**Параметры**:

- `BOT_TOKEN` (str): Токен Telegram-бота.
- `CHANNEL_ID` (str): Идентификатор канала.
- `PHOTO_DIR` (Path): Путь к директории с фотографиями.
- `COMMAND_INFO` (str): Информация о боте для команды `/info`.
- `UNKNOWN_COMMAND_MESSAGE` (str): Сообщение для неизвестной команды.
- `START_MESSAGE` (str): Сообщение для команды `/start`.
- `HELP_MESSAGE` (str): Сообщение для команды `/help`.

## Функции

### `command_start`

```python
@bot.message_handler(commands=['start'])
def command_start(message):
    logger.info(f"User {message.from_user.username} send /start command")
    bot.send_message(message.chat.id, config.START_MESSAGE)
```

**Описание**: Обрабатывает команду `/start`, отправляя пользователю приветственное сообщение.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Как работает функция**:
1. Логирует информацию об использовании команды `/start` пользователем с помощью `logger.info`.
2. Отправляет пользователю приветственное сообщение, содержащееся в `config.START_MESSAGE`.

### `command_help`

```python
@bot.message_handler(commands=['help'])
def command_help(message):
    logger.info(f"User {message.from_user.username} send /help command")
    handler.help_command(bot, message)
```

**Описание**: Обрабатывает команду `/help`, вызывая метод `help_command` обработчика `handler`.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Как работает функция**:
1. Логирует информацию об использовании команды `/help` пользователем с помощью `logger.info`.
2. Вызывает метод `handler.help_command(bot, message)` для отправки пользователю списка доступных команд.

### `command_info`

```python
@bot.message_handler(commands=['info'])
def command_info(message):
    logger.info(f"User {message.from_user.username} send /info command")
    bot.send_message(message.chat.id, config.COMMAND_INFO)
```

**Описание**: Обрабатывает команду `/info`, отправляя пользователю информацию о боте.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Как работает функция**:
1. Логирует информацию об использовании команды `/info` пользователем с помощью `logger.info`.
2. Отправляет пользователю информацию о боте, содержащуюся в `config.COMMAND_INFO`.

### `command_time`

```python
@bot.message_handler(commands=['time'])
def command_time(message):
    logger.info(f"User {message.from_user.username} send /time command")
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    bot.send_message(message.chat.id, f"Current time: {current_time}")
```

**Описание**: Обрабатывает команду `/time`, отправляя пользователю текущее время.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Как работает функция**:
1. Логирует информацию об использовании команды `/time` пользователем с помощью `logger.info`.
2. Получает текущее время с помощью `datetime.datetime.now()`.
3. Форматирует текущее время в строку в формате `"%H:%M:%S"` с помощью `strftime`.
4. Отправляет пользователю сообщение с текущим временем.

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

**Описание**: Обрабатывает команду `/photo`, отправляя пользователю случайную фотографию из директории `config.PHOTO_DIR`.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Как работает функция**:
1. Логирует информацию об использовании команды `/photo` пользователем с помощью `logger.info`.
2. Пытается получить список файлов в директории `config.PHOTO_DIR` с помощью `os.listdir`.
3. Если список файлов не пуст, выбирает случайную фотографию с помощью `random.choice` и формирует полный путь к файлу.
4. Открывает файл фотографии в режиме чтения байтов (`'rb'`) и отправляет его пользователю с помощью `bot.send_photo`.
5. Если список файлов пуст, отправляет пользователю сообщение `"No photos in the folder."`.
6. Если директория не найдена, отправляет пользователю сообщение `"Photo directory not found."`.

### `handle_voice_message`

```python
@bot.message_handler(content_types=['voice'])
def handle_voice_message(message):
    logger.info(f"User {message.from_user.username} send voice message")
    handler.handle_voice(bot, message)
```

**Описание**: Обрабатывает голосовые сообщения, перенаправляя их обработчику `handler`.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения, содержащий информацию о голосовом сообщении, отправленном пользователем.

**Как работает функция**:
1. Логирует информацию о получении голосового сообщения от пользователя с помощью `logger.info`.
2. Вызывает метод `handler.handle_voice(bot, message)` для обработки голосового сообщения.

### `handle_document_message`

```python
@bot.message_handler(content_types=['document'])
def handle_document_message(message):
    logger.info(f"User {message.from_user.username} send document message")
    handler.handle_document(bot, message)
```

**Описание**: Обрабатывает сообщения с документами, перенаправляя их обработчику `handler`.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения, содержащий информацию о документе, отправленном пользователем.

**Как работает функция**:
1. Логирует информацию о получении сообщения с документом от пользователя с помощью `logger.info`.
2. Вызывает метод `handler.handle_document(bot, message)` для обработки документа.

### `handle_text_message`

```python
@bot.message_handler(func=lambda message: message.text and not message.text.startswith('/'))
def handle_text_message(message):
    logger.info(f"User {message.from_user.username} sent message: {message.text}")
    handler.handle_message(bot, message )
```

**Описание**: Обрабатывает текстовые сообщения, не являющиеся командами, перенаправляя их обработчику `handler`.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения, содержащий информацию о текстовом сообщении, отправленном пользователем.

**Как работает функция**:
1. Логирует информацию о получении текстового сообщения от пользователя с помощью `logger.info`.
2. Вызывает метод `handler.handle_message(bot, message)` для обработки текстового сообщения.

### `handle_unknown_command`

```python
@bot.message_handler(func=lambda message: message.text and message.text.startswith('/'))
def handle_unknown_command(message):
    logger.info(f"User {message.from_user.username} send unknown command: {message.text}")
    bot.send_message(message.chat.id, config.UNKNOWN_COMMAND_MESSAGE)
```

**Описание**: Обрабатывает неизвестные команды, отправляя пользователю сообщение об этом.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения, содержащий информацию о неизвестной команде, отправленной пользователем.

**Как работает функция**:
1. Логирует информацию о получении неизвестной команды от пользователя с помощью `logger.info`.
2. Отправляет пользователю сообщение об неизвестной команде, содержащееся в `config.UNKNOWN_COMMAND_MESSAGE`.

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

**Описание**: Запускает Telegram-бота в режиме опроса.

**Как работает функция**:
1. Пытается запустить бота в режиме опроса с помощью `bot.polling(none_stop=True)`.
2. Если во время работы бота возникает ошибка, логирует ошибку с использованием `logger.error`, останавливает бота и перезапускает функцию `main`.
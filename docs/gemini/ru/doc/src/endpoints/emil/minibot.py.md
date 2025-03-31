# Модуль `src.endpoints.emil.minibot`

## Обзор

Модуль представляет собой простой Telegram-бот, предназначенный для обработки запросов, связанных с сайтом emil-design.com. Он включает в себя обработку текстовых сообщений, URL-адресов, голосовых сообщений и документов. Бот использует Google Gemini AI для генерации ответов на текстовые запросы и выполняет сценарии для обработки URL-адресов, полученных от пользователей.

## Подробней

Этот модуль является частью проекта `hypotez` и расположен в каталоге `src/endpoints/emil`. Он предназначен для работы с Telegram API через библиотеку `telebot`. Бот может обрабатывать различные типы сообщений, предоставляя пользователям информацию и выполняя определенные действия в зависимости от полученных данных. Ключевые особенности включают интеграцию с AI моделью Google Gemini для обработки текста и возможность выполнения сценариев на основе URL-адресов, предоставляемых пользователями.

## Классы

### `BotHandler`

**Описание**: Класс `BotHandler` предназначен для обработки команд, полученных от Telegram-бота.

**Как работает класс**:
Класс инициализируется с экземпляром `Scenario` и `GoogleGenerativeAI`. Он содержит методы для обработки различных типов сообщений, таких как текстовые сообщения, URL-адреса и команды. В зависимости от типа сообщения, вызываются соответствующие методы для обработки запроса и отправки ответа пользователю.

**Методы**:
- `__init__`: Инициализирует обработчик событий телеграм-бота.
- `handle_message`: Обрабатывает текстовые сообщения.
- `_send_user_flowchart`: Отправляет схему user_flowchart.
- `_handle_url`: Обрабатывает URL, присланный пользователем.
- `_handle_next_command`: Обрабатывает команду '--next' и её аналоги.
- `help_command`: Обрабатывает команду /help.
- `send_pdf`: Обрабатывает команду /sendpdf для отправки PDF.
- `handle_voice`: Обрабатывает голосовые сообщения.
- `_transcribe_voice`: Транскрибирование голосового сообщения (заглушка).
- `handle_document`: Обрабатывает полученные документы.

#### `__init__`
```python
    def __init__(self):
        """Инициализация обработчика событий телеграм-бота."""
        self.scenario = Scenario()
        self.model = GoogleGenerativeAI(os.getenv('GEMINI_API')) 
        self.questions_list = ['Я не понял?', 'Объясни пожалуйста']
```
**Как работает функция**:
Функция инициализирует экземпляр класса `BotHandler`. В ней создаются экземпляры классов `Scenario` и `GoogleGenerativeAI`, а также инициализируется список вопросов `questions_list`.
- `self.scenario` - инициализируется классом `Scenario`, который, по всей видимости, выполняет операции, связанные с обработкой сценариев.
- `self.model` - инициализируется классом `GoogleGenerativeAI` с использованием API-ключа Gemini, полученного из переменных окружения. Этот объект используется для взаимодействия с моделью генеративного ИИ от Google.
- `self.questions_list` - список, содержащий варианты вопросов, которые могут быть использованы ботом.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- Отсутствует.

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

**Как работает функция**:
Функция `handle_message` обрабатывает текстовые сообщения, полученные от пользователя. В зависимости от содержания сообщения, выполняются различные действия:

1.  Если сообщение содержит только символ `?`, вызывается метод `_send_user_flowchart` для отправки схемы user_flowchart.

2.  Если сообщение является URL-адресом (определяется с помощью функции `is_url`), вызывается метод `_handle_url` для обработки URL.

3.  Если сообщение является одной из команд `('--next', '-next', '__next', '-n', '-q')`, вызывается метод `_handle_next_command`.

4.  В противном случае, функция пытается получить ответ от модели `GoogleGenerativeAI` с помощью метода `self.model.chat(text)` и отправить его пользователю. Если во время взаимодействия с моделью происходит ошибка, она логируется с использованием `logger.error`, и пользователю отправляется сообщение об ошибке.

**Параметры**:
- `bot` (telebot): Экземпляр телеграм-бота.
- `message` (message): Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Возвращает**:
- Отсутствует.

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

**Как работает функция**:
Функция `_send_user_flowchart` отправляет пользователю схему `user_flowchart` в виде фотографии. Она получает путь к файлу изображения из атрибута `self.base_dir`, открывает файл и отправляет его пользователю с помощью метода `bot.send_photo`. Если файл не найден, в лог записывается сообщение об ошибке, и пользователю отправляется сообщение о том, что схема не найдена.

**Параметры**:
- `bot`: Экземпляр телеграм-бота.
- `chat_id`: Идентификатор чата, куда нужно отправить сообщение.

**Возвращает**:
- Отсутствует.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл схемы не найден.

#### `_handle_url`
```python
    def _handle_url(self, bot, message:'message'):
        """Обработка URL, присланного пользователем."""
        url = message.text
        if not url.startswith(('https://one-tab.com', 'https://www.one-tab.com')):\n            bot.send_message(message.chat.id, 'Мне на вход нужен URL `https://one-tab.com` Проверь, что ты мне посылаешь')
            return

        # Parsing https//one-tab.com/XXXXXXXXX page
        try:
           price, mexiron_name, urls = fetch_target_urls_onetab(url)
           bot.send_message(message.chat.id, f'Получил мехирон {mexiron_name} - {price} шек')
        except Exception as ex:
            logger.error(f"Error fetching URLs from OneTab: {ex}")
            bot.send_message(message.chat.id, "Произошла ошибка при получении данных из OneTab.")
            return
        if not urls:
            bot.send_message(message.chat.id, 'Некорректные данные. Не получил список URL комплектующих')
            return

        try:
            asyncio.run(\n                self.scenario.run_scenario(\n                        bot=bot,\n                        chat_id=message.chat.id,\n                        urls=list(urls), \n                        price=price,\n                        mexiron_name=mexiron_name\n                ))

        except Exception as ex:
            logger.error(f"Error during scenario execution: {ex}")
            bot.send_message(message.chat.id, f"Произошла ошибка при выполнении сценария. {print(ex.args)}")
```
**Как работает функция**:
Функция `_handle_url` обрабатывает URL-адрес, отправленный пользователем.

1.  Сначала проверяется, начинается ли URL с `https://one-tab.com` или `https://www.one-tab.com`. Если нет, пользователю отправляется сообщение с просьбой проверить URL.

2.  Затем функция пытается извлечь цену, имя и список URL-адресов с помощью функции `fetch_target_urls_onetab`. В случае успеха пользователю отправляется сообщение с именем и ценой.

3.  Если не удается извлечь данные, в лог записывается сообщение об ошибке, и пользователю отправляется сообщение об ошибке.

4.  Если список URL-адресов пуст, пользователю отправляется сообщение о некорректных данных.

5.  В случае успешного получения данных, запускается сценарий `self.scenario.run_scenario` с использованием `asyncio.run`, передавая ему бота, идентификатор чата, список URL-адресов, цену и имя.

6.  Если во время выполнения сценария происходит ошибка, она логируется с использованием `logger.error`, и пользователю отправляется сообщение об ошибке.

**Параметры**:
- `bot`: Экземпляр телеграм-бота.
- `message` (message): Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Возвращает**:
- Отсутствует.

**Вызывает исключения**:
- Различные исключения, которые могут возникнуть при извлечении данных из URL или выполнении сценария.

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

**Как работает функция**:
Функция `_handle_next_command` обрабатывает команду `--next` и её аналоги.

1.  Она выбирает случайный вопрос из списка `self.questions_list`.

2.  Затем отправляет этот вопрос и ответ, полученный от модели `self.model.ask(question)`, пользователю.

3.  Если во время этого процесса происходит ошибка, она логируется с использованием `logger.error`, и пользователю отправляется сообщение об ошибке.

**Параметры**:
- `bot`: Экземпляр телеграм-бота.
- `message`: Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Возвращает**:
- Отсутствует.

**Вызывает исключения**:
- Различные исключения, которые могут возникнуть при выборе вопроса или взаимодействии с моделью.

#### `help_command`
```python
    def help_command(self, bot, message):
        """Обработка команды /help."""
        bot.send_message(\n            message.chat.id,\n            'Available commands:\\n'\n            '/start - Start the bot\\n'\n            '/help - Show this help message\\n'\n            '/sendpdf - Send a PDF file'\n        )
```

**Как работает функция**:
Функция `help_command` обрабатывает команду `/help`. Она отправляет пользователю сообщение со списком доступных команд и их описанием.

**Параметры**:
- `bot`: Экземпляр телеграм-бота.
- `message`: Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Возвращает**:
- Отсутствует.

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

**Как работает функция**:
Функция `send_pdf` обрабатывает команду `/sendpdf` для отправки PDF-файла пользователю.

1.  Она пытается открыть PDF-файл, указанный в параметре `pdf_file`.

2.  Затем отправляет этот файл пользователю с помощью метода `bot.send_document`.

3.  Если во время этого процесса происходит ошибка, она логируется с использованием `logger.error`, и пользователю отправляется сообщение об ошибке.

**Параметры**:
- `bot`: Экземпляр телеграм-бота.
- `message`: Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.
- `pdf_file`: Путь к PDF-файлу, который нужно отправить.

**Возвращает**:
- Отсутствует.

**Вызывает исключения**:
- Различные исключения, которые могут возникнуть при открытии или отправке PDF-файла.

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

**Как работает функция**:
Функция `handle_voice` обрабатывает голосовые сообщения, полученные от пользователя.

1.  Она получает информацию о файле голосового сообщения с помощью метода `bot.get_file`.

2.  Затем загружает файл с помощью метода `bot.download_file`.

3.  Сохраняет файл во временную директорию.

4.  Вызывает метод `_transcribe_voice` для транскрибирования голосового сообщения в текст.

5.  Отправляет распознанный текст пользователю.

6.  Если во время этого процесса происходит ошибка, она логируется с использованием `logger.error`, и пользователю отправляется сообщение об ошибке.

**Параметры**:
- `bot`: Экземпляр телеграм-бота.
- `message`: Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Возвращает**:
- Отсутствует.

**Вызывает исключения**:
- Различные исключения, которые могут возникнуть при получении, загрузке, сохранении или транскрибировании голосового сообщения.

#### `_transcribe_voice`
```python
    def _transcribe_voice(self, file_path):
        """Транскрибирование голосового сообщения (заглушка)."""
        return 'Распознавание голоса ещё не реализовано.'
```

**Как работает функция**:
Функция `_transcribe_voice` представляет собой заглушку для транскрибирования голосового сообщения в текст. В текущей реализации она просто возвращает сообщение о том, что распознавание голоса ещё не реализовано.

**Параметры**:
- `file_path`: Путь к файлу голосового сообщения.

**Возвращает**:
- Строка с сообщением о том, что распознавание голоса ещё не реализовано.

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

**Как работает функция**:
Функция `handle_document` обрабатывает полученные документы.

1.  Она получает информацию о файле документа с помощью метода `bot.get_file`.

2.  Затем загружает файл с помощью метода `bot.download_file`.

3.  Сохраняет файл во временную директорию.

4.  Отправляет пользователю сообщение о том, что файл сохранен, и возвращает `True`.

5.  Если во время этого процесса происходит ошибка, она логируется с использованием `logger.error`, пользователю отправляется сообщение об ошибке, и возвращается `False`.

**Параметры**:
- `bot`: Экземпляр телеграм-бота.
- `message`: Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Возвращает**:
- `True`, если файл успешно обработан и сохранен.
- `False`, если произошла ошибка при обработке файла.

### `Config`

**Описание**: Класс `Config` предназначен для хранения конфигурационных параметров бота.

**Как работает класс**:
Класс содержит статические переменные, которые используются для конфигурации бота, такие как токен Telegram бота, ID канала, директория с фотографиями и сообщения для различных команд.

**Переменные**:
- `BOT_TOKEN`: Токен Telegram бота, полученный из переменной окружения или из базы данных.
- `CHANNEL_ID`: ID канала Telegram.
- `PHOTO_DIR`: Путь к директории с фотографиями.
- `COMMAND_INFO`: Информация о боте, отображаемая по команде `/info`.
- `UNKNOWN_COMMAND_MESSAGE`: Сообщение, отображаемое при вводе неизвестной команды.
- `START_MESSAGE`: Сообщение, отображаемое при старте бота.
- `HELP_MESSAGE`: Сообщение, отображаемое при вызове команды `/help`.

## Функции

### `command_start`
```python
@bot.message_handler(commands=['start'])
def command_start(message):
    logger.info(f"User {message.from_user.username} send /start command")
    bot.send_message(message.chat.id, config.START_MESSAGE)
```

**Как работает функция**:
Функция `command_start` обрабатывает команду `/start`, отправленную пользователем.

1.  Записывает в лог информацию о том, что пользователь отправил команду `/start`.

2.  Отправляет пользователю приветственное сообщение, содержащееся в переменной `config.START_MESSAGE`.

**Параметры**:
- `message`: Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Возвращает**:
- Отсутствует.

### `command_help`
```python
@bot.message_handler(commands=['help'])
def command_help(message):
    logger.info(f"User {message.from_user.username} send /help command")
    handler.help_command(bot, message)
```

**Как работает функция**:
Функция `command_help` обрабатывает команду `/help`, отправленную пользователем.

1.  Записывает в лог информацию о том, что пользователь отправил команду `/help`.

2.  Вызывает метод `help_command` объекта `handler` для отправки пользователю справочного сообщения.

**Параметры**:
- `message`: Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Возвращает**:
- Отсутствует.

### `command_info`
```python
@bot.message_handler(commands=['info'])
def command_info(message):
    logger.info(f"User {message.from_user.username} send /info command")
    bot.send_message(message.chat.id, config.COMMAND_INFO)
```

**Как работает функция**:
Функция `command_info` обрабатывает команду `/info`, отправленную пользователем.

1.  Записывает в лог информацию о том, что пользователь отправил команду `/info`.

2.  Отправляет пользователю информацию о боте, содержащуюся в переменной `config.COMMAND_INFO`.

**Параметры**:
- `message`: Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Возвращает**:
- Отсутствует.

### `command_time`
```python
@bot.message_handler(commands=['time'])
def command_time(message):
    logger.info(f"User {message.from_user.username} send /time command")
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    bot.send_message(message.chat.id, f"Current time: {current_time}")
```

**Как работает функция**:
Функция `command_time` обрабатывает команду `/time`, отправленную пользователем.

1.  Записывает в лог информацию о том, что пользователь отправил команду `/time`.

2.  Получает текущее время.

3.  Форматирует текущее время в строку.

4.  Отправляет пользователю сообщение с текущим временем.

**Параметры**:
- `message`: Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Возвращает**:
- Отсутствует.

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

**Как работает функция**:
Функция `command_photo` обрабатывает команду `/photo`, отправленную пользователем.

1.  Записывает в лог информацию о том, что пользователь отправил команду `/photo`.

2.  Пытается получить список файлов в директории, указанной в переменной `config.PHOTO_DIR`.

3.  Если список файлов не пуст, выбирает случайную фотографию из списка.

4.  Открывает файл фотографии и отправляет его пользователю.

5.  Если директория не найдена, отправляет пользователю сообщение об ошибке.

**Параметры**:
- `message`: Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Возвращает**:
- Отсутствует.

### `handle_voice_message`
```python
@bot.message_handler(content_types=['voice'])
def handle_voice_message(message):
    logger.info(f"User {message.from_user.username} send voice message")
    handler.handle_voice(bot, message)
```

**Как работает функция**:
Функция `handle_voice_message` обрабатывает голосовые сообщения, отправленные пользователем.

1.  Записывает в лог информацию о том, что пользователь отправил голосовое сообщение.

2.  Вызывает метод `handle_voice` объекта `handler` для обработки голосового сообщения.

**Параметры**:
- `message`: Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Возвращает**:
- Отсутствует.

### `handle_document_message`
```python
@bot.message_handler(content_types=['document'])
def handle_document_message(message):
    logger.info(f"User {message.from_user.username} send document message")
    handler.handle_document(bot, message)
```

**Как работает функция**:
Функция `handle_document_message` обрабатывает документы, отправленные пользователем.

1.  Записывает в лог информацию о том, что пользователь отправил документ.

2.  Вызывает метод `handle_document` объекта `handler` для обработки документа.

**Параметры**:
- `message`: Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Возвращает**:
- Отсутствует.

### `handle_text_message`
```python
@bot.message_handler(func=lambda message: message.text and not message.text.startswith('/'))
def handle_text_message(message):
    logger.info(f"User {message.from_user.username} sent message: {message.text}")
    handler.handle_message(bot, message )
```

**Как работает функция**:
Функция `handle_text_message` обрабатывает текстовые сообщения, отправленные пользователем, которые не начинаются с символа `/`.

1.  Записывает в лог информацию о том, что пользователь отправил текстовое сообщение.

2.  Вызывает метод `handle_message` объекта `handler` для обработки текстового сообщения.

**Параметры**:
- `message`: Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Возвращает**:
- Отсутствует.

### `handle_unknown_command`
```python
@bot.message_handler(func=lambda message: message.text and message.text.startswith('/'))
def handle_unknown_command(message):
    logger.info(f"User {message.from_user.username} send unknown command: {message.text}")
    bot.send_message(message.chat.id, config.UNKNOWN_COMMAND_MESSAGE)
```

**Как работает функция**:
Функция `handle_unknown_command` обрабатывает неизвестные команды, отправленные пользователем (сообщения, начинающиеся с символа `/`).

1.  Записывает в лог информацию о том, что пользователь отправил неизвестную команду.

2.  Отправляет пользователю сообщение о том, что команда неизвестна, содержащееся в переменной `config.UNKNOWN_COMMAND_MESSAGE`.

**Параметры**:
- `message`: Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Возвращает**:
- Отсутствует.
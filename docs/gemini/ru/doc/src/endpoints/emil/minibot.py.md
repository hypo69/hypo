# Модуль minibot
## Обзор

Модуль `minibot.py` представляет собой реализацию простого Telegram-бота, предназначенного для обслуживания запросов, связанных с сайтом emil-design.com. Он включает в себя обработку текстовых и голосовых сообщений, документов, а также поддерживает выполнение определенных команд. Бот использует Google Gemini для обработки текстовых запросов и предоставляет функциональность для работы с URL-адресами OneTab.

## Подробней

Этот модуль является частью проекта `hypotez` и расположен в директории `src/endpoints/emil`. Он взаимодействует с другими модулями проекта, такими как `src.logger`, `src.ai.gemini`, `src.endpoints.kazarinov.scenarios.scenario`, `src.utils.url`, и `src.utils.printer`.

Основная задача бота - предоставлять информацию и выполнять действия на основе запросов пользователей в Telegram. Бот может обрабатывать URL-адреса OneTab, выполнять сценарии, генерировать ответы на основе AI-модели Gemini и отправлять различные типы контента, такие как фотографии и PDF-файлы.

## Классы

### `BotHandler`

**Описание**: Обработчик команд, получаемых от Telegram-бота. Этот класс содержит методы для обработки различных типов сообщений и команд, а также для взаимодействия с AI-моделью и выполнения сценариев.

**Принцип работы**:
1.  При инициализации создается экземпляр класса `Scenario` и `GoogleGenerativeAI`.
2.  Метод `handle_message` определяет тип сообщения и вызывает соответствующий метод для его обработки.
3.  Методы `_handle_url`, `_handle_next_command`, `help_command`, `send_pdf`, `handle_voice`, и `handle_document` обрабатывают различные типы запросов и команд.

**Аттрибуты**:
- `base_dir` (Path): Базовая директория для хранения ресурсов, таких как схема user_flowchart.
- `scenario` (Scenario): Экземпляр класса `Scenario` для выполнения сценариев.
- `model` (GoogleGenerativeAI): Экземпляр класса `GoogleGenerativeAI` для взаимодействия с AI-моделью.
- `questions_list` (List[str]): Список вопросов, используемых при обработке команды `--next`.

**Методы**:
- `handle_message`: Обрабатывает входящие текстовые сообщения, определяя, является ли сообщение URL-адресом, командой или обычным текстом, и вызывает соответствующие обработчики.
- `_send_user_flowchart`: Отправляет пользователю схему user_flowchart.
- `_handle_url`: Обрабатывает URL-адреса, присланные пользователем, извлекая данные из OneTab и запуская сценарий.
- `_handle_next_command`: Обрабатывает команду '--next', генерируя случайный вопрос и отправляя его пользователю вместе с ответом от AI-модели.
- `help_command`: Отправляет пользователю список доступных команд.
- `send_pdf`: Отправляет пользователю PDF-файл.
- `handle_voice`: Обрабатывает голосовые сообщения, транскрибирует их и отправляет распознанный текст пользователю.
- `handle_document`: Обрабатывает полученные документы, сохраняет их во временной директории и отправляет пользователю сообщение с путем к файлу.
- `_transcribe_voice`: Заглушка для транскрибирования голосовых сообщений.

### `Config`

**Описание**: Класс, содержащий конфигурационные параметры для бота.

**Принцип работы**:
1.  При инициализации загружает значения параметров из переменных окружения или из базы данных с паролями.
2.  Предоставляет доступ к этим параметрам через атрибуты класса.

**Аттрибуты**:
- `BOT_TOKEN` (str): Токен Telegram-бота.
- `CHANNEL_ID` (str): ID канала Telegram.
- `PHOTO_DIR` (Path): Директория с фотографиями.
- `COMMAND_INFO` (str): Информация о боте.
- `UNKNOWN_COMMAND_MESSAGE` (str): Сообщение об неизвестной команде.
- `START_MESSAGE` (str): Приветственное сообщение при старте бота.
- `HELP_MESSAGE` (str): Сообщение со списком доступных команд.

## Функции

### `handle_message`

```python
def handle_message(self, bot:telebot, message:'message'):
    """Обработка текстовых сообщений."""
    ...
```

**Назначение**: Обрабатывает входящие текстовые сообщения от пользователя.

**Параметры**:
- `bot` (telebot): Экземпляр Telegram-бота.
- `message` (message): Объект сообщения от пользователя.

**Возвращает**: None

**Как работает функция**:

1.  Извлекает текст сообщения.
2.  Проверяет, является ли текст командой `?`, URL-адресом, командой для запроса следующего вопроса (`--next`, `-next`, `__next`, `-n`, `-q`) или обычным текстом.
3.  В зависимости от типа сообщения вызывает соответствующий обработчик:
    -   Если текст равен `?`, отправляет пользователю схему user\_flowchart.
    -   Если текст является URL-адресом, вызывает `_handle_url` для обработки URL.
    -   Если текст является командой для запроса следующего вопроса, вызывает `_handle_next_command`.
    -   В противном случае пытается получить ответ от AI-модели Gemini и отправляет его пользователю.
4.  Если в процессе взаимодействия с моделью возникает ошибка, логирует ее и отправляет пользователю сообщение об ошибке.

**ASCII flowchart**:

```
Начало
  ↓
Получение текста сообщения
  ↓
Проверка типа сообщения (команда, URL, текст)
  ├── Команда '?': Отправка схемы user_flowchart
  ├── URL: Вызов _handle_url
  ├── Команда '--next': Вызов _handle_next_command
  └── Текст:
      ↓
      Попытка взаимодействия с AI-моделью Gemini
      ├── Успех: Отправка ответа пользователю
      └── Ошибка: Логирование ошибки и отправка сообщения об ошибке пользователю
  ↓
Конец
```

**Примеры**:

```python
# Пример обработки текстового сообщения
# Представим, что у нас есть экземпляр бота и сообщение от пользователя
# bot = telebot.TeleBot("YOUR_BOT_TOKEN")
# message = telebot.types.Message(message_id=1, from_user=telebot.types.User(id=123, is_bot=False, first_name="Test", last_name="User", username="testuser", language_code="ru"), date=1672531200, chat=telebot.types.Chat(id=123, type="private"), content_type="text", options={"text": "Привет, бот!"})
# handler = BotHandler()
# handler.handle_message(bot, message)

# Пример обработки URL
# message = telebot.types.Message(message_id=2, from_user=telebot.types.User(id=123, is_bot=False, first_name="Test", last_name="User", username="testuser", language_code="ru"), date=1672531200, chat=telebot.types.Chat(id=123, type="private"), content_type="text", options={"text": "https://one-tab.com/XXXXXXXXX"})
# handler.handle_message(bot, message)

# Пример обработки команды "--next"
# message = telebot.types.Message(message_id=3, from_user=telebot.types.User(id=123, is_bot=False, first_name="Test", last_name="User", username="testuser", language_code="ru"), date=1672531200, chat=telebot.types.Chat(id=123, type="private"), content_type="text", options={"text": "--next"})
# handler.handle_message(bot, message)
```

### `_send_user_flowchart`

```python
def _send_user_flowchart(self, bot, chat_id):
    """Отправка схемы user_flowchart."""
    ...
```

**Назначение**: Отправляет пользователю фотографию, представляющую собой схему user\_flowchart.

**Параметры**:
- `bot` (telebot): Экземпляр Telegram-бота.
- `chat_id` (int): ID чата, куда нужно отправить фотографию.

**Возвращает**: None

**Как работает функция**:

1.  Формирует путь к файлу `user_flowchart.png`, который находится в директории `assets`.
2.  Пытается открыть файл фотографии в режиме чтения байтов.
3.  Отправляет фотографию пользователю.
4.  Если файл не найден, логирует ошибку и отправляет пользователю сообщение об ошибке.

**ASCII flowchart**:

```
Начало
  ↓
Формирование пути к файлу фотографии
  ↓
Попытка открытия файла
  ├── Успех: Отправка фотографии пользователю
  └── Ошибка (FileNotFoundError): Логирование ошибки и отправка сообщения об ошибке пользователю
  ↓
Конец
```

**Примеры**:

```python
# Пример отправки схемы user_flowchart
# Представим, что у нас есть экземпляр бота и chat_id пользователя
# bot = telebot.TeleBot("YOUR_BOT_TOKEN")
# chat_id = 123
# handler = BotHandler()
# handler._send_user_flowchart(bot, chat_id)
```

### `_handle_url`

```python
def _handle_url(self, bot, message:'message'):
    """Обработка URL, присланного пользователем."""
    ...
```

**Назначение**: Обрабатывает URL-адрес, предоставленный пользователем.

**Параметры**:
- `bot` (telebot): Экземпляр Telegram-бота.
- `message` (message): Объект сообщения от пользователя.

**Возвращает**: None

**Как работает функция**:

1.  Извлекает URL из текста сообщения.
2.  Проверяет, начинается ли URL с `https://one-tab.com` или `https://www.one-tab.com`. Если нет, отправляет пользователю сообщение об ошибке и завершает работу.
3.  Извлекает цену, название и список URL-адресов из OneTab, используя функцию `fetch_target_urls_onetab`.
4.  Отправляет пользователю сообщение с названием и ценой.
5.  Если не удалось получить список URL-адресов, отправляет пользователю сообщение об ошибке.
6.  Запускает асинхронный сценарий `run_scenario` с полученными данными.
7.  Если в процессе выполнения сценария возникает ошибка, логирует ее и отправляет пользователю сообщение об ошибке.

**ASCII flowchart**:

```
Начало
  ↓
Извлечение URL из сообщения
  ↓
Проверка URL на соответствие OneTab
  ├── Соответствует:
  │   ↓
  │   Извлечение данных из OneTab
  │   ├── Успех: Отправка сообщения пользователю с данными и запуск сценария run_scenario
  │   │   ├── Успех: Конец
  │   │   └── Ошибка: Логирование ошибки и отправка сообщения об ошибке пользователю
  │   └── Ошибка: Логирование ошибки и отправка сообщения об ошибке пользователю
  └── Не соответствует: Отправка сообщения об ошибке пользователю
  ↓
Конец
```

**Примеры**:

```python
# Пример обработки URL
# Представим, что у нас есть экземпляр бота и сообщение от пользователя с URL
# bot = telebot.TeleBot("YOUR_BOT_TOKEN")
# message = telebot.types.Message(message_id=2, from_user=telebot.types.User(id=123, is_bot=False, first_name="Test", last_name="User", username="testuser", language_code="ru"), date=1672531200, chat=telebot.types.Chat(id=123, type="private"), content_type="text", options={"text": "https://one-tab.com/XXXXXXXXX"})
# handler = BotHandler()
# handler._handle_url(bot, message)
```

### `_handle_next_command`

```python
def _handle_next_command(self, bot, message):
    """Обработка команды '--next' и её аналогов."""
    ...
```

**Назначение**: Обрабатывает команду '--next' и её аналоги, отправляя пользователю случайный вопрос из списка и ответ от AI-модели.

**Параметры**:
- `bot` (telebot): Экземпляр Telegram-бота.
- `message` (message): Объект сообщения от пользователя.

**Возвращает**: None

**Как работает функция**:

1.  Выбирает случайный вопрос из списка `self.questions_list`.
2.  Отправляет выбранный вопрос пользователю.
3.  Запрашивает ответ на вопрос у AI-модели Gemini.
4.  Отправляет полученный ответ пользователю.
5.  Если в процессе возникает ошибка, логирует ее и отправляет пользователю сообщение об ошибке.

**ASCII flowchart**:

```
Начало
  ↓
Выбор случайного вопроса из списка
  ↓
Отправка вопроса пользователю
  ↓
Запрос ответа у AI-модели Gemini
  ├── Успех: Отправка ответа пользователю
  └── Ошибка: Логирование ошибки и отправка сообщения об ошибке пользователю
  ↓
Конец
```

**Примеры**:

```python
# Пример обработки команды "--next"
# Представим, что у нас есть экземпляр бота и сообщение от пользователя с командой "--next"
# bot = telebot.TeleBot("YOUR_BOT_TOKEN")
# message = telebot.types.Message(message_id=3, from_user=telebot.types.User(id=123, is_bot=False, first_name="Test", last_name="User", username="testuser", language_code="ru"), date=1672531200, chat=telebot.types.Chat(id=123, type="private"), content_type="text", options={"text": "--next"})
# handler = BotHandler()
# handler._handle_next_command(bot, message)
```

### `help_command`

```python
def help_command(self, bot, message):
    """Обработка команды /help."""
    ...
```

**Назначение**: Обрабатывает команду `/help`, отправляя пользователю список доступных команд и их описание.

**Параметры**:
- `bot` (telebot): Экземпляр Telegram-бота.
- `message` (message): Объект сообщения от пользователя.

**Возвращает**: None

**Как работает функция**:

1.  Формирует строку с описанием доступных команд.
2.  Отправляет эту строку пользователю.

**ASCII flowchart**:

```
Начало
  ↓
Формирование строки со списком команд
  ↓
Отправка строки пользователю
  ↓
Конец
```

**Примеры**:

```python
# Пример обработки команды "/help"
# Представим, что у нас есть экземпляр бота и сообщение от пользователя с командой "/help"
# bot = telebot.TeleBot("YOUR_BOT_TOKEN")
# message = telebot.types.Message(message_id=4, from_user=telebot.types.User(id=123, is_bot=False, first_name="Test", last_name="User", username="testuser", language_code="ru"), date=1672531200, chat=telebot.types.Chat(id=123, type="private"), content_type="text", options={"text": "/help"})
# handler = BotHandler()
# handler.help_command(bot, message)
```

### `send_pdf`

```python
def send_pdf(self, bot, message, pdf_file):
    """Обработка команды /sendpdf для отправки PDF."""
    ...
```

**Назначение**: Обрабатывает команду `/sendpdf`, отправляя пользователю PDF-файл.

**Параметры**:
- `bot` (telebot): Экземпляр Telegram-бота.
- `message` (message): Объект сообщения от пользователя.
- `pdf_file` (str): Путь к PDF-файлу.

**Возвращает**: None

**Как работает функция**:

1.  Пытается открыть PDF-файл в режиме чтения байтов.
2.  Отправляет PDF-файл пользователю.
3.  Если в процессе возникает ошибка, логирует ее и отправляет пользователю сообщение об ошибке.

**ASCII flowchart**:

```
Начало
  ↓
Попытка открытия PDF-файла
  ├── Успех: Отправка PDF-файла пользователю
  └── Ошибка: Логирование ошибки и отправка сообщения об ошибке пользователю
  ↓
Конец
```

**Примеры**:

```python
# Пример обработки команды "/sendpdf"
# Представим, что у нас есть экземпляр бота и сообщение от пользователя с командой "/sendpdf"
# bot = telebot.TeleBot("YOUR_BOT_TOKEN")
# message = telebot.types.Message(message_id=5, from_user=telebot.types.User(id=123, is_bot=False, first_name="Test", last_name="User", username="testuser", language_code="ru"), date=1672531200, chat=telebot.types.Chat(id=123, type="private"), content_type="text", options={"text": "/sendpdf"})
# pdf_file = "example.pdf"
# handler = BotHandler()
# handler.send_pdf(bot, message, pdf_file)
```

### `handle_voice`

```python
def handle_voice(self, bot, message):
    """Обработка голосовых сообщений."""
    ...
```

**Назначение**: Обрабатывает голосовые сообщения, полученные от пользователя.

**Параметры**:
- `bot` (telebot): Экземпляр Telegram-бота.
- `message` (message): Объект сообщения от пользователя.

**Возвращает**: None

**Как работает функция**:

1.  Получает информацию о файле голосового сообщения.
2.  Скачивает файл голосового сообщения.
3.  Сохраняет файл во временной директории с расширением `.ogg`.
4.  Транскрибирует голосовое сообщение, используя метод `_transcribe_voice`.
5.  Отправляет распознанный текст пользователю.
6.  Если в процессе возникает ошибка, логирует ее и отправляет пользователю сообщение об ошибке.

**ASCII flowchart**:

```
Начало
  ↓
Получение информации о файле голосового сообщения
  ↓
Скачивание файла голосового сообщения
  ↓
Сохранение файла во временной директории
  ↓
Транскрибирование голосового сообщения
  ↓
Отправка распознанного текста пользователю
  ├── Успех: Конец
  └── Ошибка: Логирование ошибки и отправка сообщения об ошибке пользователю
```

**Примеры**:

```python
# Пример обработки голосового сообщения
# Представим, что у нас есть экземпляр бота и сообщение от пользователя с голосовым сообщением
# bot = telebot.TeleBot("YOUR_BOT_TOKEN")
# message = telebot.types.Message(message_id=6, from_user=telebot.types.User(id=123, is_bot=False, first_name="Test", last_name="User", username="testuser", language_code="ru"), date=1672531200, chat=telebot.types.Chat(id=123, type="private"), content_type="voice", options={"voice": telebot.types.Voice(file_id="voice_file_id", duration=5, mime_type="audio/ogg", file_size=1024)})
# handler = BotHandler()
# handler.handle_voice(bot, message)
```

### `_transcribe_voice`

```python
def _transcribe_voice(self, file_path):
    """Транскрибирование голосового сообщения (заглушка)."""
    ...
```

**Назначение**: Транскрибирует голосовое сообщение, преобразуя его в текст. В текущей реализации является заглушкой и всегда возвращает сообщение о том, что распознавание голоса еще не реализовано.

**Параметры**:
- `file_path` (str): Путь к файлу голосового сообщения.

**Возвращает**: str

**Как работает функция**:

1.  Возвращает строку "Распознавание голоса ещё не реализовано.".

**ASCII flowchart**:

```
Начало
  ↓
Возврат строки "Распознавание голоса ещё не реализовано."
  ↓
Конец
```

**Примеры**:

```python
# Пример транскрибирования голосового сообщения
# file_path = "voice_message.ogg"
# handler = BotHandler()
# transcribed_text = handler._transcribe_voice(file_path)
# print(transcribed_text)  # Вывод: Распознавание голоса ещё не реализовано.
```

### `handle_document`

```python
def handle_document(self, bot, message):
    """Обработка полученных документов."""
    ...
```

**Назначение**: Обрабатывает документы, полученные от пользователя.

**Параметры**:
- `bot` (telebot): Экземпляр Telegram-бота.
- `message` (message): Объект сообщения от пользователя.

**Возвращает**: bool

**Как работает функция**:

1.  Получает информацию о файле документа.
2.  Скачивает файл документа.
3.  Сохраняет файл во временной директории с оригинальным именем файла.
4.  Отправляет пользователю сообщение с путем к сохраненному файлу.
5.  Если в процессе возникает ошибка, логирует ее и отправляет пользователю сообщение об ошибке.

**ASCII flowchart**:

```
Начало
  ↓
Получение информации о файле документа
  ↓
Скачивание файла документа
  ↓
Сохранение файла во временной директории
  ↓
Отправка сообщения пользователю с путем к файлу
  ├── Успех: Возврат True
  └── Ошибка: Логирование ошибки и отправка сообщения об ошибке пользователю, возврат False
  ↓
Конец
```

**Примеры**:

```python
# Пример обработки документа
# Представим, что у нас есть экземпляр бота и сообщение от пользователя с документом
# bot = telebot.TeleBot("YOUR_BOT_TOKEN")
# message = telebot.types.Message(message_id=7, from_user=telebot.types.User(id=123, is_bot=False, first_name="Test", last_name="User", username="testuser", language_code="ru"), date=1672531200, chat=telebot.types.Chat(id=123, type="private"), content_type="document", options={"document": telebot.types.Document(file_name="example.txt", mime_type="text/plain", file_id="document_file_id", file_size=1024)})
# handler = BotHandler()
# result = handler.handle_document(bot, message)
# print(result)
```

### `command_start`

```python
@bot.message_handler(commands=['start'])
def command_start(message):
    ...
```

**Назначение**: Обрабатывает команду `/start`, отправляя пользователю приветственное сообщение.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от пользователя.

**Возвращает**: None

**Как работает функция**:

1.  Логирует информацию об использовании команды `/start` пользователем.
2.  Отправляет пользователю приветственное сообщение из конфигурации (`config.START_MESSAGE`).

**ASCII flowchart**:

```
Начало
  ↓
Логирование информации о команде
  ↓
Отправка приветственного сообщения пользователю
  ↓
Конец
```

**Примеры**:

```python
# Пример вызова функции при получении команды /start
# bot = telebot.TeleBot("YOUR_BOT_TOKEN")
# message = telebot.types.Message(message_id=1, from_user=telebot.types.User(id=123, is_bot=False, first_name="Test", last_name="User", username="testuser", language_code="ru"), date=1672531200, chat=telebot.types.Chat(id=123, type="private"), content_type="text", options={"text": "/start"})
# command_start(message)
```

### `command_help`

```python
@bot.message_handler(commands=['help'])
def command_help(message):
    ...
```

**Назначение**: Обрабатывает команду `/help`, вызывая метод `help_command` объекта `handler` для отправки пользователю списка доступных команд.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от пользователя.

**Возвращает**: None

**Как работает функция**:

1.  Логирует информацию об использовании команды `/help` пользователем.
2.  Вызывает метод `help_command` объекта `handler`, передавая ему объект бота и объект сообщения.

**ASCII flowchart**:

```
Начало
  ↓
Логирование информации о команде
  ↓
Вызов handler.help_command(bot, message)
  ↓
Конец
```

**Примеры**:

```python
# Пример вызова функции при получении команды /help
# bot = telebot.TeleBot("YOUR_BOT_TOKEN")
# message = telebot.types.Message(message_id=2, from_user=telebot.types.User(id=123, is_bot=False, first_name="Test", last_name="User", username="testuser", language_code="ru"), date=1672531200, chat=telebot.types.Chat(id=123, type="private"), content_type="text", options={"text": "/help"})
# command_help(message)
```

### `command_info`

```python
@bot.message_handler(commands=['info'])
def command_info(message):
    ...
```

**Назначение**: Обрабатывает команду `/info`, отправляя пользователю информацию о боте.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от пользователя.

**Возвращает**: None

**Как работает функция**:

1.  Логирует информацию об использовании команды `/info` пользователем.
2.  Отправляет пользователю информацию о боте из конфигурации (`config.COMMAND_INFO`).

**ASCII flowchart**:

```
Начало
  ↓
Логирование информации о команде
  ↓
Отправка информации о боте пользователю
  ↓
Конец
```

**Примеры**:

```python
# Пример вызова функции при получении команды /info
# bot = telebot.TeleBot("YOUR_BOT_TOKEN")
# message = telebot.types.Message(message_id=3, from_user=telebot.types.User(id=123, is_bot=False, first_name="Test", last_name="User", username="testuser", language_code="ru"), date=1672531200, chat=telebot.types.Chat(id=123, type="private"), content_type="text", options={"text": "/info"})
# command_info(message)
```

### `command_time`

```python
@bot.message_handler(commands=['time'])
def command_time(message):
    ...
```

**Назначение**: Обрабатывает команду `/time`, отправляя пользователю текущее время.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от пользователя.

**Возвращает**: None

**Как работает функция**:

1.  Логирует информацию об использовании команды `/time` пользователем.
2.  Получает текущее время.
3.  Форматирует время в строку `HH:MM:SS`.
4.  Отправляет пользователю сообщение с текущим временем.

**ASCII flowchart**:

```
Начало
  ↓
Логирование информации о команде
  ↓
Получение текущего времени
  ↓
Форматирование времени
  ↓
Отправка времени пользователю
  ↓
Конец
```

**Примеры**:

```python
# Пример вызова функции при получении команды /time
# bot = telebot.TeleBot("YOUR_BOT_TOKEN")
# message = telebot.types.Message(message_id=4, from_user=telebot.types.User(id=123, is_bot=False, first_name="Test", last_name="User", username="testuser", language_code="ru"), date=1672531200, chat=telebot.types.Chat(id=123, type="private"), content_type="text", options={"text": "/time"})
# command_time(message)
```

### `command_photo`

```python
@bot.message_handler(commands=['photo'])
def command_photo(message):
    ...
```

**Назначение**: Обрабатывает команду `/photo`, отправляя пользователю случайную фотографию из указанной директории.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от пользователя.

**Возвращает**: None

**Как работает функция**:

1.  Логирует информацию об использовании команды `/photo` пользователем.
2.  Пытается получить список файлов в директории с фотографиями (`config.PHOTO_DIR`).
3.  Если в директории есть файлы, выбирает случайный файл.
4.  Открывает файл фотографии в режиме чтения байтов.
5.  Отправляет фотографию пользователю.
6.  Если директория не найдена или в ней нет фотографий, отправляет пользователю сообщение об ошибке.

**ASCII flowchart**:

```
Начало
  ↓
Логирование информации о команде
  ↓
Попытка получения списка файлов в директории
  ├── Успех:
  │   ↓
  │   Проверка наличия файлов
  │   ├── Файлы есть:
  │   │   ↓
  │   │   Выбор случайного файла
  │   │   ↓
  │   │   Открытие файла фотографии
  │   │   ↓
  │   │   Отправка фотографии пользователю
  │   └── Файлов нет: Отправка сообщения об отсутствии фотографий
  └── Ошибка (FileNotFoundError): Отправка сообщения о ненайденной директории
  ↓
Конец
```

**Примеры**:

```python
# Пример вызова функции при получении команды /photo
# bot = telebot.TeleBot("YOUR_BOT_TOKEN")
# message = telebot.types.Message(message_id=5, from_user=telebot.types.User(id=123, is_bot=False, first_name="Test", last_name="User", username="testuser", language_code="ru"), date=1672531200, chat=telebot.types.Chat(id=123, type="private"), content_type="text", options={"text": "/photo"})
# command_photo(message)
```

### `handle_voice_message`

```python
@bot.message_handler(content_types=['voice'])
def handle_voice_message(message):
    ...
```

**Назначение**: Обрабатывает голосовые сообщения, полученные от пользователя.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от пользователя.

**Возвращает**: None

**Как работает функция**:

1.  Логирует информацию об отправке голосового сообщения пользователем.
2.  Вызывает метод `handle_voice` объекта `handler`, передавая ему объект бота и объект сообщения.

**ASCII flowchart**:

```
Начало
  ↓
Логирование информации о голосовом сообщении
  ↓
Вызов handler.handle_voice(bot, message)
  ↓
Конец
```

**Примеры**:

```python
# Пример вызова функции при получении голосового сообщения
# bot = telebot.TeleBot("YOUR_BOT_TOKEN")
# message = telebot.types.Message(message_id=6, from_user=telebot.types.User(id=123, is_bot=False, first_name="Test", last_name="User", username="testuser", language_code="ru"), date=1672531200, chat=telebot.types.Chat(id=123, type="private"), content_type="voice", options={"voice": telebot.types.Voice(file_id="voice_file_id", duration=5, mime_type="audio/ogg", file_size=1024)})
# handle_voice_message(message)
```

### `handle_document_message`

```python
@bot.message_handler(content_types=['document'])
def handle_document_message(message):
    ...
```

**Назначение**: Обрабатывает сообщения с документами, полученные от пользователя.

**Параметры**:
- `message` (telebot.types.Message): Объект сообщения от пользователя.

**Возвращает**: None

**Как работает функция**:

1.  Логирует информацию об отправке документа пользователем.
2.  Вызывает метод `handle_document` объекта `handler`, передавая ему объект бота и объект сообщения.

**ASCII flowchart**:

```
Начало
  ↓
Логирование информации о документе
  ↓
Вызов handler.handle_document(bot, message)
  ↓
Конец
```

**Примеры**:

```python
# Пример вызова функции при получении сообщения с документом
# bot = telebot.TeleBot("YOUR_BOT_TOKEN")
# message = telebot.types.Message(message_id=7, from_user=telebot.types.User(id=123, is_bot=False, first_name="Test", last_name="User", username="testuser", language_code="ru"), date=1672531200, chat=telebot.types.Chat(id=123, type="private"), content_type="document", options={"document": telebot.types
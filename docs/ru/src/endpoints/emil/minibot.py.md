# Модуль `minibot.py`

## Обзор

Модуль представляет собой простой Telegram-бот, предназначенный для обслуживания запросов, связанных с сайтом emil-design.com. Он включает в себя обработку текстовых сообщений, URL-адресов, голосовых сообщений и документов, а также поддерживает интеграцию с AI-моделями для генерации ответов на вопросы пользователей.

## Подробнее

Модуль предоставляет класс `BotHandler` для обработки различных типов сообщений и команд, получаемых от пользователей через Telegram. Он использует библиотеку `telebot` для взаимодействия с Telegram API и включает функции для обработки URL-адресов, выполнения сценариев, отправки фотографий и документов, а также распознавания голосовых сообщений. Модуль также содержит класс `Config`, который определяет настройки бота, такие как токен, идентификатор канала и пути к файлам.

## Содержание

1.  [Классы](#Классы)
    *   [BotHandler](#BotHandler)
    *   [Config](#Config)
2.  [Функции](#Функции)
    *   [command_start](#command_start)
    *   [command_help](#command_help)
    *   [command_info](#command_info)
    *   [command_time](#command_time)
    *   [command_photo](#command_photo)
    *   [handle_voice_message](#handle_voice_message)
    *   [handle_document_message](#handle_document_message)
    *   [handle_text_message](#handle_text_message)
    *   [handle_unknown_command](#handle_unknown_command)

## Классы

### `BotHandler`

**Описание**: Класс предназначен для обработки команд, получаемых от Telegram-бота.

**Принцип работы**:
Класс инициализируется с использованием сценария, модели генеративного ИИ и списка вопросов. Он предоставляет методы для обработки различных типов сообщений, отправки схем, обработки URL-адресов и выполнения других команд.

**Атрибуты**:

*   `base_dir` (Path): Базовая директория для хранения ресурсов, используемых ботом.
*   `scenario` (Scenario): Экземпляр класса `Scenario` для выполнения сценариев.
*   `model` (GoogleGenerativeAI): Экземпляр класса `GoogleGenerativeAI` для взаимодействия с AI-моделью.
*   `questions_list` (List[str]): Список вопросов, используемых для обработки команды `--next`.

**Методы**:

*   `__init__`: Инициализация обработчика событий телеграм-бота.
*   `handle_message`: Обработка текстовых сообщений.
*   `_send_user_flowchart`: Отправка схемы user\_flowchart.
*   `_handle_url`: Обработка URL, присланного пользователем.
*   `_handle_next_command`: Обработка команды '--next' и её аналогов.
*   `help_command`: Обработка команды /help.
*   `send_pdf`: Обработка команды /sendpdf для отправки PDF.
*   `handle_voice`: Обработка голосовых сообщений.
*   `_transcribe_voice`: Транскрибирование голосового сообщения (заглушка).
*   `handle_document`: Обработка полученных документов.

#### `__init__`

```python
def __init__(self):
    """Инициализация обработчика событий телеграм-бота."""
    ...
```

**Назначение**: Инициализирует экземпляр класса `BotHandler`.

**Как работает функция**:

1.  Инициализируется объект `scenario` класса `Scenario`.
2.  Инициализируется объект `model` класса `GoogleGenerativeAI` с использованием API-ключа Gemini, полученного из переменной окружения `GEMINI_API`.
3.  Создается список `questions_list`, содержащий вопросы, которые могут быть использованы ботом.

```
Инициализация scenario --> Инициализация model --> Создание questions_list
```

#### `handle_message`

```python
def handle_message(self, bot:telebot, message:'message'):
    """Обработка текстовых сообщений."""
    ...
```

**Назначение**: Обрабатывает текстовые сообщения, полученные от пользователя.

**Параметры**:

*   `bot` (telebot): Экземпляр Telegram-бота.
*   `message` (message): Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Как работает функция**:

1.  Извлекает текст сообщения из объекта `message`.
2.  Проверяет, является ли текст команды `?`. Если да, отправляет пользователю схему `user_flowchart`.
3.  Проверяет, является ли текст URL-адресом. Если да, обрабатывает URL-адрес с помощью метода `_handle_url`.
4.  Проверяет, является ли текст одной из команд для запроса следующего вопроса (`--next`, `-next`, `__next`, `-n`, `-q`). Если да, обрабатывает команду с помощью метода `_handle_next_command`.
5.  Если текст не является командой или URL-адресом, пытается использовать AI-модель для генерации ответа на сообщение.
6.  В случае ошибки при взаимодействии с моделью, логирует ошибку и отправляет пользователю сообщение об ошибке.

```
Извлечение текста --> Проверка команды "?" --> Проверка URL --> Проверка команды "--next" --> Взаимодействие с AI-моделью
                                    |
                                    V
                                 Отправка user_flowchart
```

**Примеры**:

```python
# Пример обработки текстового сообщения
bot_handler = BotHandler()
#Предположим, что bot - это экземпляр telebot.TeleBot, а message - это экземпляр telebot.types.Message
bot_handler.handle_message(bot, message)
```

#### `_send_user_flowchart`

```python
def _send_user_flowchart(self, bot, chat_id):
    """Отправка схемы user_flowchart."""
    ...
```

**Назначение**: Отправляет пользователю схему `user_flowchart` в виде фотографии.

**Параметры**:

*   `bot` (telebot): Экземпляр Telegram-бота.
*   `chat_id` (int): Идентификатор чата пользователя.

**Как работает функция**:

1.  Определяет путь к файлу `user_flowchart.png`.
2.  Пытается открыть файл фотографии и отправить его пользователю.
3.  В случае, если файл не найден, логирует ошибку и отправляет пользователю сообщение о том, что схема не найдена.

```
Определение пути к файлу --> Открытие файла --> Отправка фотографии
                                        |
                                        V
                                     Обработка FileNotFoundError
```

#### `_handle_url`

```python
def _handle_url(self, bot, message:'message'):
    """Обработка URL, присланного пользователем."""
    ...
```

**Назначение**: Обрабатывает URL-адрес, отправленный пользователем.

**Параметры**:

*   `bot` (telebot): Экземпляр Telegram-бота.
*   `message` (message): Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Как работает функция**:

1.  Извлекает URL-адрес из объекта `message`.
2.  Проверяет, является ли URL-адрес ссылкой на `one-tab.com`. Если нет, отправляет пользователю сообщение об ошибке.
3.  Парсит страницу `one-tab.com` для извлечения цены, названия товара и списка URL-адресов комплектующих.
4.  В случае ошибки при получении данных из OneTab, логирует ошибку и отправляет пользователю сообщение об ошибке.
5.  Проверяет, был ли получен список URL-адресов. Если нет, отправляет пользователю сообщение об ошибке.
6.  Выполняет сценарий обработки полученных данных с помощью метода `run_scenario` объекта `scenario`.
7.  В случае ошибки при выполнении сценария, логирует ошибку и отправляет пользователю сообщение об ошибке.

```
Извлечение URL --> Проверка URL на one-tab.com --> Парсинг страницы one-tab.com --> Выполнение сценария
                        |
                        V
                     Отправка сообщения об ошибке
```

#### `_handle_next_command`

```python
def _handle_next_command(self, bot, message):
    """Обработка команды '--next' и её аналогов."""
    ...
```

**Назначение**: Обрабатывает команду `--next` и её аналоги, отправляя пользователю случайный вопрос из списка и ответ на него.

**Параметры**:

*   `bot` (telebot): Экземпляр Telegram-бота.
*   `message` (message): Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Как работает функция**:

1.  Выбирает случайный вопрос из списка `questions_list`.
2.  Использует AI-модель для получения ответа на выбранный вопрос.
3.  Отправляет пользователю выбранный вопрос и ответ на него.
4.  В случае ошибки при чтении вопросов, логирует ошибку и отправляет пользователю сообщение об ошибке.

```
Выбор случайного вопроса --> Получение ответа от AI-модели --> Отправка вопроса и ответа
                                                                |
                                                                V
                                                             Обработка ошибки
```

#### `help_command`

```python
def help_command(self, bot, message):
    """Обработка команды /help."""
    ...
```

**Назначение**: Обрабатывает команду `/help`, отправляя пользователю список доступных команд.

**Параметры**:

*   `bot` (telebot): Экземпляр Telegram-бота.
*   `message` (message): Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Как работает функция**:

Отправляет пользователю сообщение со списком доступных команд бота.

```
Отправка списка команд
```

#### `send_pdf`

```python
def send_pdf(self, bot, message, pdf_file):
    """Обработка команды /sendpdf для отправки PDF."""
    ...
```

**Назначение**: Обрабатывает команду `/sendpdf`, отправляя пользователю PDF-файл.

**Параметры**:

*   `bot` (telebot): Экземпляр Telegram-бота.
*   `message` (message): Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.
*   `pdf_file` (str): Путь к PDF-файлу, который необходимо отправить.

**Как работает функция**:

1.  Пытается открыть PDF-файл и отправить его пользователю в виде документа.
2.  В случае ошибки при отправке файла, логирует ошибку и отправляет пользователю сообщение об ошибке.

```
Открытие PDF-файла --> Отправка PDF-файла пользователю
                                        |
                                        V
                                     Обработка ошибки
```

#### `handle_voice`

```python
def handle_voice(self, bot, message):
    """Обработка голосовых сообщений."""
    ...
```

**Назначение**: Обрабатывает голосовые сообщения, полученные от пользователя.

**Параметры**:

*   `bot` (telebot): Экземпляр Telegram-бота.
*   `message` (message): Объект сообщения, содержащий информацию о голосовом сообщении, отправленном пользователем.

**Как работает функция**:

1.  Получает информацию о файле голосового сообщения.
2.  Скачивает файл голосового сообщения.
3.  Сохраняет файл голосового сообщения во временную директорию.
4.  Транскрибирует голосовое сообщение с помощью метода `_transcribe_voice`.
5.  Отправляет пользователю распознанный текст.
6.  В случае ошибки при обработке голосового сообщения, логирует ошибку и отправляет пользователю сообщение об ошибке.

```
Получение информации о файле --> Скачивание файла --> Сохранение файла --> Транскрибирование --> Отправка текста
                                                                                            |
                                                                                            V
                                                                                         Обработка ошибки
```

#### `_transcribe_voice`

```python
def _transcribe_voice(self, file_path):
    """Транскрибирование голосового сообщения (заглушка)."""
    ...
```

**Назначение**: Транскрибирует голосовое сообщение (заглушка, функция не реализована).

**Параметры**:

*   `file_path` (str): Путь к файлу голосового сообщения.

**Как работает функция**:

Возвращает строку "Распознавание голоса ещё не реализовано.", так как функция транскрибирования не реализована.

```
Возврат сообщения о нереализованной функции
```

#### `handle_document`

```python
def handle_document(self, bot, message):
    """Обработка полученных документов."""
    ...
```

**Назначение**: Обрабатывает полученные документы, сохраняя их во временную директорию.

**Параметры**:

*   `bot` (telebot): Экземпляр Telegram-бота.
*   `message` (message): Объект сообщения, содержащий информацию о документе, отправленном пользователем.

**Как работает функция**:

1.  Получает информацию о файле документа.
2.  Скачивает файл документа.
3.  Сохраняет файл документа во временную директорию.
4.  Отправляет пользователю сообщение о том, что файл был сохранен.
5.  В случае ошибки при обработке документа, логирует ошибку и отправляет пользователю сообщение об ошибке.

```
Получение информации о файле --> Скачивание файла --> Сохранение файла --> Отправка сообщения об успехе
                                                                                            |
                                                                                            V
                                                                                         Обработка ошибки
```

### `Config`

**Описание**: Класс предназначен для хранения конфигурационных параметров бота.

**Принцип работы**:
Класс определяет различные параметры, такие как токен бота, идентификатор канала, пути к директориям и сообщения, используемые ботом.

**Атрибуты**:

*   `BOT_TOKEN` (str): Токен Telegram-бота, полученный из переменной окружения `TELEGRAM_BOT_TOKEN` или из базы данных с учетными данными.
*   `CHANNEL_ID` (str): Идентификатор канала Telegram.
*   `PHOTO_DIR` (Path): Путь к директории с фотографиями.
*   `COMMAND_INFO` (str): Информация о боте, отображаемая по команде `/info`.
*   `UNKNOWN_COMMAND_MESSAGE` (str): Сообщение, отображаемое при вводе неизвестной команды.
*   `START_MESSAGE` (str): Сообщение, отображаемое при запуске бота.
*   `HELP_MESSAGE` (str): Сообщение, содержащее список доступных команд и их описание.

## Функции

### `command_start`

```python
@bot.message_handler(commands=['start'])
def command_start(message):
    """Обработка команды /start."""
    ...
```

**Назначение**: Обрабатывает команду `/start`, отправляя пользователю приветственное сообщение.

**Параметры**:

*   `message` (telebot.types.Message): Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Как работает функция**:

1.  Логирует информацию об использовании команды `/start` пользователем.
2.  Отправляет пользователю приветственное сообщение, определенное в конфигурации бота.

```
Логирование использования команды --> Отправка приветственного сообщения
```

**Примеры**:

```python
# Пример обработки команды /start
# Предположим, что bot - это экземпляр telebot.TeleBot, а message - это экземпляр telebot.types.Message
command_start(message)
```

### `command_help`

```python
@bot.message_handler(commands=['help'])
def command_help(message):
    """Обработка команды /help."""
    ...
```

**Назначение**: Обрабатывает команду `/help`, вызывая метод `help_command` объекта `handler` для отправки пользователю списка доступных команд.

**Параметры**:

*   `message` (telebot.types.Message): Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Как работает функция**:

1.  Логирует информацию об использовании команды `/help` пользователем.
2.  Вызывает метод `help_command` объекта `handler` для отправки пользователю списка доступных команд.

```
Логирование использования команды --> Вызов метода help_command
```

**Примеры**:

```python
# Пример обработки команды /help
# Предположим, что bot - это экземпляр telebot.TeleBot, а message - это экземпляр telebot.types.Message
command_help(message)
```

### `command_info`

```python
@bot.message_handler(commands=['info'])
def command_info(message):
    """Обработка команды /info."""
    ...
```

**Назначение**: Обрабатывает команду `/info`, отправляя пользователю информацию о боте.

**Параметры**:

*   `message` (telebot.types.Message): Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Как работает функция**:

1.  Логирует информацию об использовании команды `/info` пользователем.
2.  Отправляет пользователю информацию о боте, определенную в конфигурации бота.

```
Логирование использования команды --> Отправка информации о боте
```

**Примеры**:

```python
# Пример обработки команды /info
# Предположим, что bot - это экземпляр telebot.TeleBot, а message - это экземпляр telebot.types.Message
command_info(message)
```

### `command_time`

```python
@bot.message_handler(commands=['time'])
def command_time(message):
    """Обработка команды /time."""
    ...
```

**Назначение**: Обрабатывает команду `/time`, отправляя пользователю текущее время.

**Параметры**:

*   `message` (telebot.types.Message): Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Как работает функция**:

1.  Логирует информацию об использовании команды `/time` пользователем.
2.  Получает текущее время.
3.  Форматирует текущее время в строку.
4.  Отправляет пользователю текущее время.

```
Логирование использования команды --> Получение текущего времени --> Форматирование времени --> Отправка времени
```

**Примеры**:

```python
# Пример обработки команды /time
# Предположим, что bot - это экземпляр telebot.TeleBot, а message - это экземпляр telebot.types.Message
command_time(message)
```

### `command_photo`

```python
@bot.message_handler(commands=['photo'])
def command_photo(message):
    """Обработка команды /photo."""
    ...
```

**Назначение**: Обрабатывает команду `/photo`, отправляя пользователю случайную фотографию из директории.

**Параметры**:

*   `message` (telebot.types.Message): Объект сообщения, содержащий информацию о сообщении, отправленном пользователем.

**Как работает функция**:

1.  Логирует информацию об использовании команды `/photo` пользователем.
2.  Пытается получить список файлов в директории с фотографиями, определенной в конфигурации бота.
3.  Если список файлов не пуст, выбирает случайную фотографию из списка и отправляет ее пользователю.
4.  Если список файлов пуст, отправляет пользователю сообщение о том, что в директории нет фотографий.
5.  В случае, если директория не найдена, отправляет пользователю сообщение о том, что директория не найдена.

```
Логирование использования команды --> Получение списка файлов --> Выбор случайной фотографии --> Отправка фотографии
                                          |
                                          V
                                       Обработка FileNotFoundError
```

**Примеры**:

```python
# Пример обработки команды /photo
# Предположим, что bot - это экземпляр telebot.TeleBot, а message - это экземпляр telebot.types.Message
command_photo(message)
```

### `handle_voice_message`

```python
@bot.message_handler(content_types=['voice'])
def handle_voice_message(message):
    """Обработка голосовых сообщений."""
    ...
```

**Назначение**: Обрабатывает голосовые сообщения, вызывая метод `handle_voice` объекта `handler` для обработки голосового сообщения.

**Параметры**:

*   `message` (telebot.types.Message): Объект сообщения, содержащий информацию о голосовом сообщении, отправленном пользователем.

**Как работает функция**:

1.  Логирует информацию об отправке голосового сообщения пользователем.
2.  Вызывает метод `handle_voice` объекта `handler` для обработки голосового сообщения.

```
Логирование отправки голосового сообщения --> Вызов метода handle_voice
```

**Примеры**:

```python
# Пример обработки голосового сообщения
# Предположим, что bot - это экземпляр telebot.TeleBot, а message - это экземпляр telebot.types.Message
handle_voice_message(message)
```

### `handle_document_message`

```python
@bot.message_handler(content_types=['document'])
def handle_document_message(message):
    """Обработка полученных документов."""
    ...
```

**Назначение**: Обрабатывает полученные документы, вызывая метод `handle_document` объекта `handler` для обработки документа.

**Параметры**:

*   `message` (telebot.types.Message): Объект сообщения, содержащий информацию о документе, отправленном пользователем.

**Как работает функция**:

1.  Логирует информацию об отправке документа пользователем.
2.  Вызывает метод `handle_document` объекта `handler` для обработки документа.

```
Логирование отправки документа --> Вызов метода handle_document
```

**Примеры**:

```python
# Пример обработки документа
# Предположим, что bot - это экземпляр telebot.TeleBot, а message - это экземпляр telebot.types.Message
handle_document_message(message)
```

### `handle_text_message`

```python
@bot.message_handler(func=lambda message: message.text and not message.text.startswith('/'))
def handle_text_message(message):
    """Обработка текстовых сообщений."""
    ...
```

**Назначение**: Обрабатывает текстовые сообщения, не начинающиеся с символа `/`, вызывая метод `handle_message` объекта `handler` для обработки сообщения.

**Параметры**:

*   `message` (telebot.types.Message): Объект сообщения, содержащий информацию о текстовом сообщении, отправленном пользователем.

**Как работает функция**:

1.  Логирует информацию об отправке текстового сообщения пользователем.
2.  Вызывает метод `handle_message` объекта `handler` для обработки сообщения.

```
Логирование отправки текстового сообщения --> Вызов метода handle_message
```

**Примеры**:

```python
# Пример обработки текстового сообщения
# Предположим, что bot - это экземпляр telebot.TeleBot, а message - это экземпляр telebot.types.Message
handle_text_message(message)
```

### `handle_unknown_command`

```python
@bot.message_handler(func=lambda message: message.text and message.text.startswith('/'))
def handle_unknown_command(message):
    """Обработка неизвестных команд."""
    ...
```

**Назначение**: Обрабатывает неизвестные команды, начинающиеся с символа `/`, отправляя пользователю сообщение о неизвестной команде.

**Параметры**:

*   `message` (telebot.types.Message): Объект сообщения, содержащий информацию о неизвестной команде, отправленной пользователем.

**Как работает функция**:

1.  Логирует информацию об отправке неизвестной команды пользователем.
2.  Отправляет пользователю сообщение о неизвестной команде, определенное в конфигурации бота.

```
Логирование отправки неизвестной команды --> Отправка сообщения о неизвестной команде
```

**Примеры**:

```python
# Пример обработки неизвестной команды
# Предположим, что bot - это экземпляр telebot.TeleBot, а message - это экземпляр telebot.types.Message
handle_unknown_command(message)
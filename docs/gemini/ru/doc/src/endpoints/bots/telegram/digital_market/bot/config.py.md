# Модуль конфигурации Telegram-бота для цифрового рынка
========================================================

Модуль содержит настройки для Telegram-бота цифрового рынка, включая параметры подключения к Telegram API, администраторов, URL сайта, параметры базы данных и прочие необходимые конфигурации.

## Обзор

Этот модуль предназначен для централизованного хранения и управления конфигурационными параметрами, необходимыми для работы Telegram-бота. Он использует `pydantic_settings` для загрузки настроек из переменных окружения и обеспечивает удобный доступ к ним через класс `Settings`.

## Подробнее

Модуль определяет класс `Settings`, который наследуется от `BaseSettings` из библиотеки `pydantic_settings`. Это позволяет автоматически загружать значения настроек из переменных окружения, указанных в файле `.env`. Также модуль инициализирует объекты `Bot` и `Dispatcher` из библиотеки `aiogram`, необходимые для работы с Telegram API.

## Классы

### `Settings`

**Описание**: Класс, представляющий настройки приложения, загружаемые из переменных окружения.

**Наследует**: `BaseSettings` (из `pydantic_settings`).

**Атрибуты**:
- `BOT_TOKEN` (str): Токен Telegram-бота, полученный от BotFather.
- `ADMIN_IDS` (List[int]): Список ID администраторов бота.
- `PROVIDER_TOKEN` (str): Токен провайдера платежей (например, Robokassa).
- `FORMAT_LOG` (str): Формат записи логов (по умолчанию: "{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}").
- `LOG_ROTATION` (str): Размер ротации логов (по умолчанию: "10 MB").
- `DB_URL` (str): URL для подключения к базе данных (по умолчанию: 'sqlite+aiosqlite:///data/db.sqlite3').
- `SITE_URL` (str): URL сайта, на котором размещен бот.
- `SITE_HOST` (str): Хост сайта.
- `SITE_PORT` (int): Порт сайта.
- `MRH_LOGIN` (str): Логин для MRH (предположительно, Merchant ID в Robokassa).
- `MRH_PASS_1` (str): Первый пароль для MRH (предположительно, пароль Robokassa).
- `MRH_PASS_2` (str): Второй пароль для MRH (предположительно, пароль Robokassa).
- `IN_TEST` (int): Флаг, указывающий на тестовый режим (1 - тестовый, 0 - продакшн).
- `model_config` (SettingsConfigDict): Конфигурация для `pydantic_settings`, указывающая на файл `.env`.

**Методы**:
- `get_webhook_url`(): Формирует URL для вебхука на основе токена и URL сайта.
- `get_provider_hook_url`(): Формирует URL для вебхука провайдера платежей (Robokassa).

```python
    @property
    def get_webhook_url(self) -> str:
        """Динамически формирует путь для вебхука на основе токена и URL сайта."""
        return f"{self.SITE_URL}/{self.BOT_TOKEN}"
```
     **Назначение**: Формирует URL для вебхука на основе токена и URL сайта.

     **Параметры**: Нет

     **Возвращает**:
     - `str`: URL вебхука, сформированный из `SITE_URL` и `BOT_TOKEN`.

     **Как работает функция**:
     1. Формирование URL: Функция возвращает строку, представляющую URL для вебхука, объединяя `self.SITE_URL` и `self.BOT_TOKEN`.
     
     **Примеры**:
     ```python
     settings.SITE_URL = "https://example.com"
     settings.BOT_TOKEN = "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
     webhook_url = settings.get_webhook_url
     print(webhook_url)  # Вывод: https://example.com/123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
     ```
     
     **ASCII flowchart**:
    ```
    SITE_URL + BOT_TOKEN --> Webhook URL
    ```

```python
    @property
    def get_provider_hook_url(self) -> str:
        """Динамически формирует путь для вебхука на основе токена и URL сайта."""
        return f"{self.SITE_URL}/robokassa"
```
     **Назначение**: Формирует URL для вебхука провайдера платежей (Robokassa).

     **Параметры**: Нет

     **Возвращает**:
     - `str`: URL вебхука провайдера платежей, сформированный из `SITE_URL` и "/robokassa".

     **Как работает функция**:
     1. Формирование URL: Функция возвращает строку, представляющую URL для вебхука провайдера, объединяя `self.SITE_URL` и "/robokassa".

     **Примеры**:
     ```python
     settings.SITE_URL = "https://example.com"
     provider_hook_url = settings.get_provider_hook_url
     print(provider_hook_url)  # Вывод: https://example.com/robokassa
     ```

     **ASCII flowchart**:
    ```
    SITE_URL + "/robokassa" --> Provider Webhook URL
    ```

## Функции

В данном модуле функции отсутствуют. Здесь происходит инициализация объектов и определение класса настроек.

### Инициализация объектов `Bot` и `Dispatcher`

```python
bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())
```

**Назначение**: Инициализация объектов `Bot` и `Dispatcher` из библиотеки `aiogram` для работы с Telegram API.

**Параметры**:
- `settings.BOT_TOKEN` (str): Токен Telegram-бота.
- `default=DefaultBotProperties(parse_mode=ParseMode.HTML)`: Установка режима парсинга HTML по умолчанию для бота.
- `storage=MemoryStorage()`: Использование `MemoryStorage` для хранения данных в оперативной памяти.

**Как работает**:

1. **Инициализация бота**: Создается экземпляр класса `Bot` с использованием токена, полученного из настроек, и устанавливается режим парсинга HTML.
2. **Инициализация диспетчера**: Создается экземпляр класса `Dispatcher` с использованием `MemoryStorage` для хранения данных.

**Примеры**:

```python
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties

# Предположим, что settings.BOT_TOKEN уже определен
# settings.BOT_TOKEN = "some_bot_token"

# Инициализация бота
bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

# Инициализация диспетчера
dp = Dispatcher(storage=MemoryStorage())
```

### Инициализация логгера

```python
log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log.txt")
logger.add(log_file_path, format=settings.FORMAT_LOG, level="INFO", rotation=settings.LOG_ROTATION)
```

**Назначение**: Настройка и инициализация логгера для записи событий и ошибок.

**Параметры**:
- `log_file_path` (str): Путь к файлу лога.
- `format=settings.FORMAT_LOG` (str): Формат записи логов.
- `level="INFO"` (str): Уровень логирования (INFO и выше).
- `rotation=settings.LOG_ROTATION` (str): Правила ротации логов.

**Как работает**:

1. **Определение пути к файлу лога**: Путь к файлу лога формируется на основе текущей директории модуля.
2. **Настройка логгера**: Логгер настраивается для записи в указанный файл с заданным форматом, уровнем логирования и правилами ротации.

**Примеры**:

```python
import os
from loguru import logger

# Предположим, что settings.FORMAT_LOG и settings.LOG_ROTATION уже определены
# settings.FORMAT_LOG = "{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}"
# settings.LOG_ROTATION = "10 MB"

# Определение пути к файлу лога
log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log.txt")

# Настройка логгера
logger.add(log_file_path, format=settings.FORMAT_LOG, level="INFO", rotation=settings.LOG_ROTATION)
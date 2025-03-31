# Модуль конфигурации бота для Telegram Digital Market

## Обзор

Этот модуль содержит класс `Settings`, который используется для управления конфигурационными параметрами Telegram-бота. Он загружает параметры из переменных окружения, определяет URL-адреса для вебхуков и инициализирует основные компоненты бота, такие как `Bot` и `Dispatcher`.

## Подробней

Модуль `config.py` играет важную роль в настройке и инициализации Telegram-бота в проекте `hypotez`. Он использует библиотеку `pydantic_settings` для загрузки параметров из файла `.env` и обеспечивает удобный доступ к этим параметрам через класс `Settings`. Кроме того, модуль создает экземпляры `Bot` и `Dispatcher`, необходимые для работы бота.
Расположение файла `hypotez/src/endpoints/bots/telegram/digital_market/bot/config.py` указывает на то, что это конфигурационный файл для Telegram-бота, используемого в контексте цифрового рынка.

## Классы

### `Settings`

**Описание**:
Класс `Settings` используется для хранения и управления конфигурационными параметрами бота. Он наследуется от `BaseSettings` из библиотеки `pydantic_settings` и автоматически загружает значения из переменных окружения.

**Как работает класс**:
- Класс определяет атрибуты для хранения токена бота (`BOT_TOKEN`), идентификаторов администраторов (`ADMIN_IDS`), токена провайдера (`PROVIDER_TOKEN`), формата логов (`FORMAT_LOG`), ротации логов (`LOG_ROTATION`), URL базы данных (`DB_URL`), URL сайта (`SITE_URL`), хоста сайта (`SITE_HOST`), порта сайта (`SITE_PORT`), логина MRH (`MRH_LOGIN`), паролей MRH (`MRH_PASS_1`, `MRH_PASS_2`) и флага тестового режима (`IN_TEST`).
- Метод `get_webhook_url` динамически формирует URL для вебхука на основе URL сайта и токена бота.
- Метод `get_provider_hook_url` динамически формирует URL для вебхука провайдера на основе URL сайта.
- Класс использует `SettingsConfigDict` для указания пути к файлу `.env`, из которого загружаются переменные окружения.

**Методы**:
- `get_webhook_url`: Формирует URL для вебхука бота.
- `get_provider_hook_url`: Формирует URL для вебхука провайдера.

**Параметры**:
- `BOT_TOKEN` (str): Токен Telegram-бота.
- `ADMIN_IDS` (List[int]): Список идентификаторов администраторов бота.
- `PROVIDER_TOKEN` (str): Токен провайдера платежей.
- `FORMAT_LOG` (str, optional): Формат логов. По умолчанию "{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}".
- `LOG_ROTATION` (str, optional): Ротация логов. По умолчанию "10 MB".
- `DB_URL` (str, optional): URL базы данных. По умолчанию 'sqlite+aiosqlite:///data/db.sqlite3'.
- `SITE_URL` (str): URL сайта.
- `SITE_HOST` (str): Хост сайта.
- `SITE_PORT` (int): Порт сайта.
- `MRH_LOGIN` (str): Логин MRH.
- `MRH_PASS_1` (str): Пароль MRH (часть 1).
- `MRH_PASS_2` (str): Пароль MRH (часть 2).
- `IN_TEST` (int): Флаг тестового режима.

**Примеры**:
```python
# Пример создания экземпляра класса Settings
settings = Settings()

# Пример доступа к переменным окружения
bot_token = settings.BOT_TOKEN
admin_ids = settings.ADMIN_IDS

# Пример получения URL вебхука
webhook_url = settings.get_webhook_url
```

## Функции

### `get_webhook_url`

```python
def get_webhook_url(self) -> str:
    """Динамически формирует путь для вебхука на основе токена и URL сайта."""
    return f"{self.SITE_URL}/{self.BOT_TOKEN}"
```

**Описание**:
Динамически формирует URL для вебхука на основе токена и URL сайта.

**Как работает функция**:
Функция берет `SITE_URL` и `BOT_TOKEN` из экземпляра класса `Settings` и объединяет их в строку, формируя URL для вебхука.

**Параметры**:
- Нет явных параметров, но функция использует атрибуты экземпляра класса `Settings`: `SITE_URL` (str) и `BOT_TOKEN` (str).

**Возвращает**:
- `str`: URL для вебхука.

**Примеры**:
```python
settings = Settings()
webhook_url = settings.get_webhook_url
print(webhook_url)  # Вывод: https://example.com/<bot_token>
```

### `get_provider_hook_url`

```python
def get_provider_hook_url(self) -> str:
    """Динамически формирует путь для вебхука на основе токена и URL сайта."""
    return f"{self.SITE_URL}/robokassa"
```

**Описание**:
Динамически формирует URL для вебхука провайдера на основе URL сайта.

**Как работает функция**:
Функция берет `SITE_URL` из экземпляра класса `Settings` и добавляет к нему "/robokassa", формируя URL для вебхука провайдера.

**Параметры**:
- Нет явных параметров, но функция использует атрибут экземпляра класса `Settings`: `SITE_URL` (str).

**Возвращает**:
- `str`: URL для вебхука провайдера.

**Примеры**:
```python
settings = Settings()
provider_hook_url = settings.get_provider_hook_url
print(provider_hook_url)  # Вывод: https://example.com/robokassa
```
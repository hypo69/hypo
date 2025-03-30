# Модуль конфигурации Telegram-бота для цифрового рынка

## Обзор

Этот модуль содержит настройки и инициализирует основные компоненты Telegram-бота для цифрового рынка. Он использует `pydantic_settings` для загрузки параметров из переменных окружения и предоставляет удобный интерфейс для доступа к этим параметрам. Модуль также инициализирует бота, диспетчер и настраивает логирование.

## Подробней

Этот код предназначен для настройки и запуска Telegram-бота, который взаимодействует с цифровым рынком. Он определяет класс `Settings`, который использует `pydantic-settings` для автоматической загрузки параметров из переменных окружения, указанных в файле `.env`. Это позволяет легко конфигурировать бота без необходимости изменять код.  Класс `Settings` также содержит методы для динамического формирования URL-адресов вебхуков. Бот и диспетчер инициализируются с использованием этих настроек, и настраивается логирование для записи событий в файл.

## Классы

### `Settings`

**Описание**: Класс для хранения настроек бота, загружаемых из переменных окружения.

**Методы**:
- `get_webhook_url`: Формирует URL для вебхука на основе токена и URL сайта.
- `get_provider_hook_url`: Формирует URL для вебхука для провайдера платежей Robokassa.

**Параметры**:
- `BOT_TOKEN` (str): Токен Telegram-бота.
- `ADMIN_IDS` (List[int]): Список ID администраторов бота.
- `PROVIDER_TOKEN` (str): Токен провайдера платежей.
- `FORMAT_LOG` (str): Формат логов (по умолчанию: "{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}").
- `LOG_ROTATION` (str):  Размер ротации логов (по умолчанию: "10 MB").
- `DB_URL` (str): URL базы данных (по умолчанию: 'sqlite+aiosqlite:///data/db.sqlite3').
- `SITE_URL` (str): URL сайта.
- `SITE_HOST` (str): Хост сайта.
- `SITE_PORT` (int): Порт сайта.
- `MRH_LOGIN` (str): Логин для Merchant.
- `MRH_PASS_1` (str): Пароль 1 для Merchant.
- `MRH_PASS_2` (str): Пароль 2 для Merchant.
- `IN_TEST` (int): Признак тестовой среды.

**Примеры**:
```python
from typing import List
import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    BOT_TOKEN: str
    ADMIN_IDS: List[int]
    PROVIDER_TOKEN: str
    FORMAT_LOG: str = "{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}"
    LOG_ROTATION: str = "10 MB"
    DB_URL: str = 'sqlite+aiosqlite:///data/db.sqlite3'
    SITE_URL: str
    SITE_HOST: str
    SITE_PORT: int
    MRH_LOGIN: str
    MRH_PASS_1: str
    MRH_PASS_2: str
    IN_TEST: int
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
    )

    @property
    def get_webhook_url(self) -> str:
        """Динамически формирует путь для вебхука на основе токена и URL сайта."""
        return f"{self.SITE_URL}/{self.BOT_TOKEN}"

    @property
    def get_provider_hook_url(self) -> str:
        """Динамически формирует путь для вебхука на основе токена и URL сайта."""
        return f"{self.SITE_URL}/robokassa"

# Пример использования:
settings = Settings()
print(f"Webhook URL: {settings.get_webhook_url}")
```

## Функции

### `get_webhook_url`

```python
    @property
    def get_webhook_url(self) -> str:
        """Динамически формирует путь для вебхука на основе токена и URL сайта."""
        return f"{self.SITE_URL}/{self.BOT_TOKEN}"
```

**Описание**:  Формирует и возвращает URL для вебхука Telegram-бота.

**Возвращает**:
- `str`: URL для вебхука, составленный из `SITE_URL` и `BOT_TOKEN`.

**Примеры**:
```python
settings = Settings()
webhook_url = settings.get_webhook_url
print(f"Webhook URL: {webhook_url}")
```

### `get_provider_hook_url`

```python
    @property
    def get_provider_hook_url(self) -> str:
        """Динамически формирует путь для вебхука на основе токена и URL сайта."""
        return f"{self.SITE_URL}/robokassa"
```

**Описание**: Формирует и возвращает URL для вебхука провайдера платежей Robokassa.

**Возвращает**:
- `str`: URL для вебхука Robokassa, составленный из `SITE_URL` и фиксированного пути `/robokassa`.

**Примеры**:
```python
settings = Settings()
provider_url = settings.get_provider_hook_url
print(f"Provider URL: {provider_url}")
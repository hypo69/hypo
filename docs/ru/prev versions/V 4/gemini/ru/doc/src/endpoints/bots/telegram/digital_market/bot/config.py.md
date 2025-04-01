# Модуль конфигурации бота Telegram для цифрового рынка

## Обзор

Этот модуль содержит настройки и конфигурации, необходимые для работы Telegram-бота цифрового рынка. Он определяет параметры, такие как токен бота, идентификаторы администраторов, URL-адреса сайта, настройки базы данных и другие параметры конфигурации.

## Подробней

Файл `config.py` содержит класс `Settings`, который использует `pydantic_settings` для загрузки переменных окружения из файла `.env`. Этот класс обеспечивает доступ к различным параметрам конфигурации, необходимым для правильной работы бота. Также в модуле инициализируется бот, диспетчер и настраивается логирование. Расположение файла `hypotez/src/endpoints/bots/telegram/digital_market/bot/config.py` указывает, что он является частью подсистемы Telegram-бота для цифрового рынка, что позволяет сделать вывод о том, что данный бот используется для автоматизации процессов, связанных с цифровой коммерцией.

## Классы

### `Settings`

**Описание**: Класс, представляющий настройки бота, загружаемые из переменных окружения.

**Методы**:
- `get_webhook_url`: Формирует URL для вебхука на основе токена бота и URL сайта.
- `get_provider_hook_url`: Формирует URL для вебхука провайдера платежей.

**Параметры**:
- `BOT_TOKEN` (str): Токен Telegram-бота.
- `ADMIN_IDS` (List[int]): Список идентификаторов администраторов бота.
- `PROVIDER_TOKEN` (str): Токен провайдера платежей.
- `FORMAT_LOG` (str): Формат логов (по умолчанию: "{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}").
- `LOG_ROTATION` (str): Размер ротации логов (по умолчанию: "10 MB").
- `DB_URL` (str): URL базы данных (по умолчанию: 'sqlite+aiosqlite:///data/db.sqlite3').
- `SITE_URL` (str): URL сайта.
- `SITE_HOST` (str): Хост сайта.
- `SITE_PORT` (int): Порт сайта.
- `MRH_LOGIN` (str): Логин MRH.
- `MRH_PASS_1` (str): Пароль MRH 1.
- `MRH_PASS_2` (str): Пароль MRH 2.
- `IN_TEST` (int): Флаг, определяющий, находится ли бот в тестовом режиме.

**Примеры**
```python
# Пример использования класса Settings
settings = Settings()
print(f"Bot token: {settings.BOT_TOKEN}")
print(f"Admin IDs: {settings.ADMIN_IDS}")
print(f"Webhook URL: {settings.get_webhook_url}")
```

## Функции

### `Settings.get_webhook_url`

```python
def get_webhook_url(self) -> str:
    """Динамически формирует путь для вебхука на основе токена и URL сайта."""
    ...
```

**Описание**: Формирует URL для вебхука, объединяя URL сайта и токен бота.

**Возвращает**:
- `str`: URL для вебхука.

**Примеры**:
```python
settings = Settings()
webhook_url = settings.get_webhook_url
print(f"Webhook URL: {webhook_url}")
```

### `Settings.get_provider_hook_url`

```python
def get_provider_hook_url(self) -> str:
    """Динамически формирует путь для вебхука на основе токена и URL сайта."""
    ...
```

**Описание**: Формирует URL для вебхука провайдера платежей, объединяя URL сайта и строку "robokassa".

**Возвращает**:
- `str`: URL для вебхука провайдера платежей.

**Примеры**:
```python
settings = Settings()
provider_webhook_url = settings.get_provider_hook_url
print(f"Provider Webhook URL: {provider_webhook_url}")
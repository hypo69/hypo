# Модуль `playwrid.py`

## Обзор

Модуль `playwrid.py` определяет подкласс `Playwrid` класса `PlaywrightCrawler`. Он предоставляет дополнительную функциональность, такую как возможность устанавливать пользовательские настройки браузера, профили и параметры запуска, используя Playwright.

## Оглавление

- [Классы](#классы)
    - [`Playwrid`](#playwrid)
- [Функции](#функции)
    - [`_load_settings`](#_load_settings)
    - [`_set_launch_options`](#_set_launch_options)
    - [`start`](#start)
- [Свойства](#свойства)
    - [`current_url`](#current_url)

## Классы

### `Playwrid`

**Описание**:
Подкласс `PlaywrightCrawler`, предоставляющий дополнительную функциональность.

**Атрибуты**:
- `driver_name` (str): Имя драйвера, по умолчанию `playwrid`.
- `context` (Optional[PlaywrightCrawlingContext]): Текущий контекст браузера.

**Методы**:
- [`__init__`](#__init__)
- [`_load_settings`](#_load_settings)
- [`_set_launch_options`](#_set_launch_options)
- [`start`](#start)

#### `__init__`

**Описание**:
Инициализирует Playwright Crawler с указанными параметрами запуска, настройками и user-agent.

**Параметры**:
- `settings_name` (Optional[str], optional): Имя файла настроек для использования. По умолчанию `None`.
- `user_agent` (Optional[str], optional): Строка user-agent для использования. По умолчанию используется случайный user-agent.
- `options` (Optional[List[str]], optional): Список параметров Playwright, передаваемых при инициализации. По умолчанию `None`.
- `*args`:  Дополнительные позиционные аргументы.
- `**kwargs`: Дополнительные именованные аргументы.

**Возвращает**:
- `None`

#### `_load_settings`

**Описание**:
Загружает настройки для Playwrid Crawler.

**Параметры**:
- `settings_name` (Optional[str], optional): Имя файла настроек для использования. По умолчанию `None`.

**Возвращает**:
- `SimpleNamespace`: Объект SimpleNamespace, содержащий настройки.

#### `_set_launch_options`

**Описание**:
Настраивает параметры запуска для Playwright Crawler.

**Параметры**:
- `settings` (SimpleNamespace): Объект SimpleNamespace, содержащий настройки запуска.
- `user_agent` (Optional[str], optional): Строка user-agent для использования. По умолчанию `None`.
- `options` (Optional[List[str]], optional): Список параметров Playwright, передаваемых при инициализации. По умолчанию `None`.

**Возвращает**:
- `Dict[str, Any]`: Словарь с параметрами запуска для Playwright.

#### `start`

**Описание**:
Запускает Playwrid Crawler и переходит по указанному URL.

**Параметры**:
- `url` (str): URL для перехода.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: В случае ошибки при запуске браузера, регистрирует ошибку в лог.

## Функции

### `_load_settings`

**Описание**:
Загружает настройки для Playwrid Crawler.

**Параметры**:
- `settings_name` (Optional[str], optional): Имя файла настроек для использования. По умолчанию `None`.

**Возвращает**:
- `SimpleNamespace`: Объект SimpleNamespace, содержащий настройки.

### `_set_launch_options`

**Описание**:
Настраивает параметры запуска для Playwright Crawler.

**Параметры**:
- `settings` (SimpleNamespace): Объект SimpleNamespace, содержащий настройки запуска.
- `user_agent` (Optional[str], optional): Строка user-agent для использования. По умолчанию `None`.
- `options` (Optional[List[str]], optional): Список параметров Playwright, передаваемых при инициализации. По умолчанию `None`.

**Возвращает**:
- `Dict[str, Any]`: Словарь с параметрами запуска для Playwright.

### `start`

**Описание**:
Запускает Playwrid Crawler и переходит по указанному URL.

**Параметры**:
- `url` (str): URL для перехода.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: В случае ошибки при запуске браузера, регистрирует ошибку в лог.

## Свойства

### `current_url`

**Описание**:
Возвращает текущий URL браузера.

**Возвращает**:
- `Optional[str]`: Текущий URL или `None`, если контекст браузера не задан.
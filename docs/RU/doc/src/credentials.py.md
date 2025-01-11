# `hypotez/src/credentials.py`

## Обзор

Модуль `credentials.py` предназначен для управления глобальными настройками проекта, такими как пути, пароли, логины и настройки API. Он использует класс `ProgramSettings` для хранения этих настроек и обеспечивает их загрузку из конфигурационных файлов и базы данных KeePass.

## Оглавление

- [Функции](#функции)
    - [`set_project_root`](#set_project_root)
    - [`singleton`](#singleton)
- [Классы](#классы)
    - [`ProgramSettings`](#programsettings)
        - [`__init__`](#__init__)
        - [`_load_credentials`](#_load_credentials)
        - [`_open_kp`](#_open_kp)
        - [`_load_aliexpress_credentials`](#_load_aliexpress_credentials)
        - [`_load_openai_credentials`](#_load_openai_credentials)
        - [`_load_gemini_credentials`](#_load_gemini_credentials)
        - [`_load_telegram_credentials`](#_load_telegram_credentials)
        - [`_load_discord_credentials`](#_load_discord_credentials)
        - [`_load_PrestaShop_credentials`](#_load_prestashop_credentials)
        - [`_load_presta_translations_credentials`](#_load_presta_translations_credentials)
        - [`_load_smtp_credentials`](#_load_smtp_credentials)
        - [`_load_facebook_credentials`](#_load_facebook_credentials)
        - [`_load_gapi_credentials`](#_load_gapi_credentials)
        - [`now`](#now)
- [Глобальные переменные](#глобальные-переменные)
    - [`gs`](#gs)

## Функции

### `set_project_root`

**Описание**:
Находит корневой каталог проекта, начиная с каталога текущего файла и поднимаясь вверх, пока не будет найден каталог, содержащий один из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple, optional): Имена файлов или каталогов, которые используются для идентификации корня проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневому каталогу, если он найден, в противном случае каталог, в котором находится скрипт.

### `singleton`

**Описание**:
Декоратор для реализации Singleton.

**Параметры**:
- `cls`: Класс, для которого применяется паттерн Singleton.

**Возвращает**:
- `function`: Функция, которая возвращает единственный экземпляр класса.

## Классы

### `ProgramSettings`

**Описание**:
Класс `ProgramSettings` - это синглтон, который хранит основные параметры и настройки проекта.

**Параметры**:
- `host_name` (str): Имя хоста текущей машины.
- `base_dir` (Path): Корневой каталог проекта.
- `config` (SimpleNamespace): Пространство имен для хранения настроек проекта, загруженных из `config.json`.
- `credentials` (SimpleNamespace): Пространство имен для хранения учетных данных для различных сервисов.
- `MODE` (str): Режим работы приложения (например, 'dev', 'prod').
- `path` (SimpleNamespace): Пространство имен для хранения путей к различным директориям проекта.

**Методы**:
- [`__init__`](#__init__): Инициализация экземпляра класса и загрузка настроек.
- [`_load_credentials`](#_load_credentials): Загружает учетные данные из KeePass.
- [`_open_kp`](#_open_kp): Открывает базу данных KeePass.
- [`_load_aliexpress_credentials`](#_load_aliexpress_credentials): Загружает учетные данные для Aliexpress API.
- [`_load_openai_credentials`](#_load_openai_credentials): Загружает учетные данные для OpenAI API.
- [`_load_gemini_credentials`](#_load_gemini_credentials): Загружает учетные данные для GoogleAI API.
- [`_load_telegram_credentials`](#_load_telegram_credentials): Загружает учетные данные для Telegram API.
- [`_load_discord_credentials`](#_load_discord_credentials): Загружает учетные данные для Discord API.
- [`_load_PrestaShop_credentials`](#_load_prestashop_credentials): Загружает учетные данные для PrestaShop API.
- [`_load_presta_translations_credentials`](#_load_presta_translations_credentials): Загружает учетные данные для PrestaShop Translations API.
- [`_load_smtp_credentials`](#_load_smtp_credentials): Загружает учетные данные для SMTP.
- [`_load_facebook_credentials`](#_load_facebook_credentials): Загружает учетные данные для Facebook API.
- [`_load_gapi_credentials`](#_load_gapi_credentials): Загружает учетные данные для Google API.
- [`now`](#now): Возвращает текущую метку времени.

#### `__init__`

**Описание**:
Инициализирует объект `ProgramSettings`. Загружает конфигурацию из `config.json`, устанавливает пути к директориям, добавляет пути к `sys.path`, и загружает учетные данные.

**Параметры**:
- `kwargs` : Произвольные ключевые аргументы.

#### `_load_credentials`

**Описание**:
Загружает учетные данные из KeePass для различных сервисов.

**Параметры**:
- Нет

**Возвращает**:
- `None`

#### `_open_kp`

**Описание**:
Открывает базу данных KeePass.

**Параметры**:
- `retry` (int, optional): Количество попыток открытия базы данных. По умолчанию `3`.

**Возвращает**:
- `PyKeePass | None`: Экземпляр `PyKeePass` или `None`, если открытие не удалось.

**Вызывает исключения**:
- `Exception`: В случае неудачного открытия базы данных после нескольких попыток.

#### `_load_aliexpress_credentials`

**Описание**:
Загружает учетные данные Aliexpress API из KeePass.

**Параметры**:
- `kp` (PyKeePass): Экземпляр `PyKeePass`.

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно, `False` в противном случае.

**Вызывает исключения**:
- `Exception`: В случае ошибки при извлечении данных из KeePass.

#### `_load_openai_credentials`

**Описание**:
Загружает учетные данные OpenAI API из KeePass.

**Параметры**:
- `kp` (PyKeePass): Экземпляр `PyKeePass`.

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно, `False` в противном случае.

**Вызывает исключения**:
- `Exception`: В случае ошибки при извлечении данных из KeePass.

#### `_load_gemini_credentials`

**Описание**:
Загружает учетные данные GoogleAI API из KeePass.

**Параметры**:
- `kp` (PyKeePass): Экземпляр `PyKeePass`.

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно, `False` в противном случае.

**Вызывает исключения**:
- `Exception`: В случае ошибки при извлечении данных из KeePass.

#### `_load_telegram_credentials`

**Описание**:
Загружает учетные данные Telegram API из KeePass.

**Параметры**:
- `kp` (PyKeePass): Экземпляр `PyKeePass`.

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно, `False` в противном случае.

**Вызывает исключения**:
- `Exception`: В случае ошибки при извлечении данных из KeePass.

#### `_load_discord_credentials`

**Описание**:
Загружает учетные данные Discord API из KeePass.

**Параметры**:
- `kp` (PyKeePass): Экземпляр `PyKeePass`.

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно, `False` в противном случае.

**Вызывает исключения**:
- `Exception`: В случае ошибки при извлечении данных из KeePass.

#### `_load_PrestaShop_credentials`

**Описание**:
Загружает учетные данные PrestaShop API из KeePass.

**Параметры**:
- `kp` (PyKeePass): Экземпляр `PyKeePass`.

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно, `False` в противном случае.

**Вызывает исключения**:
- `Exception`: В случае ошибки при извлечении данных из KeePass.

#### `_load_presta_translations_credentials`

**Описание**:
Загружает учетные данные для PrestaShop Translations API из KeePass.

**Параметры**:
- `kp` (PyKeePass): Экземпляр `PyKeePass`.

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно, `False` в противном случае.

**Вызывает исключения**:
- `Exception`: В случае ошибки при извлечении данных из KeePass.

#### `_load_smtp_credentials`

**Описание**:
Загружает учетные данные SMTP из KeePass.

**Параметры**:
- `kp` (PyKeePass): Экземпляр `PyKeePass`.

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно, `False` в противном случае.

**Вызывает исключения**:
- `Exception`: В случае ошибки при извлечении данных из KeePass.

#### `_load_facebook_credentials`

**Описание**:
Загружает учетные данные Facebook API из KeePass.

**Параметры**:
- `kp` (PyKeePass): Экземпляр `PyKeePass`.

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно, `False` в противном случае.

**Вызывает исключения**:
- `Exception`: В случае ошибки при извлечении данных из KeePass.

#### `_load_gapi_credentials`

**Описание**:
Загружает учетные данные Google API из KeePass.

**Параметры**:
- `kp` (PyKeePass): Экземпляр `PyKeePass`.

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно, `False` в противном случае.

**Вызывает исключения**:
- `Exception`: В случае ошибки при извлечении данных из KeePass.

#### `now`

**Описание**:
Возвращает текущую метку времени в формате, определенном в конфигурации.

**Параметры**:
- Нет

**Возвращает**:
- `str`: Текущая метка времени в строковом формате.

## Глобальные переменные

### `gs`

**Описание**:
Глобальный экземпляр класса `ProgramSettings`.

**Тип**:
- `ProgramSettings`
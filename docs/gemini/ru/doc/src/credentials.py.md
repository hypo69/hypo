# `src/credentials.py`

## Обзор

Модуль содержит глобальные настройки проекта, включая пути, пароли, логины и настройки API. Он использует `dataclasses`, `pathlib`, `typing`, `pykeepass` для управления настройками и учетными данными.

## Оглавление

- [Функции](#функции)
    - [`set_project_root`](#set_project_root)
    - [`singleton`](#singleton)
- [Классы](#классы)
    - [`ProgramSettings`](#ProgramSettings)
        - [`__post_init__`](#__post_init__)
        - [`_load_credentials`](#_load_credentials)
        - [`_open_kp`](#_open_kp)
        - [`_load_aliexpress_credentials`](#_load_aliexpress_credentials)
        - [`_load_openai_credentials`](#_load_openai_credentials)
        - [`_load_gemini_credentials`](#_load_gemini_credentials)
        - [`_load_telegram_credentials`](#_load_telegram_credentials)
        - [`_load_discord_credentials`](#_load_discord_credentials)
        - [`_load_prestashop_credentials`](#_load_prestashop_credentials)
        - [`_load_presta_translations_credentials`](#_load_presta_translations_credentials)
        - [`_load_smtp_credentials`](#_load_smtp_credentials)
        - [`_load_facebook_credentials`](#_load_facebook_credentials)
        - [`_load_gapi_credentials`](#_load_gapi_credentials)
        - [`now`](#now)

## Функции

### `set_project_root`

**Описание**: Находит корневой каталог проекта, начиная с каталога текущего файла, ища вверх и останавливаясь на первом каталоге, содержащем любой из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple): Имена файлов или каталогов для идентификации корня проекта. По умолчанию `('__root__','.git')`.

**Возвращает**:
- `Path`: Путь к корневому каталогу, если найден, в противном случае - каталог, где расположен скрипт.

### `singleton`

**Описание**: Декоратор для реализации Singleton.

**Параметры**:
- `cls`: Класс, для которого применяется декоратор.

**Возвращает**:
- `get_instance`: Функция для получения экземпляра класса.

## Классы

### `ProgramSettings`

**Описание**: Класс настроек программы, реализованный как синглтон, хранящий основные параметры и настройки проекта.

**Атрибуты**:
- `host_name` (str): Имя хоста. По умолчанию получается с помощью `socket.gethostname()`.
- `base_dir` (Path): Корневой каталог проекта. По умолчанию определяется с помощью `set_project_root()`.
- `config` (SimpleNamespace): Пространство имен для настроек из `config.json`.
- `credentials` (SimpleNamespace): Пространство имен для учетных данных.
- `MODE` (str): Режим работы (`dev` или `prod`). По умолчанию `'dev'`.
- `path` (SimpleNamespace): Пространство имен для путей к различным каталогам проекта.

#### `__post_init__`

**Описание**: Выполняет инициализацию после создания экземпляра класса.

**Параметры**:
- Нет

**Возвращает**:
- `None`

#### `_load_credentials`

**Описание**: Загружает учетные данные из настроек.

**Параметры**:
- Нет

**Возвращает**:
- `None`

#### `_open_kp`

**Описание**: Открывает базу данных KeePass.

**Параметры**:
- `retry` (int, optional): Количество попыток открытия. По умолчанию `3`.

**Возвращает**:
- `PyKeePass | None`: Экземпляр PyKeePass при успешном открытии, иначе `None`.

#### `_load_aliexpress_credentials`

**Описание**: Загружает учетные данные Aliexpress API из KeePass.

**Параметры**:
- `kp` (PyKeePass): Экземпляр базы данных KeePass.

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно, иначе `False`.

#### `_load_openai_credentials`

**Описание**: Загружает учетные данные OpenAI из KeePass.

**Параметры**:
- `kp` (PyKeePass): Экземпляр базы данных KeePass.

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно, иначе `False`.

#### `_load_gemini_credentials`

**Описание**: Загружает учетные данные Google AI (Gemini) из KeePass.

**Параметры**:
- `kp` (PyKeePass): Экземпляр базы данных KeePass.

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно, иначе `False`.

#### `_load_telegram_credentials`

**Описание**: Загружает учетные данные Telegram из KeePass.

**Параметры**:
- `kp` (PyKeePass): Экземпляр базы данных KeePass.

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно, иначе `False`.

#### `_load_discord_credentials`

**Описание**: Загружает учетные данные Discord из KeePass.

**Параметры**:
- `kp` (PyKeePass): Экземпляр базы данных KeePass.

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно, иначе `False`.

#### `_load_prestashop_credentials`

**Описание**: Загружает учетные данные PrestaShop из KeePass.

**Параметры**:
- `kp` (PyKeePass): Экземпляр базы данных KeePass.

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно, иначе `False`.

#### `_load_presta_translations_credentials`

**Описание**: Загружает учетные данные для переводов PrestaShop из KeePass.

**Параметры**:
- `kp` (PyKeePass): Экземпляр базы данных KeePass.

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно, иначе `False`.

#### `_load_smtp_credentials`

**Описание**: Загружает учетные данные SMTP из KeePass.

**Параметры**:
- `kp` (PyKeePass): Экземпляр базы данных KeePass.

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно, иначе `False`.

#### `_load_facebook_credentials`

**Описание**: Загружает учетные данные Facebook из KeePass.

**Параметры**:
- `kp` (PyKeePass): Экземпляр базы данных KeePass.

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно, иначе `False`.

#### `_load_gapi_credentials`

**Описание**: Загружает учетные данные Google API из KeePass.

**Параметры**:
- `kp` (PyKeePass): Экземпляр базы данных KeePass.

**Возвращает**:
- `bool`: `True`, если загрузка прошла успешно, иначе `False`.

#### `now`

**Описание**: Возвращает текущую метку времени в формате `год_месяц_день_часы_минуты_секунды_миллисекунды`.

**Параметры**:
- Нет

**Возвращает**:
- `str`: Текущая метка времени в строковом формате.

## Глобальные переменные

`gs`: `ProgramSettings` - Глобальный экземпляр `ProgramSettings`.
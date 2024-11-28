# Модуль credentials

## Обзор

Этот модуль предоставляет класс `ProgramSettings`, реализующий паттерн Singleton, для хранения и управления настройками программы.  Класс загружает учетные данные из файла `credentials.kdbx` (KeePass), а также конфигурацию из файла `config.json`.  Он содержит различные поля для хранения API ключей, паролей, и других важных параметров для разных сервисов (Aliexpress, OpenAI, Telegram, и др.).

## Оглавление

- [Модуль credentials](#модуль-credentials)
- [Обзор](#обзор)
- [Функции](#функции)
    - [`set_project_root`](#set_project_root)
    - [`singleton`](#singleton)
- [Класс `ProgramSettings`](#класс-programssettings)
    - [`__init__`](#init)
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



## Функции

### `set_project_root`

**Описание**:  Находит корневую директорию проекта, начиная от текущей директории файла. Поиск происходит вверх по дереву директорий, останавливаясь на первой директории, содержащей указанные маркерные файлы.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или директорий, используемых для определения корневой директории проекта.

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если найдена, иначе - директория, где расположен скрипт.


### `singleton`

**Описание**: Декоратор для реализации паттерна Singleton.  Гарантирует, что существует только один экземпляр класса.

**Параметры**:

- `cls`: Класс, который будет использоваться в качестве синглтона.

**Возвращает**:

- `function`: Функция, возвращающая единственный экземпляр класса `cls`.


## Класс `ProgramSettings`

### Описание

Класс `ProgramSettings` - синглтон, хранящий основные параметры и настройки проекта. Он загружает данные из файлов `config.json` и `credentials.kdbx`.

### `__init__`

**Описание**: Конструктор класса.  Инициализирует поля класса, устанавливает пути, загружает данные из файлов, и выполняет проверку версии.

**Параметры**:
Нет.

**Вызывает исключения**:


### `_load_credentials`

**Описание**: Загружает учетные данные из файлов настроек.

**Параметры**: Нет

**Возвращает**:  Ничего.

**Вызывает исключения**:
- `BinaryError`
- `CredentialsError`
- `DefaultSettingsException`
- `HeaderChecksumError`
- `KeePassException`
- `PayloadChecksumError`
- `UnableToSendToRecycleBin`


### `_open_kp`

**Описание**: Открывает базу данных KeePass.

**Параметры**:
- `retry` (int): Количество попыток открытия.

**Возвращает**:
- `PyKeePass | None`: Экземпляр класса `PyKeePass` при успешном открытии, иначе `None`.


**Вызывает исключения**:
- `Exception` (В случае ошибок при работе с KeePass)



###  Остальные методы (`_load_aliexpress_credentials`, `_load_openai_credentials`, и т.д.)

**Описание**: Загружают данные учетных данных для различных сервисов из KeePass.

**Параметры**:
- `kp (PyKeePass)`: Экземпляр класса `PyKeePass`, содержащий открытую базу данных KeePass

**Возвращает**:
- `bool`: `True` если загрузка прошла успешно, `False` иначе.

**Вызывает исключения**:
- `Exception` (В случае ошибок при извлечении данных)


### `now`

**Описание**: Возвращает текущую метку времени в заданном формате.

**Параметры**:
- `dformat` (str, optional): Формат метки времени. По умолчанию `'%y_%m_%d_%H_%M_%S_%f'`.

**Возвращает**:
- `str`: Строковое представление текущей метки времени.

**Вызывает исключения**:
Нет.
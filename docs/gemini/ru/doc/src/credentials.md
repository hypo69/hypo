# Документация модуля `src.credentials`

## Обзор

Модуль `src.credentials` предназначен для загрузки и хранения информации об учетных данных (API-ключи, пароли и т.д.) из файла базы данных KeePass `credentials.kdbx`. Он также включает функцию `set_project_root` для определения корневого каталога проекта.

## Содержание

- [Обзор](#обзор)
- [Подробнее](#подробнее)
- [Функции](#функции)
  - [`set_project_root`](#set_project_root)
  - [`singleton`](#singleton)
- [Классы](#классы)
  - [`ProgramSettings`](#programsettings)
- [Инициализация и конфигурация](#инициализация-и-конфигурация)
  - [Определение корневого каталога проекта](#определение-корневого-каталога-проекта)
  - [Загрузка конфигурации](#загрузка-конфигурации)
  - [Управление учетными данными с использованием KeePass](#управление-учетными-данными-с-использованием-keepass)
  - [Структура дерева базы данных KeePass](#структура-дерева-базы-данных-keepass)
  - [Глобальный экземпляр `ProgramSettings`](#глобальный-экземпляр-programsettings)

## Подробнее

Этот модуль играет важную роль в проекте, обеспечивая безопасное хранение и управление учетными данными, необходимыми для работы с различными сервисами и API. Он использует KeePass для хранения конфиденциальной информации, что позволяет избежать хранения паролей в открытом виде в коде или конфигурационных файлах. Функция `set_project_root` упрощает определение корневого каталога проекта, что важно для правильной работы с путями к файлам и ресурсам.

## Функции

### `set_project_root`

```python
def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Args:
        marker_files (tuple): File or directory names for identifying the project’s root directory.

    Returns:
        Path: The path to the root directory if found, otherwise the directory where the script is located.

     **Как работает функция**:
    Функция `set_project_root` предназначена для автоматического определения корневой директории проекта.

    1.  Определение текущего пути:
        -   Получает путь к директории, в которой находится текущий файл.

    2.  Поиск маркеров в родительских директориях:
        -   Перебирает текущую директорию и все её родительские директории.
        -   Для каждой директории проверяет наличие файлов или директорий, указанных в `marker_files`.

    3.  Установка корневой директории:
        -   Если один из маркеров найден, устанавливает текущую родительскую директорию как корневую.
        -   Прекращает дальнейший поиск.

    4.  Добавление корневой директории в `sys.path`:
        -   Если корневая директория еще не добавлена в `sys.path`, добавляет её.

    5.  Возврат корневой директории:
        -   Возвращает объект `Path`, представляющий корневую директорию проекта.

    """
    ...
```

**Описание**: Находит корневой каталог проекта, начиная с текущего каталога. Поиск идет вверх по каталогам до тех пор, пока не будет найден каталог, содержащий один из файлов в списке `marker_files`.

**Параметры**:

- `marker_files` (tuple): Кортеж строк, представляющих имена файлов или каталогов, используемых для идентификации корневого каталога проекта. По умолчанию ищет следующие маркеры: `pyproject.toml`, `requirements.txt`, `.git`.

**Возвращает**:

- `Path`: Путь к корневому каталогу проекта, если он найден, в противном случае - путь к каталогу, в котором находится скрипт.

### `singleton`

```python
def singleton(cls):
    """
    Args:
        cls: The class that should be converted into a singleton.

    Returns:
        function: A function that returns an instance of the singleton class.

     **Как работает функция**:
        Функция `singleton` является декоратором, который преобразует класс в Singleton.

    1.  Проверка наличия экземпляра:
        -   При первом вызове создается новый экземпляр класса и сохраняется в `instances`.

    2.  Возврат существующего экземпляра:
        -   При последующих вызовах возвращается сохраненный экземпляр.

    """
    ...
```

**Описание**: Декоратор для создания класса-одиночки (singleton).

**Параметры**:

- `cls`: Класс, который должен быть преобразован в singleton.

**Возвращает**:

- `function`: Функция, которая возвращает экземпляр класса-одиночки.

## Классы

### `ProgramSettings`

```python
class ProgramSettings:
    """
    Args:
        **kwargs: Arbitrary keyword arguments.

    Raises:
        BinaryError: Exception for binary data errors.
        CredentialsError: Exception for credential data errors.
        DefaultSettingsException: Exception for default settings errors.
        HeaderChecksumError: Exception for header checksum errors.
        KeePassException: Exception for KeePass database errors.
        PayloadChecksumError: Exception for payload checksum errors.
        UnableToSendToRecycleBin: Exception for recycle bin sending errors.
        Exception: General exception.

     **Как работает класс**:
        Класс `ProgramSettings` предназначен для загрузки и хранения настроек программы, включая учетные данные из KeePass.

    1.  Инициализация:
        -   Определение базовой директории проекта.
        -   Загрузка конфигурации из файла `config.json`.
        -   Инициализация путей к различным директориям проекта.
        -   Проверка наличия новой версии проекта.
        -   Загрузка учетных данных из KeePass.

    2.  Загрузка учетных данных из KeePass:
        -   Открытие базы данных KeePass с использованием пароля, полученного из файла или введенного пользователем.
        -   Загрузка учетных данных для различных сервисов (Aliexpress, OpenAI, Gemini, Telegram, Discord, PrestaShop, SMTP, Facebook, Google API).

    3.  Методы для загрузки учетных данных:
        -   `_load_aliexpress_credentials`: Загрузка учетных данных для Aliexpress API.
        -   `_load_openai_credentials`: Загрузка ключей OpenAI API.
        -   `_load_gemini_credentials`: Загрузка ключей GoogleAI API.
        -   `_load_telegram_credentials`: Загрузка токена Telegram.
        -   `_load_discord_credentials`: Загрузка учетных данных Discord.
        -   `_load_PrestaShop_credentials`: Загрузка учетных данных PrestaShop.
        -   `_load_presta_translations_credentials`: Загрузка учетных данных для переводов PrestaShop.
        -   `_load_smtp_credentials`: Загрузка учетных данных SMTP.
        -   `_load_facebook_credentials`: Загрузка учетных данных Facebook.
        -   `_load_gapi_credentials`: Загрузка ключей Google API.

    4.  Обработка исключений:
        -   Обработка различных исключений, которые могут возникнуть при работе с KeePass и загрузке учетных данных.
        -   Логирование ошибок с использованием модуля `logger`.

    5.  Singleton:
        -   Использование декоратора `@singleton` для обеспечения единственного экземпляра класса.

    6.  Глобальный экземпляр `gs`:
        -   Создание глобального экземпляра класса `ProgramSettings` для доступа к настройкам и учетным данным из любой части проекта.

    """
    ...
```

**Описание**: Класс для настроек программы. Он устанавливает основные параметры и настройки проекта. Загружает конфигурацию из `config.json` и данные учетных данных из файла базы данных KeePass `credentials.kdbx`.

**Атрибуты**:

- `host_name` (str): Имя хоста.
- `base_dir` (Path): Путь к корневому каталогу проекта.
- `config` (SimpleNamespace): Объект, содержащий конфигурацию проекта.
- `credentials` (SimpleNamespace): Объект, содержащий учетные данные.
- `MODE` (str): Режим работы проекта (например, 'dev', 'prod').
- `path` (SimpleNamespace): Объект, содержащий пути к различным каталогам проекта.

**Методы**:

- `__init__(self, **kwargs)`: Инициализирует экземпляр класса.
  - Загружает конфигурацию проекта из `config.json`.
  - Инициализирует атрибут `path` путями к различным каталогам проекта.
  - Вызывает `check_latest_release` для проверки новой версии проекта.
  - Загружает учетные данные из `credentials.kdbx`.
- `_load_credentials(self) -> None`: Загружает учетные данные из KeePass.
- `_open_kp(self, retry: int = 3) -> PyKeePass | None`: Открывает базу данных KeePass. Обрабатывает возможные исключения при открытии базы данных.
- `_load_aliexpress_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные Aliexpress из KeePass.
- `_load_openai_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные OpenAI из KeePass.
- `_load_gemini_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные GoogleAI из KeePass.
- `_load_telegram_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные Telegram из KeePass.
- `_load_discord_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные Discord из KeePass.
- `_load_PrestaShop_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные PrestaShop из KeePass.
- `_load_presta_translations_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные PrestaShop Translations из KeePass.
- `_load_smtp_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные SMTP из KeePass.
- `_load_facebook_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные Facebook из KeePass.
- `_load_gapi_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные Google API из KeePass.
- `now(self) -> str`: Возвращает текущую временную метку в формате, указанном в файле `config.json`.

## Инициализация и конфигурация

Когда проект запускается, он инициализирует и настраивает различные параметры и учетные данные. В этом разделе объясняется, как эти значения устанавливаются и управляются.

### Определение корневого каталога проекта

Проект автоматически определяет свой корневой каталог, выполняя поиск вверх от текущего каталога файла для определенных файлов-маркеров (`pyproject.toml`, `requirements.txt`, `.git`). Это гарантирует, что проект сможет найти свои ресурсы независимо от текущего рабочего каталога.

### Загрузка конфигурации

Проект загружает свои настройки по умолчанию из файла `config.json`, расположенного в каталоге `src`. Этот файл JSON содержит различные параметры конфигурации, такие как:

- **Информация об авторе**: Подробности об авторе.
- **Доступные режимы**: Поддерживаемые режимы (`dev`, `debug`, `test`, `prod`).
- **Пути**: Каталоги для журналов, временных файлов, внешнего хранилища и Google Drive.
- **Детали проекта**: Имя, версия и информация о выпуске проекта.

### Управление учетными данными с использованием KeePass

**Что такое KeePass?**

KeePass - это бесплатный менеджер паролей с открытым исходным кодом, который безопасно хранит ваши пароли и другую конфиденциальную информацию в зашифрованной базе данных. База данных защищена главным паролем, который является единственным паролем, который вам нужно запомнить. KeePass использует надежные алгоритмы шифрования (такие как AES и Twofish) для обеспечения безопасности ваших данных.

**Почему KeePass хорош?**

- **Безопасность**: KeePass использует отраслевые стандарты шифрования для защиты ваших данных, что делает его очень безопасным от несанкционированного доступа.
- **Переносимость**: Вы можете хранить свою базу данных KeePass на USB-накопителе или в облачном хранилище и получать к ней доступ с нескольких устройств.
- **Настройка**: KeePass позволяет организовывать ваши пароли в группы и подгруппы, что упрощает управление большим количеством учетных данных.
- **Открытый исходный код**: Будучи проектом с открытым исходным кодом, KeePass является прозрачным и может быть проверен сообществом на предмет его безопасности.

**Как KeePass работает в этом проекте**

Учетные данные безопасно управляются с использованием базы данных KeePass (`credentials.kdbx`). Главный пароль для этой базы данных обрабатывается по-разному в зависимости от среды:

- **Режим разработки**: Пароль считывается из файла с именем `password.txt`, расположенного в каталоге `secrets`.
- **Производственный режим**: Пароль вводится через консоль. (Удалите файл `password.txt` из каталога `secrets`)

### Структура дерева базы данных KeePass

```
credentials.kdbx
├── suppliers
│   └── aliexpress
│       └── api
│           └── entry (Aliexpress API credentials)
├── openai
│   ├── entry (OpenAI API keys)
│   └── assistants
│       └── entry (OpenAI assistant IDs)
├── gemini
│   └── entry (GoogleAI credentials)
├── telegram
│   └── entry (Telegram credentials)
├── discord
│   └── entry (Discord credentials)
├── prestashop
│   ├── entry (PrestaShop credentials)
│   └── clients
│       └── entry (PrestaShop client credentials)
│   └── translation
│       └── entry (PrestaShop translation credentials)
├── smtp
│   └── entry (SMTP credentials)
├── facebook
│   └── entry (Facebook credentials)
└── google
    └── gapi
        └── entry (Google API credentials)
```

### Глобальный экземпляр `ProgramSettings`

```python
# Global instance of ProgramSettings
gs: ProgramSettings = ProgramSettings()
```

**Зачем это нужно?**

Этот глобальный экземпляр `ProgramSettings` (`gs`) создан для предоставления доступа к настройкам проекта и учетным данным из любого места в коде. Таким образом, вам не нужно создавать новый экземпляр класса `ProgramSettings` каждый раз, когда вам нужно получить доступ к настройкам или учетным данным.

**Как это используется?**

В других модулях проекта вы можете импортировать этот глобальный экземпляр и использовать его для доступа к настройкам и учетным данным:

```python
from src import gs

# Example usage
api_key = gs.credentials.openai.api_key
```

Это упрощает доступ к настройкам и учетным данным, делая код более чистым и удобным в использовании.
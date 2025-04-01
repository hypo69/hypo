# Настройки программы

## Обзор

Этот документ предоставляет обзор класса `ProgramSettings` и связанных с ним функций и методов. Модуль загружает и сохраняет учетные данные (ключи API, пароли и т. д.) из файла базы данных KeePass `credentials.kdbx`. Также он включает функцию `set_project_root` для определения корневого каталога проекта.

## Подробнее

Этот файл является важной частью системы конфигурации проекта, отвечая за загрузку и управление параметрами и учетными данными, необходимыми для работы различных компонентов и сервисов. Он использует KeePass для безопасного хранения конфиденциальной информации, такой как ключи API и пароли.

## Функции

### `set_project_root`

```python
def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Находит корневую директорию проекта, начиная от текущего каталога.
    Поиск идёт вверх по директориям, пока не найдена директория, содержащая один из файлов из списка `marker_files`.

    Args:
        marker_files (tuple): Кортеж строк, представляющих имена файлов или каталогов,
                              которые используются для определения корневой директории проекта.
                              По умолчанию ищутся следующие маркеры: `pyproject.toml`, `requirements.txt`, `.git`.

    Returns:
        Path: Путь к корневой директории проекта, если она найдена, иначе - путь к директории, в которой расположен скрипт.

    Example:
        >>> root_path = set_project_root()
        >>> print(root_path)  # doctest: +SKIP
        /path/to/project
    """
    ...
```

**Описание**: Функция `set_project_root` предназначена для определения корневой директории проекта.

**Как работает функция**: Функция начинает поиск с текущей директории файла и поднимается вверх по дереву директорий, пока не обнаружит директорию, содержащую один из заданных маркерных файлов или директорий (например, `pyproject.toml`, `.git`). Если маркерный файл найден, функция возвращает путь к этой директории. Если ни один из маркерных файлов не найден, функция возвращает путь к директории, в которой расположен текущий скрипт.

**Параметры**:

- `marker_files` (tuple): Кортеж строк, представляющих имена файлов или каталогов, которые используются для определения корневой директории проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:

- `Path`: Путь к корневой директории проекта.

### `singleton`

```python
def singleton(cls):
    """
    Декоратор для создания класса-синглтона.

    Args:
        cls: Класс, который должен быть преобразован в синглтон.

    Returns:
        function: Функция, возвращающая экземпляр класса-синглтона.

    Example:
        >>> @singleton
        ... class MyClass:
        ...     pass
        >>> instance1 = MyClass()
        >>> instance2 = MyClass()
        >>> instance1 is instance2
        True
    """
    ...
```

**Описание**: Декоратор `singleton` используется для реализации паттерна "синглтон".

**Как работает функция**: Декоратор `singleton` принимает класс в качестве аргумента и создает обёртку, которая гарантирует, что у класса будет только один экземпляр. При первом вызове создается экземпляр класса, а при последующих вызовах возвращается тот же экземпляр.

**Параметры**:

- `cls`: Класс, для которого необходимо создать синглтон.

**Возвращает**:

- `function`: Функция, возвращающая экземпляр класса-синглтона.

## Классы

### `ProgramSettings`

```python
class ProgramSettings:
    """
    Класс настроек программы. Устанавливает основные параметры и настройки проекта.
    Загружает конфигурацию из `config.json` и данные учетных данных из файла `credentials.kdbx` в базе данных KeePass.

    Attributes:
        host_name (str): Имя хоста.
        base_dir (Path): Путь к корневой директории проекта.
        config (SimpleNamespace): Объект, содержащий конфигурацию проекта.
        credentials (SimpleNamespace): Объект, содержащий учетные данные.
        MODE (str): Режим работы проекта (например, 'dev', 'prod').
        path (SimpleNamespace): Объект, содержащий пути к различным директориям проекта.

    Methods:
        __init__(self, **kwargs): Инициализирует экземпляр класса.
        _load_credentials(self) -> None: Загружает учетные данные из KeePass.
        _open_kp(self, retry: int = 3) -> PyKeePass | None: Открывает базу данных KeePass.
        _load_aliexpress_credentials(self, kp: PyKeePass) -> bool: Загружает учетные данные Aliexpress из KeePass.
        _load_openai_credentials(self, kp: PyKeePass) -> bool: Загружает учетные данные OpenAI из KeePass.
        _load_gemini_credentials(self, kp: PyKeePass) -> bool: Загружает учетные данные GoogleAI из KeePass.
        _load_telegram_credentials(self, kp: PyKeePass) -> bool: Загружает учетные данные Telegram из KeePass.
        _load_discord_credentials(self, kp: PyKeePass) -> bool: Загружает учетные данные Discord из KeePass.
        _load_PrestaShop_credentials(self, kp: PyKeePass) -> bool: Загружает учетные данные PrestaShop из KeePass.
        _load_presta_translations_credentials(self, kp: PyKeePass) -> bool: Загружает учетные данные PrestaShop Translations из KeePass.
        _load_smtp_credentials(self, kp: PyKeePass) -> bool: Загружает учетные данные SMTP из KeePass.
        _load_facebook_credentials(self, kp: PyKeePass) -> bool: Загружает учетные данные Facebook из KeePass.
        _load_gapi_credentials(self, kp: PyKeePass) -> bool: Загружает учетные данные Google API из KeePass.
        now(self) -> str: Возвращает текущую метку времени в формате, указанном в файле `config.json`.

    Raises:
        BinaryError: Исключение для ошибок с бинарными данными.
        CredentialsError: Исключение для ошибок с данными учетных данных.
        DefaultSettingsException: Исключение для ошибок с настройками по умолчанию.
        HeaderChecksumError: Исключение для ошибок проверки контрольной суммы заголовков.
        KeePassException: Исключение для ошибок с базой данных KeePass.
        PayloadChecksumError: Исключение для ошибок проверки контрольной суммы полезной нагрузки.
        UnableToSendToRecycleBin: Исключение для ошибок отправки в корзину.
        Exception: Общее исключение.

    Example:
        >>> gs = ProgramSettings()
        >>> print(gs.config.project_name)  # doctest: +SKIP
        hypotez
    """
    ...
```

**Описание**: Класс `ProgramSettings` предназначен для управления настройками программы, загрузки конфигурации из `config.json` и учетных данных из базы данных KeePass.

**Как работает класс**: Класс инициализируется с базовыми параметрами, такими как имя хоста и корневая директория проекта. Он загружает конфигурацию из файла `config.json` и учетные данные из базы данных KeePass. Учетные данные загружаются из различных групп и записей в базе данных KeePass и сохраняются в атрибуты объекта `self.credentials`.

**Атрибуты**:

- `host_name` (str): Имя хоста.
- `base_dir` (Path): Путь к корневой директории проекта.
- `config` (SimpleNamespace): Объект, содержащий конфигурацию проекта.
- `credentials` (SimpleNamespace): Объект, содержащий учетные данные.
- `MODE` (str): Режим работы проекта (например, 'dev', 'prod').
- `path` (SimpleNamespace): Объект, содержащий пути к различным директориям проекта.

**Методы**:

- `__init__(self, **kwargs)`:
    - **Описание**: Инициализирует экземпляр класса `ProgramSettings`.
    - **Как работает метод**: Загружает конфигурацию проекта из `config.json`, инициализирует атрибут `path` с путями к различным директориям проекта, вызывает `check_latest_release` для проверки наличия новой версии проекта и загружает учетные данные из `credentials.kdbx`.
- `_load_credentials(self) -> None`:
    - **Описание**: Загружает учетные данные из KeePass.
    - **Как работает метод**: Открывает базу данных KeePass с помощью метода `_open_kp` и загружает учетные данные для различных сервисов (Aliexpress, OpenAI, Gemini, Telegram, Discord, PrestaShop, SMTP, Facebook, Google API) с помощью соответствующих методов `_load_*_credentials`.
- `_open_kp(self, retry: int = 3) -> PyKeePass | None`:
    - **Описание**: Открывает базу данных KeePass.
    - **Как работает метод**: Пытается открыть базу данных KeePass несколько раз (по умолчанию 3 попытки). Пароль для базы данных считывается из файла `password.txt` (если он существует) или запрашивается у пользователя через консоль.
- `_load_aliexpress_credentials(self, kp: PyKeePass) -> bool`:
    - **Описание**: Загружает учетные данные Aliexpress из KeePass.
    - **Как работает метод**: Извлекает учетные данные Aliexpress (api_key, secret, tracking_id, email, password) из базы данных KeePass и сохраняет их в атрибуты объекта `self.credentials.aliexpress`.
- `_load_openai_credentials(self, kp: PyKeePass) -> bool`:
    - **Описание**: Загружает учетные данные OpenAI из KeePass.
    - **Как работает метод**: Извлекает API-ключ OpenAI из базы данных KeePass и сохраняет его в атрибут объекта `self.credentials.openai.api_key`.
- `_load_gemini_credentials(self, kp: PyKeePass) -> bool`:
    - **Описание**: Загружает учетные данные GoogleAI из KeePass.
    - **Как работает метод**: Извлекает API-ключ GoogleAI из базы данных KeePass и сохраняет его в атрибут объекта `self.credentials.gemini.api_key`.
- `_load_telegram_credentials(self, kp: PyKeePass) -> bool`:
    - **Описание**: Загружает учетные данные Telegram из KeePass.
    - **Как работает метод**: Извлекает токен Telegram из базы данных KeePass и сохраняет его в атрибут объекта `self.credentials.telegram.token`.
- `_load_discord_credentials(self, kp: PyKeePass) -> bool`:
    - **Описание**: Загружает учетные данные Discord из KeePass.
    - **Как работает метод**: Извлекает идентификатор приложения Discord, публичный ключ и токен бота из базы данных KeePass и сохраняет их в атрибуты объекта `self.credentials.discord`.
- `_load_PrestaShop_credentials(self, kp: PyKeePass) -> bool`:
    - **Описание**: Загружает учетные данные PrestaShop из KeePass.
    - **Как работает метод**: Извлекает учетные данные PrestaShop (api_key, api_domain, db_server, db_user, db_password) из базы данных KeePass и сохраняет их в атрибуты объекта `self.credentials.presta.client`.
- `_load_presta_translations_credentials(self, kp: PyKeePass) -> bool`:
    - **Описание**: Загружает учетные данные PrestaShop Translations из KeePass.
    - **Как работает метод**: Извлекает учетные данные PrestaShop Translations (server, port, database, user, password) из базы данных KeePass и сохраняет их в атрибуты объекта `self.credentials.presta.translations`.
- `_load_smtp_credentials(self, kp: PyKeePass) -> bool`:
    - **Описание**: Загружает учетные данные SMTP из KeePass.
    - **Как работает метод**: Извлекает учетные данные SMTP (server, port, user, password) из базы данных KeePass и сохраняет их в атрибуты объекта `self.credentials.smtp`.
- `_load_facebook_credentials(self, kp: PyKeePass) -> bool`:
    - **Описание**: Загружает учетные данные Facebook из KeePass.
    - **Как работает метод**: Извлекает учетные данные Facebook (app_id, app_secret, access_token) из базы данных KeePass и сохраняет их в атрибуты объекта `self.credentials.facebook`.
- `_load_gapi_credentials(self, kp: PyKeePass) -> bool`:
    - **Описание**: Загружает учетные данные Google API из KeePass.
    - **Как работает метод**: Извлекает API-ключ Google API из базы данных KeePass и сохраняет его в атрибут объекта `self.credentials.gapi.api_key`.
- `now(self) -> str`:
    - **Описание**: Возвращает текущую метку времени в формате, указанном в файле `config.json`.
    - **Как работает метод**: Возвращает текущую метку времени в формате, указанном в файле `config.json`.

**Возможные исключения**:

- `BinaryError`: Исключение для ошибок с бинарными данными.
- `CredentialsError`: Исключение для ошибок с данными учетных данных.
- `DefaultSettingsException`: Исключение для ошибок с настройками по умолчанию.
- `HeaderChecksumError`: Исключение для ошибок проверки контрольной суммы заголовков.
- `KeePassException`: Исключение для ошибок с базой данных KeePass.
- `PayloadChecksumError`: Исключение для ошибок проверки контрольной суммы полезной нагрузки.
- `UnableToSendToRecycleBin`: Исключение для ошибок отправки в корзину.
- `Exception`: Общее исключение.

## Примечания

- Модуль использует PyKeePass для работы с файлом `credentials.kdbx`.
- В коде присутствуют блоки обработки исключений (`ex`).
- Файл паролей (`password.txt`) содержит пароли в открытом виде. Это потенциальная уязвимость. Необходимо разработать механизм безопасного хранения паролей.

## Инициализация и Настройка

При запуске проект инициализирует и настраивает различные конфигурации и учетные данные. Этот документ объясняет, как эти значения устанавливаются и управляются.

### Определение Корневой Директории Проекта

Проект автоматически определяет свою корневую директорию, ища вверх от текущей директории файла для определенных маркерных файлов (`pyproject.toml`, `requirements.txt`, `.git`). Это гарантирует, что проект может найти свои ресурсы независимо от текущей рабочей директории.

### Загрузка Конфигурации

Проект загружает свои настройки по умолчанию из файла `config.json`, расположенного в директории `src`. Этот JSON-файл содержит различные параметры конфигурации, такие как:

- **Информация об Авторе**: Детали об авторе.
- **Доступные Режимы**: Поддерживаемые режимы (`dev`, `debug`, `test`, `prod`).
- **Пути**: Директории для логов, временных файлов, внешнего хранилища и Google Drive.
- **Детали Проекта**: Название, версия и информация о релизе проекта.

### Управление Учетными Данными с Использованием KeePass

KeePass — это бесплатный и открытый менеджер паролей, который безопасно хранит ваши пароли и другую конфиденциальную информацию в зашифрованной базе данных. База данных защищена мастер-паролем, который является единственным паролем, который вам нужно запомнить. KeePass использует сильные алгоритмы шифрования (такие как AES и Twofish), чтобы гарантировать безопасность ваших данных.

Учетные данные безопасно управляются с использованием базы данных KeePass (`credentials.kdbx`). Мастер-пароль для этой базы данных обрабатывается по-разному в зависимости от среды:

- **Режим Разработки**: Пароль считывается из файла с именем `password.txt`, расположенного в директории `secrets`.
- **Режим Продакшн**: Пароль вводится через консоль. (Удалите файл `password.txt` из директории `secrets`)

Дерево базы данных `credentials.kdbx`:

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

### Подробное описание структуры:

1. **suppliers/aliexpress/api**:
   - Содержит учетные данные для API Aliexpress.
   - Пример записи: `self.credentials.aliexpress.api_key`, `self.credentials.aliexpress.secret`, `self.credentials.aliexpress.tracking_id`, `self.credentials.aliexpress.email`, `self.credentials.aliexpress.password`.

2. **openai**:
   - Содержит API ключи для OpenAI.
   - Пример записи: `self.credentials.openai.api_key`.

3. **openai/assistants**:
   - Содержит идентификаторы ассистентов OpenAI.
   - Пример записи: `self.credentials.openai.assistant_id`.

4. **gemini**:
   - Содержит учетные данные для GoogleAI.
   - Пример записи: `self.credentials.gemini.api_key`.

5. **telegram**:
   - Содержит учетные данные для Telegram.
   - Пример записи: `self.credentials.telegram.token`.

6. **discord**:
   - Содержит учетные данные для Discord.
   - Пример записи: `self.credentials.discord.application_id`, `self.credentials.discord.public_key`, `self.credentials.discord.bot_token`.

7. **prestashop**:
   - Содержит учетные данные для PrestaShop.
   - Пример записи: `self.credentials.presta.client.api_key`, `self.credentials.presta.client.api_domain`, `self.credentials.presta.client.db_server`, `self.credentials.presta.client.db_user`, `self.credentials.presta.client.db_password`.

8. **prestashop/clients**:
   - Содержит учетные данные для клиентов PrestaShop.
   - Пример записи: `self.credentials.presta.client.api_key`, `self.credentials.presta.client.api_domain`, `self.credentials.presta.client.db_server`, `self.credentials.presta.client.db_user`, `self.credentials.presta.client.db_password`.

9. **prestashop/translation**:
   - Содержит учетные данные для переводов PrestaShop.
   - Пример записи: `self.credentials.presta.translations.server`, `self.credentials.presta.translations.port`, `self.credentials.presta.translations.database`, `self.credentials.presta.translations.user`, `self.credentials.presta.translations.password`.

10. **smtp**:
    - Содержит учетные данные для SMTP.
    - Пример записи: `self.credentials.smtp.server`, `self.credentials.smtp.port`, `self.credentials.smtp.user`, `self.credentials.smtp.password`.

11. **facebook**:
    - Содержит учетные данные для Facebook.
    - Пример записи: `self.credentials.facebook.app_id`, `self.credentials.facebook.app_secret`, `self.credentials.facebook.access_token`.

12. **google/gapi**:
    - Содержит учетные данные для Google API.
    - Пример записи: `self.credentials.gapi.api_key`.

### Глобальный Экземпляр `ProgramSettings`

```python
# Global instance of ProgramSettings
gs: ProgramSettings = ProgramSettings()
```

Глобальный экземпляр `ProgramSettings` (`gs`) создается для того, чтобы обеспечить доступ к настройкам и учетным данным проекта из любого места в коде.
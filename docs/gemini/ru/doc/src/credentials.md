# Модуль credentials

## Обзор

Этот модуль содержит настройки проекта, включая пути, пароли, логины и параметры API. Он использует `PyKeePass` для хранения и загрузки учетных данных из базы данных KeePass. Модуль также содержит класс `ProgramSettings` для хранения и управления настройками.

## Классы

### `ProgramSettings`

**Описание**: Класс `ProgramSettings` представляет собой синглтон, хранящий основные параметры и настройки проекта.  Он загружает настройки из файла `config.json` и учетные данные из базы данных `credentials.kdbx`.

**Параметры**:

- `host_name` (str): Имя хоста.
- `base_dir` (Path): Корневая директория проекта, автоматически определяется при инициализации.
- `config` (SimpleNamespace): Объект настроек, полученный из `config.json`.
- `credentials` (SimpleNamespace): Объект с учетными данными из `credentials.kdbx`, содержащий отдельные поля для различных сервисов (Aliexpress, PrestaShop, OpenAI, Gemini, Rev.com, ShutterStock, Discord, Telegram, SMTP, Facebook, GAPI).  Структура вложенных `SimpleNamespace` отражает иерархию данных в базе данных.
- `MODE` (str): Режим работы (например, 'dev', 'prod').
- `path` (SimpleNamespace): Объект с путями к различным папкам проекта.

**Методы**:

- `__init__(self, **kwargs)`: Инициализирует экземпляр класса. Загружает настройки из файла `config.json` и учетные данные из `credentials.kdbx`. Выполняет валидацию и инициализацию путей к важным директориям (bin, src, secrets, log, tmp, data, google_drive, external_storage, tools).
- `_load_credentials()`: Загружает учетные данные из базы данных KeePass. Вызывает ряд вспомогательных методов для загрузки конкретных учетных данных.
- `_open_kp(self, retry: int = 3) -> PyKeePass | None`: Открывает базу данных KeePass. При ошибке пытается повторить попытку `retry` раз.
- `_load_aliexpress_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные Aliexpress из базы данных KeePass.
- `_load_openai_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные OpenAI из базы данных KeePass.
- `_load_gemini_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные Gemini из базы данных KeePass.
- `_load_discord_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные Discord из базы данных KeePass.
- `_load_telegram_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные Telegram из базы данных KeePass.
- `_load_PrestaShop_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные PrestaShop из базы данных KeePass.
- `_load_presta_translations_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные для переводов PrestaShop.
- `_load_smtp_credentials(self, kp: PyKeePass) -> bool`: Загружает SMTP учетные данные.
- `_load_facebook_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные Facebook.
- `_load_gapi_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные GAPI.


- `now(self) -> str`: Возвращает текущую метку времени в заданном формате.


**Вызывает исключения**:

- `BinaryError`: Ошибка, связанная с бинарными данными.
- `CredentialsError`: Ошибка при работе с учетными данными.
- `DefaultSettingsException`: Ошибка при использовании дефолтных настроек.
- `HeaderChecksumError`: Ошибка проверки контрольной суммы заголовка.
- `KeePassException`: Общая ошибка при работе с KeePass.
- `PayloadChecksumError`: Ошибка проверки контрольной суммы полезной нагрузки.
- `UnableToSendToRecycleBin`: Ошибка отправки файла в корзину.


## Функции

### `set_project_root(marker_files=(\'pyproject.toml\', \'requirements.txt\', \'.git\')) -> Path`

**Описание**: Находит корневую директорию проекта, начиная от текущего файла. Поиск идёт вверх по директориям, пока не будет найдена директория, содержащая один из файлов или папок из списка `marker_files`.

**Параметры**:

- `marker_files` (tuple): Список файлов или папок, по которым определяется корневая директория проекта.

**Возвращает**:

- `Path`: Путь к корневой директории проекта, либо директория, в которой расположен текущий файл.

### `singleton(cls)`

**Описание**: Декоратор для реализации паттерна Singleton.


**Параметры**:

- `cls`: Класс, который нужно сделать синглтоном.


**Возвращает**:

- Функцию-обертку, которая возвращает единственный экземпляр класса.
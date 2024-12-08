# Модуль `hypotez/src/credentials.py`

## Обзор

Этот модуль содержит класс `ProgramSettings`, реализующий паттерн Singleton для хранения глобальных настроек проекта.  Класс загружает и хранит информацию об учетных данных (API ключи, пароли и т.д.) из файла `credentials.kdbx` базы данных KeePass.  Также содержит функцию `set_project_root` для поиска корневой директории проекта.


## Функции

### `set_project_root`

**Описание**: Находит корневую директорию проекта, начиная от текущего каталога. Поиск идёт вверх по директориям, пока не найдена директория, содержащая один из файлов из списка `marker_files`.

**Параметры**:

- `marker_files` (tuple): Кортеж строк, представляющих имена файлов или каталогов, которые используются для определения корневой директории проекта.

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если она найдена, иначе - путь к директории, в которой расположен скрипт.


### `singleton`

**Описание**: Декоратор для создания класса-синглтона.

**Параметры**:

- `cls`: Класс, который должен быть преобразован в синглтон.

**Возвращает**:

- `function`: Функция, возвращающая экземпляр класса-синглтона.


## Классы

### `ProgramSettings`

**Описание**: Класс настроек программы. Представляет собой синглтон, хранящий основные параметры и настройки проекта.  Загружает конфигурацию из `config.json` и данные учетных данных из файла `credentials.kdbx` в базе данных KeePass.


**Атрибуты**:

- `host_name` (str): Имя хоста.
- `base_dir` (Path): Путь к корневой директории проекта.
- `config` (SimpleNamespace): Объект, содержащий конфигурацию проекта.
- `credentials` (SimpleNamespace): Объект, содержащий учетные данные.
- `MODE` (str): Режим работы проекта (например, 'dev', 'prod').
- `path` (SimpleNamespace): Объект, содержащий пути к различным директориям проекта.


**Методы**:

- `__init__(self, **kwargs)`: Инициализирует экземпляр класса.
    - Загружает конфигурацию проекта из `config.json`
    - Инициализирует атрибут `path` с путями к различным директориям проекта.
    - Вызывает `check_latest_release` для проверки на наличие новой версии проекта.
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
- `now(self, dformat: str = '%y_%m_%d_%H_%M_%S_%f') -> str`: Возвращает текущую метку времени в заданном формате.

**Возможные исключения**:

- `BinaryError`: Исключение для ошибок с бинарными данными.
- `CredentialsError`: Исключение для ошибок с данными учетных данных.
- `DefaultSettingsException`: Исключение для ошибок с настройками по умолчанию.
- `HeaderChecksumError`: Исключение для ошибок проверки контрольной суммы заголовков.
- `KeePassException`: Исключение для ошибок с базой данных KeePass.
- `PayloadChecksumError`: Исключение для ошибок проверки контрольной суммы полезной нагрузки.
- `UnableToSendToRecycleBin`: Исключение для ошибок отправки в корзину.
- `Exception`: Общее исключение.

##  Примечания

- Модуль использует PyKeePass для работы с файлом `credentials.kdbx`.
-  В коде присутствуют блоки обработки исключений (`ex`).
- Файл паролей (`password.txt`) содержит пароли в открытом виде.  Это потенциальная уязвимость. Необходимо разработать механизм безопасного хранения паролей.
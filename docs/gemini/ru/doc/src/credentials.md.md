# `src.credentials`

## Обзор

Модуль `src.credentials` предоставляет класс `ProgramSettings`, который загружает и хранит информацию о учетных данных (ключи API, пароли и т.д.) из файла базы данных KeePass `credentials.kdbx`. Он также включает функцию `set_project_root` для определения корневого каталога проекта.

## Содержание

- [Обзор](#обзор)
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
- [Примечания](#примечания)
- [Инициализация и конфигурация](#инициализация-и-конфигурация)
    - [Определение корневого каталога проекта](#определение-корневого-каталога-проекта)
    - [Загрузка конфигурации](#загрузка-конфигурации)
    - [Управление учетными данными с помощью KeePass](#управление-учетными-данными-с-помощью-keepass)
    - [Структура дерева базы данных KeePass](#структура-дерева-базы-данных-keepass)
    - [Подробное описание структуры](#подробное-описание-структуры)
    - [Глобальный экземпляр `ProgramSettings`](#глобальный-экземпляр-programsettings)

## Функции

### `set_project_root`

**Описание**: Находит корневой каталог проекта, начиная с текущего каталога. Поиск идет вверх по каталогам, пока не будет найден каталог, содержащий один из файлов из списка `marker_files`.

**Параметры**:

- `marker_files` (tuple): Кортеж строк, представляющих имена файлов или каталогов, используемых для идентификации корневого каталога проекта. По умолчанию ищет следующие маркеры: `pyproject.toml`, `requirements.txt`, `.git`.

**Возвращает**:

- `Path`: Путь к корневому каталогу проекта, если он найден, в противном случае путь к каталогу, где находится скрипт.

```python
def set_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Finds the project's root directory starting from the current file directory,
    searching upwards and stopping at the first directory containing any of the marker files.
    
    Args:
        marker_files (tuple): File or directory names for identifying the project's root directory.
    
    Returns:
        Path: The path to the root directory if found, otherwise the directory where the script is located.
    """
    __root__:Path
    current_path:Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__
```

### `singleton`

**Описание**: Декоратор для создания класса-одиночки (singleton).

**Параметры**:

- `cls`: Класс, который должен быть преобразован в singleton.

**Возвращает**:

- `function`: Функция, возвращающая экземпляр singleton-класса.

```python
def singleton(cls):
    """ A decorator to create a singleton class """
    instances = {}
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance
```

## Классы

### `ProgramSettings`

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
- `_load_presta_translations_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные переводов PrestaShop из KeePass.
- `_load_smtp_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные SMTP из KeePass.
- `_load_facebook_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные Facebook из KeePass.
- `_load_gapi_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные Google API из KeePass.
- `now(self) -> str`: Возвращает текущую метку времени в формате, указанном в файле `config.json`.

**Возможные исключения**:

- `BinaryError`: Исключение для ошибок двоичных данных.
- `CredentialsError`: Исключение для ошибок данных учетных данных.
- `DefaultSettingsException`: Исключение для ошибок настроек по умолчанию.
- `HeaderChecksumError`: Исключение для ошибок контрольной суммы заголовка.
- `KeePassException`: Исключение для ошибок базы данных KeePass.
- `PayloadChecksumError`: Исключение для ошибок контрольной суммы полезной нагрузки.
- `UnableToSendToRecycleBin`: Исключение для ошибок отправки в корзину.
- `Exception`: Общее исключение.

#### `__init__`

**Описание**: Инициализирует экземпляр класса `ProgramSettings`.

**Параметры**:

- `kwargs` (dict): Произвольные ключевые аргументы.

**Возвращает**:

- `None`

```python
def __init__(self, **kwargs):
    """Initialisation"""
    self.host_name = platform.node()
    self.base_dir = set_project_root()

    self.config = j_loads_ns(self.base_dir / 'src' / 'config.json')
    if not self.config:
        logger.error('Error loading settings')
        # TODO add exit
        # sys.exit()
        return
    self.config.project_name = self.base_dir.name

    self.path = SimpleNamespace()
    self.path.root = self.base_dir
    self.path.src = self.base_dir / 'src'
    self.path.assets = self.base_dir / 'assets'
    self.path.logs = self.base_dir / 'logs'
    self.path.tmp = self.base_dir / 'tmp'
    self.path.external = self.base_dir / 'external'
    self.path.secrets = self.base_dir / 'secrets'
    self.path.gdrive = self.config.paths.gdrive_path or self.base_dir / 'gdrive'
    
    # check for new release
    if (self.MODE := self.config.MODE) == "prod":
        if new_release := check_latest_release(self.config):
             print(new_release)
             #sys.exit()

    self.credentials = SimpleNamespace()
    self._load_credentials()
```

#### `_load_credentials`

**Описание**: Загружает учетные данные из KeePass.

**Параметры**:

- `None`

**Возвращает**:

- `None`

```python
def _load_credentials(self) -> None:
    """ Loads credentials from KeePass """
    kp: PyKeePass | None = self._open_kp()
    if not kp:
        return
    self.credentials.aliexpress = SimpleNamespace()
    self._load_aliexpress_credentials(kp)
    self.credentials.openai = SimpleNamespace()
    self._load_openai_credentials(kp)
    self.credentials.gemini = SimpleNamespace()
    self._load_gemini_credentials(kp)
    self.credentials.telegram = SimpleNamespace()
    self._load_telegram_credentials(kp)
    self.credentials.discord = SimpleNamespace()
    self._load_discord_credentials(kp)
    self.credentials.presta = SimpleNamespace()
    self._load_PrestaShop_credentials(kp)
    self.credentials.presta.translations = SimpleNamespace()
    self._load_presta_translations_credentials(kp)
    self.credentials.smtp = SimpleNamespace()
    self._load_smtp_credentials(kp)
    self.credentials.facebook = SimpleNamespace()
    self._load_facebook_credentials(kp)
    self.credentials.gapi = SimpleNamespace()
    self._load_gapi_credentials(kp)
```

#### `_open_kp`

**Описание**: Открывает базу данных KeePass.

**Параметры**:

- `retry` (int, optional): Количество попыток. По умолчанию 3.

**Возвращает**:

- `PyKeePass | None`: Объект базы данных PyKeePass или `None`, если не удалось открыть базу данных.

```python
def _open_kp(self, retry: int = 3) -> PyKeePass | None:
    """ Opens the KeePass database
    Args:
        retry (int): Number of retries
    """
    while retry > 0:
        try:
            password:str = Path( self.path.secrets / 'password.txt').read_text(encoding="utf-8") or None
            kp = PyKeePass(str(self.path.secrets / 'credentials.kdbx'), 
                           password = password or getpass.getpass(print('Enter KeePass master password: ').lower()))
            return kp
        except Exception as ex:
            print(f"Failed to open KeePass database. Exception: {ex}, {retry-1} retries left.")
            #logger.exception(ex)
            retry -= 1
            if retry < 1:
                logger.critical('Failed to open KeePass database after multiple attempts', exc_info=True)
                # TODO add exit
                # sys.exit()
                return
```

#### `_load_aliexpress_credentials`

**Описание**: Загружает учетные данные Aliexpress из KeePass.

**Параметры**:

- `kp` (PyKeePass): Объект базы данных PyKeePass.

**Возвращает**:

- `bool`: `True`, если учетные данные загружены, в противном случае `False`.

```python
def _load_aliexpress_credentials(self, kp: PyKeePass) -> bool:
    """ Loads Aliexpress credentials from KeePass"""
    try:
        group = kp.find_groups(name='aliexpress')[0]
        entry = group.find_entries(title='api')[0]
        self.credentials.aliexpress.api_key = entry.get_custom_property('api_key')
        self.credentials.aliexpress.secret = entry.get_custom_property('secret')
        self.credentials.aliexpress.tracking_id = entry.get_custom_property('tracking_id')
        self.credentials.aliexpress.email = entry.username
        self.credentials.aliexpress.password = entry.password
        return True
    except Exception as ex:
        logger.error(f"Error loading aliexpress credentials: {ex}")
        return False
```

#### `_load_openai_credentials`

**Описание**: Загружает учетные данные OpenAI из KeePass.

**Параметры**:

- `kp` (PyKeePass): Объект базы данных PyKeePass.

**Возвращает**:

- `bool`: `True`, если учетные данные загружены, в противном случае `False`.

```python
def _load_openai_credentials(self, kp: PyKeePass) -> bool:
    """ Loads OpenAI credentials from KeePass"""
    try:
        group = kp.find_groups(name='openai')[0]
        entry = group.find_entries(title='entry')[0]
        self.credentials.openai.api_key = entry.get_custom_property('api_key')

        group = kp.find_groups(name='assistants')[0]
        entry = group.find_entries(title='entry')[0]
        self.credentials.openai.assistant_id = entry.get_custom_property('assistant_id')
        return True
    except Exception as ex:
        logger.error(f"Error loading openai credentials: {ex}")
        return False
```

#### `_load_gemini_credentials`

**Описание**: Загружает учетные данные GoogleAI из KeePass.

**Параметры**:

- `kp` (PyKeePass): Объект базы данных PyKeePass.

**Возвращает**:

- `bool`: `True`, если учетные данные загружены, в противном случае `False`.

```python
def _load_gemini_credentials(self, kp: PyKeePass) -> bool:
    """ Loads GoogleAI credentials from KeePass"""
    try:
        group = kp.find_groups(name='gemini')[0]
        entry = group.find_entries(title='entry')[0]
        self.credentials.gemini.api_key = entry.get_custom_property('api_key')
        return True
    except Exception as ex:
        logger.error(f"Error loading gemini credentials: {ex}")
        return False
```

#### `_load_telegram_credentials`

**Описание**: Загружает учетные данные Telegram из KeePass.

**Параметры**:

- `kp` (PyKeePass): Объект базы данных PyKeePass.

**Возвращает**:

- `bool`: `True`, если учетные данные загружены, в противном случае `False`.

```python
def _load_telegram_credentials(self, kp: PyKeePass) -> bool:
    """ Loads Telegram credentials from KeePass"""
    try:
        group = kp.find_groups(name='telegram')[0]
        entry = group.find_entries(title='entry')[0]
        self.credentials.telegram.token = entry.get_custom_property('token')
        return True
    except Exception as ex:
        logger.error(f"Error loading telegram credentials: {ex}")
        return False
```

#### `_load_discord_credentials`

**Описание**: Загружает учетные данные Discord из KeePass.

**Параметры**:

- `kp` (PyKeePass): Объект базы данных PyKeePass.

**Возвращает**:

- `bool`: `True`, если учетные данные загружены, в противном случае `False`.

```python
def _load_discord_credentials(self, kp: PyKeePass) -> bool:
    """ Loads Discord credentials from KeePass"""
    try:
        group = kp.find_groups(name='discord')[0]
        entry = group.find_entries(title='entry')[0]
        self.credentials.discord.application_id = entry.get_custom_property('application_id')
        self.credentials.discord.public_key = entry.get_custom_property('public_key')
        self.credentials.discord.bot_token = entry.get_custom_property('bot_token')
        return True
    except Exception as ex:
        logger.error(f"Error loading discord credentials: {ex}")
        return False
```

#### `_load_PrestaShop_credentials`

**Описание**: Загружает учетные данные PrestaShop из KeePass.

**Параметры**:

- `kp` (PyKeePass): Объект базы данных PyKeePass.

**Возвращает**:

- `bool`: `True`, если учетные данные загружены, в противном случае `False`.

```python
def _load_PrestaShop_credentials(self, kp: PyKeePass) -> bool:
    """ Loads PrestaShop credentials from KeePass"""
    try:
        group = kp.find_groups(name='prestashop')[0]
        entry = group.find_entries(title='entry')[0]
        self.credentials.presta.client = SimpleNamespace()
        self.credentials.presta.client.api_key = entry.get_custom_property('api_key')
        self.credentials.presta.client.api_domain = entry.get_custom_property('api_domain')
        self.credentials.presta.client.db_server = entry.get_custom_property('db_server')
        self.credentials.presta.client.db_user = entry.get_custom_property('db_user')
        self.credentials.presta.client.db_password = entry.get_custom_property('db_password')
        return True
    except Exception as ex:
        logger.error(f"Error loading PrestaShop credentials: {ex}")
        return False
```

#### `_load_presta_translations_credentials`

**Описание**: Загружает учетные данные переводов PrestaShop из KeePass.

**Параметры**:

- `kp` (PyKeePass): Объект базы данных PyKeePass.

**Возвращает**:

- `bool`: `True`, если учетные данные загружены, в противном случае `False`.

```python
def _load_presta_translations_credentials(self, kp: PyKeePass) -> bool:
    """ Loads PrestaShop Translations credentials from KeePass"""
    try:
        group = kp.find_groups(name='translation')[0]
        entry = group.find_entries(title='entry')[0]
        self.credentials.presta.translations.server = entry.get_custom_property('server')
        self.credentials.presta.translations.port = entry.get_custom_property('port')
        self.credentials.presta.translations.database = entry.get_custom_property('database')
        self.credentials.presta.translations.user = entry.get_custom_property('user')
        self.credentials.presta.translations.password = entry.get_custom_property('password')
        return True
    except Exception as ex:
        logger.error(f"Error loading PrestaShop translations credentials: {ex}")
        return False
```

#### `_load_smtp_credentials`

**Описание**: Загружает учетные данные SMTP из KeePass.

**Параметры**:

- `kp` (PyKeePass): Объект базы данных PyKeePass.

**Возвращает**:

- `bool`: `True`, если учетные данные загружены, в противном случае `False`.

```python
def _load_smtp_credentials(self, kp: PyKeePass) -> bool:
    """ Loads SMTP credentials from KeePass"""
    try:
        group = kp.find_groups(name='smtp')[0]
        entry = group.find_entries(title='entry')[0]
        self.credentials.smtp.server = entry.get_custom_property('server')
        self.credentials.smtp.port = entry.get_custom_property('port')
        self.credentials.smtp.user = entry.get_custom_property('user')
        self.credentials.smtp.password = entry.get_custom_property('password')
        return True
    except Exception as ex:
        logger.error(f"Error loading smtp credentials: {ex}")
        return False
```

#### `_load_facebook_credentials`

**Описание**: Загружает учетные данные Facebook из KeePass.

**Параметры**:

- `kp` (PyKeePass): Объект базы данных PyKeePass.

**Возвращает**:

- `bool`: `True`, если учетные данные загружены, в противном случае `False`.

```python
def _load_facebook_credentials(self, kp: PyKeePass) -> bool:
    """ Loads Facebook credentials from KeePass"""
    try:
        group = kp.find_groups(name='facebook')[0]
        entry = group.find_entries(title='entry')[0]
        self.credentials.facebook.app_id = entry.get_custom_property('app_id')
        self.credentials.facebook.app_secret = entry.get_custom_property('app_secret')
        self.credentials.facebook.access_token = entry.get_custom_property('access_token')
        return True
    except Exception as ex:
        logger.error(f"Error loading facebook credentials: {ex}")
        return False
```

#### `_load_gapi_credentials`

**Описание**: Загружает учетные данные Google API из KeePass.

**Параметры**:

- `kp` (PyKeePass): Объект базы данных PyKeePass.

**Возвращает**:

- `bool`: `True`, если учетные данные загружены, в противном случае `False`.

```python
def _load_gapi_credentials(self, kp: PyKeePass) -> bool:
    """ Loads Google API credentials from KeePass"""
    try:
        group = kp.find_groups(name='google')[0]
        group = group.find_groups(name='gapi')[0]
        entry = group.find_entries(title='entry')[0]
        self.credentials.gapi.api_key = entry.get_custom_property('api_key')
        return True
    except Exception as ex:
        logger.error(f"Error loading google api credentials: {ex}")
        return False
```

#### `now`

**Описание**: Возвращает текущую метку времени в формате, указанном в файле `config.json`.

**Параметры**:

- `None`

**Возвращает**:

- `str`: Текущая метка времени в формате из `config.json`.

```python
def now(self) -> str:
    """Returns the current timestamp in the format specified in the config.json file."""
    return datetime.now().strftime(self.config.timestamp_format)
```

## Примечания

- Модуль использует `PyKeePass` для работы с файлом `credentials.kdbx`.
- Блоки обработки исключений (`ex`) присутствуют в коде.
- Файл паролей (`password.txt`) содержит пароли в открытом виде. Это потенциальная уязвимость. Необходимо разработать безопасный механизм хранения паролей.

## Инициализация и конфигурация

Когда проект запускается, он инициализирует и настраивает различные параметры и учетные данные. Этот документ объясняет, как эти значения устанавливаются и управляются.

### Определение корневого каталога проекта

Проект автоматически определяет свой корневой каталог, ища вверх от текущего каталога файла определенные маркерные файлы (`pyproject.toml`, `requirements.txt`, `.git`). Это гарантирует, что проект сможет найти свои ресурсы независимо от текущего рабочего каталога.

```python
def set_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Finds the project's root directory starting from the current file directory,
    searching upwards and stopping at the first directory containing any of the marker files.
    
    Args:
        marker_files (tuple): File or directory names for identifying the project's root directory.
    
    Returns:
        Path: The path to the root directory if found, otherwise the directory where the script is located.
    """
    __root__:Path
    current_path:Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__
```

### Загрузка конфигурации

Проект загружает свои настройки по умолчанию из файла `config.json`, расположенного в каталоге `src`. Этот файл JSON содержит различные параметры конфигурации, такие как:

- **Информация об авторе**: Детали об авторе.
- **Доступные режимы**: Поддерживаемые режимы (`dev`, `debug`, `test`, `prod`).
- **Пути**: Каталоги для журналов, временных файлов, внешнего хранилища и Google Drive.
- **Детали проекта**: Название, версия и информация о релизе проекта.

```python
self.config = j_loads_ns(self.base_dir / 'src' / 'config.json')
if not self.config:
    logger.error('Error loading settings')
    ...
    return

self.config.project_name = self.base_dir.name
```

### Управление учетными данными с помощью KeePass

**Что такое KeePass?**

KeePass — это бесплатный менеджер паролей с открытым исходным кодом, который надежно хранит ваши пароли и другую конфиденциальную информацию в зашифрованной базе данных. База данных защищена мастер-паролем, который является единственным паролем, который вам нужно запомнить. KeePass использует надежные алгоритмы шифрования (такие как AES и Twofish) для обеспечения безопасности ваших данных.

**Почему KeePass хорош?**

- **Безопасность**: KeePass использует стандартное шифрование для защиты ваших данных, что делает его очень безопасным от несанкционированного доступа.
- **Переносимость**: Вы можете хранить свою базу данных KeePass на USB-накопителе или в облачном хранилище и получать к ней доступ с нескольких устройств.
- **Настройка**: KeePass позволяет организовать ваши пароли в группы и подгруппы, что упрощает управление большим количеством учетных данных.
- **Открытый исходный код**: Будучи проектом с открытым исходным кодом, KeePass является прозрачным и может быть проверен сообществом на предмет безопасности.

**Как KeePass работает в этом проекте**

Учетные данные надежно управляются с помощью базы данных KeePass (`credentials.kdbx`). Мастер-пароль для этой базы данных обрабатывается по-разному в зависимости от среды:

- **Режим разработки**: Пароль считывается из файла с именем `password.txt`, расположенного в каталоге `secrets`.
- **Рабочий режим**: Пароль вводится через консоль. (Удалите файл `password.txt` из каталога `secrets`).

```python
def _open_kp(self, retry: int = 3) -> PyKeePass | None:
    """ Opens the KeePass database
    Args:
        retry (int): Number of retries
    """
    while retry > 0:
        try:
            password:str = Path( self.path.secrets / 'password.txt').read_text(encoding="utf-8") or None
            kp = PyKeePass(str(self.path.secrets / 'credentials.kdbx'), 
                           password = password or getpass.getpass(print('Enter KeePass master password: ').lower()))
            return kp
        except Exception as ex:
            print(f"Failed to open KeePass database. Exception: {ex}, {retry-1} retries left.")
            ...
            retry -= 1
            if retry < 1:
                logger.critical('Failed to open KeePass database after multiple attempts', exc_info=True)
                ...
                sys.exit()
```

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

### Подробное описание структуры:

1.  **suppliers/aliexpress/api**:
    - Содержит учетные данные API Aliexpress.
    - Пример записи: `self.credentials.aliexpress.api_key`, `self.credentials.aliexpress.secret`, `self.credentials.aliexpress.tracking_id`, `self.credentials.aliexpress.email`, `self.credentials.aliexpress.password`.

2.  **openai**:
    - Содержит ключи API OpenAI.
    - Пример записи: `self.credentials.openai.api_key`.

3.  **openai/assistants**:
    - Содержит идентификаторы ассистентов OpenAI.
    - Пример записи: `self.credentials.openai.assistant_id`.

4.  **gemini**:
    - Содержит учетные данные GoogleAI.
    - Пример записи: `self.credentials.gemini.api_key`.

5.  **telegram**:
    - Содержит учетные данные Telegram.
    - Пример записи: `self.credentials.telegram.token`.

6.  **discord**:
    - Содержит учетные данные Discord.
    - Пример записи: `self.credentials.discord.application_id`, `self.credentials.discord.public_key`, `self.credentials.discord.bot_token`.

7.  **prestashop**:
    - Содержит учетные данные PrestaShop.
    - Пример записи: `self.credentials.presta.client.api_key`, `self.credentials.presta.client.api_domain`, `self.credentials.presta.client.db_server`, `self.credentials.presta.client.db_user`, `self.credentials.presta.client.db_password`.

8.  **prestashop/clients**:
    - Содержит учетные данные клиента PrestaShop.
    - Пример записи: `self.credentials.presta.client.api_key`, `self.credentials.presta.client.api_domain`, `self.credentials.presta.client.db_server`, `self.credentials.presta.client.db_user`, `self.credentials.presta.client.db_password`.

9.  **prestashop/translation**:
    - Содержит учетные данные перевода PrestaShop.
    - Пример записи: `self.credentials.presta.translations.server`, `self.credentials.presta.translations.port`, `self.credentials.presta.translations.database`, `self.credentials.presta.translations.user`, `self.credentials.presta.translations.password`.

10. **smtp**:
    - Содержит учетные данные SMTP.
    - Пример записи: `self.credentials.smtp.server`, `self.credentials.smtp.port`, `self.credentials.smtp.user`, `self.credentials.smtp.password`.

11. **facebook**:
    - Содержит учетные данные Facebook.
    - Пример записи: `self.credentials.facebook.app_id`, `self.credentials.facebook.app_secret`, `self.credentials.facebook.access_token`.

12. **google/gapi**:
    - Содержит учетные данные Google API.
    - Пример записи: `self.credentials.gapi.api_key`.

### Примечания:

- Каждая группа (`group`) в KeePass соответствует определенному пути (`path`).
- Каждая запись (`entry`) в группе содержит определенные учетные данные.
- Методы `_load_*_credentials` загружают данные из соответствующих групп и записей в базе данных KeePass и сохраняют их в атрибутах объекта `self.credentials`.

### Глобальный экземпляр `ProgramSettings`

```python
# Global instance of ProgramSettings
gs: ProgramSettings = ProgramSettings()
```

**Почему это нужно?**

Этот глобальный экземпляр `ProgramSettings` (`gs`) создается для обеспечения доступа к настройкам проекта и учетным данным из любой точки кода. Таким образом, вам не нужно создавать новый экземпляр класса `ProgramSettings` каждый раз, когда вам нужно получить доступ к настройкам или учетным данным.

**Как это используется?**

В
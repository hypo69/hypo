# src.credentials

## Обзор

Этот документ предоставляет обзор класса `ProgramSettings`.

`ProgramSettings` загружает и хранит учетные данные (ключи API, пароли и т. д.) из файла базы данных KeePass `credentials.kdbx`. Он также включает функцию `set_project_root` для определения корневого каталога проекта.

## Оглавление

- [Функции](#Функции)
    - [`set_project_root`](#set_project_root)
    - [`singleton`](#singleton)
- [Классы](#Классы)
    - [`ProgramSettings`](#ProgramSettings)
    - [Методы класса `ProgramSettings`](#Методы-класса-ProgramSettings)
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
- [Примечания](#Примечания)
- [Инициализация и конфигурация](#Инициализация-и-конфигурация)
- [Определение корневого каталога проекта](#Определение-корневого-каталога-проекта)
- [Загрузка конфигурации](#Загрузка-конфигурации)
- [Управление учетными данными с помощью KeePass](#Управление-учетными-данными-с-помощью-KeePass)
- [Структура дерева базы данных KeePass](#Структура-дерева-базы-данных-KeePass)
- [Подробное описание структуры](#Подробное-описание-структуры)
- [Глобальный экземпляр `ProgramSettings`](#Глобальный-экземпляр-ProgramSettings)

## Функции

### `set_project_root`

**Описание**: Находит корневой каталог проекта, начиная с текущего каталога. Поиск идет вверх по каталогам, пока не будет найден каталог, содержащий один из файлов в списке `marker_files`.

**Параметры**:

- `marker_files` (tuple): Кортеж строк, представляющих имена файлов или каталогов, используемых для идентификации корневого каталога проекта. По умолчанию, он ищет следующие маркеры: `pyproject.toml`, `requirements.txt`, `.git`.

**Возвращает**:

- `Path`: Путь к корневому каталогу проекта, если он найден, в противном случае путь к каталогу, где расположен скрипт.

### `singleton`

**Описание**: Декоратор для создания singleton класса.

**Параметры**:

- `cls`: Класс, который должен быть преобразован в singleton.

**Возвращает**:

- `function`: Функция, которая возвращает экземпляр singleton класса.

## Классы

### `ProgramSettings`

**Описание**: Класс для настроек программы. Он устанавливает основные параметры и настройки проекта. Он загружает конфигурацию из `config.json` и данные учетных данных из файла базы данных KeePass `credentials.kdbx`.

**Атрибуты**:

- `host_name` (str): Имя хоста.
- `base_dir` (Path): Путь к корневому каталогу проекта.
- `config` (SimpleNamespace): Объект, содержащий конфигурацию проекта.
- `credentials` (SimpleNamespace): Объект, содержащий учетные данные.
- `MODE` (str): Режим работы проекта (например, 'dev', 'prod').
- `path` (SimpleNamespace): Объект, содержащий пути к различным каталогам проекта.

### Методы класса `ProgramSettings`

#### `__init__`

**Описание**: Инициализирует экземпляр класса.

- Загружает конфигурацию проекта из `config.json`.
- Инициализирует атрибут `path` путями к различным каталогам проекта.
- Вызывает `check_latest_release` для проверки новой версии проекта.
- Загружает учетные данные из `credentials.kdbx`.

**Параметры**:

- `**kwargs` (dict): Произвольные именованные аргументы.

**Возвращает**:

- `None`

#### `_load_credentials`

**Описание**: Загружает учетные данные из KeePass.

**Параметры**:

- `None`

**Возвращает**:

- `None`

#### `_open_kp`

**Описание**: Открывает базу данных KeePass. Обрабатывает возможные исключения при открытии базы данных.

**Параметры**:

- `retry` (int, optional): Количество попыток. По умолчанию `3`.

**Возвращает**:

- `PyKeePass | None`: Объект `PyKeePass` если база данных открыта успешно, иначе `None`.

#### `_load_aliexpress_credentials`

**Описание**: Загружает учетные данные Aliexpress из KeePass.

**Параметры**:

- `kp` (PyKeePass): Объект `PyKeePass` для работы с базой данных.

**Возвращает**:

- `bool`: `True` если данные загружены успешно, `False` если произошла ошибка.

#### `_load_openai_credentials`

**Описание**: Загружает учетные данные OpenAI из KeePass.

**Параметры**:

- `kp` (PyKeePass): Объект `PyKeePass` для работы с базой данных.

**Возвращает**:

- `bool`: `True` если данные загружены успешно, `False` если произошла ошибка.

#### `_load_gemini_credentials`

**Описание**: Загружает учетные данные GoogleAI из KeePass.

**Параметры**:

- `kp` (PyKeePass): Объект `PyKeePass` для работы с базой данных.

**Возвращает**:

- `bool`: `True` если данные загружены успешно, `False` если произошла ошибка.

#### `_load_telegram_credentials`

**Описание**: Загружает учетные данные Telegram из KeePass.

**Параметры**:

- `kp` (PyKeePass): Объект `PyKeePass` для работы с базой данных.

**Возвращает**:

- `bool`: `True` если данные загружены успешно, `False` если произошла ошибка.

#### `_load_discord_credentials`

**Описание**: Загружает учетные данные Discord из KeePass.

**Параметры**:

- `kp` (PyKeePass): Объект `PyKeePass` для работы с базой данных.

**Возвращает**:

- `bool`: `True` если данные загружены успешно, `False` если произошла ошибка.

#### `_load_PrestaShop_credentials`

**Описание**: Загружает учетные данные PrestaShop из KeePass.

**Параметры**:

- `kp` (PyKeePass): Объект `PyKeePass` для работы с базой данных.

**Возвращает**:

- `bool`: `True` если данные загружены успешно, `False` если произошла ошибка.

#### `_load_presta_translations_credentials`

**Описание**: Загружает учетные данные PrestaShop Translations из KeePass.

**Параметры**:

- `kp` (PyKeePass): Объект `PyKeePass` для работы с базой данных.

**Возвращает**:

- `bool`: `True` если данные загружены успешно, `False` если произошла ошибка.

#### `_load_smtp_credentials`

**Описание**: Загружает учетные данные SMTP из KeePass.

**Параметры**:

- `kp` (PyKeePass): Объект `PyKeePass` для работы с базой данных.

**Возвращает**:

- `bool`: `True` если данные загружены успешно, `False` если произошла ошибка.

#### `_load_facebook_credentials`

**Описание**: Загружает учетные данные Facebook из KeePass.

**Параметры**:

- `kp` (PyKeePass): Объект `PyKeePass` для работы с базой данных.

**Возвращает**:

- `bool`: `True` если данные загружены успешно, `False` если произошла ошибка.

#### `_load_gapi_credentials`

**Описание**: Загружает учетные данные Google API из KeePass.

**Параметры**:

- `kp` (PyKeePass): Объект `PyKeePass` для работы с базой данных.

**Возвращает**:

- `bool`: `True` если данные загружены успешно, `False` если произошла ошибка.

#### `now`

**Описание**: Возвращает текущую временную метку в формате, указанном в файле `config.json`.

**Параметры**:

- `None`

**Возвращает**:

- `str`: Строка с текущей временной меткой.

**Возможные Исключения**:

- `BinaryError`: Исключение для ошибок двоичных данных.
- `CredentialsError`: Исключение для ошибок данных учетных данных.
- `DefaultSettingsException`: Исключение для ошибок настроек по умолчанию.
- `HeaderChecksumError`: Исключение для ошибок контрольной суммы заголовка.
- `KeePassException`: Исключение для ошибок базы данных KeePass.
- `PayloadChecksumError`: Исключение для ошибок контрольной суммы полезной нагрузки.
- `UnableToSendToRecycleBin`: Исключение для ошибок отправки в корзину.
- `Exception`: Общее исключение.

## Примечания

- Модуль использует PyKeePass для работы с файлом `credentials.kdbx`.
- В коде присутствуют блоки обработки исключений (`ex`).
- Парольный файл (`password.txt`) содержит пароли в виде обычного текста. Это является потенциальной уязвимостью. Необходимо разработать безопасный механизм хранения паролей.

## Инициализация и конфигурация

Когда проект запускается, он инициализирует и настраивает различные параметры и учетные данные. Этот документ объясняет, как эти значения устанавливаются и управляются.

### Определение корневого каталога проекта

Проект автоматически определяет свой корневой каталог, ища вверх от текущего каталога файла конкретные маркерные файлы (`pyproject.toml`, `requirements.txt`, `.git`). Это гарантирует, что проект может найти свои ресурсы независимо от текущего рабочего каталога.

```python
def set_project_root(marker_files=('__root__','.git')) -> Path:
    """
    Находит корневой каталог проекта, начиная с текущего каталога файла,
    ища вверх и останавливаясь на первом каталоге, содержащем любой из маркерных файлов.
    
    Args:
        marker_files (tuple): Имена файлов или каталогов для идентификации корневого каталога проекта.
    
    Returns:
        Path: Путь к корневому каталогу, если найден, в противном случае каталог, где расположен скрипт.
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

Проект загружает свои настройки по умолчанию из файла `config.json`, расположенного в каталоге `src`. Этот JSON-файл содержит различные параметры конфигурации, такие как:

- **Информация об авторе**: Подробная информация об авторе.
- **Доступные режимы**: Поддерживаемые режимы (`dev`, `debug`, `test`, `prod`).
- **Пути**: Каталоги для журналов, временных файлов, внешнего хранилища и Google Диска.
- **Детали проекта**: Название, версия и информация о выпуске проекта.

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

KeePass — это бесплатный менеджер паролей с открытым исходным кодом, который безопасно хранит ваши пароли и другую конфиденциальную информацию в зашифрованной базе данных. База данных защищена мастер-паролем, который является единственным паролем, который вам нужно запомнить. KeePass использует мощные алгоритмы шифрования (такие как AES и Twofish) для обеспечения безопасности ваших данных.

**Почему KeePass хорош?**

- **Безопасность**: KeePass использует отраслевые стандарты шифрования для защиты ваших данных, что делает его очень безопасным от несанкционированного доступа.
- **Портативность**: Вы можете хранить свою базу данных KeePass на USB-накопителе или в облачном хранилище и получать к ней доступ с нескольких устройств.
- **Настройка**: KeePass позволяет вам организовывать свои пароли в группы и подгруппы, что упрощает управление большим количеством учетных данных.
- **Открытый исходный код**: Будучи проектом с открытым исходным кодом, KeePass является прозрачным и может быть проверен сообществом на предмет его безопасности.

**Как KeePass работает в этом проекте**

Учетные данные безопасно управляются с использованием базы данных KeePass (`credentials.kdbx`). Мастер-пароль для этой базы данных обрабатывается по-разному в зависимости от среды:

- **Режим разработки**: Пароль считывается из файла с именем `password.txt`, расположенного в каталоге `secrets`.
- **Производственный режим**: Пароль вводится через консоль. (Удалите файл `password.txt` из каталога `secrets`)

```python
def _open_kp(self, retry: int = 3) -> PyKeePass | None:
    """ Открывает базу данных KeePass
    Args:
        retry (int): Количество попыток
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

1. **suppliers/aliexpress/api**:
    - Содержит учетные данные Aliexpress API.
    - Пример записи: `self.credentials.aliexpress.api_key`, `self.credentials.aliexpress.secret`, `self.credentials.aliexpress.tracking_id`, `self.credentials.aliexpress.email`, `self.credentials.aliexpress.password`.
   
2. **openai**:
    - Содержит ключи OpenAI API.
    - Пример записи: `self.credentials.openai.api_key`.

3. **openai/assistants**:
   - Содержит идентификаторы ассистентов OpenAI.
   - Пример записи: `self.credentials.openai.assistant_id`.

4. **gemini**:
   - Содержит учетные данные GoogleAI.
   - Пример записи: `self.credentials.gemini.api_key`.

5. **telegram**:
   - Содержит учетные данные Telegram.
   - Пример записи: `self.credentials.telegram.token`.

6. **discord**:
   - Содержит учетные данные Discord.
   - Пример записи: `self.credentials.discord.application_id`, `self.credentials.discord.public_key`, `self.credentials.discord.bot_token`.

7. **prestashop**:
   - Содержит учетные данные PrestaShop.
   - Пример записи: `self.credentials.presta.client.api_key`, `self.credentials.presta.client.api_domain`, `self.credentials.presta.client.db_server`, `self.credentials.presta.client.db_user`, `self.credentials.presta.client.db_password`.

8. **prestashop/clients**:
   - Содержит учетные данные клиентов PrestaShop.
    - Пример записи: `self.credentials.presta.client.api_key`, `self.credentials.presta.client.api_domain`, `self.credentials.presta.client.db_server`, `self.credentials.presta.client.db_user`, `self.credentials.presta.client.db_password`.

9. **prestashop/translation**:
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
- Каждая запись (`entry`) в группе содержит конкретные учетные данные.
- Методы `_load_*_credentials` загружают данные из соответствующих групп и записей в базе данных KeePass и сохраняют их в атрибутах объекта `self.credentials`.

### Глобальный экземпляр `ProgramSettings`

```python
# Глобальный экземпляр ProgramSettings
gs: ProgramSettings = ProgramSettings()
```

**Зачем это нужно?**

Этот глобальный экземпляр `ProgramSettings` (`gs`) создан для обеспечения доступа к настройкам и учетным данным проекта из любой точки кода. Таким образом, вам не нужно создавать новый экземпляр класса `ProgramSettings` каждый раз, когда вам нужно получить доступ к настройкам или учетным данным.

**Как это используется?**

В других модулях проекта вы можете импортировать этот глобальный экземпляр и использовать его для доступа к настройкам и учетным данным:

```python
from src import gs

# Пример использования
api_key = gs.credentials.openai.api_key
```

Это упрощает доступ к настройкам и учетным данным, делая код более чистым и удобным в использовании.
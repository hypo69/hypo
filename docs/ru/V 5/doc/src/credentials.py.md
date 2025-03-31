# Модуль `credentials`

## Обзор

Модуль `credentials` предназначен для хранения глобальных настроек проекта, таких как пути, пароли, логины и параметры API. Он использует паттерн Singleton для обеспечения единственного экземпляра настроек в течение всего времени работы приложения.

## Подробней

Модуль содержит класс `ProgramSettings`, который хранит все основные параметры и настройки проекта. Он загружает конфигурацию из файла `config.json`, расположенного в директории `src`, и учетные данные из базы данных KeePass. Класс также определяет пути к различным директориям проекта, таким как `bin`, `log`, `tmp` и `data`.

## Классы

### `ProgramSettings`

**Описание**: Класс `ProgramSettings` является Singleton-ом и хранит основные параметры и настройки проекта.

**Как работает класс**:

- При инициализации класса происходит загрузка конфигурации из файла `config.json` с использованием функции `j_loads_ns`. Если загрузка не удалась, выводится сообщение об ошибке, и программа завершается.
- Далее происходит определение путей к различным директориям проекта, таким как `bin`, `log`, `tmp` и `data`.
- После этого вызывается метод `_load_credentials`, который загружает учетные данные из базы данных KeePass.

**Методы**:

- `__post_init__`: Выполняет инициализацию после создания экземпляра класса.
- `_load_credentials`: Загружает учетные данные из базы данных KeePass.
- `_open_kp`: Открывает базу данных KeePass.
- `_load_aliexpress_credentials`: Загружает учетные данные для Aliexpress API.
- `_load_openai_credentials`: Загружает учетные данные для OpenAI API.
- `_load_gemini_credentials`: Загружает учетные данные для GoogleAI API.
- `_load_telegram_credentials`: Загружает учетные данные для Telegram API.
- `_load_discord_credentials`: Загружает учетные данные для Discord API.
- `_load_prestashop_credentials`: Загружает учетные данные для PrestaShop API.
- `_load_serpapi_credentials`: Загружает учетные данные для SerpAPI API.
- `_load_smtp_credentials`: Загружает учетные данные для SMTP.
- `_load_facebook_credentials`: Загружает учетные данные для Facebook.
- `_load_gapi_credentials`: Загружает учетные данные для Google API.
- `now`: Возвращает текущую метку времени в формате год-месяц-день-часы-минуты-секунды-милисекунды.

**Параметры**:

- `host_name` (str): Имя хоста. По умолчанию получается с помощью `socket.gethostname()`.
- `base_dir` (Path): Базовая директория проекта. По умолчанию определяется с помощью функции `set_project_root()`.
- `config` (SimpleNamespace): Объект, хранящий конфигурацию проекта. По умолчанию создается пустой объект `SimpleNamespace`.
- `credentials` (SimpleNamespace): Объект, хранящий учетные данные для различных сервисов. По умолчанию создается объект `SimpleNamespace` с пустыми атрибутами для каждого сервиса.
- `path` (SimpleNamespace): Объект, хранящий пути к различным директориям проекта. По умолчанию создается объект `SimpleNamespace` с путями к директориям `root`, `src`, `bin`, `log`, `tmp`, `data`, `secrets`, `google_drive`, `external_storage` и `tools`.
- `host` (str): Хост. По умолчанию `'127.0.0.1'`.

**Примеры**:

```python
from src.credentials import ProgramSettings

# Получение экземпляра класса ProgramSettings
gs = ProgramSettings()

# Доступ к параметрам проекта
print(f"Project name: {gs.config.project_name}")
print(f"Log directory: {gs.path.log}")
```

## Функции

### `set_project_root`

```python
def set_project_root(marker_files: tuple[str, ...] = ('__root__', '.git')) -> Path:
    """
    Находит корневой каталог проекта, начиная с каталога текущего файла,
    поиска вверх и остановки в первом каталоге, содержащем любой из файлов-маркеров.

    Args:
        marker_files (tuple): Имена файлов или каталогов для идентификации корня проекта.

    Returns:
        Path: Путь к корневому каталогу, если он найден, в противном случае - каталог, в котором находится скрипт.
    """
```

**Описание**: Функция `set_project_root` определяет корневую директорию проекта, начиная поиск от текущей директории файла и поднимаясь вверх по дереву каталогов. Поиск прекращается, когда обнаружена директория, содержащая один из файлов-маркеров (по умолчанию `__root__` или `.git`).

**Как работает функция**:

1.  Определяется текущая директория файла с помощью `Path(__file__).resolve().parent`.
2.  Перебираются родительские директории, начиная с текущей.
3.  Для каждой директории проверяется наличие в ней хотя бы одного из файлов-маркеров.
4.  Если файл-маркер найден, директория считается корневой, и поиск прекращается.
5.  Если корневая директория не найдена, возвращается директория, в которой находится скрипт.
6.  Если корневая директория не содержится в `sys.path`, она добавляется в начало списка.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или каталогов, которые используются для определения корневой директории проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:

- `Path`: Объект `Path`, представляющий корневую директорию проекта.

**Примеры**:

```python
from src.credentials import set_project_root

# Определение корневой директории проекта
root_dir = set_project_root()
print(f"Project root directory: {root_dir}")
```

### `singleton`

```python
def singleton(cls):
    """Декоратор для реализации Singleton."""
```

**Описание**: Декоратор `singleton` реализует паттерн Singleton для класса, к которому он применяется.

**Как работает функция**:

1.  Создается словарь `instances` для хранения экземпляров класса.
2.  Определяется внутренняя функция `get_instance`, которая принимает произвольные аргументы.
3.  При первом вызове `get_instance` создается экземпляр класса и сохраняется в словаре `instances`.
4.  При последующих вызовах `get_instance` возвращается сохраненный экземпляр класса из словаря `instances`.

**Параметры**:

- `cls`: Класс, к которому применяется декоратор.

**Возвращает**:

- Функция `get_instance`, которая возвращает экземпляр класса.

**Примеры**:

```python
from src.credentials import singleton

@singleton
class MyClass:
    def __init__(self):
        self.value = 0

# Получение экземпляров класса MyClass
instance1 = MyClass()
instance2 = MyClass()

# Проверка, что instance1 и instance2 - это один и тот же объект
print(instance1 is instance2)  # Вывод: True

instance1.value = 10
print(instance2.value)  # Вывод: 10
```

### `ProgramSettings.__post_init__`

```python
def __post_init__(self):
    """Выполняет инициализацию после создания экземпляра класса."""
```

**Описание**: Метод `__post_init__` выполняет инициализацию объекта класса `ProgramSettings` после его создания.

**Как работает функция**:

1.  Загружает конфигурацию из файла `config.json` с использованием функции `j_loads_ns`.
2.  Если загрузка не удалась, выводит сообщение об ошибке и завершает работу программы.
3.  Устанавливает формат времени из конфигурации или использует значение по умолчанию (`'%y_%m_%d_%H_%M_%S_%f'`).
4.  Устанавливает имя проекта из имени базовой директории.
5.  Определяет пути к различным директориям проекта, таким как `bin`, `log`, `tmp` и `data`.
6.  Проверяет наличие новой версии на GitHub.
7.  Добавляет пути к директориям с бинарными файлами в `sys.path`.
8.  Отключает вывод логов GTK в консоль.
9.  Загружает учетные данные из базы данных KeePass с использованием метода `_load_credentials`.

**Параметры**:

- Отсутствуют.

**Возвращает**:

- Отсутствует.

**Примеры**:

```python
from src.credentials import ProgramSettings

# Создание экземпляра класса ProgramSettings
gs = ProgramSettings()

# После создания экземпляра выполняется метод __post_init__, который загружает конфигурацию и учетные данные
print(f"Project name: {gs.config.project_name}")
```

### `ProgramSettings._load_credentials`

```python
def _load_credentials(self) -> None:
    """ Загружает учетные данные из настроек."""
```

**Описание**: Метод `_load_credentials` загружает учетные данные из базы данных KeePass.

**Как работает функция**:

1.  Открывает базу данных KeePass с использованием метода `_open_kp`.
2.  Если открытие базы данных не удалось, выводит сообщение об ошибке и завершает работу программы.
3.  Загружает учетные данные для различных сервисов, таких как Aliexpress, OpenAI, Gemini, Discord, Telegram, PrestaShop, SMTP, Facebook и Google API, с использованием соответствующих методов.

**Параметры**:

- Отсутствуют.

**Возвращает**:

- Отсутствует.

**Примеры**:

```python
from src.credentials import ProgramSettings

# Создание экземпляра класса ProgramSettings
gs = ProgramSettings()

# Метод _load_credentials вызывается автоматически при создании экземпляра класса
print(f"Aliexpress API key: {gs.credentials.aliexpress.api_key}")
```

### `ProgramSettings._open_kp`

```python
def _open_kp(self, retry: int = 3) -> PyKeePass | None:
    """ Open KeePass database
    Args:
        retry (int): Number of retries
    """
```

**Описание**: Метод `_open_kp` открывает базу данных KeePass.

**Как работает функция**:

1.  Пытается открыть базу данных KeePass несколько раз (по умолчанию 3 попытки).
2.  Считывает пароль из файла `password.txt`, расположенного в директории `secrets`.
3.  Если файл не найден или пароль не указан, запрашивает пароль у пользователя через консоль.
4.  Открывает базу данных KeePass с использованием библиотеки `PyKeePass`.
5.  Если открытие базы данных не удалось, выводит сообщение об ошибке и уменьшает количество попыток.
6.  Если количество попыток исчерпано, выводит критическое сообщение об ошибке и завершает работу программы.

**Параметры**:

- `retry` (int): Количество попыток открытия базы данных KeePass. По умолчанию 3.

**Возвращает**:

- `PyKeePass | None`: Объект `PyKeePass`, представляющий базу данных KeePass, или `None`, если открытие базы данных не удалось.

**Примеры**:

```python
from src.credentials import ProgramSettings

# Создание экземпляра класса ProgramSettings
gs = ProgramSettings()

# Открытие базы данных KeePass
kp = gs._open_kp()

if kp:
    print("KeePass database opened successfully")
else:
    print("Failed to open KeePass database")
```

### `ProgramSettings._load_aliexpress_credentials`

```python
def _load_aliexpress_credentials(self, kp: PyKeePass) -> bool:
    """ Load Aliexpress API credentials from KeePass
    Args:
        kp (PyKeePass): The KeePass database instance.

    Returns:
        bool: True if loading was successful, False otherwise.
    """
```

**Описание**: Метод `_load_aliexpress_credentials` загружает учетные данные для Aliexpress API из базы данных KeePass.

**Как работает функция**:

1.  Находит группу записей для Aliexpress API в базе данных KeePass.
2.  Извлекает значения `api_key`, `secret`, `tracking_id`, `email` и `password` из первой записи в группе.
3.  Сохраняет извлеченные значения в атрибутах `api_key`, `secret`, `tracking_id`, `email` и `password` объекта `self.credentials.aliexpress`.
4.  Если загрузка прошла успешно, возвращает `True`, иначе возвращает `False`.

**Параметры**:

- `kp` (PyKeePass): Объект `PyKeePass`, представляющий базу данных KeePass.

**Возвращает**:

- `bool`: `True`, если загрузка прошла успешно, `False` в противном случае.

**Примеры**:

```python
from src.credentials import ProgramSettings
from pykeepass import PyKeePass

# Создание экземпляра класса ProgramSettings
gs = ProgramSettings()

# Открытие базы данных KeePass
kp = gs._open_kp()

if kp:
    # Загрузка учетных данных для Aliexpress API
    success = gs._load_aliexpress_credentials(kp)

    if success:
        print("Aliexpress credentials loaded successfully")
        print(f"API key: {gs.credentials.aliexpress.api_key}")
    else:
        print("Failed to load Aliexpress credentials")
else:
    print("Failed to open KeePass database")
```

### `ProgramSettings._load_openai_credentials`

```python
def _load_openai_credentials(self, kp: PyKeePass) -> bool:
    """ Load OpenAI credentials from KeePass
    Args:
        kp (PyKeePass): The KeePass database instance.

    Returns:
        bool: True if loading was successful, False otherwise.
    """
```

**Описание**: Метод `_load_openai_credentials` загружает учетные данные для OpenAI API из базы данных KeePass.

**Как работает функция**:

1.  Находит группы записей для OpenAI API и ассистентов в базе данных KeePass.
2.  Перебирает записи с ключами OpenAI API.
3.  Для каждой записи создает `SimpleNamespace` для хранения ключей.
4.  Сохраняет `api_key` и `project_api` в созданном `SimpleNamespace`.
5.  Возвращает `True`, если загрузка прошла успешно, иначе возвращает `False`.

**Параметры**:

- `kp` (PyKeePass): Объект `PyKeePass`, представляющий базу данных KeePass.

**Возвращает**:

- `bool`: `True`, если загрузка прошла успешно, `False` в противном случае.

**Примеры**:

```python
from src.credentials import ProgramSettings
from pykeepass import PyKeePass

# Создание экземпляра класса ProgramSettings
gs = ProgramSettings()

# Открытие базы данных KeePass
kp = gs._open_kp()

if kp:
    # Загрузка учетных данных для OpenAI API
    success = gs._load_openai_credentials(kp)

    if success:
        print("OpenAI credentials loaded successfully")
        # Пример доступа к API ключу OpenAI с именем 'hypotez':
        if hasattr(gs.credentials.openai, 'hypotez'):
            print(f"API key 'hypotez': {gs.credentials.openai.hypotez.api_key}")
        else:
            print("No OpenAI API key with name 'hypotez' found.")
    else:
        print("Failed to load OpenAI credentials")
else:
    print("Failed to open KeePass database")
```

### `ProgramSettings._load_gemini_credentials`

```python
def _load_gemini_credentials(self, kp: PyKeePass) -> bool:
    """ Load GoogleAI credentials from KeePass
    Args:
        kp (PyKeePass): The KeePass database instance.

    Returns:
        bool: True if loading was successful, False otherwise.
    """
```

**Описание**: Метод `_load_gemini_credentials` загружает учетные данные для GoogleAI (Gemini) API из базы данных KeePass.

**Как работает функция**:

1.  Находит группы записей для Gemini API в базе данных KeePass.
2.  Перебирает записи с ключами Gemini API.
3.  Для каждой записи сохраняет `api_key` в `self.credentials.gemini`.
4.  Возвращает `True`, если загрузка прошла успешно, иначе возвращает `False`.

**Параметры**:

- `kp` (PyKeePass): Объект `PyKeePass`, представляющий базу данных KeePass.

**Возвращает**:

- `bool`: `True`, если загрузка прошла успешно, `False` в противном случае.

**Примеры**:

```python
from src.credentials import ProgramSettings
from pykeepass import PyKeePass

# Создание экземпляра класса ProgramSettings
gs = ProgramSettings()

# Открытие базы данных KeePass
kp = gs._open_kp()

if kp:
    # Загрузка учетных данных для Gemini API
    success = gs._load_gemini_credentials(kp)

    if success:
        print("Gemini credentials loaded successfully")
        # Пример доступа к API ключу Gemini с именем 'owner':
        if hasattr(gs.credentials.gemini, 'owner'):
            print(f"API key 'owner': {gs.credentials.gemini.owner}")
        else:
            print("No Gemini API key with name 'owner' found.")
    else:
        print("Failed to load Gemini credentials")
else:
    print("Failed to open KeePass database")
```

### `ProgramSettings._load_telegram_credentials`

```python
def _load_telegram_credentials(self, kp: PyKeePass) -> bool:
    """Load Telegram credentials from KeePass.

    Args:
        kp (PyKeePass): The KeePass database instance.

    Returns:
        bool: True if loading was successful, False otherwise.
    """
```

**Описание**: Метод `_load_telegram_credentials` загружает учетные данные для Telegram API из базы данных KeePass.

**Как работает функция**:

1.  Находит группы записей для Telegram API в базе данных KeePass.
2.  Перебирает записи с ключами Telegram API.
3.  Для каждой записи сохраняет `token` в `self.credentials.telegram`.
4.  Возвращает `True`, если загрузка прошла успешно, иначе возвращает `False`.

**Параметры**:

- `kp` (PyKeePass): Объект `PyKeePass`, представляющий базу данных KeePass.

**Возвращает**:

- `bool`: `True`, если загрузка прошла успешно, `False` в противном случае.

**Примеры**:

```python
from src.credentials import ProgramSettings
from pykeepass import PyKeePass

# Создание экземпляра класса ProgramSettings
gs = ProgramSettings()

# Открытие базы данных KeePass
kp = gs._open_kp()

if kp:
    # Загрузка учетных данных для Telegram API
    success = gs._load_telegram_credentials(kp)

    if success:
        print("Telegram credentials loaded successfully")
        # Пример доступа к токену Telegram бота с именем 'bot':
        if hasattr(gs.credentials.telegram, 'bot'):
            print(f"Token 'bot': {gs.credentials.telegram.bot}")
        else:
            print("No Telegram token with name 'bot' found.")
    else:
        print("Failed to load Telegram credentials")
else:
    print("Failed to open KeePass database")
```

### `ProgramSettings._load_discord_credentials`

```python
def _load_discord_credentials(self, kp: PyKeePass) -> bool:
    """ Load Discord credentials from KeePass
    Args:
        kp (PyKeePass): The KeePass database instance.

    Returns:
        bool: True if loading was successful, False otherwise.
    """
```

**Описание**: Метод `_load_discord_credentials` загружает учетные данные для Discord API из базы данных KeePass.

**Как работает функция**:

1.  Находит группу записей для Discord API в базе данных KeePass.
2.  Извлекает значения `application_id`, `public_key` и `bot_token` из первой записи в группе.
3.  Сохраняет извлеченные значения в атрибутах `application_id`, `public_key` и `bot_token` объекта `self.credentials.discord`.
4.  Если загрузка прошла успешно, возвращает `True`, иначе возвращает `False`.

**Параметры**:

- `kp` (PyKeePass): Объект `PyKeePass`, представляющий базу данных KeePass.

**Возвращает**:

- `bool`: `True`, если загрузка прошла успешно, `False` в противном случае.

**Примеры**:

```python
from src.credentials import ProgramSettings
from pykeepass import PyKeePass

# Создание экземпляра класса ProgramSettings
gs = ProgramSettings()

# Открытие базы данных KeePass
kp = gs._open_kp()

if kp:
    # Загрузка учетных данных для Discord API
    success = gs._load_discord_credentials(kp)

    if success:
        print("Discord credentials loaded successfully")
        print(f"Application ID: {gs.credentials.discord.application_id}")
        print(f"Public Key: {gs.credentials.discord.public_key}")
        print(f"Bot Token: {gs.credentials.discord.bot_token}")
    else:
        print("Failed to load Discord credentials")
else:
    print("Failed to open KeePass database")
```

### `ProgramSettings._load_prestashop_credentials`

```python
def _load_prestashop_credentials(self, kp: PyKeePass) -> bool:
    """ Load prestashop credentials from KeePass
    Args:
        kp (PyKeePass): The KeePass database instance.
    Returns:
        bool: True if loading was successful, False otherwise.
    """
```

**Описание**: Метод `_load_prestashop_credentials` загружает учетные данные для PrestaShop API из базы данных KeePass.

**Как работает функция**:

1.  Находит группу записей для клиентов PrestaShop в базе данных KeePass.
2.  Перебирает записи клиентов PrestaShop.
3.  Для каждой записи создает `SimpleNamespace` для хранения учетных данных клиента.
4.  Сохраняет `api_key`, `api_domain`, `db_server`, `db_user` и `db_password` в созданном `SimpleNamespace`.
5.  Возвращает `True`, если загрузка прошла успешно, иначе возвращает `False`.

**Параметры**:

- `kp` (PyKeePass): Объект `PyKeePass`, представляющий базу данных KeePass.

**Возвращает**:

- `bool`: `True`, если загрузка прошла успешно, `False` в противном случае.

**Примеры**:

```python
from src.credentials import ProgramSettings
from pykeepass import PyKeePass

# Создание экземпляра класса ProgramSettings
gs = ProgramSettings()

# Открытие базы данных KeePass
kp = gs._open_kp()

if kp:
    # Загрузка учетных данных для PrestaShop API
    success = gs._load_prestashop_credentials(kp)

    if success:
        print("PrestaShop credentials loaded successfully")
        # Пример доступа к API ключу клиента PrestaShop с именем 'client1':
        if hasattr(gs.credentials.presta.client, 'client1'):
            print(f"API key 'client1': {gs.credentials.presta.client.client1.api_key}")
        else:
            print("No PrestaShop client with name 'client1' found.")
    else:
        print("Failed to load PrestaShop credentials")
else:
    print("Failed to open KeePass database")
```

### `ProgramSettings._load_serpapi_credentials`

```python
def _load_serpapi_credentials(self, kp: PyKeePass) -> bool:
    """ Load OpenAI credentials from KeePass
    Args:
        kp (PyKeePass): The KeePass database instance.

    Returns:
        bool: True if loading was successful, False otherwise.
    """
```

**Описание**: Метод `_load_serpapi_credentials` загружает учетные данные для SerpAPI API из базы данных KeePass.

**Как работает функция**:

1.  Находит группы записей для SerpAPI API в базе данных KeePass.
2.  Перебирает записи с ключами SerpAPI API.
3.  Для каждой записи создает `SimpleNamespace` для хранения ключей.
4.  Сохраняет `api_key` в созданном `SimpleNamespace`.
5.  Возвращает `True`, если загрузка прошла успешно, иначе возвращает `False`.

**Параметры**:

- `kp` (PyKeePass): Объект `PyKeePass`, представляющий базу данных KeePass.

**Возвращает**:

- `bool`: `True`, если загрузка прошла успешно, `False` в противном случае.

**Примеры**:

```python
from src.credentials import ProgramSettings
from pykeepass import PyKeePass

# Создание экземпляра класса ProgramSettings
gs = ProgramSettings()

# Открытие базы данных KeePass
kp = gs._open_kp()

if kp:
    # Загрузка учетных данных для SerpAPI API
    success = gs._load_serpapi_credentials(kp)

    if success:
        print("SerpAPI credentials loaded successfully")
        # Пример доступа к API ключу SerpAPI с именем 'owner':
        if hasattr(gs.credentials.serpapi, 'owner'):
            print(f"API key 'owner': {gs.credentials.serpapi.owner.api_key}")
        else:
            print("No SerpAPI API key with name 'owner' found.")
    else:
        print("Failed to load SerpAPI credentials")
else:
    print("Failed to open KeePass database")
```

### `ProgramSettings._load_smtp_credentials`

```python
def _load_smtp_credentials(self, kp: PyKeePass) -> bool:
    """ Load SMTP credentials from KeePass
    Args:
        kp (PyKeePass): The KeePass database instance.

    Returns:
        bool: True if loading was successful, False otherwise.
    """
```

**Описание**: Метод `_load_smtp_credentials` загружает учетные данные для SMTP из базы данных KeePass.

**Как работает функция**:

1.  Находит группу записей для SMTP в базе данных KeePass.
2.  Перебирает записи для SMTP.
3.  Для каждой записи создает `SimpleNamespace` и сохраняет `server`, `port`, `user` и `password`.
4.  Добавляет созданный `SimpleNamespace` в список `self.credentials.smtp`.
5.  Возвращает `True`, если загрузка прошла успешно, иначе возвращает `False`.

**Параметры**:

- `kp` (PyKeePass): Объект `PyKeePass`, представляющий базу данных KeePass.

**Возвращает**:

- `bool`: `True`, если загрузка прошла успешно, `False` в противном случае.

**Примеры**:

```python
from src.credentials import ProgramSettings
from pykeepass import PyKeePass

# Создание экземпляра класса ProgramSettings
gs = ProgramSettings()

# Открытие базы данных KeePass
kp = gs._open_kp()

if kp:
    # Загрузка учетных данных для SMTP
    success = gs._load_smtp_credentials(kp)

    if success:
        print("SMTP credentials loaded successfully")
        # Пример доступа к параметрам первого SMTP-сервера:
        if gs.credentials.smtp:
            print(f"Server: {gs.credentials.smtp[0].server}")
            print(f"Port: {gs.credentials.smtp[0].port}")
            print(f"User: {gs.credentials.smtp[0].user}")
        else:
            print("No SMTP credentials found.")
    else:
        print("Failed to load SMTP credentials")
else:
    print("Failed to open KeePass database")
```

### `ProgramSettings._load_facebook_credentials`

```python
def _load_facebook_credentials(self, kp: PyKeePass) -> bool:
    """ Load Facebook credentials from KeePass
    Args:
        kp (PyKeePass): The KeePass database instance.

    Returns:
        bool: True if loading was successful, False otherwise.
    """
```

**Описание**: Метод `_load_facebook_credentials` загружает учетные данные для Facebook API из базы данных KeePass.

**Как работает функция**:

1.  Находит группу записей для Facebook API в базе данных KeePass.
2.  Перебирает записи для Facebook API.
3.  Для каждой записи создает `SimpleNamespace` и сохраняет `app_id`, `app_secret` и `access_token`.
4.  Добавляет созданный `SimpleNamespace` в список `self.credentials.facebook`.
5.  Возвращает `True`, если загрузка прошла успешно, иначе возвращает `False`.

**Параметры**:

- `kp` (PyKeePass): Объект `PyKeePass`, представляющий базу данных KeePass.

**Возвращает**:

- `bool`: `True`, если загрузка прошла успешно, `False` в противном случае.

**Примеры**:

```python
from src.credentials import ProgramSettings
from pykeepass import PyKeePass

# Создание экземпляра класса ProgramSettings
gs = ProgramSettings()

# Открытие базы данных KeePass
kp = gs._open_kp()

if kp:
    # Загрузка учетных данных для Facebook API
    success = gs._load_facebook_credentials(kp)

    if success:
        print("Facebook credentials loaded successfully")
        # Пример доступа к параметрам первого Facebook-приложения:
        if gs.credentials.facebook:
            print(f"App ID: {gs.credentials.facebook[0].app_id}")
            print(f"App Secret: {gs.credentials.facebook[0].app_secret}")
            print(f"Access Token: {gs.credentials.facebook[0].access_token}")
        else:
            print("No Facebook credentials found.")
    else:
        print("Failed to load Facebook credentials")
else:
    print("Failed to open KeePass database")
```

### `ProgramSettings._load_gapi_credentials`

```python
def _load_gapi_credentials(self, kp: PyKeePass) -> bool:
    """ Load Google API credentials from KeePass
    Args:
        kp (PyKeePass): The KeePass database instance.

    Returns:
        bool: True if loading was successful, False otherwise.
    """
```

**Описание**: Метод `_load_gapi_credentials` загружает учетные данные для Google API из базы данных KeePass.

**Как работает функция**:

1.  Находит группу записей для Google API (gapi) в базе данных KeePass.
2.  Извлекает значение `api_key` из первой записи в группе.
3.  Сохраняет извлеченное значение в атрибуте `api_key` объекта `self.credentials.gapi`.
4.  Если загрузка прошла успешно, возвращает `True`, иначе возвращает `False`.

**Параметры**:

- `kp` (PyKeePass): Объект `PyKeePass`, представляющий базу данных KeePass.

**Возвращает**:

- `bool`: `True`, если загрузка прошла успешно, `False` в противном случае.

**Примеры**:

```python
from src.credentials import ProgramSettings
from pykeepass import PyKeePass

# Создание экземпляра класса ProgramSettings
gs = ProgramSettings()

# Открытие базы данных KeePass
kp = gs._open_kp()

if kp:
    # Загрузка учетных данных для Google API
    success = gs._load_gapi_credentials(kp)

    if success:
        print("GAPI credentials loaded successfully")
        print(f"API key: {gs.credentials.gapi['api_key']}")
    else:
        print("Failed to load GAPI credentials")
else:
    print("Failed to open KeePass database")
```

### `ProgramSettings.now`

```python
@property
def now(self) -> str:
    """Возвращает текущую метку времени в формате год-месяц-день-часы-минуты-секунды-милисекунды.

    Этот метод возвращает строку, представляющую текущую метку времени, в формате `год_месяц_день_часы_минуты_секунды_миллисекунды`.

    Args:
        dformat (str, optional): Формат для метки времени. По умолчанию `'%y_%m_%d_%H_%M_%S_%f'`.

    Returns:
        str: Текущая метка времени в строковом формате.
    """
```

**Описание**: Свойство `now` возвращает текущую метку времени в формате, определенном в `self.config.timestamp_format`.

**Как работает функция**:

1.  Получает текущее время с помощью `datetime.now()`.
2.  Форматирует текущее время в строку с использованием `strftime` и формата из `self.config.timestamp_format`.
3.  Обрезает строку, чтобы оставить только первые 3 цифры миллисекунд.
4.  Возвращает отформатированную строку.

**Параметры**:

- Отсутствуют.

**Возвращает**:

- `str`: Текущая метка времени в строковом формате.

**Примеры**:

```python
from src.credentials import ProgramSettings

# Создание экземпляра класса ProgramSettings
gs = ProgramSettings()

# Получение текущей метки времени
now = gs.now
print(f"Current timestamp: {now}")
```

## Переменные

### `gs`

```python
gs: ProgramSettings = ProgramSettings()
```

**Описание**: Глобальный экземпляр класса `ProgramSettings`, обеспечивающий доступ к настройкам программы из любой точки проекта.

**Как работает переменная**:

- Переменная `gs` инициализируется как экземпляр класса `ProgramSettings`.
- Благодаря декоратору `@singleton`, `ProgramSettings` гарантирует, что `gs` всегда будет указывать на один и тот же экземпляр класса.

**Примеры**:

```python
from src.credentials import gs

# Доступ к базовой директории проекта
print(f"Base directory: {gs.base_dir}")

# Доступ к имени проекта
print(f"Project name: {gs.config.project_name}")
```
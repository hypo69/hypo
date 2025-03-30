# Модуль `src.credentials`

## Обзор

Модуль `src.credentials` предназначен для управления учетными данными приложения, такими как API-ключи, пароли и другие секретные данные. Он использует базу данных KeePass для безопасного хранения и доступа к учетным данным. Также модуль предоставляет функциональность для определения корневой директории проекта и загрузки конфигурационных файлов.

## Оглавление

- [Обзор](#обзор)
- [Функции](#функции)
  - [`set_project_root`](#set_project_root)
  - [`singleton`](#singleton)
- [Классы](#классы)
  - [`ProgramSettings`](#programsettings)
    - [Атрибуты](#атрибуты)
    - [Методы](#методы)
    - [Возможные исключения](#возможные-исключения)
- [Инициализация и Настройка](#инициализация-и-настройка)
  - [Определение Корневой Директории Проекта](#определение-корневой-директории-проекта)
  - [Загрузка Конфигурации](#загрузка-конфигурации)
  - [Управление Учетными Данными с Использованием KeePass](#управление-учетными-данными-с-использованием-keepass)
  - [Глобальный Экземпляр `ProgramSettings`](#глобальный-экземпляр-programsettings)
- [Подробное описание структуры `credentials.kdbx`](#подробное-описание-структуры-credentialskdbx)
- [Примечания](#примечания)

## Подробней

Данный модуль играет важную роль в обеспечении безопасности и удобства управления учетными данными в проекте. Он позволяет хранить секретную информацию в зашифрованном виде и предоставляет простой интерфейс для доступа к ней. Функция `set_project_root` позволяет автоматически определять корневую директорию проекта, что упрощает работу с путями к файлам и каталогам.

## Функции

### `set_project_root`

```python
def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """ This if example function
    Args:
        marker_files (tuple): Имена файлов или директорий для идентификации корневой директории проекта.

    Returns:
        Path: Путь к корневой директории, если найдена, иначе директория, где находится скрипт.

     **Как работает функция**:
    Функция `set_project_root` ищет корневую директорию проекта, начиная с текущей директории файла,
    ища вверх и останавливаясь на первой директории, содержащей любой из маркерных файлов.
    """
    ...
```

**Описание**: Находит корневую директорию проекта, начиная от текущего каталога. Поиск идёт вверх по директориям, пока не найдена директория, содержащая один из файлов из списка `marker_files`.

**Параметры**:
- `marker_files` (tuple): Кортеж строк, представляющих имена файлов или каталогов, которые используются для определения корневой директории проекта. По умолчанию ищутся следующие маркеры: `__root__`, `.git`.

**Возвращает**:
- `Path`: Путь к корневой директории проекта, если она найдена, иначе - путь к директории, в которой расположен скрипт.

**Примеры**:

```python
from pathlib import Path
root_dir = set_project_root(marker_files=('pyproject.toml', 'requirements.txt'))
print(f"Root directory: {root_dir}")
```

### `singleton`

```python
def singleton(cls):
    """ This if example function
    Args:
        cls: Класс, который должен быть преобразован в синглтон.

    Returns:
        function: Функция, возвращающая экземпляр класса-синглтона.

     **Как работает функция**:
    Функция `singleton` является декоратором, который преобразует класс в синглтон.
    Синглтон - это класс, который может иметь только один экземпляр.
    """
    ...
```

**Описание**: Декоратор для создания класса-синглтона.

**Параметры**:
- `cls`: Класс, который должен быть преобразован в синглтон.

**Возвращает**:
- `function`: Функция, возвращающая экземпляр класса-синглтона.

**Примеры**:

```python
@singleton
class MyClass:
    pass

instance1 = MyClass()
instance2 = MyClass()
print(instance1 is instance2)  # Вывод: True
```

## Классы

### `ProgramSettings`

```python
class ProgramSettings:
    """ This if example class
    Args:
        None

    Returns:
        None

     **Как работает класс**:
    Класс `ProgramSettings` предназначен для загрузки и хранения настроек программы.
    Он загружает настройки из файла `config.json` и учетные данные из базы данных KeePass.
    Также он предоставляет методы для доступа к этим настройкам и учетным данным.
    """
    ...
```

**Описание**: Класс настроек программы. Устанавливает основные параметры и настройки проекта. Загружает конфигурацию из `config.json` и данные учетных данных из файла `credentials.kdbx` в базе данных KeePass.

**Атрибуты**:
- `host_name` (str): Имя хоста.
- `base_dir` (Path): Путь к корневой директории проекта.
- `config` (SimpleNamespace): Объект, содержащий конфигурацию проекта.
- `credentials` (SimpleNamespace): Объект, содержащий учетные данные.
- `MODE` (str): Режим работы проекта (например, 'dev', 'prod').
- `path` (SimpleNamespace): Объект, содержащий пути к различным директориям проекта.

**Методы**:
- `__init__(self, **kwargs)`: Инициализирует экземпляр класса.
- `_load_credentials(self) -> None`: Загружает учетные данные из KeePass.
- `_open_kp(self, retry: int = 3) -> PyKeePass | None`: Открывает базу данных KeePass.
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
- `now(self) -> str`: Возвращает текущую метку времени в формате, указанном в файле `config.json`.

**Возможные исключения**:
- `BinaryError`: Исключение для ошибок с бинарными данными.
- `CredentialsError`: Исключение для ошибок с данными учетных данных.
- `DefaultSettingsException`: Исключение для ошибок с настройками по умолчанию.
- `HeaderChecksumError`: Исключение для ошибок проверки контрольной суммы заголовков.
- `KeePassException`: Исключение для ошибок с базой данных KeePass.
- `PayloadChecksumError`: Исключение для ошибок проверки контрольной суммы полезной нагрузки.
- `UnableToSendToRecycleBin`: Исключение для ошибок отправки в корзину.
- `Exception`: Общее исключение.

**Примеры**:
```python
gs = ProgramSettings()
print(f"Host name: {gs.host_name}")
print(f"OpenAI API key: {gs.credentials.openai.api_key}")
```

## Инициализация и Настройка

При запуске проект инициализирует и настраивает различные конфигурации и учетные данные. Этот документ объясняет, как эти значения устанавливаются и управляются.

### Определение Корневой Директории Проекта

Проект автоматически определяет свою корневую директорию, ища вверх от текущей директории файла для определенных маркерных файлов (`pyproject.toml`, `requirements.txt`, `.git`). Это гарантирует, что проект может найти свои ресурсы независимо от текущей рабочей директории.

```python
def set_project_root(marker_files: tuple = ('__root__','.git')) -> Path:
    """
    Находит корневую директорию проекта, начиная с текущей директории файла,
    ища вверх и останавливаясь на первой директории, содержащей любой из маркерных файлов.
    
    Args:
        marker_files (tuple): Имена файлов или директорий для идентификации корневой директории проекта.
    
    Returns:
        Path: Путь к корневой директории, если найдена, иначе директория, где находится скрипт.
    """
    ...
```

### Загрузка Конфигурации

Проект загружает свои настройки по умолчанию из файла `config.json`, расположенного в директории `src`. Этот JSON-файл содержит различные параметры конфигурации, такие как:

- **Информация об Авторе**: Детали об авторе.
- **Доступные Режимы**: Поддерживаемые режимы (`dev`, `debug`, `test`, `prod`).
- **Пути**: Директории для логов, временных файлов, внешнего хранилища и Google Drive.
- **Детали Проекта**: Название, версия и информация о релизе проекта.

```python
self.config = j_loads_ns(self.base_dir / 'src' / 'config.json')
if not self.config:
    logger.error('Ошибка при загрузке настроек')
    ...
    return

self.config.project_name = self.base_dir.name
```

### Управление Учетными Данными с Использованием KeePass

**Что такое KeePass?**

KeePass — это бесплатный и открытый менеджер паролей, который безопасно хранит ваши пароли и другую чувствительную информацию в зашифрованной базе данных. База данных защищена мастер-паролем, который является единственным паролем, который вам нужно запомнить. KeePass использует сильные алгоритмы шифрования (такие как AES и Twofish), чтобы гарантировать безопасность ваших данных.

**Чем хорош KeePass?**

- **Безопасность**: KeePass использует отраслевые стандарты шифрования для защиты ваших данных, делая их высокозащищенными от несанкционированного доступа.
- **Переносимость**: Вы можете хранить свою базу данных KeePass на USB-накопителе или в облачном хранилище и получать к ней доступ с нескольких устройств.
- **Настройка**: KeePass позволяет организовывать ваши пароли в группы и подгруппы, что упрощает управление большим количеством учетных данных.
- **Открытый Исходный Код**: Будучи проектом с открытым исходным кодом, KeePass прозрачен и может быть проверен сообществом на предмет его безопасности.

**Как KeePass Работает в Этом Проекте**

Учетные данные безопасно управляются с использованием базы данных KeePass (`credentials.kdbx`). Мастер-пароль для этой базы данных обрабатывается по-разному в зависимости от среды:

- **Режим Разработки**: Пароль считывается из файла с именем `password.txt`, расположенного в директории `secrets`.
- **Режим Продакшн**: Пароль вводится через консоль. (Удалите файл `password.txt` из директории `secrets`)

```python
def _open_kp(self, retry: int = 3) -> PyKeePass | None:
    """ Открывает базу данных KeePass
    Args:
        retry (int): Количество попыток
    """
    ...
```

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

### Подробное описание структуры `credentials.kdbx`:

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

**Зачем это нужно?**

Этот глобальный экземпляр `ProgramSettings` (`gs`) создается для того, чтобы обеспечить доступ к настройкам и учетным данным проекта из любого места в коде. Таким образом, вам не нужно каждый раз создавать новый экземпляр класса `ProgramSettings`, когда вам нужно получить доступ к настройкам или учетным данным.

**Как это используется?**

В других модулях проекта вы можете импортировать этот глобальный экземпляр и использовать его для доступа к настройкам и учетным данным:

```python
from src import gs

# Пример использования
api_key = gs.credentials.openai.api_key
```

Это упрощает доступ к настройкам и учетным данным, делая код более чистым и удобным для использования.

## Примечания

- Модуль использует PyKeePass для работы с файлом `credentials.kdbx`.
- В коде присутствуют блоки обработки исключений (`ex`).
- Файл паролей (`password.txt`) содержит пароли в открытом виде. Это потенциальная уязвимость. Необходимо разработать механизм безопасного хранения паролей.
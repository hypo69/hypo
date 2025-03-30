# src.credentials

## Обзор

Модуль `src.credentials` содержит класс `ProgramSettings`, который является синглтоном и хранит основные параметры и настройки проекта, такие как пути к директориям, учетные данные для различных сервисов (Aliexpress, OpenAI, Gemini, Discord, Telegram, PrestaShop, SMTP, Facebook, GAPI, SerpAPI), а также общие настройки, такие как имя хоста.

## Подробнее

Этот модуль предназначен для централизованного хранения и управления настройками проекта. Он использует паттерн Singleton, чтобы гарантировать, что в приложении существует только один экземпляр класса `ProgramSettings`.
Модуль загружает конфигурацию из файла `config.json` и учетные данные из KeePass базы данных.
Он также определяет пути к различным директориям проекта и устанавливает переменные окружения.

## Классы

### `ProgramSettings`

**Описание**: Синглтон класс, предназначенный для хранения и управления настройками программы.

**Методы**:
- `__post_init__`: Выполняет инициализацию после создания экземпляра класса.
- `_load_credentials`: Загружает учетные данные из настроек.
- `_open_kp`: Открывает базу данных KeePass.
- `_load_aliexpress_credentials`: Загружает учетные данные Aliexpress API из KeePass.
- `_load_openai_credentials`: Загружает учетные данные OpenAI API из KeePass.
- `_load_gemini_credentials`: Загружает учетные данные GoogleAI API из KeePass.
- `_load_telegram_credentials`: Загружает учетные данные Telegram API из KeePass.
- `_load_discord_credentials`: Загружает учетные данные Discord API из KeePass.
- `_load_prestashop_credentials`: Загружает учетные данные PrestaShop API из KeePass.
- `_load_serpapi_credentials`: Загружает учетные данные SerpAPI API из KeePass.
- `_load_smtp_credentials`: Загружает учетные данные SMTP из KeePass.
- `_load_facebook_credentials`: Загружает учетные данные Facebook API из KeePass.
- `_load_gapi_credentials`: Загружает учетные данные Google API из KeePass.
- `now`: Возвращает текущую метку времени в формате год-месяц-день-часы-минуты-секунды-милисекунды.

**Параметры**:
- `host_name` (str): Имя хоста. По умолчанию `socket.gethostname()`.
- `base_dir` (Path): Базовая директория проекта. По умолчанию определяется функцией `set_project_root()`.
- `config` (SimpleNamespace): Объект, содержащий настройки из файла `config.json`.
- `credentials` (SimpleNamespace): Объект, содержащий учетные данные для различных сервисов.
- `path` (SimpleNamespace): Объект, содержащий пути к различным директориям проекта.
- `host` (str): Хост. По умолчанию `'127.0.0.1'`.

**Примеры**

```python
from src.credentials import ProgramSettings

# Получение экземпляра класса ProgramSettings
settings = ProgramSettings()

# Доступ к базовой директории проекта
print(settings.base_dir)

# Доступ к API ключу OpenAI
print(settings.credentials.openai.owner.api_key)

# Доступ к текущей метке времени
print(settings.now)
```

## Функции

### `set_project_root`

```python
def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.

    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.

     **Как работает функция**:
    Функция `set_project_root` определяет корневую директорию проекта, начиная поиск с директории, в которой расположен текущий файл.
    Она поднимается вверх по дереву директорий, пока не найдет директорию, содержащую один из файлов-маркеров (по умолчанию '__root__' или '.git').
    Если такая директория найдена, она считается корневой директорией проекта. Если корневая директория не найдена, функцией возвращается директория, где расположен скрипт.

    После определения корневой директории, если её нет в `sys.path`, она добавляется в начало списка путей поиска модулей, чтобы обеспечить возможность импорта модулей из корневой директории.
    """
```

**Описание**: Находит корневую директорию проекта, начиная с директории текущего файла, и останавливается на первой директории, содержащей любой из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple): Имена файлов или директорий, используемые для определения корневой директории проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневой директории, если она найдена, иначе - директория, где расположен скрипт.

**Примеры**:

```python
from src.credentials import set_project_root
from pathlib import Path

# Определение корневой директории проекта
root_dir = set_project_root()
print(f"Root directory: {root_dir}")

# Определение корневой директории с использованием пользовательских файлов-маркеров
root_dir = set_project_root(marker_files=('my_marker_file',))
print(f"Root directory with custom markers: {root_dir}")
```

### `singleton`

```python
def singleton(cls):
    """Args:
        cls (_type_): _description_

    Returns:
        _type_: _description_

     **Как работает функция**:
    Декоратор `singleton` гарантирует, что класс, к которому он применяется, будет иметь только один экземпляр.
    При первом вызове декорированной функции `get_instance` создается экземпляр класса и сохраняется в словаре `instances`.
    При последующих вызовах возвращается уже созданный экземпляр из словаря.
    """
```

**Описание**: Декоратор для реализации Singleton.

**Параметры**:
- `cls`: Класс, для которого нужно реализовать Singleton.

**Примеры**:

```python
from src.credentials import singleton

@singleton
class MyClass:
    def __init__(self):
        self.value = 0

# Получение экземпляров класса
instance1 = MyClass()
instance2 = MyClass()

# Проверка, что это один и тот же объект
print(instance1 is instance2)  # Вывод: True
```

### `gs`

**Описание**: Глобальный экземпляр класса `ProgramSettings`.

```python
# Global instance of ProgamSettings
gs: ProgramSettings = ProgramSettings()
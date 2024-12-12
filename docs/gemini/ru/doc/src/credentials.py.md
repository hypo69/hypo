# `credentials.py`

## Обзор

Модуль `credentials.py` содержит глобальные настройки проекта, включая пути, логины, пароли и настройки API. Он использует `pydantic` для управления настройками и `PyKeePass` для безопасного хранения учетных данных. Также реализован паттерн Singleton для класса `ProgramSettings`.

## Содержание

- [Классы](#Классы)
    - [`ProgramSettings`](#ProgramSettings)
- [Функции](#Функции)
    - [`set_project_root`](#set_project_root)
    - [`singleton`](#singleton)

## Классы

### `ProgramSettings`

**Описание**:

`ProgramSettings` - класс настроек программы. Это синглтон, который хранит основные параметры и настройки проекта. Он отвечает за загрузку конфигурации, учетных данных и управление путями проекта.

**Параметры**:

- `host_name` (str): Имя хоста, на котором запущена программа. По умолчанию получается с помощью `socket.gethostname()`.
- `base_dir` (Path): Корневой каталог проекта. По умолчанию определяется с помощью `set_project_root()`.
- `config` (SimpleNamespace): Конфигурация проекта, загружается из `config.json`.
- `credentials` (SimpleNamespace): Учетные данные для различных сервисов, таких как AliExpress, PrestaShop, OpenAI, и др.
- `MODE` (str): Режим работы программы (например, `dev`, `prod`). По умолчанию `dev`.
- `path` (SimpleNamespace): Пути к различным директориям проекта, таким как `root`, `src`, `bin`, `log`, `tmp` и другие.

**Методы**:

- `__init__(self, **kwargs)`: Инициализирует экземпляр класса, загружает конфигурацию, устанавливает пути и загружает учетные данные.
- `_load_credentials(self) -> None`: Загружает учетные данные из KeePass.
- `_open_kp(self, retry: int = 3) -> PyKeePass | None`: Открывает базу данных KeePass.
- `_load_aliexpress_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные для AliExpress.
- `_load_openai_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные для OpenAI.
- `_load_gemini_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные для Google Gemini.
- `_load_telegram_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные для Telegram.
- `_load_discord_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные для Discord.
- `_load_PrestaShop_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные для PrestaShop.
- `_load_presta_translations_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные для PrestaShop Translations.
- `_load_smtp_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные для SMTP.
- `_load_facebook_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные для Facebook.
- `_load_gapi_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные для Google API.
- `now(self) -> str`: Возвращает текущую метку времени в формате год-месяц-день-часы-минуты-секунды-милисекунды.

## Функции

### `set_project_root`

**Описание**:

Функция `set_project_root` находит корневой каталог проекта, начиная с текущей директории файла и двигаясь вверх по структуре каталогов. Поиск останавливается при нахождении одного из маркерных файлов.

**Параметры**:

- `marker_files` (tuple): Кортеж имен файлов или каталогов, которые являются маркерами корневого каталога проекта. По умолчанию `('pyproject.toml', 'requirements.txt', '.git')`.

**Возвращает**:

- `Path`: Путь к корневому каталогу проекта. Если маркерные файлы не найдены, возвращает директорию, где расположен скрипт.

### `singleton`

**Описание**:

Декоратор `singleton` реализует паттерн Singleton. Он гарантирует, что класс будет иметь только один экземпляр.

**Параметры**:

- `cls`: Класс, к которому применяется декоратор.

**Возвращает**:

- `Callable`: Функция, которая возвращает единственный экземпляр класса.
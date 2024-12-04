# Модуль hypotez/src/credentials.py

## Обзор

Этот модуль содержит реализацию класса `ProgramSettings`, предназначенного для хранения и управления глобальными настройками проекта.  Класс является синглтоном и обеспечивает доступ к пути к проекту, данным конфигурации, учетным данным (из KeePass) и другим важным параметрам.

## Классы

### `ProgramSettings`

**Описание**: Класс `ProgramSettings` представляет собой синглтон, хранящий глобальные настройки проекта, такие как пути к файлам, API-ключи и другие конфигурационные параметры.  Настройки загружаются из файла `config.json`.

**Атрибуты**:

- `base_dir (Path)`: Путь к корневой директории проекта.  Используется по умолчанию `set_project_root()`.
- `config (SimpleNamespace)`: Объект, хранящий данные конфигурации, загруженные из файла `config.json`.
- `credentials (SimpleNamespace)`: Объект, содержащий различные учетные данные, загруженные из KeePass.
- `MODE (str)`: Режим работы проекта (например, 'dev' или 'prod').
- `path (SimpleNamespace)`: Объект, содержащий пути к различным директориям проекта.


**Методы**:

- `__init__(self, **kwargs)`: Конструктор класса.  Выполняет инициализацию после создания экземпляра класса, включая загрузку настроек из `config.json` и учетных данных из KeePass.
- `_load_credentials(self) -> None`: Загружает учетные данные из базы данных KeePass.
- `_open_kp(self, retry: int = 3) -> PyKeePass | None`: Открывает базу данных KeePass. Обрабатывает возможные исключения с помощью цикла `while`.
- `_load_aliexpress_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные AliExpress из KeePass.
- `_load_openai_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные OpenAI из KeePass.
- `_load_gemini_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные GoogleAI из KeePass.
- `_load_telegram_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные Telegram из KeePass.
- `_load_discord_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные Discord из KeePass.
- `_load_PrestaShop_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные PrestaShop из KeePass.
- `_load_presta_translations_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные PrestaShop для переводов из KeePass.
- `_load_smtp_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные SMTP из KeePass.
- `_load_facebook_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные Facebook из KeePass.
- `_load_gapi_credentials(self, kp: PyKeePass) -> bool`: Загружает учетные данные Google API из KeePass.
- `now(self, dformat: str = '%y_%m_%d_%H_%M_%S_%f') -> str`: Возвращает текущую метку времени в заданном формате.

## Функции

### `set_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git')) -> Path`

**Описание**: Находит корневую директорию проекта, начиная с текущей директории и поднимаясь вверх по иерархии директорий. Останавливается на первой директории, содержащей любой из указанных маркеров.

**Параметры**:

- `marker_files (tuple):` Список файлов или каталогов, которые используются для определения корневой директории проекта.

**Возвращает**:

- `Path`: Путь к корневой директории проекта, если найдена, иначе текущая директория.

### `singleton(cls)`

**Описание**: Декоратор для реализации Singleton-паттерна.

**Параметры**:

- `cls`: Класс, который должен быть синглтоном.


**Примечания**:

- Модуль использует библиотеки `pydantic`, `pykeepass`, `pathlib`, и другие для работы с настройками и учетными данными.
- Подробные комментарии в коде описывают функциональность и возможные ошибки.
- Обработка исключений при взаимодействии с KeePass реализована с повторами (retry).
- Документация для методов `_load_*_credentials`  полностью соответствует заданному формату.
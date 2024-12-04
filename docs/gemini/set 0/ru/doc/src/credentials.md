# Модуль credentials

## Обзор

Модуль `credentials` отвечает за загрузку и хранение учетных данных для различных сервисов (AliExpress, OpenAI, Telegram, Discord и др.) из базы данных KeePass. Он также определяет корневой каталог проекта и предоставляет методы для работы с настройками.

## Классы

### `ProgramSettings`

**Описание**:  Класс `ProgramSettings` представляет собой синглтон, хранящий основные настройки проекта, включая пути к файлам, учетные данные и параметры конфигурации.

**Параметры**:
- `base_dir` (Path): Путь к корневому каталогу проекта, по умолчанию определяется автоматически.
- `config` (SimpleNamespace): Объект, хранящий дополнительные настройки, загруженные из файла `config.json`.
- `credentials` (SimpleNamespace): Объект, содержащий учетные данные для различных сервисов.
- `MODE` (str): Режим работы приложения (по умолчанию 'development').
- `path` (SimpleNamespace): Объект, содержащий пути к различным директориям проекта.

**Методы**:
- `__init__(self, **kwargs)`: Конструктор класса. Инициализирует объекты `config` и `path`, загружает данные из `config.json`, проверяет наличие новой версии ПО и загружает учетные данные из KeePass.
- `_load_credentials(self)`: Метод загружает учетные данные из KeePass для различных сервисов.
- `_open_kp(self, retry: int = 3)`: Открывает базу данных KeePass с определенным количеством попыток.
- `_load_aliexpress_credentials(self, kp: PyKeePass)`: Загружает учетные данные AliExpress из KeePass.
- `_load_openai_credentials(self, kp: PyKeePass)`: Загружает учетные данные OpenAI из KeePass.
- `_load_gemini_credentials(self, kp: PyKeePass)`: Загружает учетные данные GoogleAI из KeePass.
- `_load_telegram_credentials(self, kp: PyKeePass)`: Загружает учетные данные Telegram из KeePass.
- `_load_discord_credentials(self, kp: PyKeePass)`: Загружает учетные данные Discord из KeePass.
- `_load_PrestaShop_credentials(self, kp: PyKeePass)`: Загружает учетные данные PrestaShop из KeePass.
- `_load_presta_translations_credentials(self, kp: PyKeePass)`: Загружает учетные данные для переводов PrestaShop из KeePass.
- `_load_smtp_credentials(self, kp: PyKeePass)`: Загружает учетные данные SMTP из KeePass.
- `_load_facebook_credentials(self, kp: PyKeePass)`: Загружает учетные данные Facebook из KeePass.
- `_load_gapi_credentials(self, kp: PyKeePass)`: Загружает учетные данные Google API из KeePass.
- `now(self, dformat: str = '%y_%m_%d_%H_%M_%S_%f')`: Возвращает текущую метку времени в указанном формате.


## Функции

### `set_project_root(marker_files=...)`

**Описание**:  Находит корневой каталог проекта, начиная от текущего каталога.

**Параметры**:
- `marker_files (tuple)`: Список файлов или каталогов, указывающих на корневой каталог проекта.

**Возвращает**:
- `Path`: Путь к корневому каталогу проекта, или текущий каталог, если корень не найден.


### `singleton(cls)`

**Описание**:  Декоратор для реализации паттерна Singleton.

**Параметры**:
- `cls`: Класс, для которого требуется реализовать Singleton.

**Возвращает**:
- `function`: Функция, которая возвращает единственный экземпляр класса.


**Замечания:**

Файл содержит большое количество методов для загрузки учетных данных из KeePass, которые реализованы как методы класса `ProgramSettings`.  Описание каждого метода содержит аргументы, возвращаемые значения и потенциальные исключения. Документирование исключений, вызываемых методами, очень важно для корректной работы программы.  Также важно проработать логику обработки ошибок при загрузке данных и ситуаций, когда KeePass не доступен.
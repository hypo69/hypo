# Модуль hypotez/src/credentials.py

## Обзор

Данный модуль содержит определения классов и функций для работы с настройками проекта.  Он отвечает за получение, хранение и обработку ключевых параметров, таких как пути к файлам, пароли, API-ключи и другие конфигурационные данные. Модуль использует KeePass для хранения секретных данных и обеспечивает надежное управление ими.

## Классы

### `ProgramSettings`

**Описание**: Класс `ProgramSettings` представляет собой синглтон, хранящий глобальные настройки проекта.  Этот класс содержит пути к важным каталогам, API-ключи и другие критически важные данные, полученные из KeePass.

**Атрибуты**:

- `host_name` (str): Имя хоста системы.
- `base_dir` (Path): Корневой каталог проекта.  Использует функцию `set_project_root` для определения этого каталога.
- `config` (SimpleNamespace): Настройки проекта, загружаемые из файла `config.json`.
- `credentials` (SimpleNamespace): Объект, содержащий учетные данные для различных сервисов (AliExpress, OpenAI, etc.).  Представлен в виде вложенных объектов `SimpleNamespace` для более гибкого доступа.
- `MODE` (str): Режим работы проекта (например, 'dev', 'prod').
- `path` (SimpleNamespace): Содержит пути к важным каталогам проекта (src, bin, log, tmp, data, secrets, etc.).  Эти пути вычисляются относительно `base_dir`.

**Методы**:

- `__init__(self, **kwargs)`: Инициализатор класса. Загружает настройки из `config.json`, проверяет наличие новой версии проекта и загружает учетные данные из KeePass с использованием вспомогательных методов (`_load_credentials`, `_open_kp`, и т.д.)
- `_load_credentials(self)`: Загружает все учетные данные из базы данных KeePass.
- `_open_kp(self, retry = 3)`: Открывает базу данных KeePass. Использует механизм повторных попыток.
- `_load_aliexpress_credentials(self, kp: PyKeePass)`: Загружает учетные данные Aliexpress из KeePass.
- `_load_openai_credentials(self, kp: PyKeePass)`: Загружает учетные данные OpenAI из KeePass.
- `_load_gemini_credentials(self, kp: PyKeePass)`: Загружает учетные данные GoogleAI из KeePass.
- `_load_telegram_credentials(self, kp: PyKeePass)`: Загружает учетные данные Telegram из KeePass.
- `_load_discord_credentials(self, kp: PyKeePass)`: Загружает учетные данные Discord из KeePass.
- `_load_PrestaShop_credentials(self, kp: PyKeePass)`: Загружает учетные данные PrestaShop из KeePass.
- `_load_presta_translations_credentials(self, kp: PyKeePass)`: Загружает учетные данные для PrestaShop переводов из KeePass.
- `_load_smtp_credentials(self, kp: PyKeePass)`: Загружает учетные данные SMTP из KeePass.
- `_load_facebook_credentials(self, kp: PyKeePass)`: Загружает учетные данные Facebook из KeePass.
- `_load_gapi_credentials(self, kp: PyKeePass)`: Загружает учетные данные Google API из KeePass.
- `now(self, dformat = '%y_%m_%d_%H_%M_%S_%f')`: Возвращает текущую метку времени в указанном формате.


## Функции

### `set_project_root(marker_files=...)`

**Описание**: Определяет корневой каталог проекта, начиная с текущего каталога и двигаясь вверх по иерархии каталогов.

**Параметры**:
- `marker_files`: Кортеж имен файлов или каталогов, которые указывают на корневой каталог проекта.

**Возвращает**:
- `Path`: Путь к корневому каталогу проекта.

### `singleton(cls)`

**Описание**: Декоратор для реализации паттерна Singleton.

**Параметры**:
- `cls`: Класс, для которого необходимо реализовать Singleton.

**Возвращает**:
- Функция: Функция, которая возвращает экземпляр класса.


## Обработка исключений

Все методы, работающие с KeePass, содержат обработку исключений с использованием ключевого слова `ex`.  Это указывает на наличие блока `try...except` для перехвата и обработки потенциальных ошибок при работе с KeePass.


```
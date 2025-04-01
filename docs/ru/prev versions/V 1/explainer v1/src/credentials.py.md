## ИНСТРУКЦИЯ:

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:  

1. **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.  
2. **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости, 
    которые импортируются при создании диаграммы. 
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`, 
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!  
    
    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:\
    ```mermaid\
    flowchart TD\
        Start --> Header[<code>header.py</code><br> Determine Project Root]\
    \
        Header --> import[Import Global Settings: <br><code>from src import gs</code>] \
    ```

3. **<объяснение>**: Предоставьте подробные объяснения:  
   - **Импорты**: Их назначение и взаимосвязь с другими пакетами `src.`.  
   - **Классы**: Их роль, атрибуты, методы и взаимодействие с другими компонентами проекта.  
   - **Функции**: Их аргументы, возвращаемые значения, назначение и примеры.  
   - **Переменные**: Их типы и использование.  
   - Выделите потенциальные ошибки или области для улучшения.  

Дополнительно, постройте цепочку взаимосвязей с другими частями проекта (если применимо).  

Это обеспечивает всесторонний и структурированный анализ кода.
## Формат ответа: `.md` (markdown)
**КОНЕЦ ИНСТРУКЦИИ**
### <алгоритм>
1.  **`set_project_root(marker_files)`**:
    *   Начало: Получает путь к текущему файлу и определяет его родительский каталог как начальный путь проекта.
    *   Итерация по родительским каталогам: Перебирает каталоги вверх по иерархии, начиная с текущего и до корневого.
    *   Проверка маркеров: Для каждого каталога проверяет наличие файлов или директорий из `marker_files` (по умолчанию `__root__` или `.git`).
        *   Пример: Если `marker_files` содержит `'.git'`, то функция ищет `.git` в каждом родительском каталоге.
    *   Обновление корня: Если маркер найден, обновляет корень проекта и прерывает итерацию.
        *   Пример: Если `.git` найден в `/home/user/project`, то `/home/user/project` становится корнем проекта.
    *   Добавление корня в `sys.path`: Добавляет путь к корневому каталогу в `sys.path`, если его там нет.
    *   Возврат: Возвращает путь к корневому каталогу проекта.
        *   Пример: `/home/user/project`
2.  **`singleton(cls)`**:
    *   Декоратор: Оборачивает класс `cls` для реализации паттерна "Singleton".
    *   Создание экземпляров: Внутренняя функция `get_instance` управляет созданием и возвратом экземпляров класса.
    *   Возврат экземпляра: Если экземпляр уже существует, возвращает его; иначе создает новый, сохраняет его и возвращает.
3.  **`ProgramSettings`**:
    *   Синглтон: Класс использует декоратор `@singleton` для гарантии единственного экземпляра.
    *   `__init__`:
        *   `host_name`: Определяет имя хоста.
        *   `base_dir`: Вызывает `set_project_root` для определения корня проекта.
        *   `config`: Инициализируется пустым `SimpleNamespace`.
        *   `credentials`: Инициализируется вложенным `SimpleNamespace` для различных сервисов (aliexpress, presta, openai и т.д.)
        *   `MODE`: Устанавливается в `dev`.
        *   `path`:  Инициализируется `SimpleNamespace` для хранения путей проекта.
    *   `__post_init__`:
        *   Загрузка конфигурации: Вызывает `j_loads_ns` для загрузки `config.json` из каталога `src`.
        *   Установка атрибутов: Устанавливает атрибуты `timestamp_format` и `project_name` в `config`.
        *   Установка путей: Задает пути к директориям `root`, `bin`, `src`, `log`, `tmp`, `data`, `secrets`, `google_drive` и `external_storage` через `self.path`.
        *   Проверка обновлений: Вызывает `check_latest_release`.
        *   Установка `MODE`: Задает режим работы (`dev` или `prod`) из `config`.
        *   Добавление путей к бинарникам в `sys.path`: Добавляет пути к бинарникам в системный `path`, если их там нет.
        *   Установка переменной окружения: Устанавливает `WEASYPRINT_DLL_DIRECTORIES` для GTK.
        *   Отключение предупреждений: Подавляет предупреждения GTK.
        *   Загрузка учетных данных: Вызывает `_load_credentials`.
    *   `_load_credentials`:
        *   Открывает KeePass: Вызывает `_open_kp` для открытия базы данных KeePass.
        *   Загружает учетные данные: Вызывает методы для загрузки учетных данных для разных сервисов (aliexpress, openai, gemini, discord и т.д.).
    *   `_open_kp`:
        *   Цикл: Пытается открыть базу данных KeePass до `retry` раз (по умолчанию 3).
        *   Чтение пароля: Пытается прочитать пароль из `password.txt`, если файла нет или он пустой - запросит пароль у пользователя через консоль.
        *   Открытие базы данных: Использует `PyKeePass` для открытия базы данных.
        *   Возврат: Возвращает экземпляр `PyKeePass` или `None` в случае неудачи.
    *   Методы `_load_*_credentials`:
        *   Поиск: Ищет нужные записи в KeePass базе данных по группам.
        *   Извлечение данных: Извлекает данные (api_key, secret, и т.д.) из custom_properties записей.
        *   Установка значений: Устанавливает значения в соответствующий атрибут объекта `credentials`.
    *   `now` (property):
        *   Форматирование времени: Возвращает текущее время в формате, определенном в настройках `config.timestamp_format`.

### <mermaid>
```mermaid
flowchart TD
    Start[Start] --> FindRoot[set_project_root]
    FindRoot --> SingletonDecorator[singleton]
    SingletonDecorator --> ProgramSettingsClass[ProgramSettings class]
    ProgramSettingsClass --> Init[__init__]
    Init --> SetHostName[Set host_name]
    Init --> SetBaseDir[Set base_dir (set_project_root)]
    Init --> CreateConfigNS[Create config SimpleNamespace]
    Init --> CreateCredentialsNS[Create credentials SimpleNamespace]
    Init --> SetMode[Set MODE = 'dev']
    Init --> CreatePathNS[Create path SimpleNamespace]
    Init --> PostInit[__post_init__]
    PostInit --> LoadConfig[Load config.json (j_loads_ns)]
    PostInit --> SetTimestampFormat[Set timestamp_format]
    PostInit --> SetProjectName[Set project_name]
    PostInit --> SetProjectPaths[Set project paths (root, bin, src, etc.)]
    PostInit --> CheckRelease[check_latest_release]
    PostInit --> SetModeFromConfig[Set MODE from config]
    PostInit --> AddBinaryPaths[Add binary paths to sys.path]
    PostInit --> SetEnvVars[Set WEASYPRINT_DLL_DIRECTORIES env var]
    PostInit --> SuppressWarnings[Suppress GTK warnings]
    PostInit --> LoadCredentials[_load_credentials]
    LoadCredentials --> OpenKeePass[_open_kp]
    OpenKeePass --> ReadPassword[Read password from file or getpass]
    OpenKeePass --> OpenKP[Open KeePass db]
    OpenKeePass --> CheckSuccess[Check if KP opening success]
    CheckSuccess -- Success --> LoadAliexpressCredentials[_load_aliexpress_credentials]
    LoadAliexpressCredentials --> FindAliexpressEntry[Find Aliexpress entry]
    LoadAliexpressCredentials --> SetAliexpressCredentials[Set aliexpress credentials]
    CheckSuccess -- Failed --> Exit[Exit with error]
    LoadAliexpressCredentials --> LoadOpenAICredentials[_load_openai_credentials]
     LoadOpenAICredentials --> FindOpenAIEntry[Find OpenAI entry]
    LoadOpenAICredentials --> SetOpenAICredentials[Set OpenAI credentials]
    LoadOpenAICredentials --> LoadGeminiCredentials[_load_gemini_credentials]
     LoadGeminiCredentials --> FindGeminiEntry[Find Gemini entry]
    LoadGeminiCredentials --> SetGeminiCredentials[Set Gemini credentials]
     LoadGeminiCredentials --> LoadDiscordCredentials[_load_discord_credentials]
      LoadDiscordCredentials --> FindDiscordEntry[Find Discord entry]
    LoadDiscordCredentials --> SetDiscordCredentials[Set Discord credentials]
     LoadDiscordCredentials --> LoadTelegramCredentials[_load_telegram_credentials]
      LoadTelegramCredentials --> FindTelegramEntry[Find Telegram entry]
    LoadTelegramCredentials --> SetTelegramCredentials[Set Telegram credentials]
     LoadTelegramCredentials --> LoadPrestashopCredentials[_load_prestashop_credentials]
      LoadPrestashopCredentials --> FindPrestashopEntry[Find Prestashop entry]
    LoadPrestashopCredentials --> SetPrestashopCredentials[Set Prestashop credentials]
     LoadPrestashopCredentials --> LoadSMTPCredentials[_load_smtp_credentials]
      LoadSMTPCredentials --> FindSMTPEntry[Find SMTP entry]
    LoadSMTPCredentials --> SetSMTPCredentials[Set SMTP credentials]
    LoadSMTPCredentials --> LoadFacebookCredentials[_load_facebook_credentials]
      LoadFacebookCredentials --> FindFacebookEntry[Find Facebook entry]
    LoadFacebookCredentials --> SetFacebookCredentials[Set Facebook credentials]
    LoadFacebookCredentials --> LoadPrestaTranslationsCredentials[_load_presta_translations_credentials]
        LoadPrestaTranslationsCredentials --> FindPrestaTranslationsEntry[Find Presta Translations entry]
    LoadPrestaTranslationsCredentials --> SetPrestaTranslationsCredentials[Set Presta Translations credentials]
    LoadPrestaTranslationsCredentials --> LoadGAPICredentials[_load_gapi_credentials]
        LoadGAPICredentials --> FindGAPIEntry[Find GAPI entry]
    LoadGAPICredentials --> SetGAPICredentials[Set GAPI credentials]    
    LoadGAPICredentials --> End[End]

    subgraph "Credentials Loading Flow"
    LoadCredentials
    OpenKeePass
        ReadPassword
    OpenKP
     CheckSuccess
        LoadAliexpressCredentials
        LoadOpenAICredentials
        LoadGeminiCredentials
        LoadDiscordCredentials
        LoadTelegramCredentials
        LoadPrestashopCredentials
        LoadSMTPCredentials
        LoadFacebookCredentials
        LoadPrestaTranslationsCredentials
         LoadGAPICredentials
        Exit
    end
    subgraph "Program Initialization"
    Start
        FindRoot
        SingletonDecorator
        ProgramSettingsClass
        Init
        SetHostName
        SetBaseDir
         CreateConfigNS
        CreateCredentialsNS
         SetMode
        CreatePathNS
        PostInit
         LoadConfig
        SetTimestampFormat
         SetProjectName
         SetProjectPaths
         CheckRelease
         SetModeFromConfig
         AddBinaryPaths
         SetEnvVars
         SuppressWarnings
    end
    
    
```
**Импорты для `mermaid` диаграммы:**

*   `Start`: Начало процесса.
*   `set_project_root`: Функция для определения корня проекта.
*   `singleton`: Декоратор для реализации паттерна Singleton.
*   `ProgramSettings class`: Класс настроек программы.
*   `__init__`: Метод инициализации класса.
*    `host_name`: Имя хоста.
    `base_dir`: Базовый каталог проекта.
    `config`: SimpleNamespace для конфигураций.
    `credentials`: SimpleNamespace для учетных данных.
    `MODE`: Режим работы.
    `path`: SimpleNamespace для путей.
*   `__post_init__`: Метод, вызываемый после инициализации.
*   `j_loads_ns`: Функция для загрузки JSON в SimpleNamespace.
*   `check_latest_release`: Функция для проверки обновлений.
*   `_load_credentials`: Метод для загрузки учетных данных.
*   `_open_kp`: Метод для открытия базы данных KeePass.
*   `_load_*_credentials`: Методы для загрузки учетных данных для различных сервисов.
*   `Read password from file or getpass`: Описание процесса считывания пароля из файла `password.txt` или запроса через `getpass.getpass()`
*    `Open KeePass db`: Описание процесса открытия базы данных `PyKeePass`
*    `Check if KP opening success`: Проверка на успешное открытие базы данных. В случае ошибки, происходит выход из программы с ошибкой.
* `Exit`: Завершение программы в случае ошибки.
*   `End`: Конец процесса.
### <объяснение>
**Импорты:**

*   `datetime` (из `datetime`): Используется для работы с датой и временем, в частности для получения текущей метки времени.
*   `getpass`: Используется для безопасного получения пароля из консоли.
*   `os`: Обеспечивает взаимодействие с операционной системой, например, для работы с путями и переменными окружения.
*   `sys`: Предоставляет доступ к системным переменным и функциям, например, `sys.path` для работы с путями импорта.
*   `json`: Используется для работы с JSON-данными.
*   `warnings`: Используется для управления предупреждениями, в частности для подавления предупреждений GTK.
*   `socket`: Используется для получения имени хоста.
*   `dataclasses` (из `dataclasses`): Используется для создания классов данных (`ProgramSettings`) с автоматической генерацией методов.
*   `pathlib` (из `pathlib`): Используется для работы с путями файлов и каталогов.
*   `types` (из `types`): Используется для создания динамических объектов (`SimpleNamespace`).
*   `typing`: Используется для определения типов переменных и аргументов функций.
*   `pykeepass` (из `pykeepass`): Используется для работы с базой данных KeePass.
*   `src.check_release`: Логика проверки обновлений
*   `src.logger.logger`: Используется для логирования событий.
*   `src.logger.exceptions`: Набор кастомных исключений.
*   `src.utils.file`: Утилиты для работы с файлами.
*   `src.utils.jjson`: Утилиты для работы с JSON.
*   `src.utils.printer`: Утилиты для вывода на печать.

**Классы:**

*   **`ProgramSettings`**:
    *   **Роль**: Класс настроек программы, реализованный как Singleton, чтобы обеспечить единственный экземпляр настроек.
    *   **Атрибуты**:
        *   `host_name` (`str`): Имя хоста.
        *   `base_dir` (`Path`): Корень проекта.
        *   `config` (`SimpleNamespace`): Настройки проекта, загруженные из `config.json`.
        *   `credentials` (`SimpleNamespace`): Учетные данные для различных сервисов.
        *   `MODE` (`str`): Режим работы (`dev` или `prod`).
        *   `path` (`SimpleNamespace`): Пути к различным каталогам проекта.
    *   **Методы**:
        *   `__init__`: Инициализирует атрибуты класса.
        *   `__post_init__`: Выполняет пост-инициализацию, загружает настройки, устанавливает пути, добавляет пути к бинарникам и вызывает `_load_credentials`.
        *   `_load_credentials`: Загружает учетные данные из KeePass.
        *   `_open_kp`: Открывает базу данных KeePass с возможностью повторных попыток.
        *   `_load_*_credentials`: Методы для загрузки учетных данных для различных сервисов (Aliexpress, OpenAI, Gemini, Discord, Telegram, Prestashop, SMTP, Facebook, Google API).
        *   `now` (property): Возвращает текущую метку времени в нужном формате.
    *   **Взаимодействие**:
        *   Использует `set_project_root` для определения корня проекта.
        *   Использует `src.utils.jjson` для загрузки конфигурации из JSON.
        *   Использует `src.logger.logger` для логирования.
        *   Использует `PyKeePass` для работы с базой данных KeePass.
        *   Вызывает `check_latest_release` для проверки обновлений.

**Функции:**

*   **`set_project_root(marker_files)`**:
    *   **Аргументы**: `marker_files` (`tuple`): Кортеж с именами файлов или каталогов, указывающих на корень проекта.
    *   **Возвращаемое значение**: `Path`: Путь к корню проекта.
    *   **Назначение**: Определяет корневой каталог проекта путем поиска маркеров (файлов или каталогов) в родительских каталогах.
*   **`singleton(cls)`**:
    *   **Аргументы**: `cls`: Класс, который нужно сделать синглтоном.
    *   **Возвращаемое значение**: `function`: Функция-декоратор.
    *   **Назначение**: Реализует шаблон синглтон для класса `cls`.

**Переменные:**
*   `gs` (`ProgramSettings`): Глобальный экземпляр класса `ProgramSettings`. Это синглтон, поэтому в проекте будет только один такой экземпляр.

**Потенциальные ошибки и области для улучшения:**

*   **Безопасность**: Хранение пароля в открытом виде в `password.txt` является уязвимостью. Рекомендуется использовать более безопасные методы, например, запрос пароля через `getpass` всегда и не сохранять его в файл.
*   **Обработка ошибок**: Многие методы загрузки учетных данных имеют обработку исключений, но только выводят сообщение в консоль и возвращают `False`, не давая возможности перехватить ошибку в вызывающем коде и корректно обработать ее. Целесообразно использовать кастомные исключения.
*   **Повторение кода**: Методы `_load_*_credentials` имеют много общего кода. Можно вынести общий функционал в отдельные вспомогательные функции.
*   **Жестко закодированные пути**: Использование литеральных строк для путей, таких как `'suppliers'`, `'aliexpress'`, `'api'` может привести к ошибкам если структура KeePass базы данных изменится. Целесообразно использовать константы.
*   **Ограничение функциональности**: Функция `set_project_root` при неудачном поиске возвращает путь, где находится скрипт. Это может привести к неожиданному поведению.
*   **Проверка обновлений:** `check_latest_release` не реализована до конца, необходимо реализовать логику что делать, когда есть новая версия на github.

**Взаимосвязь с другими частями проекта:**

*   `src.check_release`: Используется для проверки наличия обновлений проекта.
*   `src.logger`: Используется для логирования событий.
*   `src.utils`: Используется для различных утилит.
*   `config.json`: Файл конфигурации, содержащий различные настройки, пути и режимы работы.
*   `credentials.kdbx`: База данных KeePass с учетными данными для разных сервисов.

**Цепочка взаимосвязей:**
1.  Программа запускается.
2.  `set_project_root` определяет корневой каталог проекта, начиная с текущего файла.
3.  Декоратор `singleton` гарантирует, что `ProgramSettings` будет создан только один раз.
4.  Создается экземпляр `ProgramSettings`.
5.  `__init__` и `__post_init__` загружают конфигурацию, устанавливают пути и выполняют другие необходимые инициализации.
6.  `_load_credentials` открывает KeePass и загружает учетные данные из него.
7.  Учетные данные используются в других частях проекта для доступа к различным сервисам (API).
8.  В ходе работы используются `logger`, `file`, `jjson` и другие утилиты для логирования, работы с файлами и JSON.
9.  В любой момент можно получить текущее время через `gs.now`.

Таким образом, `credentials.py` является центральной точкой для инициализации и настройки проекта, а также для хранения и доступа к учетным данным.
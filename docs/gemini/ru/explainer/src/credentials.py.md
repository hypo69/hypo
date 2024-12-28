## ИНСТРУКЦИЯ:

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:

1. **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.
2. **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости,
    которые импортируются при создании диаграммы.
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`,
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!

    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:
    ```mermaid
    flowchart TD
        Start --> Header[<code>header.py</code><br> Determine Project Root]

        Header --> import[Import Global Settings: <br><code>from src import gs</code>]
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
```markdown
## <алгоритм>

1.  **Начало**:
    *   Устанавливается режим работы `MODE` как `dev`.
    *   Импортируются необходимые модули, включая стандартные библиотеки Python, `pydantic`, `pykeepass`, и модули из пакета `src`.
2.  **`set_project_root`**:
    *   Определяется корневая директория проекта.
    *   Начинается поиск от директории текущего файла.
    *   Ищет родительские директории, содержащие файлы-маркеры (по умолчанию `__root__`).
        *   Пример: Если текущий файл находится в `hypotez/src/credentials.py`, а маркер `__root__` есть в `hypotez`, то `hypotez` будет корневой директорией.
    *   Возвращает найденный путь или путь директории текущего файла, если не найден маркер.
    *   Добавляет корневой путь в `sys.path`, чтобы другие модули могли быть импортированы.
3.  **`singleton` (декоратор)**:
    *   Декоратор используется для реализации паттерна Singleton.
    *   Гарантирует, что у класса будет только один экземпляр.
4.  **`ProgramSettings` (класс)**:
    *   Класс для хранения глобальных настроек проекта.
        *   Экземпляр создается один раз благодаря декоратору `@singleton`.
    *   Атрибуты:
        *   `host_name`: Имя хоста.
        *   `base_dir`: Корневая директория проекта (определяется функцией `set_project_root`).
        *   `config`: Настройки, загруженные из `config.json`.
        *   `credentials`: Учетные данные для различных сервисов (aliexpress, presta, openai, и т.д.).
        *   `MODE`: Режим работы (dev, test, prod).
        *   `path`: Пути к важным директориям проекта.
    *   Метод `__init__`:
        *   Загружает настройки из `config.json`.
        *   Инициализирует пути на основе `base_dir` и `config`.
            *   Пример: `self.path.src` = `Path(self.base_dir) / 'src'`.
        *   Проверяет наличие новой версии на GitHub.
        *   Добавляет пути к бинарникам в `sys.path` для использования бинарных файлов (ffmpeg, wkhtmltopdf).
        *   Подавляет предупреждения GTK.
        *   Вызывает `_load_credentials` для загрузки учетных данных.
    *   Метод `_load_credentials`:
        *   Открывает базу данных KeePass (`_open_kp`).
        *   Загружает учетные данные для различных сервисов (aliexpress, openai, и т.д.) из KeePass.
    *   Метод `_open_kp`:
        *   Открывает базу данных KeePass.
        *   Читает пароль из файла `password.txt` или запрашивает у пользователя.
    *   Методы `_load_*_credentials`:
        *   Загружают учетные данные из KeePass для каждого сервиса.
            *   Пример: `_load_aliexpress_credentials` получает ключи API, секрет, ID отслеживания, email и пароль из KeePass и записывает их в `self.credentials.aliexpress`.
    *   Метод `now`:
        *   Возвращает текущую метку времени в определенном формате.
5.  **Глобальный Экземпляр `gs`**:
    *   Создаётся глобальный экземпляр `ProgramSettings` как `gs`.

## <mermaid>

```mermaid
flowchart TD
    Start[Start] --> FindProjectRoot
    FindProjectRoot[set_project_root()] --> SingletonDecorator
    SingletonDecorator[singleton] --> ProgramSettingsClass
    ProgramSettingsClass[class ProgramSettings] --> InitMethod
    InitMethod[__init__()] --> LoadConfig
    LoadConfig[Load config.json <br> j_loads_ns()] --> SetProjectPaths
    SetProjectPaths[Set project paths] --> CheckLatestRelease
    CheckLatestRelease[check_latest_release()] --> AddBinPaths
    AddBinPaths[Add binary paths to sys.path] --> SuppressGtkWarnings
    SuppressGtkWarnings[Suppress GTK warnings] --> LoadCredentials
    LoadCredentials[_load_credentials()] --> OpenKeePass
     OpenKeePass[_open_kp()]-->LoadAliexpressCredentials
    LoadAliexpressCredentials[_load_aliexpress_credentials()]-->LoadOpenAICredentials
     LoadOpenAICredentials[_load_openai_credentials()]-->LoadGeminiCredentials
    LoadGeminiCredentials[_load_gemini_credentials()]-->LoadDiscordCredentials
    LoadDiscordCredentials[_load_discord_credentials()]-->LoadTelegramCredentials
     LoadTelegramCredentials[_load_telegram_credentials()]-->LoadPrestaShopCredentials
     LoadPrestaShopCredentials[_load_PrestaShop_credentials()]-->LoadSmtpCredentials
    LoadSmtpCredentials[_load_smtp_credentials()]-->LoadFacebookCredentials
    LoadFacebookCredentials[_load_facebook_credentials()]-->LoadPrestaTranslationsCredentials
    LoadPrestaTranslationsCredentials[_load_presta_translations_credentials()]-->LoadGapiCredentials
    LoadGapiCredentials[_load_gapi_credentials()]--> CreateGlobalInstance
    CreateGlobalInstance[gs: ProgramSettings = ProgramSettings()] --> End
    End[End]

  
    subgraph KeePass Interaction
    OpenKeePass
     LoadAliexpressCredentials
    LoadOpenAICredentials
    LoadGeminiCredentials
    LoadDiscordCredentials
     LoadTelegramCredentials
    LoadPrestaShopCredentials
     LoadSmtpCredentials
     LoadFacebookCredentials
    LoadPrestaTranslationsCredentials
    LoadGapiCredentials
    end
   
   
```

**Анализ зависимостей Mermaid:**

1.  `Start`: Начало выполнения программы.
2.  `FindProjectRoot`: Функция `set_project_root()` определяет корневую директорию проекта.
3.  `SingletonDecorator`: Декоратор `singleton` обеспечивает, что класс `ProgramSettings` будет иметь только один экземпляр.
4.  `ProgramSettingsClass`: Определение класса `ProgramSettings`, который содержит настройки программы.
5.  `InitMethod`: Метод `__init__` класса `ProgramSettings` – конструктор, вызываемый при создании экземпляра класса.
6.  `LoadConfig`: Загружает конфигурационные данные из файла `config.json` с помощью `j_loads_ns`.
7.  `SetProjectPaths`: Инициализирует пути к различным директориям проекта (bin, src, log, tmp, etc.)
8. `CheckLatestRelease`: Проверяет наличие новой версии проекта на GitHub.
9.  `AddBinPaths`: Добавляет пути к бинарным файлам в переменную окружения `sys.path`.
10. `SuppressGtkWarnings`: Подавляет предупреждения библиотеки GTK, чтобы они не отображались в консоли.
11. `LoadCredentials`: Запускает процесс загрузки учетных данных из KeePass, вызывая метод `_load_credentials()`.
12. `OpenKeePass`: Открывает базу данных KeePass с помощью функции `_open_kp`.
13. `LoadAliexpressCredentials`: Загружает учетные данные для Aliexpress.
14. `LoadOpenAICredentials`: Загружает учетные данные для OpenAI.
15. `LoadGeminiCredentials`: Загружает учетные данные для Gemini.
16. `LoadDiscordCredentials`: Загружает учетные данные для Discord.
17. `LoadTelegramCredentials`: Загружает учетные данные для Telegram.
18. `LoadPrestaShopCredentials`: Загружает учетные данные для PrestaShop.
19. `LoadSmtpCredentials`: Загружает учетные данные для SMTP.
20. `LoadFacebookCredentials`: Загружает учетные данные для Facebook.
21. `LoadPrestaTranslationsCredentials`: Загружает учетные данные для PrestaShop Translations.
22. `LoadGapiCredentials`: Загружает учетные данные для Google API.
23. `CreateGlobalInstance`: Создаёт глобальный экземпляр класса `ProgramSettings` – `gs`.
24.  `End`: Конец выполнения программы.
25. **KeePass Interaction:** Подграф, содержащий все этапы взаимодействия с KeePass.

## <объяснение>

### Импорты:
*   **Стандартные библиотеки Python:**
    *   `datetime`, `datetime.datetime`: Работа с датой и временем.
    *   `getpass`: Безопасный ввод паролей.
    *   `os`: Работа с операционной системой.
    *   `sys`: Доступ к параметрам и функциям интерпретатора Python.
    *   `json`: Работа с JSON.
    *   `warnings`: Фильтрация предупреждений.
    *   `socket`: Сетевые операции, получение имени хоста.
    *   `dataclasses`, `dataclasses.dataclass`, `dataclasses.field`: Использование датаклассов.
    *   `pathlib`, `pathlib.Path`: Работа с путями файловой системы.
    *    `types`, `types.SimpleNamespace`: Создание простых объектов пространства имен.
    *   `typing`, `typing.Optional`: Использование подсказок типов.
*   **Сторонние библиотеки:**
    *   `pydantic`, `pydantic.BaseModel`, `pydantic.Field`: Валидация данных и создание настроек с помощью Pydantic.
    *   `pykeepass`, `pykeepass.PyKeePass`: Работа с базами данных KeePass.
*   **Локальные модули (из `src`)**:
    *   `src.check_release`: Проверка наличия новой версии проекта.
    *   `src.logger.logger`: Логгирование событий.
    *   `src.logger.exceptions`: Пользовательские исключения.
    *   `src.utils.file`: Чтение файлов.
    *   `src.utils.jjson`: Загрузка JSON в объекты пространства имен.
    *   `src.utils.printer`: Удобная печать.

### Классы:

*   **`ProgramSettings` (singleton):**
    *   **Роль**: Хранение глобальных настроек проекта, включая пути, учетные данные и режим работы.
    *   **Атрибуты**:
        *   `host_name` (str): Имя хоста компьютера.
        *   `base_dir` (Path): Корневая директория проекта.
        *   `config` (SimpleNamespace): Конфигурация проекта, загруженная из `config.json`.
        *   `credentials` (SimpleNamespace): Учетные данные для различных сервисов, включая API ключи и пароли.
        *   `MODE` (str): Режим работы приложения (`dev`, `test`, `prod`).
        *   `path` (SimpleNamespace): Набор путей к различным директориям проекта.
    *   **Методы**:
        *   `__init__`: Инициализирует объект, загружает настройки, устанавливает пути и загружает учетные данные.
        *   `_load_credentials`: Координирует загрузку учетных данных из KeePass.
        *   `_open_kp`: Открывает базу данных KeePass.
        *   `_load_*_credentials`:  Методы для загрузки учетных данных для каждого сервиса (Aliexpress, OpenAI, Discord, и т.д.) из KeePass.
        *   `now`: Возвращает текущую метку времени в строковом формате.
    *   **Взаимодействие**:
        *   Используется как синглтон, гарантируя один экземпляр настроек во всем проекте.
        *   Взаимодействует с файловой системой для загрузки конфигурации и учетных данных.
        *   Использует модули `src.utils.jjson` для загрузки `config.json` и `pykeepass` для работы с KeePass.

### Функции:

*   **`set_project_root(marker_files=('__root__')) -> Path`**:
    *   **Аргументы**:
        *   `marker_files` (tuple): Кортеж с именами файлов или директорий для поиска корневой директории.
    *   **Возвращаемое значение**:
        *   `Path`: Путь к корневой директории проекта.
    *   **Назначение**: Находит корневую директорию проекта, начиная с директории, где находится скрипт, и ища родительские директории, содержащие один из маркерных файлов.
    *   **Пример**: Если маркерный файл `__root__` находится в `hypotez/`, то при вызове из `hypotez/src/credentials.py` вернет `hypotez/`.
*   **`singleton(cls)`**:
    *   **Аргументы**:
        *   `cls`: Класс, для которого применяется декоратор.
    *   **Возвращаемое значение**:
        *   `get_instance`: Функция, возвращающая единственный экземпляр класса.
    *   **Назначение**:  Декоратор, который обеспечивает, что класс является синглтоном, то есть имеет только один экземпляр.
    *   **Пример**: `@singleton` над классом `ProgramSettings` гарантирует, что будет создан только один экземпляр этого класса.

### Переменные:

*   `MODE` (str): Глобальная переменная для режима работы, по умолчанию 'dev'.
*   `gs` (ProgramSettings): Глобальный экземпляр класса `ProgramSettings`, содержащий все настройки проекта.

### Потенциальные ошибки и области для улучшения:

*   **Безопасность**: Хранение пароля KeePass в открытом виде в файле `password.txt` является серьезной угрозой безопасности. Этот файл должен быть удален или его содержимое должно быть зашифровано.
*   **Обработка ошибок**: В блоках `try-except` в функциях `_load_*_credentials` и `_open_kp` логирование происходит в консоль, а не через `logger`.
*   **Конфигурация путей**:  Пути к бинарникам (`gtk_bin_dir`, `ffmpeg_bin_dir` и т.д.) прописаны в коде, что может привести к проблемам при смене их местоположения. Лучше хранить эти пути в `config.json`.
*   **Дублирование кода**: Много дублирования кода в функциях `_load_*_credentials`. Можно создать общую функцию для загрузки учетных данных.
*   **Зависимость от KeePass**: Приложение сильно зависит от KeePass. Можно добавить альтернативный способ загрузки учетных данных.
*   **Жестко заданные пути**: Пути по умолчанию для `log`, `tmp`, `data`, `google_drive`, `external_storage` жестко заданы. Лучше иметь возможность их переопределить через конфигурацию.

### Взаимосвязи с другими частями проекта:

*   `src.check_release` используется для проверки обновлений.
*   `src.logger` используется для ведения логов.
*   `src.utils.jjson` используется для загрузки `config.json`.
*   `src.utils.file` используется для чтения файлов (например `password.txt`).
*   `src.utils.printer` используется для печати.
*   Данный модуль является центральным для проекта, так как предоставляет общую конфигурацию и доступ к учетным данным для других модулей.

В целом, код выполняет важную функцию загрузки и управления настройками проекта, однако требует улучшения в плане безопасности, обработки ошибок и гибкости.
```
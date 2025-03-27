## ИНСТРУКЦИЯ:

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:  

1. **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.  
2. **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости, 
    которые импортируются при создании диаграммы. 
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`, 
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!  
    
    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:\
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
### **<алгоритм>**

1.  **Инициализация CrawleePython**:

    *   Пример: `crawler = CrawleePython(max_requests=5, headless=False, browser_type='firefox', options=["--headless"])`
    *   Создается экземпляр класса `CrawleePython` с заданными параметрами, такими как максимальное количество запросов (`max_requests`), режим без графического интерфейса (`headless`), тип браузера (`browser_type`) и дополнительные опции (`options`).

2.  **Настройка Crawler**:

    *   Функция: `setup_crawler`
    *   Создается экземпляр `PlaywrightCrawler` с заданными параметрами и регистрируется обработчик запросов `request_handler`.

3.  **Обработка запросов**:

    *   Функция: `request_handler`
    *   Пример: `await context.enqueue_links()`
    *   Обработчик `request_handler` выполняет следующие действия: логирует обрабатываемый URL, добавляет в очередь найденные на странице ссылки, извлекает данные (URL, заголовок, содержимое) и сохраняет их.

4.  **Запуск Crawler**:

    *   Функция: `run_crawler`
    *   Пример: `await self.crawler.run(urls)`
    *   Запускается процесс обхода страниц по списку URL, используя настроенный экземпляр `PlaywrightCrawler`.

5.  **Экспорт данных**:

    *   Функция: `export_data`
    *   Пример: `await self.crawler.export_data(file_path)`
    *   Извлеченные данные сохраняются в JSON-файл по указанному пути.

6.  **Получение данных**:

    *   Функция: `get_data`
    *   Пример: `data = await self.crawler.get_data()`
    *   Извлекаются накопленные данные из `crawler`.

7.  **Запуск и обработка исключений**:

    *   Функция: `run`
    *   Вызываются функции для настройки, запуска обхода страниц и экспорта данных. В случае возникновения исключений, они логируются.

```mermaid
flowchart TD
    subgraph CrawleePython
        A[Инициализация CrawleePython: <br>max_requests, headless, browser_type, options] --> B(setup_crawler)
        B --> C{PlaywrightCrawler: <br>max_requests_per_crawl, headless, browser_type, launch_options}
        C --> D(request_handler)
        D --> E{enqueue_links()}
        E --> F{Extract Data: <br>url, title, content}
        F --> G{push_data()}
        G --> H(run_crawler: <br>urls)
        H --> I{crawler.run(urls)}
        I --> J(export_data: <br>file_path)
        J --> K{crawler.export_data(file_path)}
        K --> L(get_data)
        L --> M{crawler.get_data()}
        M --> N(logger.info: <br>Extracted data)
        N --> O(Error Handling: <br>logger.critical)
    end

    style CrawleePython fill:#f9f,stroke:#333,stroke-width:2px
```

### **<mermaid>**

```mermaid
flowchart TD
    subgraph CrawleePython
        A[Инициализация CrawleePython: <br>max_requests, headless, browser_type, options] --> B(setup_crawler)
        B --> C{PlaywrightCrawler: <br>max_requests_per_crawl, headless, browser_type, launch_options}
        C --> D(request_handler)
        D --> E{enqueue_links()}
        E --> F{Extract Data: <br>url, title, content}
        F --> G{push_data()}
        G --> H(run_crawler: <br>urls)
        H --> I{crawler.run(urls)}
        I --> J(export_data: <br>file_path)
        J --> K{crawler.export_data(file_path)}
        K --> L(get_data)
        L --> M{crawler.get_data()}
        M --> N(logger.info: <br>Extracted data)
        N --> O(Error Handling: <br>logger.critical)
    end

    style CrawleePython fill:#f9f,stroke:#333,stroke-width:2px
```

**Зависимости, импортированные для создания диаграммы:**

*   **`pathlib.Path`**: Используется для работы с путями к файлам и директориям.
*   **`typing.Optional, typing.List, typing.Dict, typing.Any`**: Используются для аннотации типов переменных и функций.
*   **`src.gs`**: Импортирует глобальные настройки проекта.
*   **`asyncio`**: Используется для асинхронного программирования.
*   **`crawlee.playwright_crawler.PlaywrightCrawler, crawlee.playwright_crawler.PlaywrightCrawlingContext`**: Импортируются классы для работы с PlaywrightCrawler и контекстом обхода страниц.
*   **`src.logger.logger.logger`**: Используется для логирования событий.
*   **`src.utils.jjson.j_loads_ns`**: Используется для загрузки JSON-данных с поддержкой namespace.

### **<объяснение>**

**Импорты:**

*   `pathlib.Path`: Используется для работы с путями к файлам и директориям в файловой системе.
*   `typing.Optional, List, Dict, Any`: Используются для указания типов переменных, аргументов функций и возвращаемых значений. `Optional` указывает, что переменная может иметь значение `None`. `List`, `Dict`, `Any` — это типы коллекций.
*   `src.gs`: Импортирует глобальные настройки из модуля `gs`, который, вероятно, содержит общие параметры конфигурации проекта.
*   `asyncio`: Используется для поддержки асинхронных операций, что позволяет не блокировать выполнение программы во время ожидания завершения операций ввода-вывода.
*   `crawlee.playwright_crawler.PlaywrightCrawler, PlaywrightCrawlingContext`: Импортирует классы `PlaywrightCrawler` и `PlaywrightCrawlingContext` из библиотеки Crawlee, которые используются для создания и управления веб-сканером на основе Playwright.
*   `src.logger.logger.logger`: Импортирует объект `logger` для логирования событий, что позволяет отслеживать и диагностировать работу программы.
*   `src.utils.jjson.j_loads_ns`: Импортирует функцию `j_loads_ns` для загрузки JSON-данных, возможно, с поддержкой пространств имен (namespaces).

**Классы:**

*   `CrawleePython`:
    *   **Роль**: Представляет собой обертку над `PlaywrightCrawler` из библиотеки Crawlee, предоставляя удобный интерфейс для настройки и запуска веб-сканера.
    *   **Атрибуты**:
        *   `max_requests (int)`: Максимальное количество запросов, которые выполнит сканер.
        *   `headless (bool)`: Определяет, будет ли браузер работать в режиме без графического интерфейса (headless).
        *   `browser_type (str)`: Указывает тип используемого браузера (`chromium`, `firefox`, `webkit`).
        *   `options (Optional[List[str]])`: Список дополнительных аргументов командной строки для запуска браузера.
        *   `crawler (PlaywrightCrawler)`: Экземпляр класса `PlaywrightCrawler`, который выполняет обход веб-страниц.
    *   **Методы**:
        *   `__init__(self, max_requests: int = 5, headless: bool = False, browser_type: str = 'firefox', options: Optional[List[str]] = None)`: Конструктор класса, инициализирует атрибуты экземпляра.
        *   `async setup_crawler(self)`: Создает и настраивает экземпляр `PlaywrightCrawler` с заданными параметрами. Также определяет обработчик запросов `request_handler`, который будет выполняться для каждой посещенной страницы.
        *   `async request_handler(self, context: PlaywrightCrawlingContext)`: Асинхронный обработчик запросов, который вызывается для каждой страницы. Он извлекает данные (URL, заголовок, содержимое), добавляет в очередь найденные ссылки и сохраняет извлеченные данные.
        *   `async run_crawler(self, urls: List[str])`: Запускает сканер с заданным списком начальных URL.
        *   `async export_data(self, file_path: str)`: Экспортирует собранные данные в JSON-файл.
        *   `async get_data(self) -> Dict[str, Any]`: Получает собранные данные в виде словаря.
        *   `async run(self, urls: List[str])`: Основной метод, который выполняет настройку сканера, запуск обхода страниц, экспорт данных и логирование результатов.

**Функции:**

*   `__init__(self, max_requests: int = 5, headless: bool = False, browser_type: str = 'firefox', options: Optional[List[str]] = None)`
    *   **Аргументы**:
        *   `max_requests (int)`: Максимальное количество запросов для выполнения. По умолчанию 5.
        *   `headless (bool)`: Флаг, определяющий, запускать ли браузер в headless-режиме (без GUI). По умолчанию `False`.
        *   `browser_type (str)`: Тип используемого браузера (`'chromium'`, `'firefox'`, `'webkit'`). По умолчанию `'firefox'`.
        *   `options (Optional[List[str]])`: Список дополнительных опций, передаваемых в браузер. По умолчанию `None`.
    *   **Возвращаемое значение**: `None`
    *   **Назначение**: Инициализирует экземпляр класса `CrawleePython`, устанавливая значения его атрибутов.

*   `async setup_crawler(self)`
    *   **Аргументы**: `self`
    *   **Возвращаемое значение**: `None`
    *   **Назначение**: Настраивает и инициализирует `PlaywrightCrawler` с заданными параметрами, такими как максимальное количество запросов, headless-режим и тип браузера. Также определяет обработчик запросов `request_handler`, который будет выполняться для каждой посещенной страницы.

*   `async request_handler(context: PlaywrightCrawlingContext) -> None`
    *   **Аргументы**:
        *   `context (PlaywrightCrawlingContext)`: Контекст обхода страниц, предоставляющий доступ к информации о текущем запросе и странице.
    *   **Возвращаемое значение**: `None`
    *   **Назначение**: Обработчик запросов, который вызывается для каждой посещенной страницы. Он извлекает данные (URL, заголовок, содержимое), добавляет в очередь найденные ссылки и сохраняет извлеченные данные.

*   `async run_crawler(self, urls: List[str])`
    *   **Аргументы**:
        *   `urls (List[str])`: Список URL, с которых начинается обход страниц.
    *   **Возвращаемое значение**: `None`
    *   **Назначение**: Запускает обход страниц с использованием `PlaywrightCrawler`, начиная с заданных URL.

*   `async export_data(self, file_path: str)`
    *   **Аргументы**:
        *   `file_path (str)`: Путь к файлу, в который будут экспортированы собранные данные в формате JSON.
    *   **Возвращаемое значение**: `None`
    *   **Назначение**: Экспортирует собранные данные в JSON-файл.

*   `async get_data(self) -> Dict[str, Any]`
    *   **Аргументы**: `self`
    *   **Возвращаемое значение**: `Dict[str, Any]` - словарь, содержащий собранные данные.
    *   **Назначение**: Получает собранные данные из `PlaywrightCrawler`.

*   `async run(self, urls: List[str])`
    *   **Аргументы**:
        *   `urls (List[str])`: Список URL, с которых начинается обход страниц.
    *   **Возвращаемое значение**: `None`
    *   **Назначение**: Основной метод, который выполняет настройку сканера, запуск обхода страниц, экспорт данных и логирование результатов.

**Переменные:**

*   `max_requests (int)`: Максимальное количество запросов для выполнения.
*   `headless (bool)`: Флаг, определяющий, запускать ли браузер в headless-режиме (без GUI).
*   `browser_type (str)`: Тип используемого браузера (`'chromium'`, `'firefox'`, `'webkit'`).
*   `options (Optional[List[str]])`: Список дополнительных опций, передаваемых в браузер.
*   `crawler (PlaywrightCrawler)`: Экземпляр класса `PlaywrightCrawler`, который выполняет обход веб-страниц.
*   `context (PlaywrightCrawlingContext)`: Контекст обхода страниц, предоставляющий доступ к информации о текущем запросе и странице.
*   `data (Dict[str, Any])`: Словарь, содержащий извлеченные данные (URL, заголовок, содержимое).
*   `file_path (str)`: Путь к файлу, в который будут экспортированы собранные данные.
*   `urls (List[str])`: Список URL, с которых начинается обход страниц.

**Потенциальные ошибки и области для улучшения:**

*   Обработка исключений в `request_handler`: В текущей реализации `request_handler` не предусмотрена обработка исключений, которые могут возникнуть при извлечении данных или добавлении ссылок в очередь.
*   Более гибкая настройка извлечения данных: В текущей реализации данные извлекаются жестко заданным способом (URL, заголовок, содержимое). Было бы полезно предоставить возможность настраивать, какие данные извлекать и как их обрабатывать.
*   Использование `j_loads` или `j_loads_ns`: В текущем коде нет использования `j_loads` или `j_loads_ns`. Рассмотрите возможность использования этих функций для загрузки конфигурационных файлов.

**Взаимосвязи с другими частями проекта:**

*   `src.gs`: Используется для получения глобальных настроек проекта, таких как пути к файлам и директориям.
*   `src.logger.logger.logger`: Используется для логирования событий, что позволяет отслеживать и диагностировать работу программы.
*   `src.utils.jjson.j_loads_ns`: Может использоваться для загрузки конфигурационных файлов в формате JSON с поддержкой пространств имен.

```mermaid
flowchart TD
    Start --> CrawleePythonInit[CrawleePython Initialization]
    CrawleePythonInit --> SetupCrawler
    SetupCrawler --> PlaywrightCrawlerSetup[PlaywrightCrawler Setup]
    PlaywrightCrawlerSetup --> RequestHandlerDef[Define Request Handler]
    RequestHandlerDef --> RunCrawler
    RunCrawler --> CrawlExecution[Crawler Execution]
    CrawlExecution --> ExportData
    ExportData --> SaveDataToFile[Save Data to File]
    SaveDataToFile --> GetData
    GetData --> RetrieveData[Retrieve Data]
    RetrieveData --> LoggerInfo[Log Extracted Data]
    LoggerInfo --> End
    Start --> ExceptionHandler[Exception Handling]
    ExceptionHandler --> LoggerCritical[Log Critical Error]
    LoggerCritical --> End
    style CrawleePythonInit fill:#ccf,stroke:#333,stroke-width:2px
## <алгоритм>

1.  **Инициализация CrawleePython:**
    *   Создается экземпляр класса `CrawleePython` с заданными параметрами: `max_requests` (максимальное количество запросов), `headless` (режим без графического интерфейса), `browser_type` (тип браузера), и `options` (опции запуска браузера).
    *   Пример: `crawler = CrawleePython(max_requests=5, headless=False, browser_type='firefox', options=["--headless"])`
    *   Инициализируются атрибуты объекта, такие как `self.max_requests`, `self.headless`, `self.browser_type`, `self.options` и `self.crawler`.

2.  **Настройка Crawler:**
    *   Вызывается метод `setup_crawler`, который создает экземпляр `PlaywrightCrawler` с заданными настройками.
    *   Устанавливается обработчик запросов `request_handler` с помощью декоратора `@self.crawler.router.default_handler`.
    *   Пример: `self.crawler = PlaywrightCrawler(...)`

3.  **Обработка запроса (request_handler):**
    *   Для каждого запроса выполняется функция `request_handler`.
    *   Логируется информация об обрабатываемом URL.
    *   Извлекаются и добавляются в очередь все найденные на странице ссылки с помощью `await context.enqueue_links()`.
    *   Извлекаются данные (URL, заголовок страницы, первые 100 символов содержимого страницы) с помощью `context.page.title()` и `context.page.content()`.
    *   Извлеченные данные сохраняются в `data`.
    *   Данные отправляются в набор данных с помощью `await context.push_data(data)`.
    *   Пример: 
        ```
        context.log.info(f'Processing {context.request.url} ...')
        await context.enqueue_links()
        data = {'url': context.request.url, 'title': await context.page.title(), 'content': (await context.page.content())[:100]}
        await context.push_data(data)
        ```

4.  **Запуск Crawler:**
    *   Вызывается метод `run_crawler` с начальным списком URL.
    *   Пример: `await crawler.run_crawler(['https://www.example.com'])`
    *   Crawler запускается и начинает обрабатывать URL.

5.  **Экспорт Данных:**
    *   После завершения работы crawler, вызывается метод `export_data`, который сохраняет собранные данные в JSON-файл по указанному пути.
    *   Пример: `await crawler.export_data(str(Path(gs.path.tmp / 'results.json')))`

6.  **Получение Данных:**
    *   Метод `get_data` извлекает все собранные данные.
    *   Пример: `data = await crawler.get_data()`

7.  **Запуск всего процесса (run):**
    *   Метод `run` последовательно вызывает методы `setup_crawler`, `run_crawler`, `export_data`, и `get_data`.
    *   Логируется информация о собранных данных.
    *   Обрабатываются исключения.
    *   Пример: `await crawler.run(['https://www.example.com'])`
    *   В случае ошибки, она логируется.

8. **Пример использования:**
    *   В блоке `if __name__ == '__main__':` создается асинхронная функция `main()`.
    *   Внутри `main()` создается экземпляр `CrawleePython` и запускается обход с помощью `await crawler.run()`.
    *   Функция `main()` запускается с помощью `asyncio.run(main())`.

## <mermaid>

```mermaid
flowchart TD
    Start(Start) --> Init[Initialize <code>CrawleePython</code> <br> max_requests, headless, browser_type, options];
    Init --> SetupCrawler[<code>setup_crawler()</code><br> Create PlaywrightCrawler <br> Set default handler];
    SetupCrawler --> RequestHandler[<code>request_handler(context)</code><br> Log URL, Enqueue links, Extract data, Push data];
    RequestHandler --> RunCrawler[<code>run_crawler(urls)</code><br> Start crawler with list of urls];
    RunCrawler --> ExportData[<code>export_data(file_path)</code><br> Save data to JSON file];
    ExportData --> GetData[<code>get_data()</code> <br> Retrieves extracted data];
    GetData --> LogData[Log Extracted Data];
    LogData --> End(End);
    
    style Start fill:#f9f,stroke:#333,stroke-width:2px
    style End fill:#ccf,stroke:#333,stroke-width:2px
    
    classDef customFill fill:#e0f7fa,stroke:#333,stroke-width:1px;
    class Init,SetupCrawler,RequestHandler,RunCrawler,ExportData,GetData customFill;

    
```
### <mermaid> explanation:

1.  `Start(Start)`: Начало процесса.
2.  `Init[Initialize CrawleePython ...]`: Инициализация экземпляра класса `CrawleePython` с параметрами максимального количества запросов (`max_requests`), режима без графического интерфейса (`headless`), типа браузера (`browser_type`) и опций запуска браузера (`options`).
3.  `SetupCrawler[setup_crawler()...]`: Вызов метода `setup_crawler`, в котором создается экземпляр `PlaywrightCrawler` и устанавливается обработчик запросов по умолчанию (`default_handler`).
4.  `RequestHandler[request_handler(context)...]`: Обработчик запросов `request_handler`, который выполняет следующие действия: логирование URL, добавление ссылок в очередь, извлечение данных и сохранение данных.
5.  `RunCrawler[run_crawler(urls)...]`: Запуск обхода с помощью метода `run_crawler` с начальным списком URL.
6.  `ExportData[export_data(file_path)...]`: Экспорт собранных данных в JSON-файл с помощью метода `export_data`.
7.  `GetData[get_data()...]`: Извлечение всех собранных данных с помощью метода `get_data`.
8. `LogData[Log Extracted Data]`: Логирование извлеченных данных.
9.  `End(End)`: Конец процесса.

**Описание импортированных зависимостей:**

*   **`pathlib`**:
    *   `Path` используется для работы с путями к файлам и директориям, в основном для временного файла `results.json`, в который будет выгружаться результат.
    *   Импортируется: `from pathlib import Path`

*   **`typing`**:
    *   `Optional`, `List`, `Dict`, `Any` используются для статической типизации, делая код более понятным и предотвращая ошибки.
    *   `Optional` используется для обозначения, что параметр может быть `None`.
    *   `List` используется для обозначения, что параметр является списком.
    *   `Dict` используется для обозначения, что параметр является словарем.
    *   `Any` используется для обозначения, что параметр может быть любого типа.
    *   Импортируется: `from typing import Optional, List, Dict, Any`

*   **`src`**:
    *   `gs` импортируется из пакета `src` и, предположительно, содержит глобальные настройки проекта (например, путь к временной директории).
    *   Импортируется: `from src import gs`

*   **`asyncio`**:
    *   Используется для асинхронного выполнения кода, позволяет запускать и управлять асинхронными операциями (например, `asyncio.run(main())`).
    *   Импортируется: `import asyncio`

*   **`crawlee.playwright_crawler`**:
    *   `PlaywrightCrawler` и `PlaywrightCrawlingContext` импортируются из библиотеки `crawlee` для создания и управления веб-сканером, использующим Playwright.
    *   Импортируется: `from crawlee.playwright_crawler import PlaywrightCrawler, PlaywrightCrawlingContext`

*   **`src.logger.logger`**:
    *   `logger` импортируется из пакета `src.logger` для логирования событий и сообщений в процессе работы программы.
    *   Импортируется: `from src.logger.logger import logger`

*  **`src.utils.jjson`**:
    *   `j_loads_ns` импортируется из пакета `src.utils` и используется для загрузки JSON данных.
    *   Импортируется: `from src.utils.jjson import j_loads_ns`

## <объяснение>

### Импорты:

*   **`pathlib.Path`**: Используется для работы с путями к файлам и каталогам. В данном коде используется для формирования пути к файлу `results.json`, в который будут сохранены результаты сканирования.
*   **`typing.Optional, typing.List, typing.Dict, typing.Any`**: Используются для статической типизации, что делает код более читаемым и помогает отлавливать ошибки на этапе разработки.
    *   `Optional` означает, что переменная может быть `None`.
    *   `List` используется для обозначения списка.
    *   `Dict` используется для обозначения словаря.
    *   `Any` используется для обозначения переменной любого типа.
*   **`src.gs`**: `gs` (предположительно, Global Settings) является модулем, содержащим глобальные настройки проекта. Используется для получения пути к временной директории `tmp`, где сохраняется результат.
*   **`asyncio`**: Библиотека для написания асинхронного кода. Позволяет выполнять несколько операций параллельно, не блокируя основной поток программы.
*   **`crawlee.playwright_crawler.PlaywrightCrawler, crawlee.playwright_crawler.PlaywrightCrawlingContext`**:
    *   `PlaywrightCrawler` является основным классом для создания веб-сканеров с использованием Playwright.
    *   `PlaywrightCrawlingContext` предоставляет контекст для обработки каждого запроса.
*   **`src.logger.logger.logger`**: Модуль для логирования событий, позволяющий отслеживать работу программы, записывать ошибки и отладочную информацию.
*   **`src.utils.jjson.j_loads_ns`**: Модуль для загрузки JSON данных. В данном примере не используется, но импортирован.

### Классы:

*   **`CrawleePython`**:
    *   **Роль**: Класс, представляющий собой кастомную реализацию веб-сканера на основе `PlaywrightCrawler`.
    *   **Атрибуты**:
        *   `max_requests`: Максимальное количество запросов, которые выполнит сканер.
        *   `headless`: Флаг для запуска браузера в безголовом режиме (без графического интерфейса).
        *   `browser_type`: Тип браузера (chromium, firefox, webkit).
        *   `options`: Список дополнительных опций для запуска браузера.
        *   `crawler`: Экземпляр класса `PlaywrightCrawler`, используемый для выполнения сканирования.
    *   **Методы**:
        *   `__init__(self, max_requests, headless, browser_type, options)`: Конструктор класса, инициализирует атрибуты объекта.
        *   `setup_crawler(self)`: Создает экземпляр `PlaywrightCrawler`, настраивает обработчик запросов `request_handler`.
        *   `request_handler(context)`: Обработчик запросов. Получает контекст запроса, логирует URL, добавляет найденные ссылки в очередь, извлекает заголовок и первые 100 символов контента страницы, сохраняет полученные данные.
        *   `run_crawler(self, urls)`: Запускает сканирование с указанными URL.
        *   `export_data(self, file_path)`: Экспортирует данные в JSON-файл.
        *   `get_data(self)`: Возвращает извлеченные данные.
        *   `run(self, urls)`: Главный метод, который последовательно вызывает `setup_crawler`, `run_crawler`, `export_data`, `get_data` и логирует данные.

### Функции:

*   **`__init__(self, max_requests: int = 5, headless: bool = False, browser_type: str = 'firefox', options: Optional[List[str]] = None)`**
    *   **Аргументы**:
        *   `max_requests` (int, по умолчанию 5): Максимальное количество запросов.
        *   `headless` (bool, по умолчанию `False`): Запускать браузер в безголовом режиме.
        *   `browser_type` (str, по умолчанию 'firefox'): Тип браузера.
        *    `options` (Optional[List[str]], по умолчанию `None`): Список опций для запуска браузера.
    *   **Возвращает**: None.
    *   **Назначение**: Инициализирует объект класса `CrawleePython` с заданными параметрами.

*   **`setup_crawler(self)`**
    *   **Аргументы**: None.
    *   **Возвращает**: None.
    *   **Назначение**: Создает и настраивает экземпляр `PlaywrightCrawler` с заданными параметрами, а также устанавливает обработчик запросов `request_handler`.

*   **`request_handler(context: PlaywrightCrawlingContext)`**
    *   **Аргументы**:
        *   `context` (`PlaywrightCrawlingContext`): Контекст запроса.
    *   **Возвращает**: None.
    *   **Назначение**: Обрабатывает каждый запрос, логирует информацию об URL, добавляет ссылки в очередь, извлекает данные и сохраняет их в наборе данных.

*   **`run_crawler(self, urls: List[str])`**
    *   **Аргументы**:
        *   `urls` (`List[str]`): Список URL для запуска сканирования.
    *   **Возвращает**: None.
    *   **Назначение**: Запускает сканирование с указанными URL.

*   **`export_data(self, file_path: str)`**
    *   **Аргументы**:
        *   `file_path` (`str`): Путь к файлу, в который необходимо сохранить результаты сканирования.
    *   **Возвращает**: None.
    *   **Назначение**: Экспортирует собранные данные в JSON-файл.

*   **`get_data(self)`**
    *   **Аргументы**: None.
    *   **Возвращает**: `Dict[str, Any]`: Извлеченные данные в виде словаря.
    *   **Назначение**: Возвращает извлеченные данные после сканирования.

*   **`run(self, urls: List[str])`**
    *   **Аргументы**:
        *   `urls` (`List[str]`): Список URL для запуска сканирования.
    *   **Возвращает**: None.
    *   **Назначение**: Выполняет весь процесс сканирования: настройка, запуск, экспорт данных, получение данных и логирование результатов, а также обработку исключений.

*   **`main()`**
    *   **Аргументы**: None.
    *   **Возвращает**: None.
    *   **Назначение**: Создает экземпляр класса `CrawleePython` и запускает процесс сканирования с примером URL.

### Переменные:

*   `max_requests`: Целое число, определяющее максимальное количество запросов, которые выполнит сканер.
*   `headless`: Булево значение, определяющее, запускать ли браузер в безголовом режиме.
*   `browser_type`: Строка, определяющая тип браузера, который будет использоваться (chromium, firefox, webkit).
*  `options`: Список строк, который содержит опции запуска браузера.
*   `crawler`: Экземпляр класса `PlaywrightCrawler`, который используется для управления процессом сканирования.
*   `urls`: Список строк, представляющих URL-адреса для сканирования.
*   `file_path`: Строка, представляющая путь к файлу, куда будут сохранены результаты.
*   `data`: Словарь, содержащий извлеченные данные.
*   `context`: Объект `PlaywrightCrawlingContext`, содержащий информацию о текущем контексте сканирования.

### Потенциальные ошибки или области для улучшения:

1.  **Обработка исключений**:
    *   В блоке `try-except` метода `run` логируется общая ошибка, но нет более детальной обработки конкретных типов исключений.
    *   **Улучшение**: Добавить обработку конкретных типов исключений (например, `NetworkError`, `PlaywrightError`), чтобы логировать и обрабатывать их по-разному.

2.  **Ограничение извлекаемого содержимого**:
    *   Извлекается только первые 100 символов содержимого страницы.
    *   **Улучшение**:  Изменить логику извлечения содержимого, чтобы можно было извлекать более значимые части страницы (например, контент статьи).

3.  **Отсутствие гибкости в обработке данных**:
    *   Данные жестко структурированы в виде словаря с ключами `'url'`, `'title'`, `'content'`.
    *   **Улучшение**: Добавить возможность настраивать структуру извлекаемых данных и формат их сохранения (например, через аргументы конструктора `CrawleePython`).

4.  **Конфигурация браузера**:
    *  Задаются только базовые опции запуска браузера.
    *  **Улучшение**: Расширить возможности настройки браузера через параметры (например, размер окна, user agent, прокси).

5.  **`j_loads_ns`**: Импортируется, но не используется в коде.
    *   **Улучшение**: Убрать импорт если не планируется использование в будущем.

### Взаимосвязи с другими частями проекта:

*   **`src.gs`**: Используется для получения глобальных настроек, в частности, пути к временной директории для сохранения результатов.
*   **`src.logger.logger`**: Используется для логирования событий и ошибок.
*   **`crawlee`**: Используется как основа для создания веб-сканера.

Таким образом, код представляет собой кастомную реализацию веб-сканера на основе `crawlee` и `playwright`, который может быть использован для сбора данных с веб-страниц.
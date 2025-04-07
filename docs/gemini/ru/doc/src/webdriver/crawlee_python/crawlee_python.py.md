# Модуль `src.webdriver.crawlee_python`

## Обзор

Модуль `src.webdriver.crawlee_python` предоставляет пользовательскую реализацию `PlaywrightCrawler` с использованием библиотеки Crawlee. Он позволяет настраивать параметры браузера, обрабатывать запросы и извлекать данные с веб-страниц.

## Подробней

Этот модуль предназначен для упрощения процесса веб-скрапинга с использованием библиотеки Crawlee и Playwright. Он предоставляет класс `CrawleePython`, который можно настроить для выполнения запросов к веб-страницам, извлечения данных и сохранения результатов.

## Классы

### `CrawleePython`

**Описание**:
Класс `CrawleePython` представляет собой пользовательскую реализацию `PlaywrightCrawler` для веб-скрапинга.

**Принцип работы**:
Класс инициализируется с параметрами, определяющими максимальное количество запросов, режим работы браузера (с графическим интерфейсом или без), тип браузера и дополнительные опции. Он настраивает экземпляр `PlaywrightCrawler` с указанными параметрами и предоставляет методы для запуска сканера, экспорта данных и получения извлеченных данных.

**Аттрибуты**:
- `max_requests` (int): Максимальное количество запросов для выполнения во время обхода.
- `headless` (bool): Определяет, следует ли запускать браузер в безголовом режиме.
- `browser_type` (str): Тип используемого браузера ('chromium', 'firefox', 'webkit').
- `crawler` (PlaywrightCrawler): Экземпляр PlaywrightCrawler.
- `options` (Optional[List[str]]): Список дополнительных параметров командной строки для запуска браузера.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `CrawleePython` с заданными параметрами.
- `setup_crawler`: Настраивает экземпляр `PlaywrightCrawler` с заданной конфигурацией.
- `run_crawler`: Запускает обход веб-страниц с использованием предоставленного списка URL-адресов.
- `export_data`: Экспортирует весь набор данных в JSON-файл.
- `get_data`: Извлекает извлеченные данные.
- `run`: Основной метод для настройки, запуска сканера и экспорта данных.

### `__init__`

```python
def __init__(self, max_requests: int = 5, headless: bool = False, browser_type: str = 'firefox', options: Optional[List[str]] = None):
    """
    Initializes the CrawleePython crawler with the specified parameters.

    :param max_requests: Maximum number of requests to perform during the crawl.
    :type max_requests: int
    :param headless: Whether to run the browser in headless mode.
    :type headless: bool
    :param browser_type: The type of browser to use ('chromium', 'firefox', 'webkit').
    :type browser_type: str
    :param options: A list of custom options to pass to the browser.
    :type options: Optional[List[str]]
    """
    ...
```

**Назначение**:
Инициализирует экземпляр класса `CrawleePython` с заданными параметрами.

**Параметры**:
- `max_requests` (int): Максимальное количество запросов для выполнения во время обхода. По умолчанию равно 5.
- `headless` (bool): Определяет, следует ли запускать браузер в безголовом режиме. По умолчанию `False`.
- `browser_type` (str): Тип используемого браузера ('chromium', 'firefox', 'webkit'). По умолчанию 'firefox'.
- `options` (Optional[List[str]]): Список дополнительных параметров командной строки для запуска браузера. По умолчанию `None`.

**Как работает функция**:

1. Функция инициализирует атрибуты экземпляра класса `CrawleePython` значениями, переданными в качестве аргументов.
2. Если `options` не переданы, то инициализируется пустым списком `[]`.
3. `self.crawler` инициализируется значением `None`.

**Примеры**:

```python
crawler = CrawleePython(max_requests=10, headless=True, browser_type='chromium', options=['--disable-gpu', '--no-sandbox'])
```

### `setup_crawler`

```python
async def setup_crawler(self):
    """
    Sets up the PlaywrightCrawler instance with the specified configuration.
    """
    ...
```

**Назначение**:
Настраивает экземпляр `PlaywrightCrawler` с заданной конфигурацией.

**Как работает функция**:

1.  Создает экземпляр `PlaywrightCrawler` с заданными параметрами, такими как `max_requests_per_crawl`, `headless` и `browser_type`.
2.  Устанавливает обработчик запросов по умолчанию, который извлекает информацию со страниц и добавляет ссылки на другие страницы в очередь.

**ASCII flowchart**:

```
[Настройка PlaywrightCrawler]
    |
    | Создание экземпляра PlaywrightCrawler с параметрами
    |
    | Установка обработчика запросов по умолчанию
    |
[Конец]
```

**Примеры**:

```python
await crawler.setup_crawler()
```

### `request_handler`

```python
async def request_handler(context: PlaywrightCrawlingContext) -> None:
    """
    Default request handler for processing web pages.

    :param context: The crawling context.
    :type context: PlaywrightCrawlingContext
    """
    ...
```

**Назначение**:
Обработчик запросов по умолчанию для обработки веб-страниц.

**Параметры**:
- `context` (PlaywrightCrawlingContext): Контекст обхода.

**Как работает функция**:

1.  Логирует информацию об обрабатываемом URL.
2.  Добавляет в очередь все ссылки, найденные на странице.
3.  Извлекает данные со страницы, такие как URL, заголовок и содержимое.
4.  Отправляет извлеченные данные в набор данных по умолчанию.

**ASCII flowchart**:

```
[Обработка веб-страницы]
    |
    | Логирование URL
    |
    | Добавление ссылок в очередь
    |
    | Извлечение данных (URL, заголовок, содержимое)
    |
    | Отправка данных в набор данных
    |
[Конец]
```

**Примеры**:

```python
# Эта функция вызывается автоматически PlaywrightCrawler для каждой страницы.
```

### `run_crawler`

```python
async def run_crawler(self, urls: List[str]):
    """
    Runs the crawler with the initial list of URLs.

    :param urls: List of URLs to start the crawl.
    :type urls: List[str]
    """
    ...
```

**Назначение**:
Запускает обход веб-страниц с использованием предоставленного списка URL-адресов.

**Параметры**:
- `urls` (List[str]): Список URL-адресов для начала обхода.

**Как работает функция**:

1.  Вызывает метод `run` экземпляра `PlaywrightCrawler` с предоставленным списком URL-адресов.

**ASCII flowchart**:

```
[Запуск обхода]
    |
    | Вызов crawler.run(urls)
    |
[Конец]
```

**Примеры**:

```python
await crawler.run_crawler(['https://www.example.com', 'https://www.example.org'])
```

### `export_data`

```python
async def export_data(self, file_path: str):
    """
    Exports the entire dataset to a JSON file.

    :param file_path: Path to save the exported JSON file.
    :type file_path: str
    """
    ...
```

**Назначение**:
Экспортирует весь набор данных в JSON-файл.

**Параметры**:
- `file_path` (str): Путь для сохранения экспортированного JSON-файла.

**Как работает функция**:

1.  Вызывает метод `export_data` экземпляра `PlaywrightCrawler` с предоставленным путем к файлу.

**ASCII flowchart**:

```
[Экспорт данных]
    |
    | Вызов crawler.export_data(file_path)
    |
[Конец]
```

**Примеры**:

```python
await crawler.export_data('results.json')
```

### `get_data`

```python
async def get_data(self) -> Dict[str, Any]:
    """
    Retrieves the extracted data.

    :return: Extracted data as a dictionary.
    :rtype: Dict[str, Any]
    """
    ...
```

**Назначение**:
Извлекает извлеченные данные.

**Возвращает**:
- `Dict[str, Any]`: Извлеченные данные в виде словаря.

**Как работает функция**:

1.  Вызывает метод `get_data` экземпляра `PlaywrightCrawler`.
2.  Возвращает извлеченные данные.

**ASCII flowchart**:

```
[Извлечение данных]
    |
    | Вызов crawler.get_data()
    |
    | Возврат данных
    |
[Конец]
```

**Примеры**:

```python
data = await crawler.get_data()
print(data)
```

### `run`

```python
async def run(self, urls: List[str]):
    """
    Main method to set up, run the crawler, and export data.

    :param urls: List of URLs to start the crawl.
    :type urls: List[str]
    """
    ...
```

**Назначение**:
Основной метод для настройки, запуска сканера и экспорта данных.

**Параметры**:
- `urls` (List[str]): Список URL-адресов для начала обхода.

**Как работает функция**:

1.  Настраивает сканер, вызывая метод `setup_crawler`.
2.  Запускает обход веб-страниц, вызывая метод `run_crawler`.
3.  Экспортирует данные в JSON-файл, вызывая метод `export_data`.
4.  Извлекает данные, вызывая метод `get_data`.
5.  Логирует извлеченные данные.

**ASCII flowchart**:

```
[Запуск сканера]
    |
    | Настройка сканера (setup_crawler)
    |
    | Запуск обхода (run_crawler)
    |
    | Экспорт данных (export_data)
    |
    | Извлечение данных (get_data)
    |
    | Логирование данных
    |
[Конец]
```

**Примеры**:

```python
await crawler.run(['https://www.example.com', 'https://www.example.org'])
```

## Функции

### `main`

```python
async def main():
    crawler = CrawleePython(max_requests=5, headless=False, browser_type='firefox', options=["--headless"])
    await crawler.run(['https://www.example.com'])
```

**Назначение**:
Пример использования класса `CrawleePython`.

**Как работает функция**:

1.  Создает экземпляр класса `CrawleePython` с заданными параметрами.
2.  Запускает обход веб-страниц, вызывая метод `run`.

**ASCII flowchart**:

```
[Пример использования]
    |
    | Создание экземпляра CrawleePython
    |
    | Запуск обхода (crawler.run)
    |
[Конец]
```

**Примеры**:

```python
asyncio.run(main())
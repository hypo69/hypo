# Модуль `crawlee_python`

## Обзор

Модуль `crawlee_python` предоставляет пользовательскую реализацию `PlaywrightCrawler` с использованием библиотеки Crawlee. Он позволяет настраивать параметры браузера, обрабатывать запросы и извлекать данные с веб-страниц. Этот модуль предназначен для упрощения процесса веб-скрейпинга с использованием Crawlee и Playwright.

## Подробней

Этот модуль предоставляет класс `CrawleePython`, который является оберткой над `PlaywrightCrawler`. Он позволяет задавать максимальное количество запросов, режим работы браузера (с графическим интерфейсом или без), тип браузера (Chromium, Firefox, WebKit) и дополнительные опции запуска браузера. Основная цель модуля - предоставить удобный интерфейс для настройки и запуска веб-скрейпера с использованием Crawlee и Playwright.
Модуль использует `PlaywrightCrawler` для обхода веб-страниц, извлечения данных и сохранения результатов в формате JSON.

## Классы

### `CrawleePython`

**Описание**: Пользовательская реализация `PlaywrightCrawler` с использованием библиотеки Crawlee.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `CrawleePython`.
- `setup_crawler`: Настраивает экземпляр `PlaywrightCrawler` с указанными параметрами конфигурации.
- `run_crawler`: Запускает обход веб-страниц с использованием `PlaywrightCrawler`.
- `export_data`: Экспортирует извлеченные данные в JSON-файл.
- `get_data`: Получает извлеченные данные.
- `run`: Основной метод для настройки, запуска обхода и экспорта данных.

**Параметры**:
- `max_requests` (int): Максимальное количество запросов для выполнения во время обхода.
- `headless` (bool): Определяет, запускать ли браузер в режиме без графического интерфейса.
- `browser_type` (str): Тип используемого браузера ('chromium', 'firefox', 'webkit').
- `options` (Optional[List[str]]): Список дополнительных опций для передачи в браузер.

**Примеры**
```python
    crawler = CrawleePython(max_requests=5, headless=False, browser_type='firefox', options=["--headless"])
    await crawler.run(['https://www.example.com'])
```

## Функции

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
```

**Описание**: Инициализирует экземпляр класса `CrawleePython` с заданными параметрами.

**Параметры**:
- `max_requests` (int): Максимальное количество запросов для выполнения во время обхода. По умолчанию 5.
- `headless` (bool): Определяет, запускать ли браузер в режиме без графического интерфейса. По умолчанию `False`.
- `browser_type` (str): Тип используемого браузера ('chromium', 'firefox', 'webkit'). По умолчанию 'firefox'.
- `options` (Optional[List[str]]): Список дополнительных опций для передачи в браузер. По умолчанию `None`.

**Примеры**:
```python
crawler = CrawleePython(max_requests=10, headless=True, browser_type='chromium')
```

### `setup_crawler`

```python
async def setup_crawler(self):
    """
    Sets up the PlaywrightCrawler instance with the specified configuration.
    """
```

**Описание**: Настраивает экземпляр `PlaywrightCrawler` с указанной конфигурацией. Этот метод создает экземпляр `PlaywrightCrawler` с заданными параметрами, такими как максимальное количество запросов на обход, режим работы браузера без графического интерфейса и тип браузера. Также определяется обработчик запросов по умолчанию, который извлекает информацию со страницы и добавляет найденные ссылки в очередь.

### `run_crawler`

```python
async def run_crawler(self, urls: List[str]):
    """
    Runs the crawler with the initial list of URLs.

    :param urls: List of URLs to start the crawl.
    :type urls: List[str]
    """
```

**Описание**: Запускает обход веб-страниц с использованием `PlaywrightCrawler`.

**Параметры**:
- `urls` (List[str]): Список URL-адресов для начала обхода.

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
```

**Описание**: Экспортирует весь набор данных в JSON-файл.

**Параметры**:
- `file_path` (str): Путь для сохранения экспортированного JSON-файла.

**Примеры**:
```python
await crawler.export_data('data.json')
```

### `get_data`

```python
async def get_data(self) -> Dict[str, Any]:
    """
    Retrieves the extracted data.

    :return: Extracted data as a dictionary.
    :rtype: Dict[str, Any]
    """
```

**Описание**: Извлекает извлеченные данные.

**Возвращает**:
- `Dict[str, Any]`: Извлеченные данные в виде словаря.

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
```

**Описание**: Основной метод для настройки, запуска обхода и экспорта данных.

**Параметры**:
- `urls` (List[str]): Список URL-адресов для начала обхода.

**Примеры**:
```python
await crawler.run(['https://www.example.com'])
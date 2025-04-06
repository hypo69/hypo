# Модуль `crawlee_python`

## Обзор

Модуль `crawlee_python` предоставляет пользовательскую реализацию `PlaywrightCrawler` с использованием библиотеки Crawlee. Он позволяет настраивать параметры браузера, обрабатывать запросы и извлекать данные из веб-страниц.

## Подробней

Этот модуль предоставляет класс `CrawleePython`, который является оберткой для `PlaywrightCrawler` из библиотеки Crawlee. `CrawleePython` позволяет упростить настройку и запуск краулера, а также предоставляет методы для экспорта и получения извлеченных данных.

Модуль предназначен для автоматизации сбора данных с веб-страниц, используя возможности Playwright для управления браузером и Crawlee для организации процесса краулинга.

## Классы

### `CrawleePython`

**Описание**: Пользовательская реализация `PlaywrightCrawler` с использованием библиотеки Crawlee.

**Принцип работы**:
Класс `CrawleePython` инициализируется с параметрами, определяющими поведение краулера, такими как максимальное количество запросов, режим работы браузера (с графическим интерфейсом или без), тип браузера и дополнительные опции. Затем создается экземпляр `PlaywrightCrawler` с этими параметрами.

Основная логика работы класса заключается в настройке обработчика запросов, который извлекает данные из веб-страниц и добавляет ссылки на другие страницы в очередь. После завершения работы краулера данные экспортируются в JSON-файл.

**Аттрибуты**:

- `max_requests` (int): Максимальное количество запросов для выполнения во время обхода.
- `headless` (bool): Определяет, запускать ли браузер в режиме без графического интерфейса.
- `browser_type` (str): Тип используемого браузера ('chromium', 'firefox', 'webkit').
- `crawler` (PlaywrightCrawler): Экземпляр PlaywrightCrawler.
- `options` (List[str]): Список дополнительных аргументов командной строки для запуска браузера.

**Методы**:

- `__init__`: Инициализирует экземпляр класса `CrawleePython`.
- `setup_crawler`: Настраивает экземпляр `PlaywrightCrawler`.
- `run_crawler`: Запускает обход веб-страниц.
- `export_data`: Экспортирует извлеченные данные в JSON-файл.
- `get_data`: Извлекает данные, собранные краулером.
- `run`: Главный метод для запуска, настройки краулера и экспорта данных.

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

**Назначение**: Инициализирует класс `CrawleePython` с заданными параметрами.

**Параметры**:

- `max_requests` (int): Максимальное количество запросов для выполнения во время обхода. По умолчанию 5.
- `headless` (bool): Определяет, запускать ли браузер в режиме без графического интерфейса. По умолчанию `False`.
- `browser_type` (str): Тип используемого браузера ('chromium', 'firefox', 'webkit'). По умолчанию 'firefox'.
- `options` (Optional[List[str]]): Список дополнительных аргументов командной строки для запуска браузера. По умолчанию `None`.

**Как работает функция**:

1.  Инициализирует атрибуты класса значениями, переданными в качестве аргументов.
2.  Если `options` не передан, инициализирует `self.options` пустым списком.
3.  Инициализирует `self.crawler` значением `None`.

**Примеры**:

```python
crawler = CrawleePython(max_requests=10, headless=True, browser_type='chromium')
crawler = CrawleePython(max_requests=5, browser_type='firefox', options=["--disable-gpu", "--no-sandbox"])
```

### `setup_crawler`

```python
async def setup_crawler(self):
    """
    Sets up the PlaywrightCrawler instance with the specified configuration.
    """
```

**Назначение**: Настраивает экземпляр `PlaywrightCrawler` с указанной конфигурацией.

**Как работает функция**:

1.  Создает экземпляр `PlaywrightCrawler` с параметрами `max_requests_per_crawl`, `headless` и `browser_type`, взятыми из атрибутов экземпляра `CrawleePython`.
2.  Устанавливает обработчик по умолчанию для всех запросов (`self.crawler.router.default_handler`).

    A
    ↓
    B

    Где:

    - A: Создание экземпляра `PlaywrightCrawler` с заданными параметрами.
    - B: Установка обработчика по умолчанию для всех запросов.
3. Вложенная функция `request_handler` обрабатывает запросы, логирует URL, добавляет ссылки на странице в очередь и извлекает данные (URL, заголовок, содержимое). Извлеченные данные добавляются в набор данных.

#### `request_handler`

```python
async def request_handler(context: PlaywrightCrawlingContext) -> None:
    """
    Default request handler for processing web pages.

    :param context: The crawling context.
    :type context: PlaywrightCrawlingContext
    """
```

**Назначение**: Обработчик запросов по умолчанию для обработки веб-страниц.

**Параметры**:

- `context` (PlaywrightCrawlingContext): Контекст обхода.

**Как работает функция**:

1.  Логирует информацию об обрабатываемом URL.
2.  Добавляет все найденные на странице ссылки в очередь на обработку.
3.  Извлекает данные (URL, заголовок, содержимое) из страницы с использованием API Playwright.
4.  Добавляет извлеченные данные в набор данных.

    A
    ↓
    B
    ↓
    C
    ↓
    D

    Где:

    - A: Логирование информации об обрабатываемом URL.
    - B: Добавление всех найденных на странице ссылок в очередь на обработку.
    - C: Извлечение данных (URL, заголовок, содержимое) из страницы с использованием API Playwright.
    - D: Добавление извлеченных данных в набор данных.

**Примеры**:

```python
await self.setup_crawler()
```

### `run_crawler`

```python
async def run_crawler(self, urls: List[str]):
    """
    Runs the crawler with the initial list of URLs.

    :param urls: List of URLs to start the crawl.
    :type urls: List[str]
    """
```

**Назначение**: Запускает краулер с начальным списком URL.

**Параметры**:

- `urls` (List[str]): Список URL для начала обхода.

**Как работает функция**:

1.  Запускает краулер с предоставленным списком URL, используя метод `self.crawler.run(urls)`.

    A
    ↓
    B

    Где:

    - A: Определение списка URL.
    - B: Запуск краулера с заданными URL.

**Примеры**:

```python
await self.run_crawler(['https://www.example.com', 'https://www.example.org'])
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

**Назначение**: Экспортирует весь набор данных в JSON-файл.

**Параметры**:

- `file_path` (str): Путь для сохранения экспортированного JSON-файла.

**Как работает функция**:

1.  Экспортирует данные в JSON-файл, используя метод `self.crawler.export_data(file_path)`.

    A
    ↓
    B

    Где:

    - A: Определение пути к файлу.
    - B: Экспорт данных в JSON-файл.

**Примеры**:

```python
await self.export_data('data.json')
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

**Назначение**: Извлекает извлеченные данные.

**Возвращает**:

- `Dict[str, Any]`: Извлеченные данные в виде словаря.

**Как работает функция**:

1.  Извлекает данные, используя метод `self.crawler.get_data()`.
2.  Возвращает извлеченные данные.

    A
    ↓
    B

    Где:

    - A: Извлечение данных.
    - B: Возврат извлеченных данных.

**Примеры**:

```python
data = await self.get_data()
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

**Назначение**: Главный метод для настройки, запуска краулера и экспорта данных.

**Параметры**:

- `urls` (List[str]): Список URL для начала обхода.

**Как работает функция**:

1.  Вызывает `self.setup_crawler()` для настройки краулера.
2.  Вызывает `self.run_crawler(urls)` для запуска краулера с предоставленным списком URL.
3.  Вызывает `self.export_data()` для экспорта данных в JSON-файл.
4.  Получает данные, используя метод `self.get_data()`.
5.  Логирует извлеченные данные.
6.  Обрабатывает исключения, которые могут возникнуть в процессе выполнения.

    A
    ↓
    B
    ↓
    C
    ↓
    D
    ↓
    E

    Где:

    - A: Настройка краулера.
    - B: Запуск краулера с заданными URL.
    - C: Экспорт данных в JSON-файл.
    - D: Получение извлеченных данных.
    - E: Логирование извлеченных данных.

**Примеры**:

```python
await crawler.run(['https://www.example.com'])
```

## Функции

### `main`

```python
async def main():
    crawler = CrawleePython(max_requests=5, headless=False, browser_type='firefox', options=["--headless"])
    await crawler.run(['https://www.example.com'])
```

**Назначение**: Пример использования класса `CrawleePython`.

**Как работает функция**:

1. Создает экземпляр класса `CrawleePython` с заданными параметрами.
2. Запускает краулер с URL `https://www.example.com`.

**Примеры**:

```python
asyncio.run(main())
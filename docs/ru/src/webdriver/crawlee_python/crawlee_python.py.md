# Модуль `crawlee_python`

## Обзор

Модуль `crawlee_python` предоставляет пользовательскую реализацию `PlaywrightCrawler` с использованием библиотеки Crawlee. Он позволяет настраивать параметры браузера, обрабатывать запросы и извлекать данные с веб-страниц.

## Подробней

Этот модуль предназначен для создания и управления веб-скрейперами с использованием Crawlee и Playwright. Он позволяет запускать браузеры в headless-режиме, устанавливать максимальное количество запросов и экспортировать извлеченные данные в JSON-файл.

## Классы

### `CrawleePython`

**Описание**: Пользовательская реализация `PlaywrightCrawler` с использованием библиотеки Crawlee.

**Принцип работы**:
Класс `CrawleePython` инициализируется с параметрами, определяющими поведение краулера, такими как максимальное количество запросов, режим работы браузера (headless или нет) и тип браузера. Он создает экземпляр `PlaywrightCrawler` и настраивает обработчик запросов по умолчанию, который извлекает данные со страниц и добавляет найденные ссылки в очередь.

**Аттрибуты**:
- `max_requests` (int): Максимальное количество запросов для выполнения во время обхода.
- `headless` (bool): Определяет, запускать ли браузер в headless-режиме.
- `browser_type` (str): Тип используемого браузера ('chromium', 'firefox', 'webkit').
- `crawler` (PlaywrightCrawler): Экземпляр PlaywrightCrawler.
- `options` (Optional[List[str]]): Список пользовательских параметров для передачи в браузер.

**Методы**:
- `__init__(self, max_requests: int = 5, headless: bool = False, browser_type: str = 'firefox', options: Optional[List[str]] = None)`: Инициализирует краулер CrawleePython с указанными параметрами.
- `setup_crawler(self)`: Настраивает экземпляр PlaywrightCrawler с указанной конфигурацией.
- `run_crawler(self, urls: List[str])`: Запускает краулер с начальным списком URL-адресов.
- `export_data(self, file_path: str)`: Экспортирует весь набор данных в JSON-файл.
- `get_data(self) -> Dict[str, Any]`: Извлекает извлеченные данные.
- `run(self, urls: List[str])`: Основной метод для настройки, запуска краулера и экспорта данных.

#### `__init__(self, max_requests: int = 5, headless: bool = False, browser_type: str = 'firefox', options: Optional[List[str]] = None)`

```python
def __init__(self, max_requests: int = 5, headless: bool = False, browser_type: str = 'firefox', options: Optional[List[str]] = None):
    """
    Initializes the CrawleePython crawler with the specified parameters.

    :param max_requests: Maximum number of requests to perform during the crawl.
    :type max_requests: int
    :param headless: Whether to run the browser in headless mode.
    :type headless: bool
    :param browser_type: The type of browser to use (\'chromium\', \'firefox\', \'webkit\').
    :type browser_type: str
    :param options: A list of custom options to pass to the browser.
    :type options: Optional[List[str]]
    """
    self.max_requests = max_requests
    self.headless = headless
    self.browser_type = browser_type
    self.options = options or []
    self.crawler = None
```

**Назначение**: Инициализирует экземпляр класса `CrawleePython` с заданными параметрами.

**Параметры**:
- `max_requests` (int): Максимальное количество запросов для выполнения во время обхода. По умолчанию `5`.
- `headless` (bool): Определяет, запускать ли браузер в headless-режиме. По умолчанию `False`.
- `browser_type` (str): Тип используемого браузера ('chromium', 'firefox', 'webkit'). По умолчанию `'firefox'`.
- `options` (Optional[List[str]]): Список пользовательских параметров для передачи в браузер. По умолчанию `None`.

**Как работает функция**:
1.  Присваивает значения атрибутам экземпляра класса на основе переданных аргументов.
2.  Если `options` не переданы, инициализирует `self.options` пустым списком.
3.  Устанавливает `self.crawler` в `None`.

#### `setup_crawler(self)`

```python
async def setup_crawler(self):
    """
    Sets up the PlaywrightCrawler instance with the specified configuration.
    """
    self.crawler = PlaywrightCrawler(
        max_requests_per_crawl=self.max_requests,
        headless=self.headless,
        browser_type=self.browser_type,
        launch_options={"args": self.options}
    )

    @self.crawler.router.default_handler
    async def request_handler(context: PlaywrightCrawlingContext) -> None:
        """
        Default request handler for processing web pages.

        :param context: The crawling context.
        :type context: PlaywrightCrawlingContext
        """
        context.log.info(f'Processing {context.request.url} ...')

        # Enqueue all links found on the page.
        await context.enqueue_links()

        # Extract data from the page using Playwright API.
        data = {
            'url': context.request.url,
            'title': await context.page.title(),
            'content': (await context.page.content())[:100],
        }

        # Push the extracted data to the default dataset.
        await context.push_data(data)
```

**Назначение**: Настраивает экземпляр `PlaywrightCrawler` с указанной конфигурацией.

**Как работает функция**:
1.  Создает экземпляр `PlaywrightCrawler` с заданными параметрами, такими как `max_requests_per_crawl`, `headless`, `browser_type` и `launch_options`.
2.  Определяет асинхронный обработчик запросов `request_handler` для обработки веб-страниц.

**Внутренние функции**:
- `request_handler(context: PlaywrightCrawlingContext) -> None`: Обработчик запросов по умолчанию для обработки веб-страниц.
    - **Параметры**:
        - `context` (PlaywrightCrawlingContext): Контекст обхода.
    - **Как работает функция**:
        1.  Логирует информацию об обрабатываемом URL.
        2.  Добавляет все найденные ссылки на странице в очередь.
        3.  Извлекает данные со страницы с использованием Playwright API, такие как URL, заголовок и первые 100 символов содержимого.
        4.  Помещает извлеченные данные в набор данных по умолчанию.

#### `run_crawler(self, urls: List[str])`

```python
async def run_crawler(self, urls: List[str]):
    """
    Runs the crawler with the initial list of URLs.

    :param urls: List of URLs to start the crawl.
    :type urls: List[str]
    """
    await self.crawler.run(urls)
```

**Назначение**: Запускает краулер с начальным списком URL-адресов.

**Параметры**:
- `urls` (List[str]): Список URL-адресов для начала обхода.

**Как работает функция**:
1.  Вызывает метод `run` экземпляра `PlaywrightCrawler` с переданным списком URL-адресов.

#### `export_data(self, file_path: str)`

```python
async def export_data(self, file_path: str):
    """
    Exports the entire dataset to a JSON file.

    :param file_path: Path to save the exported JSON file.
    :type file_path: str
    """
    await self.crawler.export_data(file_path)
```

**Назначение**: Экспортирует весь набор данных в JSON-файл.

**Параметры**:
- `file_path` (str): Путь для сохранения экспортированного JSON-файла.

**Как работает функция**:
1.  Вызывает метод `export_data` экземпляра `PlaywrightCrawler` с указанным путем к файлу.

#### `get_data(self) -> Dict[str, Any]`

```python
async def get_data(self) -> Dict[str, Any]:
    """
    Retrieves the extracted data.

    :return: Extracted data as a dictionary.
    :rtype: Dict[str, Any]
    """
    data = await self.crawler.get_data()
    return data
```

**Назначение**: Извлекает извлеченные данные.

**Возвращает**:
- `Dict[str, Any]`: Извлеченные данные в виде словаря.

**Как работает функция**:
1.  Вызывает метод `get_data` экземпляра `PlaywrightCrawler`.
2.  Возвращает извлеченные данные.

#### `run(self, urls: List[str])`

```python
async def run(self, urls: List[str]):
    """
    Main method to set up, run the crawler, and export data.

    :param urls: List of URLs to start the crawl.
    :type urls: List[str]
    """
    try:
        await self.setup_crawler()
        await self.run_crawler(urls)
        await self.export_data(str(Path(gs.path.tmp / 'results.json')))
        data = await self.get_data()
        logger.info(f'Extracted data: {data.items()}')
    except Exception as ex:
        logger.critical('Crawler failed with an error:', ex)
```

**Назначение**: Основной метод для настройки, запуска краулера и экспорта данных.

**Параметры**:
- `urls` (List[str]): Список URL-адресов для начала обхода.

**Как работает функция**:
1.  Вызывает метод `setup_crawler` для настройки краулера.
2.  Вызывает метод `run_crawler` для запуска краулера с переданным списком URL-адресов.
3.  Вызывает метод `export_data` для экспорта данных в JSON-файл `results.json` во временной директории.
4.  Вызывает метод `get_data` для извлечения данных.
5.  Логирует извлеченные данные.
6.  В случае возникновения ошибки логирует критическую информацию об ошибке.

## Функции

В данном модуле нет отдельных функций, только методы класса `CrawleePython`.

## Примеры

```python
if __name__ == '__main__':
    async def main():
        crawler = CrawleePython(max_requests=5, headless=False, browser_type='firefox', options=["--headless"])
        await crawler.run(['https://www.example.com'])

    asyncio.run(main())
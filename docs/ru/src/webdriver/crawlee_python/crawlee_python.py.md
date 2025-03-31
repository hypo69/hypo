# Модуль `crawlee_python`

## Обзор

Модуль предоставляет пользовательскую реализацию `PlaywrightCrawler` с использованием библиотеки Crawlee. Это позволяет настраивать параметры браузера, обрабатывать запросы и извлекать данные из веб-страниц.

## Подробней

Этот модуль предназначен для создания веб-краулеров с использованием библиотеки Crawlee и Playwright. Он позволяет автоматизировать навигацию по веб-страницам, сбор данных и экспорт результатов. Модуль предоставляет класс `CrawleePython`, который упрощает настройку и запуск краулера с различными параметрами, такими как максимальное количество запросов, режим работы браузера (с графическим интерфейсом или без) и тип браузера.

## Классы

### `CrawleePython`

**Описание**: Класс, представляющий собой пользовательскую реализацию `PlaywrightCrawler` с использованием библиотеки Crawlee.

**Как работает класс**:
1.  Инициализируется с заданными параметрами, такими как максимальное количество запросов, режим работы браузера и тип браузера.
2.  Метод `setup_crawler` создает экземпляр `PlaywrightCrawler` с указанной конфигурацией и настраивает обработчик запросов по умолчанию.
3.  Обработчик запросов по умолчанию (`request_handler`) извлекает данные со страницы, такие как URL, заголовок и содержимое, а также добавляет найденные ссылки в очередь для дальнейшей обработки.
4.  Метод `run_crawler` запускает краулер с начальным списком URL.
5.  Метод `export_data` экспортирует извлеченные данные в JSON-файл.
6.  Метод `get_data` возвращает извлеченные данные в виде словаря.
7.  Метод `run` объединяет все этапы: настройку, запуск краулера и экспорт данных.

**Методы**:

*   `__init__`: Инициализирует экземпляр класса `CrawleePython`.
*   `setup_crawler`: Настраивает экземпляр `PlaywrightCrawler`.
*   `run_crawler`: Запускает краулер с заданными URL.
*   `export_data`: Экспортирует извлеченные данные в JSON-файл.
*   `get_data`: Возвращает извлеченные данные.
*   `run`: Запускает краулер и экспортирует данные.

**Параметры**:

*   `max_requests` (int): Максимальное количество запросов для выполнения во время обхода.
*   `headless` (bool): Определяет, запускать ли браузер в режиме без графического интерфейса.
*   `browser_type` (str): Тип используемого браузера ('chromium', 'firefox', 'webkit').
*   `crawler` (PlaywrightCrawler): Экземпляр PlaywrightCrawler.
*   `options` (Optional[List[str]]): Список пользовательских опций для передачи в браузер.

**Примеры**

```python
if __name__ == "__main__":
    async def main():
        crawler = CrawleePython(max_requests=5, headless=False, browser_type='firefox', options=["--headless"])
        await crawler.run(['https://www.example.com'])

    asyncio.run(main())
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

**Описание**: Инициализирует класс `CrawleePython` с заданными параметрами.

**Как работает функция**:
Функция инициализирует экземпляр класса `CrawleePython`, устанавливая значения атрибутов `max_requests`, `headless`, `browser_type` и `options` на основе переданных аргументов. Если аргумент `options` не передан, он инициализируется пустым списком. Также инициализируется атрибут `crawler` значением `None`.

**Параметры**:

*   `max_requests` (int): Максимальное количество запросов для выполнения во время обхода. По умолчанию 5.
*   `headless` (bool): Определяет, запускать ли браузер в режиме без графического интерфейса. По умолчанию `False`.
*   `browser_type` (str): Тип используемого браузера ('chromium', 'firefox', 'webkit'). По умолчанию 'firefox'.
*   `options` (Optional[List[str]]): Список пользовательских опций для передачи в браузер. По умолчанию `None`.

**Примеры**:

```python
crawler = CrawleePython(max_requests=10, headless=True, browser_type='chromium', options=['--disable-gpu'])
```

### `setup_crawler`

```python
async def setup_crawler(self):
    """
    Sets up the PlaywrightCrawler instance with the specified configuration.
    """
```

**Описание**: Настраивает экземпляр `PlaywrightCrawler` с указанной конфигурацией.

**Как работает функция**:

1.  Создает экземпляр `PlaywrightCrawler` с параметрами `max_requests_per_crawl`, `headless` и `browser_type`, взятыми из атрибутов экземпляра класса `CrawleePython`.
2.  Устанавливает обработчик запросов по умолчанию (`request_handler`) с использованием декоратора `@self.crawler.router.default_handler`.

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
```

**Описание**: Обработчик запросов по умолчанию для обработки веб-страниц.

**Как работает функция**:

1.  Выводит информационное сообщение в лог о начале обработки URL.
2.  Добавляет все ссылки, найденные на странице, в очередь для дальнейшей обработки.
3.  Извлекает данные со страницы, такие как URL, заголовок и содержимое (первые 100 символов).
4.  Сохраняет извлеченные данные в словарь.
5.  Отправляет извлеченные данные в набор данных по умолчанию.

**Параметры**:

*   `context` (PlaywrightCrawlingContext): Контекст обхода, содержащий информацию о текущем запросе и странице.

**Примеры**:

```python
@self.crawler.router.default_handler
async def request_handler(context: PlaywrightCrawlingContext) -> None:
    ...
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

**Описание**: Запускает краулер с начальным списком URL.

**Как работает функция**:
Функция запускает краулер, используя метод `run` объекта `self.crawler` и передавая ему список URL для начала обхода.

**Параметры**:

*   `urls` (List[str]): Список URL для запуска обхода.

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

**Как работает функция**:
Функция вызывает метод `export_data` объекта `self.crawler`, передавая ему путь к файлу, в который нужно экспортировать данные.

**Параметры**:

*   `file_path` (str): Путь для сохранения экспортированного JSON-файла.

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
```

**Описание**: Извлекает извлеченные данные.

**Как работает функция**:
Функция вызывает метод `get_data` объекта `self.crawler` и возвращает полученные данные.

**Возвращает**:

*   `Dict[str, Any]`: Извлеченные данные в виде словаря.

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

**Описание**: Основной метод для настройки, запуска краулера и экспорта данных.

**Как работает функция**:

1.  Вызывает метод `setup_crawler` для настройки краулера.
2.  Вызывает метод `run_crawler` для запуска краулера с заданными URL.
3.  Вызывает метод `export_data` для экспорта данных в JSON-файл (`results.json` во временной директории).
4.  Вызывает метод `get_data` для получения извлеченных данных.
5.  Выводит информацию об извлеченных данных в лог.
6.  Обрабатывает исключения, которые могут возникнуть в процессе работы краулера, и выводит сообщение об ошибке в лог.

**Параметры**:

*   `urls` (List[str]): Список URL для запуска обхода.

**Вызывает исключения**:

*   `Exception`: Если возникает ошибка во время работы краулера.

**Примеры**:

```python
await crawler.run(['https://www.example.com'])
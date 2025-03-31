# Модуль `crawlee_python`

## Обзор

Модуль `crawlee_python` предоставляет пользовательскую реализацию `PlaywrightCrawler` с использованием библиотеки Crawlee. Он позволяет настраивать параметры браузера, обрабатывать запросы и извлекать данные с веб-страниц.

## Подробней

Этот модуль предназначен для создания и управления веб-скраперами на основе Crawlee и Playwright. Он предоставляет удобный интерфейс для настройки параметров браузера, обработки веб-страниц и извлечения данных. Модуль позволяет запускать браузер в headless-режиме, выбирать тип браузера (Chromium, Firefox, WebKit) и передавать пользовательские параметры запуска браузера.

## Классы

### `CrawleePython`

**Описание**: Класс `CrawleePython` представляет собой пользовательскую реализацию веб-скрапера на основе `PlaywrightCrawler` из библиотеки Crawlee.

**Как работает класс**:
1.  **Инициализация**: При инициализации класса задаются основные параметры краулера, такие как максимальное количество запросов (`max_requests`), режим работы браузера без графического интерфейса (`headless`), тип используемого браузера (`browser_type`) и дополнительные опции для запуска браузера (`options`).
2.  **Настройка краулера**: Метод `setup_crawler` создает экземпляр `PlaywrightCrawler` с заданными параметрами и определяет обработчик запросов по умолчанию (`request_handler`).
3.  **Обработка запросов**: `request_handler` вызывается для каждой посещенной страницы. Он извлекает информацию, такую как URL, заголовок и контент страницы, а также добавляет найденные на странице ссылки в очередь для дальнейшей обработки.
4.  **Запуск краулера**: Метод `run_crawler` запускает процесс сканирования с использованием предоставленного списка URL.
5.  **Экспорт данных**: Метод `export_data` экспортирует извлеченные данные в JSON-файл.
6.  **Получение данных**: Метод `get_data` возвращает извлеченные данные в виде словаря.
7.  **Запуск и управление**: Метод `run` объединяет все этапы: настройку, запуск краулера и экспорт данных.

**Методы**:

*   `__init__`: Инициализирует экземпляр класса `CrawleePython`.
*   `setup_crawler`: Настраивает экземпляр `PlaywrightCrawler`.
*   `run_crawler`: Запускает краулер с заданным списком URL.
*   `export_data`: Экспортирует данные в JSON-файл.
*   `get_data`: Возвращает извлеченные данные.
*   `run`: Запускает краулер, обрабатывает данные и экспортирует результаты.

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

**Назначение**: Инициализация экземпляра класса `CrawleePython` с заданными параметрами.

**Как работает функция**:

1.  Принимает параметры: `max_requests` (максимальное количество запросов), `headless` (режим без графического интерфейса), `browser_type` (тип браузера) и `options` (дополнительные опции для запуска браузера).
2.  Устанавливает значения атрибутов экземпляра класса на основе переданных параметров. Если `options` не переданы, инициализирует их пустым списком.

**Параметры**:

*   `max_requests` (int): Максимальное количество запросов для выполнения во время обхода. По умолчанию 5.
*   `headless` (bool): Определяет, запускать ли браузер в режиме без графического интерфейса. По умолчанию `False`.
*   `browser_type` (str): Тип используемого браузера (`'chromium'`, `'firefox'`, `'webkit'`). По умолчанию `'firefox'`.
*   `options` (Optional[List[str]]): Список пользовательских опций для передачи в браузер. По умолчанию `None`.

**Возвращает**:
    -   `None`

**Вызывает исключения**:
    -   Отсутствуют

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

**Назначение**: Настраивает экземпляр `PlaywrightCrawler` с указанной конфигурацией.

**Как работает функция**:

1.  Создает экземпляр `PlaywrightCrawler` с параметрами, установленными при инициализации класса: `max_requests_per_crawl`, `headless` и `browser_type`.
2.  Устанавливает обработчик запросов по умолчанию (`request_handler`) для обработки веб-страниц.
3.  Обработчик запросов извлекает URL, заголовок и первые 100 символов контента страницы, а также добавляет найденные на странице ссылки в очередь для дальнейшей обработки.
4.  Извлеченные данные помещаются в набор данных по умолчанию.

**Параметры**:

*   `self` (CrawleePython): Экземпляр класса `CrawleePython`.

**Возвращает**:
    -   `None`

**Вызывает исключения**:
    -   Отсутствуют

**Примеры**:

```python
await crawler.setup_crawler()
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

**Как работает функция**:

1.  Принимает список URL в качестве аргумента.
2.  Вызывает метод `run` экземпляра `PlaywrightCrawler` для запуска процесса сканирования с использованием предоставленных URL.

**Параметры**:

*   `self` (CrawleePython): Экземпляр класса `CrawleePython`.
*   `urls` (List[str]): Список URL для запуска сканирования.

**Возвращает**:
    -   `None`

**Вызывает исключения**:
    -   Отсутствуют

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

**Назначение**: Экспортирует весь набор данных в JSON-файл.

**Как работает функция**:

1.  Принимает путь к файлу, в который нужно сохранить экспортированные данные.
2.  Вызывает метод `export_data` экземпляра `PlaywrightCrawler` для выполнения экспорта данных в указанный файл.

**Параметры**:

*   `self` (CrawleePython): Экземпляр класса `CrawleePython`.
*   `file_path` (str): Путь для сохранения экспортированного JSON-файла.

**Возвращает**:
    -   `None`

**Вызывает исключения**:
    -   Отсутствуют

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

**Назначение**: Извлекает полученные данные.

**Как работает функция**:

1.  Вызывает метод `get_data` экземпляра `PlaywrightCrawler` для получения извлеченных данных.
2.  Возвращает извлеченные данные в виде словаря.

**Параметры**:

*   `self` (CrawleePython): Экземпляр класса `CrawleePython`.

**Возвращает**:

*   `Dict[str, Any]`: Извлеченные данные в виде словаря.

**Вызывает исключения**:
    -   Отсутствуют

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

**Назначение**: Основной метод для настройки, запуска краулера и экспорта данных.

**Как работает функция**:

1.  Принимает список URL в качестве аргумента для запуска сканирования.
2.  Вызывает метод `setup_crawler` для настройки краулера.
3.  Вызывает метод `run_crawler` для запуска процесса сканирования.
4.  Вызывает метод `export_data` для экспорта извлеченных данных в JSON-файл `results.json` во временную директорию.
5.  Вызывает метод `get_data` для получения извлеченных данных.
6.  Логирует извлеченные данные, используя `logger.info`.
7.  Обрабатывает возможные исключения, возникающие в процессе, и логирует критическую ошибку с использованием `logger.critical`.

**Параметры**:

*   `self` (CrawleePython): Экземпляр класса `CrawleePython`.
*   `urls` (List[str]): Список URL для запуска сканирования.

**Возвращает**:
    -   `None`

**Вызывает исключения**:
    -   `Exception`: Если возникает ошибка во время настройки, запуска или экспорта данных.

**Примеры**:

```python
await crawler.run(['https://www.example.com', 'https://www.example.org'])
```

## Функции

### `request_handler`

```python
async def request_handler(context: PlaywrightCrawlingContext) -> None:
    """
    Default request handler for processing web pages.

    :param context: The crawling context.
    :type context: PlaywrightCrawlingContext
    """
```

**Назначение**: Обработчик запросов по умолчанию для обработки веб-страниц.

**Как работает функция**:

1.  Логирует информацию об обрабатываемом URL с использованием `context.log.info`.
2.  Добавляет все найденные на странице ссылки в очередь для дальнейшей обработки с использованием `context.enqueue_links()`.
3.  Извлекает данные со страницы, такие как URL, заголовок и первые 100 символов контента, используя API Playwright.
4.  Помещает извлеченные данные в набор данных по умолчанию с использованием `context.push_data()`.

**Параметры**:

*   `context` (PlaywrightCrawlingContext): Контекст сканирования, предоставляющий доступ к информации о текущем запросе и странице.

**Возвращает**:
    -   `None`

**Вызывает исключения**:
    -   Отсутствуют

**Примеры**:
    -   Этот обработчик устанавливается внутри `setup_crawler` и вызывается автоматически для каждой страницы, посещенной краулером.

## Примеры использования

```python
if __name__ == "__main__":
    async def main():
        crawler = CrawleePython(max_requests=5, headless=False, browser_type='firefox', options=["--headless"])
        await crawler.run(['https://www.example.com'])

    asyncio.run(main())
```
```
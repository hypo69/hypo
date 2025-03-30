# Модуль `crawlee_python`

## Обзор

Модуль `crawlee_python` предоставляет пользовательскую реализацию `PlaywrightCrawler` с использованием библиотеки Crawlee. Он позволяет настраивать параметры браузера, обрабатывать запросы и извлекать данные с веб-страниц.

## Подробнее

Этот модуль предназначен для создания веб-скраперов, использующих возможности Crawlee и Playwright. Он позволяет запускать браузеры (Chromium, Firefox, Webkit) в headless-режиме или с графическим интерфейсом, ограничивать количество запросов и извлекать данные с веб-страниц. Извлеченные данные сохраняются в формате JSON.

## Классы

### `CrawleePython`

**Описание**: Пользовательская реализация `PlaywrightCrawler` с использованием библиотеки Crawlee.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `CrawleePython`.
- `setup_crawler`: Настраивает экземпляр `PlaywrightCrawler` с указанной конфигурацией.
- `run_crawler`: Запускает краулер с начальным списком URL-адресов.
- `export_data`: Экспортирует весь набор данных в JSON-файл.
- `get_data`: Извлекает извлеченные данные.
- `run`: Основной метод для настройки, запуска краулера и экспорта данных.

**Параметры**:
- `max_requests` (int): Максимальное количество запросов для выполнения во время обхода.
- `headless` (bool): Определяет, запускать ли браузер в headless-режиме.
- `browser_type` (str): Тип используемого браузера ('chromium', 'firefox', 'webkit').
- `options` (Optional[List[str]]): Список пользовательских параметров для передачи в браузер.

**Примеры**

```python
crawler = CrawleePython(max_requests=5, headless=False, browser_type='firefox', options=["--headless"])
```

## Функции

### `__init__`

```python
def __init__(self, max_requests: int = 5, headless: bool = False, browser_type: str = 'firefox', options: Optional[List[str]] = None):
    """
    Args:
        max_requests (int): Maximum number of requests to perform during the crawl.
        headless (bool): Whether to run the browser in headless mode.
        browser_type (str): The type of browser to use ('chromium', 'firefox', 'webkit').
        options (Optional[List[str]], optional): A list of custom options to pass to the browser. Defaults to None.
    """
```

**Описание**: Инициализирует класс `CrawleePython` с заданными параметрами.

**Параметры**:
- `max_requests` (int): Максимальное количество запросов для выполнения во время обхода. По умолчанию 5.
- `headless` (bool): Определяет, запускать ли браузер в headless-режиме. По умолчанию `False`.
- `browser_type` (str): Тип используемого браузера ('chromium', 'firefox', 'webkit'). По умолчанию 'firefox'.
- `options` (Optional[List[str]]): Список пользовательских параметров для передачи в браузер. По умолчанию `None`.

**Примеры**:

```python
crawler = CrawleePython(max_requests=10, headless=True, browser_type='chromium')
```

### `setup_crawler`

```python
async def setup_crawler(self):
    """
    """
```

**Описание**: Настраивает экземпляр `PlaywrightCrawler` с указанной конфигурацией.

**Примеры**:

```python
crawler = CrawleePython()
await crawler.setup_crawler()
```

### `run_crawler`

```python
async def run_crawler(self, urls: List[str]):
    """
    Args:
        urls (List[str]): List of URLs to start the crawl.
    """
```

**Описание**: Запускает краулер с начальным списком URL-адресов.

**Параметры**:
- `urls` (List[str]): Список URL-адресов для начала обхода.

**Примеры**:

```python
crawler = CrawleePython()
await crawler.setup_crawler()
await crawler.run_crawler(['https://www.example.com', 'https://www.example.org'])
```

### `export_data`

```python
async def export_data(self, file_path: str):
    """
    Args:
        file_path (str): Path to save the exported JSON file.
    """
```

**Описание**: Экспортирует весь набор данных в JSON-файл.

**Параметры**:
- `file_path` (str): Путь для сохранения экспортированного JSON-файла.

**Примеры**:

```python
crawler = CrawleePython()
await crawler.setup_crawler()
await crawler.run_crawler(['https://www.example.com'])
await crawler.export_data('data.json')
```

### `get_data`

```python
async def get_data(self) -> Dict[str, Any]:
    """
    Returns:
        Dict[str, Any]: Extracted data as a dictionary.
    """
```

**Описание**: Извлекает извлеченные данные.

**Возвращает**:
- `Dict[str, Any]`: Извлеченные данные в виде словаря.

**Примеры**:

```python
crawler = CrawleePython()
await crawler.setup_crawler()
await crawler.run_crawler(['https://www.example.com'])
data = await crawler.get_data()
print(data)
```

### `run`

```python
async def run(self, urls: List[str]):
    """
    Args:
        urls (List[str]): List of URLs to start the crawl.
    """
```

**Описание**: Основной метод для настройки, запуска краулера и экспорта данных.

**Параметры**:
- `urls` (List[str]): Список URL-адресов для начала обхода.

**Примеры**:

```python
crawler = CrawleePython()
await crawler.run(['https://www.example.com', 'https://www.example.org'])
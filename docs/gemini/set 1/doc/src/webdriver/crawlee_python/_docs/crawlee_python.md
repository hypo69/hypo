# Модуль crawlee_python

## Обзор

Данный модуль предоставляет класс `CrawleePython` для выполнения веб-скрейпинга с использованием библиотеки `crawlee` и фреймворка Playwright.  Класс позволяет настроить и запустить процесс сбора данных с веб-сайтов, извлечь определенную информацию и сохранить результаты в формате JSON.

## Оглавление

* [Классы](#классы)
    * [CrawleePython](#crawleepython)
        * [__init__](#init)
        * [setup_crawler](#setup-crawler)
        * [run_crawler](#run-crawler)
        * [export_data](#export-data)
        * [get_data](#get-data)
        * [run](#run)

## Классы

### `CrawleePython`

**Описание**: Класс для выполнения веб-скрейпинга с использованием Playwright.

#### `__init__`

**Описание**: Конструктор класса. Инициализирует объект `PlaywrightCrawler` с заданными параметрами.

```python
def __init__(self, max_requests: int, headless: bool = True, browser_type: str = 'chromium'):
    """
    Args:
        max_requests (int): Максимальное количество запросов во время сбора данных.
        headless (bool, optional): Флаг, указывающий на работу в бескладовом режиме. По умолчанию True.
        browser_type (str, optional): Тип браузера (например, 'chromium', 'firefox'). По умолчанию 'chromium'.

    Raises:
        ValueError: Если `max_requests` не является положительным числом.
    """
```

#### `setup_crawler`

**Описание**: Настройка обработчика запросов для сбора данных.

```python
def setup_crawler(self):
    """
    Args:
        self: Экземпляр класса CrawleePython.

    Returns:
        None

    """
```

#### `run_crawler`

**Описание**: Запуск процесса сбора данных с заданным списком начальных URL.

```python
async def run_crawler(self, initial_urls: list[str]):
    """
    Args:
        self: Экземпляр класса CrawleePython.
        initial_urls (list[str]): Список начальных URL для сбора данных.

    Returns:
        None
    """
```

#### `export_data`

**Описание**: Экспорт собранных данных в файл JSON.

```python
def export_data(self, data: list[dict], filename: str = 'data.json'):
    """
    Args:
        self: Экземпляр класса CrawleePython.
        data (list[dict]): Список словарей с собранными данными.
        filename (str, optional): Имя файла для экспорта данных. По умолчанию 'data.json'.

    Returns:
        None
    """
```

#### `get_data`

**Описание**: Возвращает собранные данные в формате словаря.

```python
def get_data(self) -> dict | None:
    """
    Args:
        self: Экземпляр класса CrawleePython.

    Returns:
        dict | None: Словарь с собранными данными или None, если данные не найдены.

    """
```

#### `run`

**Описание**: Главная функция для запуска процесса сбора данных.

```python
async def run(self, initial_urls: list[str]):
    """
    Args:
        self: Экземпляр класса CrawleePython.
        initial_urls (list[str]): Список начальных URL для сбора данных.

    Returns:
        None

    """
```

## Функции


## Примеры использования

```python
# Пример использования
async def main():
    crawler = CrawleePython(max_requests=10)
    await crawler.run(['https://news.ycombinator.com/'])

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```


```python
# Пример инициализации и запуска
async def main():
  try:
    crawler = CrawleePython(max_requests=50, headless=False)  # Запуск в режиме с GUI
    await crawler.run(['https://news.ycombinator.com/'])
  except Exception as ex:
    print(f"Произошла ошибка: {ex}")

if __name__ == "__main__":
  import asyncio
  asyncio.run(main())
```
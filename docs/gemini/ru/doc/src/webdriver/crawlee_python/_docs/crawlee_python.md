# Модуль `crawlee_python`

## Обзор

Данный модуль предоставляет класс `CrawleePython` для выполнения веб-скрапинга с использованием библиотеки `crawlee` и Playwright.  Класс позволяет настроить, запустить и экспортировать данные, собранные с веб-сайта, в формате JSON.

## Оглавление

* [Модуль `crawlee_python`](#модуль-crawlee-python)
* [Класс `CrawleePython`](#класс-crawleepython)
    * [Метод `__init__`](#метод-init)
    * [Метод `setup_crawler`](#метод-setup-crawler)
    * [Метод `run_crawler`](#метод-run-crawler)
    * [Метод `export_data`](#метод-export-data)
    * [Метод `get_data`](#метод-get-data)
    * [Метод `run`](#метод-run)
* [Пример использования](#пример-использования)


## Класс `CrawleePython`

### Описание

Класс `CrawleePython` реализует веб-скрапер, использующий Playwright для взаимодействия с веб-страницами. Он позволяет настроить параметры сканирования, собрать данные и экспортировать их в файл JSON.

### Метод `__init__`

```python
def __init__(self, max_requests: int, headless: bool = True, browser_type: str = 'chromium') -> None:
    """
    Args:
        max_requests (int): Максимальное количество запросов.
        headless (bool, optional): Режим работы браузера без графического интерфейса. По умолчанию True.
        browser_type (str, optional): Тип браузера. По умолчанию 'chromium'.

    Raises:
        TypeError: Если передан неверный тип данных для параметра.
        ValueError: Если передан неверный диапазон значений для параметра.
    """
```

### Метод `setup_crawler`

```python
def setup_crawler(self) -> None:
    """
    Настраивает сканер, определяя обработчик запросов по умолчанию.
    """
```

### Метод `run_crawler`

```python
async def run_crawler(self, initial_urls: list) -> None:
    """
    Запускает сканирование с заданными начальными URL.

    Args:
        initial_urls (list): Список начальных URL для сканирования.
    """
```

### Метод `export_data`

```python
def export_data(self, data: list, filename: str) -> None:
    """
    Экспортирует собранные данные в файл JSON.

    Args:
        data (list): Список словарей с собранными данными.
        filename (str): Имя файла для экспорта.
    """
```

### Метод `get_data`

```python
def get_data(self) -> dict:
    """
    Возвращает собранные данные в виде словаря.

    Returns:
        dict: Словарь с собранными данными.
        None: Если данные не были собраны.
    """
```

### Метод `run`

```python
async def run(self, initial_urls: list, filename: str = 'data.json') -> None:
    """
    Осуществляет полный цикл сканирования: настройку сканера, сканирование, экспорт данных и вывод результатов.

    Args:
        initial_urls (list): Список начальных URL для сканирования.
        filename (str, optional): Имя файла для экспорта данных. По умолчанию 'data.json'.
    """
```

## Пример использования

```python
import asyncio
from crawlee_python import CrawleePython

async def main():
    crawler = CrawleePython(max_requests=10, headless=False, browser_type='firefox')
    await crawler.run(['https://news.ycombinator.com/'], 'hn_data.json')

if __name__ == "__main__":
    asyncio.run(main())
```

Этот пример запускает сканер на Hacker News с параметрами по умолчанию и сохраняет результат в `hn_data.json`.  Обратите внимание, что для корректной работы необходима установка Playwright и других необходимых зависимостей.
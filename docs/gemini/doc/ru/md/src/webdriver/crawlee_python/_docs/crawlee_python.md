# Модуль `crawlee_python`

## Обзор

Данный модуль предоставляет класс `CrawleePython` для веб-скрейпинга с использованием библиотеки `crawlee` и Playwright. Класс позволяет настроить и запустить веб-скрейпинг, извлечь данные с веб-страниц и экспортировать собранные данные в файл JSON.

## Классы

### `CrawleePython`

**Описание**: Класс для выполнения веб-скрейпинга с использованием PlaywrightCrawler.

**Методы**:

#### `__init__(max_requests: int, headless: bool = True, browser_type: str = 'chromium')`

**Описание**: Инициализирует экземпляр класса.

**Параметры**:

- `max_requests` (int): Максимальное количество запросов.
- `headless` (bool, по умолчанию True): Флаг, определяющий работу браузера в бескомпромиссном режиме (без графического интерфейса).
- `browser_type` (str, по умолчанию 'chromium'): Тип браузера (например, 'chromium', 'firefox').

**Возвращает**:
- `None`

#### `setup_crawler()`

**Описание**: Настраивает скрейпер. Определяет обработчик запросов по умолчанию.

**Параметры**:
- Нет

**Возвращает**:
- `None`

#### `run_crawler(initial_urls: list[str])`

**Описание**: Запускает процесс скрейпинга с заданными начальными URL.

**Параметры**:
- `initial_urls` (list[str]): Список начальных URL для скрейпинга.

**Возвращает**:
- `None`

#### `export_data(file_path: str)`

**Описание**: Экспортирует собранные данные в файл JSON.

**Параметры**:
- `file_path` (str): Путь к файлу для экспорта данных.

**Возвращает**:
- `None`

#### `get_data()`

**Описание**: Возвращает извлеченные данные в виде словаря.

**Параметры**:
- Нет

**Возвращает**:
- `dict`: Словарь извлеченных данных.

#### `run()`

**Описание**: Метод для запуска всего процесса скрейпинга.

**Параметры**:
- Нет

**Возвращает**:
- `None`


## Функции

### `main()`

**Описание**: Главная асинхронная функция для запуска скрейпинга.


**Параметры**:
- Нет

**Возвращает**:
- `None`

## Пример использования

```python
# Пример использования класса CrawleePython
import asyncio
from crawlee_python import CrawleePython

async def main():
    crawler = CrawleePython(max_requests=10, headless=False, browser_type='chromium')
    await crawler.setup_crawler()
    await crawler.run_crawler(['https://news.ycombinator.com/'])
    crawler.export_data('data.json')
    data = crawler.get_data()
    print(data)

asyncio.run(main())
```
```
```
```
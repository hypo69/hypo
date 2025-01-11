# CrawleePython

## Обзор

Этот модуль определяет класс `CrawleePython`, который использует `PlaywrightCrawler` из библиотеки `crawlee` для выполнения веб-скрейпинга. Класс предоставляет методы для настройки, запуска, экспорта и получения извлеченных данных.

## Оглавление

- [Классы](#классы)
    - [`CrawleePython`](#crawleepython)
- [Функции](#функции)
    - [`main`](#main)

## Классы

### `CrawleePython`

**Описание**: Класс для выполнения веб-скрейпинга с использованием `PlaywrightCrawler`.

**Методы**:
- [`__init__`](#__init__)
- [`setup_crawler`](#setup_crawler)
- [`run_crawler`](#run_crawler)
- [`export_data`](#export_data)
- [`get_data`](#get_data)
- [`run`](#run)

#### `__init__`

```python
def __init__(self, max_requests: int = 10, headless: bool = True, browser_type: str = 'chromium') -> None:
```

**Описание**: Инициализирует объект `CrawleePython` с параметрами для настройки `PlaywrightCrawler`.

**Параметры**:
- `max_requests` (int, optional): Максимальное количество запросов для выполнения. По умолчанию `10`.
- `headless` (bool, optional): Запускать ли браузер в headless режиме. По умолчанию `True`.
- `browser_type` (str, optional): Тип браузера ('chromium', 'firefox', 'webkit'). По умолчанию `'chromium'`.

**Возвращает**:
- `None`: Функция ничего не возвращает.

#### `setup_crawler`

```python
def setup_crawler(self) -> None:
```

**Описание**: Настраивает crawler, определяя обработчик запросов по умолчанию.

**Параметры**:
- `self`: Ссылка на текущий экземпляр класса.

**Возвращает**:
- `None`: Функция ничего не возвращает.

#### `run_crawler`

```python
async def run_crawler(self, start_urls: list[str]) -> None:
```

**Описание**: Запускает процесс обхода страниц с заданными начальными URL.

**Параметры**:
- `start_urls` (list[str]): Список начальных URL для обхода.
- `self`: Ссылка на текущий экземпляр класса.

**Возвращает**:
- `None`: Функция ничего не возвращает.

#### `export_data`

```python
def export_data(self, filepath: str = 'output.json') -> None:
```

**Описание**: Экспортирует собранные данные в JSON-файл.

**Параметры**:
- `filepath` (str, optional): Путь к файлу для сохранения данных. По умолчанию `'output.json'`.
- `self`: Ссылка на текущий экземпляр класса.

**Возвращает**:
- `None`: Функция ничего не возвращает.

#### `get_data`

```python
def get_data(self) -> dict:
```

**Описание**: Возвращает собранные данные в виде словаря.

**Параметры**:
- `self`: Ссылка на текущий экземпляр класса.

**Возвращает**:
- `dict`: Словарь с собранными данными.

#### `run`

```python
async def run(self, start_urls: list[str], filepath: str = 'output.json') -> None:
```

**Описание**: Оркестрирует весь процесс: настройку, запуск crawler, экспорт данных и вывод собранных данных.

**Параметры**:
- `start_urls` (list[str]): Список начальных URL для обхода.
- `filepath` (str, optional): Путь к файлу для сохранения данных. По умолчанию `'output.json'`.
- `self`: Ссылка на текущий экземпляр класса.

**Возвращает**:
- `None`: Функция ничего не возвращает.

## Функции

### `main`

```python
async def main() -> None:
```

**Описание**: Главная функция для запуска примера использования класса `CrawleePython`.

**Параметры**:
- Нет параметров.

**Возвращает**:
- `None`: Функция ничего не возвращает.
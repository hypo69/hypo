# Модуль crawlee_python

## Обзор

Этот модуль предоставляет класс `CrawleePython` для выполнения веб-скрапинга с использованием библиотеки `crawlee` и Playwright.  Класс позволяет настроить, запустить и экспортировать данные, полученные с веб-страниц.

## Классы

### `CrawleePython`

**Описание**: Класс `CrawleePython` реализует веб-скрапер, основанный на PlaywrightCrawler. Он предоставляет методы для настройки, запуска, экспорта и получения данных.

**Методы**:

#### `__init__(self, max_requests: int, headless: bool = True, browser_type: str = 'chromium')`

**Описание**: Конструктор класса. Инициализирует объект `PlaywrightCrawler` с заданными параметрами.

**Параметры**:

- `max_requests` (int): Максимальное количество запросов для выполнения.
- `headless` (bool, по умолчанию True): Флаг для запуска браузера в бескладовом режиме.
- `browser_type` (str, по умолчанию 'chromium'): Тип браузера для использования.

#### `setup_crawler(self)`

**Описание**: Настраивает `PlaywrightCrawler` для обработки запросов и извлечения данных.

**Возвращает**:

- `None`

#### `run_crawler(self, initial_urls: list)`

**Описание**: Запускает процесс скрапинга с заданными начальными URL.

**Параметры**:

- `initial_urls` (list): Список начальных URL для запуска скрапинга.

**Возвращает**:

- `None`

#### `export_data(self, filename: str = 'data.json')`

**Описание**: Экспортирует собранные данные в JSON-файл.

**Параметры**:

- `filename` (str, по умолчанию 'data.json'): Имя файла для экспорта данных.

**Возвращает**:

- `None`

#### `get_data(self) -> dict`

**Описание**: Возвращает собранные данные в виде словаря.

**Возвращает**:

- `dict`: Словарь с данными.


#### `run(self, initial_urls: list)`

**Описание**: Основной метод для запуска скрапинга. Настраивает, запускает и экспортирует данные.

**Параметры**:

- `initial_urls` (list): Список начальных URL для запуска скрапинга.

**Возвращает**:

- `None`


## Функции

###  `main()`

**Описание**: Основная функция для запуска процесса скрапинга.

**Возвращает**:

- `None`
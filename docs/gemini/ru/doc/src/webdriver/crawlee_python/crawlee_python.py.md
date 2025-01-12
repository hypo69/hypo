# Модуль `crawlee_python`

## Обзор

Модуль `crawlee_python` представляет собой пользовательскую реализацию `PlaywrightCrawler` с использованием библиотеки Crawlee. Он позволяет настраивать параметры браузера, обрабатывать запросы и извлекать данные из веб-страниц.

## Оглавление
- [Классы](#классы)
    - [`CrawleePython`](#crawleepython)
- [Пример использования](#пример-использования)

## Классы

### `CrawleePython`

**Описание**:
Пользовательская реализация `PlaywrightCrawler` с использованием библиотеки Crawlee.

**Атрибуты**:
- `max_requests` (int): Максимальное количество запросов для выполнения во время обхода.
- `headless` (bool): Определяет, будет ли браузер работать в режиме без интерфейса.
- `browser_type` (str): Тип используемого браузера ('chromium', 'firefox', 'webkit').
- `crawler` (PlaywrightCrawler): Экземпляр PlaywrightCrawler.

#### `__init__`
```python
def __init__(self, max_requests: int = 5, headless: bool = False, browser_type: str = 'firefox', options: Optional[List[str]] = None)
```
**Описание**:
Инициализирует краулер CrawleePython с заданными параметрами.

**Параметры**:
- `max_requests` (int): Максимальное количество запросов для выполнения во время обхода.
- `headless` (bool): Определяет, будет ли браузер работать в режиме без интерфейса.
- `browser_type` (str): Тип используемого браузера ('chromium', 'firefox', 'webkit').
- `options` (Optional[List[str]], optional): Список пользовательских опций, передаваемых браузеру. По умолчанию `None`.

#### `setup_crawler`
```python
async def setup_crawler(self)
```
**Описание**:
Настраивает экземпляр PlaywrightCrawler с указанной конфигурацией.

#### `run_crawler`
```python
async def run_crawler(self, urls: List[str])
```
**Описание**:
Запускает краулер с начальным списком URL-адресов.

**Параметры**:
- `urls` (List[str]): Список URL-адресов для начала обхода.

#### `export_data`
```python
async def export_data(self, file_path: str)
```
**Описание**:
Экспортирует весь набор данных в файл JSON.

**Параметры**:
- `file_path` (str): Путь для сохранения экспортированного файла JSON.

#### `get_data`
```python
async def get_data(self) -> Dict[str, Any]
```
**Описание**:
Извлекает полученные данные.

**Возвращает**:
- `Dict[str, Any]`: Извлеченные данные в виде словаря.

#### `run`
```python
async def run(self, urls: List[str])
```
**Описание**:
Основной метод для настройки, запуска краулера и экспорта данных.

**Параметры**:
- `urls` (List[str]): Список URL-адресов для начала обхода.

## Пример использования

```python
if __name__ == "__main__":
    async def main():
        crawler = CrawleePython(max_requests=5, headless=False, browser_type='firefox', options=["--headless"])
        await crawler.run(['https://www.example.com'])

    asyncio.run(main())
```
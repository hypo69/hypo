# Модуль scenario

## Обзор

Модуль `scenario.py` предназначен для реализации сценария сбора информации о товарах с различных веб-сайтов, их обработки с использованием AI-моделей для перевода и анализа, а также формирования отчетов. Модуль содержит класс `Scenario`, который управляет всем процессом, начиная от сбора данных до генерации отчетов на разных языках.

## Подробней

Этот модуль является ключевым компонентом системы, отвечающим за автоматизированный сбор данных о товарах, их анализ и подготовку отчетов. Он использует различные инструменты, такие как `BeautifulSoup` для парсинга HTML, `requests` для выполнения HTTP-запросов, и AI-модели (`Google Gemini`) для обработки и перевода данных.

Модуль предназначен для работы в асинхронном режиме, что позволяет эффективно обрабатывать большое количество запросов и данных. Основные этапы работы модуля включают:

1.  Сбор данных о товарах с использованием граберов для различных поставщиков.
2.  AI-обработку собранных данных для перевода и анализа.
3.  Генерацию отчетов на основе обработанных данных.

## Классы

### `Scenario`

**Описание**:
Класс `Scenario` является исполнителем основного сценария сбора и обработки информации о товарах. Он наследуется от класса `QuotationBuilder` и управляет всеми этапами процесса, включая сбор данных, AI-обработку и генерацию отчетов.

**Методы**:

*   `__init__`: Инициализирует экземпляр класса `Scenario`, настраивает драйвер браузера и вызывает конструктор родительского класса `QuotationBuilder`.
*   `run_scenario_async`: Асинхронно выполняет основной сценарий: собирает информацию о товарах, обрабатывает ее с помощью AI, сохраняет данные и генерирует отчеты.

**Параметры**:

*   `mexiron_name` (Optional[str], optional): Имя Mexiron. По умолчанию `gs.now`.
*   `driver` (Optional[Firefox | Playwrid | str], optional): Драйвер браузера для управления браузером. По умолчанию `None`.
*   `**kwards`: Дополнительные параметры конфигурации.

**Примеры**

```python
s = Scenario(window_mode = 'headless')
asyncio.run(s.run_scenario_async(urls = urls_list, mexiron_name = 'test price quotation', ))
```

## Функции

### `fetch_target_urls_onetab`

```python
def fetch_target_urls_onetab(one_tab_url: str) -> tuple[str, str, list[str]] | bool:
    """
    Args:
        one_tab_url (str): URL OneTab для парсинга.

    Returns:
        tuple[str, str, list[str]] | bool: Кортеж, содержащий цену, имя Mexiron и список URL.

    Raises:
        requests.exceptions.RequestException: При ошибке выполнения HTTP-запроса.

    Example:
        fetch_target_urls_onetab('https://www.one-tab.com/...')
    """
```

**Описание**:
Функция `fetch_target_urls_onetab` извлекает целевые URL из OneTab URL, анализируя HTML-контент страницы.

**Параметры**:

*   `one_tab_url` (str): URL OneTab для парсинга.

**Возвращает**:

*   `tuple[str, str, list[str]] | bool`: Кортеж, содержащий цену, имя Mexiron и список URL, или `False` в случае ошибки.

**Вызывает исключения**:

*   `requests.exceptions.RequestException`: Возникает при ошибке выполнения HTTP-запроса.

**Примеры**:

```python
price, mexiron_name, urls = fetch_target_urls_onetab('https://www.one-tab.com/...')
if price and mexiron_name and urls:
    print(f"Price: {price}, Name: {mexiron_name}, URLs: {urls}")
```

### `run_sample_scenario`

```python
def run_sample_scenario():
    """"""
    ...
```

**Описание**:
Функция `run_sample_scenario` запускает пример сценария сбора данных о товарах.

**Параметры**:
# нет параметров

**Возвращает**:
# нет возвращаемого значения

**Вызывает исключения**:
# нет исключений

**Примеры**:

```python
run_sample_scenario()
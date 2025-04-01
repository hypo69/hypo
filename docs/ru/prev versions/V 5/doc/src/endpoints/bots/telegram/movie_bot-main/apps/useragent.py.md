# Модуль useragent

## Обзор

Модуль `useragent.py` предназначен для предоставления случайного User-Agent из списка. Это полезно для маскировки запросов к веб-сайтам, чтобы избежать блокировки или ограничения доступа. Он содержит функцию `get_useragent`, которая возвращает случайно выбранный User-Agent из предопределенного списка.

## Подробней

Этот модуль используется для эмуляции различных браузеров при выполнении HTTP-запросов. Это может быть полезно для обхода ограничений, установленных на стороне сервера, или для сбора данных с веб-сайтов, которые предоставляют разный контент в зависимости от User-Agent. Список User-Agent хранится в переменной `_useragent_list`.

## Функции

### `get_useragent`

```python
def get_useragent() -> str:
    """
    Args:
        None

    Returns:
        str: Случайно выбранный User-Agent из списка.

    Raises:
        None

    Example:
        >>> get_useragent()
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
    """
```

**Как работает функция**:

Функция `get_useragent` использует модуль `random` для случайного выбора User-Agent из списка `_useragent_list`. Она возвращает выбранный User-Agent в виде строки.

**Параметры**:

- Функция не принимает параметров.

**Возвращает**:

- `str`: Случайно выбранный User-Agent из списка `_useragent_list`.

**Вызывает исключения**:

- Функция не вызывает исключений.

**Примеры**:

```python
>>> get_useragent()
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
```

## Переменные

### `_useragent_list`

**Описание**:

`_useragent_list` - это список строк, содержащий различные User-Agent.

**Как работает переменная**:

`_useragent_list` содержит список User-Agent, которые используются функцией `get_useragent` для случайного выбора.

**Примеры**:

```python
_useragent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0'
]
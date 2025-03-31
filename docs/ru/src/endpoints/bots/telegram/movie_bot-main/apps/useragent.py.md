# Модуль для получения случайного User-Agent

## Обзор

Модуль содержит функцию `get_useragent`, которая возвращает случайный User-Agent из предопределенного списка. Это полезно для имитации запросов от различных браузеров и операционных систем, что может быть необходимо для обхода ограничений или сбора данных.

## Подробней

Данный модуль используется для предоставления случайного User-Agent. User-Agent — это строка, которую браузер отправляет на сервер для идентификации. Использование случайного User-Agent может помочь в следующих сценариях:

-   Обход ограничений на основе User-Agent.
-   Имитация различных браузеров и операционных систем при тестировании веб-сайтов.
-   Сбор данных из веб-сайтов, которые могут блокировать запросы с определенными User-Agent.

## Функции

### `get_useragent`

```python
def get_useragent() -> str:
    """
    Возвращает случайный User-Agent из списка.

    Args:
        Нет

    Returns:
        str: Случайный User-Agent из списка `_useragent_list`.

    Raises:
        Нет

    Example:
        >>> get_useragent()
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
    """
    ...
```

**Как работает функция**:

1.  Функция `get_useragent` использует модуль `random` для выбора случайного элемента из списка `_useragent_list`.
2.  Выбранный User-Agent возвращается в виде строки.

**Параметры**:

-   Нет

**Возвращает**:

-   `str`: Случайный User-Agent из списка.

**Вызывает исключения**:

-   Нет

### `_useragent_list`

**Описание**:

Список `_useragent_list` содержит набор строк User-Agent, которые могут быть использованы для имитации запросов от различных браузеров и операционных систем.

**Как работает**:

Список `_useragent_list` представляет собой статический список, содержащий различные User-Agent строки.  Функция `get_useragent` выбирает случайный элемент из этого списка.

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
```
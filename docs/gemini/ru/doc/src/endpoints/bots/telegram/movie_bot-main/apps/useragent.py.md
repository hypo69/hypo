# Модуль useragent

## Обзор

Модуль `useragent.py` предназначен для предоставления случайных User-Agent строк из предопределенного списка. Это полезно для имитации запросов от различных браузеров, что может быть необходимо для обхода ограничений или маскировки ботов.

## Подробней

В проекте `hypotez` данный модуль используется для выбора случайного User-Agent из списка `_useragent_list`. Это может быть полезно в скриптах, которые выполняют запросы к веб-сайтам, чтобы выглядеть как обычные пользователи и избежать блокировки. Выбор случайного User-Agent помогает имитировать разнообразие браузеров и операционных систем, с которых поступают запросы.

## Функции

### `get_useragent`

```python
def get_useragent() -> str:
    """
    Args:
        None

    Returns:
        str: Случайная строка User-Agent из списка `_useragent_list`.

    Raises:
        None

    Example:
        >>> get_useragent()
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
    """
```

**Описание**: Возвращает случайную строку User-Agent из списка `_useragent_list`.

**Параметры**:
- Нет параметров.

**Возвращает**:
- `str`: Случайная строка User-Agent.

**Примеры**:

```python
>>> get_useragent()
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
```
```python
>>> get_useragent()
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
```
```python
>>> get_useragent()
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
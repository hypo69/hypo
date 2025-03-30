# Модуль useragent

## Обзор

Модуль `useragent` предназначен для предоставления случайных User-Agent строк из предопределенного списка. Это полезно для имитации запросов от различных браузеров и операционных систем, что может быть необходимо при работе с веб-сервисами, требующими определенные User-Agent. Модуль содержит функцию `get_useragent`, которая возвращает случайно выбранный User-Agent из списка `_useragent_list`.

## Подробней

В контексте проекта `hypotez`, данный модуль может быть использован в компонентах, взаимодействующих с внешними веб-сервисами, чтобы избежать блокировки или ограничений, основанных на User-Agent. Он обеспечивает простой способ ротации User-Agent строк, делая запросы более похожими на запросы от реальных пользователей.

## Функции

### `get_useragent`

```python
def get_useragent() -> str:
    """
    Args:
        None

    Returns:
        str: Случайно выбранная строка User-Agent из списка `_useragent_list`.
    
    Raises:
        None

    Example:
        >>> get_useragent()
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
    """
```

**Описание**: Возвращает случайно выбранную строку User-Agent из списка `_useragent_list`.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `str`: Случайно выбранная строка User-Agent.

**Примеры**:
```python
get_useragent()
```

### `_useragent_list`

**Описание**: Список строк User-Agent, из которого случайным образом выбираются значения функцией `get_useragent`.

**Тип**: `list[str]`

**Пример использования**:
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
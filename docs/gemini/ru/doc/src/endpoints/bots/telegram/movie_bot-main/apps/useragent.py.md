# Модуль для работы с User-Agent
=================================================

Модуль содержит функцию :func:`get_useragent`, которая предоставляет случайный User-Agent из списка.
Данный модуль предназначен для использования в Telegram Movie Bot.

## Обзор

Модуль `useragent.py` предназначен для предоставления случайного User-Agent из списка. Это полезно для маскировки запросов, отправляемых ботом, чтобы избежать блокировки или ограничений со стороны веб-серверов.

## Подробнее

Этот модуль содержит функцию `get_useragent`, которая возвращает случайный User-Agent из предопределенного списка `_useragent_list`. Это позволяет боту представляться как различные браузеры и операционные системы, что может быть полезно для обхода ограничений или для тестирования веб-сайтов с разными User-Agent.

## Функции

### `get_useragent`

```python
def get_useragent() -> str:
    """
    Возвращает случайный User-Agent из списка.

    Returns:
        str: Случайный User-Agent.
    """
```

**Назначение**: Функция возвращает случайный User-Agent из списка `_useragent_list`.

**Параметры**:
- Нет параметров.

**Возвращает**:
- `str`: Случайный User-Agent.

**Вызывает исключения**:
- Не вызывает исключений.

**Как работает функция**:
1. Функция использует `random.choice` для случайного выбора элемента из списка `_useragent_list`.
2. Возвращает выбранный User-Agent.

```ascii
Начало --> Выбор случайного User-Agent из _useragent_list --> Возврат User-Agent
```

**Примеры**:

```python
import random
def get_useragent() -> str:
    """
    Возвращает случайный User-Agent из списка.

    Returns:
        str: Случайный User-Agent.
    """
    return random.choice(_useragent_list)

_useragent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0'
]
user_agent = get_useragent()
print(user_agent)  # Вывод: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0 (пример)
```

### `_useragent_list`

- **Описание**: Список User-Agent строк, из которых случайным образом выбирается один для возврата функцией `get_useragent`.
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
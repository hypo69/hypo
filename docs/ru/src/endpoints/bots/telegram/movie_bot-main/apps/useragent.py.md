# Модуль для работы с User-Agent
=================================================

Модуль содержит функцию :func:`get_useragent`, которая возвращает случайный User-Agent из списка.
Этот список хранится в переменной `_useragent_list`.

## Обзор

Модуль предназначен для предоставления случайных User-Agent строк для использования в запросах к веб-серверам. 
Это может быть полезно для маскировки ботов или автоматизированных скриптов, чтобы они выглядели как обычные пользователи.
Данный код используется в проекте для эмуляции различных пользовательских агентов при выполнении HTTP-запросов. Это позволяет избежать блокировки со стороны серверов, которые могут идентифицировать и блокировать запросы, исходящие от ботов с одинаковым User-Agent.

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

**Назначение**: Возвращает случайную строку User-Agent из списка `_useragent_list`.

**Параметры**: Отсутствуют.

**Возвращает**:
- `str`: Случайный User-Agent.

**Как работает функция**:
1. Функция `get_useragent` использует модуль `random` для выбора случайного элемента из списка `_useragent_list`.
2. Выбранный элемент (строка User-Agent) возвращается в качестве результата.

```
    Начало
      ↓
  Выбор случайного User-Agent
      ↓
    Возврат User-Agent
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
print(user_agent)
# => 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0' (пример)

user_agent = get_useragent()
print(user_agent)
# => 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36' (пример)
```

## Переменные

### `_useragent_list`

- **Описание**: Список строк User-Agent, из которых выбирается случайный User-Agent функцией `get_useragent`.
- **Тип**: `list` of `str`
- **Назначение**: Хранит набор User-Agent строк для случайного выбора.
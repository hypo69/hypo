# Модуль для работы с User-Agent
## Обзор

Модуль предоставляет функциональность для получения случайного User-Agent из предопределенного списка.
Он содержит функцию `get_useragent`, которая возвращает случайно выбранный User-Agent из списка `_useragent_list`.

## Подробней

Данный модуль используется для имитации запросов от различных браузеров, что может быть полезно для обхода ограничений или сбора данных с веб-сайтов. Модуль содержит список наиболее часто используемых User-Agent. Этот модуль особенно полезен для задач, требующих маскировки User-Agent.

## Функции

### `get_useragent`

```python
def get_useragent() -> str:
    """
    Возвращает случайно выбранный User-Agent из списка.

    Returns:
        str: Случайно выбранный User-Agent.

    Как работает функция:
    1. Функция использует `random.choice` для случайного выбора одного элемента из списка `_useragent_list`.
    2. Возвращает выбранный элемент.

    Внутри функции происходят следующие действия и преобразования:
     A
     |
     -- B
     
     Где:
     A - Выбор случайного User-Agent из списка.
     B - Возврат выбранного User-Agent.
    """
```
### `_useragent_list`
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
**Описание**: Список User-Agent, используемых для случайного выбора.
```
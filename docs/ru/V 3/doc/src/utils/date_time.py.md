# Модуль `date_time`

## Обзор

Модуль `date_time` предоставляет функциональность для проверки, находится ли текущее время в заданном интервале, с возможностью использования таймаута. Он содержит класс `TimeoutCheck`, который позволяет определять, попадает ли текущее время в заданный временной промежуток, что полезно для выполнения операций, которые должны происходить только в определенные периоды времени (например, ночное обслуживание).

## Подробней

Этот модуль содержит класс `TimeoutCheck`, который включает методы для проверки интервала времени и ожидания ввода с таймаутом. Основное назначение модуля - предоставить инструменты для управления выполнением задач в зависимости от времени суток и обеспечить возможность прерывания ожидания ввода пользователя по таймауту.

## Классы

### `TimeoutCheck`

**Описание**: Класс для проверки, находится ли текущее время в заданном интервале, с возможностью использования таймаута.

**Методы**:
- `__init__`: Конструктор класса `TimeoutCheck`.
- `interval`: Проверяет, находится ли текущее время в заданном интервале.
- `interval_with_timeout`: Проверяет, находится ли текущее время в заданном интервале с таймаутом.
- `get_input`: Запрашивает ввод от пользователя.
- `input_with_timeout`: Ожидает ввод с таймаутом.

**Параметры**:
- `result` (bool): Результат проверки интервала времени.
- `user_input` (str | None): Введенные пользователем данные.

**Примеры**:

```python
timeout_check = TimeoutCheck()
if timeout_check.interval_with_timeout(timeout=5):
    print("Current time is within the interval.")
else:
    print("Current time is outside the interval or timeout occurred.")
```

## Функции

### `interval`

```python
def interval(self, start: time = time(23, 0), end: time = time(6, 0)) -> bool:
    """ Check if the current time is within the specified interval.
    
    Args:
        start (time): Start of the interval (default is 23:00).
        end (time): End of the interval (default is 06:00).

    Returns:
        bool: True if the current time is within the interval, False otherwise.
    """
```

**Описание**: Проверяет, находится ли текущее время в заданном интервале.

**Параметры**:
- `start` (time): Начало интервала (по умолчанию 23:00).
- `end` (time): Конец интервала (по умолчанию 06:00).

**Возвращает**:
- `bool`: `True`, если текущее время находится в интервале, `False` в противном случае.

**Примеры**:

```python
from datetime import time
timeout_check = TimeoutCheck()
if timeout_check.interval(start=time(22, 0), end=time(7, 0)):
    print("Current time is within the interval.")
else:
    print("Current time is outside the interval.")
```

### `interval_with_timeout`

```python
def interval_with_timeout(self, timeout: int = 5, start: time = time(23, 0), end: time = time(6, 0)) -> bool:
    """ Check if the current time is within the specified interval with a timeout.

    Args:
        timeout (int): Time in seconds to wait for the interval check.
        start (time): Start of the interval (default is 23:00).
        end (time): End of the interval (default is 06:00).

    Returns:
        bool: True if the current time is within the interval and response within timeout, False if not or timeout occurs.
    """
```

**Описание**: Проверяет, находится ли текущее время в заданном интервале с таймаутом.

**Параметры**:
- `timeout` (int): Время в секундах для ожидания проверки интервала.
- `start` (time): Начало интервала (по умолчанию 23:00).
- `end` (time): Конец интервала (по умолчанию 06:00).

**Возвращает**:
- `bool`: `True`, если текущее время находится в интервале и ответ получен в течение таймаута, `False`, если нет или произошел таймаут.

**Примеры**:

```python
from datetime import time
timeout_check = TimeoutCheck()
if timeout_check.interval_with_timeout(timeout=10, start=time(22, 0), end=time(7, 0)):
    print("Current time is within the interval and response within timeout.")
else:
    print("Current time is outside the interval or timeout occurred.")
```

### `get_input`

```python
def get_input(self):
    """ Запрашиваем ввод от пользователя."""
```

**Описание**: Запрашивает ввод от пользователя.

**Примеры**:

```python
timeout_check = TimeoutCheck()
timeout_check.get_input()
print(f"User input: {timeout_check.user_input}")
```

### `input_with_timeout`

```python
def input_with_timeout(self, timeout: int = 5) -> str | None:
    """ Ожидаем ввод с тайм-аутом.

    Args:
        timeout (int): Время ожидания ввода в секундах.

    Returns:
        str | None: Введенные данные или None, если был тайм-аут.
    """
```

**Описание**: Ожидает ввод от пользователя с таймаутом.

**Параметры**:
- `timeout` (int): Время ожидания ввода в секундах.

**Возвращает**:
- `str | None`: Введенные данные или `None`, если произошел таймаут.

**Примеры**:

```python
timeout_check = TimeoutCheck()
user_input = timeout_check.input_with_timeout(timeout=3)
if user_input:
    print(f"User input: {user_input}")
else:
    print("Timeout occurred while waiting for user input.")
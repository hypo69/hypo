# Модуль `date_time`

## Обзор

Модуль `date_time` предоставляет класс `TimeoutCheck` с функциями для проверки, находится ли текущее время в заданном интервале, с возможностью установки таймаута. Это может быть полезно для выполнения задач, которые должны выполняться только в определенные периоды времени (например, ночное обслуживание).

## Подробней

Модуль содержит класс `TimeoutCheck`, который включает методы для проверки временных интервалов и ожидания ввода пользователя с использованием многопоточности и таймаутов. Это позволяет выполнять операции, чувствительные к времени, и предотвращать блокировку программы при ожидании ввода.

## Классы

### `TimeoutCheck`

**Описание**: Класс для проверки временных интервалов и ожидания ввода с таймаутом.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `TimeoutCheck`.
- `interval`: Проверяет, находится ли текущее время в заданном интервале.
- `interval_with_timeout`: Проверяет, находится ли текущее время в заданном интервале с таймаутом.
- `get_input`: Запрашивает ввод от пользователя.
- `input_with_timeout`: Ожидает ввод от пользователя с таймаутом.

**Параметры**:
- `result` (bool | None): Результат проверки временного интервала.
- `user_input` (str | None): Ввод пользователя.

**Примеры**
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
- `start` (time, optional): Время начала интервала. По умолчанию `time(23, 0)`.
- `end` (time, optional): Время окончания интервала. По умолчанию `time(6, 0)`.

**Возвращает**:
- `bool`: `True`, если текущее время находится в интервале, `False` в противном случае.

**Примеры**:
```python
from datetime import time
timeout_check = TimeoutCheck()
start_time = time(22, 0)
end_time = time(7, 0)
is_within_interval = timeout_check.interval(start=start_time, end=end_time)
print(f"Current time is within the interval: {is_within_interval}")
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
- `timeout` (int, optional): Время ожидания в секундах для проверки интервала. По умолчанию `5`.
- `start` (time, optional): Время начала интервала. По умолчанию `time(23, 0)`.
- `end` (time, optional): Время окончания интервала. По умолчанию `time(6, 0)`.

**Возвращает**:
- `bool`: `True`, если текущее время находится в интервале и ответ получен в течение таймаута, `False` в противном случае.

**Примеры**:
```python
from datetime import time
timeout_check = TimeoutCheck()
start_time = time(22, 0)
end_time = time(7, 0)
is_within_interval = timeout_check.interval_with_timeout(timeout=3, start=start_time, end=end_time)
print(f"Current time is within the interval: {is_within_interval}")
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
- `timeout` (int, optional): Время ожидания ввода в секундах. По умолчанию `5`.

**Возвращает**:
- `str | None`: Введенные данные или `None`, если произошел таймаут.

**Примеры**:
```python
timeout_check = TimeoutCheck()
user_input = timeout_check.input_with_timeout(timeout=3)
if user_input:
    print(f"User input: {user_input}")
else:
    print("Timeout occurred, no input received.")
# Модуль `date_time`

## Обзор

Модуль `date_time` предоставляет функциональность для проверки, находится ли текущее время в заданном интервале, с возможностью установки таймаута. Он содержит класс `TimeoutCheck`, который позволяет определить, попадает ли текущее время в указанный временной промежуток. Это полезно для выполнения операций, которые должны происходить только в определенные периоды времени (например, ночное обслуживание). Временной интервал по умолчанию - с 23:00 до 06:00, и функция может обрабатывать интервалы, охватывающие полночь.

## Подробнее

Этот модуль содержит класс `TimeoutCheck`, предназначенный для определения, находится ли текущее время в заданном интервале.  Класс предоставляет методы для проверки интервала с использованием потоков, что позволяет избежать блокировки основного потока выполнения при ожидании ввода пользователя или при проверке временного интервала. Расположение файла: `hypotez/src/utils/date_time.py` указывает, что данный модуль является частью подсистемы `utils` в проекте `hypotez` и, вероятно, используется для задач, связанных с обработкой времени и планированием задач.

## Классы

### `TimeoutCheck`

**Описание**: Класс для проверки, находится ли текущее время в заданном интервале с возможностью установки таймаута.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `TimeoutCheck`.
- `interval`: Проверяет, находится ли текущее время в заданном интервале.
- `interval_with_timeout`: Проверяет, находится ли текущее время в заданном интервале с таймаутом.
- `get_input`: Запрашивает ввод от пользователя.
- `input_with_timeout`: Ожидает ввод от пользователя с таймаутом.

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
    ...
```

**Описание**: Проверяет, находится ли текущее время в заданном интервале.

**Параметры**:
- `start` (time): Начало интервала (по умолчанию 23:00).
- `end` (time): Конец интервала (по умолчанию 06:00).

**Возвращает**:
- `bool`: `True`, если текущее время находится в интервале, `False` в противном случае.

**Примеры**:
```python
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
    ...
```

**Описание**: Проверяет, находится ли текущее время в заданном интервале с таймаутом.

**Параметры**:
- `timeout` (int): Время ожидания проверки интервала в секундах.
- `start` (time): Начало интервала (по умолчанию 23:00).
- `end` (time): Конец интервала (по умолчанию 06:00).

**Возвращает**:
- `bool`: `True`, если текущее время находится в интервале и ответ получен в течение таймаута, `False`, если нет или произошел таймаут.

**Примеры**:
```python
timeout_check = TimeoutCheck()
if timeout_check.interval_with_timeout(timeout=10, start=time(22, 0), end=time(7, 0)):
    print("Current time is within the interval.")
else:
    print("Current time is outside the interval or timeout occurred.")
```

### `get_input`

```python
def get_input(self):
    """ Запрашиваем ввод от пользователя."""
    ...
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
    ...
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
    print("Timeout occurred, no input received.")
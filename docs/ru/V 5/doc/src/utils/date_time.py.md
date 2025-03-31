# Модуль `date_time`

## Обзор

Модуль `date_time` предоставляет функциональность для проверки, находится ли текущее время в заданном интервале, с возможностью установки таймаута. Он включает класс `TimeoutCheck`, который позволяет определять, попадает ли текущее время в указанный временной промежуток, что полезно для выполнения операций, которые должны происходить только в определенные периоды времени (например, ночное обслуживание).

## Подробней

Этот модуль содержит класс `TimeoutCheck`, который включает методы для проверки, находится ли текущее время в заданном интервале, и для ожидания ввода пользователя с таймаутом. Класс использует модуль `threading` для реализации таймаутов.

## Классы

### `TimeoutCheck`

**Описание**: Класс для проверки, находится ли текущее время в заданном интервале с возможностью установки таймаута.

**Как работает класс**: Класс `TimeoutCheck` инициализируется с атрибутом `result`, который используется для хранения результата проверки интервала времени. Методы `interval` и `interval_with_timeout` позволяют проверять, находится ли текущее время в заданном интервале, с возможностью установки таймаута.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `TimeoutCheck` с атрибутом `result`, установленным в `None`.
- `interval`: Проверяет, находится ли текущее время в заданном интервале.
- `interval_with_timeout`: Проверяет, находится ли текущее время в заданном интервале с таймаутом.
- `get_input`: Запрашивает ввод от пользователя.
- `input_with_timeout`: Ожидает ввод от пользователя с таймаутом.

### `TimeoutCheck.__init__`

**Описание**: Инициализирует экземпляр класса `TimeoutCheck`.

**Параметры**:
- Нет параметров.

**Примеры**:
```python
timeout_check = TimeoutCheck()
```

### `TimeoutCheck.interval`

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

**Как работает функция**: Функция получает текущее время и сравнивает его с заданным интервалом, определяемым параметрами `start` и `end`. Если интервал находится в пределах одного дня (например, с 08:00 до 17:00), функция проверяет, находится ли текущее время между `start` и `end`. Если интервал охватывает полночь (например, с 23:00 до 06:00), функция проверяет, больше ли текущее время, чем `start`, или меньше, чем `end`. Результат сохраняется в атрибуте `self.result`.

**Параметры**:
- `start` (time): Начало интервала (по умолчанию 23:00).
- `end` (time): Конец интервала (по умолчанию 06:00).

**Возвращает**:
- `bool`: `True`, если текущее время находится в интервале, `False` в противном случае.

**Примеры**:
```python
from datetime import time
timeout_check = TimeoutCheck()
if timeout_check.interval(start=time(8, 0), end=time(17, 0)):
    print("Current time is within the interval.")
else:
    print("Current time is outside the interval.")
```

### `TimeoutCheck.interval_with_timeout`

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

**Как работает функция**: Функция создает и запускает поток для выполнения проверки интервала с использованием метода `interval`. Поток ожидает завершения в течение заданного времени таймаута. Если поток завершается в течение таймаута, функция возвращает результат проверки. Если происходит таймаут, функция возвращает `False`.

**Параметры**:
- `timeout` (int): Время ожидания в секундах для проверки интервала (по умолчанию 5).
- `start` (time): Начало интервала (по умолчанию 23:00).
- `end` (time): Конец интервала (по умолчанию 06:00).

**Возвращает**:
- `bool`: `True`, если текущее время находится в интервале и ответ получен в течение таймаута, `False`, если нет или произошел таймаут.

**Примеры**:
```python
from datetime import time
timeout_check = TimeoutCheck()
if timeout_check.interval_with_timeout(timeout=5, start=time(8, 0), end=time(17, 0)):
    print("Current time is within the interval.")
else:
    print("Current time is outside the interval or timeout occurred.")
```

### `TimeoutCheck.get_input`

```python
def get_input(self):
    """ Запрашиваем ввод от пользователя."""
    ...
```

**Описание**: Запрашивает ввод от пользователя.

**Как работает функция**: Функция использует `input()` для запроса ввода от пользователя и сохраняет введенные данные в атрибуте `self.user_input`.

**Параметры**:
- Нет параметров.

**Примеры**:
```python
timeout_check = TimeoutCheck()
timeout_check.get_input()
print(f"User input: {timeout_check.user_input}")
```

### `TimeoutCheck.input_with_timeout`

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

**Как работает функция**: Функция создает и запускает поток для получения ввода от пользователя с использованием метода `get_input`. Поток ожидает завершения в течение заданного времени таймаута. Если поток завершается в течение таймаута, функция возвращает введенные данные. Если происходит таймаут, функция возвращает `None`.

**Параметры**:
- `timeout` (int): Время ожидания ввода в секундах (по умолчанию 5).

**Возвращает**:
- `str | None`: Введенные данные или `None`, если произошел таймаут.

**Примеры**:
```python
timeout_check = TimeoutCheck()
user_input = timeout_check.input_with_timeout(timeout=5)
if user_input:
    print(f"User input: {user_input}")
else:
    print("Timeout occurred.")
```

## Функции

В данном модуле нет отдельных функций, только методы класса `TimeoutCheck`.

```python
if __name__ == '__main__':
    # Example usage
    timeout_check = TimeoutCheck()
    
    # Check interval with a timeout of 5 seconds
    if timeout_check.interval_with_timeout(timeout=5):
        print("Current time is within the interval.")
    else:
        print("Current time is outside the interval or timeout occurred.")
```
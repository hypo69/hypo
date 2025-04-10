# Модуль для проверки времени и ожидания ввода с таймаутом
## Обзор

Модуль `date_time` предоставляет класс `TimeoutCheck`, который используется для проверки, находится ли текущее время в заданном интервале, с возможностью установки таймаута. Также предоставляет функциональность ожидания ввода от пользователя с таймаутом.

## Подробнее

Модуль содержит класс `TimeoutCheck`, который позволяет определять, попадает ли текущее время в заданный временной интервал. Это полезно для выполнения операций, которые должны происходить только в определенные периоды времени (например, ночное обслуживание). Интервал времени по умолчанию - с 23:00 до 06:00, и функция может обрабатывать интервалы, охватывающие полночь.

Кроме того, модуль предоставляет функциональность ожидания ответа с таймаутом.

## Классы

### `TimeoutCheck`

**Описание**: Класс для проверки времени и ожидания ввода с таймаутом.

**Принцип работы**:
Класс `TimeoutCheck` использует модуль `datetime` для получения текущего времени и модуль `threading` для реализации таймаутов. Он предоставляет методы для проверки, находится ли текущее время в заданном интервале, а также для ожидания ввода от пользователя с таймаутом.

**Атрибуты**:
- `result` (bool | None): Результат проверки интервала времени.
- `user_input` (str | None): Ввод пользователя.

**Методы**:
- `interval(start: time = time(23, 0), end: time = time(6, 0)) -> bool`: Проверяет, находится ли текущее время в заданном интервале.
- `interval_with_timeout(timeout: int = 5, start: time = time(23, 0), end: time = time(6, 0)) -> bool`: Проверяет, находится ли текущее время в заданном интервале с таймаутом.
- `get_input() -> None`: Запрашивает ввод от пользователя.
- `input_with_timeout(timeout: int = 5) -> str | None`: Ожидает ввод от пользователя с таймаутом.

## Функции

### `interval`

```python
def interval(self, start: time = time(23, 0), end: time = time(6, 0)) -> bool:
    """ Функция проверяет, находится ли текущее время в указанном интервале.

    Args:
        start (time): Начало интервала (по умолчанию 23:00).
        end (time): Конец интервала (по умолчанию 06:00).

    Returns:
        bool: True, если текущее время находится в интервале, False в противном случае.
    """
```

**Назначение**: Проверка, находится ли текущее время в заданном интервале.

**Параметры**:
- `start` (time): Время начала интервала. По умолчанию `23:00`.
- `end` (time): Время окончания интервала. По умолчанию `06:00`.

**Возвращает**:
- `bool`: `True`, если текущее время находится в интервале, `False` в противном случае.

**Как работает функция**:

1.  Получает текущее время с использованием `datetime.now().time()`.
2.  Проверяет, находится ли текущее время в интервале, определяемом параметрами `start` и `end`.
3.  Если `start` меньше `end`, то интервал находится в пределах одного дня (например, с 08:00 до 17:00). В этом случае, функция проверяет, находится ли текущее время между `start` и `end` включительно.
4.  Если `start` больше `end`, то интервал охватывает полночь (например, с 23:00 до 06:00). В этом случае, функция проверяет, находится ли текущее время после `start` или до `end` включительно.
5.  Результат проверки сохраняется в атрибуте `self.result`.

```
    Получение текущего времени
    │
    └───> Проверка, находится ли интервал в пределах одного дня (start < end)
          │
          ├───> Да: Проверка, находится ли текущее время между start и end
          │     │
          │     └───> Сохранение результата в self.result
          │
          └───> Нет: Проверка, находится ли текущее время после start или до end
                │
                └───> Сохранение результата в self.result
```

**Примеры**:

```python
from datetime import time
from src.utils.date_time import TimeoutCheck

timeout_check = TimeoutCheck()

# Пример 1: Текущее время находится в интервале с 23:00 до 06:00
start_time = time(23, 0)
end_time = time(6, 0)
result = timeout_check.interval(start=start_time, end=end_time)
print(f"Текущее время находится в интервале с {start_time} до {end_time}: {result}")

# Пример 2: Текущее время находится в интервале с 08:00 до 17:00
start_time = time(8, 0)
end_time = time(17, 0)
result = timeout_check.interval(start=start_time, end=end_time)
print(f"Текущее время находится в интервале с {start_time} до {end_time}: {result}")
```

### `interval_with_timeout`

```python
def interval_with_timeout(self, timeout: int = 5, start: time = time(23, 0), end: time = time(6, 0)) -> bool:
    """ Функция проверяет, находится ли текущее время в указанном интервале с таймаутом.

    Args:
        timeout (int): Время в секундах для ожидания проверки интервала.
        start (time): Начало интервала (по умолчанию 23:00).
        end (time): Конец интервала (по умолчанию 06:00).

    Returns:
        bool: True, если текущее время находится в интервале и ответ получен в течение таймаута, False, если нет или произошел таймаут.
    """
```

**Назначение**: Проверка, находится ли текущее время в заданном интервале с таймаутом.

**Параметры**:
- `timeout` (int): Время ожидания в секундах. По умолчанию `5`.
- `start` (time): Время начала интервала. По умолчанию `23:00`.
- `end` (time): Время окончания интервала. По умолчанию `06:00`.

**Возвращает**:
- `bool`: `True`, если текущее время находится в интервале и ответ получен в течение таймаута, `False`, если нет или произошел таймаут.

**Как работает функция**:

1.  Создает новый поток (`threading.Thread`) для выполнения проверки интервала времени (`self.interval`).
2.  Запускает поток.
3.  Ожидает завершения потока в течение заданного времени (`timeout`).
4.  Если поток завершился в течение таймаута, возвращает результат проверки интервала времени (`self.result`).
5.  Если таймаут произошел, выводит сообщение о таймауте, дожидается завершения потока и возвращает `False`.

```
    Создание и запуск потока для проверки интервала
    │
    └───> Ожидание завершения потока с таймаутом
          │
          ├───> Поток завершился в течение таймаута
          │     │
          │     └───> Возврат результата проверки интервала (self.result)
          │
          └───> Таймаут произошел
                │
                ├───> Вывод сообщения о таймауте
                │
                └───> Дожидается завершения потока и возвращает False
```

**Примеры**:

```python
from datetime import time
from src.utils.date_time import TimeoutCheck

timeout_check = TimeoutCheck()

# Пример 1: Проверка интервала с таймаутом 5 секунд
start_time = time(23, 0)
end_time = time(6, 0)
result = timeout_check.interval_with_timeout(timeout=5, start=start_time, end=end_time)
print(f"Текущее время находится в интервале с {start_time} до {end_time} (с таймаутом): {result}")

# Пример 2: Проверка интервала с таймаутом 1 секунда (таймаут может произойти)
start_time = time(8, 0)
end_time = time(17, 0)
result = timeout_check.interval_with_timeout(timeout=1, start=start_time, end=end_time)
print(f"Текущее время находится в интервале с {start_time} до {end_time} (с таймаутом): {result}")
```

### `get_input`

```python
def get_input(self):
    """ Запрашиваем ввод от пользователя."""
```

**Назначение**: Запрос ввода от пользователя.

**Как работает функция**:

1.  Запрашивает ввод от пользователя с помощью функции `input("U:> ")`.
2.  Сохраняет введенные данные в атрибуте `self.user_input`.

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

**Назначение**: Ожидание ввода от пользователя с таймаутом.

**Параметры**:
- `timeout` (int): Время ожидания ввода в секундах. По умолчанию `5`.

**Возвращает**:
- `str | None`: Введенные данные или `None`, если произошел таймаут.

**Как работает функция**:

1.  Создает новый поток (`threading.Thread`) для получения ввода от пользователя (`self.get_input`).
2.  Запускает поток.
3.  Ожидает завершения потока в течение заданного времени (`timeout`).
4.  Если поток завершился в течение таймаута, возвращает введенные данные (`self.user_input`).
5.  Если таймаут произошел, выводит сообщение о таймауте и возвращает `None`.

```
    Создание и запуск потока для получения ввода
    │
    └───> Ожидание завершения потока с таймаутом
          │
          ├───> Поток завершился в течение таймаута
          │     │
          │     └───> Возврат введенных данных (self.user_input)
          │
          └───> Таймаут произошел
                │
                ├───> Вывод сообщения о таймауте
                │
                └───> Возврат None
```

**Примеры**:

```python
from src.utils.date_time import TimeoutCheck

timeout_check = TimeoutCheck()

# Пример 1: Ожидание ввода с таймаутом 5 секунд
user_input = timeout_check.input_with_timeout(timeout=5)
if user_input:
    print(f"Введенные данные: {user_input}")
else:
    print("Таймаут при вводе данных")

# Пример 2: Ожидание ввода с таймаутом 1 секунда (таймаут может произойти)
user_input = timeout_check.input_with_timeout(timeout=1)
if user_input:
    print(f"Введенные данные: {user_input}")
else:
    print("Таймаут при вводе данных")
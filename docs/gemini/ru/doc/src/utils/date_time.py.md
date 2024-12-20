# Модуль `date_time`

## Обзор

Модуль `date_time` предоставляет класс `TimeoutCheck` с функциональностью для проверки, находится ли текущее время в заданном интервале, и включает опциональный таймаут. Он также позволяет ожидать ввод пользователя с таймаутом. Этот модуль полезен для выполнения операций, которые должны происходить только в определенные периоды времени (например, обслуживание в ночное время).

## Содержание

- [Классы](#классы)
    - [`TimeoutCheck`](#timeoutcheck)
        - [`__init__`](#__init__)
        - [`interval`](#interval)
        - [`interval_with_timeout`](#interval_with_timeout)
        - [`get_input`](#get_input)
        - [`input_with_timeout`](#input_with_timeout)
- [Пример использования](#пример-использования)

## Классы

### `TimeoutCheck`

**Описание**: Класс, предоставляющий методы для проверки временных интервалов и ожидания ввода с таймаутом.

#### `__init__`

**Описание**: Инициализирует экземпляр класса `TimeoutCheck`.

#### `interval`

**Описание**: Проверяет, находится ли текущее время в заданном интервале.

**Параметры**:
- `start` (time, optional): Начало интервала. По умолчанию `23:00`.
- `end` (time, optional): Конец интервала. По умолчанию `06:00`.

**Возвращает**:
- `bool`: `True`, если текущее время находится в интервале, `False` в противном случае.

#### `interval_with_timeout`

**Описание**: Проверяет, находится ли текущее время в заданном интервале с таймаутом.

**Параметры**:
- `timeout` (int, optional): Время в секундах для ожидания проверки интервала. По умолчанию `5`.
- `start` (time, optional): Начало интервала. По умолчанию `23:00`.
- `end` (time, optional): Конец интервала. По умолчанию `06:00`.

**Возвращает**:
- `bool`: `True`, если текущее время находится в интервале и ответ получен в течение таймаута, `False` в противном случае или при таймауте.

#### `get_input`

**Описание**: Запрашивает ввод от пользователя.

#### `input_with_timeout`

**Описание**: Ожидает ввод пользователя с таймаутом.

**Параметры**:
- `timeout` (int, optional): Время ожидания ввода в секундах. По умолчанию `5`.

**Возвращает**:
- `str | None`: Введенные данные или `None`, если произошел таймаут.

## Пример использования

```python
if __name__ == '__main__':
    # Пример использования
    timeout_check = TimeoutCheck()
    
    # Проверка интервала с таймаутом в 5 секунд
    if timeout_check.interval_with_timeout(timeout=5):
        print("Текущее время находится в интервале.")
    else:
        print("Текущее время вне интервала или произошел таймаут.")
```
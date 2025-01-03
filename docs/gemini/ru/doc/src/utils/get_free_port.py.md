# Модуль `get_free_port`

## Обзор

Модуль `get_free_port` предоставляет функцию для поиска и возврата свободного порта в заданном диапазоне или первого доступного порта, если диапазон не указан.

## Оглавление

1. [Функции](#Функции)
    - [`get_free_port`](#get_free_port)
    - [`_is_port_in_use`](#_is_port_in_use)
## Функции

### `get_free_port`

**Описание**: Находит и возвращает свободный порт в указанном диапазоне или первый доступный порт, если диапазон не задан.

**Параметры**:
- `host` (str): Адрес хоста для проверки доступных портов.
- `port_range` (Optional[Tuple[int, int] | Tuple[str, str]], optional): Кортеж, содержащий начало и конец диапазона портов для поиска. По умолчанию `None`.

**Возвращает**:
- `int`: Доступный номер порта.

**Вызывает исключения**:
- `ValueError`: Если не удается найти свободный порт в указанном диапазоне или если диапазон портов недопустим.

### `_is_port_in_use`

**Описание**: Проверяет, используется ли данный порт на указанном хосте.

**Параметры**:
- `host` (str): Адрес хоста для проверки.
- `port` (int): Номер порта для проверки.

**Возвращает**:
- `bool`: `True`, если порт используется, `False` в противном случае.
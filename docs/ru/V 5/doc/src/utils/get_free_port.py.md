# Модуль для поиска свободного порта

## Обзор

Модуль `get_free_port` предоставляет функциональность для поиска свободного порта в заданном диапазоне или первого доступного порта, если диапазон не указан. Он проверяет, какие порты уже используются, и возвращает первый свободный порт.

## Подробней

Этот модуль полезен в ситуациях, когда необходимо динамически выделять порты для сетевых сервисов или приложений, чтобы избежать конфликтов с уже используемыми портами. Он позволяет задать диапазон портов для поиска или использовать первый доступный порт, начиная с 1024. В проекте `hypotez` данный модуль может использоваться для настройки сетевых соединений и сервисов, которым требуется динамическое выделение портов.

## Функции

### `get_free_port`

```python
def get_free_port(host: str, port_range: Optional[str | List[str]] = None) -> int:
    """
    Finds and returns a free port within the specified range, or the first available port if no range is given.

    Args:
        host (str): The host address to check for available ports.
        port_range (Optional[str | List[str]], optional): A port range specified as a string "min-max" or a list of strings.
               E.g.: "3000-3999", ["3000-3999", "8000-8010"], None. Defaults to `None`.

    Returns:
        int: An available port number.

    Raises:
        ValueError: If no free port can be found within the specified range, or if the port range is invalid.
    """
    ...
```

**Как работает функция**:
Функция `get_free_port` принимает адрес хоста и необязательный диапазон портов в качестве входных данных. Если диапазон портов указан, функция пытается найти свободный порт в этом диапазоне. Если диапазон портов не указан, функция ищет первый доступный порт, начиная с 1024. Если свободный порт не найден в указанном диапазоне или вообще, функция вызывает исключение `ValueError`.

**Параметры**:
- `host` (str): Адрес хоста для проверки доступных портов.
- `port_range` (Optional[str | List[str]], optional): Диапазон портов, заданный как строка "min-max" или список строк. Например: "3000-3999", ["3000-3999", "8000-8010"], `None`. По умолчанию `None`.

**Возвращает**:
- `int`: Доступный номер порта.

**Вызывает исключения**:
- `ValueError`: Если не удается найти свободный порт в указанном диапазоне или если диапазон портов недействителен.

**Примеры**:

```python
get_free_port('localhost', '3000-3005')
```

### `_is_port_in_use`

```python
def _is_port_in_use(host: str, port: int) -> bool:
    """
    Checks if a given port is in use on the specified host.

    Args:
        host (str): The host address.
        port (int): The port number to check.

    Returns:
        bool: True if the port is in use, False otherwise.
    """
    ...
```

**Как работает функция**:

Функция `_is_port_in_use` проверяет, используется ли данный порт на указанном хосте. Она создает сокет и пытается привязать его к указанному адресу хоста и номеру порта. Если привязка удается, это означает, что порт свободен, и функция возвращает `False`. Если привязка не удается (возникает исключение `OSError`), это означает, что порт используется, и функция возвращает `True`.

**Параметры**:

- `host` (str): Адрес хоста.
- `port` (int): Номер порта для проверки.

**Возвращает**:

- `bool`: `True`, если порт используется, `False` в противном случае.

**Вызывает исключения**:

- Отсутствуют.

**Примеры**:

```python
_is_port_in_use('localhost', 3000)
```

### `_parse_port_range`

```python
def _parse_port_range(port_range_str: str) -> Tuple[int, int]:
    """
    Parses port range string "min-max" into a tuple (min_port, max_port).

    Args:
        port_range_str (str): The port range string.

    Returns:
        Tuple[int, int]: A tuple containing minimum and maximum port numbers.

    Raises:
        ValueError: If the port range string format is invalid.
    """
    ...
```

**Как работает функция**:

Функция `_parse_port_range` разбирает строку диапазона портов в формате "min-max" и возвращает кортеж, содержащий минимальный и максимальный номера портов. Если строка имеет неверный формат или минимальный порт больше или равен максимальному порту, функция вызывает исключение `ValueError`.

**Параметры**:

- `port_range_str` (str): Строка диапазона портов.

**Возвращает**:

- `Tuple[int, int]`: Кортеж, содержащий минимальный и максимальный номера портов.

**Вызывает исключения**:

- `ValueError`: Если формат строки диапазона портов недействителен.

**Примеры**:

```python
_parse_port_range('3000-3999')
```
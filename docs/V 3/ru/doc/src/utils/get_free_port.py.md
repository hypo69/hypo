# Модуль для поиска свободного порта

## Обзор

Этот модуль предоставляет функцию `get_free_port`, которая позволяет найти свободный порт в заданной сети. Он может искать порт в указанном диапазоне или найти первый доступный порт, если диапазон не указан. Этот модуль важен для динамического выделения портов в приложениях, где необходимо избежать конфликтов портов.

## Подробней

Модуль `get_free_port` предоставляет функцию для поиска доступного порта на указанном хосте. Он может работать как с заданным диапазоном портов, так и без него. Если предоставлен диапазон портов (в виде строки "min-max" или списка строк), функция будет перебирать порты в этом диапазоне, пока не найдет свободный. Если диапазон не указан, функция начнет поиск с порта 1024 и будет увеличивать номер порта до тех пор, пока не найдет свободный.
Этот модуль используется для автоматического назначения портов сервисам, чтобы избежать конфликтов и упростить конфигурацию.

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
```

**Описание**: Находит и возвращает свободный порт в указанном диапазоне или первый доступный порт, если диапазон не указан.

**Параметры**:

- `host` (str): Адрес хоста для проверки доступных портов.
- `port_range` (Optional[str | List[str]], optional): Диапазон портов, заданный в виде строки "min-max" или списка строк. Например: "3000-3999", ["3000-3999", "8000-8010"], None. По умолчанию `None`.

**Возвращает**:

- `int`: Доступный номер порта.

**Вызывает исключения**:

- `ValueError`: Если не удается найти свободный порт в указанном диапазоне, или если диапазон портов недействителен.

**Примеры**:

```python
>>> get_free_port('localhost', '3000-3005')
3001
>>> get_free_port('localhost')
1024
>>> get_free_port('localhost', ['3000-3005', '8000-8005'])
3001
```
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
```

**Описание**: Проверяет, используется ли данный порт на указанном хосте.

**Параметры**:

- `host` (str): Адрес хоста.
- `port` (int): Номер порта для проверки.

**Возвращает**:

- `bool`: `True`, если порт используется, `False` в противном случае.

**Примеры**:

```python
>>> _is_port_in_use('localhost', 3000)
True
>>> _is_port_in_use('localhost', 9999)
False
```
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
```

**Описание**: Преобразует строку диапазона портов "min-max" в кортеж (min_port, max_port).

**Параметры**:

- `port_range_str` (str): Строка диапазона портов.

**Возвращает**:

- `Tuple[int, int]`: Кортеж, содержащий минимальный и максимальный номера портов.

**Вызывает исключения**:

- `ValueError`: Если формат строки диапазона портов недействителен.

**Примеры**:

```python
>>> _parse_port_range('3000-3005')
(3000, 3005)
>>> _parse_port_range('10000-10010')
(10000, 10010)
```
```python
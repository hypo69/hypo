# Модуль для поиска свободного порта

## Обзор

Модуль `get_free_port.py` предоставляет функцию для поиска свободного порта в системе. Он позволяет указать диапазон портов для поиска или использовать первый доступный порт, если диапазон не задан. Модуль включает в себя функции для проверки занятости порта и разбора строки с диапазоном портов.

## Подробней

Этот модуль полезен в ситуациях, когда необходимо динамически выделять порты для сетевых сервисов или приложений, чтобы избежать конфликтов с уже используемыми портами. Функция `get_free_port` позволяет автоматизировать процесс поиска доступного порта, что упрощает настройку и запуск сетевых приложений. В проекте `hypotez` этот модуль может использоваться для настройки различных сервисов, требующих сетевого взаимодействия, таких как веб-серверы или API.

## Функции

### `get_free_port`

```python
def get_free_port(host: str, port_range: Optional[str | List[str]] = None) -> int:
    """
    Находит и возвращает свободный порт в указанном диапазоне или первый доступный порт, если диапазон не указан.

    Args:
        host (str): IP-адрес хоста для проверки доступности портов.
        port_range (Optional[str | List[str]], optional): Диапазон портов, заданный строкой "min-max" или списком строк.
            Например: "3000-3999", ["3000-3999", "8000-8010"], None. По умолчанию `None`.

    Returns:
        int: Доступный номер порта.

    Raises:
        ValueError: Если не удается найти свободный порт в указанном диапазоне или если диапазон портов недействителен.
    """
```

**Как работает функция**:

1.  **Проверка наличия диапазона портов**: Функция начинает с проверки, был ли предоставлен `port_range`.
2.  **Обработка строкового диапазона**: Если `port_range` является строкой, функция пытается разобрать его с помощью `_parse_port_range`. Если разбор не удался, вызывается исключение `ValueError`.
3.  **Обработка списка диапазонов**: Если `port_range` является списком, функция итерируется по элементам списка, каждый из которых должен быть строкой, представляющей диапазон портов.
4.  **Поиск свободного порта в диапазоне**: Для каждого диапазона функция итерируется по портам в этом диапазоне и проверяет, используется ли порт с помощью функции `_is_port_in_use`. Если порт свободен, функция возвращает его.
5.  **Поиск первого доступного порта**: Если `port_range` не предоставлен, функция начинает поиск с порта 1024 и увеличивает его, пока не найдет свободный порт.
6.  **Обработка ошибок**: Если не удается найти свободный порт в указанном диапазоне или если указан неверный тип диапазона, функция регистрирует ошибку с помощью `logger.error` и вызывает исключение `ValueError`.

**Внутренние функции**:

*   `_is_port_in_use`

    ```python
    def _is_port_in_use(host: str, port: int) -> bool:
        """
        Проверяет, используется ли данный порт на указанном хосте.

        Args:
            host (str): IP-адрес хоста.
            port (int): Номер порта для проверки.

        Returns:
            bool: True, если порт используется, False в противном случае.
        """
    ```

    **Как работает функция**:

    1.  **Создание сокета**: Функция создает TCP-сокет с помощью `socket.socket`.
    2.  **Попытка привязки сокета к адресу**: Функция пытается привязать сокет к указанному адресу (хост и порт) с помощью `sock.bind`.
    3.  **Определение доступности порта**: Если привязка прошла успешно, это означает, что порт свободен, и функция возвращает `False`. Если при привязке возникает исключение `OSError`, это означает, что порт используется, и функция возвращает `True`.

    A
    ↓
    B → C
    ↓
    D

    A: Создание сокета
    B: Попытка привязки сокета к адресу
    C: Обработка исключения (порт занят)
    D: Возврат результата

*   `_parse_port_range`

    ```python
    def _parse_port_range(port_range_str: str) -> Tuple[int, int]:
        """
        Разбирает строку диапазона портов "min-max" в кортеж (min_port, max_port).

        Args:
            port_range_str (str): Строка диапазона портов.

        Returns:
            Tuple[int, int]: Кортеж, содержащий минимальный и максимальный номера портов.

        Raises:
            ValueError: Если формат строки диапазона портов недействителен.
        """
    ```

    **Как работает функция**:

    1.  **Разделение строки на части**: Функция разделяет строку `port_range_str` на две части по символу `-` с помощью `port_range_str.split('-')`.
    2.  **Проверка количества частей**: Функция проверяет, что получилось ровно две части. Если нет, вызывается исключение `ValueError`.
    3.  **Преобразование частей в целые числа**: Функция пытается преобразовать обе части в целые числа с помощью `int()`.
    4.  **Проверка корректности диапазона**: Функция проверяет, что минимальный порт меньше максимального. Если нет, вызывается исключение `ValueError`.
    5.  **Возврат диапазона портов**: Если все проверки пройдены успешно, функция возвращает кортеж `(min_port, max_port)`.

    A
    ↓
    B → C
    ↓
    D → E
    ↓
    F

    A: Разделение строки на части
    B: Проверка количества частей
    C: Обработка ошибки (неверный формат)
    D: Преобразование частей в целые числа
    E: Проверка корректности диапазона
    F: Возврат диапазона портов

**Примеры**:

```python
import socket
from typing import Optional, Tuple, List

from src.logger import logger


def get_free_port(host: str, port_range: Optional[str | List[str]] = None) -> int:
    def _is_port_in_use(host: str, port: int) -> bool:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.bind((host, port))
                return False  # Port is available
            except OSError:
                return True  # Port is in use

    def _parse_port_range(port_range_str: str) -> Tuple[int, int]:
        try:
            parts = port_range_str.split('-')
            if len(parts) != 2:
                logger.error(f'Error: Invalid port range string format: {port_range_str}')
                raise ValueError(f'Invalid port range string format: {port_range_str}')
            min_port = int(parts[0])
            max_port = int(parts[1])

            if min_port >= max_port:
                logger.error(f'Error: Invalid port range {port_range_str}')
                raise ValueError(f'Invalid port range {port_range_str}')
            return min_port, max_port

        except ValueError:
            logger.error(f'Error: Invalid port range {port_range_str}')
            raise ValueError(f'Invalid port range {port_range_str}')

    if port_range:
        if isinstance(port_range, str):
            try:
                min_port, max_port = _parse_port_range(port_range)
            except ValueError as ex:
                logger.error(f'Error: {ex}')
                raise ValueError(f'Invalid port range {port_range}')
            for port in range(min_port, max_port + 1):
                if not _is_port_in_use(host, port):
                    return port
            logger.error(f'Error: No free port found in range {port_range}')
            raise ValueError(f'No free port found in range {port_range}')

        elif isinstance(port_range, list):
            for item in port_range:
                try:
                    if isinstance(item, str):
                        min_port, max_port = _parse_port_range(item)
                    else:
                        logger.error(f'Error: Invalid port range item {item}')
                        raise ValueError(f'Invalid port range item {item}')

                    for port in range(min_port, max_port + 1):
                        if not _is_port_in_use(host, port):
                            return port
                except ValueError as ex:
                    logger.error(f'Error: {ex}')
                    continue  # Skip to the next range in the list if any range fails parsing or no port

            logger.error(f'Error: No free port found in specified ranges {port_range}')
            raise ValueError(f'No free port found in specified ranges {port_range}')

        else:
            logger.error(f'Error: Invalid port range type {type(port_range)}')
            raise ValueError(f'Invalid port range type {type(port_range)}')
    else:
        # If no range given, find first available port
        port = 1024  # start from 1024, since lower ports are system ports
        while True:
            if not _is_port_in_use(host, port):
                return port
            port += 1
            if port > 65535:
                logger.error(f'Error: No free port found')
                raise ValueError('No free port found')

# Пример 1: Получение свободного порта в диапазоне "3000-3005"
free_port = get_free_port('localhost', '3000-3005')
print(f'Свободный порт в диапазоне 3000-3005: {free_port}')

# Пример 2: Получение свободного порта в диапазонах ["3000-3005", "8000-8010"]
free_port = get_free_port('localhost', ["3000-3005", "8000-8010"])
print(f'Свободный порт в диапазонах 3000-3005 и 8000-8010: {free_port}')

# Пример 3: Получение первого доступного порта, начиная с 1024
free_port = get_free_port('localhost')
print(f'Первый доступный порт, начиная с 1024: {free_port}')
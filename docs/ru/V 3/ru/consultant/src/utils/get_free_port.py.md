## Анализ кода модуля `get_free_port.py`

**Качество кода:**

- **Соответствие стандартам**: 7/10
- **Плюсы**:
  - Код хорошо структурирован и разбит на небольшие, легко читаемые функции.
  - Присутствует обработка исключений для различных сценариев.
  - Используется модуль `logger` для логирования ошибок.
- **Минусы**:
  - Не все функции и методы имеют docstring.
  - Есть импорт `header`, который не используется.
  - В docstring используются двойные кавычки вместо одинарных.
  - Не все переменные аннотированы типами.

**Рекомендации по улучшению:**

1.  **Удалить неиспользуемый импорт**:
    - Удалить строку `import header  # Not used`, так как этот модуль не используется в коде.

2.  **Исправить docstring**:
    - Заменить двойные кавычки на одинарные в docstring модуля и функций.
    - Дополнить docstring для внутренних функций `_is_port_in_use` и `_parse_port_range`.
    - В docstring модуля заменить `Agrs` на `Args`.

3.  **Добавить аннотации типов**:
    - Убедиться, что все переменные и возвращаемые значения функций аннотированы типами.

4.  **Улучшить обработку ошибок**:
    - Добавить более конкретные сообщения об ошибках в блоки `except`.

5.  **Упростить логику**:
    - Упростить логику обработки списка диапазонов портов.

6.  **Добавить примеры использования**:
    - Добавить примеры использования в docstring модуля и функции `get_free_port`.

**Оптимизированный код:**

```python
## \file /src/utils/get_free_port.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3
"""
Модуль для поиска свободного порта.

Args:
    host (str): Адрес хоста для проверки доступных портов.
    port_range (Optional[str | List[str]], optional): Диапазон портов, заданный строкой "min-max" или списком строк.
           Например: "3000-3999", ["3000-3999", "8000-8010"], None. Defaults to `None`.

Returns:
    int: Доступный номер порта.

Raises:
    ValueError: Если не удается найти свободный порт в указанном диапазоне или если диапазон портов недействителен.

Example:
    >>> get_free_port('localhost', '3000-3005')
    3001
"""

import socket
from typing import Optional, Tuple, List

# import header  # Not used # Удален неиспользуемый импорт
from src.logger import logger


def get_free_port(host: str, port_range: Optional[str | List[str]] = None) -> int:
    """
    Находит и возвращает свободный порт в указанном диапазоне или первый доступный порт, если диапазон не указан.

    Args:
        host (str): Адрес хоста для проверки доступных портов.
        port_range (Optional[str | List[str]], optional): Диапазон портов, заданный строкой "min-max" или списком строк.
               Например: "3000-3999", ["3000-3999", "8000-8010"], None. Defaults to `None`.

    Returns:
        int: Доступный номер порта.

    Raises:
        ValueError: Если не удается найти свободный порт в указанном диапазоне или если диапазон портов недействителен.

    Example:
        >>> get_free_port('localhost', '3000-3005')
        3001
    """

    def _is_port_in_use(host: str, port: int) -> bool:
        """
        Проверяет, используется ли данный порт на указанном хосте.

        Args:
            host (str): Адрес хоста.
            port (int): Номер порта для проверки.

        Returns:
            bool: True, если порт используется, False в противном случае.
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.bind((host, port))
                return False  # Port is available
            except OSError:
                return True  # Port is in use

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
        try:
            parts = port_range_str.split('-')
            if len(parts) != 2:
                logger.error(f'Invalid port range string format: {port_range_str}')  # Улучшено сообщение об ошибке
                raise ValueError(f'Invalid port range string format: {port_range_str}')
            min_port = int(parts[0])
            max_port = int(parts[1])

            if min_port >= max_port:
                logger.error(f'Invalid port range: {port_range_str}')  # Улучшено сообщение об ошибке
                raise ValueError(f'Invalid port range: {port_range_str}')
            return min_port, max_port

        except ValueError as ex:  # Добавлено имя исключения
            logger.error(f'Invalid port range {port_range_str}', exc_info=True)  # Улучшено логирование ошибки
            raise ValueError(f'Invalid port range {port_range_str}') from ex  # Проброс исключения с сохранением трассировки

    if port_range:
        if isinstance(port_range, str):
            try:
                min_port, max_port = _parse_port_range(port_range)
            except ValueError as e:
                logger.error(f'Error: {e}')
                raise ValueError(f'Invalid port range {port_range}') from e  # Проброс исключения с сохранением трассировки
            for port in range(min_port, max_port + 1):
                if not _is_port_in_use(host, port):
                    return port
            logger.error(f'No free port found in range {port_range}')  # Улучшено сообщение об ошибке
            raise ValueError(f'No free port found in range {port_range}')

        elif isinstance(port_range, list):
            for item in port_range:
                if not isinstance(item, str):
                    logger.error(f'Invalid port range item {item}')  # Улучшено сообщение об ошибке
                    raise ValueError(f'Invalid port range item {item}')

                try:
                    min_port, max_port = _parse_port_range(item)
                    for port in range(min_port, max_port + 1):
                        if not _is_port_in_use(host, port):
                            return port
                except ValueError as e:
                    logger.error(f'Error: {e}')
                    continue  # Skip to the next range in the list if any range fails parsing or no port

            logger.error(f'No free port found in specified ranges {port_range}')  # Улучшено сообщение об ошибке
            raise ValueError(f'No free port found in specified ranges {port_range}')

        else:
            logger.error(f'Invalid port range type {type(port_range)}')  # Улучшено сообщение об ошибке
            raise ValueError(f'Invalid port range type {type(port_range)}')
    else:
        # If no range given, find first available port
        port = 1024  # start from 1024, since lower ports are system ports
        while True:
            if not _is_port_in_use(host, port):
                return port
            port += 1
            if port > 65535:
                logger.error(f'No free port found')  # Улучшено сообщение об ошибке
                raise ValueError('No free port found')
```
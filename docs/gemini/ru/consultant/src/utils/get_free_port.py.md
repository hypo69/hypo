# Анализ кода модуля `get_free_port`

**Качество кода**:
- **Соответствие стандартам**: 8
- **Плюсы**:
    -  Код достаточно хорошо структурирован и читаем.
    -  Присутствует  документация в формате RST для функции `get_free_port` и `_is_port_in_use`.
    -  Используется `logger` для логирования ошибок.
- **Минусы**:
    -  Некоторые комментарии можно сделать более информативными.
    -  Можно добавить проверку типа данных для `port_range`.
    -   Необходимо унифицировать кавычки в коде.
    -  Следует заменить использование `f-string` на более читаемый вариант, например, когда это ошибка.
    -  В `try-except` блоке нет необходимости использовать `OSError` так как это базовый тип ошибки и его можно заменить на `Exception`.

**Рекомендации по улучшению**:

-  Унифицировать использование кавычек, используя одинарные кавычки для строк в коде и двойные только для вывода.
-  Улучшить комментарии, сделать их более информативными.
-  Добавить проверку типа данных для `port_range`, убедившись, что это `Tuple[int, int]`.
-  Изменить обработку ошибок, используя `logger.error` и `raise ValueError` для более информативных сообщений.
-  Уточнить комментарии, избегая общих фраз типа "получаем". Вместо этого описывать более конкретно действие.
-  Упростить блок try-except, используя `Exception`.
-   Использовать f-строки для более удобного и читаемого форматирования строк, и убрать их из  `logger.error`, сделав их более наглядными.

**Оптимизированный код**:

```python
import socket
from typing import Tuple, Optional

from src.logger.logger import logger  # import logger from src.logger


def get_free_port(host: str, port_range: Optional[Tuple[int, int]] = None) -> int:
    """
    Находит и возвращает свободный порт в указанном диапазоне или первый доступный порт, если диапазон не задан.

    :param host: Адрес хоста для проверки доступных портов.
    :type host: str
    :param port_range: (Опционально) Кортеж, содержащий начало и конец диапазона портов для поиска, если необходимо.
    :type port_range: Optional[Tuple[int, int]]
    :return: Номер доступного порта.
    :rtype: int
    :raises ValueError: Если не удается найти свободный порт в указанном диапазоне, или если диапазон портов недействителен.

    Пример:
        >>> get_free_port('localhost', (8000, 9000))
        8001
    """
    def _is_port_in_use(host: str, port: int) -> bool:
        """
        Проверяет, используется ли данный порт на указанном хосте.

        :param host: Адрес хоста для проверки.
        :type host: str
        :param port: Номер порта для проверки.
        :type port: int
        :return: True, если порт используется, False в противном случае.
        :rtype: bool

        Пример:
            >>> _is_port_in_use('localhost', 8080)
            True
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.bind((host, port))
                return False  # порт свободен
            except Exception:  # заменили OSError на Exception
                return True  # порт занят

    if port_range:
        if not isinstance(port_range, tuple) or len(port_range) != 2 or port_range[0] >= port_range[1]:  # добавили проверку типа
            logger.error(f"Error: Invalid port range {port_range}")  # выводим ошибку с помощью логера
            raise ValueError(f"Invalid port range {port_range}") # выводим ошибку с помощью raise

        min_port, max_port = port_range
        for port in range(int(min_port), int(max_port) + 1):
            if not _is_port_in_use(host, port):  # проверяем, свободен ли порт
                return port
        logger.error(f"Error: No free port found in range {port_range}") # выводим ошибку с помощью логера
        raise ValueError(f"No free port found in range {port_range}")  # выводим ошибку с помощью raise
    else:
       # если диапазон не задан, находим первый доступный порт
        port = 1024  # начинаем с 1024, т.к. порты ниже - системные
        while True:
            if not _is_port_in_use(host, port):  # проверяем, свободен ли порт
                return port
            port += 1
            if port > 65535:
                logger.error("Error: No free port found")  # выводим ошибку с помощью логера
                raise ValueError('No free port found')  # выводим ошибку с помощью raise
```
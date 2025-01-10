# Анализ кода модуля `get_free_port`

**Качество кода**
10
 - Плюсы
    - Код хорошо структурирован и читаем.
    - Присутствует подробная документация для функций.
    - Используется логирование ошибок.
    - Обработка ошибок выполняется с помощью `try-except` и логирования.
 - Минусы
    - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Для форматирования строк в логгерах используется f-строки, хотя по требованию нужно использовать одинарные кавычки.

**Рекомендации по улучшению**
1. Заменить f-строки на конкатенацию строк в логерах.
2. Добавить описание модуля в начале файла.
3. Указать тип данных для `port_range` в формате `Tuple[int, int]`
4. Внести исправления в соответствии с комментариями.

**Оптимизированный код**
```python
"""
Модуль для поиска свободного сетевого порта.
=========================================================================================

Этот модуль предоставляет функцию `get_free_port`, которая используется для поиска свободного сетевого порта
в заданном диапазоне или первого доступного порта, если диапазон не указан.

Пример использования
--------------------

Пример использования функции `get_free_port`:

.. code-block:: python

    from src.utils.get_free_port import get_free_port

    free_port = get_free_port(host='127.0.0.1', port_range=(8000, 9000))
    print(f"Свободный порт: {free_port}")

"""
import socket
from typing import Tuple, Optional
from src.logger.logger import logger


def get_free_port(host: str, port_range: Optional[Tuple[int, int]] = None) -> int:
    """
    Находит и возвращает свободный порт в указанном диапазоне или первый доступный порт, если диапазон не задан.

    :param host: IP-адрес хоста для проверки доступных портов.
    :type host: str
    :param port_range: (Опционально) Кортеж, содержащий начало и конец диапазона портов для поиска.
    :type port_range: Optional[Tuple[int, int]]
    :return: Номер доступного порта.
    :rtype: int
    :raises ValueError: Если не удается найти свободный порт в указанном диапазоне или если диапазон портов недействителен.

    Example:
        >>> get_free_port('127.0.0.1', (8000, 8010))
        8000
        >>> get_free_port('127.0.0.1')
        1024
    """
    def _is_port_in_use(host: str, port: int) -> bool:
        """
        Проверяет, используется ли данный порт на указанном хосте.

        :param host: IP-адрес хоста для проверки.
        :type host: str
        :param port: Номер порта для проверки.
        :type port: int
        :return: True, если порт используется, False в противном случае.
        :rtype: bool
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                # код исполняет привязку сокета к хосту и порту.
                sock.bind((host, port))
                return False  # Порт доступен
            except OSError:
                # код исполняет возврат True если порт используется
                return True  # Порт используется

    # проверка наличия диапазона портов
    if port_range:
        # проверка валидности диапазона портов
        if len(port_range) != 2 or port_range[0] >= port_range[1]:
            # логирование ошибки неверного диапазона портов
            logger.error('Error: Invalid port range ' + str(port_range))
            raise ValueError('Invalid port range ' + str(port_range))
        # получение минимального и максимального порта
        min_port, max_port = port_range
        # цикл для проверки портов в диапазоне
        for port in range(int(min_port), int(max_port) + 1):
            # проверка что порт свободен
            if not _is_port_in_use(host, port):
                # возврат свободного порта
                return port
        # логирование ошибки отсутствия свободного порта в диапазоне
        logger.error('Error: No free port found in range ' + str(port_range))
        raise ValueError('No free port found in range ' + str(port_range))
    else:
       # Если диапазон не задан, находим первый доступный порт
        port = 1024 # начинаем с 1024, так как порты ниже являются системными
        while True:
            # проверка что порт свободен
            if not _is_port_in_use(host, port):
                # возврат свободного порта
                return port
            # инкремент порта
            port += 1
            # проверка что порт не выходит за границы
            if port > 65535:
                # логирование ошибки отсутствия свободного порта
                logger.error('Error: No free port found')
                raise ValueError('No free port found')
```
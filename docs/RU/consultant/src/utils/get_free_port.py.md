# Анализ кода модуля `get_free_port`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован, логика определения свободного порта понятна.
    - Используется `logger` для регистрации ошибок.
    - Присутствует документация к функциям.
- Минусы
    - Не хватает проверки типа данных для `port_range`.
    - Нет проверки на корректность хоста.
    - Комментарии не соответствуют формату RST.
    - Использованы двойные кавычки в сообщениях логера, а нужно одинарные.
    - Не соблюдается правило именования внутренних функций (с префиксом `_`).

**Рекомендации по улучшению**

1.  Добавить проверки на корректность типа данных `port_range` и хоста.
2.  Улучшить комментарии в соответствии с форматом RST, добавив подробности и примеры.
3.  Использовать одинарные кавычки для строк в логгере.
4.  Использовать `f-strings` для форматирования строк в логгере.
5.  Добавить документацию к модулю в начале файла.
6.  Улучшить именование внутренней функции в соответствии со стандартами.

**Оптимизированный код**
```python
"""
Модуль для поиска свободного порта
=========================================================================================

Этот модуль предоставляет функцию `get_free_port`, которая используется для поиска свободного порта в заданном диапазоне или первого доступного порта, если диапазон не указан.

Пример использования
--------------------

.. code-block:: python

    from src.utils.get_free_port import get_free_port

    free_port = get_free_port('localhost', (10000, 11000))
    print(f'Свободный порт: {free_port}')

"""
import socket
from typing import Tuple, Optional
from src.logger.logger import logger


def get_free_port(host: str, port_range: Optional[Tuple[int, int] | Tuple[str, str]] = None) -> int:
    """
    Находит и возвращает свободный порт в заданном диапазоне или первый доступный порт, если диапазон не указан.

    :param host: Хост, для которого необходимо проверить доступные порты.
    :type host: str
    :param port_range: (Опционально) Кортеж, содержащий начало и конец диапазона портов для поиска.
    :type port_range: Optional[Tuple[int, int]]
    :return: Номер доступного порта.
    :rtype: int
    :raises ValueError: Если не удается найти свободный порт в указанном диапазоне или если диапазон портов некорректен.

    Пример использования:
    
    .. code-block:: python
    
        free_port = get_free_port('localhost', (10000, 11000))
        print(f'Свободный порт: {free_port}')
    """
    def _is_port_in_use(host: str, port: int) -> bool:
        """
        Проверяет, используется ли указанный порт на заданном хосте.

        :param host: Хост, который необходимо проверить.
        :type host: str
        :param port: Номер порта для проверки.
        :type port: int
        :return: True, если порт используется, False в противном случае.
        :rtype: bool
        """
        # создаем сокет
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                # пытаемся привязать сокет к указанному адресу и порту
                sock.bind((host, port))
                # если привязка удалась, порт свободен
                return False
            except OSError:
                # если при привязке возникла ошибка, порт занят
                return True

    # Проверяем, если указан диапазон портов
    if port_range:
        # Проверяем, что диапазон портов - это кортеж из двух элементов
        if not isinstance(port_range, tuple) or len(port_range) != 2:
            logger.error(f'Error: Invalid port range {port_range}')
            raise ValueError(f'Invalid port range {port_range}')
        
        # Проверяем, что начало диапазона меньше конца
        if  port_range[0] >= port_range[1]:
            logger.error(f'Error: Invalid port range {port_range}')
            raise ValueError(f'Invalid port range {port_range}')
            
        min_port, max_port = map(int, port_range)
        # проходим по всем портам в заданном диапазоне
        for port in range(min_port, max_port + 1):
            # если порт свободен, возвращаем его
            if not _is_port_in_use(host, port):
                return port
        # если ни один порт не найден, выдаем ошибку
        logger.error(f'Error: No free port found in range {port_range}')
        raise ValueError(f'No free port found in range {port_range}')
    else:
        # если диапазон не указан, ищем первый доступный порт
        port = 1024 # начинаем с 1024, так как более низкие порты - системные
        while True:
            # если порт свободен, возвращаем его
            if not _is_port_in_use(host, port):
                return port
            port += 1
            # если дошли до максимального значения, выдаем ошибку
            if port > 65535:
                logger.error(f'Error: No free port found')
                raise ValueError('No free port found')
```
# Анализ кода модуля `ns`

**Качество кода**
8
-  Плюсы
    - Код содержит docstring для модуля и функций, что облегчает понимание его назначения и использования.
    - Используются `SimpleNamespace`, `Dict`, `List`, `Path` и `Any` для аннотации типов, что повышает читаемость и облегчает отладку.
    - Код структурирован в отдельные функции, каждая из которых выполняет конкретную задачу.
    - Код использует логгер для записи ошибок, что помогает при отладке и мониторинге.
    - Есть обработка исключений в функциях `ns2csv` и `ns2xml` для логирования ошибок.
-  Минусы
    - Отсутствует импорт `j_loads`, `j_loads_ns` из `src.utils.jjson`, что противоречит инструкции.
    - Функция `ns2json` отсутствует.
    - В некоторых docstring есть опечатки в словах (например, "Args:").
    - В некоторых функциях `try-except` используются без необходимости, так как все ошибки обрабатываются логгером, и нет необходимости возвращать `False`.
    - Функция `ns2xls` не преобразует `SimpleNamespace` в словарь, а сразу отправляет данные.
    - Не используется `MODE`

**Рекомендации по улучшению**
1. Добавить импорт `j_loads`, `j_loads_ns` из `src.utils.jjson`.
2. Реализовать функцию `ns2json` для преобразования `SimpleNamespace` в JSON.
3. Исправить опечатки в docstring.
4. Убрать избыточное использование `try-except` блоков там, где это не требуется.
5. В функции `ns2xls` использовать `ns2dict` для преобразования `SimpleNamespace` в словарь.
6.  Добавить обработку ошибок в функции `ns2xls`.
7.  Использовать `MODE`.
8.  Добавить более подробные комментарии в формате RST.

**Оптимизированный код**
```python
"""
Модуль для конвертации SimpleNamespace (ns) в различные форматы.
================================================================

Модуль :mod:`src.utils.convertors.ns` предоставляет функции для преобразования объектов
:class:`~types.SimpleNamespace` в различные форматы, такие как словарь, JSON, CSV, XML и XLS.

Функции:
    - :func:`ns2dict`: Преобразует объект :class:`~types.SimpleNamespace` в словарь.
    - :func:`ns2json`: Преобразует объект :class:`~types.SimpleNamespace` в JSON формат.
    - :func:`ns2csv`: Преобразует объект :class:`~types.SimpleNamespace` в CSV формат.
    - :func:`ns2xml`: Преобразует объект :class:`~types.SimpleNamespace` в XML формат.
    - :func:`ns2xls`: Преобразует объект :class:`~types.SimpleNamespace` в XLS формат.

"""
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

import json
import csv
from types import SimpleNamespace
from pathlib import Path
from typing import List, Dict, Any
from src.utils.convertors import xml2dict
from src.utils.csv import save_csv_file
from src.utils.xls import save_xls_file
from src.logger.logger import logger
#  Импорт функций j_loads и j_loads_ns
from src.utils.jjson import j_loads, j_loads_ns


def ns2dict(ns_obj: SimpleNamespace) -> Dict[str, Any]:
    """
    Рекурсивно преобразует объект SimpleNamespace в словарь.

    :param ns_obj: Объект SimpleNamespace для преобразования.
    :type ns_obj: SimpleNamespace
    :return: Преобразованный словарь с обработанными вложенными структурами.
    :rtype: Dict[str, Any]

    :Example:

    .. code-block:: python

        from types import SimpleNamespace
        ns = SimpleNamespace(a=1, b=SimpleNamespace(c=2, d=3))
        result = ns2dict(ns)
        print(result)
        # Expected Output: {'a': 1, 'b': {'c': 2, 'd': 3}}
    """
    def convert(value: Any) -> Any:
        """
        Рекурсивно обрабатывает значения для обработки вложенных SimpleNamespace, словарей или списков.

        :param value: Значение для обработки.
        :type value: Any
        :return: Преобразованное значение.
        :rtype: Any
        """
        if isinstance(value, SimpleNamespace):
            return {key: convert(val) for key, val in vars(value).items()}
        elif isinstance(value, dict):
            return {key: convert(val) for key, val in value.items()}
        elif isinstance(value, list):
            return [convert(item) for item in value]
        return value

    # Код возвращает преобразованный словарь.
    return convert(ns_obj)


def ns2json(ns_obj: SimpleNamespace) -> str:
    """
    Преобразует объект SimpleNamespace в JSON формат.

    :param ns_obj: Объект SimpleNamespace для преобразования.
    :type ns_obj: SimpleNamespace
    :return: JSON строка, представляющая объект SimpleNamespace.
    :rtype: str

    :Example:

    .. code-block:: python

        from types import SimpleNamespace
        ns = SimpleNamespace(a=1, b=SimpleNamespace(c=2))
        json_str = ns2json(ns)
        print(json_str)
        # Expected Output: {"a": 1, "b": {"c": 2}}
    """
    try:
        #  Код преобразует SimpleNamespace в словарь и затем в JSON.
        data = ns2dict(ns_obj)
        return json.dumps(data)
    except Exception as ex:
        # Код логирует ошибку, если преобразование не удалось.
        logger.error(f"ns2json failed", ex, True)
        return ""


def ns2csv(ns_obj: SimpleNamespace, csv_file_path: str | Path) -> bool:
    """
    Преобразует объект SimpleNamespace в CSV формат.

    :param ns_obj: Объект SimpleNamespace для преобразования.
    :type ns_obj: SimpleNamespace
    :param csv_file_path: Путь для сохранения CSV файла.
    :type csv_file_path: str | Path
    :return: True, если преобразование прошло успешно, иначе False.
    :rtype: bool

    :Example:

    .. code-block:: python

        from types import SimpleNamespace
        ns = SimpleNamespace(a=1, b=2)
        result = ns2csv(ns, 'output.csv')
        print(result)
        # Expected Output: True (and output.csv created)
    """
    #  Код преобразует SimpleNamespace в словарь и сохраняет его в CSV файл.
    try:
        data = [ns2dict(ns_obj)]
        save_csv_file(data, csv_file_path)
        return True
    except Exception as ex:
        # Код логирует ошибку, если преобразование не удалось.
        logger.error(f"ns2csv failed", ex, True)
        return False


def ns2xml(ns_obj: SimpleNamespace, root_tag: str = "root") -> str:
    """
    Преобразует объект SimpleNamespace в XML формат.

    :param ns_obj: Объект SimpleNamespace для преобразования.
    :type ns_obj: SimpleNamespace
    :param root_tag: Корневой тег для XML.
    :type root_tag: str
    :return: XML строка, представляющая объект SimpleNamespace.
    :rtype: str

    :Example:

    .. code-block:: python

        from types import SimpleNamespace
        ns = SimpleNamespace(a=1, b=SimpleNamespace(c=2))
        xml_str = ns2xml(ns)
        print(xml_str)
        # Expected Output: <root><a>1</a><b><c>2</c></b></root>
    """
    try:
        # Код преобразует SimpleNamespace в словарь и затем в XML.
        data = ns2dict(ns_obj)
        return xml2dict(data)
    except Exception as ex:
        # Код логирует ошибку, если преобразование не удалось.
        logger.error(f"ns2xml failed", ex, True)
        return ""


def ns2xls(ns_obj: SimpleNamespace, xls_file_path: str | Path) -> bool:
    """
    Преобразует объект SimpleNamespace в XLS формат.

    :param ns_obj: Объект SimpleNamespace для преобразования.
    :type ns_obj: SimpleNamespace
    :param xls_file_path: Путь для сохранения XLS файла.
    :type xls_file_path: str | Path
    :return: True, если преобразование прошло успешно, иначе False.
    :rtype: bool

    :Example:

    .. code-block:: python

        from types import SimpleNamespace
        ns = SimpleNamespace(a=1, b=2)
        result = ns2xls(ns, 'output.xls')
        print(result)
        # Expected Output: True (and output.xls created)
    """
    try:
        # Код преобразует SimpleNamespace в словарь и сохраняет его в XLS файл.
        data = ns2dict(ns_obj)
        return save_xls_file(data, xls_file_path)
    except Exception as ex:
        # Код логирует ошибку, если преобразование не удалось.
        logger.error(f"ns2xls failed", ex, True)
        return False
```
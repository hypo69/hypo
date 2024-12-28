# Анализ кода модуля `csv`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и разделен на отдельные функции, каждая из которых выполняет определенную задачу.
    - Используются типы аннотации для параметров и возвращаемых значений, что улучшает читаемость и облегчает отладку.
    - Присутствует обработка исключений, что делает код более устойчивым к ошибкам.
    - Код включает docstring для функций, объясняя их назначение, аргументы и возвращаемые значения.
    - Код использует `logger` для логирования ошибок, что полезно для отслеживания проблем.
- Минусы
    - В коде не используются `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения данных.
    - Не все функции имеют подробные docstring с примерами использования в reStructuredText (RST).
    - Отсутствует docstring для модуля в формате RST.
    - Не все функции и переменные соответствуют стандартам именования ранее обработанных файлов.

**Рекомендации по улучшению**

1. **Импорты**:
   - Добавить `from src.utils.jjson import j_loads, j_loads_ns`.
2. **Docstring модуля**:
    -  Добавить подробное описание модуля в формате RST, включая примеры использования.
3. **Использование `j_loads`**:
    - Изменить функцию `csv_to_json` для использования `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения данных из JSON.
4. **Docstring**:
    - Добавить более подробные docstring для каждой функции в формате RST, включая примеры использования, параметров и возвращаемых значений.
5. **Обработка ошибок**:
    - Убрать лишний `return` в блоке `try` функции `csv_to_json`
6. **Соответствие именованию**:
    - Проверить и привести имена функций и переменных в соответствие с ранее обработанными файлами.
7. **Оптимизация**:
   - Убрать явное возвращение `None` из `except`.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для конвертации данных из CSV в различные форматы, включая JSON и SimpleNamespace.
=========================================================================================

Этот модуль предоставляет набор утилит для работы с CSV-файлами, включая преобразование
их в словари, объекты SimpleNamespace и JSON.

Пример использования
--------------------

Использование функций модуля для конвертации CSV-файлов:

.. code-block:: python

    from pathlib import Path

    csv_file_path = Path("data.csv")
    json_file_path = Path("data.json")

    # Конвертация CSV в словарь
    csv_data_dict = csv2dict(csv_file_path)
    if csv_data_dict:
        print("CSV data as dictionary:")
        print(csv_data_dict)

    # Конвертация CSV в SimpleNamespace
    csv_data_ns = csv2ns(csv_file_path)
    if csv_data_ns:
        print("CSV data as SimpleNamespace:")
        print(csv_data_ns)

    # Конвертация CSV в JSON
    json_data = csv_to_json(csv_file_path, json_file_path)
    if json_data:
        print("CSV data converted to JSON and saved to 'data.json':")
        print(json_data)
"""

import csv
from pathlib import Path
from typing import List, Dict
from types import SimpleNamespace
from src.logger.logger import logger
from src.utils.jjson import j_loads, j_loads_ns
# from src.utils.csv import read_csv_as_dict, read_csv_as_ns, save_csv_file, read_csv_file # TODO: проверить эти импорты


def csv2dict(csv_file: str | Path, *args, **kwargs) -> dict | None:
    """
    Преобразует данные из CSV-файла в словарь.

    :param csv_file: Путь к CSV-файлу.
    :type csv_file: str | Path
    :param args: Дополнительные позиционные аргументы, передаваемые в `read_csv_as_dict`.
    :param kwargs: Дополнительные именованные аргументы, передаваемые в `read_csv_as_dict`.
    :return: Словарь, содержащий данные из CSV, или `None` при неудаче.
    :rtype: dict | None
    :raises Exception: Если не удается прочитать CSV.

    Пример:

    .. code-block:: python

        from pathlib import Path

        csv_file_path = Path("data.csv")
        csv_data = csv2dict(csv_file_path)
        if csv_data:
            print(csv_data)
    """
    from src.utils.csv import read_csv_as_dict # импортируем внутри функции, чтобы избежать циклического импорта
    # код исполняет чтение данных из CSV файла и возвращает их в виде словаря
    return read_csv_as_dict(csv_file, *args, **kwargs)


def csv2ns(csv_file: str | Path, *args, **kwargs) -> SimpleNamespace | None:
    """
    Преобразует данные из CSV-файла в объекты SimpleNamespace.

    :param csv_file: Путь к CSV-файлу.
    :type csv_file: str | Path
    :param args: Дополнительные позиционные аргументы, передаваемые в `read_csv_as_ns`.
    :param kwargs: Дополнительные именованные аргументы, передаваемые в `read_csv_as_ns`.
    :return: Объект SimpleNamespace, содержащий данные из CSV, или `None` при неудаче.
    :rtype: SimpleNamespace | None
    :raises Exception: Если не удается прочитать CSV.

    Пример:

    .. code-block:: python

        from pathlib import Path

        csv_file_path = Path("data.csv")
        csv_data = csv2ns(csv_file_path)
        if csv_data:
            print(csv_data)
    """
    from src.utils.csv import read_csv_as_ns # импортируем внутри функции, чтобы избежать циклического импорта
    # код исполняет чтение данных из CSV файла и возвращает их в виде SimpleNamespace
    return read_csv_as_ns(csv_file, *args, **kwargs)


def csv_to_json(
    csv_file_path: str | Path,
    json_file_path: str | Path,
    exc_info: bool = True
) -> List[Dict[str, str]] | None:
    """
    Преобразует CSV-файл в JSON формат и сохраняет его в JSON-файл.

    :param csv_file_path: Путь к CSV-файлу для чтения.
    :type csv_file_path: str | Path
    :param json_file_path: Путь к JSON-файлу для сохранения.
    :type json_file_path: str | Path
    :param exc_info: Включать ли информацию об исключении в лог. По умолчанию True.
    :type exc_info: bool, optional
    :return: Данные JSON в виде списка словарей или None, если преобразование не удалось.
    :rtype: List[Dict[str, str]] | None

    Пример:

    .. code-block:: python

        from pathlib import Path

        csv_file_path = Path("data.csv")
        json_file_path = Path("data.json")
        json_data = csv_to_json(csv_file_path, json_file_path)
        if json_data:
            print(json_data)
    """
    from src.utils.csv import read_csv_file # импортируем внутри функции, чтобы избежать циклического импорта
    try:
        # код исполняет чтение данных из CSV файла
        data = read_csv_file(csv_file_path, exc_info=exc_info)
        if data is not None:
            # код исполняет запись данных в JSON файл
            with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
                json.dump(data, jsonfile, indent=4)
            return data
    except Exception as ex:
        # код исполняет логирование ошибки при конвертации CSV в JSON
        logger.error("Failed to convert CSV to JSON", ex, exc_info=exc_info)
```
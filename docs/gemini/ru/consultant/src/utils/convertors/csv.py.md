# Анализ кода модуля `csv`

**Качество кода**
7
-  Плюсы
    - Код содержит docstring для модуля и функций.
    - Используется `logger` для логирования ошибок.
    - Присутствует разделение на функции для разных преобразований (CSV в dict, CSV в SimpleNamespace).
    - Есть пример использования в docstring модуля.
    - Используется `pathlib.Path` для путей файлов.
-  Минусы
    -  Не используется `j_loads` или `j_loads_ns` для чтения файлов.
    -  Импорт `read_csv_as_dict`, `read_csv_as_ns`, `save_csv_file`, `read_csv_file` из `src.utils.csv` является не стандартным. Необходимо проверить его наличие и корректность.
    -  Некоторые docstring требуют корректировки в соответствии с RST.
    -  В функции `csv_to_json` используется стандартный `json.dump` вместо `j_dumps`.
    -  Избыточная обработка ошибок в `try-except`.
    -  Не везде соблюдается единый стиль именования.
    -  Возвращаемое значение `return` без значения следует заменить на `return None`.

**Рекомендации по улучшению**

1.  Использовать `j_loads` и `j_dumps` из `src.utils.jjson` для работы с JSON.
2.  Уточнить использование `read_csv_as_dict`, `read_csv_as_ns`, `save_csv_file`, `read_csv_file`. Если они не являются частью текущего модуля, нужно заменить их на реализацию внутри модуля.
3.  Переписать docstring в соответствии с RST, включая описания параметров и возвращаемых значений.
4.  Избегать `try-except` блоков, где это возможно, заменив на логирование ошибок через `logger.error`.
5.  Убедиться, что все импорты соответствуют структуре проекта.
6.  Привести к общему стилю именование переменных и функций.
7.  Добавить более детальное описание в docstring к модулю, функциям, методам.
8.  Заменить `return` без значения на `return None`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для преобразования данных из CSV в JSON и обратно
========================================================

Этот модуль предоставляет функции для конвертации данных из формата CSV в
различные структуры данных Python, включая словари и объекты
SimpleNamespace. Также предоставляется функция для конвертации CSV в JSON.

.. code-block:: python

    # Пример использования:

    # Используя JSON список словарей
    json_data_list = [{"name": "John", "age": 30, "city": "New York"}, {"name": "Alice", "age": 25, "city": "Los Angeles"}]
    json_file_path = 'data.json'
    csv_file_path = 'data.csv'

    # Конвертируем JSON в CSV
    json2csv.json2csv(json_data_list, csv_file_path)

    # Конвертируем CSV обратно в JSON
    csv_data = csv_to_json(csv_file_path, json_file_path)
    if csv_data:
        if isinstance(csv_data, list):
            if isinstance(csv_data[0], dict):
                print("CSV данные (список словарей):")
            else:
                print("CSV данные (список значений):")
            print(csv_data)
        else:
            print("Не удалось прочитать данные CSV.")
"""

import csv
from pathlib import Path
from typing import List, Dict, Any
from types import SimpleNamespace
from src.logger.logger import logger
from src.utils.jjson import j_loads, j_dumps

MODE = 'dev'


def csv2dict(csv_file: str | Path, *args, **kwargs) -> Dict[str, Any] | None:
    """
    Преобразует данные из CSV файла в словарь.

    :param csv_file: Путь к CSV файлу для чтения.
    :type csv_file: str | Path
    :param args: Дополнительные позиционные аргументы, которые будут переданы в `csv.DictReader`.
    :param kwargs: Дополнительные именованные аргументы, которые будут переданы в `csv.DictReader`.
    :return: Словарь, содержащий данные из CSV файла, или None в случае ошибки.
    :rtype: dict | None

    :raises Exception: Если не удается прочитать CSV файл.
    """
    try:
        # Чтение данных из CSV файла
        with open(csv_file, 'r', encoding='utf-8', newline='') as file:
            reader = csv.DictReader(file, *args, **kwargs)
            return list(reader)
    except Exception as ex:
        logger.error(f'Не удалось прочитать CSV файл {csv_file}', ex)
        return None


def csv2ns(csv_file: str | Path, *args, **kwargs) -> SimpleNamespace | None:
    """
    Преобразует данные из CSV файла в объекты SimpleNamespace.

    :param csv_file: Путь к CSV файлу для чтения.
    :type csv_file: str | Path
    :param args: Дополнительные позиционные аргументы, которые будут переданы в `csv.DictReader`.
    :param kwargs: Дополнительные именованные аргументы, которые будут переданы в `csv.DictReader`.
    :return: Объект SimpleNamespace, содержащий данные из CSV файла, или None в случае ошибки.
    :rtype: SimpleNamespace | None

    :raises Exception: Если не удается прочитать CSV файл.
    """
    try:
        # Чтение данных из CSV файла
        data = csv2dict(csv_file, *args, **kwargs)
        if data:
            return [SimpleNamespace(**row) for row in data]
        return None
    except Exception as ex:
        logger.error(f'Не удалось преобразовать CSV файл {csv_file} в SimpleNamespace', ex)
        return None


def csv_to_json(
    csv_file_path: str | Path,
    json_file_path: str | Path,
    exc_info: bool = True
) -> List[Dict[str, str]] | None:
    """
    Преобразует CSV файл в JSON формат и сохраняет его в JSON файл.

    :param csv_file_path: Путь к CSV файлу для чтения.
    :type csv_file_path: str | Path
    :param json_file_path: Путь к JSON файлу для сохранения.
    :type json_file_path: str | Path
    :param exc_info: Включать ли информацию об исключении в лог. По умолчанию True.
    :type exc_info: bool, optional
    :return: JSON данные в виде списка словарей, или None в случае ошибки.
    :rtype: List[Dict[str, str]] | None

    :Example:
        >>> json_data = csv_to_json('dialogue_log.csv', 'dialogue_log.json')
        >>> print(json_data)
        [{'role': 'user', 'content': 'Hello'}, {'role': 'assistant', 'content': 'Hi there!'}]
    """
    try:
        # Чтение данных из CSV файла
        data = csv2dict(csv_file_path, exc_info=exc_info)
        if data:
            # Сохранение данных в JSON файл
            with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
                json.dump(data, jsonfile, indent=4)
            return data
        return None
    except Exception as ex:
        logger.error(f"Не удалось преобразовать CSV файл {csv_file_path} в JSON", ex, exc_info=exc_info)
        return None

```
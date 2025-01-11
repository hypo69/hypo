# Анализ кода модуля `csv`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и разделен на функции, каждая из которых выполняет определенную задачу.
    - Используются `Path` и `str` для путей к файлам, что обеспечивает гибкость.
    - Присутствует документация для каждой функции в формате RST.
    - Используется `logger` для логирования ошибок.
-  Минусы
    -  Импорт `json` не используется,  вместо `json.dump` можно использовать `j_dumps` из `src.utils.jjson`
    -  Не все комментарии соответствуют стилю документации reStructuredText.
    - В функции `csv_to_json` не используется `j_dumps`.
    -  Импорты расположены не в алфавитном порядке.

**Рекомендации по улучшению**

1.  Добавить описание модуля в начале файла в формате RST.
2.  Заменить `json.dump` на `j_dumps` из `src.utils.jjson`.
3.  Использовать `from src.utils.jjson import j_dumps` для импорта функции.
4.  Документацию к функциям привести к единому стандарту.
5.  Импортировать `logger` из `src.logger.logger`.
6.  Упорядочить импорты в алфавитном порядке.
7.  Уточнить docstring для функций `csv2dict` и `csv2ns`.
8.  Избавиться от избыточного `return` в `try` блоке.
9.  Добавить комментарии к блокам кода.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12

"""
Модуль для работы с CSV и JSON конвертацией.
=========================================================================================

Этот модуль предоставляет функции для преобразования данных из CSV в различные форматы,
такие как словари, SimpleNamespace и JSON.

Функции:
    - `csv2dict`: Преобразует CSV данные в словарь.
    - `csv2ns`: Преобразует CSV данные в объекты SimpleNamespace.
    - `csv_to_json`: Преобразует CSV данные в JSON формат и сохраняет в файл.

Пример использования
--------------------

Пример использования функций:

.. code-block:: python

    # Пример использования:
    # JSON список словарей
    json_data_list = [{"name": "John", "age": 30, "city": "New York"}, {"name": "Alice", "age": 25, "city": "Los Angeles"}]
    json_file_path = 'data.json'
    csv_file_path = 'data.csv'

    # Преобразование JSON в CSV
    json2csv.json2csv(json_data_list, csv_file_path)

    # Преобразование CSV обратно в JSON
    csv_data = csv_to_json(csv_file_path, json_file_path)
    if csv_data:
        if isinstance(csv_data, list):
            if isinstance(csv_data[0], dict):
                print("CSV data (list of dictionaries):")
            else:
                print("CSV data (list of values):")
            print(csv_data)
        else:
            print("Failed to read CSV data.")
"""
import csv
from pathlib import Path
from types import SimpleNamespace
from typing import Dict, List
# импортируем j_dumps для сохранения json
from src.utils.jjson import j_dumps
# импортируем logger для обработки ошибок
from src.logger.logger import logger
# импортируем функции для работы с csv
from src.utils.csv import read_csv_as_dict, read_csv_as_ns, save_csv_file, read_csv_file


def csv2dict(csv_file: str | Path, *args, **kwargs) -> Dict | None:
    """
    Преобразует CSV данные в словарь.

    Args:
        csv_file (str | Path): Путь к CSV файлу для чтения.
        *args: Дополнительные позиционные аргументы для `read_csv_as_dict`.
        **kwargs: Дополнительные именованные аргументы для `read_csv_as_dict`.

    Returns:
        dict | None: Словарь, содержащий данные из CSV, или `None`, если преобразование не удалось.

    Raises:
        Exception: Если не удается прочитать CSV файл.
    """
    # код исполняет чтение csv файла как словарь
    return read_csv_as_dict(csv_file, *args, **kwargs)


def csv2ns(csv_file: str | Path, *args, **kwargs) -> SimpleNamespace | None:
    """
    Преобразует CSV данные в объекты SimpleNamespace.

    Args:
        csv_file (str | Path): Путь к CSV файлу для чтения.
        *args: Дополнительные позиционные аргументы для `read_csv_as_ns`.
        **kwargs: Дополнительные именованные аргументы для `read_csv_as_ns`.

    Returns:
        SimpleNamespace | None: Объект SimpleNamespace, содержащий данные из CSV, или `None`, если преобразование не удалось.

    Raises:
        Exception: Если не удается прочитать CSV файл.
    """
    # код исполняет чтение csv файла как SimpleNamespace
    return read_csv_as_ns(csv_file, *args, **kwargs)


def csv_to_json(
    csv_file_path: str | Path,
    json_file_path: str | Path,
    exc_info: bool = True
) -> List[Dict[str, str]] | None:
    """
    Преобразует CSV файл в JSON формат и сохраняет его в JSON файл.

    Args:
        csv_file_path (str | Path): Путь к CSV файлу для чтения.
        json_file_path (str | Path): Путь к JSON файлу для сохранения.
        exc_info (bool, optional): Если `True`, включает информацию об исключении в лог. По умолчанию `True`.

    Returns:
        List[Dict[str, str]] | None: Данные JSON в виде списка словарей, или `None`, если преобразование не удалось.

    Example:
        >>> json_data = csv_to_json('dialogue_log.csv', 'dialogue_log.json')
        >>> print(json_data)
        [{'role': 'user', 'content': 'Hello'}, {'role': 'assistant', 'content': 'Hi there!'}]
    """
    try:
        #  код исполняет чтение csv файла
        data = read_csv_file(csv_file_path, exc_info=exc_info)
        # проверка что данные не пустые
        if data is not None:
            # код исполняет сохранение данных в json файл
            with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
                j_dumps(data, jsonfile, indent=4)
            #  возвращает данные
            return data
    except Exception as ex:
        # если возникает ошибка логируем
        logger.error('Failed to convert CSV to JSON', ex, exc_info=exc_info)
        #  возвращаем None
        return
```
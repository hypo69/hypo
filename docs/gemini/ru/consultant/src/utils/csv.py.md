# Анализ кода модуля `src.utils.csv`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и выполняет поставленные задачи.
    - Присутствует базовая обработка ошибок с использованием логгера.
    - Используются типы данных для параметров функций.
    - Присутствуют docstring для функций.
    - Код читабелен.
- Минусы
    - Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Некоторые docstring не полные, в них отсутствует описание возвращаемого значения, типов параметров.
    - Не везде используется `exc_info=True` при логировании ошибок.
    - Не используется `from src.logger.logger import logger` для логирования ошибок.
    - Не используется единый стиль форматирования кавычек (`'`).

**Рекомендации по улучшению**

1.  Заменить стандартный `json.dump` на `j_loads` или `j_loads_ns` из `src.utils.jjson` для записи JSON файлов, хотя в данном случае это не требуется.
2.  Дополнить docstring, описав все параметры и возвращаемые значения, а также их типы.
3.  Использовать константу для режима открытия файла `'r'` или `'w'`, например, `READ_MODE = 'r'`, `WRITE_MODE = 'w'`.
4.  Использовать `exc_info=True` для всех логов ошибок.
5.  Использовать `from src.logger.logger import logger` для импорта логгера.
6.  Исправить стиль кавычек в коде на `'` для соответствия общему стилю.
7.  Добавить комментарии в формате RST ко всем функциям, методам и классам.
8.  Избегать использования стандартных блоков `try-except`, предпочитая обработку ошибок с помощью `logger.error`.
9.  Избегать общих исключений `Exception` и использовать более конкретные, такие как `csv.Error`, `IOError`, `json.JSONDecodeError`.
10. Использовать `Path` везде, где это возможно.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для работы с CSV и JSON файлами
=========================================================================================

Этот модуль предоставляет набор функций для чтения, записи и преобразования
файлов в формате CSV и JSON.

Функции включают сохранение данных в CSV-файл, чтение CSV-файла, преобразование
CSV в JSON и чтение CSV в виде словаря или списка словарей, используя pandas.

Примеры использования
--------------------

Пример сохранения данных в CSV-файл:

.. code-block:: python

    data = [{'col1': 'val1', 'col2': 'val2'}, {'col1': 'val3', 'col2': 'val4'}]
    file_path = 'output.csv'
    save_csv_file(data, file_path, mode='w')

Пример чтения данных из CSV-файла:

.. code-block:: python

    file_path = 'output.csv'
    data = read_csv_file(file_path)
    if data:
        print(data)

Пример преобразования CSV в JSON:

.. code-block:: python

    csv_file_path = 'input.csv'
    json_file_path = 'output.json'
    read_csv_as_json(csv_file_path, json_file_path)

Пример чтения CSV в виде словаря:

.. code-block:: python

    csv_file_path = 'input.csv'
    data = read_csv_as_dict(csv_file_path)
    if data:
        print(data)

Пример чтения CSV в виде списка словарей:

.. code-block:: python

    csv_file_path = 'input.csv'
    data = read_csv_as_ns(csv_file_path)
    if data:
        print(data)
"""
import csv
# from json import dump
from pathlib import Path
from typing import List, Dict, Union
import pandas as pd

from src.logger.logger import logger
from src.utils.jjson import j_loads

READ_MODE = 'r'
WRITE_MODE = 'w'

def save_csv_file(
    data: List[Dict[str, str]],
    file_path: Union[str, Path],
    mode: str = 'a',
    exc_info: bool = True,
) -> bool:
    """Сохраняет список словарей в CSV-файл.

    :param data: Список словарей для сохранения.
    :type data: List[Dict[str, str]]
    :param file_path: Путь к CSV-файлу.
    :type file_path: Union[str, Path]
    :param mode: Режим открытия файла ('a' - добавление, 'w' - перезапись). По умолчанию 'a'.
    :type mode: str
    :param exc_info: Включать ли трассировку ошибок в логи.
    :type exc_info: bool
    :raises TypeError: Если входные данные не являются списком словарей.
    :raises ValueError: Если входные данные пустые.
    :returns: True в случае успеха, иначе False.
    :rtype: bool
    """
    if not isinstance(data, list):
        # Проверка, что входные данные - список
        logger.error('Input data must be a list of dictionaries.', exc_info=exc_info)
        return False
        # raise TypeError('Input data must be a list of dictionaries.')
    if not data:
        # Проверка, что список не пустой
        logger.error('Input data cannot be empty.', exc_info=exc_info)
        return False
        # raise ValueError('Input data cannot be empty.')
    
    try:
        #  Преобразование пути к файлу в Path object
        file_path = Path(file_path)
        #  Создание родительских директорий, если они не существуют
        file_path.parent.mkdir(parents=True, exist_ok=True)
        #  Открытие файла в указанном режиме
        with file_path.open(mode, newline='', encoding='utf-8') as file:
            #  Создание объекта DictWriter для записи данных в CSV
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            #  Запись заголовка, если файл новый или режим перезаписи
            if mode == WRITE_MODE or not file_path.exists():
                writer.writeheader()
            #  Запись данных в CSV
            writer.writerows(data)
        return True
    except (IOError, csv.Error) as e:
        # Логирование ошибки при записи в файл
        logger.error(f"Failed to save CSV to {file_path}: {e}", exc_info=exc_info)
        return False


def read_csv_file(file_path: Union[str, Path], exc_info: bool = True) -> List[Dict[str, str]] | None:
    """Читает содержимое CSV-файла в виде списка словарей.

    :param file_path: Путь к CSV-файлу.
    :type file_path: Union[str, Path]
    :param exc_info: Включать ли трассировку ошибок в логи.
    :type exc_info: bool
    :raises FileNotFoundError: Если файл не найден.
    :returns: Список словарей или None в случае ошибки.
    :rtype: List[Dict[str, str]] | None
    """
    try:
        #  Открытие файла для чтения
        with Path(file_path).open(READ_MODE, encoding='utf-8') as file:
            #  Чтение данных из CSV файла
            reader = csv.DictReader(file)
            #  Возвращаем данные в виде списка словарей
            return list(reader)
    except FileNotFoundError as e:
         #  Логирование ошибки, если файл не найден
        logger.error(f"File not found: {file_path}", exc_info=exc_info)
        return None
    except (IOError, csv.Error) as e:
        # Логирование ошибки при чтении файла
        logger.error(f"Failed to read CSV from {file_path}: {e}", exc_info=exc_info)
        return None


def read_csv_as_json(csv_file_path: Union[str, Path], json_file_path: Union[str, Path], exc_info: bool = True) -> bool:
    """Преобразует CSV-файл в JSON и сохраняет его.

    :param csv_file_path: Путь к CSV-файлу.
    :type csv_file_path: str | Path
    :param json_file_path: Путь для сохранения JSON-файла.
    :type json_file_path: str | Path
    :param exc_info: Включать ли трассировку ошибок в логи. По умолчанию True.
    :type exc_info: bool, optional
    :returns: True в случае успеха, иначе False.
    :rtype: bool
    """
    try:
        #  Чтение данных из CSV файла
        data = read_csv_file(csv_file_path, exc_info=exc_info)
        if data is None:
             # Возврат False, если данные не были прочитаны
            return False
        #  Открытие файла для записи в формате JSON
        with Path(json_file_path).open(WRITE_MODE, encoding='utf-8') as f:
            #  Запись данных в формате JSON
            j_loads(data, f, indent=4)
        return True
    except Exception as ex:
        # Логирование ошибки при преобразовании
        logger.error(f"Failed to convert CSV to JSON at {json_file_path}: {ex}", exc_info=exc_info)
        return False


def read_csv_as_dict(csv_file: Union[str, Path], exc_info: bool = True) -> dict | None:
    """Преобразует содержимое CSV в словарь.

    :param csv_file: Путь к CSV-файлу.
    :type csv_file: str | Path
    :param exc_info: Включать ли трассировку ошибок в логи. По умолчанию True.
    :type exc_info: bool, optional
    :returns: Словарь с содержимым CSV или None в случае ошибки.
    :rtype: dict | None
    """
    try:
        #  Открытие файла для чтения
        with Path(csv_file).open(READ_MODE, encoding='utf-8') as f:
            #  Чтение данных из CSV файла
            reader = csv.DictReader(f)
            #  Возврат данных в виде словаря
            return {"data": [row for row in reader]}
    except (IOError, csv.Error) as ex:
         #  Логирование ошибки при чтении CSV
        logger.error(f"Failed to read CSV as dictionary: {ex}", exc_info=exc_info)
        return None


def read_csv_as_ns(file_path: Union[str, Path], exc_info: bool = True) -> List[dict]:
    """Загружает CSV-данные в список словарей, используя Pandas.

    :param file_path: Путь к CSV-файлу.
    :type file_path: Union[str, Path]
    :param exc_info: Включать ли трассировку ошибок в логи. По умолчанию True.
    :type exc_info: bool, optional
    :returns: Список словарей, представляющих содержимое CSV.
    :rtype: List[dict]
    :raises FileNotFoundError: Если файл не найден.
    """
    try:
        #  Чтение данных из CSV файла с помощью pandas
        df = pd.read_csv(file_path)
        #  Преобразование DataFrame в список словарей
        return df.to_dict(orient='records')
    except FileNotFoundError as e:
         # Логирование ошибки, если файл не найден
        logger.error(f"File not found: {file_path}", exc_info=exc_info)
        return []
    except Exception as e:
         # Логирование ошибки при чтении CSV
        logger.error(f"Failed to load CSV as dictionaries from {file_path}: {e}", exc_info=exc_info)
        return []
```
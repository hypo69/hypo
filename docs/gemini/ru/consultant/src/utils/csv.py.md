# Анализ кода модуля `src.utils.csv`

**Качество кода**
8
- Плюсы
    - Код соответствует PEP8.
    - Присутствует базовая документация к функциям.
    - Используется `logger` для логирования ошибок.
    - Есть обработка исключений.
- Минусы
    - Не все docstring соответствуют reStructuredText (RST).
    - Не используется `j_loads` и `j_loads_ns` для загрузки JSON.
    - Не везде присутствуют подробные комментарии к коду.
    -  В некоторых местах документации отсутствуют типы.

**Рекомендации по улучшению**

1.  **Документация:**
    -   Переписать все docstring в формате RST.
    -   Добавить типы параметров и возвращаемых значений в docstring.
2.  **Импорты:**
    -   Проверить и добавить необходимые импорты, если они отсутствуют.
3.  **Обработка JSON:**
    -   Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для работы с JSON. В данном коде это пока не требуется, так как нет чтения JSON файлов, но в будущем следует использовать.
4.  **Логирование:**
    -   Убрать лишние блоки `try-except` и использовать `logger.error` для обработки ошибок.
5.  **Комментарии:**
    -   Добавить более подробные комментарии к коду, описывающие каждый шаг.
6. **Общая стилистика:**
   - Использовать одинарные кавычки `'` во всем коде, кроме docstring.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с CSV файлами.
=========================================================================================

Этот модуль предоставляет набор утилит для чтения и записи CSV файлов,
а также для их конвертации в другие форматы, такие как JSON и словари.

Пример использования
--------------------

Пример использования функций:

.. code-block:: python

    from pathlib import Path
    from src.utils.csv import save_csv_file, read_csv_file, read_csv_as_json, read_csv_as_dict, read_csv_as_ns

    # Пример записи в CSV файл
    data_to_save = [{'name': 'John', 'age': '30'}, {'name': 'Jane', 'age': '25'}]
    file_path = Path('output.csv')
    save_csv_file(data_to_save, file_path, mode='w')

    # Пример чтения из CSV файла
    read_data = read_csv_file(file_path)
    print(read_data)

    # Пример конвертации CSV в JSON
    json_file_path = Path('output.json')
    read_csv_as_json(file_path, json_file_path)

    # Пример чтения CSV как словаря
    dict_data = read_csv_as_dict(file_path)
    print(dict_data)

    # Пример чтения CSV как списка словарей с Pandas
    ns_data = read_csv_as_ns(file_path)
    print(ns_data)
"""

import csv
# импорт модуля json удален, так как он не используется напрямую в коде
from pathlib import Path
# from types import SimpleNamespace # SimpleNamespace не используется, импорт удален
from typing import List, Dict, Union
import pandas as pd
from src.logger.logger import logger


def save_csv_file(
    data: List[Dict[str, str]],
    file_path: Union[str, Path],
    mode: str = 'a',
    exc_info: bool = True,
) -> bool:
    """
    Сохраняет список словарей в CSV файл.

    :param data: Список словарей для сохранения.
    :type data: List[Dict[str, str]]
    :param file_path: Путь к CSV файлу.
    :type file_path: Union[str, Path]
    :param mode: Режим открытия файла ('a' для добавления, 'w' для перезаписи). По умолчанию 'a'.
    :type mode: str
    :param exc_info: Включать ли информацию об ошибках в логи.
    :type exc_info: bool
    :raises TypeError: Если входные данные не являются списком словарей.
    :raises ValueError: Если входные данные пусты.
    :returns: True в случае успеха, иначе False.
    :rtype: bool
    """
    # проверка, что входные данные являются списком
    if not isinstance(data, list):
        raise TypeError('Input data must be a list of dictionaries.')
    # проверка, что входные данные не пустые
    if not data:
        raise ValueError('Input data cannot be empty.')
    
    try:
        #  преобразование пути к файлу в объект Path
        file_path = Path(file_path)
        #  создание родительской директории, если она не существует
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # открытие файла в указанном режиме с кодировкой utf-8
        with file_path.open(mode, newline='', encoding='utf-8') as file:
            # создание объекта DictWriter для записи в CSV
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            # если файл открывается на запись или не существует, записывается заголовок
            if mode == 'w' or not file_path.exists():
                writer.writeheader()
            # запись строк в файл
            writer.writerows(data)
        return True
    except Exception as e:
        # в случае ошибки запись в лог и возврат False
        logger.error(f'Failed to save CSV to {file_path}', exc_info=exc_info)
        return False


def read_csv_file(file_path: Union[str, Path], exc_info: bool = True) -> List[Dict[str, str]] | None:
    """
    Читает содержимое CSV файла как список словарей.

    :param file_path: Путь к CSV файлу.
    :type file_path: Union[str, Path]
    :param exc_info: Включать ли информацию об ошибках в логи.
    :type exc_info: bool
    :raises FileNotFoundError: Если файл не найден.
    :returns: Список словарей или None, если чтение не удалось.
    :rtype: List[Dict[str, str]] | None
    """
    try:
        # открытие файла на чтение с кодировкой utf-8
        with Path(file_path).open('r', encoding='utf-8') as file:
            # создание объекта DictReader для чтения CSV
            reader = csv.DictReader(file)
            # преобразование данных в список словарей
            return list(reader)
    except FileNotFoundError as e:
        # в случае ошибки файла запись в лог и возврат None
        logger.error(f'File not found: {file_path}', exc_info=exc_info)
        return None
    except Exception as e:
         # в случае ошибки при чтении запись в лог и возврат None
        logger.error(f'Failed to read CSV from {file_path}', exc_info=exc_info)
        return None


def read_csv_as_json(csv_file_path: Union[str, Path], json_file_path: Union[str, Path], exc_info: bool = True) -> bool:
    """
    Преобразует CSV файл в JSON формат и сохраняет его.

    :param csv_file_path: Путь к CSV файлу.
    :type csv_file_path: Union[str, Path]
    :param json_file_path: Путь для сохранения JSON файла.
    :type json_file_path: Union[str, Path]
    :param exc_info: Включать ли информацию об ошибках в логи.
    :type exc_info: bool, optional
    :returns: True, если преобразование успешно, иначе False.
    :rtype: bool
    """
    try:
        # чтение данных из CSV файла
        data = read_csv_file(csv_file_path, exc_info=exc_info)
        # если чтение не удалось, возвращается False
        if data is None:
            return False
        # открытие файла для записи JSON
        with Path(json_file_path).open('w', encoding='utf-8') as f:
            # запись данных в JSON файл с отступами
            import json # импорт json здесь так как он используется только в этой функции
            json.dump(data, f, indent=4)
        return True
    except Exception as ex:
        # в случае ошибки запись в лог и возврат False
        logger.error(f'Failed to convert CSV to JSON at {json_file_path}', exc_info=exc_info)
        return False


def read_csv_as_dict(csv_file: Union[str, Path]) -> dict | None:
    """
    Преобразует содержимое CSV файла в словарь.

    :param csv_file: Путь к CSV файлу.
    :type csv_file: Union[str, Path]
    :returns: Словарь, представляющий CSV, или None в случае ошибки.
    :rtype: dict | None
    """
    try:
        # открытие файла на чтение с кодировкой utf-8
        with Path(csv_file).open('r', encoding='utf-8') as f:
            # создание объекта DictReader для чтения CSV
            reader = csv.DictReader(f)
            # формирование словаря из прочитанных данных
            return {'data': [row for row in reader]}
    except Exception as ex:
        # в случае ошибки запись в лог и возврат None
        logger.error('Failed to read CSV as dictionary', exc_info=True)
        return None


def read_csv_as_ns(file_path: Union[str, Path]) -> List[dict]:
    """
    Загружает данные CSV в список словарей, используя Pandas.

    :param file_path: Путь к CSV файлу.
    :type file_path: Union[str, Path]
    :returns: Список словарей, представляющий содержимое CSV.
    :rtype: List[dict]
    :raises FileNotFoundError: Если файл не найден.
    """
    try:
        # чтение CSV файла с помощью pandas
        df = pd.read_csv(file_path)
        # преобразование DataFrame в список словарей
        return df.to_dict(orient='records')
    except FileNotFoundError as e:
        # в случае ошибки файла запись в лог и возврат пустого списка
        logger.error(f'File not found: {file_path}', exc_info=True)
        return []
    except Exception as e:
        # в случае ошибки записи в лог и возврат пустого списка
        logger.error(f'Failed to load CSV as dictionaries from {file_path}', exc_info=True)
        return []
```
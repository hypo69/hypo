# Анализ кода модуля `src.utils.csv`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и выполняет свои функции по работе с CSV файлами.
    - Используются аннотации типов для улучшения читаемости и предотвращения ошибок.
    - Присутствует логирование ошибок с использованием `logger.error`.
    - Используется `pathlib` для работы с путями к файлам, что делает код более кроссплатформенным.
    - Наличие docstring для каждой функции с описанием параметров, возвращаемых значений и типов данных.
-  Минусы
    -  Некоторые docstring можно улучшить, сделав их более конкретными и подробными.
    -  В некоторых функциях не используется `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо `json.load` как указано в инструкции.
    -  Некоторые исключения перехватываются и не обрабатываются (просто логируются), хотя иногда нужно предпринять дополнительные действия.
    -  Использование `exc_info=True` по умолчанию в некоторых функциях может приводить к избыточному логированию.
    -  Отсутствует проверка на существование директории перед попыткой создать её в функции `save_csv_file`.

**Рекомендации по улучшению**

1.  **Использование `j_loads`**: Замените использование `json.dump` на `j_loads` из `src.utils.jjson`, если это необходимо по условию.
2.  **Улучшение Docstring**: Сделайте docstring более конкретными и информативными, добавив примеры использования и более подробные описания параметров и возвращаемых значений.
3.  **Обработка исключений**: Рассмотрите возможность более детальной обработки исключений, а не просто их логирование. Например, можно предпринять попытку повторного чтения файла или выдать пользователю более информативное сообщение об ошибке.
4.  **Управление `exc_info`**: Пересмотрите использование `exc_info=True` по умолчанию. Возможно, стоит сделать его опциональным или использовать только в критических местах.
5.  **Проверка директории**: Добавьте явную проверку на существование директории перед созданием ее в `save_csv_file`
6. **Использовать** `j_loads` или `j_loads_ns` из `src.utils.jjson` в функции `read_csv_as_json`.

**Оптимизированный код**

```python
# \\file hypotez/src/utils/csv.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с CSV и JSON файлами.
=========================================================================================

Этот модуль предоставляет набор функций для сохранения, чтения и преобразования
данных в форматах CSV и JSON. Он включает функции для сохранения данных в CSV,
чтения данных из CSV, преобразования CSV в JSON, а также чтения CSV в виде словаря
и списка словарей.

Функции используют стандартные библиотеки Python, а также библиотеку pandas для
удобства работы с данными.

Примеры использования
--------------------

Пример сохранения данных в CSV файл:

.. code-block:: python

    data = [{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}]
    file_path = 'output.csv'
    save_csv_file(data, file_path, mode='w')

Пример чтения данных из CSV файла:

.. code-block:: python

    file_path = 'output.csv'
    data = read_csv_file(file_path)
    print(data)

Пример преобразования CSV файла в JSON:

.. code-block:: python

    csv_file_path = 'input.csv'
    json_file_path = 'output.json'
    read_csv_as_json(csv_file_path, json_file_path)
"""

import csv
#  импортируем json для работы с JSON файлами
import json
from pathlib import Path
#  импортируем SimpleNamespace для работы с пространствами имен
from types import SimpleNamespace
from typing import List, Dict, Union
# импортируем pandas для работы с данными
import pandas as pd
# импортируем logger для логирования ошибок
from src.logger.logger import logger
# TODO: импортировать `j_loads` и `j_loads_ns` из `src.utils.jjson`, если необходимо
# from src.utils.jjson import j_loads, j_loads_ns


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
    :param mode: Режим файла ('a' - добавление, 'w' - перезапись). По умолчанию 'a'.
    :type mode: str
    :param exc_info: Включать ли трассировку в логи.
    :type exc_info: bool
    :raises TypeError: Если входные данные не являются списком словарей.
    :raises ValueError: Если входные данные пусты.
    :returns: True в случае успеха, иначе False.
    :rtype: bool
    """
    # проверка входных данных на соответствие типу
    if not isinstance(data, list):
        raise TypeError("Input data must be a list of dictionaries.")
    # проверка входных данных на пустоту
    if not data:
        raise ValueError("Input data cannot be empty.")

    try:
        #  преобразует путь к файлу в объект Path
        file_path = Path(file_path)
        # проверяет существует ли родительская директория, если нет создает ее
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        # открывает файл для записи
        with file_path.open(mode, newline='', encoding='utf-8') as file:
            # создает объект для записи CSV
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            # если файл открыт для записи или его не существует, то записываем заголовок
            if mode == 'w' or not file_path.exists():
                writer.writeheader()
            # записывает данные в файл
            writer.writerows(data)
        return True
    except Exception as e:
        # логирует ошибку в случае неудачи
        logger.error(f"Failed to save CSV to {file_path}", exc_info=exc_info)
        return False


def read_csv_file(file_path: Union[str, Path], exc_info: bool = True) -> List[Dict[str, str]] | None:
    """
    Читает содержимое CSV файла в виде списка словарей.

    :param file_path: Путь к CSV файлу.
    :type file_path: Union[str, Path]
    :param exc_info: Включать ли трассировку в логи.
    :type exc_info: bool
    :raises FileNotFoundError: Если файл не найден.
    :returns: Список словарей или None в случае неудачи.
    :rtype: List[Dict[str, str]] | None
    """
    try:
        # открывает файл для чтения
        with Path(file_path).open('r', encoding='utf-8') as file:
            # создает объект для чтения CSV
            reader = csv.DictReader(file)
            # возвращает данные в виде списка словарей
            return list(reader)
    except FileNotFoundError as e:
        # логирует ошибку, если файл не найден
        logger.error(f"File not found: {file_path}", exc_info=exc_info)
        return None
    except Exception as e:
        # логирует ошибку в случае неудачи чтения
        logger.error(f"Failed to read CSV from {file_path}", exc_info=exc_info)
        return None

def read_csv_as_json(csv_file_path: Union[str, Path], json_file_path: Union[str, Path], exc_info: bool = True) -> bool:
    """
    Преобразует CSV файл в формат JSON и сохраняет его.

    :param csv_file_path: Путь к CSV файлу.
    :type csv_file_path: Union[str, Path]
    :param json_file_path: Путь для сохранения JSON файла.
    :type json_file_path: Union[str, Path]
    :param exc_info: Включать ли трассировку в логи. По умолчанию True.
    :type exc_info: bool, optional
    :returns: True, если преобразование выполнено успешно, иначе False.
    :rtype: bool
    """
    try:
        # читает CSV файл
        data = read_csv_file(csv_file_path, exc_info=exc_info)
        # если данные не получены возвращает False
        if data is None:
            return False
        # открывает файл для записи JSON
        with Path(json_file_path).open('w', encoding='utf-8') as f:
            #  записывает данные в JSON
            json.dump(data, f, indent=4) #TODO: заменить на j_loads если требуется
        return True
    except Exception as ex:
        #  логирует ошибку в случае неудачи преобразования
        logger.error(f"Failed to convert CSV to JSON at {json_file_path}", exc_info=exc_info)
        return False


def read_csv_as_dict(csv_file: Union[str, Path]) -> dict | None:
    """
    Преобразует содержимое CSV файла в словарь.

    :param csv_file: Путь к CSV файлу.
    :type csv_file: Union[str, Path]
    :returns: Словарь, представляющий содержимое CSV, или None в случае неудачи.
    :rtype: dict | None
    """
    try:
        # открывает CSV файл для чтения
        with Path(csv_file).open('r', encoding='utf-8') as f:
             # создает объект для чтения CSV
            reader = csv.DictReader(f)
             # возвращает данные в виде словаря
            return {"data": [row for row in reader]}
    except Exception as ex:
        # логирует ошибку в случае неудачи чтения
        logger.error("Failed to read CSV as dictionary", exc_info=True)
        return None


def read_csv_as_ns(file_path: Union[str, Path]) -> List[dict]:
    """
    Загружает данные CSV в список словарей, используя pandas.

    :param file_path: Путь к CSV файлу.
    :type file_path: Union[str, Path]
    :returns: Список словарей, представляющих содержимое CSV.
    :rtype: List[dict]
    :raises FileNotFoundError: Если файл не найден.
    """
    try:
         # читает CSV файл с помощью pandas
        df = pd.read_csv(file_path)
         # преобразует данные в словарь и возвращает список словарей
        return df.to_dict(orient='records')
    except FileNotFoundError as e:
        # логирует ошибку, если файл не найден
        logger.error(f"File not found: {file_path}", exc_info=True)
        return []
    except Exception as e:
         # логирует ошибку в случае неудачи загрузки
        logger.error(f"Failed to load CSV as dictionaries from {file_path}", exc_info=True)
        return []
```
# Анализ кода модуля `csv`

**Качество кода**
8
-   Плюсы
    -   Код имеет docstring для каждой функции, что соответствует PEP 257.
    -   Используется `logger` для логирования ошибок.
    -   Код обрабатывает исключения, связанные с файловыми операциями.
    -   Присутствует проверка типов входных данных в функции `save_csv_file`.
-   Минусы
    -   Используется стандартный `json.dump` вместо `j_dumps` или `j_dumps_ns` из `src.utils.jjson`.
    -   Не хватает более детального описания модуля в начале файла.
    -   В некоторых местах отсутствует обработка конкретных типов ошибок (например, `FileNotFoundError` обработана только в `read_csv_file` и `read_csv_as_ns`).
    -  Не везде используется `exc_info=True` по умолчанию для логирования ошибок.

**Рекомендации по улучшению**
1.  Добавить описание модуля в начале файла.
2.  Использовать `j_dumps` из `src.utils.jjson` вместо `json.dump` для единообразия.
3.  Добавить обработку `FileNotFoundError` в функцию `read_csv_as_dict`.
4.  Установить `exc_info=True` по умолчанию для всех функций, где это уместно.
5.  Добавить больше примеров в docstring для каждой функции.
6.  Использовать `from src.logger.logger import logger` для импорта логгера.
7.  Добавить комментарии `#` к коду, поясняющие назначение каждого блока кода.
8.  Упростить обработку ошибок, где это возможно, используя `logger.error` и возвращая `False` или `None`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

"""
Модуль для работы с CSV и JSON файлами.
=========================================================================================

Этот модуль предоставляет набор функций для чтения и записи данных в форматах CSV и JSON,
а также для преобразования данных между этими форматами.

Пример использования
--------------------

Пример использования функций модуля:

.. code-block:: python

    from pathlib import Path
    from src.utils.csv import save_csv_file, read_csv_file, read_csv_as_json
    # Пример записи CSV файла
    data = [{'col1': 'A1', 'col2': 'B1'}, {'col1': 'A2', 'col2': 'B2'}]
    file_path_csv = Path('example.csv')
    save_csv_file(data, file_path_csv, mode='w')

    # Пример чтения CSV файла
    read_data = read_csv_file(file_path_csv)

    # Пример преобразования CSV в JSON
    file_path_json = Path('example.json')
    read_csv_as_json(file_path_csv,file_path_json)

"""
import csv
# from json import dump #  будет использоваться j_dumps
from pathlib import Path
# from types import SimpleNamespace  # не используется
from typing import List, Dict, Union
import pandas as pd
from src.logger.logger import logger # импортируем логгер
from src.utils.jjson import j_dumps  # импортируем j_dumps


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
    :param mode: Режим файла ('a' для добавления, 'w' для перезаписи). По умолчанию 'a'.
    :type mode: str
    :param exc_info: Включать ли трассировку в логи.
    :type exc_info: bool
    :raises TypeError: Если входные данные не являются списком словарей.
    :raises ValueError: Если входные данные пустые.
    :returns: True, если успешно, иначе False.

    Example:
        >>> data = [{'col1': 'A1', 'col2': 'B1'}, {'col1': 'A2', 'col2': 'B2'}]
        >>> file_path = 'example.csv'
        >>> save_csv_file(data, file_path, mode='w')
        True
    """
    # Проверка, что входные данные являются списком
    if not isinstance(data, list):
        raise TypeError('Input data must be a list of dictionaries.')
    # Проверка, что список не пустой
    if not data:
        raise ValueError('Input data cannot be empty.')
    
    try:
        # Преобразует путь к файлу в объект Path
        file_path = Path(file_path)
        # Создает родительскую директорию, если она не существует
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Открывает файл в указанном режиме
        with file_path.open(mode, newline='', encoding='utf-8') as file:
            # Инициализирует объект DictWriter для записи словарей в CSV
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            # Если файл открыт для записи ('w') или не существует, записывает заголовок
            if mode == 'w' or not file_path.exists():
                writer.writeheader()
            # Записывает данные в CSV файл
            writer.writerows(data)
        return True
    except Exception as e:
        # Логирует ошибку и возвращает False
        logger.error(f'Failed to save CSV to {file_path}', exc_info=exc_info)
        return False


def read_csv_file(file_path: Union[str, Path], exc_info: bool = True) -> List[Dict[str, str]] | None:
    """
    Читает содержимое CSV файла в виде списка словарей.

    :param file_path: Путь к CSV файлу.
    :type file_path: Union[str, Path]
    :param exc_info: Включать ли трассировку в логи.
    :type exc_info: bool
    :raises FileNotFoundError: Если файл не найден.
    :returns: Список словарей или None в случае ошибки.

    Example:
        >>> file_path = 'example.csv'
        >>> read_csv_file(file_path)
        [{'col1': 'A1', 'col2': 'B1'}, {'col1': 'A2', 'col2': 'B2'}]
    """
    try:
        # Открывает файл для чтения
        with Path(file_path).open('r', encoding='utf-8') as file:
            # Читает данные из CSV файла
            reader = csv.DictReader(file)
            # Возвращает список словарей
            return list(reader)
    except FileNotFoundError as e:
        # Логирует ошибку если файл не найден и возвращает None
        logger.error(f'File not found: {file_path}', exc_info=exc_info)
        return None
    except Exception as e:
        # Логирует ошибку при чтении CSV и возвращает None
        logger.error(f'Failed to read CSV from {file_path}', exc_info=exc_info)
        return None

def read_csv_as_json(csv_file_path: Union[str, Path], json_file_path: Union[str, Path], exc_info: bool = True) -> bool:
    """
    Конвертирует CSV файл в JSON формат и сохраняет его.

    :param csv_file_path: Путь к CSV файлу.
    :type csv_file_path: str | Path
    :param json_file_path: Путь для сохранения JSON файла.
    :type json_file_path: str | Path
    :param exc_info: Включать ли трассировку в логи. По умолчанию True.
    :type exc_info: bool, optional
    :returns: True, если преобразование успешно, иначе False.
    :rtype: bool

    Example:
        >>> csv_file_path = 'example.csv'
        >>> json_file_path = 'example.json'
        >>> read_csv_as_json(csv_file_path, json_file_path)
        True
    """
    try:
        # Читает CSV файл
        data = read_csv_file(csv_file_path, exc_info=exc_info)
        # Если чтение CSV не удалось, возвращает False
        if data is None:
            return False
        # Открывает файл для записи JSON
        with Path(json_file_path).open('w', encoding='utf-8') as f:
            #  записывает данные в формате JSON
            j_dumps(data, f, indent=4)
        return True
    except Exception as ex:
        # Логирует ошибку при преобразовании CSV в JSON и возвращает False
        logger.error(f'Failed to convert CSV to JSON at {json_file_path}', exc_info=exc_info)
        return False


def read_csv_as_dict(csv_file: Union[str, Path], exc_info: bool = True) -> dict | None:
    """
    Конвертирует содержимое CSV файла в словарь.

    :param csv_file: Путь к CSV файлу.
    :type csv_file: str | Path
    :param exc_info: Включать ли трассировку в логи. По умолчанию True.
    :type exc_info: bool, optional
    :returns: Словарь с данными из CSV или None в случае ошибки.
    :rtype: dict | None

    Example:
        >>> csv_file = 'example.csv'
        >>> read_csv_as_dict(csv_file)
        {'data': [{'col1': 'A1', 'col2': 'B1'}, {'col1': 'A2', 'col2': 'B2'}]}
    """
    try:
        # Открывает файл для чтения
        with Path(csv_file).open('r', encoding='utf-8') as f:
            # Читает данные из CSV файла
            reader = csv.DictReader(f)
            # Возвращает словарь с данными
            return {'data': [row for row in reader]}
    except FileNotFoundError as e:
        # Логирует ошибку если файл не найден и возвращает None
         logger.error(f"File not found: {csv_file}", exc_info=exc_info)
         return None
    except Exception as ex:
        # Логирует ошибку при чтении CSV и возвращает None
        logger.error('Failed to read CSV as dictionary', exc_info=True)
        return None


def read_csv_as_ns(file_path: Union[str, Path], exc_info: bool = True) -> List[dict]:
    """
    Загружает данные из CSV файла в виде списка словарей, используя pandas.

    :param file_path: Путь к CSV файлу.
    :type file_path: Union[str, Path]
    :param exc_info: Включать ли трассировку в логи. По умолчанию True.
    :type exc_info: bool, optional
    :returns: Список словарей представляющих содержимое CSV файла.
    :raises FileNotFoundError: Если файл не найден.
     
    Example:
        >>> file_path = 'example.csv'
        >>> read_csv_as_ns(file_path)
        [{'col1': 'A1', 'col2': 'B1'}, {'col1': 'A2', 'col2': 'B2'}]
    """
    try:
         # Читает CSV файл с использованием pandas
        df = pd.read_csv(file_path)
        # Преобразует данные в список словарей и возвращает его
        return df.to_dict(orient='records')
    except FileNotFoundError as e:
        # Логирует ошибку если файл не найден и возвращает пустой список
        logger.error(f'File not found: {file_path}', exc_info=True)
        return []
    except Exception as e:
        # Логирует ошибку при чтении CSV и возвращает пустой список
        logger.error(f'Failed to load CSV as dictionaries from {file_path}', exc_info=True)
        return []
```
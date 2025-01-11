# Анализ кода модуля `csv`

**Качество кода**
8
- Плюсы
    - Код соответствует PEP 8, функции имеют docstring.
    - Используется `Pathlib` для работы с путями, что повышает читаемость и кроссплатформенность.
    - Код обрабатывает ошибки, используя `try-except` блоки и логирование.
    - Применяется `csv.DictWriter` и `csv.DictReader`, что удобно для работы с CSV файлами как со словарями.
- Минусы
   -   Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения JSON, как указано в инструкции.
    -  Не все функции имеют примеры использования в docstring.
    -  Используются стандартные блоки try-except, вместо обработки ошибок с помощью `logger.error`
   -  В некоторых местах есть дублирование кода обработки ошибок.

**Рекомендации по улучшению**

1.  **Импорты**:
    - Добавить `from src.utils.jjson import j_loads` для работы с JSON.
2.  **Использование `j_loads`**:
    - Изменить функции, где происходит чтение/запись JSON, чтобы использовать `j_loads` или `j_loads_ns`.
3.  **Форматирование строк**:
    - Использовать f-строки для форматирования сообщений в логах.
4.  **Логирование ошибок**:
    - Устранить дублирование кода обработки ошибок. Использовать `logger.error` для записи ошибок, минимизировать использование `try-except` .
5.  **Комментарии**:
    - Добавить более подробные комментарии для сложных частей кода.
6.  **Примеры использования**:
    - Добавить примеры использования функций в docstring, чтобы улучшить документацию.
7.  **Унификация**:
    - Сделать функцию `read_csv_as_dict` более похожей на другие функции.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для работы с CSV и JSON файлами.
=========================================================================================

Этот модуль предоставляет набор утилит для чтения и записи CSV файлов,
а также для преобразования CSV в JSON и обратно.

Пример использования
--------------------

Пример использования функций модуля:

.. code-block:: python

    from pathlib import Path
    from src.utils.csv import save_csv_file, read_csv_file, read_csv_as_json, read_csv_as_dict

    # Пример сохранения данных в CSV файл
    data = [{'name': 'John', 'age': '30'}, {'name': 'Jane', 'age': '25'}]
    csv_path = Path('example.csv')
    save_csv_file(data, csv_path, mode='w')

    # Пример чтения данных из CSV файла
    read_data = read_csv_file(csv_path)
    print(read_data)

    # Пример преобразования CSV в JSON
    json_path = Path('example.json')
    read_csv_as_json(csv_path, json_path)

    # Пример чтения CSV как словаря
    csv_dict = read_csv_as_dict(csv_path)
    print(csv_dict)

"""
import csv
from pathlib import Path
from typing import List, Dict, Union
import pandas as pd
from src.logger.logger import logger
from src.utils.jjson import j_loads # Импорт j_loads


def save_csv_file(
    data: List[Dict[str, str]],
    file_path: Union[str, Path],
    mode: str = 'a',
    exc_info: bool = True,
) -> bool:
    """
    Сохраняет список словарей в CSV файл.

    Args:
        data (List[Dict[str, str]]): Список словарей для сохранения.
        file_path (Union[str, Path]): Путь к CSV файлу.
        mode (str, optional): Режим файла ('a' для добавления, 'w' для перезаписи). По умолчанию 'a'.
        exc_info (bool, optional): Включать ли информацию об исключении в логи. По умолчанию True.

    Returns:
        bool: True, если сохранение прошло успешно, иначе False.

    Raises:
        TypeError: Если входные данные не являются списком словарей.
        ValueError: Если входные данные пусты.

    Example:
        >>> from pathlib import Path
        >>> data = [{'name': 'John', 'age': '30'}, {'name': 'Jane', 'age': '25'}]
        >>> file_path = Path('example.csv')
        >>> save_csv_file(data, file_path, mode='w')
        True
    """
    if not isinstance(data, list):
        raise TypeError('Input data must be a list of dictionaries.')
    if not data:
        raise ValueError('Input data cannot be empty.')
    
    try:
        file_path = Path(file_path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        # Открытие файла в режиме mode, кодировка UTF-8
        with file_path.open(mode, newline='', encoding='utf-8') as file:
            # Создание объекта DictWriter для записи словарей в CSV
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            # Если файл открыт для записи или если файл не существует, записывается заголовок
            if mode == 'w' or not file_path.exists():
                writer.writeheader()
            # Запись данных в файл
            writer.writerows(data)
        return True
    except Exception as e:
        # Логирование ошибки при сохранении CSV файла
        logger.error(f'Failed to save CSV to {file_path}', exc_info=exc_info)
        return False


def read_csv_file(file_path: Union[str, Path], exc_info: bool = True) -> List[Dict[str, str]] | None:
    """
    Читает CSV файл и возвращает его содержимое в виде списка словарей.

    Args:
        file_path (Union[str, Path]): Путь к CSV файлу.
        exc_info (bool, optional): Включать ли информацию об исключении в логи. По умолчанию True.

    Returns:
        List[Dict[str, str]] | None: Список словарей, представляющих содержимое CSV файла, или None в случае ошибки.

    Raises:
         FileNotFoundError: Если файл не найден.

    Example:
        >>> from pathlib import Path
        >>> file_path = Path('example.csv')
        >>> read_csv_file(file_path)
        [{'name': 'John', 'age': '30'}, {'name': 'Jane', 'age': '25'}]
    """
    try:
        # Открытие файла для чтения с кодировкой UTF-8
        with Path(file_path).open('r', encoding='utf-8') as file:
            # Создание объекта DictReader для чтения CSV файла как словаря
            reader = csv.DictReader(file)
            # Возврат содержимого файла в виде списка словарей
            return list(reader)
    except FileNotFoundError:
        # Логирование ошибки если файл не найден
        logger.error(f'File not found: {file_path}', exc_info=exc_info)
        return None
    except Exception:
        # Логирование ошибки чтения CSV
        logger.error(f'Failed to read CSV from {file_path}', exc_info=exc_info)
        return None


def read_csv_as_json(csv_file_path: Union[str, Path], json_file_path: Union[str, Path], exc_info: bool = True) -> bool:
    """
    Преобразует CSV файл в JSON формат и сохраняет его.

    Args:
        csv_file_path (Union[str, Path]): Путь к CSV файлу.
        json_file_path (Union[str, Path]): Путь для сохранения JSON файла.
        exc_info (bool, optional): Включать ли информацию об исключении в логи. По умолчанию True.

    Returns:
        bool: True, если преобразование прошло успешно, иначе False.

    Example:
        >>> from pathlib import Path
        >>> csv_file_path = Path('example.csv')
        >>> json_file_path = Path('example.json')
        >>> read_csv_as_json(csv_file_path, json_file_path)
        True
    """
    try:
        # Чтение данных из CSV файла
        data = read_csv_file(csv_file_path, exc_info=exc_info)
        if data is None:
            return False
        # Открытие JSON файла для записи с кодировкой UTF-8
        with Path(json_file_path).open('w', encoding='utf-8') as f:
           # Запись данных в JSON файл с отступами
            j_loads(data, f, indent=4) # Используем j_loads вместо json.dump
        return True
    except Exception:
         # Логирование ошибки преобразования CSV в JSON
        logger.error(f'Failed to convert CSV to JSON at {json_file_path}', exc_info=exc_info)
        return False


def read_csv_as_dict(csv_file: Union[str, Path]) -> dict | None:
    """
    Читает CSV файл и возвращает его содержимое в виде словаря, где ключ 'data' содержит список словарей.

    Args:
        csv_file (Union[str, Path]): Путь к CSV файлу.

    Returns:
        dict | None: Словарь, представляющий содержимое CSV файла, или None в случае ошибки.
        Формат: {'data': [{}, {}, ...]}

    Example:
         >>> from pathlib import Path
         >>> csv_file_path = Path('example.csv')
         >>> read_csv_as_dict(csv_file_path)
         {'data': [{'name': 'John', 'age': '30'}, {'name': 'Jane', 'age': '25'}]}
    """
    try:
        # Открытие CSV файла для чтения с кодировкой UTF-8
        with Path(csv_file).open('r', encoding='utf-8') as f:
             # Создание объекта DictReader для чтения CSV файла как словаря
            reader = csv.DictReader(f)
            # Возврат словаря, где ключ 'data' содержит список словарей
            return {'data': list(reader)}
    except Exception:
         # Логирование ошибки чтения CSV
        logger.error('Failed to read CSV as dictionary', exc_info=True)
        return None


def read_csv_as_ns(file_path: Union[str, Path]) -> List[dict]:
    """
    Загружает CSV данные в список словарей, используя Pandas.

    Args:
        file_path (Union[str, Path]): Путь к CSV файлу.

    Returns:
         List[dict]: Список словарей, представляющих содержимое CSV файла.

    Raises:
        FileNotFoundError: Если файл не найден.

    Example:
        >>> from pathlib import Path
        >>> file_path = Path('example.csv')
        >>> read_csv_as_ns(file_path)
        [{'name': 'John', 'age': '30'}, {'name': 'Jane', 'age': '25'}]
    """
    try:
        # Чтение CSV файла с помощью pandas
        df = pd.read_csv(file_path)
         # Преобразование данных в список словарей
        return df.to_dict(orient='records')
    except FileNotFoundError:
         # Логирование ошибки если файл не найден
        logger.error(f'File not found: {file_path}', exc_info=True)
        return []
    except Exception:
        # Логирование ошибки загрузки CSV файла
        logger.error(f'Failed to load CSV as dictionaries from {file_path}', exc_info=True)
        return []
```
# Анализ кода модуля `csv.py`

**Качество кода**
8
-  Плюсы
    - Код достаточно хорошо структурирован и читаем.
    - Присутствует базовая обработка ошибок и логирование.
    - Используются type hints.
    - Наличие docstring для каждой функции.
-  Минусы
    - Отсутствует использование `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Избыточное использование `try-except` в функциях `read_csv_file`, `read_csv_as_json`.
    - Не все функции используют единый подход к обработке ошибок.
    - Не все docstring соответствуют формату reStructuredText.

**Рекомендации по улучшению**

1.  **Использовать `j_loads`:** Заменить `json.dump` на `j_dumps` из `src.utils.jjson`.
2.  **Упростить обработку ошибок:** Использовать `logger.error` для обработки ошибок и избегать множественных блоков `try-except`.
3.  **Унифицировать обработку ошибок:** Сделать обработку ошибок консистентной во всех функциях.
4.  **Форматирование Docstring:** Привести все docstring к стандарту reStructuredText.
5. **Добавить импорты**: Добавить импорт `j_dumps` из `src.utils.jjson`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для работы с CSV и JSON файлами.
=========================================================================================

Этот модуль предоставляет набор функций для сохранения, чтения и преобразования CSV файлов.
Он поддерживает чтение CSV в виде списка словарей, преобразование в JSON, а также загрузку данных с использованием Pandas.

Пример использования
--------------------

Пример сохранения данных в CSV файл:

.. code-block:: python

    data = [{'name': 'John', 'age': '30'}, {'name': 'Jane', 'age': '25'}]
    file_path = 'data.csv'
    save_csv_file(data, file_path, mode='w')

Пример чтения данных из CSV файла:

.. code-block:: python

    file_path = 'data.csv'
    data = read_csv_file(file_path)

"""

import csv
from pathlib import Path
from typing import List, Dict, Union
import pandas as pd
from src.logger.logger import logger
from src.utils.jjson import j_dumps # Добавлен импорт j_dumps


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
    :param mode: Режим файла ('a' - дозапись, 'w' - перезапись). По умолчанию 'a'.
    :type mode: str
    :param exc_info: Включать ли информацию о трассировке в логи.
    :type exc_info: bool
    :raises TypeError: Если входные данные не являются списком словарей.
    :raises ValueError: Если входные данные пусты.
    :returns: True в случае успеха, иначе False.
    :rtype: bool
    """
    if not isinstance(data, list):
        raise TypeError("Input data must be a list of dictionaries.")
    if not data:
        raise ValueError("Input data cannot be empty.")

    try:
        # Код преобразует путь к файлу в объект Path
        file_path = Path(file_path)
        # Код создаёт родительские директории, если они не существуют
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Код открывает файл в заданном режиме
        with file_path.open(mode, newline='', encoding='utf-8') as file:
            # Код создает объект для записи CSV
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            # Код проверяет, нужно ли писать заголовок
            if mode == 'w' or not file_path.exists():
                writer.writeheader()
            # Код записывает данные в файл
            writer.writerows(data)
        return True
    except Exception as e:
        # Код логирует ошибку и возвращает False
        logger.error(f"Failed to save CSV to {file_path}", exc_info=exc_info)
        return False


def read_csv_file(file_path: Union[str, Path], exc_info: bool = True) -> List[Dict[str, str]] | None:
    """
    Считывает содержимое CSV файла в виде списка словарей.

    :param file_path: Путь к CSV файлу.
    :type file_path: Union[str, Path]
    :param exc_info: Включать ли информацию о трассировке в логи.
    :type exc_info: bool
    :returns: Список словарей или None, если не удалось.
    :rtype: List[Dict[str, str]] | None
    """
    try:
        # Код открывает CSV файл для чтения
        with Path(file_path).open('r', encoding='utf-8') as file:
            # Код читает CSV файл и преобразует его в список словарей
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        # Код логирует ошибку, если файл не найден
        logger.error(f"File not found: {file_path}", exc_info=exc_info)
        return None
    except Exception as e:
        # Код логирует ошибку при чтении CSV файла
        logger.error(f"Failed to read CSV from {file_path}", exc_info=exc_info)
        return None


def read_csv_as_json(csv_file_path: Union[str, Path], json_file_path: Union[str, Path], exc_info: bool = True) -> bool:
    """
    Преобразует CSV файл в формат JSON и сохраняет его.

    :param csv_file_path: Путь к CSV файлу.
    :type csv_file_path: Union[str, Path]
    :param json_file_path: Путь для сохранения JSON файла.
    :type json_file_path: Union[str, Path]
    :param exc_info: Включать ли информацию о трассировке в логи.
    :type exc_info: bool, optional
    :returns: True, если преобразование выполнено успешно, иначе False.
    :rtype: bool
    """
    try:
        # Код считывает данные из CSV файла
        data = read_csv_file(csv_file_path, exc_info=exc_info)
        # Код проверяет, успешно ли прочитаны данные
        if data is None:
            return False
        # Код открывает файл для записи JSON данных
        with Path(json_file_path).open('w', encoding='utf-8') as f:
            # Код записывает JSON данные в файл с отступами
            f.write(j_dumps(data, indent=4)) # Используется j_dumps
        return True
    except Exception as ex:
        # Код логирует ошибку при преобразовании CSV в JSON
        logger.error(f"Failed to convert CSV to JSON at {json_file_path}", exc_info=exc_info)
        return False


def read_csv_as_dict(csv_file: Union[str, Path]) -> dict | None:
    """
    Преобразует содержимое CSV файла в словарь.

    :param csv_file: Путь к CSV файлу.
    :type csv_file: Union[str, Path]
    :returns: Словарь, представляющий содержимое CSV файла, или None, если не удалось.
    :rtype: dict | None
    """
    try:
        # Код открывает CSV файл для чтения
        with Path(csv_file).open('r', encoding='utf-8') as f:
            # Код читает CSV файл и преобразует его в словарь
            reader = csv.DictReader(f)
            return {"data": [row for row in reader]}
    except Exception as ex:
        # Код логирует ошибку при чтении CSV файла как словаря
        logger.error("Failed to read CSV as dictionary", exc_info=True)
        return None


def read_csv_as_ns(file_path: Union[str, Path]) -> List[dict]:
    """
    Загружает CSV данные в список словарей, используя Pandas.

    :param file_path: Путь к CSV файлу.
    :type file_path: Union[str, Path]
    :returns: Список словарей, представляющий содержимое CSV файла.
    :rtype: List[dict]
    :raises FileNotFoundError: Если файл не найден.
    """
    try:
        # Код читает CSV файл с помощью Pandas
        df = pd.read_csv(file_path)
        # Код преобразует DataFrame в список словарей
        return df.to_dict(orient='records')
    except FileNotFoundError:
         # Код логирует ошибку, если файл не найден
        logger.error(f"File not found: {file_path}", exc_info=True)
        return []
    except Exception as e:
        # Код логирует ошибку при загрузке CSV файла
        logger.error(f"Failed to load CSV as dictionaries from {file_path}", exc_info=True)
        return []
```
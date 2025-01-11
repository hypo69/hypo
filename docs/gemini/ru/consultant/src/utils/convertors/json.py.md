# Анализ кода модуля `json.py`

**Качество кода**
7
- Плюсы
    - Код выполняет заявленную функциональность по конвертации JSON в различные форматы.
    - Используются `logger` для логирования ошибок.
    - Присутствует базовая документация для функций.
- Минусы
    - Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Отсутствует документация модуля в формате RST.
    - Не все функции имеют полное описание в формате RST.
    - В `json2xml` и `json2xls` не производится загрузка данных из `json_data` аналогично `json2csv` и `json2ns`, что создает неоднаковость обработки, а `json2xls` использует переменную `file_path`, которая не определена в контексте функции.
    - Отсутствуют проверки типов и обработки ошибок при работе с данными в `json2xml` и `json2xls`.
    - Код можно сделать более консистентным в обработке `json_data` различных типов.
    - Дублирование кода при загрузке JSON из файла.

**Рекомендации по улучшению**
1.  Добавить документацию модуля в формате RST.
2.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения JSON файлов.
3.  Привести код к общему виду для обработки `json_data` всех типов.
4.  Добавить полноценные docstring в формате RST для всех функций.
5.  Исправить использование `file_path` в функции `json2xls`.
6.  Добавить проверки типов и обработки ошибок при работе с данными в `json2xml` и `json2xls`.
7.  Устранить дублирование кода при загрузке JSON из файла.

**Оптимизированный код**

```python
"""
Модуль для конвертации JSON данных в различные форматы.
=========================================================================================

Этот модуль предоставляет функции для конвертации JSON данных в форматы CSV, SimpleNamespace, XML и XLS.

Функции:
    - `json2csv`: Конвертирует JSON данные в формат CSV.
    - `json2ns`: Конвертирует JSON данные в объект SimpleNamespace.
    - `json2xml`: Конвертирует JSON данные в формат XML.
    - `json2xls`: Конвертирует JSON данные в формат XLS.

Пример использования
--------------------

Пример использования функций:

.. code-block:: python

    from pathlib import Path
    from src.utils.convertors.json import json2csv, json2ns, json2xml, json2xls

    json_data = {"key1": "value1", "key2": "value2"}
    csv_file = Path("output.csv")
    xls_file = Path("output.xls")

    json2csv(json_data, csv_file)
    ns_obj = json2ns(json_data)
    xml_data = json2xml(json_data)
    json2xls(json_data, xls_file)
"""
import csv
from types import SimpleNamespace
from pathlib import Path
from typing import List, Dict, Any

# from src.utils.csv import save_csv_file # TODO: fix import path
# from src.utils.jjson import j_dumps # TODO: fix import path
# from src.utils.xls import save_xls_file # TODO: fix import path
from src.utils.convertors.dict import dict2xml
from src.logger.logger import logger
from src.utils.jjson import j_loads, j_loads_ns

def _load_json_data(json_data: str | dict | Path) -> dict | list:
    """
    Загружает JSON данные из строки, словаря или файла.

    Args:
        json_data (str | dict | Path): JSON данные в виде строки, словаря или пути к файлу.

    Returns:
        dict | list: Загруженные JSON данные.

    Raises:
        ValueError: Если тип json_data не поддерживается.
        Exception: Если не удается прочитать JSON из файла или строки.
    """
    if isinstance(json_data, dict):
        return json_data
    elif isinstance(json_data, str):
        try:
            return j_loads(json_data)
        except Exception as ex:
            logger.error(f'Ошибка при загрузке JSON из строки: {json_data}', exc_info=ex)
            raise
    elif isinstance(json_data, Path):
        try:
            with open(json_data, 'r', encoding='utf-8') as json_file:
                return j_loads(json_file.read())
        except Exception as ex:
             logger.error(f'Ошибка при загрузке JSON из файла: {json_data}', exc_info=ex)
             raise
    else:
        raise ValueError('Неподдерживаемый тип для json_data')


def json2csv(json_data: str | list | dict | Path, csv_file_path: str | Path) -> bool:
    """
    Конвертирует JSON данные или JSON файл в формат CSV с разделителем запятая.

    Args:
        json_data (str | list | dict | Path): JSON данные в виде строки, списка словарей или пути к JSON файлу.
        csv_file_path (str | Path): Путь к CSV файлу для записи.

    Returns:
        bool: True, если конвертация прошла успешно, False в противном случае.

    Raises:
        ValueError: Если тип json_data не поддерживается.
        Exception: Если не удается прочитать JSON или записать CSV.
    """
    try:
        # Загрузка JSON данных
        data = _load_json_data(json_data)

        # Ensure data is a list of dictionaries
        if isinstance(data, dict):
            data = [data]
        
        # Сохранение CSV файла
        save_csv_file(data, csv_file_path) # TODO: fix import path
        return True
    except Exception as ex:
        logger.error('Ошибка при конвертации JSON в CSV', exc_info=ex)
        return False


def json2ns(json_data: str | dict | Path) -> SimpleNamespace:
    """
    Конвертирует JSON данные или JSON файл в объект SimpleNamespace.

    Args:
        json_data (str | dict | Path): JSON данные в виде строки, словаря или пути к JSON файлу.

    Returns:
        SimpleNamespace: JSON данные, представленные в виде объекта SimpleNamespace.
    
    Raises:
        ValueError: Если тип json_data не поддерживается.
        Exception: Если не удается прочитать JSON.
    """
    try:
         # Загрузка JSON данных
        data = _load_json_data(json_data)
        return SimpleNamespace(**data)
    except Exception as ex:
        logger.error('Ошибка при конвертации JSON в SimpleNamespace', exc_info=ex)
        return None


def json2xml(json_data: str | dict | Path, root_tag: str = 'root') -> str:
    """
    Конвертирует JSON данные или JSON файл в формат XML.

    Args:
        json_data (str | dict | Path): JSON данные в виде строки, словаря или пути к JSON файлу.
        root_tag (str, optional): Корневой тег для XML. По умолчанию 'root'.

    Returns:
        str: XML строка.

    Raises:
         ValueError: Если тип json_data не поддерживается.
         Exception: Если не удается прочитать JSON или преобразовать в XML.
    """
    try:
        # Загрузка JSON данных
        data = _load_json_data(json_data)
        # Преобразование в XML
        return dict2xml(data, root_tag=root_tag)
    except Exception as ex:
         logger.error('Ошибка при конвертации JSON в XML', exc_info=ex)
         return None


def json2xls(json_data: str | list | dict | Path, xls_file_path: str | Path) -> bool:
    """
    Конвертирует JSON данные или JSON файл в формат XLS.

    Args:
        json_data (str | list | dict | Path): JSON данные в виде строки, списка словарей или пути к JSON файлу.
        xls_file_path (str | Path): Путь к XLS файлу для записи.

    Returns:
        bool: True, если конвертация прошла успешно, False в противном случае.

    Raises:
         ValueError: Если тип json_data не поддерживается.
         Exception: Если не удается прочитать JSON или записать XLS.
    """
    try:
         # Загрузка JSON данных
        data = _load_json_data(json_data)
        # Сохранение XLS файла
        save_xls_file(data, xls_file_path) # TODO: fix import path
        return True
    except Exception as ex:
        logger.error('Ошибка при конвертации JSON в XLS', exc_info=ex)
        return False
```
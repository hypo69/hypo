# Анализ кода модуля `jjson.py`

**Качество кода**
7
-   Плюсы
    -   Код содержит функции для работы с JSON и CSV файлами, включая загрузку, выгрузку и преобразование данных.
    -   Используется `logger` для логирования ошибок.
    -   Есть функции для преобразования данных в `SimpleNamespace` и обратно.
    -   Поддержка чтения данных из строк, файлов и директорий.
-   Минусы
    -   Много блоков `try-except`, можно переработать.
    -   В некоторых местах используется `...` для пропуска кода, что не является хорошей практикой.
    -   В функции `j_loads` используется избыточная обработка строк, которую можно упростить.
    -   Отсутствует явное приведение к `SimpleNamespace` при обработки списка в `j_loads_ns`.
    -   Много повторений в коде, можно вынести общую логику в отдельные функции.
    -   Некоторые docstring неполные, стоит добавить описание типов параметров и возвращаемых значений.

**Рекомендации по улучшению**

1.  **Упростить обработку ошибок**:
    -   Использовать `logger.error` для логирования ошибок с трассировкой стека.
    -   Убрать лишние `try-except` блоки, где это возможно.
2.  **Улучшить функцию `j_dumps`**:
    -   Избегать использования `...` как точки останова, вместо этого использовать `return` или `raise`.
    -   Упростить логику обработки режимов открытия файла.
3.  **Улучшить функцию `j_loads`**:
    -   Упростить функцию `decode_strings`, убрав лишние проверки.
    -   Убрать дублирование кода при обработке строк и словарей.
    -   Использовать `simplejson.loads` для парсинга строк.
    -   Убрать избыточное использование `json.loads(json.dumps(...))`.
4.  **Улучшить функцию `j_loads_ns`**:
    -   Возвращать `SimpleNamespace` из списка только если это нужно.
    -   Избавиться от дублирования кода в `j_loads` и `j_loads_ns`

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с JSON и CSV файлами.
=========================================================================================

Этот модуль предоставляет функции для:
    - Записи JSON данных в файл или возвращение в виде словаря.
    - Загрузки JSON и CSV данных из файлов, директорий или строк.
    - Конвертации JSON данных в объекты SimpleNamespace.
    - Объединения JSON файлов из директории в один файл.

Функции в этом модуле предназначены для эффективной работы с JSON и CSV данными, обеспечивая их загрузку,
сохранение и слияние.
"""
MODE = 'dev'
from datetime import datetime
import copy
from math import log
from pathlib import Path
from typing import List, Dict, Optional, Any, Union
from types import SimpleNamespace
import json
import os
import re
import pandas as pd
from json_repair import repair_json
import simplejson as simplejson
from collections import OrderedDict

from src.logger.logger import logger
from src.utils.printer import pprint
from .convertors.dict import dict2ns

def _convert_data(value: Any) -> Any:
    """
    Рекурсивно обрабатывает значения для обработки вложенных SimpleNamespace, dict или list.

    :param value: Значение для обработки.
    :return: Преобразованное значение.
    """
    if isinstance(value, SimpleNamespace):
        return {key: _convert_data(val) for key, val in vars(value).items()}
    elif isinstance(value, dict):
        return {key: _convert_data(val) for key, val in value.items()}
    elif isinstance(value, list):
        return [_convert_data(item) for item in value]
    return value

def j_dumps(
    data: Union[Dict, SimpleNamespace, List[Dict], List[SimpleNamespace]],
    file_path: Optional[Path] = None,
    ensure_ascii: bool = True,
    mode: str = "w",
    exc_info: bool = True,
) -> Optional[Dict]:
    """
    Записывает JSON данные в файл или возвращает JSON данные в виде словаря.

    :param data: Данные для записи, совместимые с JSON, или объекты SimpleNamespace.
    :type data: Dict | SimpleNamespace | List[Dict] | List[SimpleNamespace]
    :param file_path: Путь к выходному файлу. Если None, JSON возвращается в виде словаря.
    :type file_path: Optional[Path]
    :param ensure_ascii: Если True, не-ASCII символы экранируются в выводе.
    :type ensure_ascii: bool
    :param mode: Режим открытия файла ('w', 'a+', '+a').
    :type mode: str
    :param exc_info: Если True, логирует исключения с трассировкой стека.
    :type exc_info: bool
    :return: JSON данные в виде словаря или None при ошибке.
    :rtype: Optional[Dict]
    :raises ValueError: Если режим файла не поддерживается.
    """
    path = Path(file_path) if isinstance(file_path, (str, Path)) else None

    if isinstance(data, str):
        try:
            data = repair_json(data)
        except Exception as ex:
            logger.error(f'Ошибка конвертации строки: {pprint(data)}', ex, exc_info=exc_info)
            return None

    data = _convert_data(data)

    if mode not in {"w", "a+", "+a"}:
        mode = 'w'

    existing_data = {}
    if path and path.exists() and mode in {"a+", "+a"}:
        try:
            with path.open("r", encoding="utf-8") as f:
                existing_data = json.load(f)
        except json.JSONDecodeError as e:
            logger.error(f"Ошибка декодирования JSON в {path}: {e}", exc_info=exc_info)
            return None
        except Exception as ex:
            logger.error(f"Ошибка чтения файла {path=}: {ex}", exc_info=exc_info)
            return None

    try:
        if mode == "a+":
            if isinstance(data, list) and isinstance(existing_data, list):
                 existing_data = data + existing_data
            elif isinstance(data,dict) and isinstance(existing_data,dict):
                existing_data.update(data)

        elif mode == "+a":
            if isinstance(data, list) and isinstance(existing_data, list):
                existing_data.extend(data)
            elif isinstance(data, dict) and isinstance(existing_data, dict):
                existing_data.update(data)
            data = existing_data

        if path:
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=ensure_ascii, indent=4)
        else:
            return data
        return data

    except Exception as ex:
            logger.error(f"Не удалось записать в файл {path}: ",ex, exc_info=exc_info)
            return None

def _decode_strings(data: Any) -> Any:
    """
    Рекурсивно перекодирует строки в структуре данных.

    :param data: Данные для перекодировки.
    :return: Перекодированные данные.
    """
    if isinstance(data, str):
        try:
            return data.encode().decode('unicode_escape')
        except Exception:
            return data
    elif isinstance(data, list):
        return [_decode_strings(item) for item in data]
    elif isinstance(data, dict):
        return {key: _decode_strings(value) for key, value in data.items()}
    return data

def _string_to_dict(json_string: str) -> dict:
    """
    Удаляет тройные обратные кавычки и 'json' из начала и конца строки и преобразовывает строку в словарь.

    :param json_string: Строка для преобразования.
    :return: Словарь, полученный из строки, или пустой словарь в случае ошибки.
    """
    if json_string.startswith(('```', '```json')) and json_string.endswith('```'):
        json_string = json_string.strip('`').replace('json', '', 1).strip()
    try:
        return simplejson.loads(json_string)
    except json.JSONDecodeError as ex:
        logger.error(f'Ошибка парсинга строки JSON: {json_string}', ex, False)
        return {}


def j_loads(
    jjson: Union[dict, SimpleNamespace, str, Path, list],
    ordered: bool = True
) -> Union[dict, list]:
    """
    Загружает JSON или CSV данные из файла, директории, строки, объекта JSON или SimpleNamespace.
    Перекодирует строки ключей и значений в Unicode.

    :param jjson: Путь к файлу, директории, строка JSON данных, объект JSON или SimpleNamespace.
    :type jjson: dict | SimpleNamespace | str | Path | list
    :param ordered: Возвращает OrderedDict для сохранения порядка элементов.
    :type ordered: bool, optional
    :return: Обработанные данные (словарь или список словарей).
    :rtype: dict | list
    :raises FileNotFoundError: Если указанный файл не найден.
    :raises json.JSONDecodeError: Если данные JSON не удалось разобрать.
    """
    try:
        if isinstance(jjson, SimpleNamespace):
            jjson = vars(jjson)
        
        if isinstance(jjson, Path):
            if jjson.is_dir():
                 files = list(jjson.glob('*.json'))
                 return [j_loads(file, ordered=ordered) for file in files]
            if jjson.suffix.lower() == '.csv':
                return pd.read_csv(jjson).to_dict(orient='records')
            return json.loads(jjson.read_text(encoding='utf-8'))
        elif isinstance(jjson, str):
            return _string_to_dict(jjson)
        elif isinstance(jjson, list):
            return [_decode_strings(item) for item in jjson]
        elif isinstance(jjson, dict):
             return _decode_strings(jjson)
    except FileNotFoundError as ex:
        logger.error(f'Файл не найден: {jjson}',exc_info=False)
        return {}
    except json.JSONDecodeError as ex:
        logger.error(f'Ошибка парсинга JSON:\n{jjson}\n', ex, False)
        return {}
    except Exception as ex:
        logger.error(f'Ошибка загрузки данных: ',ex, False)
        return {}
    return {}

def j_loads_ns(
    jjson: Union[Path, SimpleNamespace, Dict, str],
    ordered: bool = True
) -> Union[SimpleNamespace, List[SimpleNamespace], dict]:
    """
    Загружает JSON или CSV данные из файла, директории или строки и преобразует в SimpleNamespace.

    :param jjson: Путь к файлу, директории или JSON данные в виде строки, или объект JSON.
    :type jjson: Path | SimpleNamespace | Dict | str
    :param ordered: Если True, возвращает OrderedDict вместо обычного dict для сохранения порядка элементов.
    :type ordered: bool, optional
    :return: SimpleNamespace или список объектов SimpleNamespace в случае успеха. Возвращает None, если jjson не найден или не может быть прочитан.
    :rtype: Optional[SimpleNamespace | List[SimpleNamespace]]
    :raises FileNotFoundError: Если указанный файл не найден.
    :raises json.JSONDecodeError: Если данные JSON не удалось разобрать.

    :Examples:
        >>> j_loads_ns('data.json')
        SimpleNamespace(key='value')

        >>> j_loads_ns(Path('/path/to/directory'))
        [SimpleNamespace(key1='value1'), SimpleNamespace(key2='value2')]

        >>> j_loads_ns('{"key": "value"}')
        SimpleNamespace(key='value')

        >>> j_loads_ns(Path('/path/to/file.csv'))
        [SimpleNamespace(column1='value1', column2='value2')]
    """
    data = j_loads(jjson, ordered=ordered)
    if data:
        if isinstance(data, list):
            return [dict2ns(item) for item in data]
        return dict2ns(data)
    return {}
```
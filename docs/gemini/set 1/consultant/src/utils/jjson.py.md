# Анализ кода модуля `jjson.py`

**Качество кода: 8/10**
-  Плюсы
    - Код содержит docstring для каждой функции, что соответствует требованиям.
    - Используется `logger` для логирования ошибок, что является хорошей практикой.
    - Код разделен на функции для лучшей читаемости и поддержки.
    - Присутствует обработка различных типов входных данных, включая строки, файлы и директории.
    - Используются `Path` для работы с файловыми путями, что делает код более кроссплатформенным.
-  Минусы
    - В некоторых местах используется стандартный `try-except` блок без подробного логирования.
    - Некоторые docstring не полностью соответствуют reStructuredText (RST) стандарту.
    - Есть избыточное использование `...` как точек останова.
    - Некоторые комментарии после `#` можно сделать более информативными.
    - В `j_loads` дублируется код декодирования.
    - В `j_loads` используется `simplejson` но не везде.
    - В `j_loads` используется `json.loads(json.dumps(data))` можно упростить.

**Рекомендации по улучшению**
1. **Унификация обработки ошибок**: Заменить стандартные `try-except` блоки на использование `logger.error` с передачей информации об ошибке.
2. **Доработка docstring**:  
   -  Привести все docstring к формату reStructuredText (RST).
   -  Добавить более подробное описание параметров и возвращаемых значений.
3. **Устранение `...`**: Заменить `...` на более конкретные действия, например, `return None` или `continue`.
4. **Улучшение комментариев**: Сделать комментарии после `#` более информативными, объясняя логику кода.
5. **Упрощение `j_loads`**:
    - Устранить дублирование кода декодирования.
    - Привести к единообразному использованию `simplejson`.
    - Убрать избыточное `json.loads(json.dumps(data))`.
6.  **Унификация декодирования**: Вынести декодирование в отдельную функцию, для избежания дублирования
7.  **Убрать лишние импорты**: в коде присутствуют лишние импорты.
8.  **Обработка исключений**: в `j_dumps` для `mode in {"a+", "+a"}` добавить `exc_info=exc_info`
9. **Переименовать переменные**: `_j` на более информативное имя.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с JSON и CSV файлами.
=========================================================================================

Этот модуль предоставляет функции для:
- Сохранения JSON данных в файл или получения в виде словаря.
- Загрузки JSON и CSV данных из файлов, директорий или строк.
- Преобразования загруженных JSON данных в объекты SimpleNamespace.
- Объединения JSON файлов из директории в один JSON файл.
- Разбора Markdown строк в формат JSON.

Функции в этом модуле обрабатывают различные аспекты работы с JSON и CSV данными, обеспечивая эффективную загрузку, сохранение и объединение данных.
"""

from datetime import datetime
import copy
from math import log
from pathlib import Path
from typing import List, Dict, Optional, Any
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
# from .convertors.ns import ns2dict


def j_dumps(
    data: Dict | SimpleNamespace | List[Dict] | List[SimpleNamespace],
    file_path: Optional[Path] = None,
    ensure_ascii: bool = True,
    mode: str = "w",
    exc_info: bool = True,
) -> Optional[Dict]:
    """
    Сохраняет JSON данные в файл или возвращает JSON данные в виде словаря.

    :param data: JSON-совместимые данные или объекты SimpleNamespace для сохранения.
    :type data: Dict | SimpleNamespace | List[Dict] | List[SimpleNamespace]
    :param file_path: Путь к выходному файлу. Если None, возвращает JSON как словарь.
    :type file_path: Optional[Path], optional
    :param ensure_ascii: Если True, экранирует не-ASCII символы в выводе.
    :type ensure_ascii: bool, optional
    :param mode: Режим открытия файла ('w', 'a+', '+a').
    :type mode: str, optional
    :param exc_info: Если True, логирует исключения с трассировкой.
    :type exc_info: bool, optional
    :raises ValueError: Если режим файла не поддерживается.
    :return: JSON данные как словарь если успешно, или None если произошла ошибка.
    :rtype: Optional[Dict]
    """
    path = Path(file_path) if isinstance(file_path, (str, Path)) else None
    
    # Если данные пришли в виде строки - код попытается распарсить ее через `repair_json()`
    if isinstance(data, str):
        try:
            data = repair_json(data)
        except Exception as ex:
            logger.error(f'Ошибка конвертации строки: {pprint(data)}', ex, exc_info=False)
            return None

    def _convert(value: Any) -> Any:
        """
        Рекурсивно обрабатывает значения для работы с вложенными SimpleNamespace, dict или list.

        :param value: Значение для обработки.
        :type value: Any
        :return: Преобразованное значение.
        :rtype: Any
        """
        if isinstance(value, SimpleNamespace):
            return {key: _convert(val) for key, val in vars(value).items()}
        elif isinstance(value, dict):
            return {key: _convert(val) for key, val in value.items()}
        elif isinstance(value, list):
            return [_convert(item) for item in value]
        return value

    # Конвертация входных данных в валидный словарь `dict`
    data = _convert(data)

    # если указан неверный режим записи в файл - будет установлен 'w'
    if mode not in {"w", "a+", "+a"}:
        mode = 'w'
    
    # Чтение существующих данных из файла (если файл существует и режим 'a+' или '+a')
    existing_data = {}
    if path and path.exists() and mode in {"a+", "+a"}:
        try:
            with path.open("r", encoding="utf-8") as f:
                existing_data = json.load(f)
        except json.JSONDecodeError as e:
            logger.error(f"Ошибка декодирования существующего JSON в {path}: {e}", exc_info=exc_info)
            return None
        except Exception as ex:
            logger.error(f"Ошибка чтения {path=}: {ex}", exc_info=exc_info)
            return None

    # Обработка данных в зависимости от режима
    if mode == "a+":
        # Присоединение новых данных в начало существующего словаря
        try:
            if isinstance(data, list) and isinstance(existing_data, list):
                existing_data = data + existing_data
            else:
                existing_data.update(data)
        except Exception as ex:
            logger.error(ex, exc_info=exc_info)
            return None

    elif mode == "+a":
        # Присоединение новых данных в конец существующего словаря
        try:
            if isinstance(data, list) and isinstance(existing_data, list):
                existing_data.extend(data)
            else:
                existing_data.update(data)
            data = existing_data
        except Exception as ex:
            logger.error(ex, exc_info=exc_info)
            return None

    # Режим 'w' - перезаписывает файл новыми данными
    if path:
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=ensure_ascii, indent=4)
        except Exception as ex:
            logger.error(f"Ошибка записи в {path}: ", ex, exc_info=exc_info)
            return None
    else:
        return data

    return data


def _decode_strings(data: Any) -> Any:
    """
    Рекурсивно декодирует строки в структуре данных.

    :param data: Данные для декодирования.
    :type data: Any
    :return: Декодированные данные.
    :rtype: Any
    """
    if isinstance(data, str):
        try:
            return data.encode().decode('unicode_escape')
        except Exception:
            return data
    elif isinstance(data, list):
        return [_decode_strings(item) for item in data]
    elif isinstance(data, dict):
        return {
            _decode_strings(key): _decode_strings(value) for key, value in data.items()
        }
    return data

def j_loads(
    jjson: dict | SimpleNamespace | str | Path | list,
    ordered: bool = True,
) -> dict | list:
    """
    Загружает JSON или CSV данные из файла, директории, строки или объекта JSON.
    Перекодирует строки ключей и значений в Unicode.

    :param jjson: Путь к файлу, директории, строка JSON данных, объект JSON или SimpleNamespace.
    :type jjson: dict | SimpleNamespace | str | Path | list
    :param ordered: Возвращает OrderedDict для сохранения порядка элементов.
    :type ordered: bool, optional
    :raises FileNotFoundError: Если указанный файл не найден.
    :raises json.JSONDecodeError: Если данные JSON не удалось разобрать.
    :return: Обработанные данные (словарь или список словарей).
    :rtype: dict | list
    """


    def string2dict(json_string: str) -> dict:
        """
        Удаляет тройные обратные кавычки и 'json' из начала и конца строки.
        
        :param json_string: Строка для обработки.
        :type json_string: str
        :return: Словарь, полученный из строки.
        :rtype: dict
        """
        if json_string.startswith(('```', '```json')) and json_string.endswith('```'):
            json_string = json_string.strip('`').replace('json', '', 1).strip()
        try:
            json_data = simplejson.loads(json_string)
        except json.JSONDecodeError as ex:
            logger.error(f'Ошибка парсинга строки JSON:\\n {json_string}', ex, exc_info=False)
            return {}
        return json_data

    # Основная обработка данных
    try:
        if isinstance(jjson, SimpleNamespace):
            jjson = vars(jjson)

        if isinstance(jjson, Path):
            if jjson.is_dir():
                files = list(jjson.glob('*.json'))
                return [j_loads(file, ordered=ordered) for file in files]
            if jjson.suffix.lower() == '.csv':
                return pd.read_csv(jjson).to_dict(orient='records')
            return simplejson.loads(jjson.read_text(encoding='utf-8'))
        elif isinstance(jjson, str):
            return string2dict(jjson)
        elif isinstance(jjson, list):
            return [_decode_strings(item) for item in jjson]
        elif isinstance(jjson, dict):
           return _decode_strings(jjson)
    except FileNotFoundError as ex:
        logger.error(f'Файл не найден: {jjson}', exc_info=False)
        return {}
    except json.JSONDecodeError as ex:
        logger.error(f'Ошибка парсинга JSON:\\n{jjson}\\n', ex, exc_info=False)
        return {}
    except Exception as ex:
        logger.error(f'Ошибка загрузки данных: ', ex, exc_info=False)
        return {}

    return {}


def j_loads_ns(
    jjson: Path | SimpleNamespace | Dict | str,
    ordered: bool = True,
) -> SimpleNamespace:
    """
    Загружает JSON или CSV данные из файла, директории или строки и преобразует в SimpleNamespace.

    :param jjson: Путь к файлу, директории или строка JSON данных.
    :type jjson: Path | SimpleNamespace | Dict | str
    :param ordered: Возвращает OrderedDict для сохранения порядка элементов.
    :type ordered: bool, optional
    :return: SimpleNamespace или список объектов SimpleNamespace.
    :rtype: SimpleNamespace | List[SimpleNamespace]
    
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
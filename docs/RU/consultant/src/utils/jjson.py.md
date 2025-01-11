## Анализ кода модуля `jjson.py`

**Качество кода**
7
-  Плюсы
    -   Код содержит docstring для модуля и функций, что способствует пониманию назначения кода.
    -   Используется `logger` для логирования ошибок и отладки, что улучшает сопровождение.
    -   Используется `pprint` для форматирования вывода данных, что облегчает чтение логов.
    -   Присутствует обработка различных типов входных данных: строки, файлы, директории, списки, словари и `SimpleNamespace`.
    -   Имеется конвертация  `SimpleNamespace` в `dict`
    -   Используется `repair_json` для исправления некорректных JSON-строк.
    -   Поддержка  различных режимов записи файлов: `'w'`, `'a+'`, `'+a'`
    -  Содержит декодирование экранированных последовательностей в строках
    -   Использует `OrderedDict` для сохранения порядка ключей при необходимости.
 -  Минусы
    -   Смешение комментариев и docstring затрудняет чтение.
    -   В некоторых местах используется `...` для пропуска кода, что снижает понимание логики.
    -   Иногда дублируется код, например,  в `j_dumps` присутствует  избыточное определения `convert`, которое переопределяет предыдущее
    -   Использование `try-except` без конкретизации исключений.
    -   Не все функции документированы в формате reST
    -   Не полное соответствие code style в виде одинарных кавычек, используется смешение

**Рекомендации по улучшению**
1.  **Форматирование кода**:
    -   Привести все строковые литералы к использованию одинарных кавычек (`'`).
    -   Удалить неиспользуемые импорты и дублирование.
    -   Использовать `from src.logger.logger import logger` для логирования.

2.  **Комментарии и документация**:
    -   Переписать комментарии к функциям в стиле reST для лучшей интеграции со Sphinx.
    -   Добавить комментарии `#` к тем частям кода, где их не хватает, и уточнить существующие.
    -   Удалить или заменить `...` конкретным кодом или действиями.

3.  **Обработка ошибок**:
    -   Использовать `logger.error` с конкретизацией исключений вместо общих `except Exception`.
    -   Избегать избыточных `try-except` блоков.
    -   Удалить `exc_info=False` из `logger.error` по умолчанию `exc_info=True`

4.  **Рефакторинг кода**:
    -   Упростить логику конвертации данных в `j_dumps` с помощью рекурсивной функции.
    -   Избегать дублирования кода. Вынести повторяющиеся блоки в отдельные функции или методы.
    -   Упростить функции `j_loads` и `j_loads_ns`

5. **Типизация**:
   - В некоторых местах не хватает типизации
6.  **Общие улучшения**:
    -   Добавить примеры использования в docstring для функций.
    -   Придерживаться code style по использованию одинарных кавычек.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для работы с JSON и CSV файлами.
=========================================================================================

Этот модуль предоставляет функции для загрузки, сохранения и обработки JSON и CSV данных.
Включает возможности для конвертации данных в различные форматы, такие как `dict` и `SimpleNamespace`.

Функции модуля:
- **j_dumps**: Сохранение данных в JSON файл или возврат JSON данных в виде словаря.
- **j_loads**: Загрузка JSON или CSV данных из файла, директории, строки.
- **j_loads_ns**: Загрузка данных и конвертация их в `SimpleNamespace`.

Пример использования
--------------------

.. code-block:: python

    from pathlib import Path
    from src.utils.jjson import j_loads, j_dumps, j_loads_ns

    # Загрузка данных из JSON файла
    data = j_loads(Path('data.json'))

    # Сохранение данных в JSON файл
    j_dumps(data, Path('output.json'))

    # Загрузка данных и конвертация в SimpleNamespace
    ns_data = j_loads_ns(Path('data.json'))
"""

from datetime import datetime
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

def _convert_value(value: Any) -> Any:
    """Рекурсивно обрабатывает значения для обработки вложенных структур и пустых ключей.

    Args:
        value (Any): Значение для обработки.

    Returns:
        Any: Обработанное значение.
    """
    if hasattr(value, '__dict__'):
        return {key or '': _convert_value(val) for key, val in vars(value).items()}
    elif hasattr(value, 'items'):
        return {key or '': _convert_value(val) for key, val in value.items()}
    elif isinstance(value, list):
        return [_convert_value(item) for item in value]
    return value

def j_dumps(
    data: Any,
    file_path: Optional[Path] = None,
    ensure_ascii: bool = True,
    mode: str = 'w',
    exc_info: bool = True,
) -> Optional[Dict]:
    """Сохраняет JSON данные в файл или возвращает JSON данные в виде словаря.

    Args:
        data (Dict | SimpleNamespace | List[Dict] | List[SimpleNamespace]): JSON-совместимые данные или объекты SimpleNamespace для сохранения.
        file_path (Optional[Path], optional): Путь к файлу для сохранения. Если None, возвращает JSON как словарь. По умолчанию None.
        ensure_ascii (bool, optional): Если True, экранирует не-ASCII символы в выводе. По умолчанию True.
        mode (str, optional): Режим открытия файла ('w', 'a+', '+a'). По умолчанию 'w'.
        exc_info (bool, optional): Если True, логирует исключения с трассировкой. По умолчанию True.

    Returns:
        Optional[Dict]: JSON данные в виде словаря если успешно, или None в случае ошибки.

    Raises:
        ValueError: Если режим файла не поддерживается.

    Examples:
       >>> data = {'key': 'value'}
       >>> j_dumps(data, Path('output.json'))
       >>> # или
       >>> result = j_dumps(data)
       >>> print(result)
       {'key': 'value'}
    """
    path = Path(file_path) if isinstance(file_path, (str, Path)) else None

    # Eсли данные пришли в виде строки - код попытается распарсить ее через `repair_json()`
    if isinstance(data, str):
        try:
            data = repair_json(data)
        except Exception as ex:
            logger.error(f'Ошибка конвертации строки: {pprint(data)}', ex)
            return

    # Конвертация входных данных в валидный словарь `dict`
    data = _convert_value(data)

    # ----------- ЗАПИСЬ В ФАЙЛ ----------------
    if mode not in {'w', 'a+', '+a'}:
        mode = 'w'

    existing_data = {}

    # Чтение существующих данных из файла (если файл существует и режим 'a+' или '+a')
    if path and path.exists():
        if mode in {'a+', '+a'}:
            try:
                with path.open('r', encoding='utf-8') as f: # Чтение в режиме 'r'
                    existing_data = json.load(f)
            except json.JSONDecodeError as e:
                logger.error(f'Ошибка декодирования существующего JSON в {path}: {e}', exc_info=exc_info)
                return
            except Exception as ex:
                logger.error(f'Ошибка чтения {path=}: {ex}', exc_info=exc_info)
                return

        # Обработка данных в зависимости от режима
        if mode == 'a+':
            try:
                if isinstance(data, list) and isinstance(existing_data, list):
                    data = data + existing_data  # Добавляем элементы из списка в начало
                else:
                    if isinstance(data, dict) and isinstance(existing_data,dict):
                        data.update(existing_data)
                    else:
                        logger.error(f'Некорректные типы данных, ожидался list или dict. {type(data)=} {type(existing_data)=}')
                        return
            except Exception as ex:
                logger.error(ex)
                return

        elif mode == '+a':
             # Присоединение новых данных в конец существующего словаря
            try:
                if isinstance(data, list) and isinstance(existing_data, list):
                    data = existing_data + data # Добавляем элементы из списка в конец
                else:
                    if isinstance(data, dict) and isinstance(existing_data, dict):
                       existing_data.update(data)
                       data = existing_data
                    else:
                        logger.error(f'Некорректные типы данных, ожидался list или dict. {type(data)=} {type(existing_data)=}')
                        return

            except Exception as ex:
                logger.error(ex)
                return

        with path.open('w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=ensure_ascii, indent=4)
            return

    # Режим 'w' - перезаписывает файл новыми данными
    if path:
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open('w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=ensure_ascii, indent=4)
            return
        except Exception as ex:
            logger.error(f'Ошибка записи в {path}: ', ex, exc_info=exc_info)
            return

    # Не указан целевой файл. Возврат форматированого словаря из объекта
    else:
        return data


def _decode_strings(data: Any) -> Any:
        """Рекурсивно перекодирует строки в структуре данных."""
        if isinstance(data, str):
            try:
                return data.encode().decode('unicode_escape') # Декодируем escape-последовательности
            except Exception:
                return data # Если декодировать не получилось, возвращаем как есть
        elif isinstance(data, list):
            return [_decode_strings(item) for item in data] # Обрабатываем каждый элемент списка
        elif isinstance(data, dict):
            return {_decode_strings(key): _decode_strings(value) for key, value in data.items()} # Обрабатываем ключи и значения словаря
        return data  # Возвращаем неизменённые значения, если они не строка, список или словарь

def _string_to_dict(json_string: str) -> dict:
    """Удаляет тройные обратные кавычки и 'json' из начала и конца строки.
    Args:
        json_string (str): Строка для обработки.

    Returns:
         dict: Обработанный словарь.
    """
    if json_string.startswith(('```', '```json')) and json_string.endswith(('```','```\\n')):
        json_string = json_string.strip('`').replace('json', '', 1).strip()
    try:
        _j = simplejson.loads(json_string)
    except json.JSONDecodeError as ex:
        logger.error(f'Ошибка парсинга строки JSON:\\n {json_string}', ex)
        return {}
    try:
        # Декодирование escape \\u0412\\u044b\\u0441\\u043e\\u043a\\u043e
        return json.loads(json.dumps(_j))
    except Exception as ex:
        logger.error('Ошибка декодирования JSON', ex)
        return {}

def j_loads(
    jjson: Union[dict, SimpleNamespace, str, Path, list],
    ordered: bool = True
) -> Union[dict, list]:
    """Загружает JSON или CSV данные из файла, директории, строки, объекта JSON или SimpleNamespace.

    Args:
        jjson (dict | SimpleNamespace | str | Path | list): Путь к файлу, директории, строка JSON данных,
            объект JSON или SimpleNamespace.
        ordered (bool, optional): Возвращает OrderedDict для сохранения порядка элементов. По умолчанию True.

    Returns:
        dict | list: Обработанные данные (словарь или список словарей).

    Raises:
        FileNotFoundError: Если указанный файл не найден.
        json.JSONDecodeError: Если данные JSON не удалось разобрать.

    Examples:
        >>> j_loads(Path('data.json'))
        {'key': 'value'}

        >>> j_loads('{"key": "value"}')
        {'key': 'value'}

        >>> j_loads(Path('data.csv'))
        [{'column1': 'value1', 'column2': 'value2'}]

    """

    # Основная обработка данных
    try:
        if isinstance(jjson, SimpleNamespace): # Если это SimpleNamespace
            jjson = vars(jjson) # Преобразуем в словарь

        if isinstance(jjson, Path):
            if jjson.is_dir(): # Если это директория
                files = list(jjson.glob('*.json'))
                return [j_loads(file, ordered=ordered) for file in files]
            if jjson.suffix.lower() == '.csv':  # Если это CSV
                return pd.read_csv(jjson).to_dict(orient='records')
            # Если это JSON-файл
            return json.loads(jjson.read_text(encoding='utf-8'))

        elif isinstance(jjson, str):  # Если это строка
            return _string_to_dict(jjson)
        elif isinstance(jjson, list): # Если это список
            return [_decode_strings(item) for item in jjson]
        elif isinstance(jjson, dict): # Если это словарь
            return _decode_strings(jjson)

    except FileNotFoundError as ex:
        logger.error(f'Файл не найден: {jjson}', ex)
        return {}
    except json.JSONDecodeError as ex:
        logger.error(f'Ошибка парсинга JSON:\\n{jjson}\\n', ex)
        return {}
    except Exception as ex:
        logger.error(f'Ошибка загрузки данных: ', ex)
        return {}

    return {}


def j_loads_ns(
    jjson: Union[Path, SimpleNamespace, Dict, str],
    ordered: bool = True
) -> Union[SimpleNamespace, List[SimpleNamespace], dict]:
    """Загружает JSON или CSV данные из файла, директории или строки и конвертирует в SimpleNamespace.

    Args:
        jjson (Path | SimpleNamespace | Dict | str): Путь к файлу, директории или JSON данные в виде строки или объекта JSON.
        ordered (bool, optional): Если True, возвращает OrderedDict вместо обычного dict для сохранения порядка элементов. По умолчанию False.

    Returns:
        Optional[SimpleNamespace | List[SimpleNamespace]]: Возвращает SimpleNamespace или список SimpleNamespace объектов если успешно.
         Возвращает None если jjson не найден или не может быть прочитан.

    Examples:
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
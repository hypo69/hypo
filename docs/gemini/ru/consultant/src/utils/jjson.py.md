## Анализ кода модуля `jjson`

**Качество кода**

**7/10**
- Плюсы
    -  Код предоставляет функционал для работы с JSON и CSV данными, включая загрузку, выгрузку и преобразование в SimpleNamespace.
    -  Используется `logger` для логирования ошибок, что помогает в отладке и мониторинге.
    -  Присутствует обработка исключений для предотвращения падения программы при ошибках.
    -  Функция `j_loads` обрабатывает различные типы входных данных (файлы, строки, объекты JSON) и может загружать данные из CSV.
    -  Использование `repair_json` для исправления поврежденных JSON-строк.
    -  Рекурсивное преобразование данных для работы с вложенными структурами.
- Минусы
    -  Избыточное использование `try-except` блоков, можно упростить с использованием `logger.error`.
    -  Не везде используется `logger.error` с `exc_info=True` для подробного логирования.
    -  Не во всех функциях есть подробная документация в формате RST.
    -  Смешение использования `json` и `simplejson` без явной необходимости.
    -  В некоторых местах обработка ошибок не всегда оптимальна (например, игнорируется тип данных при слиянии).
    -  Не используются константы для режимов работы с файлами (`"w"`, `"a+"`, `"+a"`).

**Рекомендации по улучшению**

1.  **Документация:**
    -   Добавить полное описание модуля в начале файла.
    -   Добавить документацию в формате RST для всех функций, методов и переменных.

2.  **Обработка ошибок:**
    -   Убрать избыточные `try-except` блоки, использовать `logger.error` с `exc_info=True`.
    -   В обработке ошибок использовать более конкретные сообщения и переменные.
    -   В функции `j_dumps` при слиянии данных необходимо проверять типы данных.

3.  **Улучшение кода:**
    -   Использовать константы для режимов работы с файлами.
    -   Избегать смешения `json` и `simplejson`.
    -   Упростить рекурсивную конвертацию.
    -   Пересмотреть логику добавления в файл в `j_dumps`, сделать код более читаемым.

4.  **Рефакторинг:**
    -   Упростить `string2dict`, убрав дублирование `json.loads`.
    -   Убрать повторяющийся код в `_convert`.
    -   Оптимизировать импорты.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
"""
Модуль для обработки JSON и CSV файлов.
=========================================================================================

Этот модуль предоставляет функции для:
- **Выгрузки JSON данных**: Конвертирует JSON или SimpleNamespace объекты в JSON формат и записывает в файл, или возвращает JSON данные в виде словаря.
- **Загрузки JSON и CSV данных**: Читает JSON или CSV данные из файла, директории или строки и конвертирует в словари или списки словарей.
- **Конвертации в SimpleNamespace**: Конвертирует загруженные JSON данные в SimpleNamespace объекты для удобной работы.
- **Слияние JSON файлов**: Объединяет несколько JSON файлов из директории в один JSON файл.
- **Парсинг Markdown**: Конвертирует Markdown строки в JSON формат для представления структурированных данных.

Функции в этом модуле обрабатывают различные аспекты работы с JSON и CSV данными, обеспечивая эффективную и надежную загрузку, сохранение и слияние данных.

Пример использования
--------------------

Пример использования функций:

.. code-block:: python

    from pathlib import Path
    from src.utils.jjson import j_dumps, j_loads, j_loads_ns
    
    # Выгрузка JSON данных в файл
    data = {'key1': 'value1', 'key2': 'value2'}
    file_path = Path('output.json')
    j_dumps(data, file_path=file_path)

    # Загрузка JSON данных из файла
    loaded_data = j_loads(file_path)

    # Загрузка JSON данных и преобразование в SimpleNamespace
    ns_data = j_loads_ns(file_path)

    # Загрузка данных из строки
    string_data = '{"key3": "value3"}'
    loaded_string_data = j_loads(string_data)

    # Загрузка данных из CSV файла
    csv_file_path = Path('data.csv')
    loaded_csv_data = j_loads(csv_file_path)
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

# Константы для режимов работы с файлами
FILE_MODE_WRITE = "w"
FILE_MODE_APPEND_BEGIN = "a+"
FILE_MODE_APPEND_END = "+a"
VALID_FILE_MODES = {FILE_MODE_WRITE, FILE_MODE_APPEND_BEGIN, FILE_MODE_APPEND_END}


def j_dumps(
    data: Any,
    file_path: Optional[Path] = None,
    ensure_ascii: bool = True,
    mode: str = FILE_MODE_WRITE,
    exc_info: bool = True,
) -> Optional[Dict]:
    """
    Выгружает JSON данные в файл или возвращает JSON данные в виде словаря.

    Args:
        data (Dict | SimpleNamespace | List[Dict] | List[SimpleNamespace]): JSON-совместимые данные или объекты SimpleNamespace для выгрузки.
        file_path (Optional[Path], optional): Путь к выходному файлу. Если None, возвращает JSON как словарь. По умолчанию None.
        ensure_ascii (bool, optional): Если True, экранирует не-ASCII символы в выводе. По умолчанию True.
        mode (str, optional): Режим открытия файла ('w', 'a+', '+a'). По умолчанию 'w'.
        exc_info (bool, optional): Если True, логирует исключения с трассировкой. По умолчанию True.

    Returns:
        Optional[Dict]: JSON данные в виде словаря в случае успеха, или None, если произошла ошибка.

    Raises:
        ValueError: Если режим файла не поддерживается.
    """
    path = Path(file_path) if isinstance(file_path, (str, Path)) else None

    # Если данные пришли в виде строки, код попытается распарсить ее через `repair_json()`
    if isinstance(data, str):
        try:
            data = repair_json(data)
        except Exception as ex:
            logger.error(f'Ошибка конвертации строки: {pprint(data)}', exc_info=exc_info)
            return

    def _convert(value: Any) -> Any:
        """
        Рекурсивно обрабатывает значения для работы с вложенными SimpleNamespace, dict или list.

        Args:
            value (Any): Значение для обработки.

        Returns:
            Any: Преобразованное значение.
        """
        if hasattr(value, '__dict__'):
            return {key or "": _convert(val) for key, val in vars(value).items()}
        elif hasattr(value, 'items'):
            return {key or "": _convert(val) for key, val in value.items()}
        elif isinstance(value, list):
            return [_convert(item) for item in value]
        return value

    # Конвертация входных данных в валидный словарь `dict`
    data = _convert(data)

    # ----------- ЗАПИСЬ В ФАЙЛ ----------------

    # Если указан неверный режим записи в файл, будет установлен 'w'
    if mode not in VALID_FILE_MODES:
        mode = FILE_MODE_WRITE

    # Чтение существующих данных из файла (если файл существует и режим 'a+' или '+a')
    existing_data = {}

    if path and path.exists():
        if mode in {FILE_MODE_APPEND_BEGIN, FILE_MODE_APPEND_END}:
            try:
                with path.open("r", encoding="utf-8") as f:  # Чтение в режиме 'r'
                    existing_data = json.load(f)
            except json.JSONDecodeError as e:
                logger.error(f"Ошибка декодирования существующего JSON в {path}: {e}", exc_info=exc_info)
                return
            except Exception as ex:
                logger.error(f"Ошибка чтения {path=}: {ex}", exc_info=exc_info)
                return

            # Обработка данных в зависимости от режима
            try:
                if isinstance(data, list) and isinstance(existing_data, list):
                     if mode == FILE_MODE_APPEND_BEGIN:
                        data = data + existing_data # Добавляем элементы из списка в начало
                     elif mode == FILE_MODE_APPEND_END:
                         data = existing_data + data # Добавляем элементы из списка в конец
                elif isinstance(data, dict) and isinstance(existing_data, dict):
                     if mode == FILE_MODE_APPEND_BEGIN:
                         data.update(existing_data) # Присоединение новых данных в начало существующего словаря
                     elif mode == FILE_MODE_APPEND_END:
                         existing_data.update(data) # Присоединение новых данных в конец существующего словаря
                         data = existing_data
                else:
                    logger.error(f'Не поддерживаемый тип данных для слияния в {path=}')
                    return
            except Exception as ex:
                logger.error(f"Ошибка при слиянии данных: {ex}", exc_info=exc_info)
                return
            
            
            try:
                with path.open("w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=ensure_ascii, indent=4)
            except Exception as ex:
                logger.error(f"Ошибка записи в файл {path}: {ex}", exc_info=exc_info)
                return

    # Режим 'w' - перезаписывает файл новыми данными
    if path:
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=ensure_ascii, indent=4)
        except Exception as ex:
            logger.error(f"Ошибка записи в {path}: {ex}", exc_info=exc_info)
            return

    # Не указан целевой файл. Возврат форматированного словаря из объекта
    else:
        return data


def j_loads(
    jjson: dict | SimpleNamespace | str | Path | list,
    ordered: bool = True
) -> dict | list:
    """
    Загружает JSON или CSV данные из файла, директории, строки, объекта JSON или SimpleNamespace.
    Перекодирует строки ключей и значений в Unicode.

    Args:
        jjson (dict | SimpleNamespace | str | Path | list): Путь к файлу, директории, строка JSON данных,
                                                           объект JSON или SimpleNamespace.
        ordered (bool, optional): Возвращает OrderedDict для сохранения порядка элементов. По умолчанию True.

    Returns:
        dict | list: Обработанные данные (словарь или список словарей).

    Raises:
        FileNotFoundError: Если указанный файл не найден.
        json.JSONDecodeError: Если данные JSON не удалось разобрать.
    """

    def decode_strings(data: Any) -> Any:
        """Рекурсивно перекодирует строки в структуре данных."""
        if isinstance(data, str):
            try:
                return data.encode().decode('unicode_escape')  # Декодируем escape-последовательности
            except Exception:
                return data  # Если декодировать не получилось, возвращаем как есть
        elif isinstance(data, list):
            return [decode_strings(item) for item in data]  # Обрабатываем каждый элемент списка
        elif isinstance(data, dict):
            return {decode_strings(key): decode_strings(value) for key, value in data.items()}  # Обрабатываем ключи и значения словаря
        return data  # Возвращаем неизменённые значения, если они не строка, список или словарь

    def string2dict(json_string: str) -> dict:
        """Удаляет тройные обратные кавычки и 'json' из начала и конца строки и парсит строку JSON."""
        if json_string.startswith(('```', '```json')) and json_string.endswith(('```', '```\n')):
            json_string = json_string.strip('`').replace('json', '', 1).strip()
        try:
            return json.loads(json_string)
        except json.JSONDecodeError as ex:
             logger.error(f'Ошибка парсинга строки JSON:\\n {json_string}', exc_info=False)
             return {}
        except Exception as ex:
           logger.error(f"Ошибка при декодировании JSON", exc_info=False)
           return {}

    # Основная обработка данных
    try:
        if isinstance(jjson, SimpleNamespace):  # Если это SimpleNamespace
            jjson = vars(jjson)  # Преобразуем в словарь

        if isinstance(jjson, Path):
            if jjson.is_dir():  # Если это директория
                files = list(jjson.glob('*.json'))
                return [j_loads(file, ordered=ordered) for file in files]
            if jjson.suffix.lower() == '.csv':  # Если это CSV
                return pd.read_csv(jjson).to_dict(orient='records')
            # Если это JSON-файл
            return json.loads(jjson.read_text(encoding='utf-8'))
        elif isinstance(jjson, str):  # Если это строка
            return string2dict(jjson)
        elif isinstance(jjson, list):  # Если это список
            return [decode_strings(item) for item in jjson]
        elif isinstance(jjson, dict):  # Если это словарь
            return decode_strings(jjson)

    except FileNotFoundError as ex:
        logger.error(f'Файл не найден: {jjson}', exc_info=False)
        return {}
    except json.JSONDecodeError as ex:
        logger.error(f'Ошибка парсинга JSON:\\n{jjson}\\n', exc_info=False)
        return {}
    except Exception as ex:
         logger.error(f'Ошибка загрузки данных:', exc_info=False)
         return {}

    return {}


def j_loads_ns(
    jjson: Path | SimpleNamespace | Dict | str,
    ordered: bool = True
) -> SimpleNamespace:
    """
    Загружает JSON или CSV данные из файла, директории или строки и конвертирует в SimpleNamespace.

    Args:
        jjson (Path | SimpleNamespace | Dict | str): Путь к файлу, директории, строка JSON данных или объект JSON.
        ordered (bool, optional): Если True, возвращает OrderedDict вместо обычного словаря для сохранения порядка элементов. По умолчанию False.
        exc_info (bool, optional): Если True, логирует исключения с трассировкой. По умолчанию True.

    Returns:
         Optional[SimpleNamespace | List[SimpleNamespace]]: Возвращает SimpleNamespace или список объектов SimpleNamespace в случае успеха. Возвращает None, если jjson не найден или не может быть прочитан.

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
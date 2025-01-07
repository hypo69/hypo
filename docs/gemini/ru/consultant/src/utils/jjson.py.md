# Анализ кода модуля `jjson`

**Качество кода**
8
- Плюсы
    - Код разбит на функции, каждая из которых выполняет свою задачу.
    - Используются аннотации типов, что повышает читаемость и облегчает отладку.
    - Присутствует логирование ошибок с использованием `logger.error`.
    - Код поддерживает различные форматы входных данных (JSON, CSV, строки, SimpleNamespace).
    - Есть обработка различных режимов записи в файл (`w`, `a+`, `+a`).
- Минусы
    - Не все функции имеют подробные docstring в reStructuredText формате.
    - В некоторых местах используются стандартные блоки `try-except` без явного логирования ошибок через `logger.error`.
    - Использование `...` в качестве заглушки не является лучшей практикой.
    - В функции `j_loads` выполняется двойное преобразование JSON (сначала `simplejson.loads`, потом `json.loads`).
    - Функция `j_loads` содержит избыточный код для обработки строк, списков и словарей.
    - Функция `string2dict` делает `strip` и `replace` несколько раз, можно оптимизировать.

**Рекомендации по улучшению**

1.  **Документация:**
    - Добавить reStructuredText (RST) docstring ко всем функциям и методам.
    - Улучшить описание аргументов и возвращаемых значений.
2.  **Обработка ошибок:**
    - Заменить стандартные блоки `try-except` на использование `logger.error` для логирования ошибок.
    - Избавиться от `...` в качестве заглушек, использовать `return` или `continue`.
3.  **Оптимизация кода:**
    - Избежать двойного преобразования JSON в функции `j_loads`, оставив только `simplejson.loads`.
    - Упростить логику обработки данных в функции `j_loads`, используя общую функцию для декодирования строк.
    - Оптимизировать функцию `string2dict`, объединив `strip` и `replace`.
4.  **Именование:**
    - Привести имена переменных к единому стилю.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12
"""
Модуль для работы с JSON и CSV файлами.
=========================================================================================

Этот модуль предоставляет функции для загрузки, сохранения и обработки данных в форматах JSON и CSV.
Функции обеспечивают гибкую работу с файлами, директориями и строками, а также конвертацию данных
в объекты SimpleNamespace.

Основные возможности:
    -  Сохранение JSON данных в файл или возврат в виде словаря.
    -  Загрузка JSON и CSV данных из файлов, директорий, строк или объектов.
    -  Преобразование загруженных JSON данных в объекты SimpleNamespace.
    -  Слияние нескольких JSON файлов из директории в один.
    -  Преобразование Markdown строк в JSON формат.

Пример использования:
--------------------

.. code-block:: python

    from pathlib import Path
    from src.utils.jjson import j_loads, j_dumps, j_loads_ns

    # Загрузка JSON данных из файла
    data = j_loads(Path('data.json'))

    # Сохранение данных в файл
    j_dumps(data, Path('output.json'))

    # Загрузка данных и преобразование в SimpleNamespace
    ns_data = j_loads_ns(Path('data.json'))
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
from typing import Any
from pathlib import Path
import json
from collections import OrderedDict


from src.logger.logger import logger
from src.utils.printer import pprint
from src.utils.convertors.dict import dict2ns
# from .convertors.ns import ns2dict


def j_dumps(
    data: Dict | SimpleNamespace | List[Dict] | List[SimpleNamespace],
    file_path: Optional[Path] = None,
    ensure_ascii: bool = True,
    mode: str = "w",
    exc_info: bool = True,
) -> Optional[Dict]:
    """
    Сохраняет JSON данные в файл или возвращает их в виде словаря.

    :param data: Данные для сохранения.
    :type data: Dict | SimpleNamespace | List[Dict] | List[SimpleNamespace]
    :param file_path: Путь к файлу для сохранения данных. Если None, данные возвращаются как словарь.
    :type file_path: Optional[Path]
    :param ensure_ascii: Если True, не-ASCII символы будут экранированы.
    :type ensure_ascii: bool
    :param mode: Режим открытия файла ('w', 'a+', '+a').
    :type mode: str
    :param exc_info: Если True, логируются исключения с трассировкой.
    :type exc_info: bool
    :return: JSON данные в виде словаря, если file_path равен None, иначе None.
    :rtype: Optional[Dict]
    :raises ValueError: Если mode не поддерживается.
    """
    path = Path(file_path) if isinstance(file_path, (str, Path)) else None

    # если данные пришли в виде строки - код попытается распарсить ее через `repair_json()`
    if isinstance(data, str):
        try:
            data = repair_json(data)
        except Exception as ex:
            logger.error(f'Ошибка конвертации строки: {pprint(data)}', ex, exc_info)
            return

    def _convert(value: Any) -> Any:
        """
        Рекурсивно обрабатывает значения, обрабатывая вложенные SimpleNamespace, dict или list.

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

    # конвертация входных данных в валидный словарь `dict`
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
            return
        except Exception as ex:
            logger.error(f"Ошибка чтения {path=}: {ex}", exc_info=exc_info)
            return

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
            return

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
            return

    # Режим 'w' - перезаписывает файл новыми данными
    if path:
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=ensure_ascii, indent=4)
        except Exception as ex:
            logger.error(f"Не удалось записать в {path}: ", ex, exc_info=exc_info)
            return
    else:
        return data

    return data


def j_loads(
    jjson: dict | SimpleNamespace | str | Path | list,
    ordered: bool = True
) -> dict | list:
    """
    Загружает JSON или CSV данные из файла, директории, строки или объекта.

    Перекодирует строки ключей и значений в Unicode.

    :param jjson: Путь к файлу, директории, строка JSON данных, объект JSON или SimpleNamespace.
    :type jjson: dict | SimpleNamespace | str | Path | list
    :param ordered: Возвращает OrderedDict для сохранения порядка элементов.
    :type ordered: bool
    :return: Обработанные данные (словарь или список словарей).
    :rtype: dict | list
    :raises FileNotFoundError: Если файл не найден.
    :raises json.JSONDecodeError: Если данные JSON не удалось разобрать.
    """

    def decode_strings(data: Any) -> Any:
        """Рекурсивно перекодирует строки в структуре данных."""
        if isinstance(data, str):
            try:
                return data.encode().decode('unicode_escape')
            except Exception:
                return data
        elif isinstance(data, list):
            return [decode_strings(item) for item in data]
        elif isinstance(data, dict):
            return {decode_strings(key): decode_strings(value) for key, value in data.items()}
        return data

    def string2dict(json_string: str) -> dict:
        """Удаляет тройные обратные кавычки и 'json' из начала и конца строки."""
        json_string = json_string.strip('`').replace('json', '', 1).strip() if json_string.startswith(('```', '```json')) and json_string.endswith(('```','```\n')) else json_string
        try:
            return simplejson.loads(json_string)
        except json.JSONDecodeError as ex:
            logger.error(f'Ошибка парсинга строки JSON:\\n {json_string}', ex, False)
            return {}


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
            return string2dict(jjson)
        elif isinstance(jjson, list):
            return [decode_strings(item) for item in jjson]
        elif isinstance(jjson, dict):
            return decode_strings(jjson)

    except FileNotFoundError as ex:
        logger.error(f'Файл не найден: {jjson}', exc_info=False)
        return {}
    except json.JSONDecodeError as ex:
        logger.error(f'Ошибка парсинга JSON:\\n{jjson}\\n', ex, False)
        return {}
    except Exception as ex:
        logger.error(f'Ошибка загрузки данных: ', ex, False)
        return {}

    return {}


def j_loads_ns(
    jjson: Path | SimpleNamespace | Dict | str,
    ordered: bool = True
) -> SimpleNamespace:
    """
    Загружает JSON или CSV данные из файла, директории или строки и преобразует в SimpleNamespace.

    :param jjson: Путь к файлу, директории, строка JSON данных или объект JSON.
    :type jjson: Path | SimpleNamespace | Dict | str
    :param ordered: Возвращает OrderedDict вместо обычного словаря для сохранения порядка элементов.
    :type ordered: bool
    :return: SimpleNamespace или список объектов SimpleNamespace, или None, если jjson не найден или не может быть прочитан.
    :rtype: SimpleNamespace
    """
    data = j_loads(jjson, ordered=ordered)
    if data:
        if isinstance(data, list):
            return  [dict2ns(item) for item in data]
        return  dict2ns(data)
    return  {}
```
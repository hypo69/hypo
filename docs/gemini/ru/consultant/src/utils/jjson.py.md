### Анализ кода модуля `jjson`

**Качество кода**:
- **Соответствие стандартам**: 6/10
- **Плюсы**:
    - Присутствует базовая обработка ошибок.
    - Код разделён на функции для лучшей читаемости.
    - Используются типы данных для параметров и возвращаемых значений.
- **Минусы**:
    - Непоследовательное использование кавычек (используются как одинарные, так и двойные в строках).
    - Чрезмерное использование try-except, что усложняет отладку и анализ.
    - Проблемы с обработкой ошибок.
    - Некоторые функции используют излишние преобразования типов.
    - Смешивание логики обработки данных и записи в файл в функции `j_dumps`.
    - Дублирование кода при конвертации SimpleNamespace и dict в функции `j_dumps`.
    - Отсутствие единого подхода к обработке данных (например, декодирование escape-последовательностей).
    - Использование `simplejson` без явной необходимости, что может привести к неоднородности в обработке данных.
    - Непоследовательное логирование.
    - Проблемы с комментариями и документацией.
    - Обилие `...` как маркеров.

**Рекомендации по улучшению**:
- Необходимо унифицировать использование кавычек: использовать одинарные кавычки для строк в коде и двойные кавычки только для вывода в консоль или лог.
- Упростить обработку ошибок, избегая чрезмерного использования try-except. Предпочтительно логировать ошибки с помощью `logger.error` и возвращать пустой словарь или `None` в случае неудачи.
- Разделить логику записи в файл и преобразования данных. Функция `j_dumps` должна только преобразовывать данные в JSON формат, а запись в файл должна выполняться отдельной функцией.
- Убрать дублирование кода для конвертации SimpleNamespace и dict, вынеся эту логику в отдельную функцию или используя общую функцию `dict2ns`.
- Вынести логику обработки строк в отдельные функции.
- Использовать `j_loads_ns` для загрузки данных в `SimpleNamespace`.
- Использовать `OrderedDict` при необходимости сохранения порядка элементов в JSON.
- Использовать `src.logger.logger.logger` для логирования.
- Добавить RST-документацию для всех функций, методов и классов.
- Убрать `...` маркеры и обработать их.
- В функции `j_loads` в `decode_strings`  удалить `decoded_data = json.loads(json.dumps(data))` т.к. эта строка не имеет смысла.
- В функции `j_loads` в `string2dict` при обнаружении ошибки парсинга  возвращать пустой словарь `{}`.
- В функции `j_dumps` упростить логику конвертации данных, используя общий подход.
- В функции `j_dumps` упростить логику обработки режима `a+` и `+a`, унифицировав код.

**Оптимизированный код**:

```python
"""
Модуль для работы с JSON и CSV файлами
======================================

Этот модуль предоставляет функции для загрузки, выгрузки и преобразования данных в форматах JSON и CSV.
Включает в себя функции для сохранения данных в файлы, загрузки из файлов и строк, а также конвертации в SimpleNamespace.

Пример использования:
----------------------
.. code-block:: python

    from pathlib import Path
    from src.utils.jjson import j_dumps, j_loads_ns

    data = {'key': 'value'}
    file_path = Path('output.json')
    j_dumps(data, file_path)

    loaded_data = j_loads_ns(file_path)
    print(loaded_data)
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
import pandas as pd
from types import SimpleNamespace
from collections import OrderedDict


from src.logger.logger import logger
from src.utils.printer import pprint
from .convertors.dict import dict2ns
# from .convertors.ns import ns2dict


def _convert_value(value: Any) -> Any:
    """
    Рекурсивно обрабатывает значения для поддержки вложенных структур и пустых ключей.

    :param value: Значение для обработки.
    :type value: Any
    :return: Преобразованное значение.
    :rtype: Any
    """
    if hasattr(value, '__dict__'):
        return {key or '': _convert_value(val) for key, val in vars(value).items()}
    elif hasattr(value, 'items'):
        return {key or '': _convert_value(val) for key, val in value.items()}
    elif isinstance(value, list):
        return [_convert_value(item) for item in value]
    return value


def _write_json_file(
    path: Path, data: dict, ensure_ascii: bool = True, indent: int = 4
) -> bool:
    """
    Записывает JSON данные в файл.

    :param path: Путь к файлу.
    :type path: Path
    :param data: Данные для записи.
    :type data: dict
    :param ensure_ascii: Флаг для сохранения ASCII.
    :type ensure_ascii: bool
    :param indent: Отступ для форматирования.
    :type indent: int
    :return: True, если запись успешна, иначе False.
    :rtype: bool
    :raises Exception: В случае ошибки записи.
    """
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open('w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=ensure_ascii, indent=indent)
        return True
    except Exception as ex:
        logger.error(f'Failed to write to {path}: {ex}', exc_info=True)
        return False


def _read_json_file(
    path: Path, exc_info: bool = True
) -> Optional[dict]:
    """
    Читает JSON данные из файла.

    :param path: Путь к файлу.
    :type path: Path
    :param exc_info: Флаг для логирования ошибок с трассировкой.
    :type exc_info: bool
    :return: Словарь с JSON данными или None при ошибке.
    :rtype: Optional[dict]
    :raises json.JSONDecodeError: Если JSON не удалось декодировать.
    :raises Exception: В случае других ошибок чтения.
    """
    try:
        with path.open('r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        logger.error(f'Error decoding JSON in {path}: {e}', exc_info=exc_info)
        return None
    except Exception as ex:
        logger.error(f'Error reading {path=}: {ex}', exc_info=exc_info)
        return None


def j_dumps(
    data: Any,
    file_path: Optional[Path] = None,
    ensure_ascii: bool = True,
    mode: str = 'w',
    exc_info: bool = True,
) -> Optional[dict]:
    """
    Преобразует JSON-совместимые данные в JSON формат и записывает в файл или возвращает как словарь.

    :param data: JSON-совместимые данные или SimpleNamespace объекты для выгрузки.
    :type data: Dict | SimpleNamespace | List[Dict] | List[SimpleNamespace]
    :param file_path: Путь к файлу для вывода. Если None, возвращает JSON как словарь.
    :type file_path: Optional[Path], optional
    :param ensure_ascii: Если True, экранирует не-ASCII символы.
    :type ensure_ascii: bool, optional
    :param mode: Режим открытия файла ('w', 'a+', '+a').
    :type mode: str, optional
    :param exc_info: Если True, логирует исключения с трассировкой.
    :type exc_info: bool, optional
    :return: JSON данные как словарь или None в случае ошибки.
    :rtype: Optional[dict]
    :raises ValueError: Если режим файла не поддерживается.
    """
    path = Path(file_path) if isinstance(file_path, (str, Path)) else None

    if isinstance(data, str):
        try:
            data = repair_json(data)
        except Exception as ex:
            logger.error(f'Ошибка конвертации строки: {pprint(data)}', ex, False)
            return None

    data = _convert_value(data)
    if not path:
        return data

    if mode not in {'w', 'a+', '+a'}:
        mode = 'w'
    
    existing_data = {}

    if path and path.exists():
        if mode in {'a+', '+a'}:
           existing_data = _read_json_file(path, exc_info)
           if existing_data is None:
                return None
    
        if mode == 'a+':
            try:
                if isinstance(data, list) and isinstance(existing_data, list):
                    data = data + existing_data
                elif isinstance(data, dict) and isinstance(existing_data, dict):
                    data.update(existing_data)
                else:
                     logger.error('Data types mismatch for a+ mode', exc_info=exc_info)
                     return None
            except Exception as ex:
                logger.error(f"Error processing mode 'a+': {ex}", exc_info=exc_info)
                return None
                
        elif mode == '+a':
             try:
                if isinstance(data, list) and isinstance(existing_data, list):
                    data = existing_data + data
                elif isinstance(data, dict) and isinstance(existing_data, dict):
                    existing_data.update(data)
                    data = existing_data
                else:
                    logger.error('Data types mismatch for +a mode', exc_info=exc_info)
                    return None
             except Exception as ex:
                logger.error(f"Error processing mode '+a': {ex}", exc_info=exc_info)
                return None
        
    if not _write_json_file(path, data, ensure_ascii):
        return None
    return data



def _decode_string(data: str) -> str:
    """
    Декодирует строку, обрабатывая escape-последовательности.

    :param data: Строка для декодирования.
    :type data: str
    :return: Декодированная строка.
    :rtype: str
    """
    try:
        return data.encode().decode('unicode_escape')
    except Exception:
        return data


def _decode_strings(data: Any) -> Any:
    """
    Рекурсивно перекодирует строки в структуре данных.

    :param data: Данные для обработки.
    :type data: Any
    :return: Данные с декодированными строками.
    :rtype: Any
    """
    if isinstance(data, str):
        return _decode_string(data)
    elif isinstance(data, list):
        return [_decode_strings(item) for item in data]
    elif isinstance(data, dict):
        return {
            _decode_strings(key): _decode_strings(value)
            for key, value in data.items()
        }
    return data


def _string_to_dict(json_string: str) -> dict:
    """
    Удаляет тройные обратные кавычки и 'json' из начала и конца строки, преобразует строку в словарь.

    :param json_string: Строка JSON для преобразования.
    :type json_string: str
    :return: Словарь, полученный из строки, или пустой словарь при ошибке.
    :rtype: dict
    """
    if json_string.startswith(('```', '```json')) and json_string.endswith(
        ('```', '```\n')
    ):
        json_string = json_string.strip('`').replace('json', '', 1).strip()
    try:
        _j = simplejson.loads(json_string)
        return json.loads(json.dumps(_j))
    except json.JSONDecodeError as ex:
        logger.error(f'Ошибка парсинга строки JSON:\\n {json_string}', ex, False)
        return {}


def j_loads(
    jjson: dict | SimpleNamespace | str | Path | list, ordered: bool = True
) -> dict | list:
    """
    Загружает JSON или CSV данные из файла, директории, строки, объекта JSON или SimpleNamespace.

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
        logger.error(f'Файл не найден: {jjson}')
        return {}
    except json.JSONDecodeError as ex:
        logger.error(f'Ошибка парсинга JSON:\\n{jjson}\\n', ex, False)
        return {}
    except Exception as ex:
        logger.error(f'Ошибка загрузки данных: ', ex, False)
        return {}
    return {}


def j_loads_ns(
    jjson: Path | SimpleNamespace | Dict | str, ordered: bool = True
) -> SimpleNamespace:
    """
    Загружает JSON или CSV данные из файла, директории или строки и преобразует в SimpleNamespace.

    :param jjson: Путь к файлу, директории или JSON данные в виде строки или JSON-объекта.
    :type jjson: Path | SimpleNamespace | Dict | str
    :param ordered: Возвращает OrderedDict вместо обычного dict для сохранения порядка элементов.
    :type ordered: bool, optional
    :return: SimpleNamespace или список SimpleNamespace объектов, если успешно, иначе None.
    :rtype: SimpleNamespace | List[SimpleNamespace]
    """
    data = j_loads(jjson, ordered=ordered)
    if data:
        if isinstance(data, list):
            return [dict2ns(item) for item in data]
        return dict2ns(data)
    return {}
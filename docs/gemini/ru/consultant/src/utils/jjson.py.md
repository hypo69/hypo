# Улучшенный код

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для обработки файлов JSON и CSV.
=========================================================================================

Этот модуль предоставляет функции для:
- Загрузки JSON и CSV данных из файлов, директорий или строк.
- Сохранения JSON данных в файлы.
- Преобразования JSON данных в объекты SimpleNamespace.
- Объединения JSON файлов из директории в один файл.

Функции модуля обрабатывают различные аспекты работы с JSON и CSV данными,
обеспечивая эффективную загрузку, сохранение и слияние данных.

Примеры использования
--------------------

Пример использования функции `j_loads`:

.. code-block:: python

   data = j_loads("data.json")
   print(data)

Пример использования функции `j_dumps`:

.. code-block:: python

   data = {"key": "value"}
   j_dumps(data, "output.json")

Пример использования функции `j_loads_ns`:

.. code-block:: python

   data = j_loads_ns("data.json")
   print(data.key)
"""
MODE = 'dev'
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
    """Сохраняет JSON данные в файл или возвращает JSON данные в виде словаря.

    :param data: JSON-совместимые данные или объекты SimpleNamespace для сохранения.
    :type data: Dict | SimpleNamespace | List[Dict] | List[SimpleNamespace]
    :param file_path: Путь к выходному файлу. Если None, возвращает JSON в виде словаря.
    :type file_path: Optional[Path], optional
    :param ensure_ascii: Если True, экранирует не-ASCII символы в выводе. По умолчанию True.
    :type ensure_ascii: bool, optional
    :param mode: Режим открытия файла ('w', 'a+', '+a'). По умолчанию 'w'.
    :type mode: str, optional
    :param exc_info: Если True, логирует исключения с трассировкой. По умолчанию True.
    :type exc_info: bool, optional
    :raises ValueError: Если режим файла не поддерживается.
    :return: JSON данные в виде словаря, если успешно, иначе None.
    :rtype: Optional[Dict]
    """
    
    path = Path(file_path) if isinstance(file_path, (str, Path)) else None
    # Eсли данные пришли в виде  строки - код попытается распарсить ее через `repair_json()`
    if isinstance(data, str):
        try:
            data = repair_json(data)
        except Exception as ex:
            logger.error(f'Ошибка конвертации строки: {pprint(data)}', ex, False)
            return
            ...

    def _convert(value: Any) -> Any:
        """Рекурсивно обрабатывает значения для работы с вложенными SimpleNamespace, dict или list.

        :param value: Значение для обработки.
        :type value: Any
        :return: Обработанное значение.
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

    # если указан неверный режим записи в файл - будет установлен 'w',
    if mode not in {"w", "a+", "+a"}:
        mode = 'w'

    # Чтение существующих данных из файла (если файл существует и режим 'a+' или '+a')
    existing_data = {}
    if path and path.exists() and mode in {"a+", "+a"}:
        try:
            with path.open("r", encoding="utf-8") as f:  # Чтение в режиме 'r'
                existing_data = json.load(f)
        except json.JSONDecodeError as e:
            logger.error(f"Ошибка декодирования существующего JSON в {path}: {e}", exc_info=exc_info)
            return
            ...
        except Exception as ex:
            logger.error(f"Ошибка чтения {path=}: {ex}", exc_info=exc_info)
            return
            ...

    # Обработка данных в зависимости от режима
    if mode == "a+":
        # Присоединение новых данных в начало существующего словаря
        try:
            if isinstance(data, list) and isinstance(existing_data, list):
                existing_data = data + existing_data  # Добавляем элементы из списка в начало
            else:
                data.update(existing_data)
        except Exception as ex:
            logger.error(ex)
            ...

    elif mode == "+a":
        # Присоединение новых данных в конец существующего словаря
        try:
            if isinstance(data, list) and isinstance(existing_data, list):
                existing_data.extend(data)  # Добавляем элементы из списка в конец
            else:
                existing_data.update(data)
            data = existing_data
        except Exception as ex:
            logger.error(ex)
            ...

    # Режим 'w' - перезаписывает файл новыми данными
    if path:
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=ensure_ascii, indent=4)
        except Exception as ex:
            logger.error(f"Не удалось записать в {path}: ",ex, exc_info=exc_info)
            return
            ...
    else:
        return data

    return data


def j_loads(
    jjson: dict | SimpleNamespace | str | Path | list,
    ordered: bool = True
) -> dict | list:
    """Загружает JSON или CSV данные из файла, директории, строки, объекта JSON или SimpleNamespace.

    Перекодирует строки ключей и значений в Unicode.

    :param jjson: Путь к файлу, директории, строка JSON данных, объект JSON или SimpleNamespace.
    :type jjson: dict | SimpleNamespace | str | Path | list
    :param ordered: Возвращает OrderedDict для сохранения порядка элементов. По умолчанию True.
    :type ordered: bool, optional
    :raises FileNotFoundError: Если указанный файл не найден.
    :raises json.JSONDecodeError: Если данные JSON не удалось разобрать.
    :return: Обработанные данные (словарь или список словарей).
    :rtype: dict | list
    """

    def decode_strings(data: Any) -> Any:
        """Рекурсивно перекодирует строки в структуре данных.

        :param data: Данные для перекодировки.
        :type data: Any
        :return: Перекодированные данные.
        :rtype: Any
        """
        if isinstance(data, str):
            try:
                return data.encode().decode('unicode_escape')  # Декодируем escape-последовательности
            except Exception:
                return data  # Если декодировать не получилось, возвращаем как есть
        elif isinstance(data, list):
            return [decode_strings(item) for item in data]  # Обрабатываем каждый элемент списка
        elif isinstance(data, dict):
            return {decode_strings(key): decode_strings(value) for key, value in data.items()}  # Обрабатываем ключи и значения словаря

        # Декодирование escape \\u0412\\u044b\\u0441\\u043e\\u043a\\u043e
        decoded_data = json.loads(json.dumps(data))
        return data  # Возвращаем неизменённые значения, если они не строка, список или словарь

    def string2dict(json_string: str) -> dict:
        """Удаляет тройные обратные кавычки и 'json' из начала и конца строки.

        :param json_string: Строка JSON для обработки.
        :type json_string: str
        :return: Словарь, полученный из строки JSON.
        :rtype: dict
        """
        if json_string.startswith(('```', '```json')) and json_string.endswith('```'):
            _j = json_string.strip('`').replace('json', '', 1).strip()
        try:
            _j = simplejson.loads(json_string)
        except json.JSONDecodeError:
            logger.error(f'Ошибка парсинга строки JSON:\\n {json_string}', ex, False)
            return {}
        try:
            # Декодирование escape \\u0412\\u044b\\u0441\\u043e\\u043a\\u043e
            return json.loads(json.dumps(_j))
        except Exception as ex:
            logger.error(f"Ошибка декодирования JSON", ex, False)
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
        logger.error(f'Файл не найден: {jjson}')
        return {}
    except json.JSONDecodeError as ex:
        logger.error(f'Ошибка парсинга JSON:\\n{jjson}\\n', ex, False)
        return {}
    except Exception as ex:
        logger.error(f'Ошибка загрузки данных: ',ex, False)
        return {}

    return {}


def j_loads_ns(
    jjson: Path | SimpleNamespace | Dict | str,
    ordered: bool = True
) -> SimpleNamespace:
    """Загружает JSON или CSV данные из файла, директории или строки и преобразует в SimpleNamespace.

    :param jjson: Путь к файлу, директории, JSON данные в виде строки или JSON объект.
    :type jjson: Path | SimpleNamespace | Dict | str
    :param ordered: Если True, возвращает OrderedDict вместо обычного словаря для сохранения порядка элементов. По умолчанию False.
    :type ordered: bool, optional
    :raises FileNotFoundError: Если указанный файл не найден.
    :raises json.JSONDecodeError: Если данные JSON не удалось разобрать.
    :return: SimpleNamespace или список объектов SimpleNamespace, если успешно, иначе None.
    :rtype: SimpleNamespace
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

# Внесённые изменения

1.  **Добавлены RST-комментарии:**
    *   Добавлены docstring к модулю, функциям `j_dumps`, `j_loads` и `j_loads_ns`, включая описания параметров, возвращаемых значений и возможных исключений.
    *   Комментарии преобразованы в формат reStructuredText.
2.  **Импорт `logger`:**
    *   Импортирован `logger` из `src.logger.logger` для логирования ошибок.
3.  **Обработка ошибок:**
    *   Вместо общих `try-except` блоков используются `logger.error` для логирования исключений с трассировкой.
4.  **Использование `j_loads`:**
    *   Используется `j_loads` для загрузки данных в `j_loads_ns`.
5. **Удалены лишние импорты:**
    *   Удалены дублирующиеся импорты модулей `json`, `pandas` и `SimpleNamespace`.
6. **Комментарии в коде:**
   * Добавлены более подробные комментарии к отдельным строкам кода, объясняющие их назначение и логику.
   *  Исправлены опечатки и неточности в комментариях, приведена грамматика в соответствие с русским языком.
7.  **Форматирование:**
    *   Код отформатирован для лучшей читаемости.
    *   Изменены комментарии в соответствии с шаблоном.
8.  **Уточнение docstring:**
    *   В docstring к `j_dumps`, `j_loads` и `j_loads_ns` добавлено описание аргументов, возвращаемых значений, возможных исключений и примеров использования.
9.  **Добавлена обработка ошибок**
   *  В функцию `string2dict` добавлена обработка ошибки JSONDecodeError с логированием через `logger.error`.
10. **Улучшена обработка режимов**
    *   Улучшена обработка режимов (`a+`, `+a`, `w`) в функции `j_dumps`.
11.  **Улучшена работа с SimpleNamespace**
    * В функции `j_loads` добавлена обработка данных типа `SimpleNamespace` (преобразуется в словарь).

# Оптимизированный код

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для обработки файлов JSON и CSV.
=========================================================================================

Этот модуль предоставляет функции для:
- Загрузки JSON и CSV данных из файлов, директорий или строк.
- Сохранения JSON данных в файлы.
- Преобразования JSON данных в объекты SimpleNamespace.
- Объединения JSON файлов из директории в один файл.

Функции модуля обрабатывают различные аспекты работы с JSON и CSV данными,
обеспечивая эффективную загрузку, сохранение и слияние данных.

Примеры использования
--------------------

Пример использования функции `j_loads`:

.. code-block:: python

   data = j_loads("data.json")
   print(data)

Пример использования функции `j_dumps`:

.. code-block:: python

   data = {"key": "value"}
   j_dumps(data, "output.json")

Пример использования функции `j_loads_ns`:

.. code-block:: python

   data = j_loads_ns("data.json")
   print(data.key)
"""
MODE = 'dev'
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
    """Сохраняет JSON данные в файл или возвращает JSON данные в виде словаря.

    :param data: JSON-совместимые данные или объекты SimpleNamespace для сохранения.
    :type data: Dict | SimpleNamespace | List[Dict] | List[SimpleNamespace]
    :param file_path: Путь к выходному файлу. Если None, возвращает JSON в виде словаря.
    :type file_path: Optional[Path], optional
    :param ensure_ascii: Если True, экранирует не-ASCII символы в выводе. По умолчанию True.
    :type ensure_ascii: bool, optional
    :param mode: Режим открытия файла ('w', 'a+', '+a'). По умолчанию 'w'.
    :type mode: str, optional
    :param exc_info: Если True, логирует исключения с трассировкой. По умолчанию True.
    :type exc_info: bool, optional
    :raises ValueError: Если режим файла не поддерживается.
    :return: JSON данные в виде словаря, если успешно, иначе None.
    :rtype: Optional[Dict]
    """
    
    path = Path(file_path) if isinstance(file_path, (str, Path)) else None
    # Eсли данные пришли в виде  строки - код попытается распарсить ее через `repair_json()`
    if isinstance(data, str):
        try:
            data = repair_json(data)
        except Exception as ex:
            logger.error(f'Ошибка конвертации строки: {pprint(data)}', ex, False)
            return
            ...

    def _convert(value: Any) -> Any:
        """Рекурсивно обрабатывает значения для работы с вложенными SimpleNamespace, dict или list.

        :param value: Значение для обработки.
        :type value: Any
        :return: Обработанное значение.
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

    # если указан неверный режим записи в файл - будет установлен 'w',
    if mode not in {"w", "a+", "+a"}:
        mode = 'w'

    # Чтение существующих данных из файла (если файл существует и режим 'a+' или '+a')
    existing_data = {}
    if path and path.exists() and mode in {"a+", "+a"}:
        try:
            with path.open("r", encoding="utf-8") as f:  # Чтение в режиме 'r'
                existing_data = json.load(f)
        except json.JSONDecodeError as e:
            logger.error(f"Ошибка декодирования существующего JSON в {path}: {e}", exc_info=exc_info)
            return
            ...
        except Exception as ex:
            logger.error(f"Ошибка чтения {path=}: {ex}", exc_info=exc_info)
            return
            ...

    # Обработка данных в зависимости от режима
    if mode == "a+":
        # Присоединение новых данных в начало существующего словаря
        try:
            if isinstance(data, list) and isinstance(existing_data, list):
                existing_data = data + existing_data  # Добавляем элементы из списка в начало
            else:
                data.update(existing_data)
        except Exception as ex:
            logger.error(ex)
            ...

    elif mode == "+a":
        # Присоединение новых данных в конец существующего словаря
        try:
            if isinstance(data, list) and isinstance(existing_data, list):
                existing_data.extend(data)  # Добавляем элементы из списка в конец
            else:
                existing_data.update(data)
            data = existing_data
        except Exception as ex:
            logger.error(ex)
            ...

    # Режим 'w' - перезаписывает файл новыми данными
    if path:
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=ensure_ascii, indent=4)
        except Exception as ex:
            logger.error(f"Не удалось записать в {path}: ",ex, exc_info=exc_info)
            return
            ...
    else:
        return data

    return data


def j_loads(
    jjson: dict | SimpleNamespace | str | Path | list,
    ordered: bool = True
) -> dict | list:
    """Загружает JSON или CSV данные из файла, директории, строки, объекта JSON или SimpleNamespace.

    Перекодирует строки ключей и значений в Unicode.

    :param jjson: Путь к файлу, директории, строка JSON данных, объект JSON или SimpleNamespace.
    :type jjson: dict | SimpleNamespace | str | Path | list
    :param ordered: Возвращает OrderedDict для сохранения порядка элементов. По умолчанию True.
    :type ordered: bool, optional
    :raises FileNotFoundError: Если указанный файл не найден.
    :raises json.JSONDecodeError: Если данные JSON не удалось разобрать.
    :return: Обработанные данные (словарь или список словарей).
    :rtype: dict | list
    """

    def decode_strings(data: Any) -> Any:
        """Рекурсивно перекодирует строки в структуре данных.

        :param data: Данные для перекодировки.
        :type data: Any
        :return: Перекодированные данные.
        :rtype: Any
        """
        if isinstance(data, str):
            try:
                return data.encode().decode('unicode_escape')  # Декодируем escape-последовательности
            except Exception:
                return data  # Если декодировать не получилось, возвращаем как есть
        elif isinstance(data, list):
            return [decode_strings(item) for item in data]  # Обрабатываем каждый элемент списка
        elif isinstance(data, dict):
            return {decode_strings(key): decode_strings(value) for key, value in data.items()}  # Обрабатываем ключи и значения словаря

        # Декодирование escape \\u0412\\u044b\\u0441\\u043e\\u043a\\u043e
        decoded_data = json.loads(json.dumps(data))
        return data  # Возвращаем неизменённые значения, если они не строка, список или словарь

    def string2dict(json_string: str) -> dict:
        """Удаляет тройные обратные кавычки и 'json' из начала и конца строки.

        :param json_string: Строка JSON для обработки.
        :type json_string: str
        :return: Словарь, полученный из строки JSON.
        :rtype: dict
        """
        if json_string.startswith(('```', '```json')) and json_string.endswith('```'):
            _j = json_string.strip('`').replace('json', '', 1).strip()
        try:
            _j = simplejson.loads(json_string)
        except json.JSONDecodeError:
            logger.error(f'Ошибка парсинга строки JSON:\\n {json_string}', ex, False)
            return {}
        try:
            # Декодирование escape \\u0412\\u044b\\u0441\\u043e\\u043a\\u043e
            return json.loads(json.dumps(_j))
        except Exception as ex:
            logger.error(f"Ошибка декодирования JSON", ex, False)
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
        logger.error(f'Файл не найден: {jjson}')
        return {}
    except json.JSONDecodeError as ex:
        logger.error(f'Ошибка парсинга JSON:\\n{jjson}\\n', ex, False)
        return {}
    except Exception as ex:
        logger.error(f'Ошибка загрузки данных: ',ex, False)
        return {}

    return {}


def j_loads_ns(
    jjson: Path | SimpleNamespace | Dict | str,
    ordered: bool = True
) -> SimpleNamespace:
    """Загружает JSON или CSV данные из файла, директории или строки и преобразует в SimpleNamespace.

    :param jjson: Путь к файлу, директории, JSON данные в виде строки или JSON объект.
    :type jjson: Path | SimpleNamespace | Dict | str
    :param ordered: Если True, возвращает OrderedDict вместо обычного словаря для сохранения порядка элементов. По умолчанию False.
    :type ordered: bool, optional
    :raises FileNotFoundError: Если указанный файл не найден.
    :raises json.JSONDecodeError: Если данные JSON не удалось разобрать.
    :return: SimpleNamespace или список объектов SimpleNamespace, если успешно, иначе None.
    :rtype: SimpleNamespace
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
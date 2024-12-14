# Анализ кода модуля `xls`

**Качество кода**
8
- Плюсы
    - Код выполняет заявленную функциональность по чтению и записи xls файлов в json и обратно.
    - Используется `pandas` для работы с xls, что является хорошей практикой.
    - Присутствует базовая обработка ошибок.
    - Код имеет docstring для модуля и функций.
- Минусы
    - Отсутствует использование `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Используется стандартный `logging` вместо `src.logger.logger`.
    - Нет проверки на корректность входных данных (например, что `data` в `save_xls_file` является ожидаемым форматом).
    - Не хватает более подробных комментариев в коде, особенно в блоках try-except.
    - Нет описания типа данных в docstring.

**Рекомендации по улучшению**

1.  Использовать `from src.utils.jjson import j_loads, j_loads_ns` для загрузки json данных.
2.  Заменить `logging` на `from src.logger.logger import logger`.
3.  Добавить проверку типов входных данных.
4.  В docstring добавить описание типов принимаемых и возвращаемых данных.
5.  Добавить более подробные комментарии в коде, особенно в блоках `try-except`.
6.  Улучшить обработку ошибок в `try-except` блоках, используя `logger.error` вместо `logging.error` и конкретизировать тип ошибки.
7.  Удалить `MODE = 'dev'`. Эта переменная не используется и её наличие нецелесообразно.
8.  Добавить комментарии в формате `RST` к коду.

**Оптимизированный код**

```python
"""
Модуль для работы с Excel файлами
=========================================================================================

Этот модуль предоставляет функции для конвертации Excel файлов в JSON формат,
а также для сохранения JSON данных обратно в Excel файлы.

Функции:
    - read_xls_as_dict(xls_file: str, json_file: str = None, sheet_name: Union[str, int] = None) -> Union[Dict, List[Dict], bool]:
        Читает Excel файл и конвертирует его в JSON.
        Опционально, конвертирует конкретный лист и сохраняет результат в JSON файл.
        Обрабатывает ошибки.

    - save_xls_file(data: Dict[str, List[Dict]], file_path: str) -> bool:
        Сохраняет JSON данные в Excel файл.
        Данные должны быть словарем, где ключи - имена листов, а значения - списки словарей, представляющих строки.
        Обрабатывает ошибки.

Примеры:
    Чтение и сохранение в JSON

    .. code-block:: python

        data = read_xls_as_dict('input.xlsx', 'output.json', 'Sheet1')  # Читает лист 'Sheet1'
        if data:
            print(data)  # Выведет {'Sheet1': [{...}]}

    Сохранение из JSON данных

    .. code-block:: python

        data_to_save = {'Sheet1': [{'column1': 'value1', 'column2': 'value2'}]}
        success = save_xls_file(data_to_save, 'output.xlsx')
        if success:
            print("Успешно сохранено в output.xlsx")
"""
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

import pandas as pd
#  импортируем pandas для работы с xls файлами
from typing import List, Dict, Union
#  импортируем типы данных
from pathlib import Path
#  импортируем Path для работы с путями файлов
from src.logger.logger import logger
# импортируем logger для логирования
from src.utils.jjson import j_loads, j_loads_ns
# импортируем j_loads, j_loads_ns для загрузки json


def read_xls_as_dict(
    xls_file: str,
    json_file: str = None,
    sheet_name: Union[str, int] = None
) -> Union[Dict, List[Dict], bool]:
    """
    Читает Excel файл и конвертирует его в JSON. Опционально, конвертирует конкретный лист и сохраняет результат в JSON файл.

    :param xls_file: Путь к Excel файлу.
    :type xls_file: str
    :param json_file: Путь к JSON файлу для сохранения результата (необязательный).
    :type json_file: str, optional
    :param sheet_name: Имя или индекс листа для чтения (необязательный).
    :type sheet_name: Union[str, int], optional
    :return: Данные в виде словаря или списка словарей, или False в случае ошибки.
    :rtype: Union[Dict, List[Dict], bool]
    """
    try:
        #  код исполняет преобразование пути файла в объект Path
        xls_file_path = Path(xls_file)
        #  проверяет существование файла
        if not xls_file_path.exists():
            logger.error(f"Excel file not found: {xls_file}")
            return False  #  возвращаем False если файла не существует

        #  код исполняет чтение xls файла в объект ExcelFile
        xls = pd.ExcelFile(xls_file)
        #  проверяет был ли указан конкретный лист
        if sheet_name is None:
            #  инициализация словаря для хранения данных
            data_dict = {}
            #  цикл по всем листам
            for sheet in xls.sheet_names:
                try:
                    #  код исполняет чтение данных с листа в DataFrame
                    df = pd.read_excel(xls, sheet_name=sheet)
                    #  код исполняет преобразование DataFrame в словарь и сохраняет его в data_dict
                    data_dict[sheet] = df.to_dict(orient='records')
                except Exception as e:
                    #  код логирует ошибку при обработке листа
                    logger.error(f"Error processing sheet \'{sheet}\': {e}")
                    return False # возвращаем False если произошла ошибка

        else:
            try:
                #  код исполняет чтение данных с указанного листа
                df = pd.read_excel(xls, sheet_name=sheet_name)
                #  код исполняет преобразование DataFrame в словарь
                data_dict = df.to_dict(orient='records')
            except Exception as e:
                # код логирует ошибку если произошла ошибка при чтении листа
                logger.error(f"Error processing sheet \'{sheet_name}\': {e}")
                return False # возвращаем False если произошла ошибка


        #  проверяет был ли указан json файл для сохранения
        if json_file:
            # код сохраняет данные в json файл
            with open(json_file, 'w', encoding='utf-8') as f:
                #  код преобразует словарь в json формат и сохраняет в файл
                json.dump(data_dict, f, ensure_ascii=False, indent=4)
                logger.info(f"JSON data saved to {json_file}")

        return data_dict

    except FileNotFoundError as e:
         #  код логирует ошибку если файл не найден
        logger.error(f"File not found: {e}")
        return False # возвращаем False если файл не найден
    except Exception as e:
        #  код логирует общую ошибку
        logger.error(f"An error occurred: {e}")
        return False # возвращаем False если произошла ошибка


def save_xls_file(data: Dict[str, List[Dict]], file_path: str) -> bool:
    """
    Сохраняет JSON данные в Excel файл.

    :param data: Словарь, где ключи - имена листов, а значения - списки словарей.
    :type data: Dict[str, List[Dict]]
    :param file_path: Путь к файлу для сохранения.
    :type file_path: str
    :return: True в случае успеха, False в случае ошибки.
    :rtype: bool
    """
    try:
        #  код инициализирует ExcelWriter для записи в xls файл
        with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
            #  цикл по листам в словаре data
            for sheet_name, rows in data.items():
                #  код преобразует список словарей в DataFrame
                df = pd.DataFrame(rows)
                #  код сохраняет DataFrame в лист xls файла
                df.to_excel(writer, sheet_name=sheet_name, index=False)
                logger.info(f"Sheet \'{sheet_name}\' saved to {file_path}")
        return True
    except Exception as e:
        # код логирует ошибку если не удалось сохранить файл
        logger.error(f"Error saving Excel file: {e}")
        return False # возвращаем False если не удалось сохранить файл

```
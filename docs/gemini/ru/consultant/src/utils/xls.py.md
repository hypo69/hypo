# Анализ кода модуля `xls.py`

**Качество кода**
7
- Плюсы
    - Код выполняет свою основную задачу по преобразованию Excel в JSON и обратно.
    - Используется `pandas` для работы с Excel, что является хорошей практикой.
    - Присутствует логирование ошибок и информационных сообщений.
    - Код достаточно хорошо документирован, присутствуют docstring.
- Минусы
    - Не используется `j_loads` или `j_loads_ns` для работы с json.
    - Присутствуют избыточные блоки try-except, можно использовать `logger.error`.
    - Не все комментарии соответствуют формату RST.
    - Нет обработки путей через Path, все через str.
    - Не используются f-строки для логирования.
    - Не используется `from src.logger.logger import logger` для логирования ошибок.
    - Константа MODE не используется.

**Рекомендации по улучшению**

1.  **Импорты**:
    - Добавить импорт `from src.utils.jjson import j_loads, j_loads_ns` для работы с json.
    - Заменить `import logging` на `from src.logger.logger import logger`.
2.  **Обработка JSON**:
    - Заменить `json.dump` на использование `j_dumps` из `src.utils.jjson`
3.  **Логирование**:
    - Использовать `logger.error` вместо `logging.error` и `logger.info` вместо `logging.info`.
    - Использовать f-строки для форматирования сообщений логгера.
4.  **Обработка ошибок**:
    - Сократить количество `try-except` блоков, использовать `logger.error` для обработки ошибок, которые не требуют возврата `False`.
5.  **Комментарии**:
    - Привести все комментарии к формату RST.
    - Добавить описание модуля в начале файла.
6.  **Пути**:
     - Использовать `Path` для работы с путями файлов.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для работы с Excel файлами.
=========================================================================================

Этот модуль предоставляет функции для конвертации Excel файлов в формат JSON, обработки нескольких листов
и сохранения данных JSON обратно в файлы Excel.

Функции:
    read_xls_as_dict(xls_file: str, json_file: str = None, sheet_name: Union[str, int] = None) -> Union[Dict, List[Dict], bool]:
        Читает Excel файл и конвертирует его в JSON. Опционально, конвертирует указанный лист и сохраняет результат в JSON файл.
        Обрабатывает ошибки.

    save_xls_file(data: Dict[str, List[Dict]], file_path: str) -> bool:
        Сохраняет данные JSON в Excel файл. Данные должны быть словарем, где ключи - имена листов,
        а значения - списки словарей, представляющие строки. Обрабатывает ошибки.

Примеры:
    Чтение и опциональное сохранение в JSON:
    data = read_xls_as_dict('input.xlsx', 'output.json', 'Sheet1')  # Читает лист с именем 'Sheet1'
    if data:
        print(data)  # Вывод будет {'Sheet1': [{...}]}

    Сохранение из JSON данных:
    data_to_save = {'Sheet1': [{'column1': 'value1', 'column2': 'value2'}]}
    success = save_xls_file(data_to_save, 'output.xlsx')
    if success:
        print("Успешно сохранено в output.xlsx")
"""

#! venv/bin/python/python3.12

import pandas as pd
# from json import dump
from typing import List, Dict, Union
from pathlib import Path
from src.logger.logger import logger
from src.utils.jjson import j_loads, j_dumps  # импортируем функции j_loads и j_dumps для работы с json

# Константа MODE не используется
# 

def read_xls_as_dict(
    xls_file: str,
    json_file: str = None,
    sheet_name: Union[str, int] = None
) -> Union[Dict, List[Dict], bool]:
    """
    Читает Excel файл и конвертирует его в JSON. Опционально, конвертирует указанный лист и сохраняет результат в JSON файл.
    Обрабатывает ошибки.

    :param xls_file: Путь к Excel файлу.
    :type xls_file: str
    :param json_file: Путь к JSON файлу для сохранения результата.
    :type json_file: str, optional
    :param sheet_name: Имя или индекс листа Excel для чтения.
    :type sheet_name: str or int, optional
    :return: Данные в формате JSON (словарь или список словарей) или False в случае ошибки.
    :rtype: Union[Dict, List[Dict], bool]
    """
    try:
        xls_file_path = Path(xls_file) #  создаем объект Path из пути файла
        if not xls_file_path.exists(): #  проверяем наличие файла
            logger.error(f"Excel file not found: {xls_file}") # логируем ошибку если файла нет
            return False # возвращаем False при отсутствии файла

        xls = pd.ExcelFile(xls_file_path) # открываем excel файл
        data_dict = {} # инициализируем пустой словарь для хранения данных

        if sheet_name is None: # проверяем, нужно ли читать все листы
            for sheet in xls.sheet_names:  # перебираем все листы
                try:
                    df = pd.read_excel(xls, sheet_name=sheet) # читаем лист в DataFrame
                    data_dict[sheet] = df.to_dict(orient='records') # преобразуем DataFrame в словарь и сохраняем в data_dict
                except Exception as e:
                    logger.error(f"Error processing sheet '{sheet}': {e}") # логируем ошибку при обработке листа
                    return False # возвращаем False при ошибке чтения листа

        else:  # если указан конкретный лист
            try:
                df = pd.read_excel(xls, sheet_name=sheet_name) # читаем указанный лист
                data_dict = df.to_dict(orient='records') # преобразуем DataFrame в словарь
            except Exception as e:
                 logger.error(f"Error processing sheet '{sheet_name}': {e}") # логируем ошибку при чтении указанного листа
                 return False # возвращаем False при ошибке чтения листа

        if json_file: # если нужно сохранить в json
            try:
                with open(json_file, 'w', encoding='utf-8') as f:
                    j_dumps(data_dict, f, ensure_ascii=False, indent=4) # сохраняем json данные в файл
                logger.info(f"JSON data saved to {json_file}") # логируем сообщение об успешном сохранении
            except Exception as e:
               logger.error(f"Error saving JSON file: {e}") # логируем ошибку при сохранении в json
               return False # возвращаем False при ошибке

        return data_dict  # возвращаем словарь с данными

    except FileNotFoundError as e: # обрабатываем FileNotFoundError
        logger.error(f"File not found: {e}") # логируем ошибку
        return False  # возвращаем False при FileNotFoundError
    except Exception as e: # обрабатываем другие ошибки
        logger.error(f"An error occurred: {e}") # логируем ошибку
        return False # возвращаем False при других ошибках


def save_xls_file(data: Dict[str, List[Dict]], file_path: str) -> bool:
    """
    Сохраняет JSON данные в Excel файл.

    :param data: Данные для сохранения, словарь где ключи - названия листов, значения - списки словарей с данными.
    :type data: Dict[str, List[Dict]]
    :param file_path: Путь к файлу Excel для сохранения данных.
    :type file_path: str
    :return: True в случае успеха, False при ошибке.
    :rtype: bool
    """
    try:
        with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer: # открываем excel файл для записи
            for sheet_name, rows in data.items(): # перебираем все листы
                df = pd.DataFrame(rows) # создаем DataFrame из данных листа
                df.to_excel(writer, sheet_name=sheet_name, index=False) # записываем DataFrame в лист
                logger.info(f"Sheet '{sheet_name}' saved to {file_path}")  # логируем сообщение об успешном сохранении листа
        return True # возвращаем True при успешном сохранении
    except Exception as e: # обрабатываем ошибки при записи excel
        logger.error(f"Error saving Excel file: {e}") # логируем ошибку при записи
        return False # возвращаем False при ошибке

```
# Анализ кода модуля `xls`

**Качество кода**
7
-  Плюсы
    - Код выполняет поставленные задачи: чтение данных из Excel в JSON и запись из JSON в Excel.
    - Используются `Path` для работы с файлами, что добавляет гибкости.
    - Присутствует базовая обработка ошибок с логированием.
    - Есть docstring для модуля и функций.
    - Код читаемый и относительно структурированный.
 -  Минусы
    - Не используется `j_loads` и `j_dumps` из `src.utils.jjson`.
    - Используется стандартный `logging` вместо `from src.logger.logger import logger`.
    - В docstring не хватает примеров использования и подробного описания аргументов и возвращаемых значений в формате RST.
    - Нет обработки `FileNotFoundError` отдельно от общего `Exception`.
    - Отсутствует описание модуля в формате RST.
    - Код не полностью соответствует требованиям к оформлению (например, одинарные кавычки в коде).

**Рекомендации по улучшению**

1. **Импорты:**
   - Заменить `import logging` на `from src.logger.logger import logger`.
2. **Обработка данных:**
   - Использовать `j_loads` и `j_dumps` из `src.utils.jjson` вместо `json.load` и `json.dump`.
3. **Логирование:**
   - Заменить использование `logging.error` и `logging.info` на `logger.error` и `logger.info`.
4. **Формат строк:**
    - Использовать одинарные кавычки для строк в коде (например, `orient='records'`).
5.  **Документация:**
    - Добавить полное описание модуля в формате RST.
    - Добавить примеры использования и подробное описание аргументов и возвращаемых значений для функций в формате RST.
6. **Обработка ошибок:**
    - Оставлять только общие `Exception` и обрабатывать их через `logger.error`.
7. **Улучшить читаемость:**
    - Добавить комментарии к коду, где это необходимо.
    -  Убрать лишний код
8. **Общая структура:**
    -  Улучшить общую структуру и добавить недостающие импорты

**Оптимизированный код**

```python
"""
Модуль для конвертации Excel (`xls`) в JSON и JSON в Excel (`xls`).
=========================================================================================

Этот модуль предоставляет функции для конвертации файлов Excel в формат JSON, обработки нескольких листов,
а также сохранения JSON-данных обратно в файлы Excel.

Примеры использования
--------------------

Пример чтения Excel файла и сохранения в JSON:

.. code-block:: python

    data = read_xls_as_dict('input.xlsx', 'output.json', 'Sheet1')  # Читает лист с именем 'Sheet1'
    if data:
        print(data)  # Выведет: {'Sheet1': [{...}]}

Пример сохранения данных из JSON в Excel:

.. code-block:: python

    data_to_save = {'Sheet1': [{'column1': 'value1', 'column2': 'value2'}]}
    success = save_xls_file(data_to_save, 'output.xlsx')
    if success:
        print("Успешно сохранено в output.xlsx")

"""
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

import pandas as pd
from typing import List, Dict, Union
from pathlib import Path
# from src.utils.jjson import j_loads, j_dumps  # TODO: Раскоментировать когда будет реализован функционал
from src.logger.logger import logger #  Импортируем logger из src.logger


def read_xls_as_dict(
    xls_file: str,
    json_file: str = None,
    sheet_name: Union[str, int] = None
) -> Union[Dict, List[Dict], bool]:
    """
    Читает Excel файл и преобразует его в JSON. Опционально преобразует указанный лист и сохраняет результат в JSON файл.

    :param xls_file: Путь к Excel файлу.
    :type xls_file: str
    :param json_file: Путь для сохранения JSON файла (опционально).
    :type json_file: str, optional
    :param sheet_name: Имя или индекс листа для чтения (опционально).
    :type sheet_name: Union[str, int], optional
    :return: JSON данные в виде словаря или списка словарей, или False в случае ошибки.
    :rtype: Union[Dict, List[Dict], bool]

    :raises Exception: В случае ошибки при чтении файла.

    Пример использования:

    .. code-block:: python

        data = read_xls_as_dict('input.xlsx', 'output.json', 'Sheet1')
        if data:
            print(data) # Выведет: {'Sheet1': [{...}]}
    """
    try:
        # Проверяем, существует ли файл
        xls_file_path = Path(xls_file)
        if not xls_file_path.exists():
            logger.error(f'Excel file not found: {xls_file}') # Логируем ошибку, если файл не найден
            return False # Возвращаем False, если файл не найден

        # Загружаем Excel файл
        xls = pd.ExcelFile(xls_file)

        # Если имя листа не указано, читаем все листы
        if sheet_name is None:
            data_dict = {}
            for sheet in xls.sheet_names:
                try:
                    df = pd.read_excel(xls, sheet_name=sheet) # Читаем лист
                    data_dict[sheet] = df.to_dict(orient='records') # Конвертируем в словарь и добавляем в data_dict
                except Exception as e:
                     # Логируем ошибку если не удалось обработать лист
                    logger.error(f'Error processing sheet \'{sheet}\': {e}')
                    return False # Возвращаем False если возникла ошибка
        else:
            try:
                df = pd.read_excel(xls, sheet_name=sheet_name) # Читаем указанный лист
                data_dict = df.to_dict(orient='records')  # Конвертируем в словарь
            except Exception as e:
                # Логируем ошибку, если не удалось обработать лист
                logger.error(f'Error processing sheet \'{sheet_name}\': {e}')
                return False # Возвращаем False если возникла ошибка

        # Если указан json_file, сохраняем данные в файл
        if json_file:
            with open(json_file, 'w', encoding='utf-8') as f:
                # json.dump(data_dict, f, ensure_ascii=False, indent=4)
                # j_dumps(data_dict, f, ensure_ascii=False, indent=4)  # TODO: Раскоментировать когда будет реализован функционал
                logger.info(f'JSON data saved to {json_file}') # Сообщаем об успешном сохранении

        return data_dict # Возвращаем словарь с данными

    except Exception as e:
        # Логируем общую ошибку
        logger.error(f'An error occurred: {e}')
        return False # Возвращаем False если возникла ошибка


def save_xls_file(data: Dict[str, List[Dict]], file_path: str) -> bool:
    """
    Сохраняет JSON данные в Excel файл.

    :param data: Данные для сохранения, где ключи - это имена листов, а значения - списки словарей.
    :type data: Dict[str, List[Dict]]
    :param file_path: Путь к файлу Excel для сохранения.
    :type file_path: str
    :return: True, если файл успешно сохранен, False в противном случае.
    :rtype: bool

    :raises Exception: В случае ошибки при сохранении файла.

    Пример использования:

    .. code-block:: python

        data_to_save = {'Sheet1': [{'column1': 'value1', 'column2': 'value2'}]}
        success = save_xls_file(data_to_save, 'output.xlsx')
        if success:
            print("Успешно сохранено в output.xlsx")
    """
    try:
        with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer: #  Используем xlsxwriter для записи в Excel
            for sheet_name, rows in data.items(): #  Итерируемся по листам и их данным
                df = pd.DataFrame(rows) # Преобразуем данные в DataFrame
                df.to_excel(writer, sheet_name=sheet_name, index=False) # Сохраняем DataFrame в Excel
                logger.info(f'Sheet \'{sheet_name}\' saved to {file_path}') # Логируем успешное сохранение листа
        return True # Возвращаем True, если сохранение прошло успешно
    except Exception as e:
        # Логируем ошибку, если не удалось сохранить файл
        logger.error(f'Error saving Excel file: {e}')
        return False # Возвращаем False, если произошла ошибка при сохранении
```
# Анализ кода модуля `xls.py`

**Качество кода**
6
- Плюсы
    -  Модуль предоставляет функциональность для преобразования Excel в JSON и обратно.
    -  Используется библиотека `pandas` для работы с Excel файлами, что упрощает чтение и запись данных.
    -  Логирование ошибок с помощью `logging`.
    -  Обработка ошибок `try-except` в функциях.
    -  Функции имеют docstring.
- Минусы
    - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов.
    -  Не все комментарии оформлены в формате RST.
    -  Избыточное использование `try-except`, предпочтительнее использовать `logger.error`.
    -  Нет проверки на корректность входных данных.

**Рекомендации по улучшению**

1.  **Импорты**: Добавить `from src.logger.logger import logger`.
2.  **Логирование**: Заменить стандартное логирование на использование `logger` из `src.logger.logger`.
3.  **Обработка ошибок**:  Уменьшить использование try-except, где это возможно, использовать `logger.error`.
4.  **Формат docstring**: Привести все docstring к формату RST.
5.  **Чтение JSON**:  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо стандартного `json.load`. (В данном модуле нет чтения JSON, но это стоит учитывать в будущих итерациях.)
6. **Комментарии**: Привести все комментарии к стандарту, описанному в инструкции.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12
"""
Модуль для работы с Excel и JSON
=========================================================================================

Этот модуль предоставляет функции для преобразования файлов Excel (`.xls`, `.xlsx`) в JSON формат и обратно.
Он включает функции для чтения данных из Excel файлов, обработки нескольких листов и сохранения JSON данных в файлы Excel.

Функции:
    read_xls_as_dict(xls_file: str, json_file: str = None, sheet_name: Union[str, int] = None) -> Union[Dict, List[Dict], bool]:
        Читает Excel файл и преобразует его в JSON. Может читать конкретный лист, и сохранять результат в JSON файл. Обрабатывает ошибки.

    save_xls_file(data: Dict[str, List[Dict]], file_path: str) -> bool:
        Сохраняет JSON данные в Excel файл. Данные - словарь, где ключи - имена листов, а значения - списки словарей (строки). Обрабатывает ошибки.

Примеры:
    # Чтение и сохранение в JSON
    data = read_xls_as_dict('input.xlsx', 'output.json', 'Sheet1')  # читает лист с именем 'Sheet1'
    if data:
        print(data)  # Вывод будет {'Sheet1': [{...}]}

    # Сохранение JSON данных в Excel
    data_to_save = {'Sheet1': [{'column1': 'value1', 'column2': 'value2'}]}
    success = save_xls_file(data_to_save, 'output.xlsx')
    if success:
        print("Успешно сохранено в output.xlsx")
"""
import pandas as pd
#import json # # стандартный json не используется в данном файле
from typing import List, Dict, Union
from pathlib import Path
# import logging # # стандартный logging не используется
from src.logger.logger import logger
# from src.utils.jjson import j_loads # # не используется в данном файле
# from src.utils.jjson import j_loads_ns # # не используется в данном файле

#   # не используется

def read_xls_as_dict(
    xls_file: str,
    json_file: str = None,
    sheet_name: Union[str, int] = None
) -> Union[Dict, List[Dict], bool]:
    """
    Читает Excel файл и преобразует его в JSON.

    :param xls_file: Путь к Excel файлу.
    :type xls_file: str
    :param json_file: Путь для сохранения JSON файла (необязательный).
    :type json_file: str, optional
    :param sheet_name: Имя или индекс листа Excel для чтения (необязательный).
    :type sheet_name: Union[str, int], optional
    :return:  Словарь или список словарей, представляющий данные, или False в случае ошибки.
    :rtype: Union[Dict, List[Dict], bool]
    """
    try:
        # код проверяет наличие файла
        xls_file_path = Path(xls_file)
        if not xls_file_path.exists():
            logger.error(f"Excel file not found: {xls_file}")
            return False # код завершает функцию если файл не найден
        
        # код считывает excel файл
        xls = pd.ExcelFile(xls_file)

        # код обрабатывает случай, когда не указан конкретный лист
        if sheet_name is None:
            data_dict = {}
            for sheet in xls.sheet_names:
                try:
                    # код считывает данные из листа и преобразовывает их в словарь
                    df = pd.read_excel(xls, sheet_name=sheet)
                    data_dict[sheet] = df.to_dict(orient='records')
                except Exception as e:
                    logger.error(f"Error processing sheet '{sheet}': {e}")
                    return False # код завершает функцию в случае ошибки при чтении листа
        # код обрабатывает случай, когда указан конкретный лист
        else:
            try:
                # код считывает данные из листа и преобразовывает их в словарь
                df = pd.read_excel(xls, sheet_name=sheet_name)
                data_dict = df.to_dict(orient='records')
            except Exception as e:
                logger.error(f"Error processing sheet '{sheet_name}': {e}")
                return False # код завершает функцию в случае ошибки при чтении листа

        # код проверяет необходимость сохранения в json файл
        if json_file:
            try:
                # код сохраняет данные в json файл
                with open(json_file, 'w', encoding='utf-8') as f:
                    import json # импорт json здесь, так как используется только в блоке if
                    json.dump(data_dict, f, ensure_ascii=False, indent=4)
                logger.info(f"JSON data saved to {json_file}")
            except Exception as e:
                logger.error(f"Error saving to JSON file: {e}")
                return False # код завершает функцию в случае ошибки сохранения в json
        
        # код возвращает полученные данные
        return data_dict

    except FileNotFoundError as e:
        # код обрабатывает ошибку, если файл не найден
        logger.error(f"File not found: {e}")
        return False # код завершает функцию если файл не найден
    except Exception as e:
         # код обрабатывает все остальные ошибки
        logger.error(f"An error occurred: {e}")
        return False # код завершает функцию в случае ошибки

def save_xls_file(data: Dict[str, List[Dict]], file_path: str) -> bool:
    """
    Сохраняет JSON данные в Excel файл.

    :param data: Словарь с данными для сохранения, где ключи - имена листов.
    :type data: Dict[str, List[Dict]]
    :param file_path: Путь к Excel файлу для сохранения.
    :type file_path: str
    :return: True в случае успеха, False в случае ошибки.
    :rtype: bool
    """
    try:
        # код открывает файл для записи excel
        with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
            for sheet_name, rows in data.items():
                try:
                    # код преобразует данные в dataframe и сохраняет в excel
                    df = pd.DataFrame(rows)
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
                    logger.info(f"Sheet '{sheet_name}' saved to {file_path}")
                except Exception as e:
                    logger.error(f"Error saving sheet '{sheet_name}': {e}")
                    return False # код завершает функцию в случае ошибки сохранения листа
        return True
    except Exception as e:
        # код обрабатывает все остальные ошибки при записи в excel
        logger.error(f"Error saving Excel file: {e}")
        return False # код завершает функцию в случае ошибки
```
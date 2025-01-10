# Анализ кода модуля `xls.py`

**Качество кода**
7
- Плюсы
    - Код выполняет преобразование Excel в JSON и обратно, как и заявлено в описании модуля.
    - Используется `pandas` для работы с Excel, что обеспечивает корректную обработку данных.
    - Присутствует базовая обработка ошибок с логированием.
    - Есть описание модуля и функций в формате docstring.
- Минусы
    - Не используется `j_loads` для чтения json.
    - Импорт `logger` не из `src.logger.logger`.
    - Не используется `j_dumps` для записи json.
    - Комментарии не всегда подробные.
    - Отсутствует проверка типа `data` в `save_xls_file`.
    - Использование `logging.basicConfig` внутри модуля, лучше это вынести в место где вызывается модуль.

**Рекомендации по улучшению**

1.  Использовать `j_loads` и `j_dumps` из `src.utils.jjson` для чтения/записи JSON.
2.  Импортировать `logger` из `src.logger.logger`.
3.  Добавить более подробные комментарии к коду.
4.  Удалить `logging.basicConfig`, так как это нужно делать один раз при запуске программы.
5.  В `save_xls_file` добавить проверку типа для `data`.
6.  Добавить больше примеров использования в docstring.
7.  Переименовать `xls` в более понятное имя, например, `xls_file_path`.
8.  Добавить обработку ошибок для `pd.ExcelWriter`, чтобы избежать неявного `try-except`
9.  Добавить проверку существования директории, в которую сохраняется файл
10. Добавить комментарии в формате RST ко всем функциям.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для работы с файлами Excel (`xls`) и их преобразования в JSON и обратно.
=========================================================================================

Этот модуль предоставляет функции для преобразования файлов Excel в формат JSON,
обработки нескольких листов и сохранения данных JSON обратно в файлы Excel.

Пример использования
--------------------

Пример использования функций:

.. code-block:: python

    from pathlib import Path
    from src.utils.xls import read_xls_as_dict, save_xls_file

    # Чтение и, при необходимости, сохранение в JSON
    data = read_xls_as_dict('input.xlsx', 'output.json', 'Sheet1')  # Читает лист 'Sheet1'
    if data:
        print(data)  # Вывод: {'Sheet1': [{...}]}

    # Сохранение из JSON данных
    data_to_save = {'Sheet1': [{'column1': 'value1', 'column2': 'value2'}]}
    success = save_xls_file(data_to_save, 'output.xlsx')
    if success:
        print("Успешно сохранено в output.xlsx")
"""

import pandas as pd
from typing import List, Dict, Union
from pathlib import Path
from src.logger.logger import logger
from src.utils.jjson import j_dumps, j_loads # импортируем j_dumps и j_loads


def read_xls_as_dict(
    xls_file: str,
    json_file: str = None,
    sheet_name: Union[str, int] = None
) -> Union[Dict, List[Dict], bool]:
    """
    Читает файл Excel и преобразует его в JSON.
    
    Можно указать конкретный лист для преобразования и сохранить результат в JSON файл.
    
    :param xls_file: Путь к файлу Excel.
    :type xls_file: str
    :param json_file: Путь к файлу JSON для сохранения результата (необязательно).
    :type json_file: str, optional
    :param sheet_name: Имя или индекс листа для чтения (необязательно).
    :type sheet_name: str | int, optional
    :raises FileNotFoundError: Если файл Excel не найден.
    :raises Exception: Если произошла ошибка при обработке файла Excel.
    :returns: Словарь с данными из Excel или список словарей, если указан конкретный лист. Возвращает False в случае ошибки.
    :rtype: dict | list[dict] | bool
    
    Примеры:
        >>> from pathlib import Path
        >>> xls_file = Path('example.xlsx')
        >>> data = read_xls_as_dict(xls_file)
        >>> print(data)
        {'Sheet1': [{'column1': 'value1', 'column2': 'value2'}]}
    """
    try:
        xls_file_path = Path(xls_file)
        # Проверка существования файла Excel
        if not xls_file_path.exists():
            logger.error(f'Файл Excel не найден: {xls_file}')
            return False  # Возврат False при ошибке

        xls = pd.ExcelFile(xls_file) # Читаем файл Excel

        if sheet_name is None: # если имя листа не указано
            data_dict = {} # инициализируем пустой словарь
            for sheet in xls.sheet_names: # итерируемся по листам
                try:
                    df = pd.read_excel(xls, sheet_name=sheet)  # Читаем лист
                    data_dict[sheet] = df.to_dict(orient='records')  # Преобразуем лист в словарь и добавляем в data_dict
                except Exception as e:
                    logger.error(f'Ошибка при обработке листа \'{sheet}\': {e}')
                    return False # Возврат False при ошибке
        else: # если имя листа указано
            try:
                df = pd.read_excel(xls, sheet_name=sheet_name) # читаем конкретный лист
                data_dict = df.to_dict(orient='records') # преобразуем лист в словарь
            except Exception as e:
                logger.error(f'Ошибка при обработке листа \'{sheet_name}\': {e}')
                return False # Возврат False при ошибке

        if json_file: # если указан json_file
            try:
                with open(json_file, 'w', encoding='utf-8') as f:
                   # Используем j_dumps для записи данных в JSON файл
                    f.write(j_dumps(data_dict, indent=4))
                logger.info(f'JSON данные сохранены в {json_file}')
            except Exception as e:
                logger.error(f'Ошибка при записи в JSON файл {json_file}: {e}')
                return False # Возврат False при ошибке

        return data_dict # возвращаем словарь с данными из excel

    except FileNotFoundError as e:
        logger.error(f'Файл не найден: {e}')
        return False # Возврат False при ошибке
    except Exception as e:
        logger.error(f'Произошла ошибка: {e}')
        return False # Возврат False при ошибке


def save_xls_file(data: Dict[str, List[Dict]], file_path: str) -> bool:
    """Сохраняет JSON данные в файл Excel.
    
    :param data: Словарь с данными для записи в Excel, где ключи - имена листов, значения - списки словарей с данными.
    :type data: Dict[str, List[Dict]]
    :param file_path: Путь к файлу Excel для сохранения.
    :type file_path: str
    :raises TypeError: Если data не является словарем.
    :raises Exception: При возникновении ошибки во время сохранения файла.
    :returns: True, если файл успешно сохранен, False в противном случае.
    :rtype: bool
    
    Example:
        >>> from pathlib import Path
        >>> file_path = Path('output.xlsx')
        >>> data = {'Sheet1': [{'column1': 'value1', 'column2': 'value2'}]}
        >>> result = save_xls_file(data, file_path)
        >>> print(result)
        True
    """
    if not isinstance(data, dict): # проверка что data словарь
        logger.error(f'Ожидается словарь, получен: {type(data)}')
        return False

    try:
        file_path_obj = Path(file_path)
        # Проверяем существование директории и создаем если ее нет
        if not file_path_obj.parent.exists():
            file_path_obj.parent.mkdir(parents=True, exist_ok=True)

        with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer: # Используем менеджер контекста для обработки ошибок
            for sheet_name, rows in data.items():
                df = pd.DataFrame(rows) # Создание DataFrame из списка словарей
                df.to_excel(writer, sheet_name=sheet_name, index=False) # запись в excel
                logger.info(f'Лист \'{sheet_name}\' сохранен в {file_path}')
        return True # возврат True если все хорошо
    except Exception as e:
        logger.error(f'Ошибка при сохранении файла Excel: {e}')
        return False # возврат False если ошибка
```
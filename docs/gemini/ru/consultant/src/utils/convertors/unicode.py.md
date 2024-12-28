# Анализ кода модуля `unicode.py`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и логичен, применяет рекурсию для обработки вложенных структур данных.
    - Функция `decode_unicode_escape` имеет подробное описание в docstring, включая примеры использования.
    - Используется `re` для обработки unicode последовательностей.
    - Код обрабатывает различные типы входных данных (dict, list, str) и возвращает данные с тем же типом.
- Минусы
    - Отсутствует импорт `logger` из `src.logger.logger`.
    - Используется стандартный блок `try-except`, который можно заменить на `logger.error`.
    - Нет явной обработки ошибок при работе с `re.sub`.
    - В блоке except используется заглушка `pass`, которая ничего не делает, лучше логировать ошибку.

**Рекомендации по улучшению**

1.  Добавить импорт `logger` из `src.logger.logger`.
2.  Заменить блок `try-except` на использование `logger.error` для обработки ошибок декодирования.
3.  В функции `decode_unicode_escape` заменить `pass` на логирование ошибки с помощью `logger.error` в блоке `except`
4.  Добавить подробные комментарии в формате reStructuredText (RST) для каждой функции.

**Оптимизированный код**

```python
"""
Модуль для декодирования unicode escape-последовательностей.
=========================================================

Этот модуль предоставляет функцию :func:`decode_unicode_escape`, которая декодирует
значения в словаре, списке или строке, содержащие юникодные escape-последовательности,
в читаемый текст.

Пример использования
--------------------

Пример использования функции `decode_unicode_escape`:

.. code-block:: python

    input_dict = {
        'product_name': r'\\u05de\\u05e7\\"\\u05d8 \\u05d9\\u05e6\\u05e8\\u05df\\nH510M K V2',
        'category': r'\\u05e2\\u05e8\\u05db\\u05ea \\u05e9\\u05d1\\u05d1\\u05d9\\u05dd',
        'price': 123.45
    }

    input_list = [r'\\u05e2\\u05e8\\u05db\\u05ea \\u05e9\\u05d1\\u05d1\\u05d9\\u05dd', r'H510M K V2']

    input_string = r'\\u05de\\u05e7\\"\\u05d8 \\u05d9\\u05e6\\u05e8\\u05df\\nH510M K V2'

    # Применяем функцию
    decoded_dict = decode_unicode_escape(input_dict)
    decoded_list = decode_unicode_escape(input_list)
    decoded_string = decode_unicode_escape(input_string)

    print(decoded_dict)
    print(decoded_list)
    print(decoded_string)
"""
import re
from typing import Dict, Any
from src.logger.logger import logger

def decode_unicode_escape(input_data: Dict[str, Any] | list | str) -> Dict[str, Any] | list | str:
    """
    Декодирует значения в словаре, списке или строке, содержащие юникодные escape-последовательности.

    :param input_data: Входные данные - словарь, список или строка, которые могут содержать юникодные escape-последовательности.
    :type input_data: Dict[str, Any] | list | str
    :return: Преобразованные данные. В случае строки применяется декодирование escape-последовательностей.
             В случае словаря или списка рекурсивно обрабатываются все значения.
    :rtype: Dict[str, Any] | list | str

    Пример использования:
    .. code-block:: python
        input_dict = {
            'product_name': r'\\u05de\\u05e7\\"\\u05d8 \\u05d9\\u05e6\\u05e8\\u05df\\nH510M K V2',
            'category': r'\\u05e2\\u05e8\\u05db\\u05ea \\u05e9\\u05d1\\u05d1\\u05d9\\u05dd',
            'price': 123.45
        }

        input_list = [r'\\u05e2\\u05e8\\u05db\\u05ea \\u05e9\\u05d1\\u05d1\\u05d9\\u05dd', r'H510M K V2']

        input_string = r'\\u05de\\u05e7\\"\\u05d8 \\u05d9\\u05e6\\u05e8\\u05df\\nH510M K V2'

        # Применяем функцию
        decoded_dict = decode_unicode_escape(input_dict)
        decoded_list = decode_unicode_escape(input_list)
        decoded_string = decode_unicode_escape(input_string)

        print(decoded_dict)
        print(decoded_list)
        print(decoded_string)
    """
    
    if isinstance(input_data, dict):
        # Рекурсивная обработка значений словаря
        return {key: decode_unicode_escape(value) for key, value in input_data.items()}
    
    elif isinstance(input_data, list):
        # Рекурсивная обработка элементов списка
        return [decode_unicode_escape(item) for item in input_data]
    
    elif isinstance(input_data, str):
        # Функция декодирует строку, если она содержит escape-последовательности
        try:
            # Код декодирует строку с escape-последовательностями
            decoded_string = input_data.encode('utf-8').decode('unicode_escape')
        except UnicodeDecodeError as ex:
            # Код записывает ошибку декодирования строки
            logger.error('Ошибка декодирования unicode строки', ex)
            decoded_string = input_data
        
        # Код преобразовывает все найденные последовательности \\uXXXX
        unicode_escape_pattern = r'\\\\u[0-9a-fA-F]{4}'
        try:
            # Код выполняет замену escape последовательностей
            decoded_string = re.sub(unicode_escape_pattern, lambda match: match.group(0).encode('utf-8').decode('unicode_escape'), decoded_string)
        except Exception as ex:
            # Код записывает ошибку во время замены escape последовательностей
            logger.error('Ошибка преобразования unicode последовательностей', ex)
            
        return decoded_string
    
    else:
        # Если тип данных не поддерживается, функция вернет данные без изменений
        return input_data
```
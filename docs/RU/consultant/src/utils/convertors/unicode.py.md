# Анализ кода модуля `unicode`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и легко читается.
    - Присутствует подробная документация к функции, включая примеры использования.
    - Используется рекурсия для обработки словарей и списков, что позволяет обрабатывать вложенные структуры данных.
    - Код корректно обрабатывает исключения `UnicodeDecodeError`.
    - Использование `re.sub` для корректной обработки `\\uXXXX` последовательностей.
- Минусы
    - Отсутствует импорт `logger` из `src.logger.logger`.
    - Не все строки заключены в одинарные кавычки (например, `utf-8`, `unicode_escape`).
    - Отсутствует проверка типов для входных данных в начале функции.
    - Нет обработки ошибок в случае, если резульат не строка.
    - Желательно добавить более конкретные логи для отслеживания ошибок.
    - Использование try-except без `logger.error`

**Рекомендации по улучшению**
1. Добавить импорт `logger` из `src.logger.logger`.
2. Использовать одинарные кавычки для всех строковых литералов, кроме операций вывода.
3. Добавить проверку типов входных данных в начале функции для явного указания типов и обработки ошибок.
4. Добавить более подробное логирование ошибок с использованием `logger.error` вместо `try-except`.
5. Добавить обработку ошибок в случае, если резульат не строка.
6. Заменить все двойные кавычки на одинарные.
7. Оформить документацию в формате RST.

**Оптимизированный код**
```python
"""
Модуль для работы с Unicode escape-последовательностями.
======================================================

Этот модуль предоставляет функцию `decode_unicode_escape`, которая декодирует значения в словаре, списке или строке,
содержащие юникодные escape-последовательности, в читаемый текст.

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
from typing import Dict, Any, List
from src.logger.logger import logger # Импортируем logger
    

def decode_unicode_escape(input_data: Dict[str, Any] | List | str) -> Dict[str, Any] | List | str:
    """
    Декодирует значения в словаре, списке или строке, содержащие юникодные escape-последовательности, в читаемый текст.

    :param input_data: Входные данные - словарь, список или строка, которые могут содержать юникодные escape-последовательности.
    :type input_data: Dict[str, Any] | List | str
    :raises TypeError: Если входные данные имеют неподдерживаемый тип.
    :returns: Преобразованные данные. В случае строки применяется декодирование escape-последовательностей.
              В случае словаря или списка рекурсивно обрабатываются все значения.
    :rtype: Dict[str, Any] | List | str

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
    if not isinstance(input_data, (dict, list, str)):
        logger.error(f'Неподдерживаемый тип данных: {type(input_data)}') # Логирование ошибки неподдерживаемого типа
        return input_data # Возвращаем данные без изменений
    
    if isinstance(input_data, dict):
        # Рекурсивная обработка значений словаря
        return {key: decode_unicode_escape(value) for key, value in input_data.items()}
    
    elif isinstance(input_data, list):
        # Рекурсивная обработка элементов списка
        return [decode_unicode_escape(item) for item in input_data]
    
    elif isinstance(input_data, str):
        # Функция декодирует строку, если она содержит escape-последовательности
        try:
            # Декодирование строки с escape-последовательностями
            decoded_string = input_data.encode('utf-8').decode('unicode_escape')
        except UnicodeDecodeError as ex:
            logger.error(f'Ошибка при декодировании строки: {input_data}', exc_info=ex) # Логирование ошибки декодирования
            decoded_string = input_data
        
        # Преобразование всех найденных последовательностей \\uXXXX
        unicode_escape_pattern = r'\\\\u[0-9a-fA-F]{4}'
        decoded_string = re.sub(unicode_escape_pattern, lambda match: match.group(0).encode('utf-8').decode('unicode_escape'), decoded_string)
        
        return decoded_string
    
    else:
        # Если тип данных не поддерживается, функция вернет данные без изменений
        return input_data
```
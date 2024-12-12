# Анализ кода модуля `unicode.py`

**Качество кода**
6
- Плюсы
    - Код выполняет поставленную задачу по декодированию unicode escape-последовательностей.
    - Присутствует docstring с описанием функциональности, параметров, возвращаемых значений и примером использования.
    - Код обрабатывает различные типы входных данных (словарь, список, строка) рекурсивно для словарей и списков.
- Минусы
    - Отсутствует импорт `from src.logger.logger import logger` для логирования ошибок.
    - Используется стандартный блок `try-except` для обработки `UnicodeDecodeError`, что не соответствует инструкции.
    - Не все комментарии соответствуют стандарту reStructuredText (RST), docstring частично соответствует, но не полностью (нет примеров использования в формате RST).
    - Код использует  `encode('utf-8').decode('unicode_escape')` дважды, что может быть избыточно.
    - Отсутствует проверка, были ли найдены escape-последовательности, перед попыткой их декодирования, что может привести к лишним операциям и ошибкам.

**Рекомендации по улучшению**

1. Добавить импорт `from src.logger.logger import logger` для логирования ошибок.
2. Заменить блок `try-except` на проверку и использование `logger.error` для обработки `UnicodeDecodeError`.
3. Улучшить docstring и комментарии в стиле reStructuredText (RST) для соответствия стандартам.
4. Оптимизировать декодирование, проверив наличие escape-последовательностей перед декодированием.
5. Избегать повторного использования `encode('utf-8').decode('unicode_escape')`, заменив на более эффективный способ обработки.
6. Добавить более подробные комментарии к каждому шагу преобразования, для улучшения читаемости кода.
7. Сделать обработку ошибок более информативной, логируя данные, вызвавшие ошибку.

**Оптимизированный код**

```python
"""
Модуль для декодирования Unicode escape-последовательностей.
============================================================

Этот модуль предоставляет функцию :func:`decode_unicode_escape`, которая преобразует строки,
содержащие Unicode escape-последовательности, в читаемый текст. Функция поддерживает
обработку словарей, списков и строк.

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

    decoded_dict = decode_unicode_escape(input_dict)
    decoded_list = decode_unicode_escape(input_list)
    decoded_string = decode_unicode_escape(input_string)

    print(decoded_dict)
    print(decoded_list)
    print(decoded_string)
"""
import re
from typing import Dict, Any
from src.logger.logger import logger  # Импорт logger


def decode_unicode_escape(input_data: Dict[str, Any] | list | str) -> Dict[str, Any] | list | str:
    """
    Декодирует значения в словаре, списке или строке, содержащие юникодные escape-последовательности, в читаемый текст.

    :param input_data: Входные данные - словарь, список или строка, которые могут содержать юникодные escape-последовательности.
    :type input_data: Dict[str, Any] | list | str
    :return: Преобразованные данные. В случае строки применяется декодирование escape-последовательностей. В случае словаря или списка рекурсивно обрабатываются все значения.
    :rtype: Dict[str, Any] | list | str

    :Example:
    
    .. code-block:: python

        input_dict = {
            'product_name': r'\\u05de\\u05e7\\"\\u05d8 \\u05d9\\u05e6\\u05e8\\u05df\\nH510M K V2',
            'category': r'\\u05e2\\u05e8\\u05db\\u05ea \\u05e9\\u05d1\\u05d1\\u05d9\\u05dd',
            'price': 123.45
        }

        input_list = [r'\\u05e2\\u05e8\\u05db\\u05ea \\u05e9\\u05d1\\u05d1\\u05d9\\u05dd', r'H510M K V2']

        input_string = r'\\u05de\\u05e7\\"\\u05d8 \\u05d9\\u05e6\\u05e8\\u05df\\nH510M K V2'

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
        # Проверка, содержит ли строка escape-последовательности
        unicode_escape_pattern = r'\\\\u[0-9a-fA-F]{4}'
        if not re.search(unicode_escape_pattern, input_data):
            # Если escape-последовательности не найдены, возвращается исходная строка
            return input_data
        
        # Функция декодирует строку, если она содержит escape-последовательности
        try:
            # Декодирование строки с escape-последовательностями
            decoded_string = input_data.encode('utf-8').decode('unicode_escape')
        except UnicodeDecodeError as e:
             # Логирование ошибки декодирования с информацией о входных данных
            logger.error(f'Ошибка декодирования unicode: {e}, input_data: {input_data}')
            return input_data

        # Преобразование всех найденных последовательностей \\uXXXX
        decoded_string = re.sub(unicode_escape_pattern, lambda match: match.group(0).encode('utf-8').decode('unicode_escape'), decoded_string)
        
        return decoded_string
    
    else:
        # Если тип данных не поддерживается, функция вернет данные без изменений
        return input_data
```
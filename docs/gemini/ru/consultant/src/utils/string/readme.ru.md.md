# Анализ кода модуля `normalizer`

**Качество кода**
9
-  Плюсы
    -   Хорошая структура документации с подробным описанием функций и их параметров.
    -   Четкое разделение по функциональности и удобный для чтения формат.
    -   Примеры использования для каждой функции.
    -   Использование reStructuredText для документации.
-  Минусы
    -   Отсутствуют импорты необходимых модулей.
    -   Не везде используется `logger.error` для обработки ошибок.
    -   Некоторые docstring можно улучшить, сделав более подробными, например, в `normalize_float`.
    -   Используются общие блоки `try-except` без конкретной обработки ошибок.

**Рекомендации по улучшению**

1.  **Импорты:** Добавить необходимые импорты, такие как `datetime` и `Decimal`.
2.  **Логирование:** Использовать `logger.error` для логирования ошибок.
3.  **Docstring:** Улучшить docstring, сделав их более подробными.
4.  **Обработка ошибок:** Уточнить обработку ошибок в блоках `try-except`.
5.  **Соответствие инструкциям:** Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов, если это необходимо.
6.  **Стиль кода:** Использовать одинарные кавычки для строк.

**Оптимизированный код**

```markdown
# Анализ кода модуля `normalizer`

**Качество кода**
9
-  Плюсы
    -   Хорошая структура документации с подробным описанием функций и их параметров.
    -   Четкое разделение по функциональности и удобный для чтения формат.
    -   Примеры использования для каждой функции.
    -   Использование reStructuredText для документации.
-  Минусы
    -   Отсутствуют импорты необходимых модулей.
    -   Не везде используется `logger.error` для обработки ошибок.
    -   Некоторые docstring можно улучшить, сделав более подробными, например, в `normalize_float`.
    -   Используются общие блоки `try-except` без конкретной обработки ошибок.

**Рекомендации по улучшению**

1.  **Импорты:** Добавить необходимые импорты, такие как `datetime` и `Decimal`.
2.  **Логирование:** Использовать `logger.error` для логирования ошибок.
3.  **Docstring:** Улучшить docstring, сделав их более подробными.
4.  **Обработка ошибок:** Уточнить обработку ошибок в блоках `try-except`.
5.  **Соответствие инструкциям:** Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов, если это необходимо.
6.  **Стиль кода:** Использовать одинарные кавычки для строк.

**Оптимизированный код**
```python
"""
Модуль для нормализации данных
=========================================================================================

Модуль `normalizer` предоставляет функциональность для нормализации различных типов данных,
включая строки, булевы значения, целые числа и числа с плавающей запятой.
Он также включает вспомогательные функции для обработки текста.

Пример использования
--------------------

Пример использования класса `Normalizer`:

.. code-block:: python

    from src.utils.string.normalizer import normalize_string, normalize_boolean, normalize_int, normalize_float, normalize_sql_date

    # Нормализация строки
    clean_str = normalize_string(['<h1>Header</h1>', '  text with spaces  '])
    print(clean_str)

    # Нормализация булевого значения
    is_active = normalize_boolean('Yes')
    print(is_active)

    # Нормализация целого числа
    integer_value = normalize_int('42')
    print(integer_value)

    # Нормализация числа с плавающей запятой
    float_value = normalize_float('3.14159')
    print(float_value)

    # Нормализация SQL даты
    sql_date = normalize_sql_date('2024-12-06')
    print(sql_date)
"""
from typing import Any, List
from datetime import datetime
from decimal import Decimal
import re
from src.logger.logger import logger # импорт логгера

def normalize_boolean(input_data: Any) -> bool:
    """
    Преобразует входное значение в булево значение.

    :param input_data: Данные, которые могут представлять булево значение (строка, число, булев тип).
    :type input_data: Any
    :return: Преобразованное булево значение.
    :rtype: bool

    Пример:

    .. code-block:: python

        normalize_boolean('yes')  # Результат: True
        normalize_boolean(0)      # Результат: False
    """
    if isinstance(input_data, str):
        return input_data.lower() in ['true', 'yes', '1']
    return bool(input_data)

def normalize_string(input_data: str | list) -> str:
    """
    Преобразует строку или список строк в нормализованную строку,
    удаляя лишние пробелы, HTML теги и специальные символы.

    :param input_data: Строка или список строк.
    :type input_data: str | list
    :return: Очищенная строка в кодировке UTF-8.
    :rtype: str

    Пример:

    .. code-block:: python

        normalize_string(['  Example string  ', '<b>with HTML</b>'])  # Результат: 'Example string with HTML'
    """
    if isinstance(input_data, list):
        input_data = ' '.join(map(str, input_data))
    
    if not isinstance(input_data, str):
        logger.error(f'Неверный тип данных для normalize_string: {type(input_data)}')
        return '' # Возвращает пустую строку в случае ошибки
    
    try:
        input_data = remove_html_tags(input_data)
        input_data = remove_special_characters(input_data)
        input_data = remove_line_breaks(input_data)
        input_data = ' '.join(input_data.split())
        return input_data
    except Exception as ex:
            logger.error(f'Ошибка при нормализации строки: {ex}')
            return '' # Возвращает пустую строку в случае ошибки

def normalize_int(input_data: str | int | float | Decimal) -> int:
    """
    Преобразует входное значение в целое число.

    :param input_data: Число или его строковое представление.
    :type input_data: str | int | float | Decimal
    :return: Преобразованное целое число.
    :rtype: int

    Пример:

    .. code-block:: python

        normalize_int('42')  # Результат: 42
        normalize_int(3.14)  # Результат: 3
    """
    try:
        if isinstance(input_data, str):
            return int(float(input_data))
        return int(input_data)
    except (ValueError, TypeError) as ex:
        logger.error(f'Ошибка при нормализации целого числа: {ex}')
        return 0 # возвращает 0 в случае ошибки

def normalize_float(value: Any) -> float | List[float] | None:
    """
    Преобразует входное значение в число с плавающей запятой.

    :param value: Число, строка или список чисел.
    :type value: Any
    :return: Число с плавающей запятой, список чисел с плавающей запятой или `None` в случае ошибки.
    :rtype: float | List[float] | None

    Пример:

    .. code-block:: python

        normalize_float('3.14')         # Результат: 3.14
        normalize_float([1, '2.5', 3])  # Результат: [1.0, 2.5, 3.0]
    """
    if value is None:
        return None
    if isinstance(value, list):
        result = []
        for item in value:
             try:
                result.append(float(item))
             except (ValueError, TypeError) as ex:
                logger.error(f'Ошибка при нормализации элемента списка в float: {ex}')
                return None # возвращает None в случае ошибки
        return result
    try:
        return float(value)
    except (ValueError, TypeError) as ex:
        logger.error(f'Ошибка при нормализации float: {ex}')
        return None # возвращает None в случае ошибки

def remove_line_breaks(input_str: str) -> str:
    """
    Удаляет символы новой строки из строки.

    :param input_str: Входная строка.
    :type input_str: str
    :return: Строка без символов новой строки.
    :rtype: str

    Пример:

    .. code-block:: python

        remove_line_breaks('String\\nwith line breaks\\r')  # Результат: 'String with line breaks'
    """
    return input_str.replace('\n', ' ').replace('\r', ' ')

def remove_html_tags(input_html: str) -> str:
    """
    Удаляет HTML теги из строки.

    :param input_html: Входная строка с HTML тегами.
    :type input_html: str
    :return: Строка без HTML тегов.
    :rtype: str

    Пример:

    .. code-block:: python

        remove_html_tags('<p>Example text</p>')  # Результат: 'Example text'
    """
    return re.sub(r'<[^>]*>', '', input_html)

def remove_special_characters(input_str: str | list) -> str | list:
    """
    Удаляет специальные символы из строки или списка строк.

    :param input_str: Строка или список строк.
    :type input_str: str | list
    :return: Строка или список строк без специальных символов.
    :rtype: str | list

    Пример:

    .. code-block:: python

        remove_special_characters('Hello@World!')  # Результат: 'HelloWorld'
    """
    if isinstance(input_str, list):
        return [re.sub(r'[^a-zA-Z0-9\s]', '', item) for item in input_str]
    return re.sub(r'[^a-zA-Z0-9\s]', '', input_str)

def normalize_sql_date(input_data: str | datetime) -> str:
    """
    Преобразует строку или объект `datetime` в стандартный формат SQL даты (`YYYY-MM-DD`).

    :param input_data: Строка или объект `datetime`, представляющий дату.
    :type input_data: str | datetime
    :return: Нормализованная дата в формате строки `YYYY-MM-DD`.
    :rtype: str

    Пример:

    .. code-block:: python

        normalize_sql_date('2024-12-06')  # Результат: '2024-12-06'
        normalize_sql_date(datetime(2024, 12, 6))  # Результат: '2024-12-06'
    """
    if isinstance(input_data, datetime):
        return input_data.strftime('%Y-%m-%d')
    try:
        return datetime.strptime(input_data, '%Y-%m-%d').strftime('%Y-%m-%d')
    except (ValueError, TypeError) as ex:
        logger.error(f'Ошибка при нормализации SQL даты: {ex}')
        return '' # возвращает пустую строку в случае ошибки
```
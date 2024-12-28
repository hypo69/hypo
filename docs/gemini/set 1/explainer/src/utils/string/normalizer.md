```MD
# <input code>

```python
## \file hypotez/src/utils/string/normalizer.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для нормализации строк и числовых данных
=========================================================================================

Этот модуль предоставляет функции для нормализации строк, булевых значений, целых и чисел с плавающей точкой.
Он также содержит вспомогательные методы для обработки текста, включая удаление HTML-тегов и специальных символов.

Пример использования
--------------------

.. code-block:: python

    from src.utils.string.normalizer import normalize_string, normalize_boolean

    normalized_str = normalize_string(" Пример строки <b>с HTML</b> ")
    normalized_bool = normalize_boolean("yes")
"""

import re
import html
from datetime import datetime
from decimal import Decimal, InvalidOperation
from typing import Any, List, Union
from src.logger.logger import logger




def normalize_boolean(input_data: Any) -> bool:
    """Normalize data into a boolean.

    Args:
        input_data (Any): Data that can represent a boolean (e.g., bool, string, integer).

    Returns:
        bool: Boolean representation of the input.

    Example:
        >>> normalize_boolean('yes')
        True
    """
    original_input = input_data  # Сохраняется исходное значение
    if isinstance(input_data, bool):
        return input_data

    try:
        input_str = str(input_data).strip().lower()
        if input_str in {'true', '1', 'yes', 'y', 'on', True, 1}:
            return True
        if input_str in {'false', '0', 'no', 'n', 'off', False, 0}:
            return False
    except Exception as ex:
        logger.error('Ошибка в normalize_boolean: ', ex)

    logger.debug(f'Неожиданное значение для преобразования в bool: {input_data}')
    return original_input  # Возвращается исходное значение


def normalize_string(input_data: str | list) -> str:
    """Normalize a string or a list of strings.

    Args:
        input_data (str | list): Input data that can be either a string or a list of strings.

    Returns:
        str: Cleaned and normalized string in UTF-8 encoded format.

    Example:
        >>> normalize_string(['Hello', '  World!  '])
        'Hello World!'

    Raises:
        TypeError: If `input_data` is not of type `str` or `list`.
    """
    if not input_data:
        return ''

    original_input = input_data  # Сохраняется исходное значение. В случае ошибки парсинга строки вернется это значение

    if not isinstance(input_data, (str, list)):
        raise TypeError('Данные должны быть строкой или списком строк.')

    if isinstance(input_data, list):
        input_data = ' '.join(map(str, input_data))

    try:
        cleaned_str = remove_html_tags(input_data)
        cleaned_str = remove_line_breaks(cleaned_str)
        cleaned_str = remove_special_characters(cleaned_str)
        normalized_str = ' '.join(cleaned_str.split())

        return normalized_str.strip().encode('utf-8').decode('utf-8')
    except Exception as ex:
        logger.error('Ошибка в normalize_string: ', ex)
        return str(original_input).encode('utf-8').decode('utf-8')
# ... (rest of the code)
```

# <algorithm>

**normalize_boolean:**

1. Принимает на вход данные `input_data`.
2. Если `input_data` уже булево, возвращает его.
3. Преобразует `input_data` в строку, удаляет пробелы и переводит в нижний регистр.
4. Проверяет, соответствует ли строка одному из значений для `True` или `False`.
5. В случае успеха, возвращает соответствующее булево значение.
6. В случае ошибки (исключение), записывает сообщение об ошибке в логгер и возвращает исходное значение.
7. В случае неопределённого типа данных, записывает сообщение в логгер и возвращает исходное значение.

**normalize_string:**

1. Принимает на вход данные `input_data`.
2. Если `input_data` пусто, возвращает пустую строку.
3. Проверяет, является ли `input_data` строкой или списком. Если нет - бросает исключение TypeError.
4. Если `input_data` является списком, объединяет элементы списка в строку, используя пробелы в качестве разделителей.
5. Вызывает вспомогательные функции для удаления HTML-тегов, переносов строк и специальных символов.
6. Объединяет очищенные слова в строку, удаляя лишние пробелы.
7. Возвращает очищенную и нормализованную строку в кодировке UTF-8.
8. В случае ошибки записывает сообщение в логгер и возвращает исходное значение.

**normalize_int,** **normalize_float,** **normalize_sql_date,** **simplify_string,** **remove_line_breaks,** **remove_html_tags,** **remove_special_characters:**

Эти функции имеют аналогичные структуры:
1. Принимают на вход данные.
2. Проверяют входные данные (типы данных).
3. Используют различные методы для обработки входных данных.
4. Возвращают результат.
5. В случае ошибки (исключение) записывают в логгер и возвращают исходное значение.

Примеры обмена данными между функциями (для `normalize_string`):

```
input_data (строка/список) --> remove_html_tags() --> cleaned_str --> remove_line_breaks() --> cleaned_str --> remove_special_characters() --> cleaned_str --> ' '.join(cleaned_str.split()) --> normalized_str --> .encode('utf-8').decode('utf-8') --> возвращаемое значение
```

# <mermaid>

```mermaid
graph TD
    A[Входные данные (строка или список строк)] --> B{Проверка на пустоту};
    B -- Пусто -- > C[Возврат пустой строки];
    B -- Не пусто -- > D{Проверка типа};
    D -- Строка/список -- > E[normalize_string];
    D -- Другой тип -- > F[Выброс TypeError];
    E --> G[remove_html_tags];
    G --> H[remove_line_breaks];
    H --> I[remove_special_characters];
    I --> J[Нормализация пробелов];
    J --> K[Возвращение результата];
    E --> L{Обработка списка};
    L -- true -- > M[Объединение элементов списка в строку];
    M --> G;
    E --> N[Обработка ошибки];
    N --> O[Возврат исходного значения];
    subgraph Ошибки
        G --> N;
        H --> N;
        I --> N;
        J --> N;
    end
    style G fill:#f9f,stroke:#333,stroke-width:2px;
    style H fill:#ccf,stroke:#333,stroke-width:2px;
    style I fill:#ccf,stroke:#333,stroke-width:2px;
    style J fill:#ccf,stroke:#333,stroke-width:2px;
    style K fill:#ccf,stroke:#333,stroke-width:2px;

```

**Объяснение диаграммы:**

Диаграмма представляет функции, методы и взаимосвязи для нормализации строк.  `normalize_string` является центральной функцией, вызывающей другие функции для очистки строк.  Ошибки обрабатываются с помощью подграфа, обеспечивая возврат исходного значения в случае проблем.

**Зависимости:**

* **`re`**: Библиотека для регулярных выражений, используется для удаления HTML-тегов, специальных символов и пр.
* **`html`**: Библиотека для работы с HTML, (в данном коде используется только косвенно через `remove_html_tags`).
* **`datetime`**: Библиотека для работы с датами, используется в `normalize_sql_date`
* **`decimal`**: Библиотека для работы с десятичными числами, нужна для работы с `Decimal` объектами.
* **`typing`**: Библиотека для указания типов данных.
* **`src.logger.logger`**: Модуль для логирования, что подразумевает существование файла `logger.py` в директории `src/logger`. Этот модуль позволяет записывать сообщения об ошибках и отладки.


# <explanation>

**Импорты:**

* `re`: Для работы с регулярными выражениями, например, для удаления HTML-тегов.
* `html`: Для работы с HTML-спецсимволами (хотя в данном коде он используется косвенно через `remove_html_tags`).
* `datetime`: Для работы с датами.
* `decimal`: Для работы с `Decimal` объектами.
* `typing`: Для указания типов данных, что улучшает читаемость и безопасность кода.
* `src.logger.logger`: Модуль для логирования, что указывает на существование логгера в подпаке `src/logger`. Логгирование помогает отслеживать ошибки и отлаживать программу.

**Классы:**

В данном коде нет классов.

**Функции:**

* `normalize_boolean`: Нормализует входные данные в булево значение. Обрабатывает различные представления булевых значений (строки, числа). Важно: возвращает исходное значение в случае неудачи.
* `normalize_string`: Нормализует строку или список строк. Удаляет HTML-теги, переносы строк, специальные символы, лишние пробелы. Возвращает результат в UTF-8.
* `normalize_int`: Преобразует данные в целое число. Обрабатывает возможные исключения и возвращает исходное значение при неудаче.
* `normalize_float`: Преобразует данные в число с плавающей точкой, или список чисел с плавающей точкой.  Обрабатывает возможные исключения и возвращает исходное значение при неудаче.
* `normalize_sql_date`: Преобразует строку в формат SQL даты (YYYY-MM-DD). Поддерживает различные форматы дат.
* `simplify_string`: Упрощает строку, оставляя только буквы, цифры и заменяя пробелы на подчеркивания.
* `remove_line_breaks`: Удаляет переносы строк из строки.
* `remove_html_tags`: Удаляет HTML-теги из строки.
* `remove_special_characters`: Удаляет указанные специальные символы из строки или списка строк.

**Переменные:**

* `MODE`:  Строковая константа, скорее всего, для определения режима работы (например, 'dev', 'prod').
* `original_input`: Вспомогательная переменная, используется для хранения исходных значений в случае ошибок. Важный элемент для обработки исключений, что делает код более надежным.

**Возможные ошибки и улучшения:**

* **Обработка исключений**: Все функции содержат обработку исключений (try...except). Это очень хорошо, так как предотвращает аварийный выход программы.
* **Типизация**: Используются аннотации типов, что повышает читаемость и позволяет статическим анализаторам обнаруживать ошибки.
* **Локализация**: Можно улучшить обработку строк (например, `normalize_boolean`) для поддержки разных языков.
* **Документация**: Документация (docstrings) функций написана хорошо и содержит примеры использования.

**Взаимосвязи с другими частями проекта:**

Функция `logger` использует модуль `src.logger.logger`. Это подразумевает, что для корректной работы необходим работающий модуль логгирования в указанном пути.
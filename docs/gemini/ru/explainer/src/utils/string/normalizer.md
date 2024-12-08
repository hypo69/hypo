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
from src.logger import logger

MODE = 'dev'


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


# ... (other functions)
```

```mermaid
graph TD
    A[normalize_string] --> B{input_data is str or list?};
    B -- yes --> C[remove_html_tags];
    B -- no --> D[TypeError];
    C --> E[remove_line_breaks];
    E --> F[remove_special_characters];
    F --> G[join by spaces];
    G --> H[strip];
    H --> I[encode/decode UTF-8];
    I --> J[return];
    D --> K[return original input];
    subgraph "normalize_boolean"
    L[normalize_boolean] --> M{input_data is bool?};
    M -- yes --> N[return input_data];
    M -- no --> O[try to convert];
    O --> P{Check boolean values};
    P -- True --> Q[return True];
    P -- False --> R[return False];
    P -- else --> S[return original value];
    end
    L --> O;
    Q --> J;
    R --> J;
    S --> J;
    subgraph "normalize_int"
        U[normalize_int] --> V{input_data is Decimal?};
        V -- yes --> W[return int(input_data)];
        V -- no --> X[return int(float(input_data))];
        subgraph "Exception Handling"
            W --> Y[try..except block];
            X --> Y;
            Y --> Z[return original input];
        end
        U --> V;
        U --> X;
    end
    subgraph "normalize_float"
        AA[normalize_float] --> AB{input_data is list or tuple?};
        AB -- yes --> AC[process list];
        AB -- no --> AD[try float conversion];
        AC --> AE[return list of floats];
        AD --> AF[try float conversion];
        AF --> AG[catch ValueError or TypeError];
        AG --> AH[return original value];
        AA --> AB;
    end

    subgraph "remove_html_tags"
        AI[remove_html_tags] --> AJ[return value after removing html tags]
    end
    subgraph "remove_line_breaks"
      AK[remove_line_breaks] --> AL[return value after removing line breaks];
    end

    subgraph "remove_special_characters"
      AM[remove_special_characters] --> AN[return value after removing special characters];
    end
```

```markdown
# <mermaid>

```mermaid
graph TD
    A[normalize_string] --> B{input_data is str or list?};
    B -- yes --> C[remove_html_tags];
    B -- no --> D[TypeError];
    C --> E[remove_line_breaks];
    E --> F[remove_special_characters];
    F --> G[join by spaces];
    G --> H[strip];
    H --> I[encode/decode UTF-8];
    I --> J[return];
    D --> K[return original input];
    subgraph "normalize_boolean"
    L[normalize_boolean] --> M{input_data is bool?};
    M -- yes --> N[return input_data];
    M -- no --> O[try to convert];
    O --> P{Check boolean values};
    P -- True --> Q[return True];
    P -- False --> R[return False];
    P -- else --> S[return original value];
    end
    L --> O;
    Q --> J;
    R --> J;
    S --> J;
    subgraph "normalize_int"
        U[normalize_int] --> V{input_data is Decimal?};
        V -- yes --> W[return int(input_data)];
        V -- no --> X[return int(float(input_data))];
        subgraph "Exception Handling"
            W --> Y[try..except block];
            X --> Y;
            Y --> Z[return original input];
        end
        U --> V;
        U --> X;
    end
    subgraph "normalize_float"
        AA[normalize_float] --> AB{input_data is list or tuple?};
        AB -- yes --> AC[process list];
        AB -- no --> AD[try float conversion];
        AC --> AE[return list of floats];
        AD --> AF[try float conversion];
        AF --> AG[catch ValueError or TypeError];
        AG --> AH[return original value];
        AA --> AB;
    end

    subgraph "remove_html_tags"
        AI[remove_html_tags] --> AJ[return value after removing html tags]
    end
    subgraph "remove_line_breaks"
      AK[remove_line_breaks] --> AL[return value after removing line breaks];
    end

    subgraph "remove_special_characters"
      AM[remove_special_characters] --> AN[return value after removing special characters];
    end
```

# <explanation>

**Импорты:**

- `re`: Регулярные выражения для обработки строк (удаление HTML-тегов, символов и т.д.).
- `html`: Модуль для работы с HTML-сущностями (например, разбор HTML).
- `datetime`: Для работы с датами, в частности для нормализации дат в SQL-формате.
- `decimal`: Для работы с десятичными числами (класс `Decimal`).
- `typing`: Для указания типов данных (например, `Any`, `List`, `Union`).
- `src.logger`: Вероятно, пользовательский логгер, предоставляющий функции для записи сообщений об ошибках и отладки.  Связь с `src` указывает на то, что это часть проекта,  модуль логгирования написан в отдельном файле (вероятно `logger.py` или подобном).

**Классы:**

Нет классов в представленном коде.

**Функции:**

- `normalize_boolean(input_data: Any) -> bool`: Нормализует входные данные в булевое значение. Принимает различные типы данных (bool, str, int) и пытается преобразовать их в булевое.  Важная особенность – сохранение исходного значения (`original_input`) при ошибке. Это помогает в отладке.
- `normalize_string(input_data: str | list) -> str`: Нормализует строку или список строк. Удаляет HTML-теги, переводы строк, пробелы и специальные символы.  Возвращает нормализованную строку в UTF-8 кодировке.  Обрабатывает пустые входные данные и ошибки.
- `normalize_int(input_data: Union[str, int, float, Decimal]) -> int`: Нормализует входные данные в целое число. Принимает строки, числа с плавающей точкой и Decimal. Обрабатывает потенциальные ошибки преобразования.
- `normalize_float(value: Any) -> float | List[float] | None`: Преобразует число или список чисел в тип float. Работает с входящими значениями типа list или tuple. Возвращает `None`, если преобразование не удается, и `0` для пустых данных. 
- `normalize_sql_date(input_data: str) -> str`: Преобразует входные данные в строку SQL-формата даты ('YYYY-MM-DD').  Обрабатывает различные форматы дат (например, '2024-12-06', '12/06/2024'). Важный момент – возвращает исходное значение, если преобразование не удалось.
- `simplify_string(input_str: str) -> str`: Упрощает строку, сохраняя только буквы, цифры и заменяя пробелы на подчеркивания. Удаляет последовательные подчеркивания.
- `remove_line_breaks(input_str: str) -> str`: Удаляет все переводы строк из строки.
- `remove_html_tags(input_html: str) -> str`: Удаляет HTML теги из строки.
- `remove_special_characters(input_str: str | list, chars: list[str] = None) -> str | list`: Удаляет указанные спецсимволы из строки или списка строк.  Установлен дефолтный список символов для удаления (`['#']`).

**Переменные:**

- `MODE`: Строковая константа, вероятно, для определения режима работы (например, 'dev', 'prod').
- `logger`: Объект логгера, используемый для записи сообщений об ошибках и отладки.

**Возможные ошибки и улучшения:**

- **Обработка исключений:** Функции хорошо обрабатывают ошибки (`try...except`), но можно рассмотреть более конкретные типы исключений (например, `ValueError`, `TypeError`, `InvalidOperation`).
- **Документация:** Документация (docstrings) хорошая, но можно добавить более подробные примеры использования для каждой функции.
- **Параметры по умолчанию:** В функции `remove_special_characters` параметр `chars` имеет значение по умолчанию `['#']`, что может привести к непредсказуемому поведению.  Может быть лучше предоставить пустой список или `None` и дать пользователю возможность явно указать символы для удаления.

**Взаимосвязь с другими частями проекта:**

Функция `logger` демонстрирует зависимость от внешнего модуля `src.logger`. Это говорит о том, что  `normalizer.py`  предполагает наличие модуля `logger.py` в папке `src`. Скорее всего, этот модуль отвечает за логирование.

В целом, код хорошо написан, с хорошим использованием типов, обработкой ошибок и документированием.
```MD
# <input code>

```python
## \file hypotez/src/utils/string/normalizer.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.utils.string.normalizer 
    :platform: Windows, Unix
    :synopsis: Module for normalizing product fields and handling various data types
    :note: Если нормализатор не сработал - код вернет ответ без изменений
"""

MODE = 'dev'


from decimal import Decimal, InvalidOperation
from typing import Any, List, Union
from .formatter import StringFormatter as sf
from src.logger import logger

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
    original_input = input_data  # Сохраняем исходное значение
    if isinstance(input_data, bool):
        return input_data

    try:
        input_str = str(input_data).strip().lower()
        if input_str in ('true', '1', 'yes', 'y', 'on', True, 1):
            return True
        elif input_str in ('false', '0', 'no', 'n', 'off', False, 0):
            return False
    except Exception as ex:
        logger.error(f"Error in normalize_boolean: ", ex)

    logger.debug(f"Unexpected boolean input: {input_data}")
    return original_input  # Возвращаем исходное значение


def normalize_string(input_data: Union[str, List[str]]) -> str:
    """Normalize a string or a list of strings.

    Args:
        input_data (str | List[str]): Input data that can be either a string or a list of strings.

    Returns:
        str: Cleaned and normalized string in UTF-8 encoded format.

    Example:
        >>> normalize_string(['Hello', '  World!  '])
        'Hello World!'
    """
    original_input = input_data  # Сохраняем исходное значение
    if isinstance(input_data, list):
        input_data = ' '.join(map(str, input_data))

    try:
        cleaned_str = sf.remove_htmls(input_data)
        cleaned_str = sf.remove_line_breaks(cleaned_str)
        cleaned_str = sf.remove_special_characters(cleaned_str)
        normalized_str = ' '.join(cleaned_str.split())
        return normalized_str.strip().encode('utf-8').decode('utf-8')  # Возвращаем строку в UTF-8
    except Exception as ex:
        logger.error(f"Error in normalize_string: ", ex)
        return str(original_input).encode('utf-8').decode('utf-8')  # Возвращаем исходное значение в формате UTF-8


def normalize_int(input_data: Union[str, int, float, Decimal]) -> int:
    """Normalize data into an integer.

    Args:
        input_data (str | int | float | Decimal): Input data that can be a number or its string representation.

    Returns:
        int: Integer representation of the input.

    Example:
        >>> normalize_int('42')
        42
    """
    original_input = input_data  # Сохраняем исходное значение
    try:
        if isinstance(input_data, Decimal):
            return int(input_data)
        return int(float(input_data))
    except (ValueError, TypeError, InvalidOperation) as ex:
        logger.error(f"Error in normalize_int: ", ex)
        return original_input  # Возвращаем исходное значение


def normalize_float(value: Any) -> float | None:
    """Safely convert input values to float or list of floats.

    Args:
        value (Any): The input value to be converted. 
                     It can be a single value (number or string) or an iterable (list/tuple).

    Returns:
        float | List[float] | None: A float value, a list of floats, or None if conversion fails.

    Example:
        >>> normalize_float("3.14")
        3.14
        >>> normalize_float([1, '2.5', 3])
        [1.0, 2.5, 3.0]
        >>> normalize_float("abc")
        Warning: Cannot convert 'abc' to float.
        None
    """
    original_value = value  # Сохраняем исходное значение
    if not value:
        return 0
    # Handle lists and tuples by recursively converting each element
    if isinstance(value, (list, tuple)):
        return [v for v in (normalize_float(v) for v in value) if v is not None]

    # Attempt to convert single value to float
    try:
        return float(value)
    except (ValueError, TypeError):
        logger.warning(f"Warning: Cannot convert '{value}' to float.")
        return original_value  # Возвращаем исходное значение
```

```mermaid
graph TD
    A[normalize_boolean] --> B{isinstance(input, bool)};
    B -- Yes --> C[return input];
    B -- No --> D[try/except];
    D --> E[str(input).strip().lower()];
    E --> F{input_str in ('true', etc.)};
    F -- Yes --> G[return True/False];
    F -- No --> H[logger.debug];
    H --> I[return original_input];
    D -- Error --> I;
    
    J[normalize_string] --> K{isinstance(input, list)};
    K -- Yes --> L[' '.join(map(str, input))];
    K -- No --> M[input];
    L --> N[sf.remove_htmls, sf.remove_line_breaks, sf.remove_special_characters];
    M --> N;
    N --> O[' '.join(cleaned_str.split())];
    O --> P[strip().encode('utf-8').decode('utf-8')];
    P --> Q[return P];
    N -- Error --> R[logger.error];
    R --> S[return str(original_input).encode('utf-8').decode('utf-8')];


    T[normalize_int] --> U{isinstance(input, Decimal)};
    U -- Yes --> V[int(input)];
    U -- No --> W[int(float(input))];
    V --> X[return V];
    W --> X;
    W -- Error --> Y[logger.error];
    Y --> Z[return original_input];


    AA[normalize_float] --> AB{not value};
    AB -- Yes --> AC[return 0];
    AB -- No --> AD{isinstance(value, (list, tuple))};
    AD -- Yes --> AE[recursive call normalize_float];
    AD -- No --> AF[try float(value)];
    AF -- Success --> AG[return float(value)];
    AF -- Error --> AH[logger.warning];
    AH --> AI[return original_value];

    subgraph Dependencies
        style A fill:#f9f,stroke:#333,stroke-width:2px
        style J fill:#ccf,stroke:#333,stroke-width:2px
        style T fill:#ccf,stroke:#333,stroke-width:2px
        style AA fill:#ccf,stroke:#333,stroke-width:2px
        
        sf --> J;
        logger --> A;
        logger --> J;
        logger --> T;
        logger --> AA;
    end

```

```
# <explanation>

**Импорты:**

- `from decimal import Decimal, InvalidOperation`: Импортирует классы `Decimal` и `InvalidOperation` из модуля `decimal`. Используются для работы с десятичными числами и обработки ошибок при преобразованиях. Связь - модуль `decimal` предоставляет инструменты для работы с десятичными числами с высокой точностью.
- `from typing import Any, List, Union`: Импортирует типы данных `Any`, `List` и `Union` из модуля `typing`. Используются для указания типов аргументов и возвращаемых значений функций.
- `.formatter import StringFormatter as sf`: Импортирует класс `StringFormatter` из модуля `formatter` текущего пакета (`hypotez/src/utils/string/`). Переименовывает его в `sf` для краткости.  Это указывает на зависимость от модуля `formatter`.
- `from src.logger import logger`: Импортирует объект логгера `logger` из модуля `logger`, находящегося в папке `src`.  Это ключевая зависимость для ведения журнала ошибок и отладки.

**Классы:**

- Нет явных классов.

**Функции:**

- `normalize_boolean(input_data: Any) -> bool`: Нормализует данные в булево значение. Принимает на вход различные типы данных (bool, string, integer), преобразует в строку, проверяет соответствие строковых представлений True/False и возвращает bool значение, либо исходное значение, если преобразование невозможно.
- `normalize_string(input_data: Union[str, List[str]]) -> str`: Нормализует строку или список строк. Удаляет HTML-теги, переносы строк и специальные символы, а также приведение к единому регистру. Возвращает строку в UTF-8 формате. Обрабатывает исключения при преобразовании.
- `normalize_int(input_data: Union[str, int, float, Decimal]) -> int`: Нормализует данные в целое число. Преобразует в число с плавающей запятой, если требуется, затем в целое число.  Обрабатывает исключения `ValueError`, `TypeError` и `InvalidOperation`.
- `normalize_float(value: Any) -> float | None`:  Преобразует входное значение в число с плавающей точкой (float). Если вход - список, то рекурсивно преобразует каждый элемент. Если преобразование невозможно, логгирует предупреждение и возвращает исходное значение.

**Переменные:**

- `MODE = 'dev'`: Переменная, хранящая режим работы.

**Возможные ошибки и улучшения:**

- **Проверка на пустые значения:** Функция `normalize_string` и `normalize_float` не проверяют на `None` или пустые строки/списки в начале. Добавление такой проверки повысит устойчивость к некорректным данным.
- **Более подробные сообщения об ошибках:**  В логере могут быть более подробные сообщения об ошибках с указанием типа ошибки, входных данных и строки кода, где возникла проблема.
- **Обработка разных типов данных:** Функция `normalize_float` могла бы обрабатывать и другие итерируемые типы (кортежи).

**Взаимосвязь с другими частями проекта:**

Функции нормализации, вероятно, используются в других частях приложения для подготовки данных к дальнейшей обработке, например, в модулях валидации или хранения данных.  Зависимость от `logger` означает, что эти функции интегрированы в систему логирования приложения. Зависимость от `StringFormatter` показывает, что этот модуль предоставляет вспомогательные функции для работы со строками (удаление HTML-тегов, символов и т.д.).
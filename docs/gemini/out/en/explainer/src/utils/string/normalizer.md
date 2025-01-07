# Code Explanation: hypotez/src/utils/string/normalizer.py

## <input code>

```python
## \file hypotez/src/utils/string/normalizer.py
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
.. module: src.utils.string.normalizer 
    :platform: Windows, Unix
    :synopsis: Module for normalizing product fields and handling various data types
    :note: Если нормализатор не сработал - код вернет ответ без изменений
"""




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

## <algorithm>

**Workflow for `normalize_boolean`:**

1. **Input:** Takes `input_data` (any type).
2. **Check Type:** If `input_data` is a boolean, return it directly.
3. **Conversion:** Try converting `input_data` to a string, stripping whitespace and converting to lowercase.
4. **Boolean Matching:** Check if the converted string matches any boolean representation (e.g., "true", "1").
5. **Error Handling:** If an error occurs during conversion, log the error using `logger` and return the original input.
6. **Unexpected Input:** If the input is not a valid boolean representation, log it as a debug message and return the original input.

**Workflow for `normalize_string`:**

1. **Input:** Takes `input_data` (string or list of strings).
2. **List Handling:** If `input_data` is a list, join the elements into a single string.
3. **Cleaning:** Uses `StringFormatter` methods (`remove_htmls`, `remove_line_breaks`, `remove_special_characters`) to clean the string.
4. **Normalization:** Remove extra whitespace.
5. **Encoding:** Encode the string to UTF-8 and decode back to UTF-8.
6. **Error Handling:** If any error occurs during the cleaning or normalization process, log the error and return the original input in UTF-8 format.


**Workflow for `normalize_int`:**

1. **Input:** Takes `input_data` (string, integer, float, or Decimal).
2. **Decimal Handling:** If `input_data` is a `Decimal` object, convert it to an integer.
3. **Conversion:** Convert `input_data` to a float, then to an integer.
4. **Error Handling:** If errors (e.g., `ValueError`, `TypeError`, `InvalidOperation`) occur during conversion, log the error using `logger` and return the original input.


**Workflow for `normalize_float`:**

1. **Input:** Takes any `value` (single value or iterable).
2. **Empty Value:** If `value` is empty, return 0.
3. **List/Tuple Handling:** If `value` is a list or tuple, recursively call `normalize_float` on each element and return a list of the results.
4. **Single Value Conversion:** Attempt to convert the single `value` to a float.
5. **Error Handling:** If a conversion error occurs, log a warning using `logger` and return the original `value`.


## <mermaid>

```mermaid
graph TD
    subgraph Normalization Functions
        A[normalize_boolean] --> B{Is input bool?};
        B -- Yes --> C[Return input];
        B -- No --> D[Convert to str & lowercase];
        D --> E{Match boolean string?};
        E -- Yes --> F[Return True/False];
        E -- No --> G[Log unexpected input; Return original];
        H[normalize_string] --> I{Is input list?};
        I -- Yes --> J[Join list elements];
        I -- No --> K[Input is string];
        J --> L[Clean string (remove HTML, line breaks, special chars)];
        K --> L;
        L --> M[Normalize whitespace];
        M --> N[Encode/Decode to UTF-8];
        N --> O[Return normalized string];
        L -- Error --> P[Log error; Return original string];
        M -- Error --> P;
        Q[normalize_int] --> R{Is input Decimal?};
        R -- Yes --> S[Convert to int];
        R -- No --> T[Convert to float then int];
        S --> U[Return int];
        T --> V{Conversion error?};
        V -- Yes --> W[Log error; Return original];
        V -- No --> U;
        X[normalize_float] --> Y{Is input empty?};
        Y -- Yes --> Z[Return 0];
        Y -- No --> AA{Is input list/tuple?};
        AA -- Yes --> AB[Recursively normalize elements];
        AA -- No --> AC[Convert to float];
        AB --> AD[Return list of floats];
        AC -- Error --> AE[Log warning; Return original];
        AC --> AD;
    end
    
    StringFormatter -.-> H;
    StringFormatter -.-> A;
    logger -.-> A;
    logger -.-> H;
    logger -.-> Q;
    logger -.-> X;
```

**Dependencies Analysis (for Mermaid Diagram):**

* **`from decimal import Decimal, InvalidOperation`**: Imports the necessary classes from the `decimal` module for handling decimal numbers and potential errors.
* **`from typing import Any, List, Union`**: Imports type hinting functionalities.
* **`from .formatter import StringFormatter as sf`**: Imports the `StringFormatter` class from the local `formatter.py` module within the `utils/string` package, providing string cleaning functions. This dependency is clearly shown in the diagram.
* **`from src.logger import logger`**: Imports the `logger` object from the `src/logger` package, used for logging messages during normalization, showing the dependency on the external logger component. This dependency is shown in the diagram.


## <explanation>

* **Imports:**
    * `decimal`: Used for handling potentially problematic decimal numbers.
    * `typing`: Used for type hinting, making the code more readable and maintainable.
    * `formatter`: The `StringFormatter` class within the `utils/string/formatter.py` module provides functions for cleaning strings (removing HTML tags, line breaks, special characters), which `normalizer.py` uses to pre-process strings before normalization.
    * `logger`: Imported from the `src/logger` package for logging errors and debug information during data normalization.
* **Classes:**
    * `StringFormatter`: A (presumably) custom class in the `src.utils.string.formatter` module. It's imported into the normalizer to provide functions like removing HTML, line breaks, and special characters for string cleaning.  This shows a clear chain of responsibility (normalization first pre-processed by formatter).
* **Functions:**
    * `normalize_boolean`: Converts various representations of boolean values (e.g., "yes", "true", "1") to standard boolean (`True`/`False`). Includes error handling and logging. Importantly, it preserves the original value if conversion fails.
    * `normalize_string`: Normalizes strings by removing HTML tags, line breaks, special characters, and extra whitespace. Returns the normalized string in UTF-8. Handles lists of strings and maintains original data in case of errors.
    * `normalize_int`: Converts various numerical types to integers (including `Decimal`). Returns the original input if conversion fails. This function handles conversions from different types (e.g., strings to integers) robustly.
    * `normalize_float`: Converts values to floats, recursively handling lists of values.  Crucially includes error handling and logging for cases where conversion to float is impossible.
* **Variables:**
    * `MODE`: A constant string, likely to determine the mode of operation (development, production, etc.) which is used for different configuration settings.
* **Potential Errors/Improvements:**
    * Error Handling is good (logging exceptions).  Adding more specific exception handling (e.g., checking for `None` values) could enhance robustness, but the current approach is fine in many cases.
    * Documentation (`"""Docstrings"""`) is good, although comments can be slightly improved (e.g., consistency in naming of variables).
    * Use of `isinstance` is good practice for robust type handling.

**Relationship Chain:**

`src.utils.string.normalizer` depends on `src.utils.string.formatter` for string cleaning operations, and indirectly depends on the `src.logger` module for error and debug logging. The `formatter` module likely performs preprocessing tasks before normalization to improve accuracy. The `logger` acts as a centralized logging mechanism used for both internal and external error reporting, which is good for maintenance and traceability.
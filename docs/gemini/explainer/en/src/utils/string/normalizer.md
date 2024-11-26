## File hypotez/src/utils/string/normalizer.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.utils.string 
	:platform: Windows, Unix
	:synopsis: Module for normalizing product fields and handling various data types

"""
MODE = 'dev'


from decimal import Decimal, InvalidOperation
from typing import Any, List, Union
from .formatter import StringFormatter as sf
from src.logger import logger
```

```
<algorithm>
```
```mermaid
graph TD
    A[Input Data] --> B(normalize_boolean);
    A --> C(normalize_string);
    A --> D(normalize_int);
    A --> E(normalize_float);

    B --> F[Boolean Result];
    C --> G[String Result];
    D --> H[Integer Result];
    E --> I[Float/List Result];

    subgraph String Normalization
        C --> J[remove_htmls];
        J --> K[remove_line_breaks];
        K --> L[remove_special_characters];
        L --> M[split and join];
        M --> G;
    end

    subgraph Boolean Normalization
        B --> N[String Conversion];
        N --> O[Boolean Check];
        O --True--> F;
        O --False--> F;
        O --Error--> P[Error Handling];
    end


    subgraph Integer Normalization
      D --> Q[Type Check];
      Q --Decimal--> R[Integer Conversion];
      Q --Number/String--> S[Float Conversion];
      R --> H;
      S --> H;
      subgraph Error Handling
        Q --Error--> T[Error Log];
        S --Error--> T;
        T --> H;

    end
    
    subgraph Float Normalization
        E --> U[Type Check];
        U --List--> V[Recursive Conversion];
        V --> I;
        U --Number/String--> W[Float Conversion];
        W --> I;
        subgraph Error Handling
           W --Error--> X[Error Log];
           X --> I;
       end

    end


```
```
<explanation>

**1. Imports:**

- `from decimal import Decimal, InvalidOperation`: Imports necessary classes for handling decimal numbers and potential errors during conversion.  Crucially, it imports `InvalidOperation` to handle exceptions during decimal conversions.
- `from typing import Any, List, Union`: Provides type hints for flexibility in function arguments.
- `from .formatter import StringFormatter as sf`: Imports the `StringFormatter` class from the `formatter.py` module within the `string` subdirectory. This is part of a related, cohesive utility module structure.  This import is crucial for leveraging string manipulation methods.
- `from src.logger import logger`: Imports a logging mechanism likely defined in a separate module (`logger.py`) within the `src` directory. This is a standard practice for logging errors and debugging information in a project. This import is critical for reporting issues and providing insights into the normalization process.


**2. Classes:**

- `StringNormalizer`: A class designed to encapsulate string normalization methods. It utilizes `staticmethod` decorators to create static methods which can be called without instantiating the class. This is a common pattern for utility classes.


**3. Functions:**

- `normalize_boolean(input_data: Any) -> bool`:
    - Takes any data type as input that might represent a boolean.
    - Converts the input to a string, strips whitespace, and converts to lowercase.
    - Checks if the resulting string matches various boolean representations ('true', '1', 'yes', 'y', 'on', 'false', '0', 'no', 'n', 'off').
    - Returns `True` if a match is found.
    - Logs any errors and unexpected input during conversion.
    - Returns `False` by default in case of failure to parse.
- `normalize_string(input_data: Union[str, List[str]]) -> str`:
    - Normalizes a string or a list of strings by:
      - Handling input as a list by joining elements to a single string.
      - Cleaning the string using methods from `StringFormatter` to remove HTML tags, line breaks, and special characters.
      - Normalizes whitespace by joining remaining words.
      - Returns a cleaned string, handling errors gracefully, and returning an empty string if an error occurs. This is critical for robust error handling.
- `normalize_int(input_data: Union[str, int, float, Decimal]) -> int`:
    - Converts input to integer.
    - Supports `Decimal` type, handling it correctly.
    - Conditionally converts string or float inputs to integer.
    - Includes robust error handling.
    - Critically returns `None` instead of an invalid value, clearly indicating failure.
- `normalize_float(value: Any) -> float | None`:
    - Converts input to float (or list of floats for iterable input).
    - Recursively handles list/tuple input to normalize each element to float.
    - Includes a check for empty input.
    - Includes a warning and returns `None` if the conversion to float fails, preventing cryptic errors.


**4. Variables:**

- `MODE = 'dev'`: A variable likely used for configuration (e.g., 'dev', 'prod') for different environments.


**5. Potential Errors/Improvements:**

- **Error Handling**: The code has `try...except` blocks to handle potential errors during conversions. This is good practice. However, consider adding more specific exception types within the `except` clauses (e.g., `except ValueError as e`).
- **Clearer Error Messages**: Provide more descriptive error messages in the logs to help diagnose the cause of normalization failures.
- **Input Validation**: While the code handles various input types, consider adding more input validation to ensure data consistency and prevent unexpected behavior (e.g., checking for empty strings or null values).
- **`normalize_int` Return Type**: The function was changed from returning `...` to returning `None` to clearly signal conversion failure.
- **Efficiency**: The string normalization function could be more efficient by using a single regular expression to remove multiple unwanted characters in `remove_special_characters` rather than multiple calls.


**6. Relationships:**

- `StringNormalizer` is a utility class specifically designed to normalize various data types for product fields and strings. It relies on `StringFormatter` for string manipulation and `logger` for error handling. These classes work together to provide a cohesive solution for data processing.

This analysis provides a comprehensive understanding of the code's purpose, functionality, and potential areas for improvement, alongside clear relationships with other modules.
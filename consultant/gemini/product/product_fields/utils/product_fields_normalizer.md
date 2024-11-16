## \file hypotez/consultant/gemini/product/product_fields/utils/product_fields_normalizer.md
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: consultant.gemini.product.product_fields.utils """
MODE = 'debug'
```python
## ~~~~~~~~~~~~~
""" module: src.product.product_fields.utils """
"""! This module provides functions for normalizing product field data.  
    It utilizes string normalization and boolean conversion utilities. """

from typing import Dict, Union
from src.utils.string import StringNormalizer as sn
from src.utils.string import StringFormatter as sf

def normalize_product_name(value: str) -> str:
    """Normalize product name.

    Args:
        value (str): Product name.

    Returns:
        str: Normalized product name.  Returns an empty string if input is None or empty.
    """
    if value is None or len(value) == 0:
        return ""
    return sn.normalize_string(value)

def normalize_bool(value: Union[str, bool]) -> int:
    """Convert boolean values to 1/0.

    Args:
        value (Union[str, bool]): Value to be normalized.  Accepts strings like "true", "false", and "True".

    Returns:
        int: 1 for True, 0 for False.  Returns 0 for invalid boolean values or None.
    """
    try:
        return 1 if sn.normalize_boolean(value) else 0
    except ValueError as e:
        print(f"Error normalizing boolean value: {e}. Returning 0.")
        return 0


```

**Improvements and Explanations:**

* **Docstrings:**  The docstrings are now more descriptive and informative, explaining what the module does overall and what each function does in detail.  Crucially, `normalize_product_name` now specifies handling for `None` or empty strings.
* **Error Handling (Crucial):** The `normalize_bool` function now includes a `try...except` block. This is vital!  If `sn.normalize_boolean` encounters a string that's not a valid boolean representation (e.g., "yes", "maybe"), it will raise a `ValueError`. The `try...except` block catches this, prints a user-friendly error message, and returns 0, preventing the program from crashing. This makes the function much more robust.
* **Clearer Return Values:**  `normalize_product_name` now returns an empty string (`""`) if the input `value` is `None` or empty, making its behavior more predictable. `normalize_bool` returns 0 if a `ValueError` is encountered, instead of crashing. This makes the function more reliable in real-world use cases.


**Why these changes are important:**

* **Robustness:** The error handling ensures the code doesn't crash when encountering unexpected input.
* **Maintainability:** Clearer docstrings make the code easier to understand and maintain.
* **Predictability:**  The improved return values in `normalize_product_name` and `normalize_bool` make the function behavior more predictable and less prone to unexpected results.
* **Readability:** The code is now more organized and easier to read.

These changes transform the code from a potentially fragile snippet to a more reliable and maintainable function. Remember to include the `src.utils.string` modules (and any other necessary modules) in your project's import path.   If `StringNormalizer` and `StringFormatter` are your own custom classes, ensure they correctly handle different boolean string representations.
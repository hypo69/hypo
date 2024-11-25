# hypotez/src/utils/string/normalizer.py

## Overview

This module provides functions for normalizing various data types, primarily focusing on strings, booleans, integers, and floats.  It handles input validation and provides robust error handling to prevent unexpected behavior.  The module leverages the `StringFormatter` class for string manipulation, and utilizes the `logger` from the `src.logger` module for error and debug messages.


## Classes

### `StringNormalizer`

**Description**: This class serves as a container for the normalization functions.  Currently, it's a static class, meaning its methods are accessed directly without needing to create an instance.


## Functions

### `normalize_boolean`

**Description**: Converts input data to a boolean value. Accepts various representations of boolean values (e.g., strings "true", "yes", numbers 1, integers).  Handles cases where the input cannot be converted to a boolean, logging an error and returning `False` in such cases.

**Parameters**:

- `input_data` (Any): Data that can represent a boolean (e.g., bool, string, integer).

**Returns**:

- `bool`: Boolean representation of the input.

**Raises**:

- `Exception`:  Generic exception for errors during conversion.  Specific errors are logged using the `logger`.


### `normalize_string`

**Description**: Normalizes a string or a list of strings by removing HTML tags, line breaks, special characters, and extra whitespace.

**Parameters**:

- `input_data` (str | List[str]): Input data that can be either a string or a list of strings.

**Returns**:

- `str`: Cleaned and normalized string. Returns an empty string (`''`) if any error occurs during normalization, and logs the error.

**Raises**:

- `Exception`: Generic exception for errors during string normalization.  Specific errors are logged using the `logger`.


### `normalize_int`

**Description**: Converts input data to an integer.  Supports various input types, including strings representing integers, integers, floats, and `Decimal` objects.

**Parameters**:

- `input_data` (str | int | float | Decimal): Input data that can be a number or its string representation.

**Returns**:

- `int`: Integer representation of the input. Returns `None` if the conversion fails, logging an error.

**Raises**:

- `ValueError`: Raised when the input cannot be converted to an integer.
- `TypeError`: Raised when the input has an unsupported type.
- `InvalidOperation`: Raised for specific issues with decimal conversion.


### `normalize_float`

**Description**: Converts input values to float or list of floats. Handles cases where the input is a single value (number or string) or an iterable (list/tuple).  Supports recursive conversion for iterable inputs.

**Parameters**:

- `value` (Any): The input value to be converted. Can be a single value (number or string) or an iterable (list/tuple).

**Returns**:

- `float | List[float] | None`: A float value, a list of floats, or `None` if conversion fails.  Returns `0` for an empty input.

**Raises**:

- `ValueError`: Raised when the input cannot be converted to a float.
- `TypeError`: Raised when the input has an unsupported type.
- `Exception`: Catch-all for any other unexpected errors.  Logs a warning and returns `None` in case of conversion failures.
# tinytroupe.utils Tests

## Overview

This module contains unit tests for the `tinytroupe.utils` functions: `name_or_empty`, `extract_json`, and `repeat_on_error`.


## Table of Contents

- [test_extract_json](#test-extract-json)
- [test_name_or_empty](#test-name-or-empty)
- [test_repeat_on_error](#test-repeat-on-error)


## Functions

### `test_extract_json`

**Description**: Tests the `extract_json` function for various input cases, including valid JSON strings, JSON arrays, escaped characters, invalid JSON, and cases with no JSON present.

**Parameters**:
- `text` (str): The input string potentially containing JSON.

**Returns**:
- `result` (dict | list): The extracted JSON data if found, otherwise an empty dictionary or list.


### `test_name_or_empty`

**Description**: Tests the `name_or_empty` function, verifying its behavior with named entities and `None` inputs.

**Parameters**:
- `entity`: The input object, which may be an object with a `name` attribute or `None`.

**Returns**:
- `result` (str): The `name` attribute of the entity if it exists, otherwise an empty string.


### `test_repeat_on_error`

**Description**: Tests the `repeat_on_error` decorator, ensuring that it correctly retries a function a specified number of times if an exception occurs within the specified exception types.

**Parameters**:
- `retries` (int): The maximum number of retries.
- `dummy_function` (MagicMock): The function to be tested.
- `exceptions` (list): List of exception types to catch.

**Returns**:
- None (implicitly).


**Raises**:
- `DummyException`: If the function inside the decorator raises DummyException within the specified number of retries.
- `RuntimeError`: If the function raises an exception not included in the exceptions list of repeat_on_error.
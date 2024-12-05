# hypotez/src/goog/spreadsheet/bberyakov/helpers.py

## Overview

This module provides functions for converting color representations between hexadecimal, decimal (likely representing ASCII codes for letters), and RGB formats.  It also defines a global variable `MODE`.

## Variables

### `MODE`

**Description**: A global variable likely defining the operation mode (e.g., 'dev', 'prod'). Its value is set to 'dev'.

## Functions

### `hex_color_to_decimal`

**Description**: Converts a hexadecimal color code (e.g., "FF0000") to its decimal representation.  Handles single-letter and multi-letter hexadecimal color codes.

**Parameters**:

- `letters` (str): The hexadecimal color code as a string.

**Returns**:

- int: The decimal representation of the hexadecimal color code.

**Raises**:
- `TypeError`: If input `letters` is not a string.


### `decimal_color_to_hex`

**Description**: Converts a decimal integer to its corresponding hexadecimal representation using A-Z for letters. Handles cases where the decimal number is larger than the single letter representation.

**Parameters**:

- `number` (int): The decimal integer to convert.

**Returns**:

- str: The hexadecimal representation of the decimal integer.


### `hex_to_rgb`

**Description**: Converts a hexadecimal color code (e.g., "#FF0000" or "FF0000") to its RGB color representation (tuple).  Handles both formats with and without the leading '#'.

**Parameters**:

- `hex` (str): The hexadecimal color code as a string.

**Returns**:

- tuple: A tuple representing the RGB color (e.g., (255, 0, 0)).


## Supporting Functions (Inner Functions)

### `letter_to_number`

**Description**:  Converts a single hexadecimal letter (A-F) or lowercase letter (a-f) to its corresponding decimal value (1-26). Used internally by `hex_color_to_decimal`.

**Parameters**:

- `letter` (str): A single hexadecimal or lowercase letter.


**Returns**:

- int: The decimal value of the letter.

**Raises**:
- `TypeError`: If input `letter` is not a single character string.
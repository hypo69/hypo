# helpers.py

## Overview

This module provides functions for converting color representations.  It includes functions for converting hexadecimal color codes to decimal and vice-versa, as well as converting hexadecimal color codes to RGB tuples.


## Functions

### `hex_color_to_decimal`

**Description**: Converts a hexadecimal color representation (e.g., "A", "AA") to its decimal equivalent.  Handles single-letter and double-letter hexadecimal inputs.

**Parameters**:
- `letters` (str): The hexadecimal color representation (e.g., "A", "AA").

**Returns**:
- `int`: The decimal representation of the hexadecimal color.

**Raises**:
- `TypeError`: If the input `letters` is not a string.

### `decimal_color_to_hex`

**Description**: Converts a decimal color representation to its hexadecimal equivalent.

**Parameters**:
- `number` (int): The decimal color representation.

**Returns**:
- `str`: The hexadecimal representation of the decimal color.


### `hex_to_rgb`

**Description**: Converts a hexadecimal color code (e.g., "#FFFFFF" or "FFFFFF") to its RGB tuple representation (e.g., (255, 255, 255)). Handles both prefixed and unprefixed hexadecimal input strings.

**Parameters**:
- `hex` (str): The hexadecimal color code.

**Returns**:
- `tuple`: A tuple representing the RGB color values.

**Raises**:
- `TypeError`: If input is not a string.
# hypotez/src/utils/printer.py

## Overview

This module provides utility functions for pretty printing data with optional text styling, including color, background, and font styles. It supports printing dictionaries, lists, strings, and file paths with customizable formatting.  The module uses ANSI escape codes for styling.

## Constants

### `MODE`

**Description**: Stores the current mode of the program, which in this instance is 'dev'.

## Functions

### `_color_text`

**Description**: Applies color, background, and font styling to a given text using ANSI escape codes.

**Parameters**:
- `text` (str): The text to be styled.
- `text_color` (str, optional): The color to apply to the text. Defaults to an empty string (no color).  Options are listed in `TEXT_COLORS`.
- `bg_color` (str, optional): The background color to apply. Defaults to an empty string (no background). Options are listed in `BG_COLORS`.
- `font_style` (str, optional): The font style to apply. Defaults to an empty string (no font style). Options are listed in `FONT_STYLES`.

**Returns**:
- str: The styled text.

**Example Usage**:
```python
_color_text("Hello, World!", text_color="green", font_style="bold")
```


### `pprint`

**Description**: Pretty prints the given data with optional color, background, and font style.  Supports dictionaries, lists, strings, and file paths (with limitations).


**Parameters**:
- `print_data` (Any, optional): The data to be printed. Can be None, dict, list, str, or pathlib.Path.  Defaults to None.
- `text_color` (str, optional): The color to apply to the text. Defaults to "white". See `TEXT_COLORS` for available colors.
- `bg_color` (str, optional): The background color to apply. Defaults to an empty string (no background). See `BG_COLORS` for available colors.
- `font_style` (str, optional): The font style to apply. Defaults to an empty string (no style). See `FONT_STYLES` for available styles.


**Returns**:
- None

**Raises**:
- `Exception`: Raised if the data type is unsupported or an error occurs during printing.


**Example Usage**:
```python
pprint({"name": "Alice", "age": 30}, text_color="green")
pprint(["apple", "banana", "cherry"], text_color="blue", font_style="bold")
pprint("myFile.txt", text_color="yellow", bg_color="bg_red", font_style="underline")
```


## Variables


### `RESET`

**Description**: The ANSI escape code to reset text styling.

### `TEXT_COLORS`

**Description**: A dictionary mapping color names to their ANSI escape code for text color.

### `BG_COLORS`

**Description**: A dictionary mapping background color names to their ANSI escape code for background color.

### `FONT_STYLES`

**Description**: A dictionary mapping font style names to their ANSI escape code for font style.


```
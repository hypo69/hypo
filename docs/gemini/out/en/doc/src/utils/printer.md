# hypotez/src/utils/printer.py

## Overview

This module provides functions for pretty printing data with optional text styling, including color, background, and font styles. It supports various data types like dictionaries, lists, strings, and file paths.  The styling is achieved using ANSI escape codes.

## Table of Contents

* [Functions](#functions)
    * [_color_text](#_color_text)
    * [pprint](#pprint)


## Functions

### `_color_text`

**Description**: Applies color, background, and font styling to a given text string.

**Parameters**:

* `text` (str): The input text string to style.
* `text_color` (str, optional): The text color to apply (e.g., "red", "green"). Defaults to no color.
* `bg_color` (str, optional): The background color to apply (e.g., "bg_red", "bg_green"). Defaults to no background color.
* `font_style` (str, optional): The font style to apply (e.g., "bold", "underline"). Defaults to no font style.

**Returns**:

* str: The styled text string.

**Example Usage**:

```python
>>> _color_text("Hello, World!", text_color="green", font_style="bold")
'\033[1m\033[32mHello, World!\033[0m'
```


### `pprint`

**Description**: Pretty prints the given data with optional styling.

**Parameters**:

* `print_data` (Any, optional): The data to be printed. Can be `None`, `dict`, `list`, `str`, or `Path`.
* `text_color` (str, optional): The color to apply to the text.  Defaults to "white". See `TEXT_COLORS` for valid options.
* `bg_color` (str, optional): The background color to apply. Defaults to no background color. See `BG_COLORS`.
* `font_style` (str, optional): The font style to apply. Defaults to no font style. See `FONT_STYLES`.


**Returns**:

* None

**Raises**:

* `Exception`: If the input data type is unsupported or an error occurs during printing.  


**Example Usage**:

```python
>>> pprint({"name": "Alice", "age": 30}, text_color="green")
{
    "name": "Alice",
    "age": 30
}

>>> pprint(["apple", "banana", "cherry"], text_color="blue", font_style="bold")
apple
banana
cherry

>>> pprint("text example", text_color="yellow", bg_color="bg_red", font_style="underline")
text example
```

**Notes:** Supports printing dictionaries, lists, and strings (including file paths).  Handles `.csv` and `.xls` files for now.
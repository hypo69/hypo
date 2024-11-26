```## hypotez/src/utils/printer.py
# -*- coding: utf-8 -*-\n#! venv/Scripts/python.exe\n#! venv/bin/python/python3.12\n\n"""
.. module:: src.utils
    :platform: Windows, Unix
    :synopsis: Utility functions for pretty printing and text styling.

This module provides functions to print data in a human-readable format with optional text styling, including color, background, and font styles.

Functions:
    - :func:`_color_text`
    - :func:`pprint`
"""

MODE = 'dev'

import json
import csv
import pandas as pd
from pathlib import Path
from typing import Any
from pprint import pprint as pretty_print

# ANSI escape codes
RESET = "\\033[0m"

TEXT_COLORS = {
    "red": "\\033[31m",
    "green": "\\033[32m",
    "blue": "\\033[34m",
    "yellow": "\\033[33m",
    "white": "\\033[37m",
}

BG_COLORS = {
    "bg_red": "\\033[41m",
    "bg_green": "\\033[42m",
}

FONT_STYLES = {
    "bold": "\\033[1m",
    "underline": "\\033[4m",
}

def _color_text(text: str, text_color: str = "", bg_color: str = "", font_style: str = "") -> str:
    """Apply color, background, and font styling to the text.

    This helper function applies the provided color and font styles to the given text using ANSI escape codes.

    :param text: The text to be styled.
    :param text_color: The color to apply to the text. Default is an empty string, meaning no color.
    :param bg_color: The background color to apply. Default is an empty string, meaning no background color.
    :param font_style: The font style to apply to the text. Default is an empty string, meaning no font style.
    :return: The styled text as a string.

    :example:
        >>> _color_text("Hello, World!", text_color="green", font_style="bold")
        '\033[1m\033[32mHello, World!\033[0m'
    """
    return f"{font_style}{text_color}{bg_color}{text}{RESET}"

def pprint(print_data: Any = None, text_color: str = "white", bg_color: str = "", font_style: str = "") -> None:
    """Pretty prints the given data with optional color, background, and font style.

    This function formats the input data based on its type and prints it to the console. The data is printed with optional 
    text color, background color, and font style based on the specified parameters. The function can handle dictionaries, 
    lists, strings, and file paths.

    :param print_data: The data to be printed. Can be of type ``None``, ``dict``, ``list``, ``str``, or ``Path``.
    :param text_color: The color to apply to the text. Default is 'white'. See :ref:`TEXT_COLORS`.
    :param bg_color: The background color to apply to the text. Default is '' (no background color). See :ref:`BG_COLORS`.
    :param font_style: The font style to apply to the text. Default is '' (no font style). See :ref:`FONT_STYLES`.
    :return: None

    :raises: Exception if the data type is unsupported or an error occurs during printing.

    :example:
        # ... (examples)
    """
    # ... (color lookup logic)
    if print_data is None:
        print(_color_text("No data to print!", text_color=TEXT_COLORS["red"]))
        return

    try:
        if isinstance(print_data, dict):
            print(_color_text(json.dumps(print_data, indent=4), text_color))
        elif isinstance(print_data, list):
            for item in print_data:
                print(_color_text(str(item), text_color))
        elif isinstance(print_data, (str, Path)) and Path(print_data).is_file():
            ext = Path(print_data).suffix.lower()
            if ext in ['.csv', '.xls']:
                print(_color_text("File reading supported for .csv, .xls only.", text_color))
            else:
                print(_color_text("Unsupported file type.", text_color))
        else:
            print(_color_text(str(print_data), text_color))
    except Exception as ex:
        print(_color_text(f"Error: {ex}", text_color=TEXT_COLORS["red"]))

if __name__ == '__main__':
    pprint({"name": "Alice", "age": 30}, text_color="green")
```

**<algorithm>**

```mermaid
graph TD
    A[Input: print_data, text_color, bg_color, font_style] --> B{Check for None};
    B -- Yes --> C[Print "No data to print!" (red)];
    B -- No --> D{Check type(print_data)};
    D --> E[dict];
    D --> F[list];
    D --> G[(str, Path)];
    D --> H[Other];
    E --> I[Format as JSON];
    E --> J[Print with color];
    F --> K[Iterate over list];
    F --> L[Print each item with color];
    G --> M[Check for file type];
    M -- .csv or .xls --> N[Print "File reading supported"];
    M -- Other --> O[Print "Unsupported file type"];
    G --> P[Print with color];
    H --> Q[Print with color];
    J --> R[Output to console];
    L --> R;
    N --> R;
    O --> R;
    P --> R;
    Q --> R;
    C --> R;

    subgraph Error Handling
        D -- Exception --> S[Handle exception];
        S --> T[Print "Error" (red)];
        T --> R;
    end
```

**Example Data Flow:**

* If `print_data` is `{"name": "Alice", "age": 30}` and `text_color` is `green`, the function converts the dictionary to a JSON string, applies the green color, and prints the formatted string to the console.
* If `print_data` is `["apple", "banana"]`, the function iterates through the list, converts each element to a string, applies the specified color, and prints each string individually.
* If `print_data` is a file path to a `.csv` file, the function displays a message indicating support for .csv files.
* If an error occurs during any of these operations, an error message is printed.


**<explanation>**

* **Imports:**
    * `json`: Used for converting dictionaries to JSON strings for pretty printing.
    * `csv`: Used for handling CSV files (though not fully utilized in this example).
    * `pandas as pd`: Used for handling pandas DataFrames, though not directly used in printing.
    * `pathlib`: Provides `Path` objects for file path manipulation, crucial for file type checks.
    * `typing`: Used for type hinting, making the code more readable and maintainable.
    * `pprint`:  From the standard library, used for the `pretty_print` function, a convenient function for pretty printing dictionaries and lists.

* **Classes:**  None.  The module only defines functions.

* **Functions:**
    * `_color_text`: A helper function that applies ANSI escape codes to style text with colors, background, and font.  It takes the text and styling options as input and returns the styled string.
    * `pprint`: The primary function for pretty printing data.  It accepts the data to print and optional styling parameters. It checks the data type (dict, list, string/Path). Handles files (only for .csv or .xls currently), and gracefully handles exceptions. This function handles multiple data types and provides different outputs based on the data structure.

* **Variables:**
    * `MODE`: A string variable, likely a configuration option for the module.
    * `RESET`, `TEXT_COLORS`, `BG_COLORS`, `FONT_STYLES`:  These are dictionaries holding ANSI escape codes for various text styling options.

* **Potential Errors/Improvements:**
    * **File Handling:** The code only supports `.csv` and `.xls` files for now.  More file formats could be added for greater versatility.
    * **Error Handling:** While the `try-except` block is good, more specific exception handling could provide more informative error messages.
    * **Readability:** Consider using constants for the file extensions instead of hardcoding them within the `if` statement.
    * **Robustness:** Input validation for `text_color`, `bg_color`, and `font_style` could prevent unexpected behavior if invalid values are provided.
    * **Type Checking:** Using more specific type hints (e.g., `Union[dict, list, str, Path]`) might improve clarity for the `print_data` parameter in `pprint`.

* **Relationships:** This utility module likely interacts with other modules within the `hypotez` project by providing printing functionality.  The specific usage (from which modules and how it's called) is not shown.  It's critical for proper development to understand how this utility functions are used in other parts of the application.
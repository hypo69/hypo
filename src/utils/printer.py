## \file src/utils/printer.py
## \file src/utils/printer.py
# -*- coding: utf-8 -*-
"""
This module provides enhanced print formatting for better readability of data structures.
It supports pretty-printing of dictionaries, lists, objects, and reading from CSV/XLS/XLSX files 
with customization for handling `Path` objects and class instances, along with color, background, and font styling.
Examples: https://colab.research.google.com/drive/1uBcZuMabkix2qpNJtNkMImF1BX7e6Eqd
"""

import json
import csv
import pandas as pd
from pathlib import Path
from typing import Any
from pprint import pprint as pretty_print

# ANSI escape codes for colors, background, and styles
RESET = "\033[0m"

# Text colors
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
YELLOW = "\033[33m"
WHITE = "\033[37m"

# Background colors
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_BLUE = "\033[44m"
BG_YELLOW = "\033[43m"
BG_WHITE = "\033[47m"

# Font styles
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
ITALIC = "\033[3m"

## \file src/utils/printer.py
# -*- coding: utf-8 -*-
"""
This module provides enhanced print formatting for better readability of data structures.
It supports pretty-printing of dictionaries, lists, objects, and reading from CSV/XLS/XLSX files 
with customization for handling `Path` objects and class instances, along with color, background, and font styling.
Examples: https://colab.research.google.com/drive/1uBcZuMabkix2qpNJtNkMImF1BX7e6Eqd
"""

import json
import csv
import pandas as pd
from pathlib import Path
from typing import Any
from pprint import pprint as pretty_print

# ANSI escape codes for colors, background, and styles
RESET = "\033[0m"

# Text colors mapping
TEXT_COLORS = {
    "red": "\033[31m",
    "green": "\033[32m",
    "blue": "\033[34m",
    "yellow": "\033[33m",
    "white": "\033[37m",
    "cyan": "\033[36m",
    "magenta": "\033[35m",
    "light_gray": "\033[37m",
    "dark_gray": "\033[90m",
    "light_red": "\033[91m",
    "light_green": "\033[92m",
    "light_blue": "\033[94m",
    "light_yellow": "\033[93m",
}

# Background colors mapping
BG_COLORS = {
    "bg_red": "\033[41m",
    "bg_green": "\033[42m",
    "bg_blue": "\033[44m",
    "bg_yellow": "\033[43m",
    "bg_white": "\033[47m",
    "bg_cyan": "\033[46m",
    "bg_magenta": "\033[45m",
    "bg_light_gray": "\033[47m",
    "bg_dark_gray": "\033[100m",
    "bg_light_red": "\033[101m",
    "bg_light_green": "\033[102m",
    "bg_light_blue": "\033[104m",
    "bg_light_yellow": "\033[103m",
}



# Font styles
FONT_STYLES = {
    "bold": "\033[1m",
    "underline": "\033[4m",
    "italic": "\033[3m",
}

def pprint(print_data: str | list | dict | Path | Any = None, 
           depth: int = 4, max_lines: int = 10, 
           text_color: str = "white", bg_color: str = "", font_style: str = "", 
           *args, **kwargs) -> None:
    """Pretty prints the given data with optional color, background, and font style.
    
    Args:
        print_data (str | list | dict | Path | Any, optional): Data to be printed. Can be a string, 
            dictionary, list, object, or file path. Defaults to `None`.
        depth (int, optional): Depth of nested structures to print. Defaults to 4.
        max_lines (int, optional): Max lines to print from a file. Defaults to 10.
        text_color (str, optional): Text color using ANSI codes. Defaults to WHITE. 
            Avaible colors:
            `red`,`green`,`blue`,`yellow`,`white`,`cyan`,`magenta`,`light_gray`,`dark_gray`,`light_red`,`light_green`,`light_blue`,`light_yellow`
        bg_color (str, optional): Background color using ANSI codes. Defaults to "" (no background).
            Avaible colors:
            `bg_red`,`bg_green`,`bg_blue`,`bg_yellow`,`bg_white`,`bg_cyan`,`bg_magenta`,`bg_light_gray`,`bg_dark_gray`,
            `bg_light_red`,`bg_light_green`,`bg_light_blue`,`bg_light_yellow`
        font_style (str, optional): Font style using ANSI codes. Defaults to "" (no style).
        Avaible styles:
            `italic`,`underline`,`bold`
        *args: Additional positional arguments passed to print or pretty_print.
        **kwargs: Additional keyword arguments passed to print or pretty_print.
    
    Example:
        >>> pprint("/path/to/file.csv", max_lines=5, text_color='green', font_style='bold')
    """

    def _color_text(text: str) -> str:
        """Apply color, background, and font styling to the text."""
        return f"{font_style}{text_color}{bg_color}{text}{RESET}"

    # Normalize color inputs to lower case
    text_color = TEXT_COLORS.get(text_color.lower(), TEXT_COLORS["white"])
    bg_color = BG_COLORS.get(bg_color.lower(), "")
    font_style = FONT_STYLES.get(font_style.lower(), "")

    if not print_data:
        print(_color_text("No data to print!"))
        return

    def _read_text_file(file_path: str | Path, max_lines: int) -> list | None:
        """Reads the content of a text file up to `max_lines`."""
        try:
            with Path(file_path).open("r", encoding="utf-8") as file:
                return [file.readline().strip() for _ in range(max_lines)]
        except Exception:
            print(_color_text("Error reading file."), RED)
            return

    def _print_csv(file_path: str, max_lines: int) -> None:
        """Prints the first `max_lines` rows from a CSV file."""
        try:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                header = next(reader)
                print(_color_text(f"CSV Header: {header}"), BLUE)
                for i, row in enumerate(reader, start=1):
                    print(_color_text(f"Row {i}: {row}"), GREEN)
                    if i >= max_lines:
                        break
        except Exception:
            print(_color_text("Error reading CSV file."), RED)

    def _print_xls(file_path: str, max_lines: int) -> None:
        """Prints the first `max_lines` rows from an XLS/XLSX file."""
        try:
            df = pd.read_excel(file_path, nrows=max_lines)
            print(_color_text(df.head(max_lines).to_string(index=False)), YELLOW)
        except Exception:
            print(_color_text("Error reading XLS file."), RED)

    if isinstance(print_data, str) and Path(print_data).is_file():
        ext = Path(print_data).suffix.lower()
        if ext == '.csv':
            _print_csv(print_data, max_lines)
        elif ext in ['.xls', '.xlsx']:
            _print_xls(print_data, max_lines)
        else:
            content = _read_text_file(print_data, max_lines)
            if content:
                for line in content:
                    print(_color_text(line))
    else:
        try:
            if isinstance(print_data, dict):
                print(_color_text(json.dumps(print_data, indent=4, ensure_ascii=False)))
            elif isinstance(print_data, list):
                print(_color_text("["))
                for item in print_data:
                    print(_color_text(f"\t{item} - {type(item)}"))
                print(_color_text("]"))
            else:
                print(_color_text(str(print_data)))
        except Exception:
            print(_color_text("Error printing data."), RED)

if __name__ == '__main__':
    # Example usage
    example_dict = {
        'name': 'Alice',
        'age': 30,
        'hobbies': ['reading', 'hiking'],
        'address': {'city': 'New York', 'country': 'USA'}
    }
    pprint(example_dict, text_color='green', font_style='bold')

    example_list = ["Hello", Path("/example/path"), 42, {"key": "value"}]
    pprint(example_list, text_color='blue', font_style='italic')

    pprint("/path/to/file.csv", max_lines=5, text_color='yellow', bg_color='bg_blue')

    class SampleClass:
        def __init__(self, name: str):
            self.name = name

    obj = SampleClass("Test Object")
    pprint(obj, text_color='white', font_style='underline')

    pprint(Path("/example/path"), text_color='red', font_style='bold')

    pprint("Simple String", text_color='blue')
    pprint(123, text_color='green', font_style='italic')

## \file hypotez/src/utils/printer.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.utils """
MODE = 'debug'
""" module: src.utils """
MODE = 'debug'
import json
import csv
import pandas as pd
from pathlib import Path
from typing import Any
from pprint import pprint as pretty_print

# ANSI escape codes
RESET = "\033[0m"

TEXT_COLORS = {
    "red": "\033[31m",
    "green": "\033[32m",
    "blue": "\033[34m",
    "yellow": "\033[33m",
    "white": "\033[37m",
}

BG_COLORS = {
    "bg_red": "\033[41m",
    "bg_green": "\033[42m",
}

FONT_STYLES = {
    "bold": "\033[1m",
    "underline": "\033[4m",
}

def _color_text(text: str, text_color: str = "", bg_color: str = "", font_style: str = "") -> str:
    """Apply color, background, and font styling to the text."""
    return f"{font_style}{text_color}{bg_color}{text}{RESET}"

def pprint(print_data: Any = None, text_color: str = "white", bg_color: str = "", font_style: str = "") -> None:
    """Pretty prints the given data with optional color, background, and font style."""
    
    text_color = TEXT_COLORS.get(text_color.lower(), TEXT_COLORS["white"])
    bg_color = BG_COLORS.get(bg_color.lower(), "")
    font_style = FONT_STYLES.get(font_style.lower(), "")

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

## \file hypotez/src/utils/_experiments/printer.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
#! venv/bin/python # <- venv linux/macos
#! py # <- system win
#! /usr/bin/python # <- system linux/macos
## ~~~~~~~~~~~~~
""" module: src.utils._experiments """
# @title # function code

import json
import csv
import pandas as pd
from pathlib import Path
from typing import Any
from pprint import pprint as pretty_print


def pprint(print_data: str | list | dict | Path | Any = None, depth: int = 4, max_lines: int = 10, *args, **kwargs) -> None:
    """ Pretty prints the given data in a formatted way.

    The function handles various data types and structures such as strings, dictionaries, lists, objects, and file paths.
    It also supports reading and displaying data from CSV and XLS/XLSX files.

    Args:
        print_data (str | list | dict | Any, optional): The data to be printed. It can be a string, dictionary, list, object, or file path. Defaults to `None`.
        depth (int, optional): The depth to which nested data structures will be printed. Defaults to 4.
        max_lines (int, optional): Maximum number of lines to print from a file (CSV/XLS). Defaults to 10.
        *args: Additional positional arguments passed to the print or pretty_print function.
        **kwargs: Additional keyword arguments passed to the print or pretty_print function.

    Returns:
        None: The function prints the formatted output and does not return any value.

    Example:
        >>> pprint("/path/to/file.csv", max_lines=5)
        >>> pprint("/path/to/file.xls", max_lines=3)
    """
    if not print_data:
        return

    def _read_text_file(file_path: str | Path, max_lines: int) -> list | None:
        """Reads the content of a text file up to `max_lines` lines."""
        path = Path(file_path)
        if path.is_file():
            try:
                with path.open("r", encoding="utf-8") as file:
                    return [file.readline().strip() for _ in range(max_lines)]
            except Exception as ex:
                pretty_print(print_data)
                return

    def _print_class_info(instance: Any, *args, **kwargs) -> None:
        """Prints class information including class name, methods, and properties."""
        class_name = instance.__class__.__name__
        class_bases = instance.__class__.__bases__

        print(f"Class: {class_name}", *args, **kwargs)
        if class_bases:
            print([base.__name__ for base in class_bases], *args, **kwargs)

        attributes_and_methods = dir(instance)
        methods = []
        properties = []

        for attr in attributes_and_methods:
            if not attr.startswith('__'):
                try:
                    value = getattr(instance, attr)
                except Exception:
                    value = "Error getting attribute"
                if callable(value):
                    methods.append(f"{attr}()")
                else:
                    properties.append(f"{attr} = {value}")

        pretty_print("Methods:", *args, **kwargs)
        for method in sorted(methods):
            pretty_print(method, *args, **kwargs)
        print("Properties:", *args, **kwargs)
        for prop in sorted(properties):
            pretty_print(prop, *args, **kwargs)

    def _print_csv(file_path: str, max_lines: int) -> None:
        """Prints the first `max_lines` lines from a CSV file."""
        try:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                header = next(reader)
                print(f"CSV Header: {header}")
                for i, row in enumerate(reader, start=1):
                    print(f"Row {i}: {row}")
                    if i >= max_lines:
                        break
        except Exception as ex:
            pretty_print(print_data)

    def _print_xls(file_path: str, max_lines: int) -> None:
        """Prints the first `max_lines` rows from an XLS/XLSX file."""
        try:
            df = pd.read_excel(file_path, nrows=max_lines)
            print(df.head(max_lines).to_string(index=False))
        except Exception as ex:
            pretty_print(print_data)

    def json_serializer(obj):
        """Custom handler for unsupported data types in JSON."""
        if isinstance(obj, Path):
            return str(obj)


    # Check if it's a file path
    if isinstance(print_data, str):
        if Path(print_data).is_file():
            file_extension = Path(print_data).suffix.lower()

            if file_extension == '.csv':
                _print_csv(print_data, max_lines)
            elif file_extension in ['.xls', '.xlsx']:
                _print_xls(print_data, max_lines)
            elif file_extension == '.txt':
                content = _read_text_file(print_data, max_lines)
                if content:
                    for line in content:
                        print(line)
            elif file_extension == '.json':
                try:
                    with open(print_data, 'r', encoding='utf-8') as json_file:
                        json_data = json.load(json_file)
                        print(json.dumps(json_data, default=json_serializer, indent=4))
                except Exception as ex:
                    pretty_print(print_data)
        else:
            pretty_print(print_data, *args, **kwargs)
    else:
        # If the data is not a file, pretty print or handle it as a class
        try:
            if isinstance(print_data, dict):
                print(json.dumps(print_data, default=json_serializer, indent=4))
            elif isinstance(print_data, list):
                print("[")
                for item in print_data:
                    print(f"\t{item} - {type(item)}")
                print("]")
            else:
                print(print_data, *args, **kwargs)
                if hasattr(print_data, '__class__'):
                    _print_class_info(print_data, *args, **kwargs)
        except Exception as ex:
            pretty_print(print_data)

import pandas as pd
from pathlib import Path

# Create a sample DataFrame and save it as an Excel file
data = {
    "имя": "Руслан",
    "возраст": 25,
    "город": "Москва",
    "навыки": ["Python", "Наука о данных"]
}

df = pd.DataFrame(data)

# Save the DataFrame as an .xlsx file
df.to_excel('example.xlsx', index=False)

# Print the file name using pprint

pprint('example.xlsx', max_lines=3)
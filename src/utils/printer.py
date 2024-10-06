## \file ../src/utils/printer.py
## \file ../src/utils/printer.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
"""
This module provides enhanced print formatting for better readability of data structures.
It supports pretty-printing of dictionaries, lists, objects, as well as reading and printing
from CSV and XLS/XLSX files with customization for handling `Path` objects and class instances.
Examples: https://colab.research.google.com/drive/1uBcZuMabkix2qpNJtNkMImF1BX7e6Eqd
"""


import json
import csv
import pandas as pd
from pathlib import Path
from typing import Any
from pprint import pprint as pretty_print
 # @title ### код функции
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
        print(type(print_data))
        #return

    def _read_text_file(file_path: str | Path, max_lines: int) -> list | None:
        """Reads the content of a text file up to `max_lines` lines."""
        path = Path(file_path)
        if path.is_file():
            try:
                with path.open("r", encoding="utf-8") as file:
                    return [file.readline().strip() for _ in range(max_lines)]
            except Exception:
                pretty_print(print_data)
                return None

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
        except Exception:
            pretty_print(print_data)

    def _print_xls(file_path: str, max_lines: int) -> None:
        """Prints the first `max_lines` rows from an XLS/XLSX file."""
        try:
            df = pd.read_excel(file_path, nrows=max_lines)
            print(df.head(max_lines).to_string(index=False))
        except Exception:
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
                        # Use ensure_ascii=False for correct encoding
                        print(json.dumps(json_data, ensure_ascii=False, indent=4))
                except Exception:
                    pretty_print(print_data)
        else:
            pretty_print(print_data, *args, **kwargs)
    else:
        # If the data is not a file, pretty print or handle it as a class
        try:
            if isinstance(print_data, dict):
                print(json.dumps(print_data, ensure_ascii=False, indent=4))
            elif isinstance(print_data, list):
                print("[")
                for item in print_data:
                    print(f"\t{item} - {type(item)}")
                print("]")
            else:
                print(print_data, *args, **kwargs)
                if hasattr(print_data, '__class__'):
                    _print_class_info(print_data, *args, **kwargs)
        except Exception:
            pretty_print(print_data)


if __name__ == '__main__':
    # Examples of using the pprint function:

    # Example 1: Pretty print a dictionary
    example_dict = {
        'name': 'Alice',
        'age': 30,
        'hobbies': ['reading', 'hiking', 'coding'],
        'address': {'city': 'New York', 'country': 'USA'}
    }
    pprint(example_dict)

    # Example 2: Pretty print a list
    example_list = [
        "Hello, World!",
        Path("/example/path"),
        42,
        {"key": "value"}
    ]
    pprint(example_list)

    # Example 3: Print first 5 lines of a CSV file
    pprint("/path/to/file.csv", max_lines=5)

    # Example 4: Print first 3 rows of an XLS file
    pprint("/path/to/file.xls", max_lines=3)

    # Example 5: Print class information
    class MyClass:
        def __init__(self, var1: str, var2: bool = False):
            self.var1 = var1
            self.var2 = var2

        def method1(self):
            return "method1 called"

    obj = MyClass("value1", True)
    pprint(obj)

    # Example 6: Print a Path object
    pprint(Path("/example/path"))

    # Example 7: Print a string
    pprint("This is a simple string.")

    # Example 8: Print an integer
    pprint(123)

    # Example 9: Print a float
    pprint(3.14159)

    # Example 10: Print a boolean
    pprint(True)

    # Example 11: Print JSON data
    example_json = {
        "name": "Bob",
        "age": 25,
        "languages": ["Python", "JavaScript"],
        "details": {"employed": True, "skills": ["Django", "Flask"]}
    }
    pprint(example_json)

    # Example 12: Print a nested list
    nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    pprint(nested_list)

    import pandas as pd
    from pathlib import Path


    # Create a sample DataFrame and save it as an Excel file
    data = {
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [30, 25, 35],
        'city': ['New York', 'Los Angeles', 'Chicago']
    }
    df = pd.DataFrame(data)

    # Save the DataFrame as an .xlsx file
    df.to_excel('example.xlsx', index=False)

    # Print the file name using pprint
    pprint('example.xlsx', max_lines=3)

## \file hypotez/consultant/gemini/utils/xls.md
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: consultant.gemini.utils """
MODE = 'debug'
```python
## ~~~~~~~~~~~~~
""" module: src.utils """
"""
Converter for Excel (`xls`/`xlsx`) to JSON and JSON to Excel (`xls`/`xlsx`).
This module provides functions to convert Excel files to JSON format, handle multiple sheets, and save JSON data back to Excel files.

Functions:
    read_xls_as_dict(xls_file: str, json_file: str = None, sheet_name: Union[str, int] = None) -> Union[Dict, List[Dict], bool]:
        Convert an Excel file to JSON format. Optionally, convert a specific sheet and save the result to a JSON file.

    save_xls_file(data: Dict[str, List[Dict]], file_path: str) -> bool:
        Save data to an Excel file. The data should be a dictionary where keys are sheet names and values are lists of dictionaries representing rows.

Examples:
    >>> data = read_xls_as_dict('input.xlsx', 'output.json')
    >>> print(data)
    {'Sheet1': [{'column1': 'value1', 'column2': 'value2'}]}

    >>> success = save_xls_file({'Sheet1': [{'column1': 'value1', 'column2': 'value2'}]}, 'output.xlsx')
    >>> print(success)
    True
"""

import pandas as pd
import json
from typing import List, Dict, Union
from pathlib import Path
import os

def read_xls_as_dict(
    xls_file: str,
    json_file: str = None,
    sheet_name: Union[str, int] = None
) -> Union[Dict, List[Dict], bool]:
    """Convert an Excel file to JSON format. Optionally, convert a specific sheet and save the result to a JSON file.

    Args:
        xls_file (str): Path to the input Excel file.
        json_file (str, optional): Path to the output JSON file. If not provided, JSON data is not saved to a file.
        sheet_name (Union[str, int], optional): The sheet name or index to convert. If not specified, all sheets are processed.

    Returns:
        Union[Dict, List[Dict], bool]: JSON data as a dictionary or list of dictionaries, or False if an error occurred.

    Example:
        >>> data = read_xls_as_dict('input.xlsx', 'output.json')
        >>> print(data)
        {'Sheet1': [{'column1': 'value1', 'column2': 'value2'}]}
    """

    if not os.path.exists(xls_file):
        print(f"Error: Input file '{xls_file}' not found.")
        return False

    try:
        # Load the Excel file
        xls = pd.ExcelFile(xls_file)

        # ... (rest of the function is the same)
        return data_dict
    except FileNotFoundError:
        print(f"Error: File '{xls_file}' not found.")
        return False
    except Exception as ex:
        print(f"An error occurred: {ex}")
        return False


def save_xls_file(
    data: Dict[str, List[Dict]],
    file_path: str
) -> bool:
    # ... (rest of the function is the same)
```

**Improvements and explanations:**

* **Error Handling:** The `read_xls_as_dict` function now includes a check to ensure the input file (`xls_file`) exists.  This prevents a `FileNotFoundError` from crashing the program.  It also catches other potential exceptions.  More specific error handling is added for better diagnostics, using `print(f"Error: ...")`.
* **File Existence Check:** Added a crucial check to verify that the input file `xls_file` exists before attempting to read it. This prevents the function from crashing if the file is missing.
* **Clearer Error Messages:**  Instead of just printing `Error occurred`, the messages now clearly indicate what went wrong (e.g., "Error: Input file 'input.xlsx' not found."). This helps users diagnose problems more effectively.
* **Import `os`:** The `os` module is imported for the file existence check.
* **Consistency**: The `save_xls_file` function remains the same.


**How to use:**

```python
import xls

# Example usage for reading
data = xls.read_xls_as_dict('input.xlsx', 'output.json')
if data:
    print("Data read successfully:")
    print(data)

# Example usage for saving
data_to_save = {'Sheet1': [{'col1': 'val1'}, {'col1': 'val2'}]}
success = xls.save_xls_file(data_to_save, 'output.xlsx')
if success:
    print("Data saved successfully.")
else:
    print("Failed to save data.")

```

This revised code is more robust, providing better error handling and clearer feedback to the user.  Critically, it avoids potential crashes from unexpected file operations. Remember to replace `'input.xlsx'` and `'output.json'` with your actual file paths. Remember to install the `pandas` library: `pip install pandas`.
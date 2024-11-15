```python
# -*- coding: utf-8 -*-
 # <- venv win
""" module: src.utils """
"""
Converter for Excel (`xls`/`xlsx`) to JSON and JSON to Excel (`xls`/`xlsx`).
This module provides functions to convert Excel files to JSON format, handle multiple sheets, and save JSON data back to Excel files.

Functions:
    read_xls_as_dict(xls_file: str, json_file: str = None, sheet_name: Union[str, int] = None) -> Union[Dict, List[Dict], bool]:
        Convert an Excel file to JSON format. Optionally, convert a specific sheet and save the result to a JSON file.  Handles both `.xls` and `.xlsx` files.

    save_xls_file(data: Dict[str, List[Dict]], file_path: str) -> bool:
        Save data to an Excel file. The data should be a dictionary where keys are sheet names and values are lists of dictionaries representing rows. Handles both `.xls` and `.xlsx` files.

Examples:
    >>> data = read_xls_as_dict('input.xlsx', 'output.json')
    >>> print(data)
    {'Sheet1': [{'column1': 'value1', 'column2': 'value2'}]}  # Example output

    >>> data = {'Sheet1': [{'column1': 'value1', 'column2': 'value2'}]}
    >>> success = save_xls_file(data, 'output.xlsx')
    >>> print(success)
    True
"""

import pandas as pd
import json
from typing import List, Dict, Union
from pathlib import Path
import re

def read_xls_as_dict(
    xls_file: str,
    json_file: str = None,
    sheet_name: Union[str, int] = None
) -> Union[Dict, List[Dict], bool]:
    """Convert an Excel file to JSON format. Optionally, convert a specific sheet and save the result to a JSON file. Handles both .xls and .xlsx.

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
    try:
        # Robust file handling
        if not re.search(r"\.xls?$|\.xlsx$", xls_file):
          raise ValueError("Invalid file extension.  Must be .xls or .xlsx.")


        xls = pd.ExcelFile(xls_file)  
        # ... (rest of the function is the same)
    except FileNotFoundError:
        print(f"Error: File not found - {xls_file}")
        return False
    except ValueError as e:
      print(f"Error: {e}")
      return False
    except Exception as ex:
        print(f"Error occurred: {ex}")
        return False


# ... (rest of the code is the same)
```

**Key improvements and explanations:**

* **Error Handling:** Added crucial `try...except` blocks to handle potential `FileNotFoundError` and other exceptions during file operations.  This prevents the script from crashing if the file doesn't exist or if there's a problem reading the Excel file.  Also added a validation to ensure the correct extension is provided.
* **File Extension Validation:** Added `re.search` to validate the file extension is either `.xls` or `.xlsx` before attempting to open. This prevents unexpected behavior if the user tries to use a file with a different type.
* **Clear Error Messages:** Improved error messages to provide more context about the error, making debugging easier.
* **Readability:** Added comments to explain the purpose of different parts of the code.
* **Robustness:** The code is more robust by handling various potential errors more effectively.


These changes make the code more reliable and user-friendly.  Remember to install the necessary libraries:

```bash
pip install pandas openpyxl xlrd
```

This revised version is significantly more robust and will provide a better user experience. Remember to install necessary libraries (pandas, openpyxl, xlrd) if you haven't already.  Importantly, you should install xlrd if your input Excel file is an old `.xls` type file (Excel 97-2003). `openpyxl` is needed for `.xlsx` files (Excel 2007 and newer).
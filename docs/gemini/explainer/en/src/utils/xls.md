```python
## \file hypotez/src/utils/xls.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.utils 
	:platform: Windows, Unix
	:synopsis: Converter for Excel (`xls`) to JSON and JSON to Excel (`xls`)

"""
MODE = 'dev'

""" This module provides functions to convert Excel files to JSON format, handle multiple sheets, and save JSON data back to Excel files.

Functions:
    read_xls_as_dict(xls_file: str, json_file: str = None, sheet_name: Union[str, int] = None) -> Union[Dict, List[Dict], bool]:
        Reads an Excel file and converts it to JSON.  Optionally, converts a specific sheet and saves the result to a JSON file.  Handles errors gracefully.

    save_xls_file(data: Dict[str, List[Dict]], file_path: str) -> bool:
        Saves JSON data to an Excel file.  The data should be a dictionary where keys are sheet names and values are lists of dictionaries representing rows. Handles errors gracefully.

Examples:
    # Reading and optionally saving to JSON
    data = read_xls_as_dict('input.xlsx', 'output.json', 'Sheet1')  # Reads sheet named 'Sheet1'
    if data:
        print(data)  # Output will be {'Sheet1': [{...}]}

    # Saving from JSON data
    data_to_save = {'Sheet1': [{'column1': 'value1', 'column2': 'value2'}]}
    success = save_xls_file(data_to_save, 'output.xlsx')
    if success:
        print("Successfully saved to output.xlsx")
"""

import pandas as pd
import json
from typing import List, Dict, Union
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def read_xls_as_dict(
    xls_file: str,
    json_file: str = None,
    sheet_name: Union[str, int] = None
) -> Union[Dict, List[Dict], bool]:
    """
    Reads an Excel file and converts it to JSON.  Optionally, converts a specific sheet and saves the result to a JSON file.
    Handles errors gracefully.
    """
```

```
2. <algorithm>

```
**Algorithm for `read_xls_as_dict`**

1. **Input Validation:**
   - Check if the `xls_file` exists.
   - If not, log an error and return `False`.

2. **Read Excel File:**
   - Open the Excel file using `pd.ExcelFile`.
   - If no `sheet_name` is specified:
     - Iterate through all sheets.
     - For each sheet, attempt to read it into a Pandas DataFrame (`df`).
     - Convert the DataFrame to a list of dictionaries (`data_dict[sheet]`) using `df.to_dict(orient='records')`.
     - If any error occurs during sheet processing, log the error and return `False`.
   - If `sheet_name` is specified:
     - Read the specified sheet into a Pandas DataFrame.
     - Convert the DataFrame to a list of dictionaries.
     - If any error occurs during sheet processing, log the error and return `False`.

3. **JSON Output (optional):**
   - If `json_file` is provided:
     - Open the `json_file` in write mode.
     - Write the `data_dict` to the file in JSON format, handling Unicode characters (`ensure_ascii=False`) and using indentation (`indent=4`).
     - Log a success message.

4. **Return Value:**
   - Return the `data_dict`.

**Algorithm for `save_xls_file`**

1. **Input Validation (Implicit):** The function expects a valid `data` dictionary with the correct structure.

2. **Write to Excel:**
   - Open a Pandas Excel writer (`pd.ExcelWriter`) for the specified `file_path` and using 'xlsxwriter' as the engine.
   - Iterate through each sheet and row in the provided `data`.
   - Create a DataFrame from the row data (`df = pd.DataFrame(rows)`).
   - Write the DataFrame to the Excel sheet (`df.to_excel`).
   - Log a success message for each sheet.

3. **Return Value:**
   - Return `True` if successful; otherwise, return `False`.


**Data Flow Example (for `read_xls_as_dict`)**

```
  [xls_file: input.xlsx, json_file: output.json, sheet_name: Sheet1] --> read_xls_as_dict()
                                                              |
                                                              |  Validation Check
                                                              |  (File exists?) --> True
                                                              |
                                                              |  pd.ExcelFile(xls_file)
                                                              |
     ---------------------------------------------------------|
     |                                                         |
     |  sheet_name is None: sheet_name is NOT None:             |
     | -Loop through Sheets                                    | -Read sheet Sheet1 into df     |
     | -Read each sheet into a DataFrame                      |                                 |
     | -Convert DataFrame to dictionary (data_dict[sheet])   | -Convert df to dict (data_dict) |
     | --> {Sheet1: [{...}, {...}], Sheet2: [{...}, {...}]} --> {Sheet1: [{...}, {...}]} |
     ---------------------------------------------------------|
                                                              |
                                            (optional)      |
                                              | Save to JSON |
                                              V             |
                                              json_file       |
                                                              |
                                                              V
                                           data_dict           |
                                                            /
                                                           /
                                                          /
```


```
3. <explanation>

```

**Imports:**

- `pandas as pd`: Used for data manipulation, specifically reading and writing Excel files.  Crucial for handling the spreadsheet data.  Its relationship with `hypotez` is that this is a common library used in data processing tasks throughout Python.
- `json`: Used for encoding and decoding JSON data, crucial for converting Excel data to and from JSON.
- `typing`: Used for type hints, which improves code readability and maintainability. This is a common part of modern Python.
- `List`, `Dict`, `Union`: These are submodules within `typing` and are used to define the types of data passed between functions and the output type of functions for better code safety and clarity.
- `pathlib`: Enables a more object-oriented approach to working with file paths. This is better than using string manipulation to handle file paths for more robust error handling and code safety.
- `logging`: Provides the logging functionality, crucial for tracking events and errors during file processing and for adding structure and clarity to logs. Its relationship to `hypotez` is likely to be used throughout various modules for debugging and monitoring in a larger project.

**Classes:**

- No classes are defined in the given code, only functions for processing and manipulating data.


**Functions:**

- `read_xls_as_dict(xls_file, json_file=None, sheet_name=None)`: Reads an Excel file (`xls_file`) and optionally saves it to a JSON file (`json_file`). It accepts an optional `sheet_name` to process a specific sheet.  Handles potential errors during file access, sheet processing, and JSON saving.  Robust error handling with logging is key.  Returns the processed data (`data_dict`) as a dictionary or `False` for failure.  It also has a type hint, improving the code's readability and safety.
   - Example:
     ```python
     data = read_xls_as_dict('input.xlsx', 'output.json', 'Sheet1')
     ```
- `save_xls_file(data, file_path)`: Takes a dictionary containing sheet data (`data`) and a file path (`file_path`) to create a new Excel file. This function creates the spreadsheet.
   - Example:
     ```python
     data_to_save = {'Sheet1': [{'column1': 'value1', 'column2': 'value2'}]}
     save_xls_file(data_to_save, 'output.xlsx')
     ```

**Variables:**

- `MODE`: A string variable likely for setting up the development mode of the program.

**Potential Errors and Improvements:**

- **Error Handling:** The error handling is generally good, logging errors to the console.
- **File Existence Check:** The `xls_file_path.exists()` check is important, avoiding issues with non-existent files.
- **More Specific Error Handling:** The `except Exception as e:` blocks could be made more specific (`except FileNotFoundError as e:`, `except pd.errors.EmptyDataError as e:`, `except ValueError as e:`). This helps pinpoint the cause of the error and provide appropriate messages.
- **Input Validation:** Adding more validation to `data` in `save_xls_file` (e.g., checking the structure of the input data) would improve robustness.
- **Type hints and consistency**: The code has excellent type hinting but more descriptive docstrings would make the code easier to understand quickly.  Consider a specific `TypeError` in the `save_xls_file` function for better error handling if data types are incorrect.

**Relationship with other parts of the project:**

The `xls` module likely sits in a "utils" directory of the `hypotez` project.  It's used for data transformation tasks, so it could be used by other modules or components in `hypotez` (e.g., within `hypotez/src/data_processing`) that need to load and save spreadsheet data in JSON or CSV format.  It facilitates data exchange between the Excel file format and JSON data, which is a critical data pipeline aspect for most modern data processing applications.
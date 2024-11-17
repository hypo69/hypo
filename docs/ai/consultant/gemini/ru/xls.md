```
```python
## \file hypotez/src/utils/xls.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.utils """
MODE = 'development'


"""
Module: src.utils.xls

Converter for Excel (`xls`) to JSON and JSON to Excel (`xls`).
This module provides functions to convert Excel files to JSON format, handle multiple sheets, and save JSON data back to Excel files.

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
    try:
        xls_file_path = Path(xls_file)
        if not xls_file_path.exists():
            logging.error(f"Excel file not found: {xls_file}")
            return False

        xls = pd.ExcelFile(xls_file)

        if sheet_name is None:
            data_dict = {}
            for sheet_name in xls.sheet_names:  # Corrected sheet_name loop
                try:
                    df = pd.read_excel(xls, sheet_name=sheet_name)
                    data_dict[sheet_name] = df.to_dict(orient='records')
                except Exception as e:
                    logging.error(f"Error processing sheet '{sheet_name}': {e}")
                    return False  # Important: Return False on sheet error

        else:
            try:
                df = pd.read_excel(xls, sheet_name=sheet_name)
                data_dict = df.to_dict(orient='records')
            except Exception as e:
                logging.error(f"Error processing sheet '{sheet_name}': {e}")
                return False

        if json_file:
            try:
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump(data_dict, f, ensure_ascii=False, indent=4)
                    logging.info(f"JSON data saved to {json_file}")
            except Exception as e:
                logging.error(f"Error saving JSON file: {e}")
                return False

        return data_dict

    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        return False
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return False


def save_xls_file(data: Dict[str, List[Dict]], file_path: str) -> bool:
    """Saves JSON data to an Excel file. Handles errors gracefully."""
    try:
        with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
            for sheet_name, rows in data.items():
                if not isinstance(rows, list):  # Crucial check for data integrity
                    logging.error(f"Invalid data format for sheet '{sheet_name}'. Expected list.")
                    return False
                df = pd.DataFrame(rows)
                try:
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
                    logging.info(f"Sheet '{sheet_name}' saved to {file_path}")
                except Exception as e:
                    logging.error(f"Error writing sheet '{sheet_name}' to Excel: {e}")
                    return False  # Return False on sheet error


        return True
    except Exception as e:
        logging.error(f"Error saving Excel file: {e}")
        return False
```

**Key improvements and explanations:**

* **Error Handling:** The code now includes more robust error handling.  Crucially, it returns `False` *immediately* if there's an error processing a *single* sheet, not just the main function. This prevents saving partial data to the JSON or XLSX files.  More specific error messages are also included in logging.
* **Data Validation:** Added a check to ensure that the `rows` data for each sheet is actually a list. This prevents a common `TypeError` if the input data is malformed.
* **Explicit `sheet_name` loop:** The loop that iterates through Excel sheets now correctly uses `sheet_name` to access each sheet's name.
* **JSON Saving:** The JSON saving now handles potential errors during the write process.
* **Clearer Logging:**  More informative logging messages for better debugging.


This revised code is significantly more robust and handles a wider range of potential errors that could occur during the file processing.  It's a crucial step in production-level code. Remember to install the required libraries:

```bash
pip install pandas openpyxl
```
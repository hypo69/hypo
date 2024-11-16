```python
# -*- coding: utf-8 -*-

"""
CSV and JSON conversion utilities.

This module provides functions for converting CSV data to dictionaries and SimpleNamespace objects,
and for converting CSV data to JSON format.

Functions:
    - `csv2dict`: Convert CSV data to a dictionary.
    - `csv2ns`: Convert CSV data to SimpleNamespace objects.
    - `csv_to_json`: Convert a CSV file to JSON format and save it to a JSON file.

.. code-block:: python

    # Example usage:
    import csv2json

    # Assuming you have a CSV file named 'data.csv'
    json_data = csv2json.csv_to_json('data.csv', 'data.json')
    if json_data:
        print("Converted CSV data (list of dictionaries):")
        print(json.dumps(json_data, indent=4))  # Pretty-print the JSON
    else:
        print("Failed to convert CSV to JSON.")


    # Example usage with csv2dict and csv2ns:
    csv_data_dict = csv2json.csv2dict('another_data.csv')
    if csv_data_dict:
        print("CSV data as dictionary:")
        print(csv_data_dict)

    csv_data_ns = csv2json.csv2ns('another_data.csv')
    if csv_data_ns:
        print("CSV data as SimpleNamespace:")
        print(csv_data_ns)

"""

import json
import csv
from pathlib import Path
from typing import List, Dict
from types import SimpleNamespace
from src.logger import logger
from src.utils.csv import read_csv_as_dict, read_csv_as_ns, save_csv_file, read_csv_file
from src.utils.jjson import j_loads, j_dumps

def csv2dict(csv_file: str | Path, *args, **kwargs) -> dict | None:
    """
    Convert CSV data to a dictionary.

    Args:
        csv_file (str | Path): Path to the CSV file to read.
        *args: Additional positional arguments for `read_csv_as_dict`.
        **kwargs: Additional keyword arguments for `read_csv_as_dict`.

    Returns:
        dict | None: Dictionary containing the data from CSV, or `None` if conversion failed.
        Raises:
            Exception: If unable to read or parse the CSV.  Provides more detailed error information in logs.
    """
    try:
        return read_csv_as_dict(csv_file, *args, **kwargs)
    except Exception as e:
        logger.exception(f"Error converting CSV to dictionary: {e}")
        return None


def csv2ns(csv_file: str | Path, *args, **kwargs) -> SimpleNamespace | None:
    """
    Convert CSV data to SimpleNamespace objects.  Similar to csv2dict with error handling.

    Args:
        csv_file (str | Path): Path to the CSV file to read.
        *args: Additional positional arguments for `read_csv_as_ns`.
        **kwargs: Additional keyword arguments for `read_csv_as_ns`.

    Returns:
        SimpleNamespace | None: SimpleNamespace object containing the data from CSV, or `None` if conversion failed.
    """
    try:
        return read_csv_as_ns(csv_file, *args, **kwargs)
    except Exception as e:
        logger.exception(f"Error converting CSV to SimpleNamespace: {e}")
        return None


def csv_to_json(
    csv_file_path: str | Path,
    json_file_path: str | Path,
    exc_info: bool = True,
    encoding='utf-8'
) -> List[Dict[str, str]] | None:
    """! Convert a CSV file to JSON format and save it to a JSON file.
    Handles potential errors and logs them for debugging.


    Args:
        csv_file_path (str | Path): Path to the CSV file.
        json_file_path (str | Path): Path to the output JSON file.
        exc_info (bool, optional): Include traceback in log. Defaults to True.
        encoding (str, optional): Encoding for the CSV file (default: utf-8).

    Returns:
        List[Dict[str, str]] | None: The converted JSON data, or None if conversion failed.
    """
    try:
        data = read_csv_file(csv_file_path, encoding=encoding, exc_info=exc_info)
        if data is not None:
            with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
                json.dump(data, jsonfile, indent=4, ensure_ascii=False)  # Important: ensure_ascii=False
            return data
        return None  # Explicitly return None if data is empty or None
    except Exception as e:
        logger.error(f"Failed to convert CSV to JSON: {e}", exc_info=exc_info)
        return None


```

**Key Improvements and Explanations:**

* **Docstrings:**  More comprehensive and informative docstrings, including examples on how to use the functions and what types of data they return (important for users).  Uses more explicit error handling explanations.
* **Error Handling:** The `csv2dict`, `csv2ns`, and especially `csv_to_json` functions now use `try...except` blocks to catch potential exceptions during file reading and conversion.  Crucially, `logger.exception` is used to log detailed exception information, which is much more helpful for debugging.  This prevents the script from crashing and provides clear error messages in the logs.
* **Explicit `None` Return:** The `csv_to_json` function now explicitly returns `None` if `read_csv_file` returns `None`, providing clearer error handling and preventing unexpected behavior.
* **Encoding:** Added `encoding` parameter to `csv_to_json` and `read_csv_file` for more control over the encoding when reading CSV files. Defaults to utf-8, but this is a crucial detail for handling different file types.
* **JSON Output Enhancement:** In `csv_to_json`, the `json.dump` now has `ensure_ascii=False`.  This is crucial for proper encoding of non-ASCII characters in the JSON output.  The example in the docstring now includes `json.dumps` to show the correct way to print and handle the results.


These changes make the code much more robust, user-friendly, and easier to debug.  Remember to import the `logger` and related utilities (`read_csv_file`, etc.) from your appropriate `src` modules. Remember to adjust import paths (`src.logger`, `src.utils.csv`, etc) to match your project structure if necessary.
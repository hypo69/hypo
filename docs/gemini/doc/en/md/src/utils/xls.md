# hypotez/src/utils/xls.py

## Overview

This module provides functions for converting Excel (`xls`) files to JSON and vice-versa, handling multiple sheets and saving JSON data back to Excel files.  It includes error handling for robustness.

## Table of Contents

* [read_xls_as_dict](#read-xls-as-dict)
* [save_xls_file](#save-xls-file)


## Functions

### `read_xls_as_dict`

**Description**: Reads an Excel file, optionally converting a specific sheet to JSON and saving it to a file.  Handles potential errors during file reading and sheet processing.

**Parameters**:

- `xls_file` (str): Path to the input Excel file.
- `json_file` (str, optional): Path to save the output JSON file. Defaults to `None` (no saving).
- `sheet_name` (Union[str, int], optional): Name or index of the sheet to convert. Defaults to `None`. If `None`, all sheets are processed.

**Returns**:

- Union[Dict, List[Dict], bool]: A dictionary containing the converted data where keys are sheet names and values are lists of dictionaries. Returns `False` if an error occurs during file processing.

**Raises**:

- `FileNotFoundError`: If the input Excel file does not exist.
- `Exception`: If any other unexpected error occurs during file processing or sheet conversion.


### `save_xls_file`

**Description**: Saves JSON data to an Excel file.  Handles errors during file writing and sheet creation.

**Parameters**:

- `data` (Dict[str, List[Dict]]): A dictionary where keys are sheet names and values are lists of dictionaries representing the data to be saved.
- `file_path` (str): Path to the output Excel file.


**Returns**:

- bool: `True` if the file was saved successfully, `False` otherwise.

**Raises**:

- `Exception`: If any error occurs during Excel file writing.
# hypotez/src/utils/xls.py

## Overview

This module provides functions to convert Excel (`xls`) files to JSON format, handle multiple sheets, and save JSON data back to Excel files.  It uses the `pandas` library for data manipulation and handles potential errors gracefully.

## Table of Contents

* [read_xls_as_dict](#read_xls_as_dict)
* [save_xls_file](#save_xls_file)


## Functions

### `read_xls_as_dict`

**Description**: Reads an Excel file and converts it to JSON. Optionally, converts a specific sheet and saves the result to a JSON file.  Handles potential errors (file not found, sheet errors, etc.).

**Parameters**:

* `xls_file` (str): Path to the input Excel file.
* `json_file` (str, optional): Path to save the JSON output. Defaults to `None`.
* `sheet_name` (Union[str, int], optional): Name or index of the sheet to process. If `None`, all sheets are processed. Defaults to `None`.

**Returns**:

* Union[Dict, List[Dict], bool]:
    * A dictionary where keys are sheet names, and values are lists of dictionaries representing the data from the sheet(s). Returns `False` if an error occurs during file reading or processing.

**Raises**:

* `FileNotFoundError`: If the input Excel file is not found.
* `Exception`:  If an unexpected error occurs during file processing (e.g., an error reading from a specific sheet).


### `save_xls_file`

**Description**: Saves JSON data to an Excel file.  The data should be a dictionary where keys are sheet names and values are lists of dictionaries representing rows. Handles potential errors (e.g., file saving issues).

**Parameters**:

* `data` (Dict[str, List[Dict]]): Dictionary containing the data to save, with keys as sheet names and values as lists of dictionaries.
* `file_path` (str): Path to the output Excel file.

**Returns**:

* bool: `True` if the file was saved successfully; `False` otherwise.

**Raises**:

* `Exception`: If an error occurs during file saving (e.g., issues with the `xlsxwriter` engine).


## Usage Examples

```python
# Reading and optionally saving to JSON
data = read_xls_as_dict('input.xlsx', 'output.json', 'Sheet1')  # Reads sheet named 'Sheet1'
if data:
    print(data)  # Output will be {'Sheet1': [{...}]}

# Saving from JSON data
data_to_save = {'Sheet1': [{'column1': 'value1', 'column2': 'value2'}]}
success = save_xls_file(data_to_save, 'output.xlsx')
if success:
    print("Successfully saved to output.xlsx")
```
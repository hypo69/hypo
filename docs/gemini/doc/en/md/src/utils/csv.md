# src.utils.csv

## Overview

This module provides utilities for working with CSV and JSON files, including saving, reading, and converting data between formats. It leverages libraries like `csv`, `json`, `pathlib`, and `pandas` for efficient file handling.


## Table of Contents

* [save_csv_file](#save-csv-file)
* [read_csv_file](#read-csv-file)
* [read_csv_as_json](#read-csv-as-json)
* [read_csv_as_dict](#read-csv-as-dict)
* [read_csv_as_ns](#read-csv-as-ns)


## Functions

### `save_csv_file`

**Description**: Saves a list of dictionaries to a CSV file.  Appends to the file if it exists, otherwise creates a new file.

**Parameters**:
- `data` (List[Dict[str, str]]): List of dictionaries to save.  Must not be empty.
- `file_path` (Union[str, Path]): Path to the CSV file.
- `mode` (str, optional): File mode ('a' to append, 'w' to overwrite). Defaults to 'a'.
- `exc_info` (bool, optional): Include traceback information in logs. Defaults to True.

**Raises**:
- `TypeError`: If input `data` is not a list of dictionaries.
- `ValueError`: If input `data` is empty.

**Returns**:
- `bool`: True if successful, otherwise False.


### `read_csv_file`

**Description**: Reads CSV content from a file as a list of dictionaries.

**Parameters**:
- `file_path` (Union[str, Path]): Path to the CSV file.
- `exc_info` (bool, optional): Include traceback information in logs. Defaults to True.

**Raises**:
- `FileNotFoundError`: If the file does not exist.

**Returns**:
- `List[Dict[str, str]] | None`: List of dictionaries or None if failed.


### `read_csv_as_json`

**Description**: Converts a CSV file to JSON format and saves it to a new file.

**Parameters**:
- `csv_file_path` (Union[str, Path]): Path to the CSV file.
- `json_file_path` (Union[str, Path]): Path to save the JSON file.
- `exc_info` (bool, optional): Include traceback information in logs. Defaults to True.

**Returns**:
- `bool`: True if successful, otherwise False.


### `read_csv_as_dict`

**Description**: Converts CSV content to a dictionary.  The resulting dictionary will have a single key 'data' whose value is a list of dictionaries from the CSV file.


**Parameters**:
- `csv_file` (Union[str, Path]): Path to the CSV file.

**Returns**:
- `dict | None`: Dictionary representation of CSV content, or None if failed.


### `read_csv_as_ns`

**Description**: Loads CSV data into a list of dictionaries using Pandas.

**Parameters**:
- `file_path` (Union[str, Path]): Path to the CSV file.

**Returns**:
- `List[dict]`: List of dictionaries representing the CSV content.


**Raises**:
- `FileNotFoundError`: If the file does not exist.
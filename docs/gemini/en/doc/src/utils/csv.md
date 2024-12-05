# src.utils.csv

## Overview

This module provides utility functions for working with CSV and JSON files.  It includes functions for saving data to CSV files, reading data from CSV files, converting CSV to JSON, and converting CSV data into a Python dictionary or a list of dictionaries.  Error handling and logging are integrated using the `src.logger` module.


## Table of Contents

* [save_csv_file](#save-csv-file)
* [read_csv_file](#read-csv-file)
* [read_csv_as_json](#read-csv-as-json)
* [read_csv_as_dict](#read-csv-as-dict)
* [read_csv_as_ns](#read-csv-as-ns)


## Functions

### `save_csv_file`

**Description**: Saves a list of dictionaries to a CSV file.  Handles appending to existing files or overwriting.

**Parameters**:
- `data` (List[Dict[str, str]]): A list of dictionaries to be saved.
- `file_path` (Union[str, Path]): Path to the CSV file.
- `mode` (str, optional): File mode ('a' to append, 'w' to overwrite). Defaults to 'a'.
- `exc_info` (bool, optional): Include traceback information in logs. Defaults to True.

**Raises**:
- `TypeError`: If input `data` is not a list of dictionaries.
- `ValueError`: If input `data` is empty.

**Returns**:
- bool: `True` if the save operation was successful, `False` otherwise.


### `read_csv_file`

**Description**: Reads a CSV file's content as a list of dictionaries.

**Parameters**:
- `file_path` (Union[str, Path]): Path to the CSV file.
- `exc_info` (bool, optional): Include traceback information in logs. Defaults to True.

**Raises**:
- `FileNotFoundError`: If the file does not exist.

**Returns**:
- List[Dict[str, str]] | None: A list of dictionaries representing the CSV data, or `None` if an error occurred during the read operation.


### `read_csv_as_json`

**Description**: Converts a CSV file to JSON format and saves it to a new JSON file.

**Parameters**:
- `csv_file_path` (Union[str, Path]): Path to the CSV file.
- `json_file_path` (Union[str, Path]): Path to save the JSON file.
- `exc_info` (bool, optional): Include traceback information in logs. Defaults to True.


**Returns**:
- bool: `True` if successful, `False` if there was a failure.


### `read_csv_as_dict`

**Description**: Converts the content of a CSV file into a dictionary.

**Parameters**:
- `csv_file` (Union[str, Path]): Path to the CSV file.

**Returns**:
- dict | None: A dictionary representation of the CSV data, or `None` if an error occurred during conversion.


### `read_csv_as_ns`

**Description**: Reads a CSV file and returns the data as a list of dictionaries using the pandas library.

**Parameters**:
- `file_path` (Union[str, Path]): Path to the CSV file.

**Returns**:
- List[dict]: A list of dictionaries containing the data from the CSV file.  Returns an empty list if the file is not found or there is an error during loading.
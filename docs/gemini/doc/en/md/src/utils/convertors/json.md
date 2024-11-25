# hypotez/src/utils/convertors/json.py

## Overview

This module provides functions for converting JSON data to various formats: CSV, SimpleNamespace, XML, and XLS.  It leverages existing utility functions from other modules for specific conversions.

## Table of Contents

- [json2csv](#json2csv)
- [json2ns](#json2ns)
- [json2xml](#json2xml)
- [json2xls](#json2xls)


## Functions

### `json2csv`

**Description**: Converts JSON data (string, list of dictionaries, dictionary or JSON file path) to CSV format and saves it to a specified file.  Uses a comma as the delimiter.

**Parameters**:

- `json_data` (str | list | dict | Path): JSON data as a string, list of dictionaries, dictionary, or file path to a JSON file.
- `csv_file_path` (str | Path): Path to the CSV file to write.

**Returns**:

- bool: True if the conversion and save operation are successful, False otherwise.

**Raises**:

- `ValueError`: If the provided `json_data` is of an unsupported type.
- `Exception`: If there's an error parsing the JSON data or writing to the CSV file.


### `json2ns`

**Description**: Converts JSON data (string, dictionary, or JSON file path) to a SimpleNamespace object.

**Parameters**:

- `json_data` (str | dict | Path): JSON data as a string, dictionary, or file path to a JSON file.

**Returns**:

- SimpleNamespace: The parsed JSON data as a SimpleNamespace object.


**Raises**:

- `ValueError`: If the provided `json_data` is of an unsupported type.
- `Exception`: If there's an error parsing the JSON data.


### `json2xml`

**Description**: Converts JSON data (string, dictionary, or JSON file path) to XML format.  Uses the provided `root_tag` as the root element.

**Parameters**:

- `json_data` (str | dict | Path): JSON data as a string, dictionary, or file path to a JSON file.
- `root_tag` (str, optional): The root tag for the XML structure. Defaults to "root".

**Returns**:

- str: The resulting XML string.

**Raises**:

- `ValueError`: If the provided `json_data` is of an unsupported type.
- `Exception`: If there's an error parsing the JSON data or converting to XML.


### `json2xls`

**Description**: Converts JSON data (string, list of dictionaries, dictionary, or JSON file path) to XLS format and saves it to a specified file.

**Parameters**:

- `json_data` (str | list | dict | Path): JSON data as a string, list of dictionaries, dictionary, or file path to a JSON file.
- `xls_file_path` (str | Path): Path to the XLS file to write.

**Returns**:

- bool: True if the conversion and save operation are successful, False otherwise.

**Raises**:

- `ValueError`: If the provided `json_data` is of an unsupported type.
- `Exception`: If there's an error parsing the JSON data or writing to the XLS file.
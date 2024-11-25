# hypotez/src/utils/convertors/csv.py

## Overview

This module provides utilities for converting CSV data to dictionaries, SimpleNamespace objects, and JSON.  It also handles saving JSON data from CSV to file.


## Functions

### `csv2dict`

**Description**: Converts CSV data to a dictionary.

**Parameters**:
- `csv_file` (str | Path): Path to the CSV file to read.

**Returns**:
- `dict | None`: Dictionary containing the data from CSV converted to JSON format, or `None` if conversion failed.

**Raises**:
- `Exception`: If unable to read CSV.


### `csv2ns`

**Description**: Converts CSV data to SimpleNamespace objects.

**Parameters**:
- `csv_file` (str | Path): Path to the CSV file to read.


**Returns**:
- `SimpleNamespace | None`: SimpleNamespace object containing the data from CSV, or `None` if conversion failed.

**Raises**:
- `Exception`: If unable to read CSV.


### `csv_to_json`

**Description**: Converts a CSV file to JSON format and saves it to a JSON file.

**Parameters**:
- `csv_file_path` (str | Path): The path to the CSV file to read.
- `json_file_path` (str | Path): The path to the JSON file to save.
- `exc_info` (bool, optional): If True, includes traceback information in the log. Defaults to `True`.


**Returns**:
- `List[Dict[str, str]] | None`: The JSON data as a list of dictionaries, or `None` if conversion failed.

**Example**:
```python
>>> json_data = csv_to_json('dialogue_log.csv', 'dialogue_log.json')
>>> print(json_data)
[{'role': 'user', 'content': 'Hello'}, {'role': 'assistant', 'content': 'Hi there!'}]
```


**Raises**:
- `Exception`: If there's an error during file reading or writing, including errors in handling the `csv` or `json` data structures.  Error logging is facilitated through the `logger` module.
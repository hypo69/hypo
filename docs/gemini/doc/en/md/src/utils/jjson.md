# hypotez/src/utils/jjson.py

## Overview

This module provides functions for handling JSON and CSV files, including loading, dumping, merging data, and converting to/from SimpleNamespace objects. It supports reading from files, directories, or strings, and offers options for preserving data order and handling exceptions.


## Functions

### `j_dumps`

**Description**: Dumps JSON data to a file or returns it as a dictionary.  Handles SimpleNamespace objects and lists of dictionaries/SimpleNamespaces. Supports appending to existing files.

**Parameters**:

- `data` (Dict | SimpleNamespace | List[Dict] | List[SimpleNamespace]): JSON-compatible data or SimpleNamespace objects to dump.
- `file_path` (Optional[Path], optional): Path to the output file. If `None`, returns JSON as a dictionary. Defaults to `None`.
- `ensure_ascii` (bool, optional): If `True`, escapes non-ASCII characters in output. Defaults to `True`.
- `mode` (str, optional): File open mode ("w", "a+", "+a"). Defaults to "w".  `a+` appends to the beginning, `+a` to the end.  If the file exists and `mode` is `a+` or `+a`, existing data is read and merged appropriately.
- `exc_info` (bool, optional): If `True`, logs exceptions with traceback. Defaults to `True`.

**Returns**:

- `Optional[Dict]`: JSON data as a dictionary if successful, or `None` if an error occurs.


**Raises**:

- `ValueError`: If the `file_mode` is unsupported.


### `j_loads`

**Description**: Loads JSON or CSV data from a file, directory, or string. Supports merging JSON files from a directory. Can read from CSV files (converting to a list of dictionaries).

**Parameters**:

- `jjson` (Path | dict | str): Path to a file, directory, JSON data as a string, or JSON object.
- `ordered` (bool, optional): If `True`, returns `OrderedDict` to preserve element order. Defaults to `False`.
- `exc_info` (bool, optional): If `True`, logs exceptions with traceback. Defaults to `True`.

**Returns**:

- `Any`: A dictionary or list of dictionaries if successful, or `None` if an error occurs.


**Raises**:

- `FileNotFoundError`: If the specified file is not found.
- `json.JSONDecodeError`: If JSON data cannot be parsed.


### `j_loads_ns`

**Description**: Loads JSON or CSV data and converts it to SimpleNamespace objects.

**Parameters**:

- `jjson` (Path | SimpleNamespace | Dict | str): Path to a file, directory, or JSON data as a string, or JSON object.
- `ordered` (bool, optional): If `True`, preserves element order in the output. Defaults to `False`.
- `exc_info` (bool, optional): If `True`, logs exceptions with traceback. Defaults to `True`.

**Returns**:

- `Optional[SimpleNamespace | List[SimpleNamespace]]`: Returns a `SimpleNamespace` or a list of `SimpleNamespace` objects if successful. Returns `None` if the input is not found or cannot be read.


### `replace_key_in_json`

**Description**: Recursively replaces a key in a dictionary or list.


**Parameters**:

- `data` (dict | list): The dictionary or list where key replacement occurs.
- `old_key` (str): The key to be replaced.
- `new_key` (str): The new key.

**Returns**:

- `dict`: The updated dictionary with replaced keys.

**Example Usage (included in docstring):** Demonstrates various cases of key replacement, including simple, nested, list, and mixed structures.


### `process_json_file`

**Description**: Processes a single JSON file, replacing the key `"name"` with `"category_name"`.

**Parameters**:

- `json_file` (Path): Path to the JSON file.

**Raises**:

- Logs errors with traceback if any issues occur during the process.


### `recursive_process_json_files`

**Description**: Recursively processes all JSON files within a directory, replacing the `"name"` key with `"category_name"`.

**Parameters**:

- `directory` (Path): Path to the directory to process.

**Raises**:

- Logs errors with traceback if any issues occur during the process.


### `extract_json_from_string`

**Description**: Extracts JSON content from a Markdown string between ```json``` and ``` markers.


**Parameters**:

- `md_string` (str): The Markdown string to search.

**Returns**:

- `str`: The extracted JSON string, or an empty string if no JSON is found.

**Raises**:

- Logs errors with traceback if any issues occur during the process.
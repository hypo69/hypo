# Module: hypotez/src/utils/jjson.py

## Overview

This module provides functions for handling JSON and CSV files, including loading, dumping, merging, and conversion to `SimpleNamespace` objects. It supports various file formats, error handling, and data processing tasks.

## Table of Contents

- [j_dumps](#j_dumps)
- [j_loads](#j_loads)
- [j_loads_ns](#j_loads_ns)
- [process_json_file](#process_json_file)
- [recursive_process_json_files](#recursive_process_json_files)
- [extract_json_from_string](#extract_json_from_string)

## Functions

### `j_dumps`

**Description**: Dumps JSON data to a file or returns the JSON data as a dictionary.  Handles different data types (dict, SimpleNamespace, lists of those).  Supports appending to existing files.

**Parameters**:
- `data` (Dict | SimpleNamespace | List[Dict] | List[SimpleNamespace]): JSON-compatible data or SimpleNamespace objects to dump.
- `file_path` (Optional[Path], optional): Path to the output file. If `None`, returns JSON as a dictionary. Defaults to `None`.
- `ensure_ascii` (bool, optional): If `True`, escapes non-ASCII characters in output. Defaults to `True`.
- `mode` (str, optional): File open mode ('w', 'a+', '+a'). Defaults to 'w'.  'a+' appends to existing data, '+a' appends, overwriting the file if it exists.
- `exc_info` (bool, optional): If `True`, logs exceptions with traceback. Defaults to `True`.

**Returns**:
- `Optional[Dict]`: JSON data as a dictionary if successful, or `None` if an error occurs.

**Raises**:
- `ValueError`: If the `file_mode` is unsupported.
- (various exceptions): Various exceptions related to file operations or JSON parsing during file IO. Errors during the `json.load` step will result in `None` return.


### `j_loads`

**Description**: Loads JSON or CSV data from a file, directory, or string.  Can handle directories containing JSON files and merges them if the format allows.  Handles CSV files as well.

**Parameters**:
- `jjson` (Path | dict | str): Path to a file, directory, JSON data as a string, or JSON object.
- `ordered` (bool, optional): If `True`, returns `OrderedDict` to preserve element order. Defaults to `False`.
- `exc_info` (bool, optional): If `True`, logs exceptions with traceback. Defaults to `True`.

**Returns**:
- `Any`: A dictionary or list of dictionaries if successful, or `None` if an error occurs.


**Raises**:
- `FileNotFoundError`: If the specified file is not found.
- `json.JSONDecodeError`: If JSON data could not be parsed.
- (various exceptions): Various exceptions related to file operations or JSON parsing.  Will catch and log many exceptions.  `None` will be returned on any failure.


### `j_loads_ns`

**Description**: Loads JSON or CSV data, converts it to `SimpleNamespace` objects. Handles similar inputs to `j_loads`.

**Parameters**:
- `jjson` (Path | SimpleNamespace | Dict | str): Path to a file, directory, JSON data as a string, or JSON object.
- `ordered` (bool, optional): If `True`, returns `OrderedDict` to preserve element order. Defaults to `False`.
- `exc_info` (bool, optional): If `True`, logs exceptions with traceback. Defaults to `True`.

**Returns**:
- `Optional[SimpleNamespace | List[SimpleNamespace]]`: Returns `SimpleNamespace` or a list of `SimpleNamespace` objects if successful. Returns `None` if `jjson` is not found or cannot be read.

**Raises**:
- (various exceptions): Similar to `j_loads` related to file access and JSON parsing.


### `process_json_file`

**Description**: Processes a JSON file, replacing the 'name' key with 'category_name'.

**Parameters**:
- `json_file` (Path): Path to the JSON file.

**Raises**:
- (various exceptions): Any exceptions during file reading, JSON parsing, or writing.


### `recursive_process_json_files`

**Description**: Recursively processes JSON files within a directory and its subdirectories, replacing 'name' with 'category_name'.

**Parameters**:
- `directory` (Path): Path to the directory containing the JSON files.

**Raises**:
- (various exceptions): Any exceptions during file reading, JSON parsing, or writing.


### `extract_json_from_string`

**Description**: Extracts JSON content from a Markdown string.

**Parameters**:
- `md_string` (str): The Markdown string that might contain JSON enclosed in ```json ```.

**Returns**:
- `str`: The extracted JSON string or an empty string if not found.  Returns an empty string on error.

**Raises**:
- (various exceptions): Any exceptions during regex matching or handling.
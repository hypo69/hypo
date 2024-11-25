# src.suppliers.aliexpress.gapi.header

## Overview

This module defines the root path to the project. All imports are built relative to this path.  Future versions should move this to a system variable.  It currently handles finding the project root using marker files like `pyproject.toml`, `requirements.txt`, and `.git`.


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory.  Searches upwards until a directory containing any of the specified marker files is found.

**Parameters**:

- `marker_files` (tuple): Filenames or directory names used to identify the project root. Defaults to a tuple containing `'pyproject.toml'`, `'requirements.txt'`, and `.git`.


**Returns**:

- `Path`: The path to the root directory if found, otherwise the directory containing the current script.


**Raises**:

- `None`: No exceptions are explicitly raised. The function may implicitly raise `FileNotFoundError` if marker files are not found but will not handle this error directly.


### Initialization Section

**Description**:  This section initializes and sets the `__root__` variable.  It also includes error handling when attempting to load settings from `src/settings.json` and the `README.MD`.

**Variable initialization**:

- `__root__`: The absolute path to the project root. Calculated by calling the `set_project_root` function.
- `settings`: A dictionary containing project settings. Loaded from `src/settings.json`.
- `doc_str`: A string containing the documentation from the `README.MD` file.


**Error handling**:

- If `settings.json` is not found or cannot be parsed, `settings` will be `None`.
- If `README.MD` is not found or cannot be parsed, `doc_str` will be `None`.

**Constants**:

- `__project_name__`: String representing the project name. Uses the value from `settings` if available, otherwise defaults to `'hypotez'`.
- `__version__`: String representing the project version. Uses the value from `settings` if available, otherwise defaults to `''`.
- `__doc__`: String representing the project documentation. Uses the value from `doc_str` if available, otherwise defaults to `''`.
- `__details__`: String representing project details. Initialized as an empty string.
- `__author__`: String representing the author of the project. Uses the value from `settings` if available, otherwise defaults to `''`.
- `__copyright__`: String representing copyright information. Uses the value from `settings` if available, otherwise defaults to `''`.
- `__cofee__`: String representing a link for support, which defaults to a specific link. Uses value from settings if it exists; otherwise, defaults to the provided URL.


## Modules

- `sys`: Python's system module.
- `json`: Python's JSON encoding/decoding module.
- `pathlib`: Python's pathlib module for working with file paths.
- `packaging.version`: Python library for handling version numbers.
- `src.gs`: A module assumed to be present, but not explicitly documented here.

## File Information

- Location: `hypotez/src/suppliers/aliexpress/gapi/header.py`
- Encoding: UTF-8
- Shebang lines: Specify Python interpreters.
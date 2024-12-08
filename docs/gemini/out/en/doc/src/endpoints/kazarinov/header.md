# hypotez/src/endpoints/kazarinov/header.py

## Overview

This module provides functions for setting the project root directory, loading project settings, and retrieving project metadata. It utilizes the `gs` module for path manipulation and handles potential errors during file loading.

## Table of Contents

- [set_project_root](#set-project-root)
- [Module Constants](#module-constants)

## Functions

### `set_project_root`

**Description**: This function finds the root directory of the project. It starts from the current file's directory and searches upwards until it finds a directory containing any of the specified marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`). If no such directory is found, it returns the directory where the script is located.

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: The path to the root directory of the project if found, otherwise the directory where the script is located.

**Example Usage**:

```python
root_path = set_project_root()
print(root_path)
```

### Module Constants

**Description**: This section documents the module's constants.

- `__root__` (Path): Path to the root directory of the project. Determined by the `set_project_root` function.
- `settings` (dict): Project settings loaded from `settings.json`.
- `doc_str` (str): Project documentation loaded from `README.MD`.
- `__project_name__` (str): Project name. Defaults to "hypotez".
- `__version__` (str): Project version. Defaults to empty string.
- `__doc__` (str): Project documentation. Defaults to empty string.
- `__details__` (str): Project details. Defaults to empty string.
- `__author__` (str): Project author. Defaults to empty string.
- `__copyright__` (str): Project copyright. Defaults to empty string.
- `__cofee__` (str):  Project coffee link. Defaults to a link for supporting the developer with a coffee.


**Raises**:

- `FileNotFoundError`: Raised if `settings.json` or `README.MD` is not found.
- `json.JSONDecodeError`: Raised if the JSON data in `settings.json` is invalid.

**Implementation Details**:
The function `set_project_root` uses a `try...except` block to handle `FileNotFoundError` or `json.JSONDecodeError`.  The module variables (`settings`, `doc_str`) are set based on the file reading; empty strings or default values are used if the files are not found or the JSON is invalid, preventing the program from crashing.  The function modifies `sys.path` to ensure the root directory is accessible, improving code reusability across modules.



```
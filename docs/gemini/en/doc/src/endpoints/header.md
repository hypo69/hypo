# hypotez/src/endpoints/header.py

## Overview

This module contains the header logic for the Hypotez project. It defines functions for finding the project root directory and loading settings from a JSON file.


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory, searching upwards until a directory containing specific marker files (like `pyproject.toml`, `requirements.txt`, `.git`) is found. If no such directory is found, it returns the directory where the script is located.

**Parameters**:
- `marker_files` (tuple): Filenames or directory names to identify the project root. Defaults to (`'pyproject.toml'`, `'requirements.txt'`, `'.git'`).

**Returns**:
- `Path`: Path to the root directory if found, otherwise the directory where the script is located.

**Raises**:
-  No exceptions are explicitly raised in the function.


### `set_project_root`

**Description**: This function finds the project root directory by checking parent directories for specific marker files. It modifies `sys.path` to include the root directory.

**Parameters**:
- `marker_files` (tuple, optional): A tuple of file or directory names that indicate the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').

**Returns**:
- `Path`: The path to the project root directory.

**Raises**:
- No exceptions are explicitly raised in this function.


## Variables

### `__root__`

**Description**:  A variable storing the path to the root directory of the project, obtained by calling `set_project_root()`.  Its type is `Path`.

### `settings`

**Description**: A variable holding the project settings loaded from `src/settings.json`. Its type is `dict` or `None`.

### `doc_str`

**Description**:  A variable storing the content of the project's `README.MD` file.  Its type is `str` or `None`.

### `__project_name__`

**Description**: The name of the project. Defaults to 'hypotez' if `settings` are not loaded or `project_name` is not found in the settings. Its type is `str`.


### `__version__`

**Description**: The version of the project. Defaults to an empty string if `settings` are not loaded or `version` is not found. Its type is `str`.


### `__doc__`

**Description**: The project's documentation. Defaults to an empty string if `doc_str` is not loaded.  Its type is `str`.


### `__details__`

**Description**: A string storing project details.  Defaults to an empty string. Its type is `str`.

### `__author__`

**Description**: The author of the project. Defaults to an empty string if not found in the settings. Its type is `str`.

### `__copyright__`

**Description**: The copyright information for the project. Defaults to an empty string if not found in the settings. Its type is `str`.

### `__cofee__`

**Description**: A string containing a link to support the developer through a coffee donation. Defaults to a specific link if the `cofee` key is not found in the settings.  Its type is `str`.
# hypotez/src/endpoints/prestashop/api/header.py

## Overview

This module provides functions for setting the project root directory and loading project settings from a JSON file. It also handles potential errors during file loading.  The module uses the `gs` module for path manipulation.


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory, searching upwards.

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names to identify the project root.  Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: The path to the root directory if found, otherwise the directory where the script is located.

**Raises**:

- No exceptions are explicitly raised, but `FileNotFoundError` or similar could occur if the marker files are not found anywhere in the search path.


### `set_project_root`

**Description**: (Repeated, likely a copy/paste issue in the original code.) Finds the root directory of the project starting from the current file's directory, searching upwards.

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names to identify the project root.  Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: The path to the root directory if found, otherwise the directory where the script is located.

**Raises**:

- No exceptions are explicitly raised, but `FileNotFoundError` or similar could occur if the marker files are not found anywhere in the search path.


## Variables

### `__root__`

**Description**: The path to the root directory of the project, obtained from `set_project_root()`.

**Type**: `Path`

### `settings`

**Description**: A dictionary containing project settings loaded from `settings.json`.  Initialized to `None`.

**Type**: `dict`

### `doc_str`

**Description**: The content of the README.MD file. Initialized to `None`.

**Type**: `str`


### `__project_name__`

**Description**: The project name obtained from the `settings` dictionary, defaulting to 'hypotez'.

**Type**: `str`

### `__version__`

**Description**: The project version obtained from the `settings` dictionary, defaulting to ''.

**Type**: `str`

### `__doc__`

**Description**: The documentation string obtained from the README.md file, defaulting to ''.

**Type**: `str`

### `__details__`

**Description**: Additional details about the project.  Initialized to ''.

**Type**: `str`

### `__author__`

**Description**: The author of the project obtained from the `settings` dictionary, defaulting to ''.

**Type**: `str`

### `__copyright__`

**Description**: The copyright information obtained from the `settings` dictionary, defaulting to ''.

**Type**: `str`

### `__cofee__`

**Description**: The link to support the developer with a cup of coffee.  Obtained from the `settings` dictionary, defaulting to a provided link.

**Type**: `str`


## Error Handling

The module includes `try...except` blocks to handle potential `FileNotFoundError` and `json.JSONDecodeError` exceptions during file reading.  This ensures graceful failure and prevents the script from crashing if the configuration files are not found or have invalid format. The `...` in the except blocks signifies that the errors are silently ignored; this could be improved by providing more specific handling or logging.


## Module Usage

The module provides functions for setting the project root directory and loading project settings from a JSON file. This is crucial for ensuring consistent access to project resources and configurations across different scripts and modules within the project. The use of `__root__` ensures the project root is accessible from any location within the project.
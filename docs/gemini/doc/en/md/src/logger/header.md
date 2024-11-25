# hypotez/src/logger/header.py

## Overview

This module defines the root path of the project. All imports are relative to this path.

## Functions

### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory.  It searches upwards through parent directories until it finds a directory containing any of the specified marker files.

**Parameters**:

- `marker_files` (tuple): Filenames or directory names to identify the project root.  Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.


**Returns**:

- `Path`: Path to the root directory if found; otherwise, the directory where the script is located.


**Raises**:

- No exceptions are explicitly raised, though file access issues could cause errors.


### `get_settings`

**Description**: This function attempts to load settings from the `settings.json` file in the project root.


**Returns**:

- `dict`:  The loaded JSON data.  Returns `None` if the file does not exist or is invalid JSON.


**Raises**:

- `FileNotFoundError`: If the `settings.json` file is not found.
- `json.JSONDecodeError`: If the `settings.json` file is not valid JSON.


### `get_documentation_string`

**Description**: Loads the content of the README.MD file in the project root as a string.


**Returns**:

- `str`: The content of README.MD or an empty string if it's not found.

**Raises**:

- `FileNotFoundError`: If the README.MD file is not found.
- `json.JSONDecodeError`: If there is an issue parsing the file's content.


## Global Variables

### `__root__`

**Description**: Path to the root directory of the project. Determined by the `set_project_root` function.

**Type**: `Path`


### `settings`

**Description**: A dictionary containing project settings loaded from `settings.json`.  Defaults to `None` if the file is not found or invalid.

**Type**: `dict | None`


### `__project_name__`

**Description**: The project name, taken from the settings or defaults to "hypotez".

**Type**: `str`


### `__version__`

**Description**: The project version, taken from the settings or defaults to an empty string.

**Type**: `str`

### `__doc__`

**Description**: The content of the project README, taken from `README.MD` or an empty string.

**Type**: `str`


### `__details__`

**Description**: Placeholder for more detailed project information.

**Type**: `str`

### `__author__`

**Description**: The author's name, taken from the settings or defaults to an empty string.

**Type**: `str`

### `__copyright__`

**Description**: The copyright information, taken from the settings or defaults to an empty string.

**Type**: `str`


### `__cofee__`

**Description**: Link to a coffee donation for the developer.

**Type**: `str`
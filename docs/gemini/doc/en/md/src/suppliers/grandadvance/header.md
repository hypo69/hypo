# hypotez/src/suppliers/grandadvance/header.py

## Overview

This module, `header.py`, provides functions for setting the project root directory and accessing project-level settings and documentation. It utilizes the `gs` module for path manipulation and relies on a `settings.json` file located in the project root directory for configuration.  The module also retrieves documentation from a `README.MD` file.


## Functions

### `set_project_root`

**Description**: This function finds the root directory of the project. It starts from the directory of the current file and searches up the directory tree until it encounters a directory containing specified marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`).

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names to identify the project root. Defaults to (`'pyproject.toml'`, `'requirements.txt'`, `.git`).

**Returns**:

- `Path`: The path to the root directory of the project. If no marker files are found, it returns the directory where the script is located.

**Raises**:

- None


### `settings_loading`

**Description**: Attempts to load settings from the `settings.json` file in the project root.  If the file is not found or cannot be parsed as JSON, it handles the exception gracefully.


**Parameters**:

- None

**Returns**:

- `dict`: The project settings, or `None` if the settings file cannot be loaded.

**Raises**:

- `FileNotFoundError`: If the `settings.json` file is not found.
- `json.JSONDecodeError`: If the `settings.json` file is not valid JSON.


### `documentation_loading`

**Description**: Attempts to load documentation from the `README.MD` file in the project root. If the file is not found or cannot be parsed, it handles the exception gracefully.


**Parameters**:

- None

**Returns**:

- `str`: The project documentation string, or `None` if the documentation file cannot be loaded.

**Raises**:

- `FileNotFoundError`: If the `README.MD` file is not found.
- `json.JSONDecodeError`: If there is an error decoding the README file.



## Variables

### `__root__`

**Description**: The path to the project root directory, obtained from `set_project_root`.

**Type**: `Path`


### `__project_name__`

**Description**: The name of the project. Defaults to `hypotez`, and is obtained from the `settings.json` file if found, otherwise defaults to `hypotez`.

**Type**: `str`

### `__version__`

**Description**: The version of the project, obtained from the `settings.json` file if found, otherwise defaults to an empty string.

**Type**: `str`


### `__doc__`

**Description**: The documentation string of the project, obtained from the `README.MD` file if found, otherwise defaults to an empty string.

**Type**: `str`


### `__details__`

**Description**: A placeholder for project details. Currently empty.

**Type**: `str`


### `__author__`

**Description**: The author of the project, obtained from the `settings.json` file if found, otherwise defaults to an empty string.

**Type**: `str`


### `__copyright__`

**Description**: The copyright of the project, obtained from the `settings.json` file if found, otherwise defaults to an empty string.

**Type**: `str`

### `__cofee__`

**Description**: A string that links to a donate button for a cup of coffee. It defaults to a specific link if the `settings.json` file doesn't contain the key.

**Type**: `str`
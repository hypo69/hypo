# hypotez/src/goog/drive/header.py

## Overview

This module, `src.goog.drive`, provides functions for interacting with Google Drive services, with a primary focus on retrieving project-related configuration. It establishes the project's root directory and loads settings from a JSON file.


## Functions

### `set_project_root`

**Description**: This function determines the root directory of the project by traversing up the directory tree from the current file's location. It searches for specific marker files (`pyproject.toml`, `requirements.txt`, `.git`) within parent directories.

**Parameters**:

- `marker_files` (tuple): A tuple containing filenames or directory names used to identify the project root.  Defaults to a tuple containing `'pyproject.toml'`, `'requirements.txt'`, and `.git`.

**Returns**:

- `Path`: The path to the project root directory. If no marker files are found, it returns the path of the current file's directory.


**Raises**:

- None


### `set_settings`

**Description**: This function attempts to load project settings from a JSON file located within the project root directory.

**Parameters**:

- None

**Returns**:

- `dict | None`: Returns the loaded settings as a dictionary if the file exists and is valid JSON. Returns `None` if the file is not found or cannot be parsed as JSON.

**Raises**:

- `FileNotFoundError`: If the settings file (`src/settings.json`) is not found.
- `json.JSONDecodeError`: If the settings file is found but cannot be parsed as valid JSON.



### `get_documentation_string`

**Description**: This function attempts to load the project's documentation from a README.MD file located within the project root directory.

**Parameters**:

- None

**Returns**:

- `str | None`: Returns the content of the README file as a string if the file exists. Returns `None` if the file is not found.

**Raises**:

- `FileNotFoundError`: If the documentation file (`src/README.MD`) is not found.
- `json.JSONDecodeError`:  This error is not raised as no JSON parsing is performed on the README file.



## Variables

### `__root__`

**Description**: A `Path` object representing the root directory of the project. Initialized by calling the `set_project_root` function.

**Type**: `Path`


### `__project_name__`
**Description**: The name of the project. Retrieved from the settings file if available, otherwise defaults to 'hypotez'.
**Type**: `str`

### `__version__`
**Description**: The version of the project. Retrieved from the settings file if available, otherwise defaults to ''.
**Type**: `str`

### `__doc__`
**Description**: The project documentation string. Retrieved from the documentation file if available, otherwise defaults to ''.
**Type**: `str`

### `__details__`
**Description**: Additional project details (currently empty).
**Type**: `str`

### `__author__`
**Description**: The author of the project. Retrieved from the settings file if available, otherwise defaults to ''.
**Type**: `str`

### `__copyright__`
**Description**: The copyright information of the project. Retrieved from the settings file if available, otherwise defaults to ''.
**Type**: `str`

### `__cofee__`
**Description**: A link to a coffee donation option for the developer. Retrieved from the settings file if available, otherwise defaults to a specified URL.
**Type**: `str`


## Module Constants

### `MODE`

**Description**: A string variable used to set the development mode.
**Value**: `'dev'`
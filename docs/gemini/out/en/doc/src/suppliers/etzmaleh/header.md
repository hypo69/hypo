# hypotez/src/suppliers/etzmaleh/header.py

## Overview

This module, `header.py`, provides functions for setting the project root directory and loading project settings.  It also defines constants related to the project's configuration.


## Functions

### `set_project_root`

**Description**: This function determines the root directory of the project. It starts from the current file's directory and traverses up the directory tree until it finds a directory containing specific marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`). If a root directory is not found, it defaults to the directory where the script is located. It also adds the root directory to the Python path.

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names used to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: A `Path` object representing the root directory of the project.

**Raises**:

- No exceptions are explicitly documented to be raised.


### `load_settings`

**Description**:  (Implicit function) Loads project settings from a JSON file. This function is not explicitly defined in the code, but its operation is implicit given the `try...except` blocks around the file access and JSON loading.

**Parameters**:

- None.

**Returns**:

- `dict`: A dictionary containing the project settings, if successfully loaded.  Returns `None` if the file is not found or if there is an error parsing the JSON data.

**Raises**:

- `FileNotFoundError`: Raised if the settings file (`settings.json`) does not exist.
- `json.JSONDecodeError`: Raised if the settings file is not a valid JSON document.



## Constants

### `MODE`

**Description**: A string variable that is set to `'dev'`

**Type**: `str`

**Value**: `'dev'`




## Global Variables


### `__root__`

**Description**: A global variable that stores the project root path, determined by calling `set_project_root()`.


**Type**: `Path`


**Usage**:  This variable is intended to be used throughout the project to access project-level resources.


### `settings`

**Description**: A global variable that stores the project settings (a dictionary).  It is loaded from the 'settings.json' file within the project root directory if available.

**Type**: `dict` | `None`


### `__project_name__`

**Description**: A global string variable, representing the project name.  Its value is taken from the `settings.json` if available, otherwise defaults to 'hypotez'.


**Type**: `str`


### `__version__`

**Description**: A global string variable, representing the project version.  Its value is taken from the `settings.json` if available, otherwise defaults to an empty string.


**Type**: `str`


### `__doc__`


**Description**: A global string variable, representing the project documentation (README.MD). Its value is taken from the `README.MD` file if available, otherwise defaults to an empty string.


**Type**: `str`


### `__details__`

**Description**: A global string variable, representing the project details. Currently contains an empty string.


**Type**: `str`


### `__author__`

**Description**: A global string variable, representing the project author. Its value is taken from the `settings.json` if available, otherwise defaults to an empty string.


**Type**: `str`


### `__copyright__`

**Description**: A global string variable, representing the project copyright information. Its value is taken from the `settings.json` if available, otherwise defaults to an empty string.


**Type**: `str`


### `__cofee__`

**Description**: A global string variable, containing information about how to support the project's development (e.g. a link to a coffee donation platform). Its value is taken from the `settings.json` if available, otherwise defaults to a predefined string.


**Type**: `str`
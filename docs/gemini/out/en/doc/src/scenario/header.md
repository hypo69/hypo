# hypotez/src/scenario/header.py

## Overview

This module defines functions for finding the project root directory and loading project settings. It also handles potential errors during file loading.


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project by searching upwards from the current file's directory until it finds a directory containing specified marker files (pyproject.toml, requirements.txt, .git).

**Parameters**:
- `marker_files` (tuple): A tuple of filenames or directory names to identify the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').


**Returns**:
- `Path`: The path to the root directory if found, otherwise the directory where the script is located.

**Raises**:
- None


### `set_project_root`

**Description**:
This function attempts to load project settings from settings.json file located in the project root directory.

**Returns**:
- `dict`: A dictionary containing project settings, if loaded successfully. Otherwise returns `None`.

**Raises**:
- `FileNotFoundError`: If the settings.json file does not exist.
- `json.JSONDecodeError`: If the settings.json file contains invalid JSON data.

### `set_project_root`

**Description**:
This function attempts to load project documentation (README.MD) from the project root directory.

**Returns**:
- `str`: The content of the README.MD file, if found and read successfully. Otherwise returns an empty string.


**Raises**:
- `FileNotFoundError`: If the README.MD file does not exist.
- `json.JSONDecodeError`:  If the README.MD file contains invalid data.

## Global Variables

### `__root__`

**Description**: Holds the path to the project root directory obtained by calling the `set_project_root` function.


### `settings`

**Description**:  A dictionary containing project settings. Defaults to `None`. Populated by loading data from `settings.json`.


### `doc_str`

**Description**:  A string containing the project's documentation (if available). Defaults to `None`. Populated by reading data from `README.MD`.


### `__project_name__`

**Description**:  The project name, retrieved from `settings.json`. Defaults to 'hypotez'.


### `__version__`

**Description**: The project version, retrieved from `settings.json`. Defaults to empty string.


### `__doc__`

**Description**: The project documentation string. Defaults to empty string.


### `__details__`

**Description**:  The project details. Defaults to empty string.


### `__author__`

**Description**:  The project author, retrieved from `settings.json`. Defaults to empty string.


### `__copyright__`

**Description**: The project copyright, retrieved from `settings.json`. Defaults to empty string.


### `__cofee__`

**Description**: A link to a donation page for the developer. Defaults to a specific URL.
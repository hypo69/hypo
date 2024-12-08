# hypotez/src/endpoints/advertisement/facebook/header.py

## Overview

This module provides functionality for setting the project root directory and loading project settings. It utilizes the `gs` module for file path manipulation and the `json` module for reading settings from a JSON file.


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project. It searches upward from the current file's location until it finds a directory containing any of the specified marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`).

**Parameters**:
- `marker_files` (tuple): A tuple of filenames or directory names used to identify the project root. Defaults to a tuple containing `'pyproject.toml'`, `'requirements.txt'`, and `.git`.


**Returns**:
- `Path`: The path to the root directory if found, otherwise the directory where the script is located.


## Module Constants

### `MODE`

**Description**: A string constant representing the project mode (e.g., 'dev', 'prod').


## Variables

### `__root__`

**Description**: A path object representing the root directory of the project, obtained by calling `set_project_root()`.


### `settings`

**Description**: A dictionary containing project settings loaded from `settings.json`.  Defaults to `None` if the file is not found or if there is a JSON decoding error.


### `doc_str`

**Description**: A string containing the documentation from `README.MD`, loaded if found.  Defaults to `None` if the file is not found or is malformed.  


### `__project_name__`

**Description**: String representing the project name. Defaults to 'hypotez' if the 'project_name' key is not found in the settings or if the `settings` variable is `None`.

### `__version__`

**Description**: String representing the project version. Defaults to an empty string if the 'version' key is not found in the settings or if the `settings` variable is `None`.

### `__doc__`

**Description**: String representing the project documentation.  Defaults to an empty string if `doc_str` is `None`.

### `__details__`

**Description**: String representing project details. Defaults to an empty string.

### `__author__`

**Description**: String representing the author of the project. Defaults to an empty string if the 'author' key is not found in the settings or if the `settings` variable is `None`.

### `__copyright__`

**Description**: String representing the copyright information. Defaults to an empty string if the 'copyright' key is not found in the settings or if the `settings` variable is `None`.

### `__cofee__`

**Description**: String containing information to support the development team. Defaults to a predefined string if the `cofee` key is not found in the settings or if `settings` is `None`.

**Raises**:
- `FileNotFoundError`: Raised if `settings.json` or `README.MD` is not found.
- `json.JSONDecodeError`: Raised if there is an error decoding the JSON data in `settings.json`.
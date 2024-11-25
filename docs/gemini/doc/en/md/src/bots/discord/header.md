# hypotez/src/bots/discord/header.py

## Overview

This module contains header information and utility functions for the Discord bot. It defines constants, sets the project root, loads settings from a JSON file, and retrieves documentation from a README file.

## Functions

### `set_project_root`

**Description**: Finds the root directory of the project. It searches upwards from the current file's directory until it finds a directory containing any of the specified marker files (pyproject.toml, requirements.txt, .git).

**Parameters**:
- `marker_files` (tuple): A tuple of filenames or directory names to identify the project root. Defaults to a tuple containing 'pyproject.toml', 'requirements.txt', '.git'.

**Returns**:
- `Path`: The path to the root directory of the project. If no such directory is found, returns the directory where the script is located.


**Raises**:
-  N/A


## Variables

### `MODE`

**Description**:  Represents the current mode (e.g., 'dev', 'prod').

**Type**: str


### `__root__`

**Description**: The root directory of the project, obtained from `set_project_root()`.

**Type**: Path

### `settings`

**Description**: A dictionary containing project settings, loaded from settings.json.

**Type**: dict


### `doc_str`

**Description**: String containing documentation from README.MD, if found.

**Type**: str


### `__project_name__`

**Description**: The name of the project, obtained from `settings`. Defaults to 'hypotez'.

**Type**: str


### `__version__`

**Description**: The version of the project, obtained from `settings`. Defaults to ''.

**Type**: str


### `__doc__`

**Description**: The documentation string, obtained from `doc_str`. Defaults to ''.

**Type**: str


### `__details__`

**Description**: Additional details string. Currently empty.

**Type**: str


### `__author__`

**Description**: The author of the project, obtained from `settings`. Defaults to ''.

**Type**: str


### `__copyright__`

**Description**: The copyright information, obtained from `settings`. Defaults to ''.

**Type**: str


### `__cofee__`

**Description**: A string containing a link for donating coffee to the developer. Defaults to a provided link.

**Type**: str


## Errors


**Description**:  Error handling for loading settings and documentation.

-   `FileNotFoundError`: Caught when `settings.json` or `README.MD` is not found.
-   `json.JSONDecodeError`: Caught when the JSON data in `settings.json` is invalid.
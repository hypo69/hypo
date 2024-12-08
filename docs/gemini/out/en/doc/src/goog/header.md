# hypotez/src/goog/header.py

## Overview

This module provides functions for setting the project root directory and loading project settings. It utilizes the `gs` module and handles potential errors during file loading.


## Functions

### `set_project_root`

**Description**: This function finds the root directory of the project by searching upwards from the current file's directory. It stops at the first directory containing specified marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`).

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names to identify the project root. Defaults to (`'pyproject.toml'`, `'requirements.txt'`, `'.git'`).


**Returns**:

- `Path`: The path to the root directory if found, otherwise the directory where the script is located.


**Raises**:
None.


### `__init__`

**Description**: Initializes the module, retrieving project settings from `settings.json` and project documentation from `README.MD`.

**Parameters**:
None.

**Returns**:
None.

**Raises**:
- `FileNotFoundError`: Raised if `settings.json` or `README.MD` is not found.
- `json.JSONDecodeError`: Raised if `settings.json` is not a valid JSON file.


## Variables

### `__root__`

**Description**: Path to the root directory of the project.

**Type**: `Path`


### `settings`

**Description**: Project settings loaded from `settings.json`.

**Type**: `dict` | `None`


### `doc_str`

**Description**: Project documentation loaded from `README.MD`.

**Type**: `str` | `None`


### `__project_name__`

**Description**: Project name retrieved from the `settings.json` file.

**Type**: `str`


### `__version__`

**Description**: Project version retrieved from the `settings.json` file.

**Type**: `str`


### `__doc__`

**Description**: Project documentation string.

**Type**: `str`


### `__details__`

**Description**: Project details.

**Type**: `str`


### `__author__`

**Description**: Project author retrieved from the `settings.json` file.

**Type**: `str`


### `__copyright__`

**Description**: Project copyright retrieved from the `settings.json` file.

**Type**: `str`


### `__cofee__`

**Description**: A link to donate to the developer for a cup of coffee.

**Type**: `str`


## Module Constants

### `MODE`

**Description**: The current mode of operation (e.g., 'dev', 'prod').

**Type**: `str`


## Imports

- `sys`
- `json`
- `packaging.version`
- `pathlib`
- `gs` (from `src`)
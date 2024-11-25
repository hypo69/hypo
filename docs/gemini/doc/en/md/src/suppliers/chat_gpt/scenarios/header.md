# hypotez/src/suppliers/chat_gpt/scenarios/header.py

## Overview

This module provides utility functions for setting the project root directory and loading project settings. It also retrieves project name, version, documentation, and other details from configuration files.

## Functions

### `set_project_root`

**Description**: Finds the root directory of the project. It searches upwards from the current file's directory until it finds a directory containing any of the specified marker files (pyproject.toml, requirements.txt, .git).

**Parameters**:
- `marker_files` (tuple): A tuple of filenames or directory names to identify the project root. Defaults to (`'pyproject.toml'`, `'requirements.txt'`, `.git`).

**Returns**:
- `Path`: Path to the root directory if found, otherwise the directory where the script is located.


### `set_project_root`

**Description**: Finds the root directory of the project. It searches upwards from the current file's directory until it finds a directory containing any of the specified marker files (pyproject.toml, requirements.txt, .git).

**Parameters**:
- `marker_files` (tuple, optional): Filenames or directory names to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.


**Returns**:
- `Path`: Path to the root directory if found, otherwise the directory where the script is located.

**Raises**:
- No exceptions are explicitly raised.


## Variables

### `__root__`

**Description**: Path to the project's root directory. Determined by calling `set_project_root()`.

**Type**: `Path`

### `settings`

**Description**: Dictionary containing project settings loaded from `settings.json`.

**Type**: `dict` | `None`

**Note**: `settings` may be `None` if `settings.json` is not found or if there's an error during parsing.

### `doc_str`

**Description**: String containing the project documentation loaded from `README.MD`.

**Type**: `str` | `None`

**Note**: `doc_str` may be `None` if `README.MD` is not found or if there's an error during reading.


### `__project_name__`

**Description**: Name of the project, defaults to 'hypotez'.

**Type**: `str`

**Note**:  Value is taken from `settings.json` if available, otherwise defaults to 'hypotez'.


### `__version__`

**Description**: Version of the project, default to empty string.

**Type**: `str`

**Note**: Value is taken from `settings.json` if available, otherwise defaults to empty string.


### `__doc__`

**Description**: Documentation string, default to empty string.

**Type**: `str`


**Note**: Value is taken from `README.MD` if available, otherwise defaults to empty string.



### `__details__`

**Description**: Project details, default to empty string.

**Type**: `str`

**Note**: Currently defaults to an empty string, may be populated in future.


### `__author__`

**Description**: Author of the project, defaults to empty string.

**Type**: `str`

**Note**: Value is taken from `settings.json` if available, otherwise defaults to empty string.


### `__copyright__`

**Description**: Copyright information, defaults to empty string.

**Type**: `str`

**Note**: Value is taken from `settings.json` if available, otherwise defaults to empty string.


### `__cofee__`

**Description**: A string representing a link to a donation button for supporting the developer.

**Type**: `str`

**Note**: Value is taken from `settings.json` if available, otherwise defaults to a pre-defined link.
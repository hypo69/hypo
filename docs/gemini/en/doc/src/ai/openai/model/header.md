# hypotez/src/logger/header.py

## Overview

This module, `src.logger`, defines the root path of the project. All imports are built relative to this path.  Future versions will likely store this path in a system variable.  Currently, the mode is set to 'dev'.

## Functions

### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory, searching upwards until a directory containing specified marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`) is found.

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names used to identify the project root.  Defaults to (`'pyproject.toml'`, `'requirements.txt'`, `'.git'`).

**Returns**:

- `Path`: The path to the root directory if found.  Otherwise, returns the directory where the script is located.

**Raises**:

- None


## Variables

### `__root__`

**Description**: Path to the root directory of the project.  Initialized by calling `set_project_root()`.

**Type**: `Path`


## Module Variables

### `settings`

**Description**: Dictionary containing project settings loaded from `src/settings.json`. Defaults to `None` if the file is not found or cannot be parsed.


**Type**: `dict` | `None`


### `doc_str`

**Description**: String containing documentation from `src/README.MD`. Defaults to `None` if the file is not found or cannot be parsed.

**Type**: `str` | `None`


### `__project_name__`

**Description**: Project name obtained from the `settings` dictionary or defaults to 'hypotez' if settings are unavailable.

**Type**: `str`


### `__version__`

**Description**: Project version obtained from the `settings` dictionary or defaults to an empty string if settings are unavailable.


**Type**: `str`


### `__doc__`

**Description**: Documentation string obtained from `doc_str` or an empty string if unavailable.

**Type**: `str`


### `__details__`

**Description**: A placeholder string for additional project details.  Currently empty.


**Type**: `str`


### `__author__`

**Description**: Author of the project, obtained from the `settings` dictionary or an empty string if unavailable.


**Type**: `str`


### `__copyright__`

**Description**: Copyright information, obtained from the `settings` dictionary or an empty string if unavailable.


**Type**: `str`


### `__cofee__`

**Description**: A link for supporting the developer.  Obtained from `settings` dictionary or a default URL if unavailable.


**Type**: `str`
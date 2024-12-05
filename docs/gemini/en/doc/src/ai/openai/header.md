# hypotez/src/logger/header.py

## Overview

This module defines the root path of the project. All imports are relative to this path.  Future implementations should consider moving this to a system variable.  Currently, the module uses `pyproject.toml`, `requirements.txt`, and `.git` as markers to determine the root directory.

## Functions

### `set_project_root`

**Description**: Finds the root directory of the project by searching upwards from the current file's directory. Stops at the first directory containing any of the specified marker files.

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names used to identify the project root. Defaults to (`'pyproject.toml'`, `'requirements.txt'`, `.git`).


**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.


**Raises**:

- None


### `set_project_root`

**Description**: This function is used to locate the project root directory and add it to the Python path if needed.

**Parameters**:

- `marker_files` (tuple, optional): A tuple of files or directories that indicate the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: The path to the root directory of the project.

**Raises**:

- None


## Variables

### `__root__`

**Description**: The path to the root directory of the project, determined by `set_project_root()`.

**Type**: `Path`


## Imports


- `sys`
- `json`
- `pathlib`
- `packaging.version`
- `src.gs`


## Global Variables

### `MODE`

**Description**: Stores the current mode of operation (e.g., 'dev').

**Type**: `str`


### `settings`

**Description**:  A dictionary containing project settings loaded from `settings.json`.

**Type**: `dict`


### `doc_str`

**Description**:  Contains the content of the project's README.MD file.

**Type**: `str`


### `__project_name__`

**Description**:  The project name, extracted from the `settings` dictionary or defaults to `'hypotez'`.

**Type**: `str`


### `__version__`

**Description**: The project version, extracted from the `settings` dictionary or defaults to an empty string.

**Type**: `str`


### `__doc__`

**Description**: The project documentation string, extracted from the `README.MD` file or defaults to an empty string.

**Type**: `str`


### `__details__`

**Description**:  A placeholder for project details.

**Type**: `str`


### `__author__`

**Description**: The author of the project, extracted from the `settings` dictionary or defaults to an empty string.

**Type**: `str`


### `__copyright__`

**Description**: The copyright holder of the project, extracted from the `settings` dictionary or defaults to an empty string.

**Type**: `str`


### `__cofee__`

**Description**: Information for treating the developers to coffee.

**Type**: `str`


## Exceptions

- `FileNotFoundError`: Raised if `settings.json` or `README.MD` is not found.
- `json.JSONDecodeError`: Raised if there's an issue decoding the JSON data in `settings.json`.
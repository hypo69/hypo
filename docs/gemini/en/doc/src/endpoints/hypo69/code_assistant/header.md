# src.logger

## Overview

This module defines the root path of the project. All imports are based on this path.  Future versions will likely move this functionality into a system variable.


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory. It searches upward through parent directories until it finds a directory containing any of the specified marker files. If no such directory is found, it returns the directory where the script is located.

**Parameters**:

- `marker_files` (tuple): Filenames or directory names to identify the project root.  Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.


**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.


**Raises**:

- None


### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory. It searches upward through parent directories until it finds a directory containing any of the specified marker files. If no such directory is found, it returns the directory where the script is located.


**Parameters**:

- `marker_files` (tuple, optional): Filenames or directory names to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.


**Returns**:

- `Path`: Path to the root directory if found; otherwise, the directory containing the script.


**Raises**:

- None



## Global Variables

### `__root__`

**Description**: Path to the root directory of the project, as determined by `set_project_root()`.


**Type**:

- `Path`


### `settings`

**Description**: Dictionary containing project settings loaded from `src/settings.json`.


**Type**:

- `dict` | `None`


### `doc_str`

**Description**: String containing the README.MD file content.


**Type**:

- `str` | `None`


### `__project_name__`

**Description**: Project name retrieved from the `settings` dictionary, defaulting to "hypotez".


**Type**:

- `str`


### `__version__`

**Description**: Project version retrieved from the `settings` dictionary, defaulting to an empty string.


**Type**:

- `str`


### `__doc__`

**Description**: Project documentation retrieved from `README.MD`, defaulting to an empty string.


**Type**:

- `str`


### `__details__`

**Description**: Project details.


**Type**:

- `str`


### `__author__`

**Description**: Project author retrieved from the `settings` dictionary, defaulting to an empty string.


**Type**:

- `str`


### `__copyright__`

**Description**: Project copyright retrieved from the `settings` dictionary, defaulting to an empty string.


**Type**:

- `str`


### `__cofee__`

**Description**: Link to the author's Boosty page for donations.


**Type**:

- `str`
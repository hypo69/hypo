# hypotez/src/product/product_fields/header.py

## Overview

This module provides functions for setting the project root directory and loading project settings.  It handles potential errors during file loading and provides default values for missing settings.

## Functions

### `set_project_root`

**Description**: Finds the root directory of the project.

**Parameters**:

- `marker_files` (tuple): Filenames or directory names to identify the project root (default: `('pyproject.toml', 'requirements.txt', '.git')`).

**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.

**Raises**:

- No explicit exceptions are raised.


### `set_project_root`

**Description**:  Finds the root directory of the project starting from the current file's directory. Searches upwards until a directory containing any of the specified marker files is found. If none of the marker files exist, the current directory is returned.

**Parameters**:

- `marker_files` (tuple, optional): A tuple containing file or directory names to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.


**Returns**:

- `Path`: The path to the project root directory. If no matching directory is found, returns the directory containing the current file.


**Raises**:

- No exceptions are raised.


## Variables

### `__root__`

**Description**: Path to the project root directory, determined by `set_project_root()`.


### `settings`

**Description**: Dictionary containing project settings loaded from `src/settings.json`.


### `doc_str`

**Description**: String containing the documentation loaded from `src/README.MD`.


### `__project_name__`

**Description**: Project name. Defaults to `hypotez` if `settings` is unavailable or doesn't contain the key.


### `__version__`

**Description**: Project version. Defaults to an empty string if `settings` is unavailable or doesn't contain the key.


### `__doc__`

**Description**: Project documentation. Defaults to an empty string if `doc_str` is not available.


### `__details__`

**Description**: Project details. Defaults to an empty string.


### `__author__`

**Description**: Project author. Defaults to an empty string if `settings` is unavailable or doesn't contain the key.


### `__copyright__`

**Description**: Project copyright. Defaults to an empty string if `settings` is unavailable or doesn't contain the key.


### `__cofee__`

**Description**: A link to support the developers with a cup of coffee. Defaults to a specific link if `settings` is unavailable or doesn't contain the key.
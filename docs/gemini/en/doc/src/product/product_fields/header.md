# hypotez/src/product/product_fields/header.py

## Overview

This module contains functions for setting the project root directory, loading project settings, and retrieving project metadata. It handles potential errors during file loading and provides defaults for missing values.

## Functions

### `set_project_root`

**Description**: Finds the root directory of the project by searching upwards from the current file's location.  It stops at the first directory containing any of the specified marker files.

**Parameters**:

- `marker_files` (tuple): Filenames or directory names to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.

**Raises**:
- None


### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory, searching upwards and stopping at the first directory containing any of the marker files.

**Parameters**:

- `marker_files` (tuple): Filenames or directory names to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.


## Variables

### `__root__`

**Description**: A Path object representing the project root directory, determined by the `set_project_root` function.

**Type**: `Path`


### `settings`

**Description**: A dictionary containing project settings loaded from `src/settings.json`.

**Type**: `dict` or `None`


### `doc_str`

**Description**: A string containing the content of the project's README.md file.

**Type**: `str` or `None`


### `__project_name__`

**Description**: The project name.  Defaults to 'hypotez' if `settings` is missing or `project_name` key is not found.

**Type**: `str`


### `__version__`

**Description**: The project version. Defaults to an empty string if `settings` is missing or `version` key is not found.

**Type**: `str`


### `__doc__`

**Description**: The project documentation, taken from `README.md`. Defaults to an empty string if `README.MD` is not found or cannot be read.

**Type**: `str`


### `__details__`

**Description**: An empty string; intended for further details (currently unused).

**Type**: `str`


### `__author__`

**Description**: The author of the project, taken from `settings.json`.  Defaults to an empty string if `settings` is missing or `author` key is not found.

**Type**: `str`


### `__copyright__`

**Description**: The copyright information for the project, taken from `settings.json`. Defaults to an empty string if `settings` is missing or `copyright` key is not found.

**Type**: `str`

### `__cofee__`

**Description**: A string containing a link to a coffee donation link for supporting the developer. Defaults to a provided link if not found in settings.json.

**Type**: `str`
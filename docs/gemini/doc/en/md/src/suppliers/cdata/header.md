# hypotez/src/suppliers/cdata/header.py

## Overview

This module provides functions for setting the project root directory, loading project settings, and retrieving project metadata. It also handles potential errors during file reading and JSON decoding.

## Functions

### `set_project_root`

**Description**: Finds the root directory of the project by searching upwards from the current file's directory. It stops at the first directory containing any of the specified marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`).

**Parameters**:

- `marker_files` (tuple): Filenames or directory names to identify the project root. Defaults to (`'pyproject.toml'`, `'requirements.txt'`, `.git`).

**Returns**:

- `Path`: Path to the root directory if found; otherwise, the directory where the script is located.

**Raises**:

- None


### `set_project_root`

**Description**:  Finds the root directory of the project starting from the current file's directory, searching upwards and stopping at the first directory containing any of the marker files.

**Parameters**:

- `marker_files` (tuple, optional): Filenames or directory names to identify the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').


**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.


**Raises**:
- None


## Variables

### `__root__`

**Description**: Path to the root directory of the project. Initialized by calling the `set_project_root` function.

**Type**: `Path`


### `settings`

**Description**: Project settings loaded from `src/settings.json`.  Initialized to `None`.

**Type**: `dict`


### `doc_str`

**Description**: Content of the `README.MD` file. Initialized to `None`.

**Type**: `str`



### `__project_name__`

**Description**: Project name from settings, defaults to `hypotez` if settings are missing or invalid.

**Type**: `str`

### `__version__`

**Description**: Project version from settings, defaults to empty string if settings are missing or invalid.


**Type**: `str`


### `__doc__`

**Description**: Documentation string from the README file, defaults to empty string if file not found or invalid.

**Type**: `str`


### `__details__`

**Description**: Details string; currently empty.

**Type**: `str`


### `__author__`

**Description**: Author name from settings, defaults to empty string if settings are missing or invalid.

**Type**: `str`


### `__copyright__`

**Description**: Copyright information from settings, defaults to empty string if settings are missing or invalid.

**Type**: `str`


### `__cofee__`

**Description**: Link for coffee support to the developers, defaults to a pre-set link.

**Type**: `str`
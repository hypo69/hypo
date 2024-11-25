# src.suppliers.kualastyle.header

## Overview

This module defines functions for setting the project root directory and loading project settings. It also retrieves project metadata such as name, version, documentation, author, copyright, and a coffee link.


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory, searching upwards.

**Parameters**:

- `marker_files` (tuple): Filenames or directory names to identify the project root.  Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.

**Raises**:

- No exceptions are explicitly raised.


### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory, searching upwards and stopping at the first directory containing any of the marker files.

**Parameters**:

- `marker_files` (tuple, optional): Filenames or directory names to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.


## Global Variables

### `__root__`

**Description**: Path to the root directory of the project.

**Type**: `Path`

### `settings`

**Description**: Project settings loaded from `settings.json`.

**Type**: `dict`


### `doc_str`

**Description**: Project documentation loaded from `README.MD`.

**Type**: `str`

### `__project_name__`

**Description**: Project name, retrieved from the `settings` dictionary, falling back to 'hypotez' if not found or if settings are unavailable.

**Type**: `str`

### `__version__`

**Description**: Project version, retrieved from the `settings` dictionary, falling back to an empty string if not found or if settings are unavailable.

**Type**: `str`

### `__doc__`

**Description**: Project documentation string, retrieved from `doc_str`.

**Type**: `str`

### `__details__`

**Description**: Project details (currently empty).

**Type**: `str`

### `__author__`

**Description**: Project author, retrieved from the `settings` dictionary.

**Type**: `str`

### `__copyright__`

**Description**: Project copyright, retrieved from the `settings` dictionary.

**Type**: `str`


### `__cofee__`

**Description**: Link to a coffee account, retrieved from the `settings` dictionary, defaults to a sample link if not found or if settings are unavailable.

**Type**: `str`
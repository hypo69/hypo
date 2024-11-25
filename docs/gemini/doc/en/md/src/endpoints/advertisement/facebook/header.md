# hypotez/src/endpoints/advertisement/facebook/header.py

## Overview

This module provides functions for setting the project root directory and retrieving project settings. It utilizes the `gs` module and handles potential `FileNotFoundError` and `json.JSONDecodeError` exceptions during file reading.

## Functions

### `set_project_root`

**Description**: This function finds the root directory of the project by searching upwards from the current file's directory until it encounters a directory containing specified marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`).

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: The path to the root directory of the project if found, otherwise the directory where the script is located.

**Raises**:

- No exceptions are explicitly documented to be raised by this function.


### `set_project_root`

**Description**: This function finds the root directory of the project by searching upwards from the current file's directory until it encounters a directory containing specified marker files.

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names to identify the project root. Defaults to a tuple of common project marker files.

**Returns**:

- `Path`: The path to the root directory of the project if found, otherwise the directory of the current script.


## Variables

### `__root__`

**Description**: Stores the path to the project root directory. Initialized by the `set_project_root` function.


### `settings`

**Description**: A dictionary containing project settings. Loaded from `src/settings.json`.


### `doc_str`

**Description**: A string containing the project documentation, loaded from `src/README.MD`.


### `__project_name__`

**Description**: The project name, retrieved from the `settings` dictionary. Defaults to `'hypotez'`.


### `__version__`

**Description**: The project version, retrieved from the `settings` dictionary. Defaults to an empty string.


### `__doc__`

**Description**: The project documentation string, retrieved from `doc_str`. Defaults to an empty string.


### `__details__`

**Description**: A string containing project details. Defaults to an empty string.


### `__author__`

**Description**: The project author, retrieved from the `settings` dictionary. Defaults to an empty string.


### `__copyright__`

**Description**: The project copyright, retrieved from the `settings` dictionary. Defaults to an empty string.


### `__cofee__`

**Description**: A string containing a link for supporting the developer by providing a cup of coffee. Defaults to a specific link.


## Module Attributes

### `MODE`

**Description**: A string representing the development mode.  Currently set to `'dev'`.
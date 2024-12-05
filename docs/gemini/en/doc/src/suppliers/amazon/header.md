# hypotez/src/suppliers/amazon/header.py

## Overview

This module provides functionalities for retrieving and managing project settings, version information, and documentation from designated files. It utilizes the `gs` module for path manipulation and handles potential errors during file loading.

## Functions

### `set_project_root`

**Description**: This function identifies the root directory of the project by searching up the directory tree from the current file's location. It checks for specific marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`) to determine the project root.

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names used as markers to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: The path to the root directory of the project. Returns the directory of the current file if no suitable root directory is found.

**Raises**:

- No exceptions are explicitly raised in the documented code.


### `(global) __root__`

**Description**: Global variable holding the path to the project's root directory. It is initialized by calling the `set_project_root` function.

**Type**:

`Path`


## Variables

### `settings`

**Description**: A dictionary containing project settings loaded from `src/settings.json`.

**Type**:

`dict`


### `doc_str`

**Description**: String containing the content of the `README.MD` file in the project root.

**Type**:

`str`

### `__project_name__`

**Description**: String representing the project name, obtained from `settings.json` (defaulting to `hypotez` if not found).

**Type**:

`str`

### `__version__`

**Description**: String representing the project version, obtained from `settings.json` (defaulting to empty string if not found).

**Type**:

`str`

### `__doc__`

**Description**: String containing the project documentation content, obtained from `README.MD` (defaulting to empty string if not found).

**Type**:

`str`

### `__details__`

**Description**: String representing project details (currently empty).

**Type**:

`str`

### `__author__`

**Description**: String representing the project author, obtained from `settings.json` (defaulting to empty string if not found).

**Type**:

`str`


### `__copyright__`

**Description**: String representing the project copyright, obtained from `settings.json` (defaulting to empty string if not found).

**Type**:

`str`


### `__cofee__`

**Description**: String representing a link for supporting the developer with a coffee. Obtained from `settings.json` (defaulting to a specified link if not found).

**Type**:

`str`
# hypotez/src/webdriver/edge/header.py

## Overview

This module provides functions for initializing and configuring the project. It primarily focuses on finding the project root directory and loading settings from a JSON file.


## Functions

### `set_project_root`

**Description**: This function locates the project root directory by traversing up the directory tree from the current file's location. It checks for specific marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`) to identify the project root. If found, it adds the root directory to the Python path.

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names used to identify the project root directory. Defaults to a tuple containing `'pyproject.toml'`, `'requirements.txt'`, and `.git`.

**Returns**:

- `Path`: The path to the project root directory.  If the root directory isn't found, it returns the directory where the script is located.

**Raises**:

- No exceptions are explicitly raised.


### `set_project_root`

**Description**: This function locates the project root directory by traversing up the directory tree from the current file's location. It checks for specific marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`) to identify the project root. If found, it adds the root directory to the Python path.

**Parameters**:

- `marker_files` (tuple, optional): A tuple of filenames or directory names used to identify the project root directory. Defaults to a tuple containing `'pyproject.toml'`, `'requirements.txt'`, and `.git`.

**Returns**:

- `Path`: The path to the root directory if found, otherwise the directory where the script is located.

**Raises**:

- No exceptions are explicitly raised.


## Global Variables

### `__root__`

**Description**: A `Path` object representing the root directory of the project, obtained by calling `set_project_root()`.

**Type**: `Path`

### `settings`

**Description**: A dictionary containing project settings loaded from `src/settings.json`.

**Type**: `dict` or `None`

### `doc_str`

**Description**: A string containing the content of the `README.MD` file.

**Type**: `str` or `None`


### `__project_name__`

**Description**: The name of the project, obtained from the `settings.json` file or defaults to `'hypotez'`.

**Type**: `str`


### `__version__`

**Description**: The version of the project, obtained from the `settings.json` file or defaults to an empty string.

**Type**: `str`


### `__doc__`

**Description**: The documentation string for the project, obtained from the `README.MD` file or defaults to an empty string.

**Type**: `str`


### `__details__`

**Description**: Project details, obtained from the `settings.json` file or defaults to an empty string.

**Type**: `str`

### `__author__`

**Description**: The author of the project, obtained from the `settings.json` file or defaults to an empty string.

**Type**: `str`


### `__copyright__`

**Description**: The copyright information for the project, obtained from the `settings.json` file or defaults to an empty string.

**Type**: `str`

### `__cofee__`

**Description**: A string containing the link to donate a cup of coffee to the developer.

**Type**: `str`
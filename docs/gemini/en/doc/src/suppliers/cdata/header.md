# hypotez/src/suppliers/cdata/header.py

## Overview

This module contains code for handling project initialization and retrieval of settings and documentation. It defines a function to locate the project root directory and loads settings from a JSON file.


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project.  Starts from the current file's directory, searches upwards, and stops at the first directory containing any of the specified marker files.

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.

**Raises**:

- None


### `set_project_root`

**Description**: Finds the root directory of the project.  Starts from the current file's directory, searches upwards, and stops at the first directory containing any of the specified marker files.

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.

**Raises**:

- None


## Variables

### `__root__`

**Description**: A Path object containing the root directory of the project.  Initialized using the `set_project_root` function.


### `settings`

**Description**: A dictionary containing project settings.  Loaded from `src/settings.json`.  Can be None if the file is not found or invalid JSON.


### `doc_str`

**Description**: A string containing the project documentation. Loaded from `src/README.MD`. Can be None if the file is not found or is an invalid format.


### `__project_name__`

**Description**: The project name, retrieved from the `settings` dictionary or defaults to "hypotez".


### `__version__`

**Description**: The project version, retrieved from the `settings` dictionary or defaults to an empty string.


### `__doc__`

**Description**: The project documentation, retrieved from the `doc_str` variable.  Defaults to an empty string if `doc_str` is None.


### `__details__`

**Description**: A string containing project details (currently empty).


### `__author__`

**Description**: The author of the project, retrieved from the `settings` dictionary or defaults to an empty string.


### `__copyright__`

**Description**: The copyright information, retrieved from the `settings` dictionary or defaults to an empty string.


### `__cofee__`

**Description**:  A string containing a link to a coffee support for the project, retrieved from the settings dictionary, or a default link if not present.
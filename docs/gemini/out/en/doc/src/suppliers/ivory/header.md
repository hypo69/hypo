# hypotez/src/suppliers/ivory/header.py

## Overview

This module provides functions for setting the project root directory and loading project settings from a JSON file.  It also handles potential errors during file loading and provides fallback values for missing settings.


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory, searching upwards until a directory containing specified marker files is found.

**Parameters**:

- `marker_files` (tuple): Filenames or directory names to identify the project root. Defaults to a tuple containing 'pyproject.toml', 'requirements.txt', and '.git'.


**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.


**Raises**:

- None


### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory, searching upwards until a directory containing specified marker files is found.

**Parameters**:

- `marker_files` (tuple, optional): Filenames or directory names to identify the project root. Defaults to a tuple containing 'pyproject.toml', 'requirements.txt', and '.git'.


**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.


**Raises**:

- None
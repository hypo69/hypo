# hypotez/src/webdriver/header.py

## Overview

This module defines functions for setting the project root directory and loading settings from a JSON file. It also handles potential errors during file loading and uses the `gs` module for accessing the project's root directory.


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory. It searches upwards through parent directories until a directory containing any of the specified marker files is found. If none are found, it returns the directory where the script is located.

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.


**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.


**Raises**:

- `FileNotFoundError`: Raised if a file specified in `marker_files` is not found in any of the parent directories.


### `set_project_root`

**Description**: This function sets the project root by locating the directory that contains the files specified in marker_files from the current file location upwards.


**Parameters**:

- `marker_files`: A tuple of file/folder names to be used for locating the root folder.


**Returns**:

- `Path`: The root folder Path, or the current folder Path if no suitable root is found.


**Raises**:


None.
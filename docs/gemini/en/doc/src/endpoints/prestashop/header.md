# hypotez/src/logger/header.py

## Overview

This module defines the root path of the project. All imports are built relative to this path.

## Functions

### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory, searching upwards and stopping at the first directory containing any of the marker files.

**Parameters**:

- `marker_files` (tuple): Filenames or directory names to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.

**Raises**:

- `FileNotFoundError`: If any of the specified marker files are not found in the search path.


### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory, searching upwards and stopping at the first directory containing any of the marker files.

**Parameters**:

- `marker_files` (tuple, optional): Filenames or directory names to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.

**Raises**:

- `FileNotFoundError`: If any of the specified marker files are not found in the search path.

## Variables

### `__root__`

**Description**: Stores the path to the project root.

**Type**: `Path`


## Module Constants

### `MODE`

**Description**: Stores the current mode of the project.

**Type**: `str`


## Notes

- The code imports necessary modules and defines a function to determine the project root, which is essential for relative imports and module searching within a project structure.


- The use of `Path` objects (from `pathlib`) enhances the code's robustness and portability.


- Error handling (using `try...except` blocks) is implemented to manage potential `FileNotFoundError` and `json.JSONDecodeError` exceptions gracefully during the file reading process for settings and README.

- The code uses `settings.json` to store project metadata, reducing the need to hardcode information within the module.

- Comments explain the purpose of each section and variable, improving code readability.
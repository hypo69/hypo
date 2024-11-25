# hypotez/src/logger/header.py

## Overview

This module defines the root path of the project. All imports are constructed relative to this path.  Future implementations should consider using system variables for the root path.


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project, starting from the current file's directory, by searching up the directory tree until a directory containing any of the specified marker files is found.

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names to identify the project root.  Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: The path to the root directory if found.  Otherwise, returns the directory where the script is located.

**Raises**:

- No exceptions explicitly documented.


## Global Variables

### `__root__`

**Description**: A `Path` object representing the root directory of the project, determined by the `set_project_root` function.

**Type**: `Path`

### `settings`

**Description**: A dictionary containing project settings loaded from `src/settings.json`.

**Type**: `dict` | `None`

### `doc_str`

**Description**: The content of the README.MD file.

**Type**: `str` | `None`

### `__project_name__`

**Description**: The project name, taken from the settings or defaults to "hypotez".

**Type**: `str`

### `__version__`

**Description**: The project version, taken from the settings or defaults to an empty string.

**Type**: `str`

### `__doc__`

**Description**: The project documentation, taken from README.MD or defaults to an empty string.

**Type**: `str`

### `__details__`

**Description**: Project details, defaults to an empty string.

**Type**: `str`

### `__author__`

**Description**: Author of the project, taken from the settings or defaults to an empty string.

**Type**: `str`

### `__copyright__`

**Description**: Copyright information, taken from the settings or defaults to an empty string.

**Type**: `str`

### `__cofee__`

**Description**: A string containing a link to boost the developer.

**Type**: `str`


## Table of Contents

[Overview](#overview)
[Functions](#functions)
[Global Variables](#global-variables)
# hypotez/src/goog/header.py

## Overview

This module provides functions for setting the project root directory and loading project settings.  It leverages the `gs` module and handles potential exceptions during file loading.

## Table of Contents

- [set_project_root](#set-project-root)
- [Project Settings](#project-settings)

## Functions

### `set_project_root`

**Description**: Finds the root directory of the project by searching upward from the current file's directory for marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`).

**Parameters**:
- `marker_files` (tuple): Filenames or directory names used to locate the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:
- `Path`: The path to the project root directory.  If no marker file is found, returns the directory containing the current file.


**Raises**:
- None


### Project Settings

**Description**: Loads settings from `src/settings.json` and project documentation from `src/README.MD`.  Handles potential `FileNotFoundError` and `json.JSONDecodeError` exceptions during file loading.


**Parameters**:
- None

**Returns**:
- None


**Raises**:
- `FileNotFoundError`: If `src/settings.json` or `src/README.MD` is not found.
- `json.JSONDecodeError`: If the JSON data in `src/settings.json` is invalid.


## Variables

### `__root__`

**Description**: The path to the project root directory, set by the `set_project_root` function.

**Type**: `Path`

**Default**: Result of `set_project_root()`

### `settings`

**Description**: A dictionary containing project settings loaded from `src/settings.json`.

**Type**: `dict`

**Default**: `None`


### `doc_str`

**Description**: String containing project documentation loaded from `src/README.MD`.

**Type**: `str`

**Default**: `None`


### `__project_name__`

**Description**: Project name.  Derived from the `settings` dictionary, defaults to `'hypotez'`.

**Type**: `str`

**Default**:  `'hypotez'`


### `__version__`

**Description**: Project version. Derived from the `settings` dictionary, defaults to an empty string.

**Type**: `str`

**Default**: Empty String

### `__doc__`

**Description**: Project documentation. Derived from the `doc_str` variable, defaults to an empty string.

**Type**: `str`

**Default**: Empty String

### `__details__`

**Description**: Project details. Defaults to an empty string.

**Type**: `str`

**Default**: Empty String

### `__author__`

**Description**: Project author. Derived from the `settings` dictionary, defaults to an empty string.

**Type**: `str`

**Default**: Empty String

### `__copyright__`

**Description**: Project copyright. Derived from the `settings` dictionary, defaults to an empty string.

**Type**: `str`

**Default**: Empty String

### `__cofee__`

**Description**: A string containing a link to support the developer via coffee.  Derived from the `settings` dictionary, with a default value if `settings` are unavailable.

**Type**: `str`

**Default**: "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
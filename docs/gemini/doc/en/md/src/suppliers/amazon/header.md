# hypotez/src/suppliers/amazon/header.py

## Overview

This module provides utility functions for setting the project root directory and loading project settings. It leverages the `gs` module and handles potential errors during file loading.  It defines several variables holding project information, such as name, version, documentation, details, author, copyright, and a coffee link.

## Table of Contents

- [set_project_root](#set-project-root)
- [Project Settings](#project-settings)


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project by searching upwards from the current file's directory. It stops at the first directory containing specified marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`).

**Parameters**:

- `marker_files` (tuple): Filenames or directory names used to identify the project root. Defaults to a tuple containing `'pyproject.toml'`, `'requirements.txt'`, and `.git`.


**Returns**:

- `Path`: The path to the root directory of the project, or the directory containing the script if no matching directory is found. It also inserts the root directory into `sys.path`.


**Raises**:

- None


### Project Settings

**Description**: This section describes how project settings are loaded and handled.

**Details**: The script attempts to load project settings from a `settings.json` file located in the `src` directory relative to the project root.  The `json` library is used for loading. If the file is not found or cannot be parsed, a default value of `None` for the `settings` variable is used.


## Global Variables

### `__root__`

**Description**: Path to the root directory of the project.  Initialized by the `set_project_root` function.

**Type**: `Path`

### `__project_name__`

**Description**: Name of the project. Defaults to `'hypotez'`.

**Type**: `str`


### `__version__`

**Description**: Version of the project. Defaults to an empty string.

**Type**: `str`


### `__doc__`

**Description**: Project documentation, or an empty string.


**Type**: `str`


### `__details__`

**Description**: Project details, defaults to an empty string.


**Type**: `str`


### `__author__`

**Description**: Project author. Defaults to an empty string.


**Type**: `str`


### `__copyright__`

**Description**: Project copyright. Defaults to an empty string.

**Type**: `str`


### `__cofee__`

**Description**: A link to a coffee option for the developer. Defaults to a specific link.

**Type**: `str`
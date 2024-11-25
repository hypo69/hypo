# hypotez/src/logger/header.py

## Overview

This module, `src.logger`, defines the root path to the project.  All imports are structured relative to this path.  Future development will involve moving this functionality into a system variable.


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory. It searches upwards through parent directories until a directory containing any of the specified marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`) is found.  If no such directory is found, it returns the directory where the script is located.

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names to identify the project root.  Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.


### `set_project_root`


**Raises**:

- No exceptions are explicitly documented for this function.


## Global Variables

### `__root__`

**Description**: Path to the root directory of the project. Set by the `set_project_root` function.


### `settings`

**Description**: A dictionary containing project settings, loaded from `src/settings.json`.  If the file is not found or contains invalid JSON, `settings` is set to `None`.

### `doc_str`

**Description**: Content of the README.md file, if found.  If the file is not found or contains invalid data, `doc_str` is set to `None`.


### `__project_name__`

**Description**: Project name, retrieved from `settings.json`. Defaults to 'hypotez' if not found.


### `__version__`

**Description**: Project version, retrieved from `settings.json`. Defaults to an empty string if not found.


### `__doc__`

**Description**: Project documentation, retrieved from `README.MD`. Defaults to an empty string if not found.


### `__details__`

**Description**: Project details. Currently empty.


### `__author__`

**Description**: Author of the project, retrieved from `settings.json`. Defaults to an empty string if not found.


### `__copyright__`

**Description**: Copyright information, retrieved from `settings.json`. Defaults to an empty string if not found.


### `__cofee__`

**Description**: A string containing a link to a donation platform.  Retrieved from `settings.json`. Defaults to a specific link if not found.


## Table of Contents

[Overview](#overview)
[Functions](#functions)
[Global Variables](#global-variables)
[Table of Contents](#table-of-contents)
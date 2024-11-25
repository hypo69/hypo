# hypotez/src/goog/drive/header.py

## Overview

This module provides functions for interacting with Google Drive.  It primarily focuses on establishing the project root directory and loading settings from a JSON file.

## Table of Contents

* [set_project_root](#set_project_root)
* [Global Variables](#global-variables)


## Functions

### `set_project_root`

**Description**: This function determines the root directory of the project. It starts from the current file's directory and recursively searches upward for directories containing specified marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`). If found, the function adds the root directory to Python's `sys.path` and returns the path. Otherwise, it returns the current directory.

**Parameters**:

* `marker_files` (tuple): A tuple of filenames or directory names that indicate the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.


**Returns**:

* `Path`: The path to the project root directory. If the root directory cannot be determined, it returns the directory of the script.


**Raises**:

* None


### Global Variables

**Description**: This section documents the global variables and their purpose.

**Variables**:

* `__root__` (Path): Path to the root directory of the project.  This is set by calling `set_project_root()`.
* `settings` (dict):  Dictionary containing project settings, loaded from `src/settings.json`.  Defaults to `None` if the file is not found or invalid JSON.
* `doc_str` (str): Content from the `README.MD` file in the project root.  Defaults to `None` if the file is not found or invalid.
* `__project_name__` (str): The name of the project, taken from the `settings` dictionary. Defaults to `hypotez` if `settings` is not available or the key is missing.
* `__version__` (str): The version of the project. Defaults to an empty string if not found in `settings`.
* `__doc__` (str): The documentation string from `README.MD`. Defaults to an empty string if not found.
* `__details__` (str): An empty string (currently has no use).
* `__author__` (str): The author of the project, taken from the `settings` dictionary. Defaults to an empty string if not available.
* `__copyright__` (str): The copyright information of the project, taken from the `settings` dictionary. Defaults to an empty string if not available.
* `__cofee__` (str): The link to a donation page for the developer, taken from the `settings` dictionary. Defaults to a default link if not available or the key is missing.


**Note**: The `try...except` blocks handle potential `FileNotFoundError` and `json.JSONDecodeError` exceptions gracefully.
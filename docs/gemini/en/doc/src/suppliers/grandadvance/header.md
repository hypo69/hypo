# hypotez/src/suppliers/grandadvance/header.py

## Overview

This module, `header.py`, provides utility functions for setting the project root directory and loading project settings. It leverages the `gs` module and `pathlib` for file system interactions and `json` for handling settings data.  The module also handles potential errors like `FileNotFoundError` and `json.JSONDecodeError` during file reading, preventing the application from crashing.  Crucially, it initializes important variables like `__root__`, `__project_name__`, `__version__`, and more with settings from a `settings.json` file or defaults if the file doesn't exist or is invalid.

## Table of Contents

* [set_project_root](#set_project_root)
* [Variables](#variables)


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project by searching upwards from the current file's directory until a directory containing specified marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`) is found. If no such directory is found, it returns the directory where the script is located.

**Parameters**:
- `marker_files` (tuple): A tuple of filenames or directory names to identify the project root.  Defaults to (`'pyproject.toml'`, `'requirements.txt'`, `'.git'`).

**Returns**:
- `Path`: The path to the root directory if found, or the directory where the script is located.  If no root directory is found it returns the current directory.


**Raises**:
- None


### Variables

**Description**:  Initializes several important variables for the project, primarily based on data from `settings.json` file.  Provides default values if the file is not found or invalid JSON.


**Variables**:
- `__root__`: `Path`: The path to the root directory of the project. Initialized by calling `set_project_root()`.
- `settings`: `dict`:  A dictionary holding project settings, parsed from `settings.json`.  Defaults to `None` if `settings.json` is not found or not valid.
- `doc_str`: `str`: The contents of the `README.MD` file, used for project documentation. Defaults to `None` if not found.
- `__project_name__`: `str`: The name of the project. Defaults to 'hypotez' if not found in settings.
- `__version__`: `str`: The version of the project. Defaults to an empty string if not found in settings.
- `__doc__`: `str`: The project documentation string, defaults to an empty string if not found.
- `__details__`: `str`: A string to store details of the project. Defaults to an empty string.
- `__author__`: `str`: The author of the project. Defaults to an empty string if not found in settings.
- `__copyright__`: `str`: Copyright information for the project. Defaults to an empty string if not found in settings.
- `__cofee__`: `str`: A string providing a link to support the developer via coffee. Defaults to a URL if not found in settings.


**Raises**:
- `FileNotFoundError`: Raised if `settings.json` or `README.MD` is not found.
- `json.JSONDecodeError`: Raised if `settings.json` is not valid JSON.
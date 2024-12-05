# hypotez/src/endpoints/advertisement/header.py

## Overview

This module defines functions for retrieving project settings and version information.  It primarily focuses on locating the project root directory and loading settings from a JSON file.  It also handles potential errors during file reading and loading.

## Table of Contents

* [set_project_root](#set-project-root)
* [Project Settings](#project-settings)


## Functions

### `set_project_root`

**Description**: This function determines the root directory of the project by traversing upwards from the current file's directory and searching for specific marker files (e.g., `pyproject.toml`, `requirements.txt`). If found, it adds the root directory to `sys.path`.

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names used to locate the project root directory. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: The absolute path to the project root directory. Returns the current directory if the project root cannot be determined.

**Raises**:

- None


### Project Settings

**Description**: This section describes the functionality related to loading and accessing project settings.

**Variables**:

- `__root__` (Path): The absolute path to the project's root directory, obtained from calling `set_project_root()`.
- `settings` (dict): A dictionary containing project settings loaded from `settings.json`.  Defaults to `None` if the file does not exist or contains invalid JSON.
- `doc_str` (str): The content of the README.md file, if found, otherwise `None`.
- `__project_name__` (str): The project name, obtained from `settings`. Defaults to 'hypotez' if not found.
- `__version__` (str): The project version, obtained from `settings`. Defaults to '' if not found.
- `__doc__` (str): The contents of the README.MD file, or an empty string if not found.
- `__details__` (str): An empty string.
- `__author__` (str): The author of the project, obtained from `settings`. Defaults to '' if not found.
- `__copyright__` (str): The copyright information, obtained from `settings`. Defaults to '' if not found.
- `__cofee__` (str): A string containing the link for supporting the developers. Defaults to the specified link if settings are not found, or empty if not found.

**Loading Process**:

The code attempts to load settings from `gs.path.root / 'src' / 'settings.json'`.  If successful, it populates the `settings` variable. Similarly, it attempts to load the `README.MD` file and populate `doc_str`. If any of the operations fail, appropriate error handling is used. The values of the loaded variables are then assigned to the corresponding constants, using `get()` to handle potential `KeyError` if a specific key is not present.

**Exceptions**:

- `FileNotFoundError`: Raised if `settings.json` or `README.MD` is not found.
- `json.JSONDecodeError`: Raised if the content of `settings.json` is not valid JSON.
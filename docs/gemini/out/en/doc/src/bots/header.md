# hypotez/src/bots/header.py

## Overview

This module provides functions for setting the project root directory and loading project settings. It leverages the `gs` module for path manipulation and handles potential errors during file loading. The module defines constants for the current mode (`MODE`) and critical project metadata like `__root__`, `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, and `__cofee__`, populating these from `settings.json` and `README.MD` files.

## Table of Contents

- [set_project_root](#set-project-root)
- [Project Settings](#project-settings)


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project by searching upwards from the current file's location for files or directories specified in `marker_files`.

**Parameters**:

- `marker_files` (tuple): Filenames or directory names to identify the project root. Defaults to (`'pyproject.toml'`, `'requirements.txt'`, `.git`).

**Returns**:

- `Path`: Path to the root directory if found; otherwise, the directory where the script is located.


**Raises**:
- No exceptions are explicitly raised.


### Project Settings

**Description**: Loads project settings from `settings.json` and project documentation from `README.MD`.

**Functionality**:
- Attempts to load settings from `settings.json`.
- Attempts to load documentation from `README.MD`.
- If either file is not found or cannot be parsed, relevant variables are set to default values.

**Variables:**
- `settings`: Dictionary containing project settings.
- `doc_str`: String containing project documentation from `README.MD`.

**Raises**:

- `FileNotFoundError`: If `settings.json` or `README.MD` are not found.
- `json.JSONDecodeError`: If the content of `settings.json` cannot be parsed as JSON.

**Metadata Loading**:
- `__project_name__`: Project name from `settings`. Defaults to `'hypotez'`.
- `__version__`: Version string from `settings`. Defaults to `''`.
- `__doc__`: Documentation string from `README.MD`. Defaults to `''`.
- `__details__`: Details string (currently empty).
- `__author__`: Author string from `settings`. Defaults to `''`.
- `__copyright__`: Copyright string from `settings`. Defaults to `''`.
- `__cofee__`: Coffee link string from `settings`. Defaults to a provided link.
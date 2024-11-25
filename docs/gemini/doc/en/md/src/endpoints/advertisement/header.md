# hypotez/src/endpoints/advertisement/header.py

## Overview

This module contains the necessary functions for initializing the project environment and retrieving project settings. It aims to locate the project root directory, load settings from a JSON file, and potentially read documentation from a README file. The module utilizes the `gs` module for file path manipulation.


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project by searching up from the current file's directory until it finds a directory containing specified marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`).

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names to identify the project root. Defaults to (`'pyproject.toml'`, `'requirements.txt'`, `'.git'`).

**Returns**:

- `Path`: The path to the project root directory. Returns the directory where the script is located if no marker files are found.

**Raises**:

- None


### `load_settings`

**Description**: Loads project settings from a JSON file named `settings.json` located in the project's `src` directory.

**Parameters**:

- None

**Returns**:

- `dict | None`: A dictionary containing project settings if the file is found and valid, otherwise `None`.

**Raises**:

- `FileNotFoundError`: If the `settings.json` file does not exist.
- `json.JSONDecodeError`: If the `settings.json` file is not a valid JSON file.


### `load_documentation`

**Description**: Loads project documentation from a markdown file named `README.MD` located in the project's `src` directory.

**Parameters**:

- None

**Returns**:

- `str | None`: A string containing the project documentation if the file is found and valid, otherwise `None`.

**Raises**:

- `FileNotFoundError`: If the `README.MD` file does not exist.
- `json.JSONDecodeError`: If the `README.MD` file is not a valid markdown file.


## Global Variables

### `__root__`

**Description**: A `Path` object representing the root directory of the project. Set using the `set_project_root` function.

**Type**: `Path`

**Scope**: Global

### `settings`

**Description**: A dictionary containing project settings, loaded from `settings.json`. Initialized to `None`.

**Type**: `dict | None`

**Scope**: Global

### `doc_str`

**Description**: A string containing project documentation, loaded from `README.MD`. Initialized to `None`.

**Type**: `str | None`

**Scope**: Global

### `__project_name__`

**Description**: The project name, retrieved from the `settings.json` file. Defaults to `'hypotez'` if not found or if `settings` is `None`.

**Type**: `str`

**Scope**: Global

### `__version__`

**Description**: The project version, retrieved from the `settings.json` file. Defaults to an empty string if not found or if `settings` is `None`.

**Type**: `str`

**Scope**: Global

### `__doc__`

**Description**: The project documentation, retrieved from the `README.MD` file. Defaults to an empty string if not found.

**Type**: `str`

**Scope**: Global

### `__details__`

**Description**: An empty string; used to store project details.

**Type**: `str`

**Scope**: Global

### `__author__`

**Description**: The author of the project, retrieved from the `settings.json` file. Defaults to an empty string if not found or if `settings` is `None`.

**Type**: `str`

**Scope**: Global

### `__copyright__`

**Description**: The copyright information of the project, retrieved from the `settings.json` file. Defaults to an empty string if not found or if `settings` is `None`.

**Type**: `str`

**Scope**: Global

### `__cofee__`

**Description**: A string containing a link for supporting the project developers. Retrieved from the `settings.json` file. Defaults to a predefined link if not found or if `settings` is `None`.

**Type**: `str`

**Scope**: Global
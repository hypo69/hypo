# hypotez/src/fast_api/header.py

## Overview

This module defines functions and variables to handle project initialization, including finding the project root directory and loading settings. It utilizes the `gs` module for path management and handles potential errors during file loading.

## Table of Contents

- [set_project_root](#set-project-root)
- [Variables](#variables)


## Functions

### `set_project_root`

**Description**: This function finds the root directory of the project. It starts from the current file's directory and searches up the directory tree until it encounters a directory containing any of the specified marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`).

**Parameters**:

- `marker_files` (tuple): A tuple containing filenames or directory names used to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: The path to the project root directory if found; otherwise, it returns the directory containing the script. It also adds the root directory to the Python path if it's not already present.

**Raises**:

- None


## Variables

### `__root__`

**Description**: A variable representing the path to the project root directory.

**Type**: Path


### `settings`

**Description**: A dictionary containing project settings loaded from `src/settings.json`.  Defaults to `None` if the file is not found or cannot be parsed.

**Type**: dict


### `doc_str`

**Description**: A string containing the documentation of the project, loaded from `README.MD`.  Defaults to `None` if the file is not found or cannot be parsed.

**Type**: str


### `__project_name__`

**Description**: The name of the project.  Defaults to 'hypotez' if the setting is not found or invalid.

**Type**: str


### `__version__`

**Description**: The version of the project. Defaults to an empty string if the setting is not found or invalid.

**Type**: str


### `__doc__`

**Description**: The project's documentation.  Defaults to an empty string if not found or invalid.

**Type**: str


### `__details__`

**Description**: Placeholder for project details. Defaults to an empty string.

**Type**: str


### `__author__`

**Description**: The author of the project. Defaults to an empty string if the setting is not found or invalid.

**Type**: str


### `__copyright__`

**Description**: The copyright information for the project. Defaults to an empty string if the setting is not found or invalid.

**Type**: str


### `__cofee__`

**Description**: A link to donate to the project developer. Defaults to a specified URL if the setting is not found or invalid.

**Type**: str
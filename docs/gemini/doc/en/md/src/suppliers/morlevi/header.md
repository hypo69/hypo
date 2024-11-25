# hypotez/src/suppliers/morlevi/header.py

## Overview

This module defines functions for setting the project root directory and retrieving project settings. It also handles potential errors when loading project settings and documentation from JSON and markdown files respectively.

## Functions

### `set_project_root`

**Description**: Finds the root directory of the project. It searches up the directory tree from the current file's location until it finds a directory containing the specified marker files (`pyproject.toml`, `requirements.txt`, `.git`).

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: The path to the root directory if found, otherwise the directory where the script is located.

**Raises**:

- None


### `settings_data`

**Description**: Retrieves project settings from a JSON file.

**Parameters**:

- None

**Returns**:

- `dict | None`: A dictionary containing project settings if the file exists and is valid JSON, otherwise `None`.

**Raises**:

- `FileNotFoundError`: Raised if the `settings.json` file is not found.
- `json.JSONDecodeError`: Raised if the `settings.json` file is not valid JSON.


### `doc_string_data`

**Description**: Retrieves project documentation from a markdown file.

**Parameters**:

- None

**Returns**:

- `str | None`: A string containing project documentation if the file exists, otherwise `None`.

**Raises**:

- `FileNotFoundError`: Raised if the `README.MD` file is not found.
- `json.JSONDecodeError`: Raised if the `README.MD` file format is invalid.


## Variables

### `__root__`

**Description**: Holds the path to the project's root directory.  Initialized by `set_project_root()`.


### `__project_name__`

**Description**: The name of the project. Default to "hypotez".


### `__version__`

**Description**: The version of the project. Default to empty string.


### `__doc__`

**Description**: The project documentation string. Default to empty string.


### `__details__`

**Description**:  Details about the project. Default to empty string.


### `__author__`

**Description**: The author of the project. Default to empty string.


### `__copyright__`

**Description**: The copyright information for the project. Default to empty string.


### `__cofee__`

**Description**:  A string containing a link to a coffee boost for the developer. Default to a predefined URL.
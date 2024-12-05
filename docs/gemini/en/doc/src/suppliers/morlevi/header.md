# hypotez/src/suppliers/morlevi/header.py

## Overview

This module provides functions for initializing project settings and retrieving project metadata. It defines a function to locate the project root directory and loads settings from a JSON file.


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory. It searches upwards for directories containing specific marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`).

**Parameters**:

- `marker_files` (tuple): Filenames or directory names to identify the project root. Defaults to a tuple containing `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.

**Raises**:
- None


### `load_settings`

**Description**: This function is not explicitly defined in the provided code, but its functionality is implied by the `settings` variable's usage. It attempts to load settings from a JSON file located at `gs.path.root / 'src' / 'settings.json'.`

**Returns**:
- `dict | None`: Returns a dictionary containing the project settings if loaded successfully, or `None` otherwise.

**Raises**:
- `FileNotFoundError`: If the settings file (`settings.json`) is not found.
- `json.JSONDecodeError`: If the file exists but cannot be parsed as valid JSON.


### `get_project_metadata`

**Description**: This function is not explicitly defined in the provided code, but its functionality is implied by the variable assignments. It reads project metadata, including project name, version, documentation, details, author, copyright, and a coffee-boosting link.

**Parameters**:
- None

**Returns**:
- `dict`: Returns a dictionary containing the project's metadata.

**Raises**:
- `FileNotFoundError`: If the README.MD file is not found.
- `json.JSONDecodeError`: If the settings file cannot be parsed.


## Variables

### `__root__`

**Description**: Holds the path to the root directory of the project, retrieved by calling `set_project_root()`.

**Type**: `Path`

### `settings`

**Description**: Stores project settings loaded from `settings.json`.  May be `None` if loading fails.


### `doc_str`

**Description**: Stores the content of the README.MD file, if found, otherwise `None`.

**Type**: `str`

### `__project_name__`

**Description**: The name of the project. Obtained from the `settings` dictionary if available; otherwise defaults to "hypotez".

**Type**: `str`

### `__version__`

**Description**: The version of the project. Obtained from the `settings` dictionary if available; otherwise defaults to an empty string.

**Type**: `str`

### `__doc__`

**Description**: The project documentation. Obtained from the `doc_str` if available; otherwise defaults to an empty string.

**Type**: `str`

### `__details__`

**Description**: Project details. Defaults to an empty string.

**Type**: `str`

### `__author__`

**Description**: Author of the project. Retrieved from the `settings` dictionary if available, otherwise defaults to an empty string.

**Type**: `str`

### `__copyright__`

**Description**: Copyright information for the project. Retrieved from the `settings` dictionary if available; otherwise defaults to an empty string.

**Type**: `str`


### `__cofee__`

**Description**:  A link to a platform to show appreciation for the developer by purchasing them a coffee.  If `settings` is available, the value from the dictionary is used; otherwise, a default link is used.

**Type**: `str`
# src.suppliers.aliexpress.campaign.header

## Overview

This module provides functions for setting the project root directory and loading project settings.  It handles potential errors during file reading and JSON parsing.


## Functions

### `set_project_root`

**Description**: This function locates the root directory of the project by searching upwards from the current file's directory until it finds a directory containing specific marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`).

**Parameters**:
- `marker_files` (tuple): A tuple containing filenames or directory names used to identify the project root. Defaults to (`'pyproject.toml'`, `'requirements.txt'`, `.git`).

**Returns**:
- `Path`: The path to the root directory if found; otherwise, the path to the directory where the script is located.


**Raises**:
-  No exceptions are explicitly raised, but the function might implicitly raise `FileNotFoundError` if a required marker file is not found in any of the checked directories.


### `set_project_root`

**Description**:  This function attempts to find and load project settings from `src/settings.json` and project documentation from `src/README.MD`.

**Parameters**: None

**Returns**:
- None.

**Raises**:
- `FileNotFoundError`: If `src/settings.json` or `src/README.MD` does not exist.
- `json.JSONDecodeError`: If `src/settings.json` cannot be parsed as valid JSON.


## Constants

### `MODE`

**Description**:  A string variable holding the project mode (e.g., 'dev', 'prod'). Currently set to 'dev'.


## Variables

### `__root__`

**Description**: Path object representing the root directory of the project, obtained by calling `set_project_root()`.


### `settings`

**Description**: A dictionary containing project settings loaded from `src/settings.json`.  Can be `None` if the file is not found or cannot be parsed.


### `doc_str`

**Description**: A string containing project documentation loaded from `src/README.MD`.  Can be `None` if the file is not found.


### `__project_name__`

**Description**: A string holding the project name. Defaults to "hypotez" if settings are unavailable.


### `__version__`

**Description**: A string holding the project version. Defaults to an empty string if settings are unavailable.


### `__doc__`

**Description**: A string containing project documentation. Defaults to an empty string if the documentation file cannot be loaded or parsed.


### `__details__`

**Description**: A string containing project details. Defaults to an empty string.


### `__author__`

**Description**: A string holding the project author. Defaults to an empty string if settings are unavailable.


### `__copyright__`

**Description**: A string containing the project copyright. Defaults to an empty string if settings are unavailable.


### `__cofee__`

**Description**: A string containing the developer's coffee link. Defaults to a standard link if settings are unavailable.
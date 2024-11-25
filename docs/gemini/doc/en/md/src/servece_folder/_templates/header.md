# src.<module>

## Overview

This module determines the root path of the project.  All imports are based on this path.  Future versions will potentially move this to a system variable.


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project by traversing upwards from the current file's directory, looking for marker files (pyproject.toml, requirements.txt, .git).  If the root directory is not already in the Python path, it's added.

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names used to identify the project root.  Defaults to (`'pyproject.toml'`, `'requirements.txt'`, `'.git'`).


**Returns**:

- `Path`: The Path to the root directory. If no marker file is found, it returns the directory of the current script.


**Raises**:

- None


## Variables

### `__root__`

**Description**: Path to the root directory of the project.


**Type**: `Path`



### `settings`

**Description**: Dictionary containing project settings loaded from settings.json.


**Type**: `dict` | `None`


### `doc_str`

**Description**: String containing the README.MD content.


**Type**: `str` | `None`


### `__project_name__`

**Description**: Project name. Defaults to 'hypotez' if settings.json doesn't exist or is invalid.


**Type**: `str`


### `__version__`

**Description**: Project version. Defaults to an empty string if settings.json doesn't exist or is invalid.


**Type**: `str`


### `__doc__`

**Description**: Project documentation. Defaults to an empty string if README.MD doesn't exist or is invalid.


**Type**: `str`


### `__details__`

**Description**:  Project details.


**Type**: `str`



### `__author__`

**Description**: Project author. Defaults to an empty string if settings.json doesn't exist or is invalid.


**Type**: `str`



### `__copyright__`

**Description**: Project copyright. Defaults to an empty string if settings.json doesn't exist or is invalid.


**Type**: `str`


### `__cofee__`

**Description**:  A link for coffee support. Defaults to a specified link if settings.json doesn't exist or is invalid.


**Type**: `str`


## Error Handling

**Description**: The code includes `try...except` blocks to handle potential errors:


- `FileNotFoundError`: if `settings.json` or `README.MD` is not found.
- `json.JSONDecodeError`: if the JSON data in `settings.json` is invalid.
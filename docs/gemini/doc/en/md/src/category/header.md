# hypotez/src/category/header.py

## Overview

This module defines the root path to the project. All imports are built relative to this path.  Future versions will likely move this functionality into a system-wide variable for better management.

## Table of Contents

- [set_project_root](#set-project-root)
- [Module Variables](#module-variables)


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project, starting from the current file's directory. It searches up the directory tree and stops at the first directory containing any of the specified marker files.

**Parameters**:

- `marker_files` (tuple): Filenames or directory names to identify the project root. Defaults to (`'pyproject.toml'`, `'requirements.txt'`, `.git`).


**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.


## Module Variables

### `__root__`

**Description**: Path to the root directory of the project. Determined by `set_project_root`.

### `settings`

**Description**: A dictionary containing project settings loaded from `settings.json` located in the `src` directory.  Loads an empty dictionary if the file is missing or invalid.

### `doc_str`

**Description**: String containing the documentation from `README.MD` found in the `src` directory.

### `__project_name__`

**Description**: Project name, retrieved from `settings.json`. Defaults to `hypotez` if the key is not found or if `settings` is not defined.

### `__version__`

**Description**: Project version, retrieved from `settings.json`. Defaults to an empty string if not found.

### `__doc__`

**Description**: Project documentation, retrieved from `README.MD` if found.

### `__details__`

**Description**:  Project details (currently an empty string).

### `__author__`

**Description**: Author's name, retrieved from `settings.json`. Defaults to an empty string if not found.


### `__copyright__`

**Description**: Project copyright, retrieved from `settings.json`. Defaults to an empty string if not found.


### `__cofee__`

**Description**: A string containing a link for supporting the developer through donations. Defaults to a standard link if `settings` does not exist or the relevant key isn't found.


**Example Usage** (Illustrative, not executable within this documentation):

```python
project_root = set_project_root()
print(project_root)
print(__project_name__)
```


**Raises**:

- `FileNotFoundError`: If `settings.json` or `README.MD` is not found.
- `json.JSONDecodeError`: If the JSON data in `settings.json` cannot be decoded correctly.
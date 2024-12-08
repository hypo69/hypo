# hypotez/src/suppliers/hb/header.py

## Overview

This module defines functions for setting the project root directory and retrieving project settings and documentation. It leverages the `gs` module for path manipulation and `json` for loading settings.

## Functions

### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory, searching upwards and stopping at the first directory containing any of the marker files.

**Parameters**:

- `marker_files` (tuple): Filenames or directory names to identify the project root.  Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.


**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.

**Raises**:

- None


### `set_project_root` (Example Usage)

```python
root_path = set_project_root()
print(root_path)
```

### `settings`

**Description**: Contains project settings loaded from `src/settings.json`

**Returns**

- dict | None: Dictionary containing project settings if found, otherwise `None`

**Raises**:

- `FileNotFoundError`: Raised if the `settings.json` file does not exist.
- `json.JSONDecodeError`: Raised if the `settings.json` file is not valid JSON.

### `doc_str`

**Description**: Contains project documentation loaded from `src/README.MD`

**Returns**

- str | None: String containing project documentation if found, otherwise `None`

**Raises**:

- `FileNotFoundError`: Raised if the `README.MD` file does not exist.
- `json.JSONDecodeError`: Raised if the `README.MD` file is not valid Markdown.


## Constants

### `__root__`

**Description**:  Path to the root directory of the project. Initialized by the `set_project_root` function.

**Type**: Path

### `__project_name__`

**Description**: Project name retrieved from settings or defaults to 'hypotez' if unavailable.

**Type**: str

### `__version__`

**Description**: Project version retrieved from settings or defaults to '' if unavailable.

**Type**: str

### `__doc__`

**Description**: Project documentation string retrieved from settings or defaults to '' if unavailable.

**Type**: str

### `__details__`

**Description**: Project details (currently empty).

**Type**: str

### `__author__`

**Description**: Project author retrieved from settings or defaults to '' if unavailable.

**Type**: str

### `__copyright__`

**Description**: Project copyright retrieved from settings or defaults to '' if unavailable.

**Type**: str

### `__cofee__`

**Description**: Project coffee link retrieved from settings or defaults to a specific link if unavailable.

**Type**: str
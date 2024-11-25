# hypotez/src/logger/header.py

## Overview

This module, `hypotez/src/logger/header.py`, defines the root path of the project.  All imports are constructed relative to this path.  Future versions may store this path in a system-level variable.  Currently, the mode is set to 'dev'.

## Functions

### `set_project_root`

**Description**: This function recursively searches up the directory tree from the current file's location to find the project root directory. It searches for specific marker files (`pyproject.toml`, `requirements.txt`, `.git`) to identify the project.

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names to use as markers for the project root. Defaults to (`'pyproject.toml'`, `'requirements.txt'`, `.git`).

**Returns**:

- `Path`: The path to the root directory of the project. If no marker file is found, returns the directory where the script is located.

**Example Usage**:
```python
root_path = set_project_root()
print(root_path)
```

**Raises**:

- No exceptions are explicitly raised.


### `set_project_root`

**Description**: This function recursively searches up the directory tree from the current file's location to find the project root directory. It searches for specific marker files (`pyproject.toml`, `requirements.txt`, `.git`) to identify the project.

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names to use as markers for the project root. Defaults to (`'pyproject.toml'`, `'requirements.txt'`, `.git`).

**Returns**:

- `Path`: The path to the root directory of the project. If no marker file is found, returns the directory where the script is located.

**Example Usage**:
```python
root_path = set_project_root()
print(root_path)
```

**Raises**:

- No exceptions are explicitly raised.


## Global Variables

### `__root__`

**Description**: This variable holds the path to the root directory of the project, determined by the `set_project_root()` function.


### `settings`

**Description**: This variable contains project settings loaded from `src/settings.json`.

**Type**: dict


### `doc_str`

**Description**: This variable stores the contents of the project's README.md file.

**Type**: str


### `__project_name__`

**Description**:  The name of the project, retrieved from `settings.json` or defaulting to `hypotez` if no settings are found.

**Type**: str

### `__version__`

**Description**:  The version of the project, retrieved from `settings.json` or defaulting to an empty string if no settings are found.

**Type**: str

### `__doc__`

**Description**: Project documentation (README.MD).

**Type**: str


### `__details__`

**Description**: Project details.

**Type**: str


### `__author__`

**Description**: Project author.

**Type**: str


### `__copyright__`

**Description**: Project copyright.

**Type**: str


### `__cofee__`

**Description**:  A string containing a link to a coffee tip for the developer.


**Type**: str
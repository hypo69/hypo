# hypotez/src/product/header.py

## Overview

This module defines the root path of the project.  All imports are built relative to this path.  Future implementations will likely move this functionality to a system-wide variable.

## Table of Contents

* [set_project_root](#set_project_root)
* [Module Variables](#module-variables)

## Functions

### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory, searching upwards and stopping at the first directory containing any of the marker files.

**Parameters**:

- `marker_files` (tuple): Filenames or directory names to identify the project root.  Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.


**Raises**:
- No exceptions explicitly raised.


### Module Variables

**Description**: This section documents the module-level variables.

* `__root__` (Path): Path to the root directory of the project. This is determined by the `set_project_root` function.

## Module Usage Example

```python
from hypotez.src.product.header import set_project_root

project_root = set_project_root()
print(project_root) 
```


## Global Variables

**Description**:  This section defines the variables that are used in the rest of the project.


* `MODE` (str):  Stores the current development mode (e.g., 'dev', 'prod').

* `__project_name__` (str): The name of the project, defaults to 'hypotez'.

* `__version__` (str): The version of the project, defaults to empty string.

* `__doc__` (str): The project documentation, defaults to empty string.

* `__details__` (str): Extra project details, defaults to empty string.

* `__author__` (str): The author of the project, defaults to empty string.

* `__copyright__` (str): The copyright information, defaults to empty string.

* `__cofee__` (str): A link for supporting the project, defaults to a specific URL.


* `settings` (dict): Project settings loaded from `settings.json` if found, otherwise `None`.

* `doc_str` (str): Project documentation loaded from `README.MD` if found, otherwise `None`.

**Note:**  The module imports `gs.path.root` from the `src` package. This is implicitly assumed to be defined somewhere else, likely in a separate module. Also note the `try...except` blocks around file reading operations.  These are critical for robust error handling.
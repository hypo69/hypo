# hypotez/src/gui/header.py

## Overview

This module defines the root path to the project. All imports are built relative to this path.  In the future, this functionality will be moved to system variables.

## Functions

### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory, searching upwards and stopping at the first directory containing any of the marker files.

**Parameters**:

- `marker_files` (tuple): Filenames or directory names to identify the project root.  Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.

**Raises**:

- None


### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory, searching upwards and stopping at the first directory containing any of the marker files.

**Parameters**:

- `marker_files` (tuple, optional): Filenames or directory names to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.


**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.


**Raises**:
- None


## Variables


### `__root__`

**Description**: Path to the root directory of the project.


**Type**: `Path`


## Usage Example

```python
from hypotez.src.gui.header import set_project_root

root_path = set_project_root()
print(root_path)
```

## Constants

### `MODE`

**Description**: Indicates the development mode of the application. Currently set to 'dev'.

**Type**: `str`


## Imports


```python
import sys
import json
from packaging.version import Version

from pathlib import Path
```


```python
from src import gs
```


## Global Variables

### `settings`

**Description**: Stores project settings loaded from `settings.json`.


**Type**: `dict`


### `doc_str`

**Description**: Stores the content of the `README.MD` file.


**Type**: `str`


### `__project_name__`

**Description**: Name of the project, derived from the `settings.json`. Defaults to `hypotez`.

**Type**: `str`

### `__version__`

**Description**: Version of the project, derived from the `settings.json`. Defaults to an empty string.

**Type**: `str`


### `__doc__`

**Description**: Documentation string from README.MD, defaults to empty string if file not found.

**Type**: `str`


### `__details__`

**Description**:  Detailed description string.  Defaults to empty string.

**Type**: `str`

### `__author__`

**Description**: Author of the project, derived from the `settings.json`. Defaults to an empty string.

**Type**: `str`

### `__copyright__`

**Description**: Copyright information, derived from the `settings.json`. Defaults to an empty string.

**Type**: `str`

### `__cofee__`

**Description**: Link to contribute to the developer, defaults to a sample URL if not found in the `settings.json`.

**Type**: `str`


## Error Handling

The code includes `try...except` blocks to handle potential errors when reading `settings.json` and `README.MD`.  Exceptions such as `FileNotFoundError` and `json.JSONDecodeError` are caught.  The `...` placeholder in the `except` blocks indicates that no specific action is taken when an exception occurs.


```
```
```
```
```
# hypotez/src/product/header.py

## Overview

This module defines the root path of the project. All imports are built relative to this path.  Future implementations should consider using system environment variables for this purpose.

## Functions

### `set_project_root`

**Description**: Finds the root directory of the project, starting from the current file's directory and searching upwards. It stops at the first directory containing any of the specified marker files.

**Parameters**:

- `marker_files` (tuple): Filenames or directory names used to identify the project root. Defaults to a tuple containing 'pyproject.toml', 'requirements.txt', and '.git'.


**Returns**:

- `Path`: The path to the root directory if found, otherwise the directory where the script is located.


**Raises**:

- No exceptions are explicitly documented to be raised.


### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory, searching upwards and stopping at the first directory containing any of the marker files.


**Parameters**:

- `marker_files` (tuple, optional): Filenames or directory names to identify the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').


**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.


**Raises**:

- No exceptions are explicitly documented to be raised.


## Variables

### `__root__`

**Description**:  Represents the root path of the project after calling `set_project_root()`.


**Type**: `Path`



## Imports

- `sys`
- `json`
- `packaging.version`
- `pathlib`
- `src.gs`


## Global Variables

### `MODE`

**Description**: This global variable likely stores a string representing the current development mode (e.g., 'dev', 'prod'). Its documentation lacks a descriptive value.


**Type**: `str`


### `settings`

**Description**: A global variable to hold settings loaded from the 'settings.json' file.


**Type**: `dict | None`


### `doc_str`

**Description**: Stores the content of the README.MD file (if exists).


**Type**: `str | None`


### `__project_name__`

**Description**: The name of the project, obtained from the `settings.json` file or defaults to 'hypotez' if the file isn't found or if "project_name" is missing.


**Type**: `str`



### `__version__`

**Description**: The version of the project, obtained from the `settings.json` file or defaults to '' if the file isn't found or if "version" is missing.


**Type**: `str`



### `__doc__`

**Description**: The documentation string for the project, loaded from the README.MD file or defaults to '' if the file isn't found.


**Type**: `str`



### `__details__`

**Description**:  A global variable likely containing project details. Its documentation lacks a descriptive value.


**Type**: `str`



### `__author__`

**Description**: The author of the project, obtained from the `settings.json` file or defaults to '' if the file isn't found or if "author" is missing.


**Type**: `str`



### `__copyright__`

**Description**: The copyright information for the project, obtained from the `settings.json` file or defaults to '' if the file isn't found or if "copyright" is missing.


**Type**: `str`



### `__cofee__`

**Description**: A global variable likely containing a link to donate a coffee to the project. Its documentation describes it as a link for supporting development.


**Type**: `str`
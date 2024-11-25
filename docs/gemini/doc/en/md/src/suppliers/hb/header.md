# hypotez/src/suppliers/hb/header.py

## Overview

This module, `header.py`, defines the function `set_project_root` to find the root directory of the project.  It also initializes global variables for project name, version, documentation, author, copyright, and a coffee link. It reads settings from `src/settings.json` and project documentation from `src/README.MD`, handling potential `FileNotFoundError` and `json.JSONDecodeError` exceptions gracefully.


## Table of Contents

* [set_project_root](#set_project_root)


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory.  Searches upwards, stopping at the first directory containing specified marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`). Adds the root directory to `sys.path` if it's not already there.

**Parameters**:

- `marker_files` (tuple): Filenames or directory names to identify the project root.  Defaults to a tuple containing `'pyproject.toml'`, `'requirements.txt'`, and `.git`.

**Returns**:

- `Path`: Path to the root directory if found. Otherwise, returns the directory where the script is located.


**Raises**:

- None


## Global Variables

### `__root__`

**Description**: Path to the root directory of the project. Initialized by the `set_project_root` function.


### `settings`

**Description**: Project settings, loaded from `src/settings.json`. Initialized as `None`, then loaded from file, handling potential exceptions.


### `doc_str`

**Description**: Project documentation string, loaded from `src/README.MD`. Initialized as `None`, then loaded from file, handling potential exceptions.


### `__project_name__`

**Description**: Name of the project. Retrieved from `settings.json` or defaults to 'hypotez'.


### `__version__`

**Description**: Version of the project. Retrieved from `settings.json` or defaults to an empty string.


### `__doc__`

**Description**: Project documentation. Retrieved from `README.MD` or defaults to an empty string.


### `__details__`

**Description**: Project details. Defaults to an empty string.


### `__author__`

**Description**: Author of the project. Retrieved from `settings.json` or defaults to an empty string.


### `__copyright__`

**Description**: Copyright information for the project. Retrieved from `settings.json` or defaults to an empty string.


### `__cofee__`

**Description**:  A link to treat the developer to a cup of coffee. Retrieved from `settings.json` or defaults to a pre-defined link.
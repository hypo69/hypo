# hypotez/src/ai/dialogflow/header.py

## Overview

This module defines the root path of the project. All imports are relative to this path.  It also handles loading settings from `settings.json` and project documentation from `README.MD`.

## Functions

### `set_project_root`

**Description**: Finds the root directory of the project by searching upwards from the current file's directory until a directory containing any of the specified marker files is found.

**Parameters**:

- `marker_files` (tuple): Filenames or directory names to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.

**Raises**:

- No exceptions explicitly raised.


### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory, searching upwards and stopping at the first directory containing any of the marker files.

**Parameters**:

- `marker_files` (tuple, optional): Filenames or directory names to identify the project root. Defaults to a tuple containing `'pyproject.toml'`, `'requirements.txt'`, and `.git`.

**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.


## Variables

### `__root__`

**Description**: Path to the root directory of the project.


### `settings`

**Description**: Loaded settings from `settings.json`.  Returns `None` if the file is not found or if there's an error in decoding the JSON.


### `doc_str`

**Description**: Content read from the `README.MD` file. Returns `None` if the file is not found or if there is an error reading the file.


### `__project_name__`

**Description**: Project name, loaded from `settings.json`. Defaults to 'hypotez' if not found or if the file contains no "project_name" key.

### `__version__`

**Description**: Project version, loaded from `settings.json`. Defaults to an empty string if not found.


### `__doc__`

**Description**: Project documentation, loaded from `README.MD`. Defaults to an empty string if not found.


### `__details__`

**Description**: Project details. Currently an empty string.


### `__author__`

**Description**: Author of the project, loaded from `settings.json`. Defaults to an empty string if not found.


### `__copyright__`

**Description**: Copyright information, loaded from `settings.json`. Defaults to an empty string if not found.


### `__cofee__`

**Description**: Link to support the developers. Loaded from settings.json, defaults to a link if no "coffee" key is found.


## Module Attributes

- `MODE` :  Currently set to 'dev'.


## Imports

- `sys`
- `json`
- `pathlib`
- `packaging.version`
- `src.gs`
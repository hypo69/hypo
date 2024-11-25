# hypotez/src/logger/header.py

## Overview

This module, `src.logger`, defines the root path of the project.  All imports are relative to this path.  Future implementations should consider storing this path in a system variable.


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project by searching upwards from the current file's directory until a directory containing one of the specified marker files is found.

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names to identify the project root.  Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: The path to the root directory if found, otherwise the directory containing the script.

**Raises**:

- No exceptions are explicitly raised.


### `set_project_root`

**Description**: (This section is repeated - likely a copy/paste error in the input) Finds the root directory of the project by searching upwards from the current file's directory until a directory containing one of the specified marker files is found.

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names to identify the project root.  Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: The path to the root directory if found, otherwise the directory containing the script.

**Raises**:

- No exceptions are explicitly raised.

## Variables

### `__root__`

**Description**:  Path to the root directory of the project, as determined by `set_project_root()`.


### `settings`

**Description**:  A dictionary containing project settings, loaded from `src/settings.json`. If the file does not exist or is not valid JSON, `settings` will be `None`.


### `doc_str`

**Description**: String containing the content of the `README.MD` file, or `None` if the file does not exist or cannot be read.



### `__project_name__`

**Description**:  The project name, taken from `settings.json` if available, otherwise defaults to 'hypotez'.


### `__version__`

**Description**:  The project version, taken from `settings.json` if available, otherwise an empty string.


### `__doc__`

**Description**:  The documentation string, taken from `README.MD` if available, otherwise an empty string.


### `__details__`

**Description**:  An empty string.


### `__author__`

**Description**:  The author, taken from `settings.json` if available, otherwise an empty string.


### `__copyright__`

**Description**:  Copyright information, taken from `settings.json` if available, otherwise an empty string.


### `__cofee__`

**Description**: A string containing a link for supporting the developer via coffee donation. Taken from `settings.json` if available, otherwise defaults to a provided link.


## Module Attributes

### `MODE`

**Description**: A string representing the current development mode, set to 'dev'.
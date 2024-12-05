# hypotez/src/logger/header.py

## Overview

This module defines the root path of the project. All imports are built relative to this path.  It also loads settings from `src/settings.json` and documentation from `src/README.MD`, if they exist.

## Functions

### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory, searching upwards and stopping at the first directory containing any of the marker files.

**Parameters**:

- `marker_files` (tuple): Filenames or directory names to identify the project root.  Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.

**Raises**:

- None


## Variables

### `__root__`

**Description**: Path to the root directory of the project, calculated by `set_project_root()`.

### `settings`

**Description**: Dictionary containing project settings, loaded from `src/settings.json`.  Defaults to `None` if the file does not exist or cannot be parsed.

### `doc_str`

**Description**: String containing project documentation, loaded from `src/README.MD`. Defaults to `None` if the file does not exist or cannot be parsed.

### `__project_name__`

**Description**: Project name, obtained from the `settings` dictionary. Defaults to 'hypotez' if settings are unavailable or `project_name` key is missing.

### `__version__`

**Description**: Project version, obtained from the `settings` dictionary. Defaults to an empty string if settings are unavailable or `version` key is missing.


### `__doc__`

**Description**: Project documentation, obtained from `doc_str`. Defaults to an empty string if `doc_str` is `None`.


### `__details__`

**Description**: Project details, currently an empty string.


### `__author__`

**Description**: Project author, obtained from the `settings` dictionary. Defaults to an empty string if settings are unavailable or `author` key is missing.


### `__copyright__`

**Description**: Project copyright, obtained from the `settings` dictionary. Defaults to an empty string if settings are unavailable or `copyright` key is missing.


### `__cofee__`

**Description**: A link to a donation page, obtained from the `settings` dictionary. Defaults to a predefined link if settings are unavailable or `cofee` key is missing.


## Module Attributes

- `MODE`: String defining the current mode (e.g., 'dev').
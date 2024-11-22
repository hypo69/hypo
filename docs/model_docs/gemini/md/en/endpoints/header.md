```markdown
# hypotez/src/endpoints/header.py

## Overview

This module defines the root path of the project. All imports are built relative to this path.  It also handles loading settings and project documentation from `settings.json` and `README.MD` respectively.  It populates the project metadata (name, version, etc.) from the `settings.json` file.

## Table of Contents

- [Functions](#functions)
- [Global Variables](#global-variables)


## Functions

### `get_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory, searching upwards and stopping at the first directory containing any of the marker files.

**Parameters**:
- `marker_files` (tuple): Filenames or directory names to identify the project root.  Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:
- `Path`: Path to the root directory if found, otherwise the directory where the script is located.


## Global Variables

### `__root__`

**Description**: Path to the root directory of the project.  Initialized by the `get_project_root` function.

### `settings`

**Description**: A dictionary containing project settings loaded from `settings.json`.  Initialized from settings.json but is `None` if the file is not found or can't be parsed.

### `doc_str`

**Description**: String containing project documentation loaded from `README.MD`.  Initialized from README.MD but is `None` if the file is not found or can't be parsed.


### `__project_name__`

**Description**: Project name, loaded from settings. Defaults to `hypotez`.


### `__version__`

**Description**: Project version, loaded from settings. Defaults to empty string.


### `__doc__`

**Description**: Project documentation string. Defaults to an empty string.


### `__details__`

**Description**: Project details. Defaults to an empty string.


### `__author__`

**Description**: Project author, loaded from settings. Defaults to an empty string.


### `__copyright__`

**Description**: Project copyright, loaded from settings. Defaults to an empty string.


### `__cofee__`

**Description**: A string containing a link to the developer's coffee donation page. Loaded from settings. Defaults to a link to a specific coffee donation page.


### `MODE`

**Description**: A string variable specifying the development mode. Currently set to 'development'.


### `__file__`

**Description**: The filename of the current Python file


### `__name__`

**Description**: The name of the current module.

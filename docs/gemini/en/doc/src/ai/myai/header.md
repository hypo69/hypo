# hypotez/src/ai/myai/header.py

## Overview

This module, `hypotez/src/ai/myai/header.py`, provides utility functions for project initialization and retrieval of project-related metadata like the project root, name, version, and documentation. It aims to streamline project setup and access to essential information.


## Functions

### `set_project_root`

**Description**: This function locates the root directory of the project by searching upward from the current file's directory. It looks for specific marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`) to pinpoint the project's root.

**Parameters**:

- `marker_files` (tuple): A tuple of file or directory names used to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: The path to the root directory of the project, or the current directory if the root can't be determined.

**Raises**:
- None


### `get_project_settings`

**Description**: This function attempts to read project settings from a `settings.json` file located in the project's root directory.


**Returns**:

- `dict`: The project settings as a dictionary if found and parsed successfully, otherwise `None`.

**Raises**:
- `FileNotFoundError`: If the `settings.json` file does not exist.
- `json.JSONDecodeError`: If the `settings.json` file exists but is not valid JSON.


### `get_project_documentation`

**Description**: This function attempts to read project documentation from a `README.MD` file located in the project's root directory.

**Returns**:

- `str`: The project documentation as a string if found and read successfully.  Otherwise, returns an empty string.

**Raises**:
- `FileNotFoundError`: If the `README.MD` file does not exist.
- `json.JSONDecodeError`: If the `README.MD` file exists but cannot be read.


## Variables

### `__root__`

**Description**:  A path object representing the root directory of the project, set by the `set_project_root()` function.


### `__project_name__`

**Description**: The name of the project, retrieved from the `settings.json` file if it exists, otherwise defaults to 'hypotez'.

### `__version__`

**Description**: The version of the project, retrieved from the `settings.json` file if it exists. Otherwise, defaults to an empty string.

### `__doc__`

**Description**: The project documentation, retrieved from the `README.MD` file if it exists, otherwise defaults to an empty string.

### `__details__`

**Description**:  A variable storing detailed information. Currently set to an empty string.

### `__author__`

**Description**: The author of the project, retrieved from the `settings.json` file if it exists.  Otherwise, defaults to an empty string.

### `__copyright__`

**Description**: The copyright information of the project, retrieved from the `settings.json` file if it exists.  Otherwise, defaults to an empty string.

### `__cofee__`

**Description**: A string containing a message for supporting the developer. It is retrieved from the `settings.json` file and defaults to a specific message if not found.


## Module Constants


### `MODE`

**Description**: A string representing the current mode of operation (e.g., 'dev', 'prod').


## Table of Contents

* [Overview](#overview)
* [Functions](#functions)
    * [`set_project_root`](#set_project_root)
    * [`get_project_settings`](#get_project_settings)
    * [`get_project_documentation`](#get_project_documentation)
* [Variables](#variables)
    * [`__root__`](#__root__)
    * [`__project_name__`](#__project_name__)
    * [`__version__`](#__version__)
    * [`__doc__`](#__doc__)
    * [`__details__`](#__details__)
    * [`__author__`](#__author__)
    * [`__copyright__`](#__copyright__)
    * [`__cofee__`](#__cofee__)
* [Module Constants](#module-constants)
    * [`MODE`](#mode)
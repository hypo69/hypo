# hypotez/src/bots/discord/header.py

## Overview

This module provides functions for setting the project root directory, loading settings from a JSON file, and loading documentation from a README.md file. It also defines global variables containing project information like name, version, documentation, details, author, copyright, and a coffee link.

## Functions

### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory, searching upwards and stopping at the first directory containing any of the marker files specified.

**Parameters**:

- `marker_files` (tuple): Filenames or directory names to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.

**Raises**:

- None

### `set_project_root`

**Description**: This function is not implemented yet.

**Parameters**:
- None


**Returns**:
- None

**Raises**:
- None



## Global Variables

### `__root__`

**Description**: Stores the path to the root directory of the project. Initialized by calling `set_project_root()`.

**Type**: `Path`

### `settings`

**Description**: Stores the project settings loaded from `settings.json`.

**Type**: `dict` or `None`


### `doc_str`

**Description**: Stores the documentation loaded from `README.MD`.

**Type**: `str` or `None`


### `__project_name__`

**Description**: The name of the project. Retrieved from `settings.json`, defaulting to 'hypotez'.

**Type**: `str`

### `__version__`

**Description**: The version of the project. Retrieved from `settings.json`, defaulting to ''.

**Type**: `str`


### `__doc__`

**Description**: The project's documentation. Retrieved from `README.MD`, defaulting to ''.

**Type**: `str`

### `__details__`

**Description**: Additional details about the project.

**Type**: `str`

### `__author__`

**Description**: The author of the project. Retrieved from `settings.json`, defaulting to ''.

**Type**: `str`

### `__copyright__`

**Description**: The copyright information for the project. Retrieved from `settings.json`, defaulting to ''.

**Type**: `str`

### `__cofee__`

**Description**: A link for supporting the developer. Retrieved from `settings.json`, defaulting to a link.

**Type**: `str`


## Error Handling

The code includes `try...except` blocks to handle potential errors during file reading and JSON parsing. If `settings.json` or `README.MD` are not found or contain invalid data, appropriate exceptions are caught, and default values are used.


## Table of Contents

* [Overview](#overview)
* [Functions](#functions)
    * [`set_project_root`](#set_project_root)
* [Global Variables](#global-variables)
    * [`__root__`](#__root__)
    * [`settings`](#settings)
    * [`doc_str`](#doc_str)
    * [`__project_name__`](#__project_name__)
    * [`__version__`](#__version__)
    * [`__doc__`](#__doc__)
    * [`__details__`](#__details__)
    * [`__author__`](#__author__)
    * [`__copyright__`](#__copyright__)
    * [`__cofee__`](#__cofee__)
* [Error Handling](#error-handling)
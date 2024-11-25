# hypotez/src/bots/header.py

## Overview

This module defines the root path of the project. All imports are based on this path.  It attempts to locate the project root by searching for marker files (pyproject.toml, requirements.txt, .git) starting from the current file's directory and moving up the directory tree.  If the project root is not found, it uses the current directory as the root.   The module also loads settings from a settings.json file in the project root and README.md.  The settings and documentation are used to populate project-level variables.

## Functions

### `set_project_root`

**Description**: Finds the root directory of the project.

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: The path to the root directory if found, otherwise the directory of the script.

**Raises**:

- None


### `set_project_root`


**Description**: Finds the root directory of the project.

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: The path to the root directory if found, otherwise the directory of the script.

**Raises**:

- None

## Global Variables

### `__root__`

**Description**: The path to the root directory of the project.

**Type**: `Path`


### `settings`

**Description**:  A dictionary containing project settings loaded from `settings.json`.


**Type**: `dict`


### `doc_str`

**Description**: String containing the content of the README.MD file.


**Type**: `str`


### `__project_name__`

**Description**: The project name. Defaults to 'hypotez' if not found in settings.json.


**Type**: `str`

### `__version__`

**Description**: Project version. Defaults to empty string if not found in settings.json.


**Type**: `str`

### `__doc__`

**Description**: Project documentation. Defaults to empty string if not found in README.md.


**Type**: `str`

### `__details__`


**Type**: `str`


**Description**: Placeholder for more project details. Currently empty.


### `__author__`


**Type**: `str`


**Description**: Project author. Defaults to empty string if not found in settings.json.

### `__copyright__`


**Type**: `str`


**Description**: Project copyright. Defaults to empty string if not found in settings.json.

### `__cofee__`


**Type**: `str`


**Description**: Link to the author's coffee link for support


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
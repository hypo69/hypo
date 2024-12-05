# hypotez/src/webdriver/header.py

## Overview

This module contains functions for retrieving project-related information, such as the project root directory, settings, and documentation. It leverages the `src` and `gs` modules for accessing necessary resources.

## Functions

### `set_project_root`

**Description**: This function determines the root directory of the project. It starts from the current file's directory and searches upwards through parent directories until it finds a directory containing specified marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`).

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names to identify the project root. Defaults to (`'pyproject.toml'`, `'requirements.txt'`, `.git`).

**Returns**:

- `Path`: The path to the root directory of the project, or the directory containing the current file if no project root is found.  It also adds the root directory to `sys.path` if it's not already present.

**Raises**:

- No exceptions are explicitly raised.


### `settings`

**Description**: This function tries to load settings from `settings.json` in the project's `src` directory.

**Parameters**:

- N/A

**Returns**:
- `dict`: A dictionary containing project settings. Returns `None` if the file is not found or cannot be parsed as JSON.

**Raises**:
- `FileNotFoundError`: If the `settings.json` file is not found.
- `json.JSONDecodeError`: If the `settings.json` file is found but contains invalid JSON.


### `doc_str`

**Description**: This function attempts to read the README.MD file located in the `src` directory to get documentation.

**Parameters**:

- N/A

**Returns**:

- `str`: The content of the README.MD file as a string. Returns None if the file is not found or cannot be read.

**Raises**:
- `FileNotFoundError`: If the README.MD file is not found.
- `json.JSONDecodeError`: If the file is found but is in a format that isn't readable.


## Variables

### `__root__`

**Description**: Stores the path to the project root directory, obtained from the `set_project_root` function.  This variable is a `Path` object.

### `__project_name__`

**Description**: Stores the project name, obtained from the `settings.json` file. Defaults to 'hypotez' if the setting is not found or `settings` is `None`.

### `__version__`

**Description**: Stores the project version, obtained from the `settings.json` file. Defaults to an empty string if the setting is not found or `settings` is `None`.

### `__doc__`

**Description**: Stores the project documentation, obtained from the `README.MD` file. Defaults to an empty string if the file is not found or cannot be read.

### `__details__`

**Description**: Stores project details. Currently empty string.

### `__author__`

**Description**: Stores the author's name, obtained from the `settings.json` file. Defaults to an empty string if the setting is not found or `settings` is `None`.

### `__copyright__`

**Description**: Stores copyright information, obtained from the `settings.json` file. Defaults to an empty string if the setting is not found or `settings` is `None`.

### `__cofee__`

**Description**: Stores a link to a coffee support option for developers. Defaults to a predefined string if the setting is not found or `settings` is `None`.


## Table of Contents

[Overview](#overview)
[Functions](#functions)
    - [set_project_root](#set_project_root)
    - [settings](#settings)
    - [doc_str](#doc_str)
[Variables](#variables)
    - [__root__](#__root__)
    - [__project_name__](#__project_name__)
    - [__version__](#__version__)
    - [__doc__](#__doc__)
    - [__details__](#__details__)
    - [__author__](#__author__)
    - [__copyright__](#__copyright__)
    - [__cofee__](#__cofee__)
# hypotez/src/webdriver/chrome/header.py

## Overview

This module provides functions for initializing the project environment, retrieving project settings, and accessing documentation. It leverages the `gs` module and the `settings.json` and `README.MD` files within the project's root directory to configure the project's metadata and documentation.

## Table of Contents

- [set_project_root](#set-project-root)
- [Module Variables](#module-variables)


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project. It starts from the current file's directory, searches upwards, and stops at the first directory containing specified marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`). If no marker files are found, it defaults to the current directory.

**Parameters**:

- `marker_files` (tuple): Filenames or directory names to identify the project root. Defaults to a tuple containing `'pyproject.toml'`, `'requirements.txt'`, and `.git`.

**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.


### Module Variables

**Description:** This section defines the module-level variables that store metadata about the project, such as the project name, version, documentation, author, copyright, and support details. These variables are populated from the `settings.json` and `README.MD` files in the project's root directory. If the files are not found, or an error occurs during loading, the variables will default to appropriate values.

**Variables**:

- `__root__` (Path): Path to the root directory of the project. Calculated by calling the `set_project_root` function.
- `settings` (dict, optional):  Dictionary containing project settings loaded from `settings.json`. Defaults to `None`.
- `doc_str` (str, optional): String containing project documentation loaded from `README.MD`. Defaults to `None`.
- `__project_name__` (str): Name of the project. Loaded from `settings.json`, defaults to 'hypotez' if not found.
- `__version__` (str): Version of the project. Loaded from `settings.json`, defaults to an empty string if not found.
- `__doc__` (str): Project documentation. Loaded from `README.MD`, defaults to an empty string if not found.
- `__details__` (str): Additional project details. Loaded from `settings.json` and defaults to an empty string if not found.
- `__author__` (str): Author of the project. Loaded from `settings.json` and defaults to an empty string if not found.
- `__copyright__` (str): Copyright information for the project. Loaded from `settings.json` and defaults to an empty string if not found.
- `__cofee__` (str): Information regarding how to support the developers. Loaded from `settings.json` and defaults to a specific URL.


**Raises**:

- `FileNotFoundError`: Raised if `settings.json` or `README.MD` are not found.
- `json.JSONDecodeError`: Raised if the JSON data in `settings.json` is invalid.
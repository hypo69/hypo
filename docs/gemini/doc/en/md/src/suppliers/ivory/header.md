# hypotez/src/suppliers/ivory/header.py

## Overview

This module provides functions for setting the project root directory and loading project settings. It utilizes the `gs` module and attempts to load settings from a `settings.json` file within the project's `src` directory.  It also attempts to load documentation from a `README.MD` file.

## Table of Contents

* [set_project_root](#set-project-root)
* [Project Settings](#project-settings)


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory. It searches upwards in the directory tree until it finds a directory containing any of the specified marker files (`pyproject.toml`, `requirements.txt`, `.git`). If no marker file is found, it returns the current directory.


**Parameters**:

- `marker_files` (tuple): Filenames or directory names to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.


**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.


**Raises**:

- None


### Project Settings

**Description**: This section handles loading project settings from the `settings.json` file in the project's `src` directory.


**Loading Settings**: The `settings` variable is populated with the loaded settings from the `settings.json` file. If the file is not found or cannot be parsed as JSON, the variable is set to `None`


**Global Variables**: The loaded settings, if successful, are used to populate several global variables, including:
- `__project_name__`: Name of the project.
- `__version__`: Version of the project.
- `__doc__`: Project documentation.
- `__details__`: Additional details about the project.
- `__author__`: Author of the project.
- `__copyright__`: Copyright information of the project.
- `__cofee__`: Donation link to support the developer.


**Error Handling**: The code uses `try...except` blocks to handle potential `FileNotFoundError` and `json.JSONDecodeError` exceptions.
# hypotez/src/utils/_examples/header.py

## Overview

This module defines utility functions for determining the project root directory. It also handles loading settings and project documentation.

## Table of Contents

- [set_project_root](#set-project-root)
- [Project Settings](#project-settings)
- [Project Documentation](#project-documentation)


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project by searching upwards from the current file's location.

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.

**Raises**:

- `FileNotFoundError`: Raised if any of the marker files are not found in the search path.


### Project Settings

**Description**: Loads project settings from a JSON file named `settings.json` located in the project's `src` directory.

**Raises**:

- `FileNotFoundError`: Raised if the `settings.json` file is not found.
- `json.JSONDecodeError`: Raised if the `settings.json` file is not valid JSON.

### Project Documentation

**Description**: Loads project documentation from a `README.MD` file located in the project's `src` directory.

**Raises**:

- `FileNotFoundError`: Raised if the `README.MD` file is not found.
- `json.JSONDecodeError`: Raised if the `README.MD` file is not valid JSON.
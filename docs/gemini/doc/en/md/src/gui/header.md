# hypotez/src/gui/header.py

## Overview

This module defines the root path of the project and sets it as the first element in the Python path. It also loads project settings from `src/settings.json` and reads the README.md file.  This module is crucial for ensuring consistent imports across the project.

## Table of Contents

- [Functions](#functions)
    - [`set_project_root`](#set_project_root)


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project by searching upwards from the current file's location. It checks for specific marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`) to determine the project root. If the root directory is not already in the Python path, it is added.

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names used to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: The path to the root directory of the project. If no marker file is found, the directory containing the current script is returned.


**Raises**:

- None
# hypotez/src/suppliers/ebay/header.py

## Overview

This module contains functions for setting the project root directory and retrieving project settings and documentation. It leverages the `gs` module for file path management and `json` for loading settings.

## Table of Contents

- [set_project_root](#set-project-root)
- [Project Settings](#project-settings)
- [Project Documentation](#project-documentation)


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project.

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names to identify the project root.  Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: Path to the root directory. If no marker files are found, returns the directory containing the current file.

**Raises**:

- None


### Project Settings

**Description**: Retrieves project settings from a JSON file.

**Details**:
Reads settings from `src/settings.json` and populates global variables.


**Raises**:

- `FileNotFoundError`: If `src/settings.json` does not exist.
- `json.JSONDecodeError`: If the file exists but cannot be parsed as valid JSON.

### Project Documentation

**Description**: Retrieves project documentation from a markdown file.

**Details**:
Reads documentation from `src/README.MD` and populates global variable.


**Raises**:

- `FileNotFoundError`: If `src/README.MD` does not exist.
- `json.JSONDecodeError`: If the file exists but cannot be parsed.
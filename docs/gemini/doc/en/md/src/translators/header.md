# hypotez/src/translators/header.py

## Overview

This module, `header.py`, provides functions for setting the project root directory and retrieving project settings.  It handles potential errors during file access.

## Table of Contents

* [Functions](#functions)
    * [`set_project_root`](#set_project_root)

## Functions

### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory. It searches upwards until it finds a directory containing specified marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`).

**Parameters**:

- `marker_files` (tuple): Filenames or directory names to identify the project root. Defaults to a tuple of `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.


**Raises**:

-  No exceptions are explicitly raised by this function, but it relies on `Path` object operations.


### `settings_loading`
**Description:** Attempts to load project settings from `settings.json` located in the project's root directory. Handles `FileNotFoundError` and `json.JSONDecodeError` exceptions during file reading.

**Parameters:**
- None.
**Returns**:
- `dict`:  Dictionary containing project settings or `None` if the settings file was not found or could not be parsed.

**Raises**:
- `FileNotFoundError`: If the settings file (`settings.json`) does not exist.
- `json.JSONDecodeError`: If the settings file has invalid JSON format.


### `doc_loading`

**Description:** Attempts to load project documentation from `README.MD` located in the project's root directory.  Handles `FileNotFoundError` and `json.JSONDecodeError` exceptions during file reading.

**Parameters:**

- None

**Returns**:

- `str`: String containing the project documentation or `None` if the documentation file was not found or could not be parsed.

**Raises**:

- `FileNotFoundError`: If the documentation file (`README.MD`) does not exist.
- `json.JSONDecodeError`: If the documentation file does not contain valid markdown text.
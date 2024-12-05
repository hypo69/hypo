# hypotez/src/goog/spreadsheet/header.py

## Overview

This module provides functions for initializing project settings and retrieving important metadata, such as the project root directory, name, version, and documentation. It utilizes the `src.gs` module and loads settings from a `settings.json` file within the project's source directory. Error handling is implemented to gracefully manage potential file not found or JSON decoding issues.

## Table of Contents

- [set_project_root](#set_project_root)
- [Project Initialization](#project-initialization)


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project by searching up the directory tree from the current file's location until a directory containing specific marker files (like `pyproject.toml`, `requirements.txt`, or `.git`) is found. If none of the marker files are found, the current directory is returned.

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.

**Raises**:

- None


### Project Initialization

**Description**: This section describes the initialization process for project-related variables.

**Details**:

- It retrieves the project root directory using the `set_project_root` function.
- It attempts to load project settings from a `settings.json` file located in the `src` directory relative to the project root.  If the file is not found or cannot be parsed as JSON, `settings` is set to `None`.
- It loads optional project documentation from a `README.MD` file if found, otherwise `doc_str` is set to `None`.
- It then extracts project name, version, documentation, details, author, copyright, and coffee encouragement information from the `settings` dictionary, using default values when the dictionary or keys are missing or invalid.

**Example usage:**

```python
# ... (Code to use the variables)
print(f"Project name: {__project_name__}")
print(f"Version: {__version__}")
print(f"Documentation: {__doc__}")
```


```
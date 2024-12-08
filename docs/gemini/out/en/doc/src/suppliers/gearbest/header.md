# hypotez/src/suppliers/gearbest/header.py

## Overview

This module defines functions for retrieving project settings and version information. It leverages the `gs` module (likely for path manipulation) and handles potential errors during file reading.  Crucially, it sets the project root directory in `sys.path` to allow importing modules from the project's source tree.

## Table of Contents

* [set_project_root](#set_project_root)
* [Module-Level Variables](#module-level-variables)


## Functions

### `set_project_root`

**Description**: Locates the root directory of the project. It starts from the current file's directory and traverses upward until it finds a directory containing specified marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`). If the root is not found, the current directory is returned.  If not in `sys.path`, it is added to support import of modules within the project.

**Parameters**:
- `marker_files` (tuple): A tuple of filenames or directory names used to identify the project root. Defaults to a tuple of `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:
- `Path`: The path to the project root directory. If not found, it returns the path of the current file.

**Raises**:
- `None`: No exceptions are explicitly raised.


## Module-Level Variables

These variables hold project information, potentially loaded from a `settings.json` file and `README.MD` file within the project root.

### `__root__`

**Description**: Path to the project root directory obtained from `set_project_root`.

### `settings`

**Description**: Project settings loaded from `settings.json` (likely a dictionary). `None` if the file does not exist or is not valid JSON.

### `doc_str`

**Description**: String content from `README.MD` (if available).  `None` if the file does not exist or is not valid.

### `__project_name__`

**Description**: Project name, obtained from `settings`. Defaults to "hypotez" if not found.

### `__version__`

**Description**: Project version, obtained from `settings`. Defaults to an empty string if not found.

### `__doc__`

**Description**: Documentation string, obtained from `doc_str`. Defaults to an empty string if not found.

### `__details__`

**Description**: Project details. Defaults to an empty string if not found.

### `__author__`

**Description**: Project author, obtained from `settings`. Defaults to an empty string if not found.

### `__copyright__`

**Description**: Project copyright, obtained from `settings`. Defaults to an empty string if not found.

### `__cofee__`

**Description**: A link for supporting the project developers with a cup of coffee. Defaults to a specific link if not found.
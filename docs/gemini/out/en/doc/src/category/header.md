# hypotez/src/category/header.py

## Overview

This module, `src.category.header.py`, defines the root path of the project.  All imports are constructed relative to this path.  Future versions will likely store this path in a system variable for better management.

## Table of Contents

* [Overview](#overview)
* [Functions](#functions)
    * [`set_project_root`](#set_project_root)

## Functions

### `set_project_root`

**Description**: Finds the root directory of the project by traversing up from the current file's directory, searching for specified marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`).

**Parameters**:

* `marker_files` (tuple): A tuple of filenames or directory names to use as markers to identify the project root.  Defaults to a tuple containing `'pyproject.toml'`, `'requirements.txt'`, and `.git`.

**Returns**:

* `Path`: The path to the root directory if found; otherwise, the directory where the script is located.

**Raises**:

* None
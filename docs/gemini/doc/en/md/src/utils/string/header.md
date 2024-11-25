# hypotez/src/logger/header.py

## Overview

This module defines the root path of the project. All imports are built relative to this path.  It also handles loading settings from `settings.json` and potentially `README.MD` for documentation purposes.  Further improvements include storing this path in a system variable.

## Table of Contents

* [Functions](#functions)
    * [`set_project_root`](#set_project_root)

## Functions

### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory, searching upwards and stopping at the first directory containing any of the specified marker files.

**Parameters**:

* `marker_files` (tuple): Filenames or directory names to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

* `Path`: Path to the root directory if found, otherwise the directory where the script is located.

**Raises**:

* None
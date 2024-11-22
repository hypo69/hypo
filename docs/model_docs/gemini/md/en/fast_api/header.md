```markdown
# hypotez/src/fast_api/header.py

## Overview

This module defines the header for the fastAPI application. It handles project initialization, locating the project root directory, loading settings from a JSON file, and retrieving documentation.

## Table of Contents

- [Overview](#overview)
- [Functions](#functions)
  - [`get_project_root`](#get_project_root)


## Functions

### `get_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory.  Searches upwards and stops at the first directory containing any of the specified marker files (pyproject.toml, requirements.txt, .git). If no suitable root is found, the current directory is returned.

**Parameters**:
- `marker_files` (tuple): Filenames or directory names to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:
- `Path`: Path to the root directory if found, otherwise the directory where the script is located.

**Raises**:
- None


```

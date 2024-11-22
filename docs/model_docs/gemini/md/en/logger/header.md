```markdown
# hypotez/src/logger/header.py

## Overview

This module defines the root path of the project.  All imports are relative to this path.  It also handles loading settings from a JSON file and the project's README.

## Table of Contents

- [Overview](#overview)
- [Functions](#functions)
    - [`get_project_root`](#get_project_root)

## Functions

### `get_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory. It searches upwards and stops at the first directory containing any of the specified marker files.

**Parameters**:

- `marker_files` (tuple): Filenames or directory names to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.


**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.

**Example Usage**:

```python
root_path = get_project_root()
print(root_path)
```


**Raises**:
No exceptions are explicitly raised.


```
```
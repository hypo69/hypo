# hypotez/src/suppliers/ksp/header.py

## Overview

This module defines functions for setting the project root directory and loading project settings and documentation. It uses the `gs` module for path manipulation and `json` for loading settings.  It also handles potential `FileNotFoundError` and `json.JSONDecodeError` exceptions during file loading.  The module utilizes the `packaging.version` library for version handling.

## Table of Contents

* [set_project_root](#set-project-root)
* [Project Settings and Documentation](#project-settings-and-documentation)


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project by searching upward from the current file's directory.

**Parameters**:
- `marker_files` (tuple): A tuple of filenames or directory names to identify the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').

**Returns**:
- `Path`: Path to the root directory if found, otherwise the directory where the script is located.

**Raises**:
- None


### Project Settings and Documentation

**Description**:
This section handles loading project settings and documentation from `settings.json` and `README.MD`. The module sets variables `__root__`, `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__` based on loaded data. Missing or invalid files result in default values.


```python
def set_project_root(marker_files=(\'pyproject.toml\', \'requirements.txt\', \'.git\')) -> Path:
    """
    Finds the root directory of the project starting from the current file's directory,
    searching upwards and stopping at the first directory containing any of the marker files.

    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.
    
    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
    __root__:Path
    current_path:Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__
```

```python
# ... (rest of the code) ...
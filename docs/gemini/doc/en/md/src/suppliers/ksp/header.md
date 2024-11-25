# hypotez/src/suppliers/ksp/header.py

## Overview

This module provides functions for initializing and accessing project-related information, such as the project root directory, settings, and documentation. It leverages the `gs` module for path manipulation and `json` for loading settings data.

## Table of Contents

- [set_project_root](#set-project-root)
- [Project Initialization](#project-initialization)


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project by searching upwards from the current file's location.


**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.


**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.


**Raises**:

- No exceptions are explicitly raised in the function definition.


### Project Initialization

**Description**: This section describes the process of initializing project information.

**Details**:

- It defines a `__root__` variable by calling `set_project_root()` which retrieves the root directory.

- It attempts to load settings from `src/settings.json` located in the project root.
  - If the file is not found or contains invalid JSON, a `FileNotFoundError` or `json.JSONDecodeError` may be raised, but the code handles this exception gracefully.
  - `settings` variable is set to `None` if an exception occurs.
-  It attempts to load documentation from `src/README.MD`. Similar to settings, an error is handled gracefully, setting `doc_str` to `None`.
- Finally, it assigns project name, version, documentation, and other details from the loaded `settings`.
- Using `settings.get()` for values, and assigning default values if `settings` is `None` or the key is not found. This prevents potential `AttributeError` errors.
- The `__root__`, `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, and `__cofee__` variables are defined using the data obtained.


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
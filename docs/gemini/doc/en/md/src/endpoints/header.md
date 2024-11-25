# hypotez/src/endpoints/header.py

## Overview

This module defines functions for setting the project root directory and loading project settings. It utilizes the `gs` module and `pathlib` to handle file paths.  It also handles potential errors when loading settings from `settings.json` and `README.MD`.

## Table of Contents

* [Functions](#functions)
    * [`set_project_root`](#set_project_root)

## Functions

### `set_project_root`

**Description**: Finds the root directory of the project, starting from the current file's location. It searches up the directory tree until it finds a directory containing one of the specified marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`). If no such directory is found, it returns the current directory. It also adds the root directory to `sys.path` if it's not already present.

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names to search for. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: The path to the root directory of the project. If no root directory is found, it returns the directory where the current script is located.

**Raises**:

- `None`: This function does not explicitly raise any errors.


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
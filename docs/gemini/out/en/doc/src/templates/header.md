# src.templates.header

## Overview

This module provides a function `set_project_root` to determine the root directory of a project.  It searches upwards from the current file's location for directories containing specific marker files like `pyproject.toml`, `requirements.txt`, or `.git`. The function also adds the project root to `sys.path` if it's not already present.

## Functions

### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory.

**Parameters**:

- `marker_files` (tuple): Filenames or directory names used to identify the project root. Defaults to a tuple containing `'pyproject.toml'`, `'requirements.txt'`, and `.git`.

**Returns**:

- `Path`: Path to the root directory if found. Otherwise, it returns the directory where the script is located.

**Raises**:

- None


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

### `__init__`

**Description**: Initializes the project root variable.  This is not a normal function but is a result of the script executing the `set_project_root` function, storing the result as `__root__`.

**Parameters**:
- None

**Returns**:
- None


```python
# Get the root directory of the project
__root__ = set_project_root()
```

**Note:** The `__root__` variable is defined *after* calling `set_project_root`, but the documentation will still show this section because the code itself defines it.

```python
"""__root__ (Path): Path to the root directory of the project"""
```

### `import` statements


**Description**: Imports necessary libraries.


```python
import sys
import json
from packaging.version import Version
from pathlib import Path
from src import gs
```
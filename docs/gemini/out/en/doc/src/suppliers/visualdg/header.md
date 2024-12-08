# hypotez/src/suppliers/visualdg/header.py

## Overview

This module provides utilities for interacting with the `visualdg` supplier, primarily focused on project initialization and settings retrieval.  It defines a function to locate the project root directory and loads project settings from a JSON file.


## Table of Contents

* [set_project_root](#set-project-root)
* [Project Settings](#project-settings)


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project by searching up the directory tree from the current file's location. This function ensures that the project's root directory is correctly added to the Python path.

**Parameters**:

- `marker_files` (tuple, optional): A tuple of file or directory names to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: The path to the project root directory. If no marker files are found, it returns the path of the directory containing the current script.

**Raises**:

- None


### Project Settings

**Description**: This section details the loading of project settings from a JSON file.  Error handling is implemented to manage potential issues during file reading and JSON parsing.


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
import json
from pathlib import Path

# ... (other imports)

settings:dict = None
try:
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = json.load(settings_file)
except (FileNotFoundError, json.JSONDecodeError):
    ...
```
```python
# ... (Rest of the code)

```

**Note**: The rest of the code in the file is handling loading the project `README.MD` (documentation) file and setting project metadata (like name, version, author, etc) from the loaded settings.  Error handling is also included to gracefully manage missing or unreadable files.  The `gs.path.root` variable is assumed to be defined elsewhere.
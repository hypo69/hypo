# hypotez/src/webdriver/crawlee_python/header.py

## Overview

This module provides functionality for setting the project root directory and loading project settings. It utilizes the `gs` module and parses a `settings.json` file to retrieve project-specific information.

## Table of Contents

- [set_project_root](#set-project-root)
- [Project Settings](#project-settings)


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory. It searches upwards in the directory tree until it encounters a directory containing the specified marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`). If no such directory is found, it returns the directory where the script is located.


**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names used to identify the project root. Defaults to (`'pyproject.toml'`, `'requirements.txt'`, `.git`).


**Returns**:

- `Path`: The path to the root directory of the project if found; otherwise, the directory where the script is located.


**Raises**:

- `Exception`:  Any exception that might occur during path manipulation.


### Project Settings

**Description**: Loads and initializes project settings from the `settings.json` file.

**Details**:

- The module attempts to load settings from the `settings.json` file located in the project's `src` directory.
- If the file is not found or the JSON data is invalid, it handles the exception gracefully and sets the `settings` variable to `None` which causes further usage to fall back on default values.
- Project name, version, documentation, details, author, copyright, and coffee donation link are parsed from the loaded settings. If settings are not loaded successfully, defaults are used.


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
# Get the root directory of the project
__root__ = set_project_root()
"""__root__ (Path): Path to the root directory of the project"""

from src import gs

config:dict = None
try:
    with open(gs.path.root / \'src\' /  \'settings.json\', \'r\') as settings_file:
        config = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    ...

doc_str:str = None
try:
    with open(gs.path.root / \'src\' /  \'README.MD\', \'r\') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError):
    ...


__project_name__ = settings.get("project_name", \'hypotez\') if settings  else \'hypotez\'
__version__: str = settings.get("version", \'\')  if settings  else \'\'\
__doc__: str = doc_str if doc_str else \'\'\
__details__: str = \'\'\
__author__: str = settings.get("author", \'\')  if settings  else \'\'\
__copyright__: str = settings.get("copyrihgnt", \'\')  if settings  else \'\'\
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
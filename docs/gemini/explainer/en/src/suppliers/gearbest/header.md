## File hypotez/src/suppliers/gearbest/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.suppliers.gearbest
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'dev'


import sys
import json
from packaging.version import Version

from pathlib import Path
def set_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git')) -> Path:
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


# Get the root directory of the project
__root__ = set_project_root()
"""__root__ (Path): Path to the root directory of the project"""

from src import gs

settings:dict = None
try:
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = json.load(settings_file)
except (FileNotFoundError, json.JSONDecodeError):
    ...

doc_str:str = None
try:
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError):
    ...


__project_name__ = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
__version__: str = settings.get("version", '')  if settings  else ''
__doc__: str = doc_str if doc_str else ''
__details__: str = ''
__author__: str = settings.get("author", '')  if settings else ''
__copyright__: str = settings.get("copyrihgnt", '')  if settings else ''
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
```

```
<algorithm>
**Step 1: Finding Project Root**

*   **Input:** Current file path (`__file__`).
*   **Process:** The `set_project_root` function recursively traverses parent directories.
*   **Condition:** Checks if any of the specified marker files (`pyproject.toml`, `requirements.txt`, `.git`) exist in the current parent directory.
*   **Output:** Path to the project root directory (`__root__`). Example:  If the script is in `hypotez/src/suppliers/gearbest`, and `pyproject.toml` is in `hypotez`, the function returns the `hypotez` directory path.

**Step 2: Loading Settings**

*   **Input:** Project root path (`__root__`).
*   **Process:** Attempts to read the `settings.json` file from the `src` directory within the project root.
*   **Error Handling:** Catches `FileNotFoundError` and `json.JSONDecodeError` to handle cases where the file doesn't exist or is not valid JSON.
*   **Output:** Loaded JSON data (`settings`) if successful.

**Step 3: Loading Documentation**

*   **Input:** Project root path (`__root__`).
*   **Process:** Attempts to read the `README.MD` file from the `src` directory within the project root.
*   **Error Handling:** Catches `FileNotFoundError` and `json.JSONDecodeError` to handle cases where the file doesn't exist or is not valid text.
*   **Output:** Loaded content of `README.MD` file (`doc_str`).

**Step 4: Extracting Project Information**

*   **Input:** Loaded settings data (`settings`), read documentation (`doc_str`).
*   **Process:** Extracts values from the `settings.json` file based on keys (e.g., `project_name`, `version`).
*   **Default Values:** Uses default values ('hypotez' for `project_name`, empty strings for other values) if a key is missing.
*   **Output:** Project name, version, documentation, etc., stored as module-level variables.



</algorithm>
```

```
<explanation>

**Imports:**

*   `sys`: Provides access to system-specific parameters and functions, particularly for manipulating the Python path. Used to add the project root directory to the system path.
*   `json`: Used for encoding and decoding JSON data.
*   `packaging.version`: Used for comparing and working with software version numbers.
*   `pathlib`: Provides object-oriented way of working with paths.

**Classes:**

*   No classes are defined in this file.

**Functions:**

*   `set_project_root(marker_files=...)`:
    *   **Arguments:** `marker_files`: A tuple of filenames or directory names used to locate the project root directory. Default is `('pyproject.toml', 'requirements.txt', '.git')`.
    *   **Return Value:** A `Path` object representing the root directory of the project.
    *   **Purpose:** Locates the project root directory by traversing up the directory tree from the current file's location until a directory containing at least one of the specified marker files is found. This function is critical for properly configuring the Python import system. If not found, returns current directory.
    *   **Example:** If the script is in `hypotez/src/suppliers/gearbest`, the function will traverse up the directories until `hypotez` (containing `pyproject.toml`) is found.

**Variables:**

*   `MODE`: A string variable, likely used for configuration (e.g., 'dev', 'prod').
*   `__root__`: A `Path` object representing the root directory of the project. Calculated and used throughout the script.
*   `settings`: A dictionary to store the project settings loaded from `settings.json`.
*   `doc_str`: A string to store the documentation (e.g., content of `README.MD`).
*   `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`: Module-level variables holding project metadata. These are extracted from `settings` if it exists.

**Potential Errors/Improvements:**

*   Error handling is good in the `try...except` blocks.
*   The `set_project_root` function could be more robust. It might not work in a non-standard project setup. For example, what if there is no `pyproject.toml`?  Consider a fallback to `__file__` if no marker file is found to prevent crashes.
*   Consider using `Pathlib`'s `glob` for multiple `marker_files` search.
*   Add type hints where missing for clarity and maintainability. For example, in `settings: dict = None`.  Generally, adding type hints is beneficial.


**Relationships:**

*   This module relies on `gs.path.root` which implies an external `gs` module (likely from the `src` package). This module is responsible for managing paths related to the project's resources, including the project root directory.  It is critical for the `__root__` calculation and subsequent file reading.
*   The code interacts with `settings.json` and potentially `README.MD` files which are likely project configuration or documentation.
*   The `__root__` variable is crucial to properly import modules from the `src` package, establishing a chain of dependencies between modules in the `hypotez` project.
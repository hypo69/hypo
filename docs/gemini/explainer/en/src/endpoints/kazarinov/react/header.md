## File hypotez/src/endpoints/kazarinov/react/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.endpoints.kazarinov.react 
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
**Step 1: Find Project Root**

*   **Input:** Current file path (`__file__`).
*   **Process:**
    *   Resolve the current file path to an absolute path using `.resolve()`.
    *   Get the parent directory (`parent`).
    *   Iterate through parent directories (starting from the current file's directory) upwards.
    *   Check if any marker files (`pyproject.toml`, `requirements.txt`, `.git`) exist in each parent directory.
    *   If found, set `__root__` to that parent directory and break the loop.
*   **Output:** Path to the root directory (`__root__`).

**Example:**
```
Current File: /path/to/project/endpoints/kazarinov/react/header.py
__root__ = /path/to/project/
```

**Step 2: Load Settings**

*   **Input:** Project root directory (`__root__`).
*   **Process:**
    *   Construct the path to the settings file (`gs.path.root / 'src' / 'settings.json'`).
    *   Try to open the settings file and load JSON data into the `settings` variable.
    *   Handle potential `FileNotFoundError` or `json.JSONDecodeError` using `try...except`.
*   **Output:** Dictionary `settings` if successful, `None` otherwise.

**Example:**
```
__root__ = /path/to/project/
settings = {'project_name': 'MyProject', 'version': '1.0.0'}
```


**Step 3: Load Documentation**

*   **Input:** Project root directory (`__root__`).
*   **Process:**
    *   Construct the path to the README file (`gs.path.root / 'src' / 'README.MD'`).
    *   Try to open the README file and read its content into the `doc_str` variable.
    *   Handle potential `FileNotFoundError` or `json.JSONDecodeError` using `try...except`.
*   **Output:** String `doc_str` if successful, `None` otherwise.


**Step 4: Extract Project Information**

*   **Input:** `settings`, `doc_str`.
*   **Process:**
    *   Extract project name, version, author, copyright, and coffee link from the `settings` dictionary (if available).
*   **Output:** Variables: `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`.

**Example:**

```
settings = {'project_name': 'MyProject', 'version': '1.0.0'}
__project_name__ = 'MyProject'
```


```
<explanation>

**Imports:**

*   `sys`: Used for manipulating the Python path.  Important for locating other parts of the project.
*   `json`: Used for loading and parsing JSON data from the settings file.
*   `packaging.version`: Used for working with software versions. Not used in this particular function.
*   `pathlib`: Used for working with file paths in a more object-oriented way.
*   `src`: Likely a custom package in the project, probably containing utility classes and functions (gs).

**Classes:**

*   No classes are defined in this module.

**Functions:**

*   `set_project_root(marker_files=...)`: This function is crucial for finding the project root directory. It iterates through parent directories starting from the current file, searching for specific marker files (`pyproject.toml`, `requirements.txt`, `.git`). The function inserts the root path into `sys.path` to enable importing modules from subdirectories of the project.

**Variables:**

*   `MODE`: A string variable to define the execution mode, in this case, 'dev'.
*   `__root__`: A `Path` object that stores the project root directory, initialized from the returned value of `set_project_root()`.
*   `settings`: A dictionary variable that stores the project settings loaded from `settings.json`.
*   `doc_str`: A string variable that stores the content of the README file (if found).
*   `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`: These variables hold the project's metadata retrieved from the `settings` dictionary.


**Potential Errors and Improvements:**

*   Error Handling: The `try...except` blocks are good practice, but consider logging the error instead of just ignoring it if the settings file is missing or invalid.
*   `gs`: This code relies on a `gs` module (likely from `src`).  Ensure that `gs.path.root` is correctly defined and accessible.  If `gs` is not a module in the expected location, the code will fail with a `ModuleNotFoundError`.
*   `marker_files`: The marker file tuple could be configurable, perhaps as a constant at the module level.

**Relationship with Other Parts of the Project:**

*   The code relies heavily on the `src` package, specifically the `gs` module. This `gs` module likely provides functions to interact with the file system, allowing for the finding of critical project files such as the `settings.json`.
*   The `settings.json` file likely defines configurations or settings that are used by other parts of the project, demonstrating that this code is in fact part of an initial setup process.  Other scripts are likely to use `__root__`, `__project_name__`, `__version__`, etc. throughout.
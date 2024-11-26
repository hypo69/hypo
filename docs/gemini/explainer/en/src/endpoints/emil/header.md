## file hypotez/src/endpoints/emil/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.endpoints.emil 
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
__author__: str = settings.get("author", '')  if settings  else ''
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
```

```
<algorithm>
1. **Initialization:**
   - Sets `MODE` to 'dev'. 
   - Imports necessary modules: `sys`, `json`, `Version` (from `packaging.version`), and `Path` (from `pathlib`).

2. **Project Root Determination:**
   - `set_project_root()` function is called:
     - Takes a tuple `marker_files` as input.  
     - Starts at the directory of the current file (`__file__`).
     - Recursively checks parent directories for the presence of files/directories in `marker_files`.
     - If a marker file is found, the parent directory is the project root (`__root__`).
     - Adds the project root to `sys.path` if not already present.
     - Returns the `__root__` path.
   - Example: If `__file__` is `/path/to/project/hypotez/src/endpoints/emil/header.py`, the script will search up the directory tree for `pyproject.toml`, `requirements.txt`, or `.git`.


3. **Settings Loading:**
   - `__root__` is used to construct the path to the `settings.json` file.
   - Tries to load the JSON data from `settings.json` using `json.load()`.
   - If the file is not found or invalid JSON, a `...` (no-op) handles it.
   - Loads settings into the `settings` variable (dictionary).


4. **Documentation Loading:**
   - Tries to load the README.MD file into `doc_str`.
   - If the file is not found or is not valid, a `...` (no-op) handles it.
     
5. **Project Information Extraction:**
    - Extracts values from the `settings` dictionary or defaults:
      - `__project_name__`, `__version__`, `__doc__`, `__author__`, `__copyright__`, `__cofee__`.
      - Uses `settings.get()` to handle potential missing keys and provide defaults.


6. **Result:**
    - Sets variable containing project information.
   - Example:  If `settings.json` contains `"project_name": "My Project"` and `"version": "1.0.0"`, then `__project_name__` will be "My Project" and `__version__` will be "1.0.0".
```

```
<explanation>

- **Imports:**
    - `sys`: Provides access to system-specific parameters and functions, used here to modify the Python path.
    - `json`: Used for working with JSON data (loading and potentially saving settings and project metadata).
    - `packaging.version`: Used for handling and comparing software versions, not directly used but part of a standard library for handling different versions of Python packages.
    - `pathlib`: Used for working with file paths in an object-oriented way, specifically for the `Path` object used to find the project root.

- **Classes:**
    - None. No classes are defined in the provided code.

- **Functions:**
    - `set_project_root(marker_files)`: This function is crucial for finding the project root directory. It takes a tuple of filenames or directory names as input. It starts from the current file's directory and traverses up the directory hierarchy until it encounters any of the given marker files. This ensures that the function can be used in various situations without requiring a hardcoded path to the project root.  It correctly modifies the system path to include the root. It's well-documented and clear about the input and output.

- **Variables:**
    - `MODE`: A string, likely a configuration variable for running the application in different modes (e.g., development, production).
    - `__root__`: Stores the path to the project root. A very important variable for project files access.
    - `settings`, `doc_str`, `__project_name__`, `__version__`, `__doc__`, `__author__`, `__copyright__`, `__cofee__`:  These variables store data related to project configuration and metadata, likely read from files.


- **Potential Errors/Improvements:**
    - Error Handling: The `try...except` blocks for loading `settings.json` and `README.MD` are good practice. Consider adding more specific error messages for better debugging. For example, use `print("Error loading settings")` to give a more helpful message to the user.
    - Default Values: Using `settings.get()` to provide default values for settings that might be missing in the JSON is a good approach.


- **Relationships with other parts of the project:**
    - `gs.path.root`: This likely refers to a `src.gs` module that provides a class or object representing the file system structure of the project, handling project root directory access.  This dependency from `gs.path.root` makes the code more general-purpose and less tightly coupled.
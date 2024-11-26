## File hypotez/src/bots/discord/header.py

# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.bots.discord 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'dev'


"""
	:platform: Windows, Unix
	:synopsis:

"""


"""
	:platform: Windows, Unix
	:synopsis:

"""


"""
  :platform: Windows, Unix

"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""MODE = 'dev'
  
""" module: src.bots.discord """

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
    with open(gs.path.root / 'src' /  'settings.json', 'r') as settings_file:
        settings = json.load(settings_file)
except (FileNotFoundError, json.JSONDecodeError):
    ...

doc_str:str = None
try:
    with open(gs.path.root / 'src' /  'README.MD', 'r') as settings_file:
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
```
1. **Import Modules:** Imports necessary libraries: `sys`, `json`, `packaging.version`, and `pathlib`.

   * Example: `import sys` imports the `sys` module, which provides access to system-specific parameters and functions.
   

2. **`set_project_root` Function:**  Finds the project root directory.

   * **Input:** A tuple of file/directory names (`marker_files`) that are expected to exist only in the root.
   * **Process:** Starts from the current file's directory and traverses its parent directories until it finds a directory containing any of the marker files (e.g., `pyproject.toml`).
   * **Output:** Returns the path to the root directory, or the current directory if no root is found. Also adds the root directory to the `sys.path` to enable the import of modules from the project's source directory.

   * Example: If the script is in `/home/user/project/bots/discord/header.py` and the project root has `pyproject.toml`, it will return `/home/user/project/`.


3. **Get Project Root:** Calls `set_project_root()` to find the root directory (`__root__`).

4. **Import `gs`:** Imports the `gs` module from the `src` package.

5. **Load Settings:** Attempts to load settings from `gs.path.root / 'src' / 'settings.json'`.

   * **Error Handling:** Uses a `try...except` block to handle potential `FileNotFoundError` or `json.JSONDecodeError` if the file is missing or corrupt.

6. **Load Documentation:** Attempts to load documentation from `gs.path.root / 'src' / 'README.MD'`.

   * **Error Handling:** Uses a `try...except` block to handle potential `FileNotFoundError` or `json.JSONDecodeError` if the file is missing or corrupt.


7. **Extract Project Information:** Extracts `project_name`, `version`, `doc`, `details`, `author`, `copyright`, and `cofee` from the `settings` dictionary or defaults if the dictionary is not loaded.

   * **Default Values:** Uses `settings.get("key", default)` to provide default values (`'hypotez'`, `''`, etc.) for missing keys.

   * **Example:** If `settings` is empty, the `__project_name__` variable will be assigned the string `'hypotez'`.


```

<explanation>

* **Imports:**
    * `sys`: Provides access to system-specific parameters and functions, including the `sys.path` for importing modules from different directories.  Crucial for finding and including other parts of the application from the root folder.
    * `json`: Used for loading and handling JSON data (settings).
    * `packaging.version`:  Needed for handling versions, though not directly used in this specific module.
    * `pathlib`: Provides object-oriented file system paths, making file operations more structured and readable.
    * `gs`:  This is an external module/package likely defining paths (`gs.path`) within the project. This module needs to be defined elsewhere in the project to correctly import other parts.

* **Classes:** No classes are defined in this module.

* **Functions:**
    * `set_project_root()`:  This is a crucial function for finding the project root directory, ensuring that the application can locate its dependencies and resources regardless of how it's run in the project. It checks if the project root is already in `sys.path`, preventing conflicts if the script is run from different locations inside the project.

* **Variables:**
    * `MODE`: A string defining the current mode ('dev').
    * `__root__`:  A `Path` object representing the root directory of the project.  Critically important for referencing resources in the project, and ensuring consistency across different script runs.
    * `settings`: A dictionary holding project settings, loaded from `settings.json`.
    * `doc_str`:  String representing the documentation from `README.MD`.
    * `__project_name__`, `__version__`, etc.:  Variables containing project metadata, fetched from the `settings` dictionary.  Useful for identifying and working with the project.

* **Potential Errors/Improvements:**
    * **Error Handling:**  The `try...except` blocks for loading `settings.json` and `README.MD` are good, but the `...` in the except clause might be a problem.  A more specific exception or logging would improve debugging.
    * **`gs` module:** The `gs` module is presumed to be external, and the `gs.path` is critical. Its exact implementation/definition in `src` needs to be checked for its correct implementation to handle paths effectively.
    * **File Existence Check:** Consider checking file existence before opening them to prevent exceptions, adding more robust error handling.

* **Relationships with other project parts:**
    * The code depends on the `gs` module, which in turn likely depends on modules (e.g., file path manipulation) within the `src` package.  The code also directly loads the `settings.json` and `README.MD` files. These external components are critical for setting up the project structure correctly. The `__root__` variable allows to navigate the other files and folders inside the project.
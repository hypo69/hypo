## File hypotez/src/suppliers/aliexpress/gapi/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
module: src.suppliers.aliexpress.gapi 
	:platform: Windows, Unix
	:synopsis: Модуль определяющий корневой путь к проекту. Все импорты строятся относительно этого пути.
    :TODO: В дальнейшем перенести в системную переменную
"""
MODE = 'dev'

import sys
import json
from packaging.version import Version

from pathlib import Path
def set_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """!
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
```
1. **Project Root Determination:**
   * The `set_project_root` function is called, taking a tuple of marker files as input.
   * Starting from the directory of the current file, it iterates through parent directories.
   * It checks if any of the marker files exist in the current parent directory.
   * The first parent directory containing any marker file is identified as the project root.  Example: If `pyproject.toml`, `requirements.txt`, or `.git` exist in a parent directory, that parent is the root.
   * If no matching root is found, the current file's directory is returned.
   * The root path is added to `sys.path` to enable modules in the project root to be imported.


2. **Project Settings Loading:**
   * The `__root__` variable now holds the path to the project root.
   * The code tries to open `src/settings.json` within the project root.
   * If the file exists and is valid JSON, the contents are loaded into the `settings` dictionary. Otherwise, `settings` remains `None`.


3. **README Loading:**
   * The code tries to open `src/README.MD` within the project root.
   * If the file exists, its contents are read into `doc_str`. Otherwise, `doc_str` remains `None`.


4. **Project Metadata Gathering:**
   * Various project metadata variables (`__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`) are populated using values from the `settings` dictionary or default values. 
   * Error handling with `if settings` makes sure that the code doesn't crash if settings.json is missing.




```
<explanation>

**Imports:**

* `sys`: Provides access to system-specific parameters and functions, like `sys.path` for importing modules from arbitrary locations.
* `json`: Used for working with JSON formatted data, specifically for loading settings from `settings.json`.
* `packaging.version`: Provides utilities for handling software versions, although not directly used in this example.
* `pathlib`: Used for interacting with files and directories in a platform-independent way.
* `src`: This is a crucial import.  It refers to a package within the project (`src` directory or a module from it) where the `gs` module, likely containing functions for working with file paths, is located.

**Classes:**

* There are no classes defined in this file.

**Functions:**

* `set_project_root(marker_files)`:
    * **Args:** `marker_files` (tuple): A list of files or directory names used to pinpoint the project root directory.
    * **Returns:** `Path`: The root directory of the project as a `Path` object.
    * **Functionality:** Recursively searches parent directories from the current file's location for the given marker files. If found, the containing directory is returned; otherwise, the current file's directory is returned.  Crucially, the function adds the root path to `sys.path` so other modules within the project can be imported. This is essential for modular project structure.


**Variables:**

* `__root__`: (Path): Stores the path to the project root. This is crucial because other modules within the project rely on this variable to locate other modules (e.g., the `src` package, `gs.path`).
* `MODE`: (str): Likely a constant indicating the development mode (e.g., 'dev', 'prod').
* `settings`, `doc_str`: (dict, str): Dictionaries and strings that store project metadata (settings) and README contents. They are initialized with `None`.  This handles potential errors if the files don't exist or are corrupted.
* `__project_name__`, `__version__`, `__doc__`, etc.: (str): Strings containing project metadata (name, version, description, etc.).  They are obtained from the `settings` dictionary (if available) or set to default values if not.

**Potential Errors/Improvements:**

* **Robustness:** The `try...except` blocks for loading `settings.json` and `README.MD` are good.  Consider adding logging to record the success or failure of these operations, especially for debugging.
* **Error Handling**: A more descriptive message than just `...` in the exceptions would be helpful.  e.g., adding a message like: `print(f"Error loading settings: {e}")`
* **Import Path Dependency**: The code assumes that `gs` and other relevant modules are correctly structured within the `src` folder.  Adding better validation of module paths might prevent problems in a non-standard project structure.
* **Readability**: Using more descriptive variable names (e.g., `project_root` instead of `__root__`) could enhance the readability.


**Relationship with Other Parts of the Project:**

The `header.py` file is foundational. It establishes the project root and imports the `gs` module, which likely contains functions related to file paths and settings.  The metadata collected (project name, version, etc.) is expected to be used elsewhere in the project for tasks like identifying the project, generating documentation, and/or logging. Modules dependent on the `gs` module, and other modules which use the project name and version (such as package-building scripts) will rely upon this setup.
## File hypotez/src/suppliers/ivory/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.suppliers.ivory 
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
```
1. **Get Project Root:**
   - The `set_project_root` function is called to find the root directory of the project.
   - It starts from the directory containing the current script (`__file__`).
   - It iterates through parent directories looking for `pyproject.toml`, `requirements.txt`, or `.git` files.
   - Example: If `header.py` is in `hypotez/src/suppliers/ivory`, the function would search up the directory tree for these files, and return the `hypotez` directory.
   - The found directory is added to the `sys.path` allowing modules within the project to be found.
   - Returns the root path


2. **Load Project Settings:**
   - The project settings are loaded from `gs.path.root / 'src' / 'settings.json'`.
   - This reads the settings from a JSON file.
   - Example:  `settings.json` might contain data like `{ "project_name": "MyProject", "version": "1.0.0" }`
   - The file is opened and the json is loaded.
   - A `try-except` block catches `FileNotFoundError` or `json.JSONDecodeError` if the file doesn't exist or is not valid JSON.  This is important for robustness.


3. **Load Project Documentation:**
   - Attempts to read the project documentation from `gs.path.root / 'src' / 'README.MD'`.
   - The content is loaded into `doc_str`.
   - A `try-except` block catches potential errors if the file is not found or can't be read.


4. **Set Project Properties:**
   - Reads values from the `settings` dictionary, using `settings.get` which is safe against missing keys.
   - `get` returns a default value if the key is not found. This is crucial for handling missing data.
   - Example: `__project_name__ = settings.get("project_name", 'hypotez')`
   - Sets `__project_name__`, `__version__`, `__doc__`, `__author__`, `__copyright__`, and `__cofee__`.




```
<explanation>

**Imports**:

- `sys`: Used to manipulate the Python path. This code inserts the project root into the path, making modules in the `src` directory accessible.
- `json`: Used to load the project settings from a JSON file.
- `packaging.version`: Used for handling project versions (though not used directly in this specific file).
- `pathlib`: Used to work with file paths in a more object-oriented and platform-independent way.
- `src.gs`: This import is crucial as it refers to a module (`gs`) in the `src` directory.  It's likely this module handles paths related to the project. The `gs.path.root` part suggests there's a `path` module within `gs` defining where the project's root directory is. The exact implementation of `gs` is critical to understanding how this code interacts with the overall project structure.

**Classes**:

- None. This file defines no classes.

**Functions**:

- `set_project_root(marker_files) -> Path`: This function is crucial for finding the root directory of the project.
   - **Args:** `marker_files`: A tuple of filenames or directory names that indicate the project root.  Common project markers like `pyproject.toml`, `requirements.txt`, or `.git` are used.
   - **Returns:** The `Path` object to the project root.
   - **Purpose**: Locates the project root directory, adds the root to `sys.path`, making modules within the project accessible, and returns this path.

**Variables**:

- `MODE`: A string variable set to 'dev'.  Potentially used for different operation modes (development, production, etc.).
- `__root__`:  This is a `Path` object that represents the root path of the project.
- `settings`: A `dict` variable that holds the project settings read from `settings.json`.
- `doc_str`: A `str` variable that stores the contents of the project's documentation file (`README.MD`).
- `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`: String variables representing project metadata; defaults are supplied if the settings file is missing or the key is absent.

**Potential Errors/Improvements**:

- **Error Handling**: While the `try...except` blocks are good, consider more specific exception handling (e.g., instead of just `json.JSONDecodeError` catch the specific type of error).
- **gs Module**:  The reliance on the `gs` module is a strong dependency. Make sure `gs` is correctly imported and functions as intended.  The code depends on `gs.path.root` to define the project root - if the `gs` module is missing or malformed this code will fail.
- **Robustness**: The use of `.get()` for dictionaries is a good defensive approach. However, always provide suitable fallback values in case the key does not exist or the dictionary is `None`.


**Chain of Relationships**:

- This file relies on the `gs` module for locating the project root.
- It reads `settings.json` (likely containing version, author, etc.) and `README.MD` to populate project metadata.
- This file likely serves as a base for other project modules, providing access to important project information (root path, metadata).  It ensures the project structure and variables are available consistently throughout the project.
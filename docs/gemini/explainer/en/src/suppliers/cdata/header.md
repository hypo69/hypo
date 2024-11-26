## File hypotez/src/suppliers/cdata/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.suppliers.cdata 
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
```
Start
|
V
```
Get Current File Path
```
   | (Path(__file__).resolve().parent)
   |
   V
```
Find Project Root
```
   | (Iterating through parent directories)
   | (Checking for marker files: pyproject.toml, requirements.txt, .git)
   |
   V
```
Set Project Root in sys.path
```
   | (If root not already in sys.path, insert it)
   |
   V
```
Load Settings
```
|
V
(gs.path.root / 'src' / 'settings.json')
| (try-except block to handle potential errors)
V
```
Load README
```
|
V
(gs.path.root / 'src' / 'README.MD')
| (try-except block to handle potential errors)
V
```
Extract Project Metadata
```
| (settings.get() for project_name, version, author, copyright, etc.)
| (default values if not found in settings)
|
V
```
End
```

<explanation>

**Imports**:

- `sys`: Used for manipulating the Python runtime environment, specifically for inserting the project root directory into the `sys.path` to allow imports from modules within the project.
- `json`: Used for working with JSON data to load settings from `settings.json`.
- `packaging.version`: Used for working with software versions, although in this file, it seems to have no use.
- `pathlib`: Used for path manipulation, enabling the code to work with file paths in an object-oriented manner and in a platform-independent way.


**Classes**:

- The code doesn't define any classes; it defines a function, `set_project_root`.

**Functions**:

- `set_project_root(marker_files)`: This function aims to locate the root directory of a project.
    - Takes a tuple of marker files as input to identify the project root directory.
    - Iterates through parent directories of the current file's directory, checking if any of the specified marker files exist within those parent directories.
    - Returns the path to the project root directory.
    - It modifies the `sys.path` to include the project root, enabling the import of modules from the project.
    - **Example:** If `__file__` points to `hypotez/src/suppliers/cdata/header.py`, and `pyproject.toml` exists in `hypotez`, the function would return `Path('hypotez')`.


**Variables**:

- `MODE`: A string variable with a value of 'dev'. It likely represents the operation mode (e.g., development, production).
- `__root__`: A `Path` object storing the path to the project root, initialized by `set_project_root()`.
- `settings`: A dictionary used to store the project settings loaded from 'settings.json'.
- `doc_str`: A string variable used to store the contents of the 'README.MD' file.
- `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`: Variables to store project metadata (name, version, etc.). These values are loaded from the `settings` dictionary (or have defaults).


**Potential Errors/Improvements**:

- **Error Handling**: The code uses `try...except` blocks to handle `FileNotFoundError` and `json.JSONDecodeError` during the loading of `settings.json` and `README.MD`. This is a good practice. The error handling could be improved by logging the errors or providing more specific error messages instead of `...`.
- **Missing `gs` Package**: The code uses a `gs` module (e.g., `gs.path.root`).  This implies a `gs` package (or at least a module) exists in the project, but it isn't defined within this file. This might be a problem if this file is used in isolation.  The `gs` package should be documented properly, showing its purpose and structure.
- **`copyrihgnt`**: The variable `__copyright__` has a typo (`copyrihgnt`).  This should be `copyright` to be consistent.


**Relationships with other parts of the project**:

- The code relies on the existence of `settings.json` and `README.MD` in the project's `src` directory.
- It heavily depends on the `gs` package (`gs.path.root`) for accessing the project's root directory.  The relationship with `gs` needs further definition.
- The code likely forms part of a larger project structure, including other suppliers and potentially using shared settings.
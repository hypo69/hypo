## File hypotez/src/webdriver/firefox/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.webdriver.firefox 
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
__author__: str = settings.get("author", '')  if settings else ''
__copyright__: str = settings.get("copyrihgnt", '')  if settings else ''
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
```

```
<algorithm>
```
```mermaid
graph TD
    A[Start] --> B{Find Project Root};
    B -- Yes --> C[Set __root__];
    B -- No --> D[Use Current Directory];
    C --> E[Add __root__ to sys.path];
    D --> E;
    E --> F[Load settings.json];
    F -- Success --> G[Load README.MD];
    F -- Failure --> H[Use Default Values];
    G -- Success --> I[Get project details];
    G -- Failure --> I;
    H --> I;
    I --> J[End];
    
    subgraph Load settings.json
    F --> |settings|
    end
    subgraph Load README.MD
    G --> |doc_str|
    end

    subgraph Get Project Details
    I --> |__project_name|, |__version__|, |__author__|,|__copyright__|,|__cofee__|,|__doc__|;
    end
```

```
<explanation>
**Imports:**

- `sys`: Used for manipulating the Python runtime environment, specifically for adding the project root directory to the module search path (`sys.path`).
- `json`: Used for encoding and decoding JSON data for loading `settings.json`.
- `packaging.version`: Used for handling and potentially validating version strings, although not directly utilized in this script.
- `pathlib`: Used for working with file paths in a more object-oriented manner.  This is a key improvement over string-based path manipulations.


**Classes:**

- There are no classes defined in this file.  All logic is contained within functions.


**Functions:**

- `set_project_root(marker_files)`:
    - **Arguments:** A tuple `marker_files` containing filenames or directory names (like 'pyproject.toml') to locate the project root. Defaults to common project markers.
    - **Return Value:** A `Path` object representing the project root directory.
    - **Functionality:** Recursively searches up the directory tree from the current file's location until a directory containing any of the specified `marker_files` is found.  If not found, it returns the current directory. It also adds the root to `sys.path` for importability.  This is crucial for correctly locating other packages within the project.
    - **Example:** If `marker_files` includes `'pyproject.toml'`, and the project root is two levels above the current file, `set_project_root` will return the path to the project root.


**Variables:**

- `MODE`: A string variable, likely representing the operational mode of the application (e.g., 'dev', 'prod').
- `__root__`: A `Path` object, stores the path to the project root directory after `set_project_root` is called.
- `settings`: A dictionary to store data loaded from `settings.json`.
- `doc_str`: A string variable to store the content of the `README.MD` file.
- `__project_name__`, `__version__`, `__author__`, `__copyright__`, `__cofee__`, `__doc__`: Variables storing project metadata retrieved from `settings.json`, with fallback values.

**Relationship with Other Project Components (if applicable):**

- `gs.path.root`: This suggests the existence of a module (`gs`) containing functions and/or classes to interact with paths within the project.  Likely part of a project-specific utility library.
- `from src import gs`: This import establishes a relationship where the current module depends on the `gs` module for functionalities, such as path operations.
- `settings.json` and `README.MD` files are assumed to be located in the project's root directory. They are critical for configuration and documentation.
- The variable names (`__project_name__`, `__version__`, etc.) are conventionally used as metadata, suggesting the existence of a wider system that uses this information.  For example, a system potentially uses these variables for building documentation, versioning, or other similar tasks.

**Potential Errors/Improvements:**

- Error Handling:  The `try...except` blocks around file reading are good practice.  Consider adding more specific error messages (logging) to make debugging easier.
- File Existence Check:  Before opening `settings.json` or `README.MD`, a simple check to see if the files exist would prevent unnecessary exceptions.

- `copyrihgnt` should probably be `copyright`.

- Missing `__init__.py`: It's important for Python to recognize the `src` directory as a package. Make sure `src/__init__.py` exists.

- Using `Path` throughout: The code now leverages `Path` objects consistently, which is generally preferred for its robustness compared to string manipulation.
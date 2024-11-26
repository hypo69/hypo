## File hypotez/src/category/header.py

# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
module: src.category 
	:platform: Windows, Unix
	:synopsis: Модуль определяющий корневой путь к проекту. Все импорты строятся относительно этого пути.
    :TODO: В дальнейшем перенести в системную переменную"""
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
```mermaid
graph TD
    A[__file__ / current path] --> B{Check if marker files exist in current dir};
    B -- Yes --> C[__root__ = current_path];
    B -- No --> D[Go to parent dir];
    D --> B;
    C --> F[return __root__];
    D --> E[Check for markers in parent];
    E -- Yes --> C;
    E -- No --> D;
    F --> G[Add __root__ to sys.path]
    G --> H[Initialize variables (__project_name__, __version__, ...)]
    Subgraph settings_load
        H --> I[Open settings.json];
        I -- Success --> J[Load settings from json];
        I -- Failure --> K[settings = None];
        J --> H;
        K --> H;
    end
    Subgraph doc_load
        H --> L[Open README.MD];
        L -- Success --> M[Read doc string];
        L -- Failure --> N[doc_str = None];
        M --> H;
        N --> H;
    end
    H --> O[Set variables with settings/defaults];
    O --> P[Return values];
```
```
<explanation>

**Imports**:

- `sys`: Provides access to system-specific parameters and functions, primarily used for manipulating the Python path (`sys.path`).
- `json`: Used for encoding and decoding JSON data, enabling reading and parsing the `settings.json` file.
- `packaging.version`: Used for checking and working with software version strings.
- `pathlib`: Used for working with file paths in a more object-oriented and platform-independent manner.

**Classes**:

-  There are no classes defined in this code.


**Functions**:

- `set_project_root(marker_files=...)`:
    - **Arguments**: `marker_files` (default: `('pyproject.toml', 'requirements.txt', '.git')`) is a tuple of filenames/directory names to search for. This signifies the root folder of the project.
    - **Return Value**: `Path` to the root directory. Returns the current directory if no marker file is found.
    - **Functionality**: This function recursively traverses the directory tree upwards from the current file's location until it finds a directory containing any of the specified marker files.  It ensures that the root directory of the project is added to the Python path using `sys.path.insert(0, str(__root__))`, which is crucial for importing modules from the project's source code.


**Variables**:

- `__root__`:  A `Path` object representing the root directory of the project, found by `set_project_root()`.  Critically, this variable is used to modify `sys.path`, ensuring the project's modules are discoverable.
- `MODE`: A string variable, likely for development/production mode configuration.
- `settings`: A dictionary that holds project configuration, loaded from `settings.json`.  Uses `try-except` blocks to gracefully handle the case of missing or invalid `settings.json`.
- `doc_str`: String containing the content of `README.MD` file.  Handles errors during reading the `README.MD` file.
- `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`: Variables containing project metadata.  Their values are extracted from the `settings` dictionary.  They use `settings.get()` to handle missing keys. The `if settings` checks are crucial for preventing errors if `settings` is `None`.


**Potential Errors/Improvements**:

- **Robustness**: The use of `try-except` blocks around file loading is a good start for handling file not found errors, but a more comprehensive approach could include more specific error handling (e.g., `json.JSONDecodeError` for corrupted JSON). It would be beneficial to provide a fallback mechanism for the `settings.json` file not being present or if a key does not exist. This should include default values for those settings.
- **Error Logging**: Including logging statements within the `try-except` blocks can significantly improve debugging and provide information about problems encountered.
- **Configuration Flexibility**:  Using a more configurable way of specifying the marker files (e.g., through a configuration file) would enhance flexibility and maintainability.
- **Docstring Improvement**:  Adding type hints for all variables and functions would improve readability and maintainability.
- **`gs.path.root`**:  This suggests the existence of a `gs` module (likely `hypotez/src/gs.py`).  Understanding how this module determines and provides the `root` path is crucial to understanding the full functionality and potential issues within the module. This module must be investigated for a complete picture.



**Relationship Chain**:

The `header.py` module relies on `gs.path` for obtaining the project root.  This suggests a dependency chain to `gs.py` (and the potentially other parts) for proper functioning. `settings.json` and `README.md` files contain project-specific data and documentation respectively.
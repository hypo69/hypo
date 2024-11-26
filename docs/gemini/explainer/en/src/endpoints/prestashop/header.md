## File hypotez/src/logger/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
module: src.logger 
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

1. **Initialization:**
    *   The script imports necessary modules (`sys`, `json`, `packaging.version`, `pathlib`).
    *   A global variable `MODE` is set to 'dev'.
    *   The function `set_project_root` is defined.

2. **Project Root Determination:**
    *   `set_project_root` takes a tuple of marker files as input.
    *   It starts at the current file's directory and recursively checks parent directories.
    *   If any marker file exists in a parent directory, that directory is returned as the project root. Otherwise, the current directory is returned.
    *   The root directory is added to `sys.path` to allow imports from any subfolder of the project root.
    *   Example: If `pyproject.toml` is found in the parent folder, that folder will be set as `__root__`.


3. **Settings and Documentation Loading:**
    *   The script retrieves the project root using the `set_project_root` function and assigns it to `__root__`.
    *   It attempts to load project settings from `src/settings.json`. If successful, it assigns the loaded settings to `settings`.
    *   It attempts to read documentation from `src/README.MD`. If successful, it assigns the content to `doc_str`.
    *   Both operations use `try...except` blocks to handle potential `FileNotFoundError` and `json.JSONDecodeError` exceptions.


4. **Project Information Gathering:**
    *   The script retrieves the project name, version, documentation, author, copyright, and coffee-link from the `settings` dictionary if the `settings` dictionary is available.
    *   Defaults are provided if a specific value is not found or if the settings file is missing.


**Data Flow:**

```
+-----------------+       +-----------------+       +-----------------+
| Current File Dir |------>|set_project_root|------>|__root__ (Path)|
+-----------------+       +-----------------+       +-----------------+
       ^                                    |
       |                                    |
       |                                    v
       |   (marker_files)                    | Loads project settings
       |                                    | and documentation.
       |                                    v
       +----------------------------------------+
                                                |
               +-----------------+               |
               | src/settings.json |----------------|
               +-----------------+  |    (try block)
                                        |
                                        v  
     +-----------------+       +-----------------+       +-----------------+
     |  __project_name__,   |---->|   __version__   |------->|   Project Information  |
     |  __doc__,         |    |   __author__ ,  |      |   Variables            |
     | __details__,      |    |   __copyright__, |      +-----------------+
     | __cofee__        |    |   __cofee__    |      |
     +-----------------+    +-----------------+      v
                                      Project usage
```

```
<explanation>

**Imports:**

*   `sys`: Provides access to system-specific parameters and functions, primarily used for manipulating the Python path (`sys.path`).
*   `json`: Used for encoding and decoding JSON data for loading settings from `settings.json`.
*   `packaging.version`:  Used for handling versions in a robust way, a standard approach to managing software versions.
*   `pathlib`: Allows working with file paths in a more object-oriented and platform-independent way.  Crucial for handling file paths correctly across different operating systems.

**Classes:**

No classes are defined in the provided code.


**Functions:**

*   `set_project_root(marker_files)`:
    *   **Arguments:** `marker_files` (tuple): A tuple of filenames or directory names used to locate the project root.
    *   **Return value:** `Path`: The path to the project root directory, or the current directory if no suitable root is found.
    *   **Functionality:** Recursively searches up the directory tree for the first directory containing any of the specified marker files, adding the root to `sys.path` if not already present.  This is a common pattern for determining the project root when writing modules that can be imported.

**Variables:**

*   `MODE`: A global variable, likely a string constant used to track the current mode (e.g., 'dev', 'prod').
*   `__root__`: A global variable of type `Path` representing the root directory of the project, initialized by `set_project_root()`.
*   `settings`: A global dictionary storing project settings loaded from `settings.json`.
*   `doc_str`: A global string storing the project documentation (README content) loaded from `README.MD`.
*   `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`: Global variables storing project information extracted from the settings (or default values). These are commonly used for metadata.

**Potential Errors/Improvements:**

*   Error handling: The `try...except` blocks for `settings.json` and `README.MD` are good, but more specific exception handling (e.g., `FileNotFoundError` vs. `json.JSONDecodeError` ) can enhance code robustness.
*   File format validation: The code assumes `settings.json` is valid JSON. Consider validating the JSON structure further to avoid unexpected behavior.
*   Logging: Consider using a logging module for more sophisticated error reporting and debugging information.
*   Clearer variable naming: Using more descriptive names (e.g., `project_root` instead of `__root__`) can improve code readability.
*   `gs.path.root`:  It's unclear where `gs` comes from.  Knowing the `gs` module's location and purpose would clarify this code's role within the larger project.


**Relationship with other parts of the project:**

The code heavily relies on the `gs` module, likely containing a global settings object or functions for accessing project paths (`gs.path.root`). This means this file interacts closely with code within the `src` package to determine the project's overall structure. The way `set_project_root` is implemented suggests the project is designed in a modular fashion, with different parts of the application relying on this function for consistent access to the project structure.  The use of `from src import gs` indicates a dependency relationship between the `logger` and other `src` modules.  A better understanding of the `gs` module's functionality would make the analysis far more complete.
```
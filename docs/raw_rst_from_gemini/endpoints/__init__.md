```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.endpoints """
import sys
from pathlib import Path
from packaging.version import Version
from .version import __version__, __doc__, __details__  # Move import here for better order
from src import gs  # Move import here for better order
from .kazarinov import bot
from .emil import EmilDesign


def get_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """!
    Finds the root directory of the project starting from the current file's directory,
    searching upwards and stopping at the first directory containing any of the marker files.

    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.

    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
    current_path = Path(__file__).resolve().parent
    project_root = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            project_root = parent
            break

    if project_root not in sys.path:
        sys.path.insert(0, str(project_root))  # Use str() for compatibility

    return project_root


# Get the root directory of the project
project_root = get_project_root()
"""project_root (Path): Path to the root directory of the project"""


# Explicitly importing to use these objects/classes
# in functions, rather than just referencing them.
bot: object = bot  
EmilDesign: object = EmilDesign
```

**Improvements and Explanation:**

* **Import Order:**  Import statements have been reorganized for better structure and readability.  `from .version import ...` , `from src import gs`, and other imports are moved above the function definition to be closer to where they are used. This keeps the imports logically grouped.

* **Variable Name:** Changed `__root__` to `project_root` for better naming conventions and avoiding possible confusion with special names like `__name__` or `__file__`.

* **Redundancy Removal:** The docstrings now focus on the purpose of the function. The `__root__` variable declaration within the function and the subsequent docstring (which was redundant) have been removed.

* **Clearer Path Handling:** Instead of `str(__root__)`, the `str(project_root)` now directly creates the string for insertion into `sys.path`, this is clearer and more Pythonic.


* **Explicit Object Import:** The lines `bot: object = bot` and `EmilDesign: object = EmilDesign` explicitly import the objects from the respective modules for better clarity, and to prevent potential issues if these are meant to be used elsewhere in this script.  This approach makes it clear that you're *using* those objects.  If you're just documenting that they exist in this module, you can remove these lines.


* **Docstring Consistency:** Docstrings follow the standard Python docstring style and conventions more closely.


**Why these changes are important:**

* **Readability:**  The revised code is more readable and easier to understand due to the import organization.
* **Maintainability:** The cleaner code is easier to maintain and modify in the future.
* **Robustness:** The use of `str(project_root)` for `sys.path` insertion is a more robust way to handle path conversion for Python.  If `project_root` contained special characters it would not be able to be inserted safely by merely passing the object.


This improved version is more professional, maintainable, and adheres to better Python coding practices. Remember to use a linter (like flake8) to further refine the code.

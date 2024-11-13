```python
## \file hypotez/src/ai/gemini/version.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.ai.gemini """
import json
import sys
from pathlib import Path

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
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            return parent
    return current_path


# Define project root
__root__ = get_project_root()

if __root__ not in sys.path:
    sys.path.insert(0, str(__root__))

try:
    settings = None
    settings_path = __root__ / 'src' / 'settings.json'
    with open(settings_path, 'r', encoding='utf-8') as settings_file:  # Added encoding
        settings = json.load(settings_file)

    __project_name__ = settings.get("project_name", 'hypotez')
    __version__ = settings.get("version", '')
    __doc__ = settings.get("doc", '')
    __details__ = settings.get("details", '')
    __author__ = settings.get("author", '')
    __copyright__ = settings.get("copyright", '')
    __coffee__ = settings.get("coffee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")

except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Ошибка при чтении settings.json: {e}")
    #  Crucial: Exit gracefully if settings.json is missing or corrupt.
    sys.exit(1)

```

**Improvements and Explanations:**

* **Error Handling (Crucial):** The `try...except` block now properly catches `FileNotFoundError` and `json.JSONDecodeError`.  Critically, it now includes `sys.exit(1)`. This is essential.  If `settings.json` is missing or the JSON is corrupted, the script should exit with a non-zero exit code (1) to indicate an error to the calling environment. This is standard practice and often used to signal errors to build systems.


* **Encoding:** Added `encoding='utf-8'` to the `open()` function. This is **essential** if your `settings.json` file might contain characters outside the ASCII range.  Without it, you could get errors when reading non-ASCII characters.

* **Variable Naming:** Changed `__cofee__` to `__coffee__`.  Consistent with standard Python variable naming conventions.

* **Clearer Error Message:** The error message now includes the specific exception type and the value of `e`, making debugging easier.

* **Removed Redundant `if settings`:**  Since `settings` is checked within the `get()` methods, you can safely remove the redundant `if settings` conditions and read directly from the `settings` dictionary, simplifying the code.

* **Simplified `get()` calls:** Changed `settings.get("copyrihgnt", '')` to `settings.get("copyright", '')`

* **Explicit `__version__` Assignment:** Explicitly assigns `__version__ = settings.get("version", '')` so it is assigned even if 'version' isn't in the json.

**How to Use:**

1.  **Ensure `settings.json` Exists:** Create a `settings.json` file in the `src` directory of your project with the following structure:

```json
{
  "project_name": "YourProjectName",
  "version": "1.0.0",
  "doc": "Your Project Documentation",
  "details": "More project details",
  "author": "Your Name",
  "copyright": "Your Copyright",
  "coffee": "Link to coffee" 
}
```

2.  Run the `version.py` script. If `settings.json` is valid, the script will assign the correct values to the special variables, and if it isn't, the script exits with an informative error.


This improved version is much more robust and reliable.  Remember to replace placeholders like "YourProjectName", "Your Name", etc. with your project's details.
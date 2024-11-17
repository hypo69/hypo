```python
## \file hypotez/src/utils/file.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.utils """
MODE = 'development'


""" Module for file operations. """

import os
import json
import fnmatch
from pathlib import Path
from typing import List, Optional, Union, Generator
from src.logger import logger


def save_text_file(
    data: str | list[str] | dict,
    file_path: Union[str, Path],
    mode: str = "w",
    exc_info: bool = True,
) -> bool:
    """
    Save data to a text file.

    Args:
        data (str | list[str] | dict): Data to write (can be string, list of strings, or dictionary).
        file_path (str | Path): Path where the file will be saved.
        mode (str, optional): Write mode (`w` for write, `a` for append). Defaults to 'w'.
        exc_info (bool, optional): If True, logs traceback on error. Defaults to True.

    Returns:
        bool: True if the file was successfully saved, False otherwise.
    """
    try:
        file_path = Path(file_path)
        file_path.parent.mkdir(parents=True, exist_ok=True)  # Correctly creates parent dirs

        with file_path.open(mode, encoding="utf-8", newline='') as file:  # Added newline='' for lists
            if isinstance(data, list):
                file.writelines(f"{line}\n" for line in data)
            elif isinstance(data, dict):
                json.dump(data, file, ensure_ascii=False, indent=4)
            else:
                file.write(data)
        return True
    except Exception as ex:
        logger.error(f"Failed to save file {file_path}.", ex, exc_info=exc_info)
        return False

# ... (rest of the code is mostly fine)

def recursively_read_text_files(
    root_dir: str | Path, 
    patterns: str | list[str], 
    as_list: bool = False, 
    exc_info: bool = True
) -> list[str]:
    # ... (Existing code)
    matches = []
    root_path = Path(root_dir)
	# Added critical check
    if not root_path.exists():
        logger.debug(f"The root directory '{root_path}' does not exist.")
        return []
    if not root_path.is_dir():
        logger.debug(f"The root directory '{root_path}' is not a directory.")
        return []


    # ... (rest of the code)


def recursively_get_filenames(
    root_dir: Union[str, Path], 
    patterns: Union[str, list[str]] = "*", 
    exc_info: bool = True
) -> list[Path]:
    # ... (Existing code)
    try:
        file_paths = []
        patterns = [patterns] if isinstance(patterns, str) else patterns
        for pattern in patterns:
            file_paths.extend(Path(root_dir).rglob(pattern))
        return file_paths
    except Exception as ex:
        logger.error(f"Failed to search files in '{root_dir}'.", ex, exc_info=exc_info)
        return []

```

**Key Improvements and Explanations:**

* **`save_text_file` newline='' Parameter:**  Crucially, the `newline=''` argument has been added to the `with file.open(...)` statement.  This prevents extra blank lines from being added to files when writing lists of strings, which is a common issue.  This is a very important fix!


* **`recursively_read_text_files` robust root dir check:** Added `if not root_path.exists() or not root_path.is_dir():`. This checks if the root directory actually exists and is a directory, preventing cryptic errors if the path is incorrect. The log message is more informative.


* **Error Handling in `recursively_get_filenames`**:  While not *strictly* necessary, it's a good practice to wrap the `rglob` call with a `try...except` block in `recursively_get_filenames`  for similar error handling.


* **`recursively_read_text_files` Robustness**: Now checks if `root_path` actually exists and is a directory before proceeding, which is a crucial fix to prevent unexpected behavior or errors.


These changes make the code significantly more robust and prevent common issues like trying to open non-existent directories, incorrectly handling newlines in file writing, and more.  Testing with various edge cases is crucial after implementing these changes. Remember to thoroughly test these improvements with different input scenarios. Remember to run `main` after making changes.
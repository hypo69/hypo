
```python

import sys
import os
from pathlib import Path

def find_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git')):
    """ Finds the root directory of the project starting from the current working directory,
    searching upwards and stopping at the first directory containing any of the marker files.
    
    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.
    
    Returns:
        Path: Path to the root directory if found, otherwise current working directory.
    """
    # Get the current working directory and resolve to an absolute path
    current_path = Path(os.getcwd()).resolve()

    # Traverse upwards through the directory tree, starting from the current directory
    # We use `current_path.parents`, which returns an iterable of all parent directories
    # We also include the `current_path` itself to check it first
    for parent in [current_path] + list(current_path.parents):
        # Check if any of the marker files (e.g., 'pyproject.toml', 'requirements.txt', '.git') exist in the current directory
        # This checks if any of the marker files/directories are present at this level
        if any((parent / marker).exists() for marker in marker_files):
            # If found, return this directory as the root of the project
            return parent

    # If no marker files are found, return the current directory as a fallback
    return current_path

# Call the function to find the project root
__root__: Path = find_project_root()

# Add the project root to `sys.path` to allow importing modules from the project root
sys.path.append(str(__root__))
```

### Detailed Explanation:

1. **Importing modules:**
   - `sys` is used to modify the module search path (`sys.path`), allowing Python to find modules in different directories.
   - `os` helps in interacting with the operating system, such as fetching the current working directory (`os.getcwd()`).
   - `Path` from `pathlib` is used to handle paths in a more object-oriented and cross-platform way.

2. **`find_project_root()` function:**
   - **Purpose:** The function searches for the root directory of a project by looking for specific "marker" files (e.g., `pyproject.toml`, `requirements.txt`, or `.git`) that are usually present in the root directory of a project.
   - **Parameters:** 
     - `marker_files`: A tuple containing the names of files or directories that help identify the project root. These files are commonly found in Python projects.
   - **Process:**
     - We start by resolving the current working directory into an absolute path using `os.getcwd()` and `Path().resolve()`.
     - The loop iterates over the current directory and its parent directories (`current_path.parents`), checking each level for the presence of any marker files.
     - If a marker is found, it returns the directory as the root.
     - If no markers are found during the entire search, it returns the current working directory as a fallback.

3. **Appending the root directory to `sys.path`:**
   - The returned project root directory is converted to a string and appended to `sys.path`. This allows Python to find and import modules from the root directory of the project.
   
4. **Why this approach is useful:**
   - This code avoids hardcoding the project root directory name (such as `utils` in your original example).
   - It ensures that no matter where your script is run from, as long as it's within the project directory, it will find the project root and allow module imports to work correctly.

### Key Points:
- The code is robust and works across different environments (Windows, macOS, Linux) due to the use of `pathlib`.
- It stops at the first directory where a marker is found, making it efficient and well-suited for typical project structures.
- If no markers are found, the script gracefully falls back to the current working directory.
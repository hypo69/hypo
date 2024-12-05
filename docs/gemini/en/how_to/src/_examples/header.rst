rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code block defines a function `set_project_root` that determines the root directory of a project. It searches up the directory tree from the current file's location until it finds a directory containing specific marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`).  If found, it sets the project root and adds it to the Python path (`sys.path`). The code also loads project settings from `settings.json` and documentation from `README.MD` if they exist.  Finally, it extracts project metadata (name, version, author, etc.) from the settings.

Execution steps
-------------------------
1. **Import necessary modules:** The code imports the `sys`, `json`, `pathlib`, and `packaging.version` modules.
2. **Define `set_project_root` function:** This function takes an optional `marker_files` tuple as input.  It starts from the directory containing the script (`__file__`).
3. **Traverse up the directory tree:** It iterates through parent directories until one containing any of the specified marker files is located.
4. **Set the project root:** If a directory with marker files is found, it's set as the project root.
5. **Add project root to sys.path:** If the root directory isn't already in `sys.path`, the function appends it to ensure the project's modules can be imported correctly.
6. **Return the project root path:** The function returns the determined project root path.
7. **Determine the project root:** The `__root__` variable is set to the value returned from the `set_project_root` function.
8. **Load project settings:** It attempts to load settings from `gs.path.root / 'src' / 'settings.json'` into the `settings` variable.  If the file doesn't exist or is not valid JSON, it handles the exception gracefully, leaving `settings` as `None`.
9. **Load project documentation:** The code attempts to load the documentation from `gs.path.root / 'src' / 'README.MD'`.  If the file is not found or any error occurs, it will handle the exception and `doc_str` will be `None`.
10. **Extract project metadata:** The code extracts project name, version, author, copyright, and documentation from the `settings` dictionary (if loaded successfully). It provides default values if a particular key isn't found or the settings are unavailable.
11. **Provide the project details:** The code defines variables for project name, version, documentation, details, author, copyright, and developer support links using values from the `settings` dictionary.

Usage example
-------------------------
.. code-block:: python

    import sys
    from pathlib import Path
    from hypotez.src.utils._examples.header import set_project_root

    # Example usage (replace 'path/to/your/script' with the actual path):
    try:
        root_dir = set_project_root()
        print(f"Project root directory: {root_dir}")
        print(f"Project name: {__project_name__}")  # Accessing the global variable
        print(f"Project version: {__version__}")
    except Exception as e:
        print(f"An error occurred: {e}")
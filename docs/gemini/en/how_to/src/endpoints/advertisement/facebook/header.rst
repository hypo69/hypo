rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code block defines a function `set_project_root` that determines the root directory of a project. It searches up the directory tree from the current file's location until it finds a directory containing specific marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`). If found, it adds the root directory to the Python path and returns the path.  The code also loads project settings from `settings.json` and documentation from `README.MD` files.  It extracts key project metadata like name, version, author, copyright, and a developer support link from these files.


Execution steps
-------------------------
1. The code imports necessary modules: `sys`, `json`, `pathlib`, `packaging.version`.
2. It defines the function `set_project_root` which takes a tuple of marker files as an argument.
3. It gets the current file's directory.
4. It iterates through parent directories starting from the current file's directory.
5. For each parent directory, it checks if any of the specified marker files exist within that directory.
6. If a directory with a marker file is found, it sets `__root__` to that directory and breaks the loop.
7. If `__root__` is not already in `sys.path`, it adds the root directory to the `sys.path`.
8. It returns the path to the root directory.
9. It calls `set_project_root()` to retrieve the project root directory.
10. It attempts to load project settings from `settings.json` located in the project root directory, storing the contents in the `settings` variable.  It handles potential errors like `FileNotFoundError` or `json.JSONDecodeError`.
11. It attempts to load documentation from `README.MD` in the project root directory, storing the contents in the `doc_str` variable.  It handles potential errors like `FileNotFoundError` or `json.JSONDecodeError`.
12. It extracts project metadata (project name, version, author, copyright, support link) from the loaded settings (or defaults if settings aren't loaded).
13. It returns the project root path


Usage example
-------------------------
.. code-block:: python

    import os
    from pathlib import Path
    from hypotez.src.endpoints.advertisement.facebook.header import set_project_root

    # Example usage (assuming you have a project structure with pyproject.toml, requirements.txt and settings.json)
    project_root = set_project_root()
    print(f"Project root directory: {project_root}")

    # Access project metadata (Example)
    print(f"Project Name: {__project_name__}")
    print(f"Project Version: {__version__}")

    # Access documentation (Example)
    print(f"Project Documentation: {__doc__}")
    # ... (other metadata access) ...
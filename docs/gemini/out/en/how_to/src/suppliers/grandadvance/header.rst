rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code block defines a function `set_project_root` that locates the root directory of a project. It searches upward from the current file's directory until it finds a directory containing specific marker files (like `pyproject.toml`, `requirements.txt`, or `.git`).  It then sets the project root directory in `sys.path` if it's not already present. The code also loads settings from a `settings.json` file and documentation from a `README.MD` file within the project root, providing various project details.

Execution steps
-------------------------
1. **Import necessary modules:** The code imports `sys`, `json`, `Path` from `pathlib`, `Version` from `packaging.version`, and potentially other modules based on what modules are used by the application.
2. **Define `set_project_root` function:** This function takes a tuple of marker files as input.
3. **Find the root directory:** The code starts from the directory of the current file (`__file__`). It then recursively traverses its parent directories until one containing any of the specified marker files is found.
4. **Set project root in `sys.path`:** If the project root directory is not already present in `sys.path`, it's added to the beginning of the list.
5. **Return the project root:** The function returns the `Path` object representing the found project root.
6. **Get project root:** The `__root__ = set_project_root()` line calls the function and assigns the returned Path object to the `__root__` variable.
7. **Load settings from `settings.json`:** The code attempts to load the settings from the `settings.json` file in the project root directory using `json.load`. It handles potential `FileNotFoundError` or `json.JSONDecodeError` exceptions.
8. **Load documentation from `README.MD`:** The code attempts to load the documentation from the `README.MD` file in the project root directory. It also handles potential `FileNotFoundError` or `json.JSONDecodeError` exceptions.
9. **Extract project details:** If the `settings` dictionary is not empty or `None`, the code extracts the `project_name`, `version`, `author`, `copyright`, and `cofee` information from the settings. Otherwise, default values are used.
10. **Assign extracted details:** The code assigns the extracted values to the variables `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, and `__cofee__`.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.grandadvance.header import set_project_root

    # Example usage, assuming the marker files (pyproject.toml, requirements.txt, .git) are present in the project directory.
    project_root = set_project_root()
    print(f"Project root: {project_root}")
    print(f"Project name: {__project_name__}")  # Accessing the variable defined in the code block
    print(f"Project version: {__version__}")
rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code block defines a function `set_project_root` to locate the root directory of a project. It searches up the directory tree from the current file's location until it finds a directory containing specific marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`).  It then adds this root directory to Python's module search path (`sys.path`) and returns the path object.  The code further reads settings from `settings.json` and the project's `README.MD` file, loading them into respective variables.  Finally, it initializes project variables like name, version, documentation, details, author, copyright, and a coffee link based on the loaded data or defaults.

Execution steps
-------------------------
1. **Import necessary modules:** Imports `sys`, `json`, `Version` from `packaging`, `Path` from `pathlib`. This ensures needed functionalities are available.
2. **Define the `set_project_root` function:** This function takes an optional tuple of marker files as input.
3. **Locate the project root:** It starts from the current file's directory and traverses up the directory tree to find the first directory containing any of the specified marker files.
4. **Add the root directory to sys.path:**  It appends the found root directory to the `sys.path` list. This allows Python to import modules from this location.
5. **Return the project root:** Returns the `Path` object representing the located root directory.
6. **Call `set_project_root` function:** This call sets the `__root__` variable to the project root.
7. **Read `settings.json`:** Attempts to read the content of the `settings.json` file in the root directory and load it as a JSON dictionary into the `settings` variable.  Handles `FileNotFoundError` and `json.JSONDecodeError` if the file doesn't exist or isn't valid JSON.
8. **Read `README.MD`:** Attempts to read the content of the `README.MD` file in the project root and loads it into the `doc_str` variable. Also handles file-related exceptions.
9. **Initialize project variables:** Extracts values from the `settings` dictionary (if available) for project name, version, documentation, details, author, copyright, and the coffee link. If `settings` is empty, uses default values.
10. **Return the root directory and loaded variables:** This code block returns the root directory to `sys.path` and the retrieved settings from `settings.json` and `README.md` as variables.

Usage example
-------------------------
.. code-block:: python

    # Assuming you have a project structure like this:
    # myproject/
    #   src/
    #     goog/
    #       drive/
    #         header.py
    #     settings.json
    #     README.MD
    #   pyproject.toml
    #   requirements.txt

    # In your script:
    from hypotez.src.goog.drive.header import set_project_root

    project_root = set_project_root()
    print(f"Project root: {project_root}")
    print(f"Project name: {__project_name__}")
    print(f"Project version: {__version__}")
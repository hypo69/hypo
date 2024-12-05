rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code block defines a function `set_project_root` that locates the project's root directory. It then loads project settings from a JSON file and project documentation from a Markdown file. Finally, it assigns various project attributes like name, version, documentation, author, copyright, and a coffee donation link.

Execution steps
-------------------------
1. **Import necessary modules:** The code imports `sys`, `json`, `Version` from `packaging`, and `Path` from `pathlib`. This ensures the necessary functions and classes are available for use.
2. **Define `set_project_root` function:** This function takes a tuple of marker files as input. It starts from the current file's directory and traverses up the directory tree.
3. **Locate project root:** The function iterates through parent directories until it finds a directory containing any of the specified marker files (`pyproject.toml`, `requirements.txt`, `.git`). This determines the project's root directory.
4. **Add root directory to sys.path:** If the found root directory is not already in the `sys.path` list, it's added to the beginning of the list, making modules within the project accessible.
5. **Return the root path:** The function returns the identified root path, which is stored in the `__root__` variable.
6. **Load project settings:** The code attempts to open and load settings from a `settings.json` file located within the project's root directory using `json.load()`.  If the file isn't found or the JSON is invalid, it handles potential errors and proceeds without settings.
7. **Load project documentation:** The code attempts to open and read documentation from a `README.MD` file located within the project's root directory.  If the file isn't found or the read fails, it handles errors and continues without documentation.
8. **Assign project attributes:** The code extracts specific settings (project name, version, author, copyright, coffee donation link) from the loaded settings dictionary, using default values if certain settings are missing.
9. **Set project attributes:** It assigns these extracted values to variables like `__project_name__`, `__version__`, `__doc__`, `__author__`, `__copyright__`, and `__coffee__`.
10. **Return the root path and project attributes:** The code stores the project root path and other project attributes in variables and returns the root path.

Usage example
-------------------------
.. code-block:: python

    from hypotez.src.endpoints.advertisement.header import set_project_root

    # Call the function to get the project root directory
    project_root = set_project_root()

    # Access project attributes (example)
    print(f"Project Name: {__project_name__}")  # Replace __project_name__ with the actual variable name
    print(f"Project Version: {__version__}")
    print(f"Project Root: {project_root}")
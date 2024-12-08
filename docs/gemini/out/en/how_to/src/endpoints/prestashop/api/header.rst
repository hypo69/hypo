rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code block defines a function `set_project_root` that locates the root directory of a project.  It then retrieves project settings from a JSON file and documentation from a Markdown file.  Finally, it assigns these values to variables for later use.

Execution steps
-------------------------
1. **Import necessary modules:** The code imports `sys`, `json`, `Version`, and `Path` from the `pathlib` module.

2. **Define `set_project_root` function:**  This function takes an optional `marker_files` tuple as input. It initializes a `Path` object to the current file's directory and iterates through the parent directories until it finds one containing any of the specified marker files (like 'pyproject.toml' or '.git').

3. **Check if root directory is in `sys.path`:** If the determined root directory is not already in the Python module search path (`sys.path`), it's added to the front of the list.

4. **Return project root directory:** The function returns the path to the located project root directory.

5. **Initialize `__root__` variable:** The code calls `set_project_root()` to determine the project root directory and stores the result in the `__root__` variable.

6. **Import `gs`:**  The `src` package is imported.

7. **Load project settings:** The code tries to open and load settings from the `settings.json` file located within the project root. If successful, it stores the settings in the `settings` dictionary.  If not successful, it handles `FileNotFoundError` or `json.JSONDecodeError` exceptions.

8. **Load project documentation:** The code tries to open and read documentation from the `README.MD` file located within the project root. If successful, it stores the documentation content in the `doc_str` variable. If not, it handles `FileNotFoundError` or `json.JSONDecodeError` exceptions.

9. **Assign project attributes:**  The code assigns values to various project variables (like `__project_name__`, `__version__`, `__doc__`, etc.) based on the settings dictionary or defaults if no settings are found.  These variables are meant to hold information about the project, like its name, version, and documentation.

Usage example
-------------------------
.. code-block:: python

    from hypotez.src.endpoints.prestashop.api.header import set_project_root

    # Example usage of set_project_root (assuming 'pyproject.toml' and 'requirements.txt' exist in the project root)
    root_path = set_project_root()
    print(f"Project root: {root_path}")

    # Example access to project variables (after running the code block above)
    # ... assuming the 'settings.json' file is correctly formatted, and the 'README.MD' exists.
    print(f"Project Name: {__project_name__}")
    print(f"Project Version: {__version__}")
    print(f"Documentation: {__doc__}")
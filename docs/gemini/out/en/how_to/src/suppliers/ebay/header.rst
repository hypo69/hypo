rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code snippet defines a function `set_project_root` that determines the root directory of a project. It then loads project settings from a `settings.json` file and project documentation from a `README.MD` file located within the project root directory. Finally, it defines several variables, such as project name, version, documentation, etc., either pulling data from the settings file or setting default values if the file is missing or the data is not present.

Execution steps
-------------------------
1. The code imports necessary modules: `sys`, `json`, `packaging.version`, and `pathlib`.
2. It defines a function `set_project_root` that takes a tuple of marker files as input.
3. It starts by resolving the current file path to get the current directory.
4. It iterates through parent directories, checking if any of the specified marker files exist within those directories.
5. If a directory with marker files is found, the function sets the `__root__` variable to this directory, and it breaks the loop.
6. The function ensures the root directory is in `sys.path` to allow imports of modules within the project.
7. It returns the determined root directory (`__root__`).
8. The code calls `set_project_root` to get the root directory and stores it in the `__root__` variable.
9. The code attempts to open the `settings.json` file in the root directory and load the JSON data into the `settings` variable. If the file is not found or the JSON is invalid, it handles the error gracefully (using `...`).
10. The code attempts to open the `README.MD` file in the root directory and read the content into the `doc_str` variable. If the file is not found or there's an error, it gracefully handles the error.
11. The code defines several variables (`__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`) by extracting data from the `settings` dictionary if it's available. If `settings` is `None` or a key is missing, it uses a default value.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.ebay.header import set_project_root

    # Example usage assuming 'pyproject.toml' and 'requirements.txt' exist in the project root
    root_dir = set_project_root()
    print(f"Project root: {root_dir}")

    # Accessing project details
    print(f"Project name: {__project_name__}")
    print(f"Version: {__version__}")
    print(f"Documentation: {__doc__}")
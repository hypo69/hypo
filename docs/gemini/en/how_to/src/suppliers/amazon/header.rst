rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code block defines a function `set_project_root` that determines the root directory of a project. It then initializes several variables related to project metadata. These variables include the project root directory (`__root__`), project name (`__project_name__`), version (`__version__`), documentation (`__doc__`), details (`__details__`), author (`__author__`), copyright (`__copyright__`), and a coffee link (`__cofee__`). The values are loaded from `settings.json` and `README.MD` files located within the project's root directory.  It handles potential `FileNotFoundError` and `json.JSONDecodeError` exceptions during file loading.  Crucially, it adds the project root to the Python path (`sys.path`). This ensures that modules within the project can be imported correctly.

Execution steps
-------------------------
1. The code defines the function `set_project_root` that takes a tuple of marker files as an argument.
2. It starts by resolving the current file's path and taking its parent directory as the initial potential project root (`__root__`).
3. It iterates through the parent directories of the current file's directory.
4. For each parent directory, it checks if any of the marker files specified exists within that directory.
5. If a marker file is found, it updates `__root__` to this parent directory and breaks the loop.
6. If no marker file is found in any parent directory, `__root__` remains the initial path.
7. It adds the determined `__root__` to the Python path `sys.path`.
8. It returns the determined project root path (`__root__`).
9. It calls `set_project_root()` to get the project root path.
10. It tries to load settings from `settings.json` in the project root and handles potential errors.
11. It tries to load documentation from `README.MD` in the project root and handles potential errors.
12. It initializes project metadata variables (`__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`) with values from the loaded settings, defaulting to provided values if the settings file is not found or is invalid.


Usage example
-------------------------
.. code-block:: python

    # Example usage (assuming the project structure and files are correct)
    from hypotez.src.suppliers.amazon.header import __project_name__, __version__, __doc__

    print(f"Project Name: {_project_name_}")
    print(f"Project Version: {_version_}")
    print(f"Project Doc: {_doc_}")
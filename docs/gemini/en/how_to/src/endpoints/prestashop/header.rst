rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code defines a function `set_project_root` that determines the root directory of a project.  It searches up the directory tree from the current file's location, looking for specific marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`).  If found, the function returns the path to the root directory.  If not found, it returns the directory where the script resides. Importantly, it adds the root directory to Python's module search path (`sys.path`), enabling correct imports from other parts of the project.  The code then loads project settings from a `settings.json` file and optional project documentation from a `README.MD` file. Finally it sets project metadata variables such as name, version, documentation, author, copyright and a coffee support link.

Execution steps
-------------------------
1. **Import necessary modules**: The code imports `sys`, `json`, `Path` from `pathlib`, `Version` from `packaging.version`, and `gs` from `src`.

2. **Define the `set_project_root` function**: This function takes an optional tuple `marker_files` as input.  It starts from the current file's directory and recursively checks parent directories.

3. **Check for marker files**: It iterates through parent directories and checks if any of the specified marker files exist within that directory.

4. **Set the root directory**: When a marker file is found, the function stores the parent directory as the `__root__` variable.

5. **Add the root directory to sys.path**: If the root directory is not already in `sys.path`, it's added to the beginning of the list. This modification allows Python to find modules and packages located within the project directory tree.

6. **Return the root directory**:  The function returns the determined project root directory.

7. **Set the project root**: The `__root__` variable is initialized by calling `set_project_root()`.

8. **Load project settings**: The code attempts to load settings from `settings.json` located in the `src` directory within the project root. It handles `FileNotFoundError` and `json.JSONDecodeError` if the file is missing or corrupted.

9. **Load project documentation**:  The code attempts to load documentation from `README.MD` located in the `src` directory within the project root. It handles `FileNotFoundError` and `json.JSONDecodeError` if the file is missing or corrupted.

10. **Set project metadata**: The code defines project metadata variables (`__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__coffee__`) using values from the settings or default values if settings are not available or relevant keys are missing.

Usage example
-------------------------
.. code-block:: python

    # Example usage (assuming you have a project directory structure):
    from hypotez.src.endpoints.prestashop.header import __root__, __project_name__, __version__

    print(f"Project root: {__root__}")
    print(f"Project name: {__project_name__}")
    print(f"Project version: {__version__}")
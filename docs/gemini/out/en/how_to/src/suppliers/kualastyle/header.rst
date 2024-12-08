rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code block defines a function `set_project_root` that locates the project root directory. It then sets the project root path in `sys.path` and loads project settings and documentation.

Execution steps
-------------------------
1. **Import necessary modules:** The code imports `sys`, `json`, `packaging.version`, and `pathlib` for file operations and version handling.

2. **Define `set_project_root` function:** This function takes a tuple of marker files as input.

3. **Find the project root:** It starts from the directory of the current file (`__file__`) and iterates up the directory tree until it finds a directory containing any of the specified marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`).

4. **Add project root to `sys.path`:** If the project root is found, it adds the path to the `sys.path` list. This ensures that Python can import modules from the project's source directory.

5. **Return the project root:** The function returns the path to the project root directory.

6. **Get the project root:** The code calls `set_project_root()` to find the root directory and assigns the result to `__root__`.

7. **Load project settings:** It attempts to load project settings from a `settings.json` file located in the `src` directory of the project root.  If the file doesn't exist or is not valid JSON, an exception is caught and no settings are loaded.

8. **Load project documentation:**  The code attempts to load documentation from a `README.MD` file located in the `src` directory. If the file doesn't exist or is not valid content, an exception is caught, and no documentation is loaded.


9. **Assign project metadata:**  It retrieves project name, version, author, copyright, and coffee-donation link from the settings (if available) or uses defaults.

10. **Set global variables:** The extracted values are assigned to global variables such as `__project_name__`, `__version__`, `__doc__`, and more for later use (e.g., in packaging information, or displayed documentation).

Usage example
-------------------------
.. code-block:: python

    import pathlib

    # Replace with the path to your module file
    module_file_path = pathlib.Path("./hypotez/src/suppliers/kualastyle/header.py")

    # Call set_project_root with your marker files.  
    project_root = set_project_root(marker_files=('pyproject.toml',))

    # Print the project root directory
    print(f"Project root: {project_root}")

    # This example assumes you have a 'settings.json' file in the project root's 'src' folder.  
    # Access the values you need after this block runs.  For example
    print(f"Project Name: {__project_name__}")
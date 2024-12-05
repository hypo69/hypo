rst
How to use this code block
=========================================================================================

Description
-------------------------
This code block defines a function `set_project_root` that finds the root directory of a project. It searches upwards from the current file's directory until it finds a directory containing specific marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`).  If found, it adds the root directory to Python's `sys.path`.  It then loads project settings from `settings.json` and optionally the project's documentation from `README.MD`.  Finally, it defines several variables storing project details (name, version, documentation, author, copyright, etc.).

Execution steps
-------------------------
1. **Import necessary modules:** The code imports `sys`, `json`, `Version` from `packaging.version`, and `Path` from `pathlib`.

2. **Define `set_project_root` function:** This function takes a tuple of marker file names as input.

3. **Determine current path:** It gets the current file's path and resolves it to an absolute path.

4. **Iterate through parent directories:** It iterates through the current file's parent directories using a generator expression.

5. **Check for marker files:** For each parent directory, it checks if any of the specified marker files exist within that directory.

6. **Set root path:** If a marker file is found, the `__root__` variable is updated with the path of the parent directory, and the loop breaks.

7. **Add root path to sys.path:** If the root path is not already in `sys.path`, it's added to the beginning of the list using `sys.path.insert(0, str(__root__))`.

8. **Return root path:** The function returns the determined root path.

9. **Call `set_project_root`:** The code calls `set_project_root` to obtain the root directory of the project.

10. **Load project settings:** The code attempts to load project settings from `settings.json` located within the project's root directory using `json.load()`.

11. **Load project documentation:** The code attempts to load project documentation from `README.MD` located within the project's root directory and reads it into the `doc_str` variable.

12. **Define project details:** The code defines project variables (name, version, documentation, author, copyright, etc.) using data from the loaded settings (or default values if settings are not found).


Usage example
-------------------------
.. code-block:: python

    # Example usage (assuming you have pyproject.toml, requirements.txt, etc.)
    import os
    from hypotez.src.logger import header
    # ... other imports

    # Find project root, which will now be in sys.path.
    root_dir = header.set_project_root()

    # Verify the root directory:
    print(f"Project root directory: {root_dir}")

    # Access project name:
    project_name = header.__project_name__
    print(f"Project name: {project_name}")

    # Access project version
    version = header.__version__
    print(f"Project version: {version}")


    # Access project documentation, if available.
    documentation = header.__doc__
    if documentation:
        print("Project Documentation:")
        print(documentation)
    else:
        print("No documentation found.")
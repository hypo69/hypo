rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code defines a function `set_project_root` to locate the project root directory. It then loads project settings from a `settings.json` file and optionally retrieves documentation from a `README.MD` file.  Finally, it assigns these values to variables accessible across the project.

Execution steps
-------------------------
1. **Import necessary modules:** The code imports `sys`, `json`, `Version` from `packaging`, `Path` from `pathlib`. This ensures that the required functions and classes are available.

2. **Define `set_project_root` function:** This function takes a tuple of marker files as input. It starts from the current file's directory and traverses up the directory tree until it finds a directory containing at least one of the marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`).


3. **Determine project root:** The code iterates through parent directories to locate the project's root directory based on the presence of the specified marker files.  It returns the path to this root directory.

4. **Add project root to sys.path:** If the project root isn't already in the Python path, it is added to the `sys.path` list so Python can import modules from within the project.

5. **Load project settings:**  The code attempts to load project settings from a `settings.json` file located within the project root directory. If the file is not found or cannot be parsed, it handles the error gracefully.


6. **Load project documentation:** The code attempts to load project documentation from a `README.MD` file located within the project root directory. If the file is not found or cannot be parsed, it handles the error gracefully.

7. **Initialize project variables:**  The code assigns values to variables representing project name, version, documentation, details, author, copyright, and a coffee support link. These values are obtained from the loaded project settings (if available) or default values if the settings file is missing or corrupted.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.morlevi.header import set_project_root

    # Example usage of the function to set the project root
    project_root = set_project_root()
    print(f"Project root: {project_root}")

    # Example of accessing project name, assuming settings.json is present
    # and contains "project_name" key
    from hypotez.src.suppliers.morlevi.header import __project_name__
    print(f"Project name: {__project_name__}")

    # Example of accessing project version
    from hypotez.src.suppliers.morlevi.header import __version__
    print(f"Project version: {__version__}")
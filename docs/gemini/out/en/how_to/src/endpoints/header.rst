How to use this code block
=========================================================================================

Description
-------------------------
This Python code defines a function `set_project_root` that determines the root directory of a project. It then loads settings from a `settings.json` file and optionally, project documentation from a `README.MD` file.  It also retrieves project metadata like name, version, author, copyright, and a "coffee" support link from these settings and stores it as module-level variables.  It ensures the project root directory is added to the Python path for correct module imports.  Importantly, it handles potential errors (e.g., `FileNotFoundError`, `json.JSONDecodeError`) gracefully to avoid crashes during script execution.

Execution steps
-------------------------
1. **Import necessary modules:** The code imports `sys`, `json`, `packaging.version`, `pathlib`, and potentially other modules used in the project.


2. **Define `set_project_root` function:** This function takes a tuple of marker files as input. It starts at the directory containing the current script's `.py` file (`__file__`) and recursively checks parent directories to find the first directory containing any of the provided marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`).

3. **Check `sys.path`:** If the project root is found, the code checks if it's already in the `sys.path`. If not, it appends the project root path to the beginning of `sys.path`. This ensures correct import of modules from the project.

4. **Locate and load settings:** The code uses `gs.path.root` (likely a defined variable in another part of the project) to locate the `settings.json` file. It attempts to load the JSON data into the `settings` variable.  Error handling with `try...except` blocks prevents the script from crashing if the file is missing or the JSON format is invalid.

5. **Locate and load documentation:** Similarly, the code attempts to open and read the `README.MD` file to `doc_str`.  Again, error handling catches potential `FileNotFoundError` and `json.JSONDecodeError`.

6. **Retrieve project metadata:** Using the loaded `settings` dictionary, the code extracts values for project name, version, author, copyright, and the coffee support link, storing them as module-level variables (`__project_name__`, `__version__`, etc.). Default values are used if a corresponding key is missing in the settings.

7. **Store module-level variables:**  The extracted values are assigned to module-level variables (e.g., `__project_name__`, `__version__`, `__doc__`, etc.) within the script, making them available to other parts of the code.

8. **Return the root path:** The function returns the `__root__` path.


Usage example
-------------------------
.. code-block:: python

    # Assuming you have a 'gs' module that defines gs.path.root (you would need to provide that in a separate example).
    import sys
    from hypotez.src.endpoints.header import set_project_root

    # Example usage. Replace with your actual marker files.
    root_path = set_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git'))
    print(f"Project root: {root_path}")
    print(f"Project name: {__project_name__}")  # Accessing the module-level variable
    print(f"Project version: {__version__}")  # Accessing another module-level variable
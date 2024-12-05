rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code block defines a function `set_project_root` to locate the root directory of a project. It then loads project settings from a `settings.json` file and project documentation from a `README.MD` file, if these files exist. Finally, it assigns the obtained values to variables for later use (e.g., in documentation generation or other project-level initialization).  The code also adds the project root directory to Python's module search path.


Execution steps
-------------------------
1. **Import necessary modules:** The code imports `sys`, `json`, `Version` from `packaging.version`, and `Path` from `pathlib`.


2. **Define `set_project_root` function:** This function takes a tuple of filenames (`marker_files`) as input.  It starts from the current file's directory and iterates through its parent directories.

3. **Find the project root:** The function checks if any of the specified `marker_files` exist within each parent directory.  If any are found, the function sets `__root__` to that parent directory and breaks the loop.  If none of the marker files are found, it keeps the current path as the root.

4. **Add project root to sys.path:**  If the found root directory is not already in the Python module search path (`sys.path`), it adds it to the beginning of the path.

5. **Return the project root:** The function returns the `__root__` directory path.


6. **Retrieve project settings (from settings.json):** The code attempts to load the project settings from `settings.json` and stores the loaded content in the `settings` variable.  Handles `FileNotFoundError` or `json.JSONDecodeError` if the file is not found or the JSON is malformed.


7. **Retrieve documentation (from README.MD):** The code attempts to read project documentation from `README.MD` and stores it in the `doc_str` variable. Handles `FileNotFoundError` or `json.JSONDecodeError` if the file is not found or the format is incorrect.


8. **Assign values to variables:**  The code extracts values from the `settings` dictionary, if available, for variables like `__project_name__`, `__version__`, `__doc__`, `__author__`, `__copyright__`, and `__coffee__`. It uses default values if a key is missing or if the `settings` dictionary is not loaded.

9. **Returns the root path and the initialized project variables:** The function returns the `__root__` object and the initialized variables that are potentially utilized for further project-level operations.


Usage example
-------------------------
.. code-block:: python

    # Assuming you have a 'pyproject.toml', 'requirements.txt', and '.git' folder in your project
    from hypotez.src.endpoints.kazarinov.scenarios.header import set_project_root

    root_dir = set_project_root()
    print(f"Project root directory: {root_dir}")
    print(f"Project name: {__project_name__}")  # Access the variable defined in the code
rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code block defines a function `set_project_root` that finds the root directory of a project.  It then loads project settings from a JSON file and optionally a README.md file. Finally, it sets several project-related variables for later use, such as the project name, version, and documentation.

Execution steps
-------------------------
1. **Import necessary modules:** The code imports `sys`, `json`, `packaging.version`, and `pathlib` for various functionalities.

2. **Define `set_project_root` function:** This function takes an optional tuple of file/directory names (`marker_files`) as input. It starts from the directory containing the current Python file (`__file__`).

3. **Iterate through parent directories:** It recursively searches upward through parent directories until it finds a directory that contains any of the files/directories in the `marker_files` tuple (e.g., `pyproject.toml`, `requirements.txt`, `.git`).

4. **Set project root and add to `sys.path`:** If a suitable directory is found, it sets the `__root__` variable to the parent directory and inserts it into the `sys.path` list, allowing Python to import modules from the project's source folder.

5. **Return root directory:** The function returns the identified root path (`__root__`).

6. **Get project root:** It calls the `set_project_root` function to determine the project's root directory and stores the result in the `__root__` variable.

7. **Load project settings:**  The code attempts to open and parse a JSON file named `settings.json` located in the project's `src` directory.

8. **Load README:** The code tries to open the project's `README.MD` file and read the content into the `doc_str` variable.

9. **Set project variables:**  It defines several variables (`__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`) using values from the `settings` dictionary. Defaults are provided for cases where the `settings` are not available.

Usage example
-------------------------
.. code-block:: python

    # Example usage (assuming the necessary files and modules are in place)
    from hypotez.src.goog.text_to_speech.header import set_project_root

    project_root = set_project_root()
    print(f"Project root: {project_root}")
    print(f"Project name: {__project_name__}")  # Accessing the project name
    print(f"Project version: {__version__}")    # Accessing the project version
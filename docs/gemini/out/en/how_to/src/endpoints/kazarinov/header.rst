rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code block defines a function `set_project_root` that locates the project root directory.  It then initializes several project-related variables, including the project name, version, documentation, author, copyright information and a developer support link. These variables are loaded from the `settings.json` file within the project's root directory.  If the `settings.json` file is missing or invalid, default values are used. It also handles potential `FileNotFoundError` and `json.JSONDecodeError` exceptions during file reading.

Execution steps
-------------------------
1. **Import necessary modules:** The code imports the `sys`, `json`, `pathlib`, and `packaging.version` modules.


2. **Define `set_project_root` function:** This function takes a tuple of marker files as input. It starts from the current file's directory and traverses up the directory tree.


3. **Locate project root:** The code iterates through parent directories until it finds a directory containing any of the specified marker files (`pyproject.toml`, `requirements.txt`, `.git`).


4. **Set project root path:** The path to the found root directory is stored in the `__root__` variable.


5. **Add root to Python path:** The function adds the root directory to the `sys.path` to enable importing modules from the project.


6. **Load project settings:** The code attempts to read the `settings.json` file located in the project's `src` folder.


7. **Handle potential errors:** The code uses a `try...except` block to catch `FileNotFoundError` and `json.JSONDecodeError` exceptions in case the `settings.json` file doesn't exist or is corrupted.


8. **Load project documentation:** The code reads the `README.MD` file within the project's `src` folder and stores the content in the `doc_str` variable.


9. **Handle potential documentation errors:** The code uses a `try...except` block to catch `FileNotFoundError` and `json.JSONDecodeError` exceptions in case the `README.MD` file doesn't exist.


10. **Assign project-related variables:** The code assigns the `project_name`, `version`, `documentation`, `author`, `copyright`, and `developer_support_link` variables with values from the `settings.json` file or uses default values.


11. **Return project root:** The function returns the project root path (`__root__`).


12. **Initialize project variables:** The function calls `set_project_root()` to determine and set the project root directory.


Usage example
-------------------------
.. code-block:: python

    # ... (other imports) ...

    # Set the project root directory.
    project_root = set_project_root()

    # Access project name.
    project_name = __project_name__
    print(f"Project name: {project_name}")

    # Access project version.
    project_version = __version__
    print(f"Project version: {project_version}")

    # Access project documentation (README.md content).
    project_documentation = __doc__
    print(f"Project documentation:\n{project_documentation}")
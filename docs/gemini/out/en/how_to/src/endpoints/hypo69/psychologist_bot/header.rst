rst
How to use this code block
=========================================================================================\n\nDescription
-------------------------
This Python code block defines a function `set_project_root` that locates the root directory of a project. It searches upwards from the current file's directory until it finds a directory containing specific marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`). If found, it adds the root directory to Python's `sys.path`. Otherwise, it uses the current directory as the root. It then loads settings from `src/settings.json` and project documentation from `src/README.MD`, storing these in variables. Finally, it defines several variables containing project metadata (name, version, documentation, author, copyright, and a coffee link).


Execution steps
-------------------------
1. **Import necessary modules:** The code imports modules `sys`, `json`, `Version` from `packaging` and `Path` from `pathlib`.


2. **Define `set_project_root` function:** This function takes a tuple of filenames/directories (`marker_files`) as input.


3. **Determine the current directory:** The code gets the directory containing the script using `Path(__file__).resolve().parent`.


4. **Iterate and find the project root:** The code iterates through the current directory and its parent directories. In each directory, it checks if any of the marker files specified in `marker_files` exist.  If found, the root directory is assigned, and the loop breaks.


5. **Add root to sys.path:** If the root directory isn't already in `sys.path`, it's added at the beginning.


6. **Return the project root:** The function returns the determined root directory (`__root__`).


7. **Get project root:** The `__root__` variable is assigned the result of calling `set_project_root()`.


8. **Load settings:** The code attempts to load settings from `gs.path.root / 'src' / 'settings.json'`.  If it fails (FileNotFoundError or json.JSONDecodeError), it skips to the next step.


9. **Load documentation:** The code attempts to load documentation from `gs.path.root / 'src' / 'README.MD'`. If it fails, it assigns an empty string to `doc_str`.


10. **Define project metadata variables:** The code sets variables such as `__project_name__`, `__version__`, `__doc__`, `__author__`, `__copyright__`, and `__cofee__` based on the loaded settings or default values if settings are not available or invalid.


11. **Return the variables:** The script effectively sets these metadata variables.


Usage example
-------------------------
.. code-block:: python

    import sys
    from pathlib import Path

    # Replace with the actual location of header.py
    current_file_path = Path(__file__).resolve()
    project_root_path = set_project_root()


    print(f"Project root: {project_root_path}")
    print(f"Project name: {__project_name__}")  # Access the variable
    print(f"Project version: {__version__}")  # Access the variable
    print(f"Project documentation: {__doc__}") # Access the variable
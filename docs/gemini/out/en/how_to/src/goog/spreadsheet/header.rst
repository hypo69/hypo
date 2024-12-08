rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code block defines a function `set_project_root` that locates the project's root directory. It then sets the project root directory in the Python path and loads settings from a JSON file named `settings.json` and optionally, documentation from `README.MD` within the project.  It retrieves various project metadata like the project name, version, documentation, author, copyright, and a coffee donation link.  The function initializes crucial variables for project-related information for use in subsequent modules.

Execution steps
-------------------------
1. **Import necessary libraries:** The code starts by importing the `sys`, `json`, `packaging.version`, and `pathlib` modules.
2. **Define `set_project_root` function:** This function takes a tuple of marker files as input (e.g., `pyproject.toml`, `requirements.txt`).
3. **Find the project root:** It iterates through parent directories starting from the current file's directory. For each parent directory, it checks if any of the marker files exist within it. If a marker file is found, it sets the `__root__` variable to that parent directory and breaks the loop.
4. **Add root to Python path:** If the found root directory is not already in the Python path, it adds it to the beginning of the path using `sys.path.insert(0, str(__root__))`.
5. **Return the root directory:**  The function returns the `__root__` Path object.
6. **Set the project root directory:** The function `set_project_root()` is called to determine the project root and store it in the `__root__` variable.
7. **Load settings from JSON:** It attempts to load settings from the file `gs.path.root / 'src' / 'settings.json'`.  This is critical to access project-specific configuration information.
8. **Load Documentation from README:** It tries to load documentation from the `gs.path.root / 'src' / 'README.MD'`.
9. **Initialize project metadata:** It extracts project metadata (name, version, doc string, author, etc.) from the `settings` dictionary if the loading is successful, otherwise defaults are used.
10. **Handle potential errors:**  `try...except` blocks handle `FileNotFoundError` and `json.JSONDecodeError` to gracefully handle cases where the configuration file or README does not exist.


Usage example
-------------------------
.. code-block:: python

    import os
    from pathlib import Path
    from hypotez.src.goog.spreadsheet.header import set_project_root, gs

    # Create dummy files for the example.  Important: Replace these with the actual file paths in your project.
    (Path(__file__).parent / "pyproject.toml").touch()
    (Path(__file__).parent / "settings.json").write_text('{"project_name": "MyProject", "version": "1.0.0"}')

    # Replace with actual path to the src folder.
    os.makedirs(Path(__file__).parent / 'src', exist_ok=True)
    
    # Simulate gs.path existence:
    gs.path = type('FakePath', (object,), {'root': Path(__file__).parent})
    
    # Call the function
    root_dir = set_project_root()
    print(f"Project root: {root_dir}")
    print(f"Project name: {__project_name__}")
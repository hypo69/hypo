rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code defines a function `set_project_root` to locate the project root directory. It searches upward from the current file's directory until it finds a directory containing specific marker files (like `pyproject.toml`, `requirements.txt`, or `.git`).  The function then adds the project root to Python's module search path (`sys.path`).  It also attempts to load settings from a `settings.json` file located within the project root.

Execution steps
-------------------------
1. The code imports necessary modules: `sys`, `json`, `pathlib`, `packaging.version`, and potentially other modules depending on the project structure (e.g., from `src`).


2. It defines the function `set_project_root` which takes a tuple of marker files as input.

3. It starts at the directory containing the current file.

4. It iterates through parent directories of the current file's directory.

5. For each parent directory, it checks if any of the marker files exist within that directory.

6. If any marker file is found, the function sets `__root__` to that parent directory and breaks out of the loop.

7. If no marker file is found in any parent directory, `__root__` remains as the directory of the current file.

8. It adds the project root (`__root__`) to the Python module search path (`sys.path`) if it's not already present.

9. The function returns the `__root__` directory.

10. The code calls `set_project_root()` to get the project root directory and stores it in the variable `__root__`.

11. It attempts to load the `settings.json` file from the project root directory.

12. If the file is found and the JSON is valid, the loaded data is stored in the `settings` variable.

13. If the file is not found or the JSON is invalid, it handles the exception with `...` (e.g., continues execution or logs an error).


Usage example
-------------------------
.. code-block:: python

    import os
    from pathlib import Path

    # Example usage (assuming you have a project structure with pyproject.toml in the root):
    # Create a dummy settings.json file for testing
    settings_json_content = {"name": "My Project", "version": "1.0.0"}
    (Path(__file__).parent / "src" / "settings.json").write_text(
        json.dumps(settings_json_content, indent=4)
    )
    # Replace 'pyproject.toml' with the actual path if necessary.
    root_dir = set_project_root(marker_files=('pyproject.toml',))

    print(f"Project root: {root_dir}")

    if settings:
        print("Settings loaded successfully:")
        for key, value in settings.items():
            print(f"\t{key}: {value}")
    else:
        print("Settings file not found or invalid.")
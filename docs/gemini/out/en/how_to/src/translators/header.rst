rst
How to use the header.py file
========================================================================================

Description
-------------------------
This Python script (`header.py`) initializes the project environment by finding the project root directory, adding it to the Python path, and loading project settings and documentation. It primarily sets up variables (`__root__`, `settings`, `doc_str`, etc.) that are used throughout the project.  It handles cases where settings.json or README.MD are missing.

Execution steps
-------------------------
1. **Import necessary modules**: The script imports modules like `sys`, `json`, `pathlib`, `packaging.version`, and the `gs` module, likely from the project's own packages.

2. **Determine the project root**: The `set_project_root` function searches upwards from the current file's location for directories containing specific marker files (like `pyproject.toml`, `requirements.txt`, or `.git`). This ensures the script works correctly regardless of the project's structure.

3. **Add project root to sys.path**: The root directory is added to `sys.path`, so Python can import modules from the project.

4. **Load project settings**: It attempts to load the project settings from `src/settings.json` using `json.load()`.  This file likely contains configuration data for the project.

5. **Load documentation**: The script tries to load documentation from `src/README.MD`. This step is critical for context.

6. **Set project variables**: Values from settings are assigned to project-level variables (`__project_name__`, `__version__`, `__doc__`, etc.).

7. **Handle missing files**: `try...except` blocks ensure the script doesn't crash if `settings.json` or `README.MD` aren't found, setting default values instead.

8. **Return and use root path**: Finally, the script returns the path of the project root and it's used by the calling scripts.


Usage example
-------------------------
.. code-block:: python

    # Assuming 'gs' is defined elsewhere.
    import header

    # Get the project root directory
    project_root = header.__root__
    print(f"Project root: {project_root}")

    # Access project settings (if they exist)
    if header.settings:
        project_name = header.__project_name__
        version = header.__version__
        print(f"Project Name: {project_name}, Version: {version}")

    # Access documentation (if it exists)
    documentation = header.__doc__
    if documentation:
        print("\nProject Documentation:\n", documentation)
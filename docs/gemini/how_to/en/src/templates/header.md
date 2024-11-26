# How to Use `hypotez/src/templates/header.py`

This file, `hypotez/src/templates/header.py`, provides a way to locate the project root directory and add it to Python's module search path.  This is crucial for projects with a modular structure.

## Purpose

The primary function of this script is to automatically determine the root directory of the project and add it to Python's `sys.path`.  This ensures that modules within the project are accessible from any file within the project.

## Key Concepts

* **Project Root:** The top-level directory of the project, containing essential files like `pyproject.toml`, `requirements.txt`, or a `.git` directory.
* **`sys.path`:** A list of directories Python searches for modules.
* **`Path` object (from `pathlib`):**  Provides an object-oriented way to work with file paths, ensuring platform compatibility.


## Usage Guide

1. **Import the `set_project_root` function:**

   ```python
   from hypotez.src.templates.header import set_project_root
   ```


2. **Call `set_project_root` to determine the project root:**

   ```python
   project_root = set_project_root()
   ```

   This function searches upwards from the current file's location for directories containing specific marker files (by default `pyproject.toml`, `requirements.txt`, and `.git`).  It returns a `Path` object representing the project root.  Crucially, it also adds the project root to the `sys.path` list.


3. **Verify the project root:**

   ```python
   print(f"Project root: {project_root}")
   ```

   This will output the path to the project root.

4. **Import modules from the project:**

   ```python
   from src import gs  # Import gs module from the project
   ```

   After calling `set_project_root()`, modules from within the project (e.g., `src/gs.py`) will be accessible.


## Function Details

* **`set_project_root(marker_files=...)`**:
    * Takes an optional `marker_files` tuple to specify which files to look for to determine the project root.
    * Traverses up the directory tree from the current file until a directory containing at least one of the specified marker files is found.
    * If the root directory isn't already in `sys.path`, it prepends it, ensuring modules can be imported.
    * Returns the `Path` object representing the project root.
    * Very Importantly, it modifies `sys.path`.  This is critical for making the project's modules importable.


## Example Project Structure (Illustrative)

```
myproject/
├── src/
│   └── gs.py
└── pyproject.toml
└── requirements.txt
└── setup.py  # or a similar configuration file
```

In a Python file located within the `myproject` directory, you would simply import the `gs` module:

```python
from myproject.src import gs 
```

This example uses the `header.py` to automate this process, and in that case, the file `gs.py` will be located in `/src/gs.py`.  After running `header.py`, the directory `myproject` is added to `sys.path`.


## Potential Issues and Troubleshooting

* **Incorrect marker files:** If the project doesn't use the files specified in `marker_files`, you need to adjust the `marker_files` argument in `set_project_root()` or add other appropriate marker files.
* **Missing modules:** If a module is still not found after setting the project root, ensure the module is properly structured within the project (`src/gs.py` in the example) and the file paths are correct.



By following these steps, you can consistently and reliably determine the project root and import necessary modules in your Python projects using this `header.py` file. Remember to adjust the marker files as needed for your specific project structure.
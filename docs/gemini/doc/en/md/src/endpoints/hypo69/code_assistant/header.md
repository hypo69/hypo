# hypotez/src/logger/header.py

## Overview

This module, `src.logger`, defines the root path to the project. All imports are structured relative to this path.  Future versions will likely move this functionality to system variables.  The current version uses marker files like `pyproject.toml`, `requirements.txt`, and `.git` to locate the project root.


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project starting from the current file's directory by searching upwards. The search stops at the first directory containing any of the specified marker files.

**Parameters**:

- `marker_files` (tuple): Filenames or directory names to identify the project root.  Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.


**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.


**Example Usage**:

```python
root_path = set_project_root()
print(root_path)
```

### `set_project_root`

**Description**:  Finds the root directory of the project. This function is used to establish the project's root path, which is essential for relative imports and locating project files.

**Parameters**:

- `marker_files` (tuple, optional): A tuple of file or directory names to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.


**Returns**:

- `Path`: The path to the project root.  If the project root cannot be found using the provided markers, the current file's directory is returned.

**Raises**:

- None


## Variables

### `__root__`

**Description**:  Stores the path to the project's root directory, obtained by calling `set_project_root()`.


### `settings`

**Description**: A dictionary containing project settings, loaded from `src/settings.json`.


### `doc_str`

**Description**: A string containing the content of the project's `README.MD` file.



### `__project_name__`

**Description**: The project name, obtained from `settings.json`, defaulting to `hypotez`.

### `__version__`

**Description**: The project version, obtained from `settings.json`, defaulting to an empty string.

### `__doc__`

**Description**: The project documentation string, obtained from `README.MD`, defaulting to an empty string.


### `__details__`

**Description**: Project details (empty string by default)


### `__author__`

**Description**: The project author, obtained from `settings.json`, defaulting to an empty string.


### `__copyright__`

**Description**: The project copyright, obtained from `settings.json`, defaulting to an empty string.


### `__cofee__`

**Description**: A string containing the coffee encouragement link. Obtained from settings.json, defaulting to a specified URL.




## Error Handling

The module includes `try...except` blocks to gracefully handle potential errors during file reading:

- `FileNotFoundError`: If the `settings.json` or `README.MD` files are not found.
- `json.JSONDecodeError`: If the content of `settings.json` is not valid JSON.

These blocks prevent the script from crashing and provide better error handling.
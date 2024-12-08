# hypotez/src/suppliers/aliexpress/header.py

## Overview

This module, `src.suppliers.aliexpress`, provides utility functions for interacting with the AliExpress supplier data. This includes retrieving settings from `settings.json` and project-level documentation from `README.MD`, and setting the project root directory for proper module imports.

## Functions

### `set_project_root`

**Description**: This function dynamically finds the root directory of the project. It starts from the current file's directory and searches upwards until it finds a directory containing specified marker files (`pyproject.toml`, `requirements.txt`, `.git`).  If no such directory is found, it returns the directory containing the current script. This ensures that project-specific modules and resources are importable.


**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names used to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.


**Returns**:

- `Path`: The path to the root directory of the project. Returns the directory containing the script if the root directory is not found.


**Example Usage**:

```python
root_path = set_project_root()
print(root_path)
```


### `set_project_root`

**Description**: This function dynamically finds the root directory of the project. It starts from the current file's directory and searches upwards until it finds a directory containing specified marker files (`pyproject.toml`, `requirements.txt`, `.git`).  If no such directory is found, it returns the directory containing the current script. This ensures that project-specific modules and resources are importable.


**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names used to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.


**Returns**:

- `Path`: The path to the root directory of the project. Returns the directory containing the script if the root directory is not found.


**Example Usage**:

```python
root_path = set_project_root()
print(root_path)
```

**Note**: The function adds the found project root directory to `sys.path` to enable import capabilities.

```python
if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
```



## Module Variables

The module defines several variables for storing project information.

### `__root__`

**Type**: `Path`

**Description**: Stores the path to the project root directory, determined by the `set_project_root` function.


### `settings`

**Type**: `dict`

**Description**: Stores project settings loaded from `src/settings.json`. The settings are loaded from the `src` directory under the root directory, identified by the __root__ variable.


### `__project_name__`

**Type**: `str`

**Description**: Project name, retrieved from `settings.json` or defaults to "hypotez".


### `__version__`

**Type**: `str`

**Description**: Project version, retrieved from `settings.json` or defaults to an empty string.


### `__doc__`

**Type**: `str`

**Description**: Project documentation, read from `src/README.MD` or defaults to an empty string.



### `__details__`

**Type**: `str`

**Description**: Project details, currently an empty string.


### `__author__`

**Type**: `str`

**Description**: Author's name, retrieved from `settings.json` or defaults to an empty string.


### `__copyright__`

**Type**: `str`

**Description**: Copyright information, retrieved from `settings.json` or defaults to an empty string.


### `__cofee__`

**Type**: `str`

**Description**: A link for coffee support, retrieved from `settings.json` or defaults to a predefined link.

## Error Handling

The module uses `try...except` blocks to handle potential errors:

- `FileNotFoundError`: Catches the case where `settings.json` or `README.MD` is not found.
- `json.JSONDecodeError`: Handles cases where the JSON data in `settings.json` is invalid.

In these cases, appropriate error handling or fallback mechanisms are implemented to prevent the script from crashing.

```python
...
except (FileNotFoundError, json.JSONDecodeError):
    ...
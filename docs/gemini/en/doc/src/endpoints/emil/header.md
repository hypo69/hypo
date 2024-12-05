# hypotez/src/endpoints/emil/header.py

## Overview

This module, `header.py`, provides functions for setting the project root directory and loading project settings. It leverages the `gs` module for file path manipulation and the `json` module for loading settings from a JSON file.  The module also retrieves project details, including name, version, documentation, and author information.

## Table of Contents

* [set_project_root](#set-project-root)
* [Project Settings](#project-settings)
* [Project Details](#project-details)


## Functions

### `set_project_root`

**Description**: This function finds the root directory of the project. It searches upwards from the current file's directory until it finds a directory containing any of the specified marker files (`pyproject.toml`, `requirements.txt`, `.git`). If no such directory is found, it returns the directory where the script is located.  It then adds the root directory to `sys.path`.


**Parameters**:

- `marker_files` (tuple): Filenames or directory names to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.


**Returns**:

- `Path`: Path to the root directory if found, otherwise the directory where the script is located.


**Example Usage**:

```python
root_path = set_project_root()
print(root_path)
```


### Project Settings

**Description**: This section handles loading project settings from a JSON file named `settings.json` located in the `src` directory of the project root.


**Details**:

- The `settings` variable stores the loaded settings.
- If the file is not found or is not a valid JSON file, a `...` placeholder is used to indicate the exception handling.


### Project Details

**Description**: This section retrieves project details, including the project name, version, documentation, author, copyright, and a coffee link, from the loaded settings or defaults.

**Details**:

- It retrieves values from the `settings` dictionary using `settings.get()`.  If `settings` is `None`, default values are used.
- The documentation string (`__doc__`) is retrieved if available; otherwise, it defaults to an empty string.
- The coffee link is extracted, or defaults to a predefined link.
- This section sets several variables like `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, and `__cofee__`.


**Example Usage**:

```python
print(__project_name__)
print(__version__)
```


```python
print(__doc__)  # Prints project documentation if available
```


```python
print(__cofee__) # Prints the coffee link
```
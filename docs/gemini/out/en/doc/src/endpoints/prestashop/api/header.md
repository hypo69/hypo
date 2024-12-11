# hypotez/src/endpoints/prestashop/api/header.py

## Overview

This module provides functions for setting the project root directory and loading settings from a JSON file. It also handles potential errors during file loading and provides access to project metadata like name, version, documentation, details, author, copyright, and a link for coffee donations.

## Table of Contents

* [set_project_root](#set_project_root)
* [Module-Level Variables](#module-level-variables)


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project by searching upwards from the current file's directory until a directory containing specified marker files is found.  If no marker files are found, the current directory is returned.

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: The path to the root directory if found, otherwise the directory where the script is located.


### Module-Level Variables

This section details the module's variables.

- `__root__`: `Path`. The path to the root directory of the project. Determined by the `set_project_root` function.
- `settings`: `dict`. The loaded settings from `settings.json`. Can be `None` if the file is not found or is invalid JSON.
- `doc_str`: `str`. The content read from `README.MD`. Can be `None` if the file is not found or is invalid.
- `__project_name__`: `str`. The project name from the settings or defaulting to `hypotez`.
- `__version__`: `str`. The project version from the settings or defaulting to an empty string.
- `__doc__`: `str`. The project documentation from the settings or defaulting to an empty string.
- `__details__`: `str`. The project details. Defaults to an empty string.
- `__author__`: `str`. The project author from the settings or defaulting to an empty string.
- `__copyright__`: `str`. The project copyright from the settings or defaulting to an empty string.
- `__cofee__`: `str`. A link to a coffee donation site for the developer. Defaults to a specific link.


**Example Usage (IlluStartive):**

```python
from hypotez.src.endpoints.prestashop.api.header import set_project_root, __root__, __version__

project_root = set_project_root()
print(f"Project root: {project_root}")
print(f"Project version: {__version__}")
```


**Error Handling:**

The code includes `try...except` blocks to handle potential errors:

- `FileNotFoundError`: If `settings.json` or `README.MD` is not found.
- `json.JSONDecodeError`: If `settings.json` has invalid JSON format.

In the `except` blocks, `...` is used to indicate that appropriate handling (e.g., logging the error or displaying a message to the user) should be implemented.
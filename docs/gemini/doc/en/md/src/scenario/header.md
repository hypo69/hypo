# hypotez/src/scenario/header.py

## Overview

This module, `header.py`, defines functions for setting the project root directory and loading project settings from a JSON file.  It also retrieves documentation from a README.md file. The module handles potential exceptions during file loading.

## Table of Contents

* [set_project_root](#set-project-root)
* [Module Variables](#module-variables)


## Functions

### `set_project_root`

**Description**: This function determines the root directory of the project. It starts from the current file's directory and searches upwards for directories containing specified marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`). If found, the function returns the path to the root directory. Otherwise, it returns the directory where the script is located. It also adds the root directory to `sys.path` to allow import of other modules.

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names used to identify the project root.  Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: The path to the project root directory. Returns the directory of the script if no marker files are found.


## Module Variables

These variables store project information, obtained from the `settings.json` file if it exists and is valid, or have default values.

- `__root__` (Path): The determined path to the project root directory. Initialized from the `set_project_root` function.
- `settings` (dict): A dictionary containing project settings.  Loaded from `src/settings.json` if the file exists and the JSON is valid. Defaults to `None`.
- `doc_str` (str): The content of the `README.MD` file located in the project root.  Defaults to `None`.
- `__project_name__` (str): Project name, obtained from `settings`, defaulting to 'hypotez'.
- `__version__` (str): Project version, obtained from `settings`, defaulting to an empty string.
- `__doc__` (str): Project documentation string, obtained from `README.MD` if available; defaults to an empty string.
- `__details__` (str): Project details, obtained from `settings`, defaulting to an empty string.
- `__author__` (str): Author of the project, obtained from `settings`, defaulting to an empty string.
- `__copyright__` (str): Copyright information, obtained from `settings`, defaulting to an empty string.
- `__cofee__` (str): A link to support the author via coffee, obtained from `settings` , defaulting to a predefined link.

**Raises**:

- `FileNotFoundError`: Raised if `settings.json` or `README.MD` is not found.
- `json.JSONDecodeError`: Raised if `settings.json` cannot be parsed as valid JSON.
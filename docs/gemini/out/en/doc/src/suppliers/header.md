# hypotez/src/suppliers/header.py

## Overview

This module provides functions for setting the project root directory and loading project settings. It also handles potential errors during file loading and configuration retrieval.


## Functions

### `set_project_root`

**Description**: This function finds the root directory of the project by searching upwards from the current file's location until it finds a directory containing specific marker files (e.g., `pyproject.toml`, `requirements.txt`, `.git`).

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names used to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:

- `Path`: The path to the root directory if found, otherwise the directory where the script is located.

**Raises**:

-  No exceptions are explicitly raised.


### `__doc__`

**Description**:

Docstring for the `__doc__` variable, although there isn't a function definition. This variable holds the content of the 'README.MD' file if found, or an empty string otherwise.

**Parameters**: None

**Returns**:

- `str`: The content of the README.MD file if it exists; otherwise, an empty string.


### `__root__`

**Description**:

Docstring for the `__root__` variable. This variable stores the path to the root directory of the project, obtained by calling the `set_project_root` function.


**Parameters**: None


**Returns**:

- `Path`: The path to the root directory of the project.


### `settings`

**Description**:

Docstring for the `settings` variable. This variable holds the loaded JSON data from the 'settings.json' file in the project's root directory.

**Parameters**: None


**Returns**:

- `dict`: The loaded JSON data if the file is found and valid; otherwise, `None`.

**Raises**:

- `FileNotFoundError`: Raised if the 'settings.json' file is not found.
- `json.JSONDecodeError`: Raised if the 'settings.json' file exists but cannot be parsed as valid JSON.

### `__project_name__`

**Description**:

Docstring for the `__project_name__` variable. This variable holds the project name, obtained from the 'settings.json' file (or 'hypotez' if not found).

**Parameters**: None

**Returns**:

- `str`: The project name.


### `__version__`

**Description**:

Docstring for the `__version__` variable. This variable holds the project version, obtained from the 'settings.json' file (or empty string if not found).

**Parameters**: None

**Returns**:

- `str`: The project version.


### `__details__`

**Description**:

Docstring for the `__details__` variable. This variable holds project details, which is initialized as an empty string.


**Parameters**: None

**Returns**:

- `str`: Project details.


### `__author__`

**Description**:

Docstring for the `__author__` variable. This variable holds the author information, obtained from the 'settings.json' file (or an empty string if not found).

**Parameters**: None

**Returns**:

- `str`: The project author.


### `__copyright__`

**Description**:

Docstring for the `__copyright__` variable. This variable holds the copyright information, obtained from the 'settings.json' file (or an empty string if not found).


**Parameters**: None

**Returns**:

- `str`: The project copyright.



### `__cofee__`

**Description**:

Docstring for the `__cofee__` variable. This variable holds a coffee link for supporting the developer, if found in 'settings.json', otherwise defaults to a predefined link.


**Parameters**: None

**Returns**:

- `str`: The coffee link.
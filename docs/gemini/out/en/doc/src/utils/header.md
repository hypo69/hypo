# hypotez/src/logger/header.py

## Overview

This module defines the root path of the project.  All imports are constructed relative to this path.  Future versions will likely move this path into a system variable.


## Functions

### `set_project_root`

**Description**: Finds the root directory of the project by searching upwards from the current file's directory until a directory containing any of the specified marker files is found.

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names to use as markers to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.


**Returns**:

- `Path`: The path to the root directory if found, otherwise the directory where the script is located.


**Raises**:

- None


## Variables

### `__root__`

**Description**: The root path of the project, set by the `set_project_root` function.

**Type**: `Path`


### `settings`

**Description**: Project settings loaded from `src/settings.json`.

**Type**: `dict` or `None`

**Details**: This variable contains project settings, loaded from a JSON file. If the file is not found or is invalid JSON, it will be `None`.

### `doc_str`

**Description**: Content of the README.MD file from the project root.

**Type**: `str` or `None`

**Details**: Reads the contents of the `README.MD` file if it exists, otherwise is `None`.

### `__project_name__`

**Description**: The project name, obtained from the `settings` or defaulting to 'hypotez'.

**Type**: `str`


### `__version__`

**Description**: The project version, obtained from the `settings` or defaulting to an empty string.

**Type**: `str`


### `__doc__`

**Description**: The project documentation string from README.MD, defaults to an empty string.

**Type**: `str`


### `__details__`

**Description**:  Empty string; currently no details are stored.

**Type**: `str`


### `__author__`

**Description**: The project author, obtained from the `settings` or defaulting to an empty string.

**Type**: `str`


### `__copyright__`

**Description**: The project copyright, obtained from the `settings` or defaulting to an empty string.

**Type**: `str`


### `__cofee__`

**Description**: A string containing a link to a boosty.to page for supporting the developer with a cup of coffee.

**Type**: `str`

**Details**: This variable contains a message about how to support the developer, with the URL defaulting to `https://boosty.to/hypo69`.
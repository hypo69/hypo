# hypotez/src/templates/version.py

## Overview

This module defines constants for the project's mode, name, version, and other details. It attempts to load settings from a `settings.json` file in the parent directory.

## Variables

### `MODE`

**Description**: A string representing the development mode.  Currently set to 'dev'.

### `settings`

**Description**: A dictionary containing project settings.  Loaded from `../settings.json`.  Defaults to `None` if the file doesn't exist or is not valid JSON.

### `__project_name__`

**Description**: The project name.  Defaults to 'hypotez' if `settings.json` is not found or doesn't contain a 'project_name' key.

### `__version__`

**Description**: The project version.  Defaults to an empty string if `settings.json` is not found or doesn't contain a 'version' key.


### `__doc__`

**Description**: The project documentation.  Defaults to an empty string.

### `__details__`

**Description**: The project details. Defaults to an empty string.

### `__author__`

**Description**: The author of the project.  Defaults to an empty string if `settings.json` is not found or doesn't contain an 'author' key.

### `__copyright__`

**Description**: The copyright information. Defaults to an empty string if `settings.json` is not found or doesn't contain a 'copyright' key.

### `__cofee__`

**Description**: A string containing a link for donating coffee to the developer. Defaults to a default link if `settings.json` is not found or doesn't contain a 'cofee' key.


## Functions

### `load_settings`

**Description**:  This function is not explicitly defined in the code, but is implied by the `try...except` block.  It attempts to load project settings from the `settings.json` file into the `settings` variable.


**Raises**:
- `FileNotFoundError`: If the `../settings.json` file is not found.
- `json.JSONDecodeError`: If the `settings.json` file is not valid JSON.
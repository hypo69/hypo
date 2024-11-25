# hypotez/src/suppliers/bangood/header.py

## Overview

This module provides functionality for obtaining and utilizing project settings, including the project root directory, version information, and documentation. It leverages the `gs` module for path manipulation and reads settings from a JSON file. The module also attempts to read documentation from a README.md file.

## Table of Contents

- [set_project_root](#set-project-root)
- [Project Settings](#project-settings)
- [Global Variables](#global-variables)

## Functions

### `set_project_root`

**Description**: This function determines the root directory of the project. It searches upward from the current file's directory until it finds a directory containing any of the specified marker files (pyproject.toml, requirements.txt, .git).

**Parameters**:
- `marker_files` (tuple): A tuple of filenames or directory names to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:
- `Path`: The path to the root directory of the project if found, otherwise the directory where the script is located.

**Raises**:
- None


### Project Settings

**Description**: This section outlines the handling of project settings. The script attempts to load settings from a JSON file (`settings.json`) located within the project root.

**Details**:
- If `settings.json` is found and parsed successfully, the loaded settings are stored in the `settings` variable.
- If `settings.json` is not found or cannot be parsed, `settings` is set to `None`.

### Global Variables

**Description**: This section describes the global variables defined in this module, which are derived from project settings and the README.MD file.

**Variables**:
- `__root__` (Path): Path to the root directory of the project, determined by the `set_project_root` function.
- `settings` (dict | None): Dictionary containing project settings (loaded from `settings.json`) or None if the file is not found or cannot be parsed.
- `__project_name__` (str): Name of the project, obtained from the settings or defaults to 'hypotez'.
- `__version__` (str): Version of the project, obtained from the settings or defaults to an empty string.
- `__doc__` (str): Project documentation, obtained from `README.MD` or defaults to an empty string.
- `__details__` (str): Project details (currently empty).
- `__author__` (str): Author of the project, obtained from the settings or defaults to an empty string.
- `__copyright__` (str): Copyright information of the project, obtained from the settings or defaults to an empty string.
- `__cofee__` (str): Link to a tip jar or similar donation platform, obtained from the settings or defaults to a default value.

**Note**: The `try...except` blocks handle potential `FileNotFoundError` and `json.JSONDecodeError` exceptions during file reading. The `...` in the exception blocks indicates that the corresponding errors are simply ignored and no action is taken.
# src.suppliers.visualdg.header

## Overview

This module contains functions for setting the project root directory and retrieving project settings and documentation.  It utilizes the `gs` module and leverages the `settings.json` and `README.MD` files for configuration and documentation.

## Table of Contents

* [set_project_root](#set-project-root)
* [Project Settings](#project-settings)
* [Project Documentation](#project-documentation)


## Functions

### `set_project_root`

**Description**: This function finds the root directory of the project. It searches upwards from the current file's directory until it encounters a directory containing one of the specified marker files (`pyproject.toml`, `requirements.txt`, `.git`). If no such directory is found, the current file's directory is returned.

**Parameters**:

* `marker_files` (tuple): A tuple of filenames or directory names to identify the project root. Defaults to (`'pyproject.toml'`, `'requirements.txt'`, `'.git'`).


**Returns**:

* `Path`: The path to the root directory of the project.

**Raises**:
* None


### Project Settings

**Description**: This section details the retrieval of project settings from the `settings.json` file located in the `src` directory relative to the project root.

**Parameters**:

* None


**Returns**:
* `dict`: A dictionary containing the project settings. Returns `None` if the file does not exist or contains invalid JSON.


**Raises**:

* `FileNotFoundError`: If `settings.json` is not found.
* `json.JSONDecodeError`: If `settings.json` contains invalid JSON.

### Project Documentation

**Description**: This section explains the retrieval of project documentation from the `README.MD` file located in the `src` directory relative to the project root.

**Parameters**:

* None


**Returns**:
* `str`: The content of the `README.MD` file as a string. Returns `None` if the file does not exist or any error occurs during reading.


**Raises**:

* `FileNotFoundError`: If `README.MD` is not found.
* `json.JSONDecodeError`: If there's an issue decoding the content of the file.
# Module: hypotez/src/utils/_examples/get_relative_path.py

## Overview

This module demonStartes the usage of the `get_relative_path` function from the `src.utils.path` module to obtain the relative path of a file within a project. It leverages the `pathlib` module for path manipulation.  The script prints the calculated relative path to the console.

## Table of Contents

* [Functions](#functions)


## Functions

### `get_relative_path`

**Description**: Calculates the relative path between two given paths.

**Parameters**:
- `path1` (Path): The absolute path to the source file.
- `path2` (str): The absolute path to the target directory.

**Returns**:
- str: The relative path between the source file and the target directory, or `None` if the calculation fails.

**Raises**:
- None


### `main`


**Description**: The main function of the script, which demonStartes the usage of `get_relative_path`.

**Parameters**:
- None


**Returns**:
- None
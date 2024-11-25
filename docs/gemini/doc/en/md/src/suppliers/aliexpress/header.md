# hypotez/src/suppliers/aliexpress/header.py

## Overview

This module defines functions for setting the project root directory and loading project settings from a JSON file. It also handles potential errors like file not found and invalid JSON format.  The module utilizes the `gs` module for path manipulation and relies on a `settings.json` file within the project root for configuration.

## Table of Contents

- [set_project_root](#set-project-root)
- [Project Configuration](#project-configuration)


## Functions

### `set_project_root`

**Description**: This function determines the root directory of the project by searching upwards from the current file's location.  It checks for specific marker files (`pyproject.toml`, `requirements.txt`, `.git`) to identify the project root.

**Parameters**:

- `marker_files` (tuple): A tuple of filenames or directory names used to identify the project root. Defaults to (`'pyproject.toml'`, `'requirements.txt'`, `.git`).


**Returns**:

- `Path`: The path to the project root directory. If no marker files are found, it returns the directory where the script is located.


**Raises**:

- None


### Project Configuration

**Description**: This section describes the logic for loading project settings from `settings.json`.


**Variables**:

- `settings`:  A dictionary containing project settings loaded from `settings.json`. If `settings.json` is not found or contains invalid JSON, `settings` will be `None`.

- `doc_str`: A string containing the content of the `README.MD` file. If `README.MD` is not found, `doc_str` will be `None`.


**Code Snippets**
```python
config:dict = None
try:
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        config = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    ...
```

```python
doc_str:str = None
try:
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError):
    ...
```


**Variables used for Project Metadata**:

- `__project_name__`
- `__version__`
- `__doc__`
- `__details__`
- `__author__`
- `__copyright__`
- `__cofee__`


These variables are populated using data from the `settings` dictionary, with fallback values provided if `settings` is `None` or if a particular key is missing.

```python
__project_name__ = config.get("project_name", 'hypotez') if config else 'hypotez'
__version__: str = config.get("version", '')  if config else ''
__doc__: str = doc_str if doc_str else ''
__details__: str = ''
__author__: str = config.get("author", '')  if config else ''
__copyright__: str = config.get("copyrihgnt", '')  if config else ''
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
```


```
```
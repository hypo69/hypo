# hypotez/src/utils/_examples/get_relative_path.py

## Overview

This module demonstrates how to get the relative path from a given file path to a specified target directory. It utilizes the `get_relative_path` function from the `src.utils.path` module.

## Table of Contents

- [Overview](#overview)
- [Functions](#functions)
    - [`get_relative_path`](#get_relative_path)

## Functions

### `get_relative_path`

**Description**: This function calculates the relative path from a given file path to a target directory.

**Parameters**:

- `base_path` (Path): The absolute path of the file for which the relative path should be calculated.
- `target_path` (str): The absolute path of the target directory.

**Returns**:

- `Path`: The relative path from `base_path` to `target_path`.  Returns `None` if the relative path cannot be determined.


**Example Usage (within the module):**

```python
relative_path = get_relative_path(Path(__file__).resolve(), 'hypotez')
print(relative_path)
```


```python
def get_relative_path(base_path: Path, target_path: str) -> Path | None:
    """
    Args:
        base_path (Path): The absolute path of the file for which the relative path should be calculated.
        target_path (str): The absolute path of the target directory.

    Returns:
        Path: The relative path from base_path to target_path. Returns None if the relative path cannot be determined.
    
    """
    try:
        return base_path.relative_to(Path(target_path))
    except ValueError:
        return None
```


```python
# Example Usage (within the module):
relative_path = get_relative_path(Path(__file__).resolve(), 'hypotez')
print(relative_path)
```
```
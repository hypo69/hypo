# hypotez/src/utils/path.py

## Overview

This module defines the root path to the project. All imports are constructed relative to this path.

## Variables

### `MODE`

**Description**:  Specifies the development mode ('dev').

### Functions

### `get_relative_path`

**Description**: Returns the portion of a path starting from a specified segment to the end.

**Parameters**:

- `full_path` (str): The full path.
- `relative_from` (str): The path segment to start extraction from.

**Returns**:

- `Optional[str]`: The relative path starting from `relative_from`, or `None` if the segment is not found.

**Examples**:
```python
# Example usage (assuming 'full_path' is '/path/to/project/file.txt' and 'relative_from' is 'project')
relative_path = get_relative_path('/path/to/project/file.txt', 'project')
print(relative_path)  # Output: file.txt

relative_path = get_relative_path('/path/to/project/file.txt', 'nonexistent')
print(relative_path) # Output: None
```

**Implementation Details**:

1. Converts the input strings to `Path` objects.
2. Extracts the parts of the path.
3. Finds the index of the `relative_from` segment in the parts list.
4. If found, constructs a new `Path` object from the segment onwards.
5. Returns the `as_posix()` representation of the relative path, or `None` if the segment is not found.


## Classes

(No classes defined in this file)
# hypotez/src/utils/path.py

## Overview

This module defines the root path to the project. All imports are built relative to this path.  Future versions will likely move this functionality to system environment variables.

## Functions

### `get_relative_path`

**Description**: Returns the part of the path from a specified segment to the end.

**Parameters**:
- `full_path` (str): The full path.
- `relative_from` (str): The segment of the path from which extraction should begin.

**Returns**:
- `Optional[str]`: The relative path starting from `relative_from`, or `None` if the segment is not found.

**Raises**:
- `TypeError`: If input `full_path` or `relative_from` are not strings.
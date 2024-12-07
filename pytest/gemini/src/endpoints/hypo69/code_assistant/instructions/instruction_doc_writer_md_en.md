# Instruction Doc Writer

## Overview

This module provides functions for generating documentation for Python code in Markdown format.  It includes functionalities for creating detailed documentation for classes and functions, complete with parameter descriptions, return values, and exception handling.  The documentation also includes a table of contents.

## Functions

### `generate_documentation`

**Description**: This function takes a Python file path as input and generates the corresponding documentation in Markdown format.

**Parameters**:

- `filepath` (str): The path to the Python file to be documented.


**Returns**:

- str: The generated Markdown documentation string.

**Raises**:

- `FileNotFoundError`: If the input file does not exist.
- `Exception`: For any other errors during the documentation generation process.
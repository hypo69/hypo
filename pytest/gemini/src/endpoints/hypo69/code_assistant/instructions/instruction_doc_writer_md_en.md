# Instruction Doc Writer

## Overview

This module provides a function for generating documentation in Markdown format for Python code.  The generated documentation includes detailed descriptions of classes, functions, and methods, complete with parameters, return values, and exception handling information.  It adheres to specified formatting and includes a table of contents for navigation.


## Functions

### `generate_documentation`

**Description**: This function takes a Python file path as input and generates corresponding Markdown documentation.

**Parameters**:

- `filepath` (str): The path to the Python file to document.

**Returns**:

- str: The generated Markdown documentation string.

**Raises**:

- `FileNotFoundError`: If the input `filepath` does not exist.
- `TypeError`: If the input is not a string.
- `Exception`: For any other unexpected errors during the documentation generation process.
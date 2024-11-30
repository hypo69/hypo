# Instruction Doc Writer

## Overview

This module provides a function for generating documentation in Markdown format for Python code. It ensures proper formatting, including headers, descriptions, parameters, return values, and exceptions.

## Table of Contents

- [Overview](#overview)
- [Functions](#functions)
- [Example Usage](#example-usage)


## Functions

### `generate_documentation`

**Description**: This function takes Python code as input and generates its corresponding Markdown documentation.

**Parameters**:
- `code` (str): The Python code to generate documentation for.

**Returns**:
- str: The generated Markdown documentation.

**Raises**:
- `TypeError`: If the input `code` is not a string.
- `ValueError`: If the provided code is invalid Python.


## Example Usage

```python
import instruction_doc_writer

code_snippet = """
def greet(name: str) -> str:
    """
    Greets the given name.

    Args:
        name (str): The name to greet.

    Returns:
        str: The greeting message.
    """
    return f"Hello, {name}!"
"""

markdown_doc = instruction_doc_writer.generate_documentation(code_snippet)
print(markdown_doc)

```
```python
# Example output (will vary based on exact input)
# # Module Name
#
# ## Overview
#
# This module provides a function for generating documentation in Markdown format for Python code. It ensures proper formatting, including headers, descriptions, parameters, return values, and exceptions.
#
# ## Functions
#
# ### `greet`
#
# **Description**: Greets the given name.
#
# **Parameters**:
# - `name` (str): The name to greet.
#
# **Returns**:
# - `str`: The greeting message.
```
```python
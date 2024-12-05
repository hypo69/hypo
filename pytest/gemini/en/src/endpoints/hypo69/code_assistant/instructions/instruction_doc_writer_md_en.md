# Instruction Doc Writer

## Overview

This module provides functionality for generating documentation for Python code in Markdown format, adhering to specific formatting guidelines.  It includes methods for creating documentation headers, class descriptions, function signatures, and parameter/return/exception details.

## Table of Contents

* [Overview](#overview)
* [Classes](#classes)
* [Functions](#functions)


## Classes


### `InstructionDocWriter`

**Description**: This class encapsulates the logic for generating documentation in Markdown format.

**Methods**:

- `generate_docstring(func):`
    - **Description**: Generates a docstring in the specified format.
    - **Parameters**:
        - `func` (function): The function for which to generate the docstring.
    - **Returns**:
        - `str`: The generated docstring.

- `generate_markdown(code_text):`
    - **Description**: Generates markdown documentation for provided code.
    - **Parameters**:
        - `code_text` (str): The Python code to be documented.
    - **Returns**:
        - `str`: The generated Markdown documentation.

## Functions

### `generate_docstring`

**Description**: Creates a formatted docstring based on the provided function signature.

**Parameters**:

- `func` (function): The Python function to extract information from.


**Returns**:

- `str`:  The formatted docstring in Markdown.

**Raises**:

- `TypeError`: If input `func` is not a function.
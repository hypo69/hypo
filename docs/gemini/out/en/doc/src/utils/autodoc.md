# src.utils.autodoc

## Overview

This module provides a decorator `autodoc` that automatically updates a function's docstring with the timestamp of its last call.  This decorator is designed to dynamically update function documentation with the time of the last execution, making it useful for logging and tracking function usage.

## Functions

### `autodoc`

**Description**: This decorator updates the docstring of a function with the current timestamp after each call.

**Parameters**:
- `func` (callable): The function to be decorated.

**Returns**:
- `wrapper` (callable): The wrapped function, which updates the docstring before calling the original function.

**Raises**:
None.


### `update_docstring`

**Description**: Updates the docstring of a given function with the current timestamp.

**Parameters**:
- `func` (callable): The function whose docstring needs to be updated.

**Returns**:
None.

**Raises**:
None.


### `example_function`

**Description**: An example function demonstrating the `autodoc` decorator.  It prints a message indicating the input parameters and updates its docstring with the last call timestamp.

**Parameters**:
- `param1` (int): The first input parameter.
- `param2` (str): The second input parameter.

**Returns**:
None.

**Raises**:
None.


## Usage Examples

The provided example code demonstrates how to use the `autodoc` decorator.  Calling `example_function` multiple times will result in the docstring being updated with the timestamp of each invocation, effectively tracking usage.
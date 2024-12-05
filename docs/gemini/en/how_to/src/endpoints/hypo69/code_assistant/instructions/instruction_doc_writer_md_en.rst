# How to Generate Python Code Documentation

## Overview

This document outlines the instructions for generating Markdown documentation for Python code.  It details the required format, including header structure, class and function documentation, table of contents (TOC), and example file structure.

## Instructions

1. **File Structure:**
   - Each Python file should have a corresponding Markdown file with the same name but a `.md` extension.
   - The Markdown file should begin with a header that corresponds to the Python file's name and a concise description.

2. **Python Code Comments:**
   - All classes and functions in the Python code should use docstrings in the specified format:
     ```python
     def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:
         """
         Args:
             param (str): Description of the `param` parameter.
             param1 (Optional[str | dict | str], optional): Description of the `param1` parameter. Defaults to `None`.

         Returns:
             dict | None: Description of the return value. Returns a dictionary or `None`.

         Raises:
             SomeError: Description of the situation in which the `SomeError` exception is raised.
         """
         # ... function body ...
     ```
   - Use `ex` instead of `e` in exception handling blocks.  For example, `try...except SomeException as ex:`

3. **Table of Contents (TOC):**
   - Each Markdown file should begin with a table of contents (TOC) section.
   - Links within the TOC should point to the relevant sections for classes, functions, etc., as in the example below.

4. **Formatting:**
   -  Use proper Markdown syntax for headers, lists, and links.
   -  For classes, functions, and methods, include sections for descriptions, parameters, return values, and raised exceptions.  Use the following format as an example:
     ```markdown
     ## Functions

     ### `function_name`

     **Description**: Brief description of the function.

     **Parameters**:
     - `param` (str): Description of the `param` parameter.
     - `param1` (Optional[str | dict | str], optional): Description of the `param1` parameter. Defaults to `None`.

     **Returns**:
     - `dict | None`: Description of the return value.

     **Raises**:
     - `SomeError`: Description of the situation in which the `SomeError` exception is raised.
     ```

5. **Example Markdown File:**

```markdown
# MyPythonModule

## Overview

This module provides functions for working with data.

## Classes

### `MyClass`

**Description**: A class for managing data.

**Methods**:
- `my_method`: Processes data and returns results.


## Functions

### `my_function`

**Description**: Retrieves data from a source.

**Parameters**:
- `source_url` (str): The URL of the data source.
- `params` (Optional[dict], optional): Additional parameters for the request. Defaults to `None`.

**Returns**:
- `list[dict]`: A list of dictionaries containing the data.

**Raises**:
- `HTTPError`: If there is an error communicating with the server.
- `ValueError`: If the data format is invalid.


## Classes

### `MyOtherClass`

**Description**: Another class for data processing.

**Methods**:
- `other_method`: Displays data in the console.

## Table of Contents

[Overview](#overview)
[Classes](#classes)
[Functions](#functions)
[MyClass](#myclass)
[MyOtherClass](#myotherclass)
[my_function](#myfunction)
```

This structured approach ensures consistent and informative documentation for your Python code.
```
# INSTRUCTION DOCUMENTATION

## Overview

This document outlines the format for generating Markdown documentation from Python files.  The generated documentation should be comprehensive and easily digestible, including a table of contents for navigation, clear descriptions, parameter and return value details, and exception handling specifications.  All examples provided should be followed meticulously, ensuring consistency in formatting and structure across all generated files.


## Documentation Structure


### File Structure

Each documentation file should adhere to the following structure:

1.  **Header:** A top-level header (`#`) providing the name of the module or file.
2.  **Overview:** A brief description of the module's purpose or file contents.
3.  **Table of Contents (TOC):** A well-structured list of links to all major sections, enabling quick navigation within the documentation.
4.  **Classes:**  A section listing all classes present in the file, including detailed descriptions and method documentation.
5.  **Functions:** A section documenting all functions, including descriptions, parameters, return values, and potential exceptions raised.

### Class Documentation

Each class documented should include a description and a list of methods associated with the class.

- **`ClassName`**
- **Description:** A clear and concise description of the class's purpose.
- **Methods:** A list of methods belonging to the class. Each method should have a brief description.


### Function Documentation

Each function documented should adhere to the following format for a function named `function_name`:

- **`function_name`**
- **Description**: A concise description of the function's purpose.
- **Parameters**: A list of parameters with their types and descriptions. Use the `param` or `param1` format for parameter names and specify data types (e.g., `str`, `int`, `Optional[str]`).
- **Returns**: A description of the function's return value, including its type (e.g., `dict`, `str`, `None`).
- **Raises**: A list of potential exceptions that might be raised and the associated error conditions.  Use the `SomeError` format for exception names and a detailed description.

### Exception Handling

Always use `ex` instead of `e` in `try...except` blocks in the Python code being documented.

### Examples

The following examples illustrate the expected format for classes, functions, and exception handling:

```python
# Example of a Python class and function
class MyClass:
    def my_method(self, param: str) -> str:
        """
        Args:
            param (str): Description of the param parameter.

        Returns:
            str: Description of the return value.
        """
        return param
```

```python
# Example of documentation format for a function
def my_function(param: str, param1: Optional[str] = None) -> dict | None:
    """
    Args:
        param (str): Description of the param parameter.
        param1 (Optional[str], optional): Description of the param1 parameter. Defaults to None.

    Returns:
        dict | None: Description of the return value. Returns a dictionary or None.

    Raises:
        ValueError: Description of the situation in which the ValueError exception is raised.
    """
    return {'key': param}
```

```python
# Example of a try...except block using ex
try:
    # some code
    result = my_function("hello")
except ValueError as ex:
    print(f"An error occurred: {ex}")
```


### Markdown Syntax

All headers, lists, and links should use proper Markdown syntax to ensure clarity and readability.


## TOC Example

```
[Table of Contents](#table-of-contents)

* [Overview](#overview)
* [Classes](#classes)
  * [`MyClass`](#myclass)
    * [`my_method`](#mymethod)
* [Functions](#functions)
  * [`my_function`](#myfunction)
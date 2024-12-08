# Code Assistant Instructions

## Overview

This module provides instructions for processing code within the project using a model.  It outlines the expected format and structure for input Python files to facilitate accurate and efficient code analysis and generation by the model.  Details on handling various code elements, such as classes, functions, and exception handling, are provided.


## Instructions

The model expects Python code files conforming to the following guidelines:


*   **Python Code Format:** Input Python code should be well-formatted and adhere to standard Python coding conventions.
*   **Docstrings:**  All functions and classes should have comprehensive docstrings using the specified format:

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
    # Function body
```

*   **Exception Handling:**  Exception handling blocks should use `ex` instead of `e`:

```python
try:
    # Code that might raise an exception
ex:
    # Error handling block
```

*   **Input Validation:**  Include input validation to handle potential errors or unexpected data.  Example: Validate data types, check for null values, and ensure input values are within expected ranges.
*   **Clear Variable Names:** Use descriptive variable names to enhance code readability and maintainability.
*   **Comments:**  Add comments to explain complex logic, algorithms, or non-obvious code sections.


##  Example

```python
def calculate_area(length: float, width: float) -> float:
    """
    Calculates the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.

    Raises:
        ValueError: If either length or width is negative.
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative values.")
    return length * width
```

These instructions will help the model to process the project code effectively.
# Code Assistant Instructions Explainer

## Overview

This document provides instructions for creating Markdown documentation for Python code, focusing on clarity, structure, and completeness.  It details the expected format, including headers, descriptions, parameter specifications, return values, exceptions, and a table of contents. The documentation aims to fully explain the code's functionality, dependencies, and relationships within the project.

## Instructions

### 1. Documentation Format

- Use Markdown (.md) format.
- Each Python file starts with a header and a brief description.
- Class and function documentation utilizes a specific format for clarity:

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

- Use `ex` instead of `e` in exception blocks.

### 2. Table of Contents (TOC)

- Every documentation file begins with a TOC.
- The TOC links to all significant sections (e.g., Classes, Functions, Overview).

### 3. Documentation Formatting

- Use appropriate Markdown headers, lists, and links.
- Class, function, and method documentation sections should include a concise description, parameters, return values, and exceptions.  Example:

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

### 4. Section Headings

- Use consistent header levels (1, 2, 3, 4).

### 5. Example Structure

```markdown
# Module Name

## Overview

Brief description of the module's purpose.

## Classes

### `ClassName`

**Description**: Brief description of the class.

**Methods**:
- `method_name`: Brief description of the method.

## Functions

### `function_name`

**Description**: Brief description of the function.

**Parameters**:
- `param` (str): Description of the `param` parameter.


# Example Input Python Code

## Example Analysis of Python Code


```


```


```
```
```
```


```

```


```


```
```


```

```


```
```
```

```

```
```

This is a template for generating documentation.  Provide the Python code you want documented, and I will generate the Markdown output following these guidelines.
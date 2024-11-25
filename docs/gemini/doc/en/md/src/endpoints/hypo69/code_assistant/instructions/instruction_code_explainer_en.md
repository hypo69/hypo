# Code Assistant Instructions Documentation

## Overview

This document provides instructions for generating Markdown documentation for Python code files.  The generated documentation will include a comprehensive overview, class and function descriptions, detailed parameter and return value explanations, and a table of contents for easy navigation.

## Instructions

The following format is required for each Python file:

### 1. File Header and Description

Each file must begin with a header and a brief description of its contents.

```markdown
# Module Name

## Overview

Brief description of the module's purpose.  Include context and high-level functionality.
```

### 2. Table of Contents

A table of contents should be included at the beginning of each file to aid in navigation.

```markdown
## Table of Contents

- [Overview](#overview)
- [Classes](#classes)
    - [`ClassName`](#classname)
- [Functions](#functions)
    - [`function_name`](#function_name)
```


### 3. Class and Function Documentation

All classes and functions should be documented using the provided Python comment format, including detailed descriptions, parameters, return values, and potential exceptions.

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
    pass
```

```markdown
## Classes

### `ClassName`

**Description**: Brief description of the class.


**Methods**:

- `method_name`: Description of the method.  Include parameters, return values, and exceptions.


## Functions

### `function_name`

**Description**: Description of the function.

**Parameters**:
- `param` (type): Description of the `param` parameter.
- `param2` (type): Description of the `param2` parameter.

**Returns**:
- `return_type`: Description of the return value.

**Raises**:
- `ExceptionType`: Description of the situation in which the exception is raised.

```

### 4. Markdown Formatting

Use proper Markdown syntax for all headers, lists, and links.  Avoid excessive use of bolding; use it for emphasis only.


### 5. Example File Structure


```markdown
# Data Processing Module

## Overview

This module handles data preprocessing and transformation for various analytical tasks.


## Table of Contents

- [Overview](#overview)
- [Classes](#classes)
    - [`DataProcessor`](#dataproc)
- [Functions](#functions)
    - [`transform_data`](#transformdata)



## Classes

### `DataProcessor`

**Description**: This class encapsulates the data processing logic.

**Attributes**:

- `data`: The input data (list, dict, etc.)
- `config`: Configuration parameters for processing (dict).


**Methods**:

- `preprocess_data`: Method to perform data preprocessing. Include parameters, return values, and exceptions.


## Functions

### `transform_data`

**Description**: Transforms data based on defined rules in `config`.


**Parameters**:
- `data`: The input data (list, dict).
- `config`: Configuration settings (dict).


**Returns**:
- `transformed_data`: The processed data (list, dict, etc.).


**Raises**:
- `InvalidConfigError`: Raised if `config` is invalid.



```

This comprehensive documentation format will ensure that subsequent use and understanding of the Python files are clear and efficient.
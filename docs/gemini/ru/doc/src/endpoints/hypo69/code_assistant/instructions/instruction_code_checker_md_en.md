# instruction_code_checker.md

## Overview

This module contains instructions for checking Python code and generating documentation in reStructuredText (RST) format.  It emphasizes proper commenting, error handling, and data manipulation using `j_loads` or `j_loads_ns`.

## Main Requirements

1. **Documentation Format**: Use reStructuredText (RST) for comments and docstrings.  Use single quotes (`'`) in Python code.

2. **Comment Preservation**: Preserve existing comments (`#`).  Comment out code blocks requiring changes using `#`.

3. **Data Handling**: Use `j_loads` or `j_loads_ns` from `src.utils.jjson` for file reading instead of `json.load`. Leave `...` unchanged as placeholders.

4. **Structure Analysis**: Verify and add missing imports.  Ensure function, variable, and import names are consistent with previous files.

5. **Refactoring and Enhancements**: Add RST-style docstrings. Use `from src.logger import logger` for logging.  Avoid excessive `try-except` blocks; prefer `logger.error` for error handling.  Use specific terms instead of vague words (e.g., 'get' -> 'retrieval').

6. **Response Template**: The response should include the original code, improved code, a list of changes, and the final code ready to replace the original.

7. **Final Code**: The final code block should replace the original code in the prompt.

8. **Code Examples**: Include RST documentation and improvement examples in `TODO` format.

9. **Additional Instruction**: Rewrite all comments in RST format, following Python docstring standards and the provided examples.


## Example Usage (TODO)

```python
# Example of using the logger
from src.logger import logger

def my_function(input_data):
    """
    Performs some processing on input data.

    :param input_data: The input data to process.
    :type input_data: str
    :raises ValueError: If input_data is not a string.
    :return: The processed data.
    :rtype: str
    """
    if not isinstance(input_data, str):
        logger.error("Invalid input data type.")
        raise ValueError("Input data must be a string.")
    processed_data = input_data.upper()
    return processed_data
```

## TODO

- Add examples of improved code with RST comments.
- Provide a more detailed example response structure including original code, improved code, changes, and the final code.


```
```
```python
# Example improved code (TODO):
# Replace with actual code improvements
```
```
```
```
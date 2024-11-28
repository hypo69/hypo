# instruction_code_checker_en

## Overview

This module provides instructions for code checking and documentation generation for Python files.  It focuses on improving code quality, consistency, and readability through the addition of comprehensive docstrings and error handling.

## Requirements

The following requirements must be met for each processed Python file:

* **Documentation Format:**
    * Use reStructuredText (RST) for all comments and docstrings.  Use single quotes (`'`) in Python code.
* **Comment Preservation:**
    * Preserve all existing comments after the `#` symbol without modification.
    * Comment out or modify code blocks where needed with explanations.
* **Data Handling:**
    * Use `j_loads` or `j_loads_ns` from `src.utils.jjson` for file reading instead of `json.load`.
    * Keep `...` as placeholders in the code unchanged.
* **Structure Analysis:**
    * Verify and add any missing imports.
    * Ensure consistency in function, variable, and import names.
* **Refactoring and Enhancements:**
    * Add RST-style docstrings to functions, methods, and classes.
    * Use `from src.logger import logger` for error logging.
    * Reduce reliance on standard `try-except` blocks; prioritize `logger.error` for error handling.
    * Replace vague terms (e.g., 'get', 'do') with specific actions (e.g., 'validation', 'execution').
* **Response Template:**
    * The response will contain sections for the original code, improved code, changes made, and a full optimized code block for pasting.
* **Final Code:** The response's final section contains the complete improved code ready for replacement.  Commented lines denote changes.
* **Code Examples (TODO):** Include examples of RST documentation improvements and refactoring suggestions.
* **Additional Instruction:**
    * Rewrite all comments in RST format (module descriptions, function/method/variable docstrings). Adhere to Python docstring standards.
    * Fully document all modules, functions, methods, and variables in RST format using the example provided in the instruction.


## Examples (TODO)

### Docstring Example

```python
def my_function(input_data: str, log_level: str = 'INFO') -> dict:
    """Processes input data and logs details.

    :param input_data: The input string data.
    :type input_data: str
    :param log_level: The logging level (INFO, WARNING, ERROR). Defaults to INFO.
    :type log_level: str
    :return: Processed data as a dictionary.
    :rtype: dict
    """
    try:
        # ... process input_data ...
        result = {'processed': input_data}
        logger.log(log_level, f"Processing input: {input_data}")
        return result
    except Exception as e:
        logger.error(f"Error processing input: {e}")
        return None
```

## Missing Section

This document currently lacks the necessary implementation sections to provide the output. The missing sections are:

- **Original Code:** A placeholder for the code to be documented.
- **Improved Code:** A placeholder for the code with improvements.
- **Changes Made:** A placeholder for a summary of the modifications.
- **Full Optimized Code:** A placeholder for the final, optimized code.



```
```
```
```
```
```
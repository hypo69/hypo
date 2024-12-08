How to use this code block
=========================================================================================

Description
-------------------------
This code block outlines requirements for code documentation generation in Hebrew. It specifies the format, handling of existing comments, data handling, structural analysis, improvement suggestions, and the expected output format for the generated code.  It also includes instructions on using reStructuredText (RST) for documentation and avoiding common pitfalls in code documentation.


Execution steps
-------------------------
1. **Analyze the code**: Carefully review the provided code block to understand its logic and the actions it performs. Identify sections that need changes or enhancements.
2. **Create RST documentation**:  Generate reStructuredText (RST) documentation for all functions, methods, and classes.  The documentation should follow Python documentation standards for Sphinx compatibility and include detailed descriptions, parameters, and return values.
3. **Modify the code**:  Update the Python code based on the requirements. Replace `json.load` with `j_loads` or `j_loads_ns`, add missing imports, align variable and function names with existing conventions, and implement `from src.logger import logger` for error logging.  Remove redundant `try-except` blocks, replacing them with `logger.error` handling where appropriate.
4. **Structure the response**:  The final response should be structured in three parts:
    *   **Received Code**: The original code block, unmodified.
    *   **Improved Code**: The code after adding RST documentation and making necessary modifications.
    *   **Changes Made**: A detailed list of modifications.  Each change should be clearly described.
5. **Format the response**:  Avoid starting the response with ```. Use ``` only to enclose code blocks.
6. **Final Code Output**: Include the fully improved code in a single code block, ready to be copied and pasted. Each line of code that was changed should be marked with a `#`.
7. **Include examples**: Provide examples of RST documentation and suggested improvements.


Usage example
-------------------------
```rst
How to handle data loading
=========================================================================================

Description
-------------------------
This section describes the correct way to load data using the provided functions.

Execution steps
-------------------------
1. Use `j_loads` or `j_loads_ns` from `src.utils.jjson` to load data from files.
2. Maintain any existing `...` placeholders in the code.

Usage example
-------------------------
.. code-block:: python

    from src.utils.jjson import j_loads

    data = j_loads("path/to/your/file.json")  # Example usage


```

```python
# Example function with RST documentation.
def example_function(param1: str, param2: int) -> str:
    """
    Executes a sample task.

    :param param1: Description of parameter 1.
    :param param2: Description of parameter 2.
    :return: Description of the returned value.
    """
    # ... (your code here)
    return "Example output"
```
```
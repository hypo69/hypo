How to generate Markdown documentation for Python code
=========================================================================================

Description
-------------------------
This document describes how to generate Markdown documentation for Python code blocks, including classes, functions, and methods, in a consistent format.  The generated documentation should include detailed descriptions, parameter information, return values, and exceptions.  It follows a structured format using Markdown headings and lists.

Execution steps
-------------------------
1. **Analyze the input Python code:** Carefully examine the code, identifying classes, functions, and methods.

2. **Generate documentation for each element:**
   - Use Markdown headings to create sections for Overview, Classes, Functions, etc.
   - Use `#`, `##`, `###`, etc. for appropriate heading levels.
   - Create a summary description for each class, function, and method.
   - Document parameters (name, type, description, default value if applicable).
   - Document return values (type, description).
   - Document exceptions (exception type, conditions under which it's raised, description).
   - Use bullet points for lists of parameters, return values, and exceptions.


3. **Example for functions:**

   ```markdown
   ## Functions

   ### `function_name`

   **Description**:  A concise description of the function.

   **Parameters**:
   - `param1` (str): A description of the `param1` parameter.
   - `param2` (int, optional): A description of the `param2` parameter. Defaults to 10.

   **Returns**:
   - `dict`: Returns a dictionary containing processed data.

   **Raises**:
   - `ValueError`: Raised if `param1` is not a valid string.
   - `TypeError`: Raised if input data types are incorrect.

   ```

4. **Example for classes:**

   ```markdown
   ## Classes

   ### `ClassName`

   **Description**:  A concise description of the class.

   **Methods**:
   - `method_name`: A concise description of the method.
   ```

5. **Formatting consistency:** Ensure consistent formatting throughout the documentation using correct Markdown syntax for headings, lists, and code blocks.

Usage example
-------------------------
.. code-block:: python

    # Example usage for generating documentation.
    # (This would be the input code to be processed.)

    def function_example(param1: str, param2: int = 10) -> dict:
        """
        Args:
            param1 (str): A description of the param1 parameter.
            param2 (int, optional): A description of the param2 parameter. Defaults to 10.

        Returns:
            dict: Returns a dictionary containing processed data.

        Raises:
            ValueError: Raised if param1 is not a valid string.
            TypeError: Raised if input data types are incorrect.
        """
        # Code implementation here
        return {"result": param1}

```
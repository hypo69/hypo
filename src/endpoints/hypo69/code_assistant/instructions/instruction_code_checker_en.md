
# INSTRUCTION
## Main Requirements:
## Output Language: EN (English)

1. **Documentation Format**:
   - Use **reStructuredText (RST)** for all comments and docstrings.
   - Always use single quotes (`'`) in Python code.

2. **Preserving Comments**:
   - All existing comments after `#` must be preserved without changes.
   - Code blocks that need to be modified must be commented line-by-line using the `#` symbol.

3. **Data Handling**:
   - Use `j_loads` or `j_loads_ns` from `src.utils.jjson` instead of the standard `json.load` for reading files.
   - Leave any `...` in the code unchanged as stopping points.

4. **Structure Analysis**:
   - Check and add missing imports in the code.
   - Align function, variable, and import names with previously processed files.

5. **Refactoring and Improvements**:
   - Add RST-style comments for all functions, methods, and classes.
   - Use `from src.logger import logger` for error logging.
   - Avoid excessive use of standard `try-except` blocks, preferring error handling with `logger.error`.

6. **Response Template**:
   - The response must include three sections:
     - **Received Code** — the original code without changes.
     - **Improved Code** — code with added comments and corrections.
     - **Changes Made** — a detailed list of modifications made.
   - The response must not start with ` ``` `. Use them only to wrap code blocks.

7. **Final Code**:
   - At the end of the response, include the complete code (original with improvements) in one block, ready to be copied and pasted to replace the original code.
   - All modified parts of the code must be commented line-by-line using the `#` symbol in this block.

8. **Code Examples**:
   - Include examples of RST documentation and possible improvements in `TODO` format.

9. **Additional Instruction**:
   - All comments for modules, functions, methods, and variables must be rewritten in reStructuredText (RST) format. This includes:
     - Module description at the beginning of the file.
     - Documentation for each function, method, and variable.
     - Compliance with Python docstring standards (e.g., for Sphinx).

     Example format for module documentation:

     ```python
     """
     Module for Programmer Assistant Functionality
     =========================================================================================

     This module contains the :class:`CodeAssistant` class, used to work with various AI models 
     such as Google Gemini and OpenAI, for performing code-processing tasks.

     Usage Example
     --------------------

     Example usage of the `CodeAssistant` class:

     .. code-block:: python

         assistant = CodeAssistant(role='code_checker', lang='en', model=['gemini'])
         assistant.process_files()
     """
     ```

     Example format for function documentation:

     ```python
     def example_function(param1: str, param2: int) -> str:
         """
         Performs an example task.

         :param param1: Description of parameter 1.
         :param param2: Description of parameter 2.
         :return: Description of the return value.
         """
         ...
     ```

## Response Sections:

1. **Received Code**:  
   <provided code>

2. **Improved Code**:  
   <code with improvements>

3. **Changes Made**:  
   <list of modifications>

4. **Final Optimized Code**:  
   <final optimized code>
----------------------------
** END OF INSTRUCTION **

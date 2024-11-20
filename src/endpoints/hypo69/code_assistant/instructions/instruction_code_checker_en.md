# INSTRUCTION
#### Main Requirements:

1. **Documentation Format**:
   - Use **reStructuredText (RST)** for all comments and docstrings.
   - Always use single quotes (`'`) in Python code.

2. **Preservation of Comments**:
   - All existing comments after `#` must be preserved unchanged.
   - Blocks of code that need to be modified should be commented line-by-line using the `#` symbol.

3. **Data Handling**:
   - Use `j_loads` or `j_loads_ns` from `src.utils.jjson` instead of the standard `json.load` for reading files.
   - Leave any `...` in the code unchanged as stopping points.

4. **Structure Analysis**:
   - Check for and add missing imports to the code.
   - Align function names, variables, and imports with previously processed files.

5. **Refactoring and Enhancements**:
   - Add RST comments to all functions, methods, and classes.
   - Use `from src.logger import logger` for error logging.
   - Avoid excessive use of standard `try-except` blocks, preferring error handling with `logger.error`.

6. **Response Template**:
   - The response should include three sections:
     - **Received Code** — the original code without changes.
     - **Improved Code** — the code with added comments and fixes.
     - **Changes Made** — a detailed list of the changes made.
   - The response should not begin with ` ``` `. Use them only for wrapping code blocks.

7. **Final Code Output**:
   - At the end of the response, include the complete code (original with improvements) in a single block that can be copied and pasted to replace the original code.
   - Any part of the code that has been changed must be commented line-by-line with the `#` symbol in this block.

8. **Code Examples**:
   - Include examples of RST documentation and possible improvements in `TODO` format.

# Output Language: EN (English)
----------------------------
** END OF INSTRUCTION ** 

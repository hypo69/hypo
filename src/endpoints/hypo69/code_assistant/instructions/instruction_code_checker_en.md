# INSTRUCTION 
#### Main Requirements:

1. **Documentation Format**:
   - Use **reStructuredText (RST)** for all comments and docstrings.
   - Always use single quotes (`'`) in Python code.
   
2. **Comment Preservation**:
   - Preserve all existing comments after `#` without any changes.

3. **Data Handling**:
   - Use `j_loads` or `j_loads_ns` from `src.utils.jjson` for file reading instead of the standard `json.load`.
   - If the code contains `...`, leave them unchanged as stop points.

4. **Structure Analysis**:
   - Check and add missing imports in the code.
   - Align function, variable, and import names with previously processed files.

5. **Refactoring and Improvements**:
   - Add RST-style comments to all functions, methods, and classes.
   - Use `from src.logger import logger` for error logging.
   - Avoid excessive use of standard `try-except` blocks, preferring error handling with `logger.error`.

6. **Response Template**:
   - The response must include three sections:
     - **Received Code** — the original code without any modifications.
     - **Improved Code** — the code with added comments and fixes.
     - **Changes Made** — a detailed list of the changes made.

7. **Code Examples**:
   - Include examples of RST documentation and possible improvements in the `TODO` format.

# Output Language: EN (English)
----------------------------
** END OF INSTRUCTION ** 
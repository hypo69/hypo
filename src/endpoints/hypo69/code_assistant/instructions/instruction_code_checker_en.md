### INSTRUCTION

#### Main Requirements:
1. **Documentation Format**:
   - Use **reStructuredText (RST)** for all comments and docstrings.
   - Always use single quotes (`'`) in Python code.

2. **Preserving Comments**:
   - All existing comments after `#` must be preserved without any changes.

3. **Data Handling**:
   - For file reading, use `j_loads` or `j_loads_ns` from `src.utils.jjson` instead of the standard `json.load`.
   - If the code contains `...`, leave them unchanged as stop points.

4. **Structure Analysis**:
   - Check and add missing imports in the code.
   - Ensure consistency in function names, variable names, and imports with previously processed files.

5. **Refactoring and Improvements**:
   - Add RST comments to all functions, methods, and classes.
   - Use `logger.error` for error logging, avoiding standard `try-except` blocks.

6. **Response Template**:
   - The response should consist of three sections:
     - **Received Code** — the original code without any changes.
     - **Improved Code** — code with added comments and corrections.
     - **Changes Made** — a detailed list of all changes made.

7. **Code Examples**:
   - Include examples of RST documentation and potential improvements in the `TODO` format.

----------------------------
**END OF INSTRUCTION**
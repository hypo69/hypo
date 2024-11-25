```
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


## Response Sections:

1. **Received Code**:  
   ```
   ``` (No code provided in the prompt)

2. **Improved Code**:  
   ```
   ``` (No code provided to improve)


3. **Changes Made**:  
   ```
   ``` (No changes to apply)

4. **Final Optimized Code**:  
   ```
   ``` (No code to include)


```

**Explanation and Next Steps:**

The provided input does not contain any code to process.  To get a response, please provide the code snippet you want checked and improved.  I will then follow the instructions from the prompt to produce a revised code block, along with the modifications made.
# INSTRUCTION  
## Main Requirements:  
## Output Language: EN (English)  

1. **Documentation Format**:  
   - Use **reStructuredText (RST)** for all comments and docstrings.  
   - Always use single quotes (`'`) in Python code.  

2. **Comment Preservation**:  
   - All existing comments after the `#` symbol must be preserved without changes.  
   - Code blocks requiring changes must be commented line by line using the `#` symbol.  

3. **Data Handling**:  
   - Use `j_loads` or `j_loads_ns` from `src.utils.jjson` instead of the standard `json.load` for file reading.  
   - Leave any `...` in the code unchanged as stop points.  

4. **Structure Analysis**:  
   - Verify and add missing imports in the code.  
   - Ensure function, variable, and import names align with previously processed files.  

5. **Refactoring and Enhancements**:  
   - Add RST-format comments to all functions, methods, and classes.  
   - Use `from src.logger import logger` for error logging.  
   - Avoid overusing standard `try-except` blocks; prefer error handling using `logger.error`.  
   - In comments, avoid vague words like 'get' or 'do'. Instead, use specific terms such as 'validation', 'execution', or 'sending'.  

6. **Response Template**:  
   - The response must include three sections:  
     - **Received Code** — the original code without changes.  
     - **Improved Code** — the code with added comments and fixes.  
     - **Changes Made** — a detailed list of the changes made.  
     - **FULL Code** — the full code with all improvements.  
   - The response should not begin with ` ``` `. Use these only to enclose code blocks.  

7. **Final Code**:  
   - The final section of the response must present the full code (original code with improvements) in a single block, ready to be copied and pasted as a replacement for the original code.  
   - All modified parts of the code should be commented line by line using the `#` symbol in this block.  

8. **Code Examples**:  
   - Include examples of RST documentation and potential improvements in `TODO` format.  

9. **Additional Instruction**:  
   - Rewrite all comments for modules, functions, methods, and variables in RST format. This includes:  
     - A description of the module at the beginning of the file.  
     - Documentation for each function, method, and variable.  
     - Adherence to Python docstring standards (e.g., Sphinx-style).  
     - Lines commented with `#` must provide a detailed explanation of the block of code they precede.  

     Example module documentation format:  

     ```python  
     """  
     Module for programmer assistant functionality  
     =========================================================================================  

     This module contains the :class:`CodeAssistant`, which works with various AI models,  
     such as Google Gemini and OpenAI, to handle code processing tasks.  

     Example Usage  
     --------------------  

     Example of using the `CodeAssistant` class:  

     .. code-block:: python  

         assistant = CodeAssistant(role='code_checker', lang='en', model=['gemini'])  
         assistant.process_files()  
     """  
     ```  

     Example function documentation format:  

     ```python  
     def example_function(param1: str, param2: int) -> str:  
         """  
         Performs a sample task.  

         :param param1: Description of parameter 1.  
         :param param2: Description of parameter 2.  
         :return: Description of the return value.  
         """  
         ...  
     ```  

     Example comment style in code:  

     ```python  
     @close_pop_up()  
     async def specification(self, value: Any = None):  
         """Fetch and set specification.  

         Args:  
             value (Any): This value can be passed in the kwargs dictionary under the key `{specification = value}`  
             when defining the class. If `value` is provided, its value is set in the `ProductFields.specification` field.  
         """  
         try:  
             # Code executes value retrieval using execute_locator  
             value = value or await self.d.execute_locator(self.l.specification) or ''  
         except Exception as ex:  
             logger.error('Error retrieving value for the `specification` field', ex)  
             ...  
             return  

         # Validation of the retrieved result  
         if not value:  
             logger.debug(f'Invalid result {value=}\nLocator {self.l.specification}')  
             ...  
             return  

         # If the value is a list, the code converts it into a string separated by `\n`  
         if isinstance(value, list):  
             value = '\n'.join(map(str, value))  

         # Code writes the result into the `specification` field of the `ProductFields` object  
         self.fields.specification = value  
         return True  
     ```  

## Response Block Order:  

1. **Original Code**:  
   <provided code>  

2. **Improved Code**:  
   <code with improvements>  

3. **Changes Made**:  
   <list of changes>  

4. **Optimized Code**:  
   <final optimized code>  

## You respond in English
## Responding format: `.md` (markdown)
----------------------------  
** END OF INSTRUCTION **  